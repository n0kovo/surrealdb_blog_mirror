---
position: 30
title: USE
description: The USE statement specifies a namespace and / or a database to use for the subsequent SurrealQL statements when switching between namespaces and databases.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/use.mdx"
---

# `USE` statement

The `USE` statement specifies a namespace and / or a database to use for the subsequent SurrealQL statements when switching between namespaces and databases. If you have a single namespace and database, you can define them in the [sql command](../../cli/db/commands/sql.md#example-usage).

Ensure that your database and namespace exist and you have [started your database](../../cli/db/commands/start.md) before using the Sql command option.

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
USE [ NS @ns ] [ DB @db ];
```

  
**Railroad Diagram**

```
                  ╭─────────────────────────╮ ╭─────────────────────────╮               
                  │                         │ │                         │               
        ╭─────╮   │    ╭────╮     ┌─────┐   │ │    ╭────╮     ┌─────┐   │   ╭───╮       
├┼──────│ USE │───╯────│ NS │─────│ @ns │───╰─╯────│ DB │─────│ @db │───╰───│ ; │─────┼┤
        ╰─────╯        ╰────╯     └─────┘          ╰────╯     └─────┘       ╰───╯
```

## Example usage

The following query shows example usage of this statement if you have multiple namespaces and databases.

```surql
/**[test]

[[test.results]]
value = "{ database: 'test', namespace: 'test' }"

*/

USE NS test; -- Switch to the 'main' Namespace
```

```surql
/**[test]

[[test.results]]
value = "{ database: 'test', namespace: 'test' }"

*/

USE DB test; -- Switch to the 'main' Database
```

```surql
/**[test]

[[test.results]]
value = "{ database: 'test', namespace: 'test' }"

*/

USE NS test DB test; -- Switch to the 'main' Namespace and 'main' Database
```

You can also use the [INFO Statement](info.md) to check the current namespace and database.

```surql
INFO FOR NS; -- Check the current Namespace
```

```surql
INFO FOR DB; -- Check the current Database
```

## `USE` statement behaviour when resource does not exist

*Since v3.0.0*

A `USE` statement creates the namespace or database that it names if it does not exist yet, as long as the user has permission to define it. A misspelled name therefore creates a new, empty namespace or database, and the statement succeeds.

```surql
USE NS typo DB typo;
//- { database: 'typo', namespace: 'typo' }

(INFO FOR ROOT).namespaces.typo;
//- 'DEFINE NAMESPACE typo'
```

A user who cannot define the namespace or database, such as a user with the `VIEWER` role, also gets a successful result from `USE`, but nothing is created. The [`STRICT`](define/database.md#defining-a-strict-database) clause of `DEFINE DATABASE` applies to the tables inside a database, and does not change what `USE` does.

The namespace and database named in the `surreal-ns` and `surreal-db` headers of an [HTTP request](../../rest-api/http-protocol.md) are not created in this way. A query that uses a namespace or database that does not exist fails with an error such as `The namespace 'mian' does not exist`.

## Value returned by `USE` statement

*Since v3.0.0*

Before SurrealDB 3.0.0, the output of a `USE` statement was `NONE`. Since then, each `USE` statement returns an object containing the current namespace and database.

```surql
USE NS main;
```

```surql title="Output"
{ database: 'main', namespace: 'main' }
```
