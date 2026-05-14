---
title: "Building an AI-native multi-model UI with SurrealDB"
slug: "building-an-ai-native-multi-model-ui-with-surrealdb"
date: "2025-07-29T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
  - "ai"
read_time: "11 min read"
summary: "Schema definition in SurrealDB is a powerful thing, and the more you know the more you can make your schema work for you."
source: "https://surrealdb.com/blog/building-an-ai-native-multi-model-ui-with-surrealdb"
cover: "../../assets/59ad767c9fc8154f.jpg"
---

# Building an AI-native multi-model UI with SurrealDB

![Building an AI-native multi-model UI with SurrealDB](../../assets/59ad767c9fc8154f.jpg)

While many products refer to themselves as AI databases or vector databases, we tend to use the term "AI-native" for SurrealDB. That's because SurrealDB at its core is a multi-model general purpose database that just happens to have been built from the ground up with features purpose fit for generative AI such as vector similarity and indexing, graph and record links, and use as an embedded data store.

It's no exaggeration to say that AI has taken the world by storm. This is one that we have welcomed as it has been the perfect opportunity to showcase how SurrealDB's features let you build apps using generative AI without needing anything but a running SurrealDB database and nothing extra to download or bolt on to make it happen.

As such, many of our recent blog posts have showcased SurrealDB's uses in AI applications, such as the official [SurrealDB LangChain integration](/blog/announcing-our-official-langchain-integration), [semantic search wih SurrealDB and OpenAI](/blog/semantic-search-with-surrealdb-and-openai) (and [another one](/blog/semantic-search-in-rust-with-surrealdb-and-mistral-ai) using Mistral), and [building a smart knowledge agent with SurrealDB and Rig.rs](/blog/rag-can-be-rigged).

This post goes a good ways beyond a minimal example to show just how easy it is to get all this and more. Since SurrealDB is a multi-model database that just happens to be AI-native, AI solutions can be combined or used alongside all of SurrealDB's features such as full-text search, recursive queries, and embedding as an in-memory database.

To demonstrate this, we will create a demo UI using Rust and the [Iced crate](https://iced.rs/) which is one of the nicest ways to build a UI in Rust ([egui](https://github.com/emilk/egui) is another one, which I tend to use more frequently but Iced has a bit more of a webpage feel which is nice).

This UI will have a few buttons to let you do a few things.

The first button lets you insert documents into the database that are taken from Wikipedia's summary API. You can see an example of the output [here](https://en.wikipedia.org/api/rest_v1/page/summary/calgary), from which we will use the `title` and `extract` fields:

```json
{
  "title": "Calgary",
  "extract": "Calgary is a major city in the Canadian province of Alberta. As of 2021, the city proper had a population of 1,306,784 and a metropolitan population of 1,481,806 making it the third-largest city and fifth-largest metropolitan area in Canada."
}
```

The other buttons on the UI will do the following:

- Manually link two documents together via their titles.
- Look through the `extract` for capitalized words, check if there is an article with a matching title and link the articles together if that is the case. In the example above, it would link `Calgary` to `Alberta` and `Canada` if the database had all three of these documents.
- Add OpenAI embeddings.
- Add Mistral embeddings.
- Perform OpenAI similarity search for a document.
- Perform Mistral similarity search for a document.
- Perform full-text search on the documents in the database.
- See all the links for a document by performing a recursive query to a depth of 3.
- See all document titles.
- Run raw queries (since an embedded database won't have an endpoint for you to connect via Surrealist or the CLI).

I must admit to having had a bit too much fun putting this together, and it was difficult to tell myself to stop building and refactoring the app and get around to writing about it. This is probably a blessing in disguise, as it leaves it with the potential for other features that you might want to pick up yourself to further develop the app as you see fit.

Here is what the end product will look like once it is run:

![](../../assets/42bcfa79144b1353.mp4)

## SurrealQL statements when setting up

The SurrealQL code begins with some statements to set up the namespace and database, along with the fields for the `document` table. Documents are first added by calling into Wikipedia and taking the text at the `extract` and `title` fields. The arrays for embeddings will be empty by default so that you can experiment with adding and querying articles without needing to call in to OpenAI or Mistral for embeddings.

```surrealql
DEFINE NAMESPACE ns;
DEFINE DATABASE db;
USE NS ns;
USE DB db;
DEFINE FIELD extract ON document TYPE string;
DEFINE FIELD title ON document TYPE string;
DEFINE FIELD mistral_embedding ON document TYPE option<array<float>> DEFAULT [];
DEFINE FIELD openai_embedding ON document TYPE option<array<float>> DEFAULT [];
```

After that we have some statements to set up full-text search. The `en_analyzer` search analyzer will break up any input string by class (i.e. the input `"Hi!123"` would become `['Hi', '!', '123']`), then change each token to lowercase, and then build an edgengram over everything from 3 to 10 characters in length.

```surrealql
DEFINE ANALYZER en_analyzer TOKENIZERS class FILTERS lowercase,edgengram(4,10);
```

The name `en_analyzer` is a hint that you could expand the app into other languages if you wanted. For example, you could set up another analyzer that works with French through this sort of analyzer definition.

```surrealql
DEFINE ANALYZER fr_analyzer TOKENIZERS class FILTERS lowercase,snowball(french);
```

A search analyzer is easy to test out by using the `search::analyze()` function. Let's give it a try!

```surrealql
DEFINE ANALYZER en_analyzer TOKENIZERS class FILTERS lowercase,edgengram(3,10);
search::analyze("en_analyzer", "I run really fast");

-- Output:
[
	'run',
	'rea',
	'real',
	'reall',
	'really',
	'fas',
	'fast'
]
```

An edgengram works best when an app is watching user keypresses in real time. This is one of the features that was not yet added to the app, but you can continue the feature [here](https://docs.rs/iced/latest/iced/keyboard/index.html) if you like.

Once a search analyzer has been made, it will need an index to use the `@@` operator (the [MATCHES](/docs/surrealql/operators#matches) operator). These include `BM25` which will allow us to see not just matches, but the score so that results can be sorted by best match. (Fun fact: I originally assumed that the BM in BM25 was a fancy algorithm name like "Biedermann-Mendelstein" but it just stands for "Best Match")

The statement also has a `HIGHLIGHTS` clause which lets us highlight any matching text to make it easy to find when looking at the results of a full-text search.

```surrealql
DEFINE INDEX en_extract ON document FIELDS extract SEARCH ANALYZER en_analyzer BM25 HIGHLIGHTS;
DEFINE INDEX en_title ON document FIELDS title SEARCH ANALYZER en_analyzer BM25 HIGHLIGHTS;
```

Finally, we have two statements that relate to the linking of documents.

The first is a table definition that sets a relation (that we will just call `link` for lack of imagination) that must be `ENFORCED`. This clause will make sure that a `RELATE` statement fails if the two documents to be related don't exist yet.

```surrealql
DEFINE TABLE link TYPE RELATION IN document OUT document ENFORCED;
```

(By the way, being able to relate documents that don't exist yet is a feature that is nice to have. This flexibility allows for patterns such as using graph queries as assertions, as [this example shows](/blog/ten-tips-and-tricks-for-your-database-schema#10-use-graph-queries-in-the-schema))

Our app will mindlessly try to `RELATE` one document to another if it finds a matching word in the summary, so we will add a `UNIQUE` index to ensure that no two documents can be related to one another more than once. This is the easiest way to let the schema do the thinking for us.

```surrealql
DEFINE INDEX only_one_link ON link FIELDS in,out UNIQUE;
```

Following these `DEFINE` statements are a number of queries used throughout the app to accomplish the behaviour returned from the various buttons on the app.

## SurrealQL statements used when running the app

After these first definitions come a number of other SurrealQL statements used during the running of the app. Here they are in the same order that the buttons were introduced above.

### Adding new documents

This one is pretty simple. Note the `ONLY` keyword which will return a single record instead of an array of records.

```surrealql
CREATE ONLY $doc SET title = $title, extract = $extract;
```

### Manually linking documents

The logic here is also straightforward since we are going to create `document` records that have an ID made up of the article name. For example, `document:Germany` or `document:Solar_System`. Since record IDs must be unique, no article with the same name can be created twice. This is a good pattern to use if you know ahead of time what a record ID is going to be, as `SELECT * FROM document:Germany` (or even just `document:Germany.*`) will always be faster than `SELECT * FROM document WHERE title = "Germany"`.

After that, a quick `RELATE` statement is all that is needed. Here is the part of the SDK code that contains the statement.

```surrealql
let one = RecordId::from_table_key("document", one);
let two = RecordId::from_table_key("document", two);
match self
    .db
    .query("RELATE $one->link->$two;")
    .bind(("one", one))
    .bind(("two", two)) // Then handle the result...
```

### Automatically linking documents

This is the part in which we can click a single button to look through an article's extract for capitalized words, and see if there are any matching articles. This part of the query does nothing but grab each article.

```rust
let mut response = match self.db.query("SELECT * FROM document").await {
    Ok(response) => response,
    Err(e) => return e.to_string(),
};
```

Later on you might want to add another button that only looks at documents without an outbound link via the `WHERE !->link->document` clause.

```surrealql
SELECT * FROM document WHERE !->link->document
```

But we don't want to use this as default behaviour because that would mean that `document:Earth` linked to `document:Moon` wouldn't be linked to a document called `document:Sun` that we add later, even if the text in the Earth article included a mention of the Sun.

### Adding embeddings

These embeddings are created by calling into either OpenAI or Mistral. This requires a key for both. If the key does not exist then the client will receive "NONE" as its key and an error will be returned that is turned into a `String` so that the program does not panic. Most of the rest of the Rust code will return `Result<String, String>` by mapping all possible errors to a `String` and returning that, so that the program can display any errors instead of shutting down if they happen.

```rust
static OPENAI_API_KEY: LazyLock<String> =
    LazyLock::new(|| std::env::var("OPENAI_API_KEY").unwrap_or("NONE".to_string()));

static MISTRAL_API_KEY: LazyLock<String> =
    LazyLock::new(|| std::env::var("MISTRAL_API_KEY").unwrap_or("NONE".to_string()));
```

When a user clicks on the button to add embeddings, the database will use one of these two queries to find any documents that don't have embeddings yet.

```surrealql
SELECT title, extract FROM document WHERE !openai_embedding;
SELECT title, extract FROM document WHERE !mistral_embedding;
```

These can be turned into a Rust struct that holds a `title` and `extract`. Serde's `Deserialise` trait will do the job.

```rust
#[derive(Deserialize, Debug, Clone)]
struct PageContent {
    title: String,
    extract: String,
}
```

Then the OpenAI or Mistral client will call in using the key provided to return a `Vec<f32>`, which we can add to the document in question with an `UPDATE` statement.

```surrealql
UPDATE type::thing('document', $title) SET openai_embedding = $embeds;
```

### Querying embeddings

OpenAI and Mistral embeddings: these are done via the following two queries. A query is first made to the database to get the record for an article's name. Since we know what an article's record ID must be, we can construct it using the [`type::thing()`](/docs/surrealql/functions/database/type#typething) function which directly creates a record pointer.

The `field_name` part in this case is the name of the field with the embeddings, either `openai_embedding` or `mistral_embedding`.

```surrealql
db.query(format!("type::thing('document', '{doc}').{field_name};"))
```

This will return a large vector of floats which we will give the name `embeds` to. It can then be passed into this function that goes through each of the `document` records, finds the four closest neighbours, and sorts them by distance.

```surrealql
(SELECT 
    (extract.slice(0, 50) + '...') AS extract,
    title,
    vector::distance::knn() AS distance
        FROM document
        WHERE {field_name} <|4,COSINE|> $embeds
        ORDER BY distance).filter(|$t| $t.distance > 0.0001);
```

Some notes on this query:

- The `extract.slice` part is used to only show the first 50 characters of an extract. This can be changed to `extract` to show the entire field.
- The `vector::distance::knn()` function returns the nearest neighbours, based on the following `WHERE` clause. Here, `<|4,COSINE|>` will use the cosine distance to return the closest four results, while the vector function will allow us to see the distance so that we can sort by closest match. For more details on how vector searching works, see [the reference guide](/docs/surrealdb/models/vector).
- `.filter` at the end is used to filter out any results that have a distance effectively equal to zero. This will filter out the article itself, because we don't want to see the article for `document:Sun` as the closest neighbour to the same `document:Sun`.

### Using full-text search

The full-text search query is one of the most interesting ones used in this app. Its basic structure is `SELECT <fields> FROM document WHERE title @0@ $input OR extract @1@ $input`. While the default matches operator is `@@`, a number needs to be passed in if we want to use any of the search functions like `search::highlight` or `search::score`, so that it knows which match to calculate from.

```surrealql
SELECT 
    search::highlight('**', '**', 0) AS title, 
    search::highlight('**', '**', 1) AS extract,
(search::score(0) * 3) + search::score(1) AS score
FROM document
WHERE title @0@ $input OR extract @1@ $input
ORDER BY score DESC;
```

For example, to calculate the score we can make a match on `title` more relevant than a match inside `extract` by multiplying the score by a certain amount (3 should be fine).

So when the database sees `(search::score(0) * 3) + search::score(1) AS score`, it will know that `search::score(0)` means the score of the match on `title` because `WHERE title @0@ $input` has a 0 in the matches operator.

We can test this out by entering a few articles on Greek gods:

```syntax
Zeus,Hera,Poseidon,Hades,Athena,Apollo,Artemis,Ares,Aphrodite,Hephaestus,Hermes,Hestia,Dionysus,Demeter,Persephone
```

A search for "Zeus" will then turn up the article on Zeus first with a score of 12.7, followed by Hephaestus way back in second place with a score of just 1.5 because of a few mentions of Zeus in his article's summary.

### Recursive link querying

This recursive query is surprisingly simple thanks to the magic of recursive graph queries. It is composed of the record ID, `.{..3}` to tell the database to go down to a depth of 3, and then an output structure that looks like `.{ id, next: ->link->document.@ }`. The final `.@` lets the database know that this is the path to keep following recursively, while other fields like `id` come along for the ride.

```surrealql
type::thing('document', '{doc}').{..3}.{ id, next: ->link->document.@ }
```

If we select the "Link unlinked docs" button and then type "Hades" and click on "See linked articles", we should see that Hades is connected to Poseidon, who is connected to Persephone, who herself is connected to both Demeter, Hades, and Zeus, and so on. This is thanks to the mention of all these gods in her summary:

"...is the daugher of Zeus and Demeter. She became the queen of the underworld after her abduction by her uncle Hades..."

### Viewing all document titles

This query is as simple as a query gets: just the `title` fields, sorted.

```surrealql
(SELECT VALUE title FROM document).sort()
```

## Final code

Want to give the code a try? Here it is along with the `Cargo.toml` dependencies.

```rust
// Cargo.toml dependencies
// 
// anyhow = "1.0.97"
// async-openai = "0.28.3"
// iced = {version = "0.13.1", features = ["advanced", "image"] }
// mistralai-client = "0.14.0"
// serde = "1.0.219"
// serde_json = "1.0.140"
// surrealdb = { version = "2.2.1", features = ["kv-mem"] }
// tokio = "1.44.0"
// ureq = "3.0.12"

use std::fmt::Display;
use std::sync::{Arc, LazyLock};

use async_openai::Client as OpenAiClient;
use async_openai::config::OpenAIConfig;
use async_openai::types::CreateEmbeddingRequestArgs;
use iced::theme::{Custom, Palette};
use iced::widget::{button, row, scrollable, text_editor, text_input};
use mistralai_client::v1::client::Client as MistralClient;
use serde::Deserialize;
use surrealdb::engine::any::{Any, connect};
use surrealdb::{RecordId, Surreal, Value};

use iced::widget::{column, text};
use iced::{Center, Element, Theme, color};
use tokio::runtime::Runtime;

use mistralai_client::v1::constants::EmbedModel::MistralEmbed;

static OPENAI_API_KEY: LazyLock<String> =
    LazyLock::new(|| std::env::var("OPENAI_API_KEY").unwrap_or("NONE".to_string()));

static MISTRAL_API_KEY: LazyLock<String> =
    LazyLock::new(|| std::env::var("MISTRAL_API_KEY").unwrap_or("NONE".to_string()));

static OPENAI_CLIENT: LazyLock<OpenAiClient<OpenAIConfig>> = LazyLock::new(|| {
    let config = OpenAIConfig::new().with_api_key(&*OPENAI_API_KEY);
    OpenAiClient::with_config(config)
});

static MISTRAL_CLIENT: LazyLock<MistralClient> =
    LazyLock::new(|| MistralClient::new(Some(MISTRAL_API_KEY.clone()), None, None, None).unwrap());

trait StringOutput {
    fn output(self) -> String;
}

impl StringOutput for Result<String, String> {
    fn output(self) -> String {
        match self {
            Ok(o) => o,
            Err(e) => e,
        }
    }
}

#[derive(Deserialize, Debug, Clone)]
struct PageContent {
    title: String,
    extract: String,
}

fn page_for(page: &str) -> String {
    format!("http://en.wikipedia.org/api/rest_v1/page/summary/{page}")
}

fn init() -> &'static str {
    r#"
    DEFINE NAMESPACE ns;
    DEFINE DATABASE db;
    USE NS ns;
    USE DB db;
    DEFINE FIELD extract ON document TYPE string;
    DEFINE FIELD title ON document TYPE string;
    DEFINE FIELD mistral_embedding ON document TYPE option<array<float>> DEFAULT [];
    DEFINE FIELD openai_embedding ON document TYPE option<array<float>> DEFAULT [];
    DEFINE ANALYZER en_analyzer TOKENIZERS class FILTERS lowercase,edgengram(3,10);
    DEFINE INDEX en_extract ON document FIELDS extract SEARCH ANALYZER en_analyzer BM25 HIGHLIGHTS;
    DEFINE INDEX en_title ON document FIELDS title SEARCH ANALYZER en_analyzer BM25 HIGHLIGHTS;

    DEFINE TABLE link TYPE RELATION IN document OUT document ENFORCED;

    DEFINE INDEX only_one_link ON link FIELDS in,out UNIQUE;"#
}

struct App {
    rt: Option<Runtime>,
    db: Surreal<Any>,
    app_output: String,
    query_content: text_editor::Content,
    document_content: text_editor::Content,
    link_content: text_editor::Content,
    openai_doc_search: text_editor::Content,
    mistral_doc_search: text_editor::Content,
    fts_text: text_editor::Content,
    seelinks_text: text_editor::Content,
}

impl Default for App {
    fn default() -> Self {
        let rt = tokio::runtime::Builder::new_current_thread()
            .enable_all()
            .build()
            .unwrap();

        let db = rt.block_on(async {
            let db = connect("memory").await.unwrap();
            db.use_db("db").await.unwrap();
            db.use_ns("ns").await.unwrap();
            db.query(init()).await.unwrap();
            db
        });

        Self {
            rt: Some(rt),
            db,
            app_output: Default::default(),
            query_content: Default::default(),
            document_content: Default::default(),
            link_content: Default::default(),
            openai_doc_search: Default::default(),
            fts_text: Default::default(),
            mistral_doc_search: Default::default(),
            seelinks_text: Default::default(),
        }
    }
}

#[derive(Debug, Clone)]
enum Message {
    Query,
    QueryContent(text_editor::Action),
    InsertDocuments,
    InsertDocumentsContent(text_editor::Action),
    LinkDocuments,
    LinkDocumentsContent(text_editor::Action),
    OpenAiSimilaritySearch,
    OpenAiSimilaritySearchContent(text_editor::Action),
    MistralSimilaritySearch,
    MistralSimilaritySearchContent(text_editor::Action),
    Fts,
    FtsContent(text_editor::Action),
    TryLink,
    SeeDocs,
    SeeLinks,
    SeeLinksContent(text_editor::Action),
    AddOpenAi,
    AddMistral,
}

async fn get_openai_embeddings(content: Vec<PageContent>) -> Result<Vec<Vec<f32>>, String> {
    let extracts = content
        .into_iter()
        .map(|v| v.extract)
        .collect::<Vec<String>>();
    // Get the OpenAI embeddings
    let request = CreateEmbeddingRequestArgs::default()
        .model("text-embedding-3-small")
        .input(extracts)
        .dimensions(1536u32)
        .build()
        .map_err(|e| e.to_string())?;
    match OPENAI_CLIENT.embeddings().create(request).await {
        Ok(res) => Ok(res
            .data
            .into_iter()
            .map(|v| v.embedding)
            .collect::<Vec<Vec<f32>>>()),
        Err(e) => Err(e.to_string()),
    }
}

async fn get_mistral_embeddings(content: Vec<PageContent>) -> Result<Vec<Vec<f32>>, String> {
    let extracts = content
        .into_iter()
        .map(|v| v.extract)
        .collect::<Vec<String>>();
    // Get the Mistral embeddings
    match MISTRAL_CLIENT
        .embeddings_async(MistralEmbed, extracts, None)
        .await
    {
        Ok(res) => Ok(res
            .data
            .into_iter()
            .map(|d| d.embedding)
            .collect::<Vec<Vec<f32>>>()),
        Err(e) => Err(e.to_string()),
    }
}

fn get_possible_links(title: &str, content: &str) -> Vec<String> {
    content
        .split_whitespace()
        .filter(|word| matches!(word.chars().next(), Some(c) if c.is_uppercase()))
        .filter_map(|word| {
            let only_alpha = word
                .chars()
                .filter(|c| c.is_alphabetic())
                .collect::<String>();
            // Keep long words
            if only_alpha.chars().count() >= 3 && only_alpha != title {
                Some(only_alpha)
            } else {
                None
            }
        })
        //.flatten()
        .collect::<Vec<String>>()
}

#[derive(Deserialize, Debug)]
struct LinkOutput {
    r#in: RecordId,
    out: RecordId,
}

impl Display for LinkOutput {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "in: {} out: {}", self.r#in.key(), self.out.key())
    }
}

impl App {
    async fn try_to_link(&self) -> Result<String, String> {
        let mut response = self
            .db
            .query("SELECT * FROM document")
            .await
            .map_err(|e| e.to_string())?;
        let unlinked_docs = response
            .take::<Vec<PageContent>>(0)
            .map_err(|e| format!("{e:?}"))?;
        let mut output = String::from("Docs linked: ");
        for doc in unlinked_docs {
            let possible_links = get_possible_links(&doc.title, &doc.extract);
            for link in possible_links {
                let first = RecordId::from(("document", &doc.title));
                let second = RecordId::from(("document", &link));
                if let Ok(mut o) = self
                    .db
                    .query("RELATE $first->link->$second")
                    .bind(("first", first))
                    .bind(("second", second))
                    .await
                {
                    if let Ok(Some(o)) = &o.take::<Option<LinkOutput>>(0) {
                        output += "\n";
                        output += &o.to_string();
                    }
                }
            }
        }
        Ok(output)
    }

    async fn ai_similarity_search(
        &self,
        doc: String,
        field_name: String,
    ) -> Result<Value, surrealdb::Error> {
        let doc = doc.trim().to_owned();
        let field_name = field_name.trim().to_owned();

        let mut current_doc = self
            .db
            // Grab just the embeds field from a document
            .query(format!("type::thing('document', '{doc}').{field_name};"))
            .await?;
        let embeds: Value = current_doc.take(0)?;

        let mut similar = self
            .db
            .query(format!(
                "(SELECT 
    (extract.slice(0, 50) + '...') AS extract,
    title,
    vector::distance::knn() AS distance
        FROM document
        WHERE {field_name} <|4,COSINE|> $embeds
        ORDER BY distance).filter(|$t| $t.distance > 0.0001);",
            ))
            .bind(("embeds", embeds))
            .await?;
        similar.take::<Value>(0)
    }

    async fn add_openai(&self) -> Result<String, String> {
        let no_open_id: Vec<PageContent> = self
            .db
            .query("SELECT title, extract FROM document WHERE !openai_embedding")
            .await
            .map_err(|e| e.to_string())?
            .take(0)
            .map_err(|e| e.to_string())?;
        if !no_open_id.is_empty() {
            let embeddings = get_openai_embeddings(no_open_id.clone())
                .await
                .map_err(|e| e.to_string())?;
            let zipped = no_open_id.into_iter().zip(embeddings.into_iter());

            let mut results = String::from("Embeddings added for:");
            for (one, two) in zipped {
                let mut res = self
                    .db
                    .query(
                        "UPDATE type::thing('document', $title)
            SET openai_embedding = $embeds",
                    )
                    .bind(("title", one.title))
                    .bind(("embeds", two))
                    .await
                    .map_err(|e| e.to_string())?;
                if let Ok(Some(v)) = res.take::<Option<PageContent>>(0) {
                    results.push('\n');
                    results.push_str(&v.title);
                }
            }
            Ok(results)
        } else {
            Err(String::from("No documents found to update"))
        }
    }

    async fn add_mistral(&self) -> Result<String, String> {
        let no_mistral_id: Vec<PageContent> = self
            .db
            .query("SELECT title, extract FROM document WHERE !mistral_embedding")
            .await
            .map_err(|e| e.to_string())?
            .take(0)
            .map_err(|e| e.to_string())?;
        if !no_mistral_id.is_empty() {
            let embeddings = get_mistral_embeddings(no_mistral_id.clone())
                .await
                .map_err(|e| e.to_string())?;
            let zipped = no_mistral_id.into_iter().zip(embeddings.into_iter());

            let mut results = String::from("Embeddings added for:");
            for (one, two) in zipped {
                let mut res = self
                    .db
                    .query(
                        "UPDATE type::thing('document', $title)
            SET mistral_embedding = $embeds",
                    )
                    .bind(("title", one.title))
                    .bind(("embeds", two))
                    .await
                    .map_err(|e| e.to_string())?;
                match res.take::<Option<PageContent>>(0) {
                    Ok(Some(v)) => {
                        results.push('\n');
                        results.push_str(&v.title);
                    }
                    Ok(None) => return Err("No PageContent found".to_string()),
                    Err(e) => return Ok(e.to_string()),
                }
            }
            Ok(results)
        } else {
            Err(String::from("No documents found to update"))
        }
    }

    async fn insert_documents(&self, page_names: String) -> Result<String, String> {
        // Get each page name separated by a comma and add _ in between words
        let page_names = page_names
            .trim()
            .split(",")
            .map(|p| p.split_whitespace().collect::<Vec<&str>>().join("_"));
        let mut result = String::new();

        let results = page_names
            .map(|page| {
                std::thread::spawn(move || {
                    let url = page_for(&page);
                    let res = ureq::get(url).call();
                    match res {
                        Ok(mut o) => o.body_mut().read_to_string().unwrap(),
                        Err(_) => format!("No page {page} found"),
                    }
                })
            })
            .collect::<Vec<_>>();

        for res in results {
            let s = res.join().unwrap();
            let mut content: PageContent = match serde_json::from_str(&s) {
                Ok(content) => content,
                Err(_) => return Err(s),
            };
            // Add an underscore again as response from Wikipedia won't have it
            content.title = content
                .title
                .split_whitespace()
                .collect::<Vec<&str>>()
                .join("_");
            result.push('\n');
            result.push_str(&self.add_document(content).await);
        }
        Ok(result)
    }

    async fn add_document(&self, content: PageContent) -> String {
        let doc = RecordId::from_table_key("document", &content.title);

        let res = self
            .db
            .query("CREATE ONLY $doc SET title = $title, extract = $extract;")
            .bind(("doc", doc))
            .bind(("title", content.title))
            .bind(("extract", content.extract));
        match res.await {
            Ok(mut r) => match r.take::<Option<PageContent>>(0) {
                Ok(Some(good)) => format!("{good:?}"),
                Ok(None) => "No PageContent found".to_string(),
                Err(e) => e.to_string(),
            },
            Err(e) => e.to_string(),
        }
    }

    fn update(&mut self, message: Message) {
        use Message as M;

        let rt = self.rt.take().unwrap();

        rt.block_on(async {
            match message {
                M::Query => self.app_output = self.raw_query(&self.query_content.text()).await,
                M::InsertDocuments => {
                    let content = self
                        .insert_documents(self.document_content.text())
                        .await
                        .output();

                    self.app_output = format!("Add article result: {content}");
                }
                M::LinkDocuments => {
                    self.app_output = self.link_documents(self.link_content.text()).await
                }

                M::OpenAiSimilaritySearch => {
                    self.app_output = match self
                        .ai_similarity_search(
                            self.openai_doc_search.text(),
                            "openai_embedding".to_string(),
                        )
                        .await
                    {
                        Ok(o) => o.to_string(),
                        Err(e) => e.to_string(),
                    }
                }
                M::MistralSimilaritySearch => {
                    self.app_output = match self
                        .ai_similarity_search(
                            self.mistral_doc_search.text(),
                            "mistral_embedding".to_string(),
                        )
                        .await
                    {
                        Ok(o) => o.to_string(),
                        Err(e) => e.to_string(),
                    }
                }
                M::TryLink => self.app_output = self.try_to_link().await.output(),
                M::Fts => self.app_output = self.fts_search(self.fts_text.text()).await.output(),
                M::SeeDocs => self.app_output = self.see_docs().await,
                M::SeeLinks => self.app_output = self.linked_docs(self.seelinks_text.text()).await,
                M::AddOpenAi => self.app_output = self.add_openai().await.output(),
                M::AddMistral => self.app_output = self.add_mistral().await.output(),
                // Text windows
                M::QueryContent(action) => self.query_content.perform(action),
                M::InsertDocumentsContent(action) => self.document_content.perform(action),
                M::LinkDocumentsContent(action) => self.link_content.perform(action),
                M::OpenAiSimilaritySearchContent(action) => self.openai_doc_search.perform(action),
                M::MistralSimilaritySearchContent(action) => {
                    self.mistral_doc_search.perform(action)
                }
                M::FtsContent(action) => self.fts_text.perform(action),
                M::SeeLinksContent(action) => self.seelinks_text.perform(action),
            }
        });

        self.rt = Some(rt);
    }

    async fn link_documents(&self, documents: String) -> String {
        let documents = documents.trim();
        let Some((one, two)) = documents.split_once(",") else {
            return "Please insert two document names separated by a comma".to_string();
        };
        let one = RecordId::from_table_key("document", one);
        let two = RecordId::from_table_key("document", two);

        match self
            .db
            .query("RELATE $one->link->$two;")
            .bind(("one", one))
            .bind(("two", two))
            .await
        {
            Ok(mut r) => match r.take::<Value>(0) {
                Ok(val) => format!("Link added: {val}"),
                Err(e) => e.to_string(),
            },
            Err(e) => e.to_string(),
        }
    }

    async fn raw_query(&self, query: &str) -> String {
        match self.db.query(query).await {
            Ok(mut r) => {
                let mut results = vec![];
                let num_statements = r.num_statements();
                for index in 0..num_statements {
                    match r.take::<Value>(index) {
                        Ok(good) => results.push(good.to_string()),
                        Err(e) => results.push(e.to_string()),
                    }
                }
                results.join("\n")
            }
            Err(e) => e.to_string(),
        }
    }

    async fn see_docs(&self) -> String {
        let res = self
            .raw_query("(SELECT VALUE title FROM document).sort()")
            .await;
        format!("All database article titles: {res}")
    }

    async fn fts_search(&self, input: String) -> Result<String, String> {
        let input = input.trim().to_owned();
        match self
            .db
            .query(
                "SELECT 
                search::highlight('**', '**', 0) AS title, 
                search::highlight('**', '**', 1) AS extract,
(search::score(0) * 3) + search::score(1) AS score
                FROM document
            WHERE title @0@ $input OR extract @1@ $input
            ORDER BY score DESC;",
            )
            .bind(("input", input))
            .await
        {
            Ok(mut res) => Ok(res.take::<Value>(0).map_err(|e| e.to_string())?.to_string()),
            Err(e) => Err(e.to_string()),
        }
    }

    async fn linked_docs(&self, doc: String) -> String {
        let doc = doc.trim();
        self.raw_query(&format!(
            "type::thing('document', '{doc}').{{..3}}.{{ id, next: ->link->document.@ }};
                "
        ))
        .await
    }

    fn view(&self) -> Element<Message> {
        column![
            row![iced::widget::image("surreal.png").height(100).width(200)],
            row![
                button("Insert document")
                    .width(190)
                    .on_press(Message::InsertDocuments),
                text_editor(&self.document_content)
                    .placeholder("Add Wikipedia article title to insert, separated by commas")
                    .on_action(Message::InsertDocumentsContent),
            ],
            row![text("")],
            row![
                button("Link documents")
                    .width(190)
                    .on_press(Message::LinkDocuments),
                text_editor(&self.link_content)
                    .placeholder("Enter two document titles, separated by a comma")
                    .on_action(Message::LinkDocumentsContent),
            ],
            row![
                button("Link unlinked docs")
                    .width(190)
                    .on_press(Message::TryLink),
                text_input(
                    "Try to create links for docs based on possible article names in their summary",
                    ""
                )
            ],
            row![text("")],
            row![
                button("Add OpenAI embeddings")
                    .width(190)
                    .on_press(Message::AddOpenAi),
                text_input(
                    "Add OpenAI embeddings to documents that do not have them",
                    ""
                )
            ],
            row![
                button("Add Mistral embeddings")
                    .width(190)
                    .on_press(Message::AddMistral),
                text_input(
                    "Add Mistral embeddings to documents that do not have them",
                    ""
                )
            ],
            row![
                button("OpenAI similarity search")
                    .width(190)
                    .on_press(Message::OpenAiSimilaritySearch),
                text_editor(&self.openai_doc_search)
                    .placeholder("Enter document name")
                    .on_action(Message::OpenAiSimilaritySearchContent),
            ],
            row![
                button("Mistral similarity search")
                    .width(190)
                    .on_press(Message::MistralSimilaritySearch),
                text_editor(&self.mistral_doc_search)
                    .placeholder("Enter document name")
                    .on_action(Message::MistralSimilaritySearchContent),
            ],
            row![
                button("Full text search").width(190).on_press(Message::Fts),
                text_editor(&self.fts_text)
                    .placeholder("Find a document via full-text search")
                    .on_action(Message::FtsContent),
            ],
            row![
                button("See linked articles")
                    .width(190)
                    .on_press(Message::SeeLinks),
                text_editor(&self.seelinks_text)
                    .placeholder("Finds all linked aticles down to a depth of 3")
                    .on_action(Message::SeeLinksContent),
            ],
            row![text("")],
            row![
                button("See all document titles")
                    .width(190)
                    .on_press(Message::SeeDocs),
                text_input("See titles of all documents in the database", "")
            ],
            row![text("")],
            row![
                button("Run query").width(190).on_press(Message::Query),
                text_editor(&self.query_content)
                    .placeholder("Run any raw SurrealQL query")
                    .on_action(Message::QueryContent),
            ],
            scrollable(text(&self.app_output).size(19).center()).width(1000)
        ]
        .padding(50)
        .align_x(Center)
        .into()
    }
}

fn main() -> Result<(), iced::Error> {
    let surreal = Palette {
        background: color!(0x15131D),
        text: color!(0xF9F9F9),
        primary: color!(0x242133),
        success: color!(0xFF00A0),
        danger: color!(0xFF00A0),
    };

    let custom = Arc::new(Custom::new("Surreal".to_string(), surreal));
    let cloned = Theme::Custom(custom);
    iced::application(
        "SurrealDB AI-native multi-model demo UI",
        App::update,
        App::view,
    )
    .theme(move |_| cloned.clone())
    .run()?;
    Ok(())
}
```
