---
position: 1
title: Schema management
description: "How to shape data in SurrealDB: tables, fields, indexes, events, tenancy, and related patterns."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/schema-management/index.mdx"
---

# Schema management

Schema management is where you describe what lives in the database: tables and fields, indexes, events, optional files and buckets, and the namespace / database layout for multi-tenant setups.

What makes SurrealDB convenient is that schema management can be almost entirely dispensed with at the outset, because standard CRUD (Create, Read, Update, Delete) operations do not require a schema to be defined at the outset. This allows you to experiment at your leisure until it is time to firm up your database's expected record and data types, at which point schema definition comes to the fore.

Schema is not all about defining data, however. For example, statements like [`DEFINE EVENT`](../../reference/query-language/statements/define/event.md) set up effects that take place after a statement is executed.

The learn pages here explain how and why to use these pieces together. For exact statement grammar, defaults, and edge cases, use the SurrealQL reference ([`DEFINE`](../../reference/query-language/statements/define/overview.md) and related pages).

If you are new to SurrealDB, it helps to read [tables](tables-and-fields/tables.md) and [fields](tables-and-fields/fields-and-validation.md) first, then [indexes](indexes/index-types-and-strategies.md) and [events](events-and-triggers/defining-events.md) when you need behaviour beyond simple storage.

For managing schema files across environments, synchronising locally and running phased rollouts in production, see [SurrealKit schema migration](../../manage/schema-migration/index.md).
