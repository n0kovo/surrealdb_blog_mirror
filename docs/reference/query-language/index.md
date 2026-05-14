---
position: 1
title: SurrealQL
description: "Reference for SurrealQL, SurrealDB's query language: statements, clauses, functions, and language primitives."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/index.mdx"
---

# SurrealQL

SurrealQL is SurrealDB's query language. Syntax is broadly SQL-like, with extensions for nested fields, graph edges, record IDs, and other SurrealDB-specific constructs.

For a guided introduction, see [Learn: Querying](../../learn/querying/index.md).

## Examples

A minimal query can follow a familiar SQL shape:

```surql
SELECT name,
       metadata
FROM   user
WHERE  age >= 18; 
```

Projections can include nested objects and graph traversals:

```surql
SELECT name,
       metadata.{
          date_registered,
          last_login
       },
       ->wrote->post AS posts
FROM user
WHERE age >= 18;
```

Further detail is organised under [Statements](statements/overview.md) and the other sections in this reference.
