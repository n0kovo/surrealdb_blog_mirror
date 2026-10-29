---
position: 12
title: ALTER NAMESPACE
description: The ALTER NAMESPACE statement can be used to modify the namespace.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/namespace.mdx"
---

# `ALTER NAMESPACE` statement

*Since v3.0.0*

The `ALTER NAMESPACE` statement can be used to modify the namespace. `ALTER NAMESPACE` is used on the current namespace, which is why a `IF EXISTS` clause does not exist.

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER NAMESPACE COMPACT
```

  
**Railroad Diagram**

```
        ╭─────────────────╮     ╭─────────╮       
├┼──────│ ALTER NAMESPACE │─────│ COMPACT │─────┼┤
        ╰─────────────────╯     ╰─────────╯
```

## COMPACT

Performs storage compaction on the current namespace keyspace. To compact other resources, use [ALTER SYSTEM](system.md) to compact the entire datastore, [ALTER DATABASE](database.md) to compact the current database keyspace, or [ALTER TABLE](table.md) to compact a specific table keyspace.

The storage engine carries out the compaction. In SurrealDB 4.0, SurrealKV supports it: it writes recent changes to disk, merges the data files that hold the keys, and drops deleted data and old versions that no reader can see, which frees their space. The statement returns once the compaction is done, and reads and writes carry on meanwhile. Before 4.0, RocksDB was the only engine that supported compaction requests. The in-memory engine and TiKV do not support them, and return the following error:

```surql
'There was a problem with the key-value store: The storage layer does not support compaction requests.'
```

A successful compaction returns `NONE`.

```surql
ALTER NAMESPACE COMPACT;
```

```surql title="Output"
NONE
```

## See also

* [`DEFINE NAMESPACE`](../define/namespace.md)
