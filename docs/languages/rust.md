---
position: 9
title: Rust
description: Connect to SurrealDB and run your first queries with the Rust SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/rust.mdx"
---

# Getting started

The Rust SDK for SurrealDB lets you connect to a database and query it from your application. This guide covers connecting, authenticating, and running your first queries.

## 1. Install the SDK

Create a new project using `cargo new` and add the [`surrealdb`](https://crates.io/crates/surrealdb) crate along with [`tokio`](https://crates.io/crates/tokio), which lets you use the database inside an `async fn main()`. Enabling the `macros` and `rt-multi-thread` features on `tokio` allows the `#[tokio::main]` attribute to be used on top of `fn main()`.

The two main ways to connect to SurrealDB when getting started are by connecting to a running instance via the `protocol-ws` feature, or by running an embedded instance in memory using the `kv-mem` feature. Each of these can be added via a feature flag in the SDK.

```sh
cargo new my_project
cd my_project
cargo add surrealdb --features kv-mem,protocol-ws
cargo add tokio --features macros,rt-multi-thread
```

Once installed, import the SDK's types into `src/main.rs`.

```rust
use surrealdb::engine::remote::ws::Ws;
use surrealdb::opt::auth::Root;
use surrealdb::Surreal;
```

## 2. Connect to SurrealDB

Use [`Surreal::new`](../reference/rust/methods/new.md) with the `Ws` engine to connect to a running SurrealDB instance, then [`signin`](../reference/rust/methods/signin.md) to authenticate and [`use_ns`/`use_db`](../reference/rust/methods/use.md) to select the namespace and database you want to work with. Most operations require both.

Supported connection protocols include:
- **WebSocket** (`ws://`, `wss://`) via the `protocol-ws` feature, for long-lived stateful connections
- **HTTP** (`http://`, `https://`) for short-lived stateless connections
- **Memory/embedded** (`mem://`) via the `kv-mem` feature, for [embedded instances](../reference/rust/embedding.md)

```rust
#[tokio::main]
async fn main() -> surrealdb::Result<()> {

    // Connect to the server
    let db = Surreal::new::<Ws>("127.0.0.1:8000").await?;

    // Signin as a namespace, database, or root user
    db.signin(Root {
        username: "root".to_string(),
        password: "secret".to_string(),
    })
    .await?;

    // Select a specific namespace / database
    db.use_ns("main").use_db("main").await?;

    Ok(())
}
```

## 3. Inserting data into SurrealDB

Once connected, you can use [`create`](../reference/rust/methods/create.md) to create records. The most ergonomic way to pass data to and from the database is to use a struct that derives [`SurrealValue`](https://docs.rs/surrealdb/latest/surrealdb/types/trait.SurrealValue.html), which allows for both serialisation and deserialisation between the Rust code and the database.

```rust
use surrealdb::Surreal;
use surrealdb::engine::remote::ws::Ws;
use surrealdb::opt::auth::Root;
use surrealdb::types::{RecordId, SurrealValue};

#[derive(Debug, SurrealValue)]
struct Name {
    first: String,
    last: String,
}

#[derive(Debug, SurrealValue)]
struct Person {
    title: String,
    name: Name,
    marketing: bool,
}

#[derive(Debug, SurrealValue)]
struct Record {
    id: RecordId,
}

#[tokio::main]
async fn main() -> surrealdb::Result<()> {
    let db = Surreal::new::<Ws>("127.0.0.1:8000").await?;

    db.signin(Root {
        username: "root".to_string(),
        password: "secret".to_string(),
    })
    .await?;

    db.use_ns("main").use_db("main").await?;

    // Create a new person with a random id
    let created: Option<Record> = db
        .create("person")
        .content(Person {
            title: "Founder & CEO".to_string(),
            name: Name {
                first: "Tobie".to_string(),
                last: "Morgan Hitchcock".to_string(),
            },
            marketing: true,
        })
        .await?;
    dbg!(created);

    Ok(())
}
```

## 4. Retrieving data from SurrealDB

### Selecting records

The [`select`](../reference/rust/methods/select.md) method retrieves all records from a table. Deserialize the result into a `Vec` of a struct that derives `SurrealValue`.

```rust
// Select all people records
let people: Vec<Record> = db.select("person").await?;
dbg!(people);
```

### Running SurrealQL queries

For more advanced use cases, you can use the [`query`](../reference/rust/methods/query.md) method to run [SurrealQL](../reference/query-language/index.md) statements directly. Use [`.bind()`](../reference/query-language/language-primitives/parameters.md) to safely pass dynamic values, and [`.take()`](../reference/rust/methods/query.md) to transform a query result into anything that can be deserialized, in this case a `Value`.

```rust
use surrealdb::types::Value;

// Perform a custom advanced query
let mut groups = db
    .query("SELECT marketing, count() FROM type::table($table) GROUP BY marketing")
    .bind(("table", "person"))
    .await?;
dbg!(groups.take::<Value>(0).unwrap());
```

## 5. Closing the connection

Rust has no explicit close method. The connection is closed automatically when the `Surreal` client is dropped, for example when it goes out of scope at the end of your function.

## Next steps

You have learned how to install the SDK, connect to SurrealDB, create records, and retrieve data. There is a lot more you can do with the SDK, including updating and deleting records, authentication, live queries, and transactions.

- **[Authentication](../reference/rust/concepts/authenticating-users.md)** — Read more about authentication levels and how to integrate them into your application.
- **[Live queries](../reference/rust/concepts/live.md)** — Learn how to subscribe to real-time changes in your data with live queries.
- **[Embedding SurrealDB](../reference/rust/embedding.md)** — Run SurrealDB in memory or on disk directly inside your Rust application.
- **[API Reference](../reference/rust/methods/index.md)** — Complete reference for all methods, types, and errors.

> [!NOTE]
> This getting-started guide covers the essentials. For the complete methods, API, and concept reference, see the [Rust SDK reference](../reference/rust/index.md).
