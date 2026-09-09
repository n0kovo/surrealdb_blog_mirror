---
position: 1
title: SurrealQL
description: SurrealQL statements, clauses, functions and language primitives. The full reference for the SurrealDB query language.
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

## Clauses

- [Clauses](clauses/overview.md) - the clauses statements share, such as `WHERE`, `LIMIT`, `START` and `OMIT`

## Language primitives

Reference pages for the pieces a query is built from:

- [Statements](language-primitives/statements.md) - what a statement is, and how several combine into one query
- [Comments](language-primitives/comments.md) - the three comment forms SurrealQL accepts
- [Data types](language-primitives/data-types/index.md) - every value type, from records to geometries
- [Operators](language-primitives/operators.md) - comparison, arithmetic, set and graph operators
- [Casting](language-primitives/casting.md) - converting a value from one type to another
- [Idioms](language-primitives/idioms.md) - path syntax for reaching into records and graphs
- [Parameters](language-primitives/parameters.md) - built-in parameters and your own
- [Formatters](language-primitives/formatters.md) - formatting datetimes and numbers
- [Record links](language-primitives/record-links.md) - pointing at another record
- [Record references](language-primitives/record-references.md) - links the database keeps in step for you

## Machine learning

- [ML functions](functions/ml-functions/functions.md) - call a stored model from a query
