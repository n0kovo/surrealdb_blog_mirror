---
position: 10
title: Learn
description: "How SurrealDB stores, queries and secures data: SurrealQL and schema. The document, graph, vector and time-series models, and access control."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/learn.mdx"
---

# Learn

This section covers what SurrealDB does and how to tell it what you want. It is the conceptual half of the documentation: each page explains a mechanism and shows it working, rather than listing every option. The exhaustive syntax lives in [the reference](reference.md).

- **[Querying](learn/querying/index.md)** — Mutate and query your data with SurrealQL, the SDKs, or GraphQL.
- **[Schema management](learn/schema-management/index.md)** — Define namespaces, tables, fields, indexes, events and functions.
- **[Data models](learn/data-models/index.md)** — Store documents, graphs, vectors, time series and geospatial data in one engine.
- **[Security](learn/security/index.md)** — Authentication, access methods, row-level permissions and capabilities.
- **[Extensions](learn/extensions/index.md)** — Extend the database with custom functions, modules and WASM plugins.
- **[SurrealDB Agent Memory](https://surrealdb.com/docs/agent-memory)** — The memory and knowledge layer for AI agents, built on SurrealDB.

## Where to start

Reading order depends on what you are building. For an application backend, [querying](learn/querying/index.md) then [schema management](learn/schema-management/index.md) covers most of what you need. For a data model that spans relations and graph edges, start at [data models](learn/data-models/index.md). Anything that will hold user data wants [security](learn/security/index.md) before it ships.
