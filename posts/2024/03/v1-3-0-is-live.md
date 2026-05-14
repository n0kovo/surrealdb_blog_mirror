---
title: "v1.3.0 is live! 🎉"
slug: "v1-3-0-is-live"
date: "2024-03-12T00:00:00.000Z"
categories:
  - "releases"
read_time: "2 min read"
summary: "This new release comes with bug fixes, performance improvements, and feature updates to our define & remove statements and KNN syntax."
source: "https://surrealdb.com/blog/v1-3-0-is-live"
cover: "../../assets/47546a9c31a1138b.jpg"
---

# v1.3.0 is live! 🎉

![v1.3.0 is live! 🎉](../../assets/47546a9c31a1138b.jpg)

We are constantly improving the experience of using SurrealDB and in this release, we have been working on improving the schemafull experience.

## Better schemafull experience

`DEFINE` statements now allow you to include an `IF NOT EXISTS` clause which ensures that the define statement is only run if the resource doesn't already exist. If it exists, you will get an error.

```surrealql
DEFINE DATABASE IF NOT EXISTS blog
```

This brings us more in line with how things work in the SQL databases you might be familiar with.

We've also added an `IF EXISTS` clause to the `REMOVE` statement, which will only remove the resource if it exists.

```surrealql
REMOVE DATABASE IF EXISTS blog;
```

This along with improving error messages and more consistent handling of negative numbers in record IDs, are just a few examples of the various ways we are taking your feedback and improving the developer experience.

## Improved KNN syntax

In addition to improving the schemafull experience, we have also made improvements to the KNN Syntax, with the KNN operator now supporting a new syntax using \<| and |> instead of < and >.

```surrealql
SELECT id FROM point WHERE point_b <|2|> [2, 3, 4, 5]
```

This helps differentiate it from our other features that also use the < and > syntax, such as type-casting.

## Sometimes it's better to wait

The last thing to highlight here is that it's now possible to initialise a SurrealDB connection and run setup actions like authentication and selecting the database concurrently with other queries by making it possible to wait for the SDK to connect or select the database to use before allowing other queries to execute.

This is done with the new `Surreal::wait_for` syntax.

```rust
use surrealdb::opt::WaitFor::Connection;

// This will wait until the connection is established.
// As soon as it is, it will return and allow the client to continue.
DB.wait_for(Connection).await;

// This will still likely return an error.
// While we know that the connection is already established at this point,
// there is no guarantee that the database has already been selected.
// This query requires the database to be selected first.
DB.create(Resource::from("person")).await?;
```

This would protect you against potential race conditions that you might have been susceptible to before:

```rust
// A static, global instance of the client
static DB: Lazy<Surreal<Any>> = Lazy::new(|| {
    // Connect and setup the database connection in the background
    tokio::spawn(async {
        // This example is for demonstration purposes only.
        // If the `unwrap` panics the client will be left hanging,
        // waiting for the setup to happen when using `Surreal::wait_for`.
        setup_db().await.unwrap();
    });
    // Initialise a new unconnected instance of the client
    Surreal::init()
});

// Connect to the server and run setup actions
async fn setup_db() -> surrealdb::Result<()> {
    // Connect to the server
    DB.connect("ws://localhost:8000").await?;

    // Signin as a namespace, database, or root user
    DB.signin(Root {
        username: "root",
        password: "root",
    }).await?;

    // Select a specific namespace / database
    DB.use_ns("namespace").use_db("database").await?;

    Ok(())
}

// Whether this would run successfully or return an error would depend on whether
// `DB::setup` was able to execute before getting to this point.
DB.create(Resource::from("person")).await?;
```

## But wait, there's more!

There are of course other great things we've included in this release, which we have not covered here. To see more examples and improvements [check out our release notes](/releases), [documentation](/docs/surrealdb) and [livestream.](https://www.youtube.com/watch?v=kQQV2kDFHQA)
