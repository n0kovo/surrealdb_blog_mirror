---
position: 1
title: ALTER
description: The ALTER statement can be used to change the behaviour of database resources.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/overview.mdx"
---

# `ALTER` statement

The `ALTER` statement can be used to change the behaviour of database resources.

There are two main cases in which to use an `ALTER` statement:

* Modifying previously defined resources. This can currently be used to modify tables and fields. For other such modifications, use the `OVERWRITE` clause in other `DEFINE` statements.
* Modifying other resources using clauses not present in other `DEFINE` statements. Examples of this are the `PREPARE REMOVE` clause to prepare an index for removal, the `COMPACT` clause to compact the system/namespace/database/single table, and the `QUERY_TIMEOUT` clause to define or drop the query timeout for the entire datastore.

Each resource has its own `ALTER` statement:

| Statement | Alters |
| --- | --- |
| [`ALTER ACCESS`](access.md) | An existing access method |
| [`ALTER ANALYZER`](analyzer.md) | An existing analyzer |
| [`ALTER API`](api.md) | An existing API definition |
| [`ALTER BUCKET`](bucket.md) | An existing bucket |
| [`ALTER CONFIG`](config.md) | Authentication access and GraphQL behaviour |
| [`ALTER DATABASE`](database.md) | The current database |
| [`ALTER EVENT`](event.md) | An existing event |
| [`ALTER FIELD`](field.md) | A field's clauses, or drop them entirely |
| [`ALTER FUNCTION`](function.md) | An existing custom function |
| [`ALTER INDEX`](indexes.md) | An index on a table, including `PREPARE REMOVE` |
| [`ALTER NAMESPACE`](namespace.md) | The current namespace |
| [`ALTER PARAM`](param.md) | An existing parameter |
| [`ALTER SEQUENCE`](sequence.md) | An existing sequence |
| [`ALTER SYSTEM`](system.md) | The entire datastore, including `QUERY_TIMEOUT` |
| [`ALTER TABLE`](table.md) | A table's schema, such as moving from schemaless to schemafull |
| [`ALTER USER`](user.md) | An existing database, namespace or root user |

Some examples of `ALTER` statements are as follows.

## Modify a table schema

When starting a new project, you may require a table to be schemaless to allow for flexibility in the data structure. However, as the project progresses, you may want to lock down the schema to prevent new fields from being added.

An example of `ALTER` to modify an existing table:

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "NONE"

[[test.results]]
value = "[{ id: user:317esn5r3spd4em0lfze, name: 'LordofSalty' }]"
skip-record-id-key = true

[[test.results]]
value = "NONE"

*/

DEFINE TABLE user SCHEMALESS;
DEFINE FIELD name ON TABLE user TYPE string;
CREATE user SET name = "LordofSalty";

-- Now make it schemafull to ensure that no other fields can be used
ALTER TABLE user SCHEMAFULL;
```

## Modify table permissions

You can also use the `ALTER` statement to change a table's permissions. An `ALTER` statement only needs to include the items to be altered, not the entire definition.

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "NONE"

*/

-- Will show up as DEFINE TABLE user TYPE ANY SCHEMAFULL PERMISSIONS NONE
DEFINE TABLE user SCHEMAFULL;

-- Now defined as DEFINE TABLE user TYPE ANY SCHEMAFULL PERMISSIONS FULL
ALTER TABLE user PERMISSIONS FOR create FULL;
```

## Using `IF EXISTS` clause

You can use the' IF EXISTS' clause to prevent an error from occurring when trying to alter a table that does not exist.

```surql
/**[test]

[[test.results]]
value = "NONE"

*/

ALTER TABLE IF EXISTS user SCHEMAFULL;
```
