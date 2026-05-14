---
title: "Create a Search Engine with SurrealDB Full-Text Search"
slug: "create-a-search-engine-with-surrealdb-full-text-search"
date: "2023-11-13T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "6 min read"
summary: "When it comes to managing and retrieving vast amounts of textual data, the ability to perform efficient and accurate searches is paramount."
source: "https://surrealdb.com/blog/create-a-search-engine-with-surrealdb-full-text-search"
cover: "../../assets/709feaf7660f28cb.jpg"
---

# Create a Search Engine with SurrealDB Full-Text Search

![Create a Search Engine with SurrealDB Full-Text Search](../../assets/709feaf7660f28cb.jpg)

When it comes to managing and retrieving vast amounts of textual data, the ability to perform efficient and accurate searches is paramount. SurrealDB has integrated a powerful Full-Text Search capability right into its core, ensuring developers have access to robust and flexible search functionality, regardless of their deployment environment and without a steep learning curve.

### How is Full-Text search different from `string::contains`?

While pattern-matching functions and full-text search are both techniques used to search for specific text within a dataset, they serve different purposes and have different underlying mechanisms.

Pattern Matching functions like **`string::contains`** are used to determine if a specific sequence of characters (or a pattern) exists in a string and typically handle simple queries.

```surrealql
RETURN string::contains('Hello, world', 'world');
```

On the flip side, full-text search is a powerhouse. It allows you to double down into any text string, regardless of its position or context within a document. In essence, full-text search offers a broader and more versatile searching capacity.

It's more flexible and scalable than plain pattern matching.

But before diving into understanding how Full-Text search works in SurrealDB, here are some core concepts to brush up on!

## Core Concepts

For us to be confident with using the search feature, we need to follow along the transformational journey of the phrase '**_Getting started with SurrealDB_**'.

### 1. Tokenisers

Imagine you're slicing a delicious pie - each piece represents a token, and the knife is the tokeniser. Tokenisers define where to 'cut' your data into manageable pieces based on rules such as spaces, letters, digits, email and more.

If we tokenise the sentence '**_Getting started with SurrealDB_**' based on space, it would be broken down into tokens: Getting, started, with, SurrealDB.

![GettingStartedWithSurrealDB](../../assets/255a967e604cac99.jpg)

### 2. Filters

Once tokens are generated, they pass through filters for additional processing and refinement. Here’s a rundown of some vital filters.

| | | |
|---|---|---|
| **lowercase** | Converts characters to lowercase |
| **ascii** | Converts to ASCII, removing diacritics |
| **stemmer(language)** | Converts to the **_[word stem](https://en.wikipedia.org/wiki/Word_stem)_**, like removing plurals |
| **edge n-gram** and **n-gram** | Token processing techniques, for example, the ngram token filter will change 'fox' to [f, fo, o, ox, x] |
| **snowball** | Reduces tokens to their **_[root form](https://en.wikipedia.org/wiki/Word_stem)_** and converts the case to lowercase |

### 3. Analyzers

[Analyzers](/docs/surrealql/statements/define/analyzer) are foundational to how text is processed in Full-Text Search. It is defined by its name, a set of tokenisers, and a collection of filters.

For instance, if we were to define an analyzer for the phrase '**_Getting started with SurrealDB_**' based on the snowball filter, it would look like this:

```surrealql
DEFINE ANALYZER example_snowball TOKENIZERS class FILTERS snowball(english);
-- Input Text: 'Getting started with SurrealDB'
-- Tokens: ['get', 'start', 'with', 'surrealdb']
```

### 4. The Matches operator

To match search terms with an indexed column, the [MATCHES](/docs/surrealql/operators#matches) operator `@[ref]@` is introduced. The operator can include a numeric reference, which is used by the [scoring function](/docs/surrealql/functions/database/search). For example:

```surrealql
SELECT title, search::score(1) AS score FROM book
  WHERE title @1@ 'file system'
  ORDER BY score DESC;
```

### 5. Search Function

These functions are used in conjunction with the 'matches' operator to either collect the relevance score or highlight the searched keywords within the content.

[`search::highlight()`](/docs/surrealql/functions/database/search#highlight): Highlights the matching keywords.

[`search::offsets()`](/docs/surrealql/functions/database/search#offsets): Returns the position of the matching keywords.

[`search::score()`](/docs/surrealql/functions/database/search#score): Returns the relevance score.

## Full-Text Search in SurrealDB

There are multiple services and libraries that help you integrate search functionality into your application. But they all come with some overhead and challenges. [SurrealDB](/features) stands out by addressing key pain points seen in other services.

| | | |
|---|---|---|
| **Simplified Querying with SurrealQL** | SurrealDB uses SurrealQL for both data operations and search, ensuring consistency for developers. Many search providers require another language for database queries |
| **Data Integrity** | SurrealDB search is ACID compliant. If you search right after an insert, you can trust the results |
| **Scalability** | SurrealDB's full-text search scales alongside the database. When you expand SurrealDB, both the database and its search capabilities grow |
| **Integrated Faceted Search** | Think of Amazon's product count in search results. While some systems treat this as an extra feature, SurrealDB integrates it, reducing setup complexity |

Developers can define custom analyzers to specify exactly how their text data should be processed. The engine supports multiple tokenisers and advanced filters.

## Build a search engine using SurrealDB

Let’s test out the search query of SurrealQL by building a simple search engine. Consider a library dedicated only to Linux-related books. Here are some of the titles you can find in this Linux books dataset.

| | | |
|---|---|---|
| ID | Title | Content |
| 1 | Understanding Network Configurations in Linux | To be a network engineer it is important to be well versed with configurations. This book explains different network configurations |
| 2 | Linux Server Administration | Managing a Linux server requires specific knowledge and skills. This book covers configuring services. |
| 3 | Shell Scripting with Linux | This book teaches you how to write effective scripts to automate tasks and streamline your workflow. |
| 4 | Advanced Linux Commands | This book dives deep into the world of Linux, exploring advanced commands and techniques. |
| 5 | Linux for Beginners | New to Linux? No problem. This book is designed to help beginners get started with Linux. |

Let’s add these books and some more to our SurrealDB database.

```javascript
INSERT INTO book [
    {title:'Linux Installation Guide', content: 'Learn how to install Linux with this comprehensive guide. We cover everything from downloading the ISO, creating a bootable USB, to the actual installation process.'},
    {title:'Advanced Linux Commands', content: 'This book dives deep into the world of Linux, exploring advanced commands and techniques that can help you master your system.'},
    {title:'Linux for Beginners', content: 'New to Linux? No problem. This book is designed to help beginners get started with Linux, covering the basics of the operating system and providing simple tutorials.'},
    {title:'Linux Networking Essentials', content: 'Discover the fundamentals of networking in Linux. This book covers network configuration, troubleshooting, and essential commands.'},
    {title:'Linux Security Handbook', content: 'Security is crucial, and this book provides a detailed guide on securing your Linux system. Learn about firewalls, encryption, and best practices.'},
    {title:'Shell Scripting with Linux', content: 'Shell scripting is a powerful tool in Linux. This book teaches you how to write effective scripts to automate tasks and streamline your workflow.'},
    {title:'Linux Server Administration', content: 'Managing a Linux server requires specific knowledge and skills. This book covers everything from setting up a server, configuring services, to monitoring performance.'},
    {title:'Linux File Systems Explained', content: 'Understanding file systems is key to mastering Linux. This book explains different file systems, their features, and how to manage them.'},
    {title:'Linux Installation tools Explained', content: 'Understanding file systems is key to mastering Linux. This book explains different Linux Installation tools, and how to use them.'},
    {title:'Understanding Network configurations in Linux', content: 'To be a network engineer it is important to be well versed with configurations. This book explains different network configurations'}
]
```

As we will primarily search through the title and content of our `book` record, we will define [full-text](/docs/surrealql/statements/define/indexes) indexes on these fields. `book_title` and `book_content` are our indexes here.

We will also select the required tokenisers that will consider spaces, punctuation, and other language rules.

We then create a [custom analyzer](/docs/surrealql/statements/define/analyzer) and select the required tokenisers that will consider spaces, punctuation, and other language rules.

Using [BM25](https://en.wikipedia.org/wiki/Okapi_BM25) allows us to provide a sophisticated relevance scoring mechanism for search queries, which can improve the quality of search results. How we pick the parameters for BM25 [(@k1, @b)] is a blog for another day but all you need to know to get started is that 1.2 and 0.75 work for most datasets.

```javascript
DEFINE ANALYZER book_analyzer TOKENIZERS blank,class,camel,punct FILTERS snowball(english);
DEFINE INDEX book_title ON book FIELDS title SEARCH ANALYZER book_analyzer BM25(1.2,0.75);
DEFINE INDEX book_content ON book FIELDS content SEARCH ANALYZER book_analyzer BM25(1.2,0.75) HIGHLIGHTS;
```

### Search Query

Let’s build our SurrealQL query to search for all the books that specifically talk about 'network configurations'.

```javascript
SELECT
  id,
  title,
  search::highlight('<b>', '</b>', 1) AS content_highlighted,
  search::score(0) * 2 + search::score(1) * 1 AS score
FROM book
WHERE title @0@ 'network configuration'
   OR content @1@ 'network configuration'
ORDER BY score DESC
LIMIT 10;
```

We use `search::highlight(<b>, </b>, 1)` to highlight instances of the search term in the **`content`** field, making them stand out with bold tags. The **`1`** indicates that it references the `content` field.

The **`search::score(0)`** retrieves the relevance score for the `title` field, and **`search::score(1)`** does the same for the **`content`** field.

Results are ordered by the calculated score in descending order (**`ORDER BY score DESC`**), prioritising books with higher scores and we limit the results to the top 10 (**`LIMIT 10`**) relevant books.

### Search Output

```javascript
[
    {
        content_highlighted:
            'To be a <b>network</b> engineer it is important to be well versed with <b>configurations</b>. This book explains different <b>network</b> <b>configurations</b>',
        id: 'book:2m1pq6cpn5fng7ad70ha',
        score: 8.831891536712646,
        title: 'Understanding Network Configurations in Linux',
    },
    {
        content_highlighted:
            'Discover the fundamentals of <b>networking</b> in Linux. This book covers <b>network</b> <b>configuration</b>, troubleshooting, and essential commands.',
        id: 'book:ehinzz40h53qawbagxx9',
        score: 5.694946765899658,
        title: 'Linux Networking Essentials',
    },
];
```

On defining the indexes and firing the search query, our output follows the conditions and format described in the query. We have 2 books that have the phrase 'network configuration' mentioned in them.

`content_highlighted`: Shows a snippet of the book content where the search terms 'network' and 'configurations' are found.

`id`: Returns the record ID of the matched books.

`score`: Returns the combined search score. This score can be positive or negative based on the occurrence of the matches.

### Get your calculators out!

The final combined score for the book titled 'Understanding Network configurations in Linux'.

> search::score(0) = 2.611705780029297

>

> search::score(1) = 3.6084799766540527

>

> Final score=(2.611705780029297×2)+(3.6084799766540527×1)

>

> Final Score=5.223411560058594+3.608479976654057

>

> Final Score≈8.831891536712646

### Why did we give the title a weight of 2 and the content a weight of 1 in the final score calculation?

For our use case of searching through books, we are assuming that a match in the title is more significant than a match in the content as we consider the title of the book to be a concise summary of its content and thus, a strong indicator of relevance. But it's not a rule and you are free to set the weights based on what you feel is more relevant.

## Beyond the 101’s of Search

Building the above Linux books database search engine has shown how effortlessly you can set up Full-Text Search with SurrealDB.

You now have the power to [define custom analyzers](/docs/surrealql/statements/define/analyzer) and use various tokenisers to tailor the search precisely to the dataset's unique demands.

The use of SurrealQL to interact with data as well as search increases familiarity and we are not forced to juggle different query languages or worry about the consistency of our operations.

In the upcoming blogs around search features, we dive deep into indexes and how [SurrealIX](/features) stands out from existing solutions. To learn more about [SurrealIX](/features), visit the [documentation](/docs/surrealql/statements/define/indexes) or our [live stream](https://www.youtube.com/live/b_HVN87Wwg0?si=dBo6ta1HldG5mwtO) on Full-Text Search.

If you've experimented with the above example or have any questions, don't miss the chance to join our vibrant [developer community on Discord](https://discord.gg/surrealdb) and share your experience with us!
