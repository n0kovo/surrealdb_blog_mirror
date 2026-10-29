---
position: 15
title: ALTER SYSTEM
description: The ALTER SYSTEM statement is used to alter the entire datastore.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/system.mdx"
---

# `ALTER SYSTEM` statement

*Since v3.0.0*

The `ALTER SYSTEM` statement is used to alter the entire datastore. It can be used to compact the system, to set or drop a systemwide query timeout, or to set the compatibility level of new databases.

This statement is the only `ALTER` statement that does not have a corresponding `DEFINE` statement.

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER SYSTEM 
    COMPACT |
    QUERY_TIMEOUT @duration |
    DROP QUERY_TIMEOUT |
    COMPATIBILITY 3 | 4
```

  
**Railroad Diagram**

```
        ╭──────────────╮                   ╭─────────╮                      
├┼──────│ ALTER SYSTEM │───╮───────────────│ COMPACT │────────────────╭───┼┤
        ╰──────────────╯   │               ╰─────────╯                │     
                           │                                          │     
                           │    ╭───────────────╮     ┌───────────┐   │     
                           ╰────│ QUERY_TIMEOUT │─────│ @duration │───╯     
                           │    ╰───────────────╯     └───────────┘   │     
                           │                                          │     
                           │          ╭────────────────────╮          │     
                           ╰──────────│ DROP QUERY_TIMEOUT │──────────╯     
                           │          ╰────────────────────╯          │     
                           │                                          │     
                           │                              ╭───╮       │     
                           │                           ╭──│ 3 │──╮    │     
                           │                           │  ╰───╯  │    │     
                           │                           │         │    │     
                           │       ╭───────────────╮   │  ╭───╮  │    │     
                           ╰───────│ COMPATIBILITY │───╯──│ 4 │──╰────╯     
                                   ╰───────────────╯      ╰───╯
```

## `QUERY_TIMEOUT` clause

A query timeout can be set for the system as a whole. The minimum possible timeout is one millisecond, below which the value will be set as `NONE`.

```surql
ALTER SYSTEM QUERY_TIMEOUT 100ns;
INFO FOR ROOT.config;
```

```surql title="Output"
{ QUERY_TIMEOUT: NONE }
```

Any value above `1ms` will set the timeout, beyond which no query that takes any longer than this will succeed.

```surql
ALTER SYSTEM QUERY_TIMEOUT 1ms;
FOR $_ IN 0..1000 {
    FOR $_ IN 0..1000 {
        CREATE |person:1000|;
    }
};
```

```surql title="Output"
'The query was not executed because it exceeded the timeout: 1ms'
```

## `COMPATIBILITY` clause

*Since v4.0.0*

Sets the [compatibility level](../define/database.md#compatibility-level) that a database starts at when a `DEFINE DATABASE` statement does not give one. A datastore created by SurrealDB 4.0 starts new databases at level 4. One that a 3.x release created starts them at level 3, so that every database in it behaves the same way until the level is raised.

```surql
ALTER SYSTEM COMPATIBILITY 4;
```

The clause changes only databases defined afterwards. To change an existing database, use [`ALTER DATABASE`](database.md#compatibility).

## COMPACT clause

Compacts the entire datastore. To compact other resources, use [ALTER NAMESPACE](namespace.md) to compact the current namespace keyspace, [ALTER DATABASE](database.md) to compact the current database keyspace, or [ALTER TABLE](table.md) to compact a specific table keyspace.

The storage engine carries out the compaction. In SurrealDB 4.0, SurrealKV supports it: it writes recent changes to disk, merges the data files that hold the keys, and drops deleted data and old versions that no reader can see, which frees their space. The statement returns once the compaction is done, and reads and writes carry on meanwhile. Before 4.0, RocksDB was the only engine that supported compaction requests. The in-memory engine and TiKV do not support them, and return the following error:

```surql
'There was a problem with the key-value store: The storage layer does not support compaction requests.'
```

A successful compaction returns `NONE`.

```surql
ALTER SYSTEM COMPACT;
```

```surql title="Output"
NONE
```
