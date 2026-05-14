---
title: "Release v1.1.0"
slug: "release-v1-1-0"
date: "2024-01-09T00:00:00.000Z"
categories:
  - "releases"
read_time: "3 min read"
summary: "We're excited to announce SurrealDB v1.1.0, with many performance improvements, bug fixes, and new features, and native machine learning computation, right within the database."
source: "https://surrealdb.com/blog/release-v1-1-0"
cover: "../../assets/75ddc5f436c25d82.jpg"
---

# Release v1.1.0

![Release v1.1.0](../../assets/75ddc5f436c25d82.jpg)

Hello developers!

After months of hard work, we're excited to roll out v1.1.0.

This release is packed with features and improvements that we believe will make your development experience smoother and more efficient. From additional configuration flags, performance improvements, memory leak fixes, bug fixes, and new features, there's a lot to explore. We've also improved the internal memory allocators and released machine learning model computation powered by SurrealML. This release incorporates a number of contributions and feature suggestions from the community. For full release information, view the [release notes](/releases#v1-1-0).

Let's dive right into it and see what's new:

## Run machine learning models in SurrealQL

![Machine Learning with SurrealML](../../assets/b8b64fad4d27e2e3.jpg)

SurrealML is our first step towards bringing Machine Learning to the Surreal ecosystem. With the introduction of our own file format with metadata and versioning included within the file, machine learning models can be greatly simplified, ensuring reproducibility and consistency in machine learning pipelines.

Using the `surreal` command line tool, we can import our SurrealML models directly into SurrealDB, effortlessly. SurrealDB automatically reads and understands the model requirements, immediately setting up a custom in-built function which can be used to infer results from the model itself. Inference works with either raw data inputs, for advanced usage, or with the field-name key bindings, packaged into the SurrealML file format itself. Developers no longer have to use external platforms or systems to run model predictions against data residing in their database. Instead the model logic can sit directly within the SurrealQL language, extending the power of custom functions.

As with live queries, the real power comes when we combine this functionality with the other powerful features within SurrealQL. Model inference can now be used seamlessly within EVENTs, LIVE QUERIES, and custom functions, both as a traditional database backend, or connected to directly from the browser.

```surrealql
CREATE house_listing SET squarefoot_col = 500.0, num_floors_col = 1.0;
CREATE house_listing SET squarefoot_col = 1000.0, num_floors_col = 2.0;
CREATE house_listing SET squarefoot_col = 1500.0, num_floors_col = 3.0;

SELECT * FROM (
  SELECT
    *,
    ml::houses::price-prediction<1.0.0>({
      squarefoot: squarefoot_col,
      num_floors: num_floors_col
    }) AS price_prediction
  FROM house_listing
)
WHERE price_prediction > 177206.21875;
```

For more information regarding SurrealML, view the [documentation](/docs/surrealdb) and read the [blog](/blog/what-is-surrealml-a-getting-started-guide) post.

## Use live queries in the Rust SDK

![Live Queries in Rust](../../assets/5a661096b2fd0b0a.jpg)

This release introduces a new Live Query API to the Rust SDK, for powerful realtime updates in your Rust applications. By simply specifying `.live()` at the end of a `select()` query, you can receive a stream of changes, as they occur whtin a local or remote database.

```rust
// Select the namespace/database to use
db.use_ns("namespace").use_db("database").await?;

// Listen to all updates on a table
let mut stream = db.select("person").live().await?;

// Listen to updates on a range of records
let mut stream = db.select("person").range("jane".."john").live().await?;

// Listen to updates on a specific record
let mut stream = db.select(("person", "h5wxrf2ewk8xjxosxtyc")).live().await?;

// The returned stream implements `futures::Stream` so we can
// use it with `futures::StreamExt`, for example.
while let Some(result) = stream.next().await {
  handle(result);
}

// Handle the result of the live query notification
fn handle(result: Result<Notification<Person>>) {
  match result {
    Ok(notification) => println!("{notification:?}"),
    Err(error) => eprintln!("{error}"),
  }
}
```

## Improved string parsing functionality

Previously, any string within SurrealQL was parsed as a Record ID, Datetime, or UUID if they had the same format as one of those types. In this release, string prefixes allow you to decide what value a string holds, forcing it to be parsed as a raw string, or forcing it to be parsed as a specific type.

```surrealql
-- Interpeted as a record ID, because of the structure with the semicolon:
RETURN "5:20";
-- Forcefully parsed as just a string
RETURN s"5:20";

-- This will be a record ID.
RETURN r"person:john";
-- This fails, as it's not a valid record ID.
RETURN r"I am not a record ID";

-- Example for a date and a UUID.
RETURN d"2023-11-28T11:41:20.262Z";
RETURN u"8c54161f-d4fe-4a74-9409-ed1e137040c1";
```

We're excited to see what users will build with the new functionality and performance improvements introduced in this release. For questions, find us on [GitHub](https://github.com/surrealdb) and [Discord](https://discord.gg/surrealdb).
