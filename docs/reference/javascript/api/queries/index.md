---
position: 1
title: Query builders
description: "The chainable builder classes returned by the SDK's query methods."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/api/queries/index.mdx"
---

# Query builders

Query methods on a session or transaction return a builder rather than a plain promise. Each builder exposes chainable methods for configuring the operation, and is awaited to execute it.

## Builders

- [**SelectPromise**](select-promise.md) - Configures `SELECT` queries.
- [**CreatePromise**](create-promise.md) - Configures `CREATE` operations.
- [**UpdatePromise**](update-promise.md) - Configures `UPDATE` operations.
- [**UpsertPromise**](upsert-promise.md) - Configures `UPSERT` operations (insert or replace).
- [**InsertPromise**](insert-promise.md) - Configures `INSERT` operations.
- [**DeletePromise**](delete-promise.md) - Configures `DELETE` operations.
- [**RelatePromise**](relate-promise.md) - Configures `RELATE` operations for graph relationships.
- [**Query**](query.md) - Executes raw SurrealQL, with streaming and batch processing support.
- [**LivePromise**](live-promise.md) - Manages real-time live query subscriptions.
- [**RunPromise**](run-promise.md) - Executes SurrealDB functions and SurrealML models.
- [**ApiPromise**](api-promise.md) - Executes user-defined API calls.

## See also

- [Core classes](../core/index.md) - The classes these builders are created from
- [Executing queries](../../concepts/executing-queries.md) - Conceptual overview with examples
- [SurrealQL statements](../../../query-language/statements/overview.md) - The query language reference
