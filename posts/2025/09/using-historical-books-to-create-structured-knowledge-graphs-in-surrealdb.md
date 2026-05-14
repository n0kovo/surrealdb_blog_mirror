---
title: "Using historical books to create structured knowledge graphs in SurrealDB"
slug: "using-historical-books-to-create-structured-knowledge-graphs-in-surrealdb"
date: "2025-09-11T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "12 min read"
summary: "PDF scans of old historical books can be brought to life with LLM models and then stored and queried in a structured form using SurrealQL."
source: "https://surrealdb.com/blog/using-historical-books-to-create-structured-knowledge-graphs-in-surrealdb"
cover: "../../assets/529f2c0a7af13039.jpg"
---

# Using historical books to create structured knowledge graphs in SurrealDB

![Using historical books to create structured knowledge graphs in SurrealDB](../../assets/529f2c0a7af13039.jpg)

Welcome back to the second blog post on giving structure to unstructured data so that it can be stored and worked with in SurrealDB. If you haven't seen the first post yet, [check it out here](/blog/using-unstructured-data-to-create-knowledge-graphs-in-surrealdb).

While the original content of that first post had no structure, it was still fairly predictable and involved working with quick self-introductions of this sort that made it easy to work with:

> “My name is Tyler Banks, and I’ve been working as a software engineer for the past four years. Currently, I’m part of the developer relations team, where I focus on creating tools and documentation to help developers integrate our APIs more easily. Our team is led by Brian Thompson.”

This time we are going to work with some content that is much less predictable. We are going to get into the mind of a historical researcher who wants get an idea of how the First World War changed the views of the English-speaking world towards certain nations in Europe. The shift from the largely peaceful [Belle Époque](https://en.wikipedia.org/wiki/Belle_%C3%89poque) into a worldwide war was such a sudden transition that it remains one of the most researched parts of world history.

A researcher studying this could structure the project in three-year intervals like this:

- How did people feel in 1911, three years before the war began?
- How did people feel in 1914 during and after the leadup to the war?
- How did people feel in 1917 when the entire continent had been at war for

years?

- How did people feel in 1920 after it was over?

A researcher doing this would ideally go through thousands and thousands of books, newspaper articles, and anything else available. We don't have the space for that in this blog post. Instead, we will choose one book from each year that pertains to Europe as a whole in as general a way as possible.

Archive.org is the best place to find books from the past that can be read online and downloaded as pdfs, and a quick search is enough to find some good candidate books.

The four books are:

- [The Complete Pocket-Guide to Europe](https://archive.org/details/completepocketgu02sted/page/46/mode/2up),

written in 1911 during happier times in Europe. 592 pages.

- [Europe Since Napoleon](https://archive.org/details/europesincenapol0000unse_q7p6/page/n3/mode/2up),

written in 1914. It includes recent events at the time such as those in the Balkan Peninsula. 368 pages.

- [Present-day Europe: Its National States of Mind](https://archive.org/details/presentdayeurope00stod/page/n11/mode/2up),

written in 1917. 346 pages.

- [Geographical and Industrial Studies: The New Europe](https://archive.org/details/geographicalindu00alle/page/n5/mode/2up),

written in 1920. 474 pages.

## Starting the project and checking the data

To get started, use `cargo new history` to start a new project, then download the pdfs for each book and save them as 1911.pdf, 1914.pdf, 1917.pdf, and 1920.pdf. Here are the pdf links.

- [Save as 1911.pdf](https://ia800201.us.archive.org/34/items/completepocketgu02sted/completepocketgu02sted.pdf)
- [Save as 1914.pdf](https://ia800407.us.archive.org/25/items/europesincenapol0000unse_q7p6/europesincenapol0000unse_q7p6.pdf)
- [Save as 1917.pdf](https://ia801207.us.archive.org/5/items/presentdayeurope00stod/presentdayeurope00stod.pdf)
- [Save as 1920.pdf](https://dn790002.ca.archive.org/0/items/geographicalindu00alle/geographicalindu00alle.pdf)

A little bit of code using the [`pdf_extract`](https://crates.io/crates/pdf-extract) crate is enough to turn these pdfs into `.txt` files.

```rust
use std::io::Write;

fn main() {
    for path in ["1911.pdf", "1914.pdf", "1917.pdf", "1920.pdf"] {
        let bytes = std::fs::read(path).unwrap();
        let out = pdf_extract::extract_text_from_mem(&bytes).unwrap();
        let mut f = std::fs::File::create(path.replace("pdf", "txt")).unwrap();
        f.write(&mut out.as_bytes()).unwrap();
        println!("Done {path}!");
    }
}
```

Note: If you don't feel like following this step, just click on the `FULL TEXT` button inside each book's page on Archive.org where the text has already been extracted. But since we are following the steps of an imaginary researcher who may be working with random pdfs from all sorts of sources, knowing how to extract the text from a pdf is a good place to start.

In the last post we only used the [QuestionAnsweringModel](https://docs.rs/rust-bert/latest/rust_bert/pipelines/question_answering/struct.QuestionAnsweringModel.html) from the `rust_bert` crate, but there are many other models to choose from. The first model to try out is the [SentimentModel](https://docs.rs/rust-bert/latest/rust_bert/pipelines/sentiment/struct.SentimentModel.html). This model gives outputs that look like this, and is a very confident one with scores that are very often in the high 0.9s. The `polarity` part of the output is a simple enum that only has two variants: `Positive` and `Negative`.

```syntax
[
    Sentiment {
        polarity: Positive,
        score: 0.998,
    },
    Sentiment {
        polarity: Negative,
        score: 0.992,
    },
    Sentiment {
        polarity: Positive,
        score: 0.999,
    },
]
```

This model will be a good way to give our books a quick test to see if they do have enough content, and whether our hypothesis is correct that sentiment should change drastically from year to year.

The code below first creates the model, then goes through the books line by line to see if a country's name shows up. If so, it will check the sentiment and keep it if the confidence level is at least 0.9. Finally, it adds up the number of positive and negative results and displays them per country per year.

```rust
use rust_bert::pipelines::sentiment::{Sentiment, SentimentModel, SentimentPolarity};
use std::fs::read_to_string;

fn main() {
    let sentiment_model = SentimentModel::new(Default::default()).unwrap();

    for subject in [
        "Germany", "France", "Russia", "Belgium", "Italy", "Austria", "Britain",
    ] {
        for path in ["1911.txt", "1914.txt", "1917.txt", "1920.txt"] {
            let content = read_to_string(path).unwrap();
            let res = content.lines().filter(|l| {
                l.to_ascii_lowercase()
                    .contains(&subject.to_ascii_lowercase())
            });
            let output = sentiment_model.predict(
                content
                    .clone()
                    .lines()
                    .filter(|l| {
                        l.to_ascii_lowercase()
                            .contains(&subject.to_ascii_lowercase())
                    })
                    .collect::<Vec<&str>>(),
            );
            let (positive, negative): (Vec<(&str, Sentiment)>, Vec<(&str, Sentiment)>) = res
                .into_iter()
                .zip(output.into_iter())
                .filter(|(_, sentiment)| sentiment.score > 0.9)
                .partition(|n| n.1.polarity == SentimentPolarity::Positive);
            let positive = positive.len() as f64;
            let negative = negative.len() as f64;
            let ratio = positive / (positive + negative);

            println!(
                "{path} for {subject}: positive ratio is {ratio:.2} (positive is {positive}, negative is {negative})"
            );
        }
        println!();
    }
}
```

Looks like the model is working well and these four books have good data. We can see Germany's positive ratio drop in 1914, plummet in 1917, and recover after the war. Britain is pretty much stable throughout, France drops a little bit in 1914, and Russia had a catastrophic drop in 1914 after which its ratio recovered.

```syntax
1911.txt for Germany: positive ratio is 0.55 (positive is 11, negative is 9)
1914.txt for Germany: positive ratio is 0.21 (positive is 15, negative is 55)
1917.txt for Germany: positive ratio is 0.18 (positive is 25, negative is 113)
1920.txt for Germany: positive ratio is 0.47 (positive is 27, negative is 31)

1911.txt for France: positive ratio is 0.68 (positive is 28, negative is 13)
1914.txt for France: positive ratio is 0.37 (positive is 46, negative is 79)
1917.txt for France: positive ratio is 0.46 (positive is 46, negative is 54)
1920.txt for France: positive ratio is 0.56 (positive is 25, negative is 20)

1911.txt for Russia: positive ratio is 0.48 (positive is 13, negative is 14)
1914.txt for Russia: positive ratio is 0.03 (positive is 5, negative is 189)
1917.txt for Russia: positive ratio is 0.30 (positive is 83, negative is 198)
1920.txt for Russia: positive ratio is 0.66 (positive is 61, negative is 31)

1911.txt for Britain: positive ratio is 0.53 (positive is 8, negative is 7)
1914.txt for Britain: positive ratio is 0.52 (positive is 37, negative is 34)
1917.txt for Britain: positive ratio is 0.43 (positive is 6, negative is 8)
1920.txt for Britain: positive ratio is 0.64 (positive is 7, negative is 4)
```

</br>

## Adding a second model

The `SentimentModel` works well enough to get a general sentiment of how a country is portrayed. But we'd also like to find the interactions that took place between one country or another in each of these books. Now, keep in mind that while each of these books are written in a certain year, they include events from well before that year. So for example, the book written in 1917 is not a book _about the year 1917_, but a book about Europe written by an author who views the continent _from a 1917 point of view_.

To give this a try, we can use the [ZeroShotClassificationModel](https://docs.rs/rust-bert/latest/rust_bert/pipelines/index.html#6-zero-shot-classification) we mentioned in the last post but never tried. This model requires some fine tuning but is quite fun to use.

The Zero-shot classification model takes a number of options that it then compares against a text and then returns a confidence level for each. For example, if you took the text of this blog and gave it the options ["tech blog", "grocery list", "comic book"], it would have a high confidence for the first option and next to zero for the other two.

It's quite good when the source text possible options are clear. Here's a clear example from the book written in 1920:

```syntax
Germany planned to march her armies quickly through Belgium into France and take Paris.
```

Since we are considering which countries have positive or negative reactions to each other, we would like to somehow know that this is a negative event between Germany and France. We can test it out by seeing whether it thinks "Germany did something good to France" is more plausible, or whether "Germany did something good to France" is. The 1024 in the code below represents the tokens used for the `ZeroShotClassificationModel`'s default model.

```rust
fn main() {
    let z = ZeroShotClassificationModel::new(Default::default()).unwrap();

    z.predict_multilabel(&["Germany planned to march her armies quickly through Belgium into France and take Paris."],
        &[
            "Germany did something good to France",
            "Germany did something bad to France"],
        None,
        1024);
}
```

</br>

Printing out the `text` and `score` fields shows that it did a pretty good job. Though note that this model tends to be not very confident: only 0.76. You need a text like "Germany invaded France" for it to reach 0.99.

```syntax
[
    Label {
        text: "Germany did something good to France",
        score: 0.14272432029247284,
        id: 0,
        sentence: 0,
    },
    Label {
        text: "Germany did something bad to France",
        score: 0.7630993127822876,
        id: 1,
        sentence: 0,
    },
]
```

However, the vast majority of the content in these books will have nothing to do with one country or another. So we'll want a third variant that represents a "none of the above" situation. Coming up with this third variant is the tricky part. Let's see what happens when we try a "{country_one} did nothing in particular to {country_two}" format, such as "Germany did nothing in particular to France". We'll also include a statement after the first one that has nothing to do with either Germany or France: "I dedicate this book to my cat".

```rust
use rust_bert::pipelines::zero_shot_classification::ZeroShotClassificationModel;

fn main() {
    let z = ZeroShotClassificationModel::new(Default::default()).unwrap();
    let statements = [
        "Germany planned to march her armies quickly through Belgium into France and take Paris...",
        "I dedicate this book to my cat",
    ];

    for text in statements {
        println!("\nResults for {text}");
        z.predict_multilabel(
            &[text],
            &[
                "Germany did something good to France",
                "Germany did something bad to France",
                "Germany did nothing in particular to France",
            ],
            None,
            1024,
        )
        .unwrap()
        .into_iter()
        .for_each(|res| {
            res.into_iter()
                .for_each(|res| println!("{} {}", res.text, res.score))
        });
    }
}
```

The model still does a good job with the first sentence, but not at all with the second. For the second, it is not at all convinced about any of the three options but still has a slight preference for "Germany did something bad to France" for the sentence "I dedicate this book to my cat".

```syntax
Results for Germany planned to march her armies quickly through Belgium into France and take Paris...
Germany did something good to France 0.13134652376174927
Germany did something bad to France 0.8228927850723267
Germany did nothing in particular to France 0.00036616341094486415

Results for I dedicate this book to my cat
Germany did something good to France 0.0025551856961101294
Germany did something bad to France 0.0041771335527300835
Germany did nothing in particular to France 0.00007780511805322021
```

The same sort of output happens if we try "Nothing happened". The model seems quite sure that at least _something_ did happen.

```syntax
Results for I dedicate this book to my cat
Germany did something good to France 0.0025551856961101294
Germany did something bad to France 0.0041771335527300835
Nothing happened 0.0001571544271428138
```

Things look better if we change this to "Something else happened". This variant gets a certain amount of confidence, but not enough to overshadow something like "Germany did something bad to France" if the model is very sure about that statement.

```syntax
Results for Germany planned to march her armies quickly through Belgium into France and take Paris...
Germany did something good to France 0.13134652376174927
Germany did something bad to France 0.8228927850723267
Something else happened 0.6181733012199402

Results for I dedicate this book to my cat
Germany did something good to France 0.0025551856961101294
Germany did something bad to France 0.0041771335527300835
Something else happened 0.2970941662788391
```

If you are feeling ambitious at this point, you could bring in the `QuestionAnsweringModel` that we used in the last post to do a second check to confirm that something happened between one country and another.

```rust
let q = QuestionAnsweringModel::new(Default::default()).unwrap();

let statement = "I dedicate this book to my cat, who somehow knows that Germany planned to march her armies quickly through Belgium into France and take Paris in 1914 and that France wanted to retake Alsace-Lorraine";

q.predict(
    &[QaInput {
        question: "What did Germany do to France?".to_string(),
        context: statement.to_string(),
    }],
    1,
    1,
);
```

This would let you check the `score` again and throw out anything with a low level of confidence, as well as grab the `answer` for a quicker textual representation than the full line of context.

```syntax
Answer {
    score: 0.31812939047813416,
    start: 74,
    end: 90,
    answer: "march her armies",
}
```

We won't be using this model in addition to the other two due to lack of time and space, but feel free to give it a try!

## The rest of the code

The rest of the code involves working with these two models to create two types of graph relations: a `media->mention->country` path and a `country->interaction->country` path. For `media` we will create records like `media:1911` for each year, which will make the graphical summary at the end more interesting to work with. And the countries we will look at will each have their own record.

```surrealql
CREATE media:1911, media:1914, media:1917, media:1920, country:Germany, country:France,
country:Russia, country:Belgium, country:Italy, country:Austria, country:Britain;
```

Each of these edges can be inserted using a Rust struct that holds some information on the records involved and the context. (We could use a `Datetime` for the year but we'll go with a `String` for simplicity)

```rust
#[derive(Serialize)]
struct Mention {
    r#in: RecordId,
    out: RecordId,
    year: String,
    passage: String,
    sentiment: String,
}
```

Next is a function to break each book into chunks. It's a simple function that just grabs 400 characters, turns new lines into spaces, and removes the large spaces you sometimes see between words generated from pdfs, like "Ge- rmany".

```rust
fn get_passages(content: &str, countries: Vec<&str>) -> Vec<String> {
    content
        .chars()
        .collect::<Vec<char>>()
        .chunks(400)
        .map(|b| {
            b.iter()
                .map(|c| if c == &'\n' { &' ' } else { c })
                .collect::<String>()
        })
        .map(|s| {
            let s = s.replace("-     ", "");
            let s = s.replace("-    ", "");
            let s = s.replace("-   ", "");
            let s = s.replace("-  ", "");
            s.replace("- ", "")
        })
        .filter(|page| countries.iter().all(|country| page.contains(country)))
        .collect::<Vec<String>>()
}
```

After that comes all the logic to work with the models for each possible combination of country for each book. To speed up the models we have batched the inputs to a certain extent. However, we haven't collected absolutely everything before batching because the database can insert these graph edges at each combination of year and country, and that will let us go straight to Surrealist to begin taking a look at the results even as they are coming in. To ensure that we know what's going on we have a `println!` statement at each point in the way.

Here is all the code:

```rust
use rust_bert::pipelines::{
    sentiment::{SentimentModel as StModel, SentimentPolarity},
    zero_shot_classification::ZeroShotClassificationModel as ZsModel,
};
use serde::Serialize;
use std::fs::read_to_string;
use surrealdb::{RecordId, engine::any::connect};
use tokio::runtime::Runtime;

const COUNTRIES: [&str; 7] = [
    "Germany", "France", "Russia", "Belgium", "Italy", "Austria", "Britain",
];

#[derive(Serialize)]
struct Mention {
    r#in: RecordId,
    out: RecordId,
    year: String,
    passage: String,
    sentiment: String,
}

fn get_passages(content: &str, countries: Vec<&str>) -> Vec<String> {
    content
        .chars()
        .collect::<Vec<char>>()
        .chunks(400)
        .map(|b| {
            b.iter()
                .map(|c| if c == &'\n' { &' ' } else { c })
                .collect::<String>()
        })
        .map(|s| {
            let s = s.replace("-     ", "");
            let s = s.replace("-    ", "");
            let s = s.replace("-   ", "");
            let s = s.replace("-  ", "");
            s.replace("- ", "")
        })
        .filter(|page| countries.iter().all(|country| page.contains(country)))
        .collect::<Vec<String>>()
}

fn main() {
    println!("Starting ZsModel");
    let zs_model = ZsModel::new(Default::default()).unwrap();
    println!("Starting StModel");
    let st_model = StModel::new(Default::default()).unwrap();

    let runtime = Runtime::new().unwrap();

    runtime.block_on(async {
        let db = connect("ws://localhost:8000").await.unwrap();
        db.use_ns("ns").use_db("db").await.unwrap();

        db.query("CREATE media:1911, media:1914, media:1917, media:1920, country:Germany, country:France, country:Russia, country:Belgium, country:Italy, country:Austria, country:Britain").await.unwrap();

        for year in ["1911", "1914", "1917", "1920"] {

        let content = read_to_string(format!("{year}.txt")).unwrap();
        // General sentiment pass
        for country in COUNTRIES {
            println!("Getting {year} sentiment for {country}...");
            let relevant_passages = get_passages(&content, vec![country]);
            let relevant_passages = relevant_passages
                .iter()
                .map(|s| s.as_str())
                .collect::<Vec<_>>();
            let zipped = relevant_passages.clone().into_iter().zip(
                st_model
                    .predict(&relevant_passages)
                    .into_iter()
                    .filter(|s| s.score > 0.95),
            );

            let relations = zipped.into_iter().map(|(a, b)| {
                Mention {
                    r#in: format!("media:{year}").parse::<RecordId>().unwrap(),
                    out: RecordId::from_table_key("country", country),
                    year: year.to_string(),
                    passage: a.to_string(),
                    sentiment: if b.polarity == SentimentPolarity::Positive { "positive".to_string() } else { "negative".to_string() }
                }
            }).collect::<Vec<_>>();
            db.query(format!("INSERT RELATION INTO mention_{year} $relations")).bind(("relations", relations)).await.unwrap();
        }

        for country in COUNTRIES {
            println!("Getting {year} interactions for {country}...");
            let others = COUNTRIES.into_iter().filter(|n| *n != country);
            for other in others {
                // e.g. does this have both Britain and France
                let passages = get_passages(&content, vec![country, other]);
                let passages_ref = passages.iter().map(|s| s.as_ref()).collect::<Vec<_>>();
                let events = zs_model.predict(
                    &passages_ref,
                    [
                        &format!("{country} did something good to {other}"),
                        &format!("{country} did something bad to {other}"),
                        "Something else happened",
                    ],
                    None,
                    1024,
                ).unwrap_or_default();
                let zipped = passages.into_iter().zip(events.into_iter());
                let good = zipped.clone().filter(|(_, e)| {
                    e.text.contains("something good") && e.score > 0.6
                }).map(|(s, _)| {
                    Mention {
                        r#in: RecordId::from_table_key("country", country),
                    out: RecordId::from_table_key("country", other),
                    year: year.to_string(),
                    passage: s.to_string(),
                    sentiment: "positive".to_string()
                    }
                }).collect::<Vec<Mention>>();
                db.query(format!("INSERT RELATION INTO interaction_{year} $good")).bind(("good", good)).await.unwrap();

                let bad = zipped.clone().filter(|(_, e)| {
                    e.text.contains("something bad") && e.score > 0.6
                }).map(|(s, _)| {
                    Mention {
                        r#in: RecordId::from_table_key("country", country),
                    out: RecordId::from_table_key("country", other),
                    year: year.to_string(),
                    passage: s.to_string(),
                    sentiment: "negative".to_string()
                    }
                }).collect::<Vec<Mention>>();
                db.query(format!("INSERT RELATION INTO interaction_{year} $bad")).bind(("bad", bad)).await.unwrap();
            }
        }
        }
    });
}
```

## Querying the results

If you start a new SurrealDB instance via the `surreal start --unauthenticated` command and then run this code with `cargo run` (preferably `cargo run --release` for greater performance as there is a lot of data to work with), you should see this sort of output in the terminal. It will take some time to get through all of the content in each of the books.

```syntax
Starting ZsModel
Starting StModel
Getting 1911 sentiment for Germany...
Getting 1911 sentiment for France...
Getting 1911 sentiment for Russia...
Getting 1911 sentiment for Belgium...
Getting 1911 sentiment for Italy...
Getting 1911 sentiment for Austria...
Getting 1911 sentiment for Britain...
Getting 1911 interactions for Germany...
```

But we can start looking at the data right away as it comes in. As it runs, go to [Surrealist](https://app.surrealdb.com/) and connect. Let's see what we can see with some queries.

Here's one to show a single negative example of one thing a country did, followed by one thing a country had done to it over a single year.

```surrealql
SELECT 
    id,
    rand::enum(->interaction_1914[WHERE sentiment='negative' AND year='1914'].{out, passage}) AS negative_active_1914,
    rand::enum(<-interaction_1914[WHERE sentiment='negative' AND year='1914'].{in, passage}) AS negative_passive_1914
FROM country;
```

Sometimes the individual results show passages that truly do reflect interactions between two countries, such as these two between Austria and Germany.

```surrealql
{
    id: country:Germany,
    negative_active_1914: {
        out: country:Austria,
        passage: 'on”  as  he  termed   it.  Three  successive  wars,  against  Denmark,  against  Austria,  and  against  France,  were  deliberately  waged  to  erect   the  imposing  edifice  of  modern  Germany.  The  worship   of  brute  force,  inspired  by  the  conditions  under  which  German  union  was  achieved,  has  alienated  countries  which  by  origin,  by  past  alliances,  and  by  varied  o'
    },
    negative_passive_1914: {
        in: country:Austria,
        passage: 'eme  in  Central  Italy  and  in  the  kingdom  of the  Two  Sicilies.  It is true,  Austria  gave  up  her  provinces  in  the  Netherlands  (which  were  united  to  Holland),  but  these  had  long  been  of  very  little  value  to  her.  In  Germany  Metternich’s  influence   138  AUSTRIA-HUNGARY   outweighed  Stein’s,  and  the  hope  of a united  Germany  was  thwarted;  the  Federal  Diet '
    }
}
```

</br>

But sometimes the passage only holds a more general sentiment that isn't perfectly accurate. In the first example here we see a "negative interaction" between Italy and France that in fact is just an Italian politician making a negative speech along with a previous sentence showing France declaring war.

```surrealql
{
    id: country:Italy,
    negative_active_1914: {
        out: country:France,
        passage: 'd  offered  an  unpardonable  insult,  and  by  26  April  war  had  begun,  while  France  formally  declared  war  on  29  April.  Victor  Emmanuel  announced  the  news  to  his  countrymen  thus:  ‘‘  People  of  Italy!  Austria  has  invaded  Piedmont  because  I have  espoused  the  cause  of  our  common  country  in  the  Councils  of  Europe.  For  myself,  I  have  but  one  ambition,-to'
    },
    negative_passive_1914: {
        in: country:Germany,
        passage: 'ost.  Hence  he  joined  with  the  Tsar  in  the  Holy  Alliance,  though  he  thought  that  it was  mere  ‘‘empty  words”,  as  far  as  its  religious  intentions  went.  He  did  his  best,  through  the  Carlsbad  Decrees,  to  crush  out  all  thought,  all  initiative  in  South  Germany;  he  acquiesced  in  the  repressive  and  unsympathetic  Austrian  government  in  Italy,  and  he'
    }
}
```

But keep in mind that the use case here is a researcher using thousands and thousands of books and articles to gauge general sentiment. That means that we would probably see queries more in this sort of way

This is especially the case if we remember that a real researcher would have thousands and thousands of books and articles to work with, all with different lengths and styles of writing.

```surrealql
SELECT 
    id,
    count(->interaction_1914[WHERe sentiment='positive']->country[where country:Britain]) AS `1914`.positive,
    count(->interaction_1914[WHERE sentiment='negative']->country[where country:Britain]) AS `1914`.negative,
    count(->interaction_1917[WHERE sentiment='positive']->country[where country:Britain]) AS `1917`.positive,
    count(->interaction_1917[WHERE sentiment='negative']->country[where country:Britain]) AS `1917`.negative,
    count(->interaction_1920[WHERE sentiment='positive']->country[where country:Britain]) AS `1920`.positive,
    count(->interaction_1920[WHERE sentiment='negative']->country[where country:Britain]) AS `1920`.negative
FROM country;
```

That will show much more general trends for each country, such as this which shows Italy's interactions with Britain over the years.

```surrealql
{
    "1914": {
        negative: 16,
        positive: 11
    },
    "1917": {
        negative: 11,
        positive: 7
    },
    "1920": {
        negative: 0,
        positive: 1
    },
    id: country:Italy
}
```

Or the total positive and negative numbers for each country over the years, which now differs from our original test because this time we are working with 400-character chunks instead of single lines.

```surrealql
SELECT 
    id,
    count(<-mention_1911[WHERE sentiment='positive']<-media) AS `1911`.positive,
    count(<-mention_1911[WHERE sentiment='negative']<-media) AS `1911`.negative,
    count(<-mention_1914[WHERE sentiment='positive']<-media) AS `1914`.positive,
    count(<-mention_1914[WHERE sentiment='negative']<-media) AS `1914`.negative,
    count(<-mention_1917[WHERE sentiment='positive']<-media) AS `1917`.positive,
    count(<-mention_1917[WHERE sentiment='negative']<-media) AS `1917`.negative,
    count(<-mention_1920[WHERE sentiment='positive']<-media) AS `1920`.positive,
    count(<-mention_1920[WHERE sentiment='negative']<-media) AS `1920`.negative
FROM country;
```

The results for Germany are still similar to our original test, just fewer in number.

```surrealql
{
    "1911": {
        negative: 13,
        positive: 12
    },
    "1914": {
        negative: 61,
        positive: 19
    },
    "1917": {
        negative: 62,
        positive: 51
    },
    "1920": {
        negative: 24,
        positive: 34
    },
    id: country:Germany
},
```

</br>

Finally, there are visual queries that we can do with Surrealist's graph visualisation view. These have been saved for last because they are by far the most fun.

If you want some examples on how to use this view in general, [see this blog post](/blog/visualising-your-data-with-surrealists-graph-view).

To start off, we can use this query that looks at both the `in` and `out` fields of any graph edges connected to a country to see the entire network of edges we have. There are 1886 edges in total, making it a pretty noisy graph.

```surrealql
SELECT 
    id,
    <->?<->?
FROM country;
```

Since we've chosen a lot of edge names, we actually don't need to use any other queries to start poking through the data. Instead, we can select and deselect the edges on the right of the screen and mouseover the parts we are most interested in. If we only show the mentions for a country, we can see some general trends such as how Austria fades out as a subject of mention in 1920:

But not so for Germany, which is still heavily mentioned.

You can also see when choosing to display all edges that Belgium is mentioned quite a bit in 1920 compared to the other books.

Finding interesting bits to then check out with a more comprehensive query is exactly what this view is for. Let's put a query together to calculate the mentions per year per country to see if Belgium really is mentioned more in 1920 than the other countries.

```surrealql
SELECT *, <float>mention_1920 / <float>(mention_1911 + mention_1914 + mention_1917 + mention_1920) AS total_ratio_1920 FROM (SELECT 
    id,
    count(<-mention_1911) AS mention_1911,
    count(<-mention_1914) AS mention_1914,
    count(<-mention_1917) AS mention_1917,
    count(<-mention_1920) AS mention_1920
FROM country) ORDER BY total_ratio_1920 DESC;
```

And it turns out that this is the case! Belgium is mentioned in the 1920 book way more than in previous years, while Austria at the bottom has completely dropped off the map. We can't draw any conclusions from this single book, but it might be a hint that the world in 1920 was particularly interested in Belgium's reconstruction. Only more data will tell.

```surrealql
[
	{
		id: country:Belgium,
		mention_1911: 13,
		mention_1914: 10,
		mention_1917: 20,
		mention_1920: 30,
		total_ratio_1920: 0.410958904109589f
	},
	{
		id: country:Germany,
		mention_1911: 25,
		mention_1914: 80,
		mention_1917: 113,
		mention_1920: 58,
		total_ratio_1920: 0.21014492753623187f
	},
	{
		id: country:Russia,
		mention_1911: 28,
		mention_1914: 104,
		mention_1917: 155,
		mention_1920: 76,
		total_ratio_1920: 0.209366391184573f
	},
	{
		id: country:France,
		mention_1911: 50,
		mention_1914: 116,
		mention_1917: 76,
		mention_1920: 56,
		total_ratio_1920: 0.18791946308724833f
	},
	{
		id: country:Italy,
		mention_1911: 33,
		mention_1914: 85,
		mention_1917: 68,
		mention_1920: 38,
		total_ratio_1920: 0.16964285714285715f
	},
	{
		id: country:Britain,
		mention_1911: 17,
		mention_1914: 68,
		mention_1917: 10,
		mention_1920: 15,
		total_ratio_1920: 0.13636363636363635f
	},
	{
		id: country:Austria,
		mention_1911: 26,
		mention_1914: 134,
		mention_1917: 86,
		mention_1920: 16,
		total_ratio_1920: 0.061068702290076333f
	}
]
```
