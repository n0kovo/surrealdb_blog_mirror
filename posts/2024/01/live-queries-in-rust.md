---
title: "Live Queries in Rust"
slug: "live-queries-in-rust"
date: "2024-01-10T00:00:00.000Z"
categories:
  - "tutorials"
  - "engineering"
read_time: "4 min read"
summary: "SurrealDB comes with a LIVE SELECT statement that allows you to listen for creations, updates and deletions to specific records you are interested in or entire tables."
source: "https://surrealdb.com/blog/live-queries-in-rust"
cover: "../../assets/59ad14f2f05bd8c7.jpg"
---

# Live Queries in Rust

![Live Queries in Rust](../../assets/59ad14f2f05bd8c7.jpg)

SurrealDB comes with a `LIVE SELECT` [statement](/docs/surrealql/statements/live) that allows you to listen for creations, updates and deletions to specific records you are interested in or entire tables. While you could already take advantage of this powerful feature with our JavaScript SDK or WebSockets, the Rust SDK [added an API for it in v1.1.0](https://docs.rs/surrealdb-beta/1.1.0/surrealdb/method/struct.Select.html#method.live).

The Rust API for live queries builds on top of the already existing `select` method by simply adding a `live` method which converts the select query into a live select one. It works seamlessly with our current API, so you can use it with single records, a range of records, or entire tables. Unlike the normal select method which returns either a single result or a vector of results, it returns a stream of notifications. This works for the WebSocket engine and the local ones (the key value stores you can embed in your app). The only engine not yet supported is the HTTP one.

In this article, we show some examples of running live queries via the Rust SDK. We will skip imports for brevity but your IDE and/or the Rust compiler should give you the correct suggestions. Please refer to [this example](https://github.com/surrealdb/surrealdb/blob/8e9bd3a2d6289118a79822a48e2c45541020dfdf/lib/examples/live/main.rs) in our repo for a full, working example.

## Getting Started

```rust
// Connect to a WebSocket endpoint
// We are using the WebSocket engine for this example but you can also
// use a local engine embeded in your app.
let db = Surreal::new::<Ws>("localhost:8000").await?;

// Signin as a namespace, database, or root user
db.signin(Root {
  username: "root",
  password: "root",
})
.await?;

// Select a specific namespace / database
db.use_ns("namespace").use_db("database").await?;
```

Once you have signed into your server and selected the namespace and database to use, you are ready to start sending queries to your database.

## Listening for Changes on a Table

```rust
// Listen to all updates on the person table
let mut stream = db.select("person").live().await?;
```

This query listens to all changes made on the `person` table and returns a stream of notification results. Since the Rust SDK automatically deserialises responses on your behalf, you will either need to give the compiler a way to infer the response type of the notifications, or manually tell it what the response type should be. There are multiple ways to do this. The best one for you will depend on how you structure the rest of your code. In this article, we are going to process responses from a function. This allows the compiler to infer the type from the function parameter.

Let’s define a `handle` function that simply prints out the [notification](https://docs.rs/surrealdb-beta/1.1.2/surrealdb/struct.Notification.html) results:

```rust
// Handle the result of the live query notification
fn handle(result: Result<Notification<Person>>) {
    match result {
        Ok(notification) => println!("{notification:?}"),
        Err(error) => eprintln!("{error}"),
    }
}
```

`Person`, in this case, is what you expect the records coming from the database to deserialise into. This means that it must implement `serde::Deserialise`. `notification.action` will tell you whether the action that triggered this notification was a creation, update or deletion. `notification.data` will contain your deserialised object, `Person` in this particular case.

With this out of the way, we can now listen to changes being made on the table and process them in real time.

```rust
// The returned stream implements `futures::Stream` so we can
// use it with `futures::StreamExt`
while let Some(result) = stream.next().await {
    handle(result);
}
```

If you do not care about strong types for your particular use case or you simply want to try out the feature, you can use `surrealdb::opt::Resource` as your select parameter. This makes the compiler infer that the response type will be `surrealdb::sql::Value` so you won’t need to define it in that case.

```rust
// Listen to all updates on the person table
let mut stream = db.select(Resource::from("person")).live().await?;

// The returned stream implements `futures::Stream` so we can
// use it with `futures::StreamExt`
while let Some(notification) = stream.next().await {
    println!("{notification:?}");
}
```

That’s all you need when using `Resource`. It doesn’t return a result because `Value`s are not deserialised first and if a notification itself can’t be deserialised from a remote server, it can’t be routed anyway. `surrealdb::sql::Value` is the internal type SurrealDB uses so it’s returned as is. This is not unique to live queries or new to this release. Resources can be used with any CRUD method.

## Listening for Changes on a Range of Records

Listening on a range of records is simply a matter of using the `range` method on a select query before calling `live` on it.

```rust
let mut stream = db.select(Resource::from("person"))
    // This is a range on the `id` of the person
    .range("jane".."john")
    .live()
    .await?;

while let Some(notification) = stream.next().await {
    println!("{notification:?}");
}
```

Again, we are using `Resource` as a parameter here for brevity but the first approach works too. the only difference with this code is the `range` method. This supports the full range syntax that Rust supports; `start..end`, `start..`, `..`, `start..=end`, `..end` and `..=end`. You can also specify the bounds manually using the [Bound](https://doc.rust-lang.org/std/ops/enum.Bound.html) enum directly, `(start, end)`, for extra flexibility.

## Listening to Changes on a Single Record

As you may have guessed already, listening to changes on a particular `Person` record is not much different from what we have done so far. In this case, we simply need to listen on a record ID instead of a table.

```rust
// Listen only to changes happening to John's data
let mut stream = db.select(Resource::from(("person", "john")).live().await?;

while let Some(notification) = stream.next().await {
    println!("{notification:?}");
}
```

## Conclusion

If you need to listen to changes happening to your data in real-time, live queries are a powerful feature that enables you to do this. They integrate seamlessly with the Rust SDK allowing you to take advantage of the other SurrealDB features like authentication and permissions. The SDK also manages creating and closing the query for you automatically. As you may have noticed, we did not need to manually close the stream after using it. It’s automatically closed when the stream is dropped. Do try out the Live Queries in the Rust SDK & share your experience in our [community on Discord](https://discord.gg/surrealdb)!
