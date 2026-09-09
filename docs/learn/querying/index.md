---
position: 1
title: Querying
description: "SurrealQL, the SDKs and GraphQL: SQL-like syntax for SurrealDB. Graphs, links, and practical querying tips."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/index.mdx"
---

In this section we will learn about the multitude of ways to write and send queries to your SurrealDB database. The main focus is on the SurrealQL query language, which strongly resembles traditional SQL but differs in a number of ways to accommodate patterns such as graph traversal, record links, and other features unique to SurrealDB.

Queries can also be written without using direct SurrealQL through methods such as SDKs in your preferred programming language, [GraphQL](graphql/overview.md), or [GQL](gql/overview.md) (ISO graph pattern queries on the `/gql` endpoint). The [Postgres wire protocol](../../reference/rest-api/postgres-protocol.md) lets standard Postgres clients (`psql`, JDBC, etc.) connect and run SurrealQL or GQL with tabular results. Built-in [`eval::*`](../../reference/query-language/functions/database-functions/eval.md) functions can also run SurrealQL or GQL query strings from inside a transaction when explicitly enabled.

This section also includes tips and tricks to get the most out of your queries. For even more information after reading this section, feel free to look into the [reference](../../reference/query-language/index.md) section of the documentation which has separate pages for each statement, data type, clause and more for the entire SurrealQL query language.

## Concepts and guides

- [Parameterised queries](concepts-and-guides/parameterised-queries.md) - pass values as parameters instead of building query strings
- [Working with types](concepts-and-guides/working-with-types.md) - how values are typed, cast and asserted
- [Custom functions](concepts-and-guides/custom-functions.md) - name and reuse a query with `DEFINE FUNCTION`
- [Subqueries and advanced patterns](concepts-and-guides/subqueries-and-advanced-patterns.md) - nest queries and compose results
- [Transactions](concepts-and-guides/transactions.md) - group statements so they succeed or fail together
- [Idempotent operations](concepts-and-guides/idempotent-operations.md) - write statements that are safe to retry
- [Error handling](concepts-and-guides/error-handling.md) - what a failed statement returns, and how to react to it
- [Sequences](concepts-and-guides/sequences.md) - generate monotonic numbers without a race
- [Sessions and scoping](concepts-and-guides/sessions-and-scoping.md) - what a session carries, and how long it lasts
- [Query optimisation](concepts-and-guides/query-optimisation.md) - read a query plan and index for it
- [Bulk operations and data import](concepts-and-guides/bulk-operations-and-data-import.md) - load many records efficiently
- [Connecting from serverless & edge](concepts-and-guides/connecting-from-serverless-and-edge.md) - connection patterns where processes are short-lived
- [Representations and codecs](concepts-and-guides/representations-and-codecs.md) - how values are encoded over each protocol
- [Testing](concepts-and-guides/testing.md) - assert query results as part of a test suite

## Performance

- [Performance best practices](performance/performance-best-practices.md) - what to measure, and what usually costs the most

## Custom APIs

- [Middleware](custom-apis/middleware.md) - run code before and after a custom API handler
