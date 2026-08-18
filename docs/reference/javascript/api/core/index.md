---
position: 1
title: Core classes
description: "The connection, session, transaction, and query execution classes that make up the SDK's core surface."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/api/core/index.mdx"
---

# Core classes

The core classes cover connecting to SurrealDB, scoping work to a session or a transaction, and executing queries. Every other part of the SDK is reached through one of these.

## Classes

- [**Surreal**](surreal.md) - The main entry point for connecting to and interacting with a SurrealDB instance.
- [**SurrealSession**](surreal-session.md) - Session-scoped context with authentication and query execution.
- [**SurrealQueryable**](surreal-queryable.md) - The query execution methods shared by sessions and transactions.
- [**SurrealTransaction**](surreal-transaction.md) - Atomic transaction support for executing multiple queries.
- [**SurrealApi**](surreal-api.md) - Methods for invoking user-defined API endpoints.

## See also

- [Query builders](../queries/index.md) - The builder returned by each query method
- [Data types](../values/index.md) - Value classes used in queries and results
- [Errors](../errors/index.md) - Error classes raised by these methods
