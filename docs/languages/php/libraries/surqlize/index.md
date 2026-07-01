---
position: 1
title: Overview
description: Surqlize is an object-relational mapper for SurrealDB in PHP, built on version 2 of the SDK, with attribute-driven models, a typed query builder, graph relations, and schema tooling.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/libraries/surqlize/index.mdx"
---

# Surqlize (ORM)

[Surqlize](https://github.com/surrealdb/surqlize.php) is an object-relational mapper for SurrealDB in PHP. You describe tables as PHP classes with attributes, then compose SurrealQL through a typed query builder instead of writing strings. It is built on top of [version 2 of the SDK](../../v2/index.md) and uses the SDK to execute queries.

The core idea is small: describe your SurrealDB tables with models and attributes, then build queries through typed PHP APIs that your IDE and static analyser understand. Surqlize compiles each query to a deterministic SurrealQL string for tests, and runs it through the SDK with parameter-bound values at runtime.

> [!IMPORTANT]
> Surqlize is published as `0.0.1-alpha.2` and is in early development. It requires PHP `8.4` and depends on the alpha [v2 SDK](../../v2/index.md), so its API may change.

## Getting started

- **[Installation](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/installation)** — Install Surqlize with Composer and the alpha SDK it depends on.
- **[Models](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/models)** — Describe tables as PHP classes with attribute-driven fields.
- **[Connections](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/connections)** — Register an SDK executor and inject one per query when needed.

## Building queries

- **[Querying](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/querying)** — Typed select, where, ordering, projections, and the execution methods.
- **[Mutations](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/mutations)** — Create, update, upsert, and delete with model helpers and builders.
- **[Edges and graph](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/edges-and-graph)** — Edge models, graph traversal, and RELATE.
- **[Search, vector, and geometry](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/search-vector-geometry)** — Full-text search, vector KNN, and geometry helpers.

## Schema and tooling

- **[Schema](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/schema)** — Define tables with a schema contract or the fluent DSL.
- **[Code generation and CLI](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/code-generation-and-cli)** — Generate typed field adapters and run the CLI commands.
- **[Transactions](https://surrealdb.com/docs/languages/php/ecosystem/surqlize/transactions)** — Batch ORM queries into a single transaction with rollback.

## Sources

- [GitHub repository](https://github.com/surrealdb/surqlize.php)
- [PHP SDK v2](../../v2/index.md) that Surqlize builds on
- [Laravel integration](../../frameworks/laravel/index.md) for using Surqlize in Laravel
