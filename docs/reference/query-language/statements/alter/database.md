---
position: 2
title: ALTER DATABASE
description: The ALTER statement can be used to change authentication access and behaviour, global parameters, table configurations, table events, schema definitions, and indexes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/database.mdx"
---

*Since v3.0.0*

The `ALTER DATABASE` statement can be used to modify the database. `ALTER DATABASE` is used on the current database, which is why a `IF EXISTS` clause does not exist.

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER DATABASE COMPACT
```

  
**Railroad Diagram**

```
        ╭────────────────╮     ╭─────────╮       
├┼──────│ ALTER DATABASE │─────│ COMPACT │─────┼┤
        ╰────────────────╯     ╰─────────╯
```

## COMPACT

Performs storage compaction on the current database keyspace. To compact other resources, use [ALTER SYSTEM](system.md) to compact the entire datastore, [ALTER NAMESPACE](namespace.md) to compact the current namespace keyspace, or [ALTER TABLE](table.md) to compact a specific table keyspace.

The actual compaction used will depend on the datastore, such as RocksDB or SurrealKV.

This clause will not work with in-memory storage which has nothing persistent to compact, producing the following error:

```surql
'The storage layer does not support compaction requests.'
```

A successful compaction will return `NONE`.

```surql
ALTER DATABASE COMPACT;
-- NONE
```

## See also

* [`DEFINE DATABASE`](../define/database.md)
