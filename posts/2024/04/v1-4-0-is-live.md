---
title: "v1.4.0 is live! 🎉"
slug: "v1-4-0-is-live"
date: "2024-04-09T00:00:00.000Z"
categories:
  - "releases"
read_time: "2 min read"
summary: "This new release comes with bug fixes, performance improvements, and feature updates to -insert thing-"
source: "https://surrealdb.com/blog/v1-4-0-is-live"
cover: "../../assets/ae56ab96db78fe33.jpg"
---

# v1.4.0 is live! 🎉

![v1.4.0 is live! 🎉](../../assets/ae56ab96db78fe33.jpg)

We are excited to announce the release of SurrealDB 1.4.0. This release brings a number of improvements and bug fixes which can be seen in detail on our [releases page](/releases), and in the [documentation](/docs/surrealdb).

## Introduction of specialised table types

In previous versions of SurrealDB, developers could specify constraints on the `in` and `out` fields of a table, in order to ensure that a graph relationship was only able to be created between specific tables. This could lead to problems, as it was possible to insert normal record data into graph edge tables, leading to a breakdown in referential integrity.

```surrealql
DEFINE TABLE assigned_to SCHEMAFULL
    PERMISSIONS
        FOR create, select, update, delete
            WHERE in.owner == $auth.id AND out.author == $auth.id;

DEFINE FIELD in ON assigned_to TYPE record<tag>;
DEFINE FIELD out ON assigned_to TYPE record<sticky>;
```

With the addition of a new `TYPE` clause in SurrealDB 1.4.0, users can now specify that a table can store either normal records (with `TYPE NORMAL`), or edge relations (with `TYPE RELATION`), ensuring more strict control over the schema of a database. `IN` and `OUT` keywords can be used to ensure that the table can be constrained for only certain types of relationships.

A table can be either `TYPE RELATION` (allowing only for the storage of graph edges, or relations), `TYPE NORMAL` (allowing for the storage of normal records, or graph nodes), and `TYPE ANY` which allows for the original behaviour of storing any document or record type in the same table. If no table type is set, then due to SurrealDB's schemaless functionality, `TYPE ANY` will be used as the default option, allowing for any record type to be stored in the table.

As a consequence, the previous example can now be shortened to the following, whilst improving the database behaviour:

```surrealql
DEFINE TABLE assigned_to SCHEMAFULL TYPE RELATION IN tag OUT sticky
    PERMISSIONS
        FOR create, select, update, delete
            WHERE in.owner == $auth.id AND out.author == $auth.id;
```

## Bulk insert support in the Rust SDK

This was one of the frequently requested features. While this was already possible using the `query` method, in SurrealDB 1.4.0, we have added an `insert` method that makes it more convenient.

```rust
db.insert(Resource::from("person"))
    .content(vec![
        User {
            id: thing("person:tobie")?,
            name: "Tobie",
            settings: Settings {
                active: true,
                marketing: false,
            },
        },
        User {
            id: thing("person:jaime")?,
            name: "Jaime",
            settings: Settings {
                active: true,
                marketing: true,
            },
        },
    ])
    .await?;
```

## But wait, there's more!

There are of course other great things, and bugfixes, we've included in this release, which we have not covered here. To see more examples and improvements [check out our release notes](/releases), and [documentation](/docs/surrealdb).
