---
position: 16
title: ALTER TABLE
description: The ALTER TABLE statement is used to alter a defined table.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/table.mdx"
---

# `ALTER TABLE` statement

The `ALTER TABLE` statement is used to alter a defined table.

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER TABLE [
	[ IF EXISTS ] @name
		[ DROP COMMENT ]
        [ DROP CHANGEFEED ]
        [ DROP INLINE EDGES ]
        [ DROP INLINE REFERENCES ]
        [ COMPACT ]
		[ SCHEMAFULL | SCHEMALESS ]
		[ TYPE [ ANY | NORMAL | RELATION [ [ IN | FROM ] @table ] [ [ OUT | TO ] @table ] [ ENFORCED ] [ LIGHTWEIGHT ]]]
		[ PERMISSIONS [ NONE | FULL
			| FOR select @expression
			| FOR create @expression
			| FOR update @expression
			| FOR delete @expression
		] ]
    [ CHANGEFEED @duration [ INCLUDE ORIGINAL ] ]
    [ COMMENT @string ] 
    [ INLINE EDGES @number ]
    [ INLINE REFERENCES @number ]
]
```

  
**Railroad Diagram**

```
                                  ╭────────────────────────────╮                                                                                                                                                                               
                                  │                            │                                                                                                                                                                               
        ╭───────╮     ╭───────╮   │    ╭────╮     ╭────────╮   │   ┌───────┐                                                        ╭──────╮                 ╭─────────╮                                                                       
├┼──────│ ALTER │─────│ TABLE │───╯────│ IF │─────│ EXISTS │───╰───│ @name │────╭─╮─────────────────────────────────────────────────│ DROP │───╮─────────────│ COMMENT │──────────────╭───────────────────────────────────────────────╭─╮────┼┤
        ╰───────╯     ╰───────╯        ╰────╯     ╰────────╯       └───────┘    │ │                                                 ╰──────╯   │             ╰─────────╯              │                                               │ │      
                                                                                │ │                                                            │                                      │                                               │ │      
                                                                                │ │                                                            │            ╭────────────╮            │                                               │ │      
                                                                                │ │                                                            ╰────────────│ CHANGEFEED │────────────╯                                               │ │      
                                                                                │ │                                                            │            ╰────────────╯            │                                               │ │      
                                                                                │ │                                                            │                                      │                                               │ │      
                                                                                │ │                                                            │    ╭────────╮        ╭───────╮       │                                               │ │      
                                                                                │ │                                                            ╰────│ INLINE │───╮────│ EDGES │─────╭─╯                                               │ │      
                                                                                │ │                                                                 ╰────────╯   │    ╰───────╯     │                                                 │ │      
                                                                                │ │                                                                              │                  │                                                 │ │      
                                                                                │ │                                                                              │  ╭────────────╮  │                                                 │ │      
                                                                                │ │                                                                              ╰──│ REFERENCES │──╯                                                 │ │      
                                                                                │ │                                                                                 ╰────────────╯                                                    │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                                                    ╭─────────╮                                                                    │ │      
                                                                                │ ╰────────────────────────────────────────────────────────────────────│ COMPACT │────────────────────────────────────────────────────────────────────╯ │      
                                                                                │ │                                                                    ╰─────────╯                                                                    │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                                                  ╭────────────╮                                                                   │ │      
                                                                                │ ╰───────────────────────────────────────────────────────────────╮──│ SCHEMAFULL │──╭────────────────────────────────────────────────────────────────╯ │      
                                                                                │ │                                                               │  ╰────────────╯  │                                                                │ │      
                                                                                │ │                                                               │                  │                                                                │ │      
                                                                                │ │                                                               │  ╭────────────╮  │                                                                │ │      
                                                                                │ │                                                               ╰──│ SCHEMALESS │──╯                                                                │ │      
                                                                                │ │                                                                  ╰────────────╯                                                                   │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                                                             ╭─────╮                                                               │ │      
                                                                                │ │               ╭─────────────────────────────────────────────────────────────│ ANY │─────────────────────────────────────────────────────────────╮ │ │      
                                                                                │ │               │                                                             ╰─────╯                                                             │ │ │      
                                                                                │ │               │                                                                                                                                 │ │ │      
                                                                                │ │    ╭──────╮   │                                                           ╭────────╮                                                            │ │ │      
                                                                                │ ╰────│ TYPE │───┼───────────────────────────────────────────────────────────│ NORMAL │────────────────────────────────────────────────────────────┼─╯ │      
                                                                                │ │    ╰──────╯   │                                                           ╰────────╯                                                            │ │ │      
                                                                                │ │               │                                                                                                                                 │ │ │      
                                                                                │ │               │                   ╭────────────────────────────────╮ ╭───────────────────────────────╮                                          │ │ │      
                                                                                │ │               │                   │                                │ │                               │                                          │ │ │      
                                                                                │ │               │                   │      ╭────╮                    │ │     ╭─────╮                   │                                          │ │ │      
                                                                                │ │               │                   │  ╭───│ IN │───╮                │ │  ╭──│ OUT │──╮                │                                          │ │ │      
                                                                                │ │               │                   │  │   ╰────╯   │                │ │  │  ╰─────╯  │                │ ╭────────────────╮ ╭───────────────────╮ │ │ │      
                                                                                │ │               │                   │  │            │                │ │  │           │                │ │                │ │                   │ │ │ │      
                                                                                │ │               │    ╭──────────╮   │  │  ╭──────╮  │   ┌────────┐   │ │  │  ╭────╮   │   ┌────────┐   │ │  ╭──────────╮  │ │  ╭─────────────╮  │ │ │ │      
                                                                                │ │               ╰────│ RELATION │───╯──╯──│ FROM │──╰───│ @table │───╰─╯──╯──│ TO │───╰───│ @table │───╰─╯──│ ENFORCED │──╰─╯──│ LIGHTWEIGHT │──╰─╯ │ │      
                                                                                │ │                    ╰──────────╯         ╰──────╯      └────────┘           ╰────╯       └────────┘        ╰──────────╯       ╰─────────────╯      │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                                                               ╭──────╮                                                            │ │      
                                                                                │ │                                                          ╭────────────────────│ NONE │─────────────────────╮                                      │ │      
                                                                                │ │                                                          │                    ╰──────╯                     │                                      │ │      
                                                                                │ │                                                          │                                                 │                                      │ │      
                                                                                │ │                                        ╭─────────────╮   │                    ╭──────╮                     │                                      │ │      
                                                                                │ ╰────────────────────────────────────────│ PERMISSIONS │───┼────────────────────│ FULL │─────────────────────┼──────────────────────────────────────╯ │      
                                                                                │ │                                        ╰─────────────╯   │                    ╰──────╯                     │                                      │ │      
                                                                                │ │                                                          │                                                 │                                      │ │      
                                                                                │ │                                                          │    ╭─────╮     ╭────────╮     ┌─────────────┐   │                                      │ │      
                                                                                │ │                                                          ╰────│ FOR │─────│ select │─────│ @expression │───╯                                      │ │      
                                                                                │ │                                                          │    ╰─────╯     ╰────────╯     └─────────────┘   │                                      │ │      
                                                                                │ │                                                          │                                                 │                                      │ │      
                                                                                │ │                                                          │    ╭─────╮     ╭────────╮     ┌─────────────┐   │                                      │ │      
                                                                                │ │                                                          ╰────│ FOR │─────│ create │─────│ @expression │───╯                                      │ │      
                                                                                │ │                                                          │    ╰─────╯     ╰────────╯     └─────────────┘   │                                      │ │      
                                                                                │ │                                                          │                                                 │                                      │ │      
                                                                                │ │                                                          │    ╭─────╮     ╭────────╮     ┌─────────────┐   │                                      │ │      
                                                                                │ │                                                          ╰────│ FOR │─────│ update │─────│ @expression │───╯                                      │ │      
                                                                                │ │                                                          │    ╰─────╯     ╰────────╯     └─────────────┘   │                                      │ │      
                                                                                │ │                                                          │                                                 │                                      │ │      
                                                                                │ │                                                          │    ╭─────╮     ╭────────╮     ┌─────────────┐   │                                      │ │      
                                                                                │ │                                                          ╰────│ FOR │─────│ delete │─────│ @expression │───╯                                      │ │      
                                                                                │ │                                                               ╰─────╯     ╰────────╯     └─────────────┘                                          │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                                                          ╭───────────────────────────────────╮                                    │ │      
                                                                                │ │                                                                          │                                   │                                    │ │      
                                                                                │ │                                       ╭────────────╮     ┌───────────┐   │    ╭─────────╮     ╭──────────╮   │                                    │ │      
                                                                                │ ╰───────────────────────────────────────│ CHANGEFEED │─────│ @duration │───╯────│ INCLUDE │─────│ ORIGINAL │───╰────────────────────────────────────╯ │      
                                                                                │ │                                       ╰────────────╯     └───────────┘        ╰─────────╯     ╰──────────╯                                        │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                                            ╭─────────╮     ┌─────────┐                                                            │ │      
                                                                                │ ╰────────────────────────────────────────────────────────────│ COMMENT │─────│ @string │────────────────────────────────────────────────────────────╯ │      
                                                                                │ │                                                            ╰─────────╯     └─────────┘                                                            │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                                  ╭────────╮        ╭───────╮         ┌─────────┐                                                  │ │      
                                                                                │ ╰──────────────────────────────────────────────────│ INLINE │───╮────│ EDGES │─────╭───│ @number │──────────────────────────────────────────────────╯ │      
                                                                                │                                                    ╰────────╯   │    ╰───────╯     │   └─────────┘                                                    │      
                                                                                │                                                                 │                  │                                                                  │      
                                                                                │                                                                 │  ╭────────────╮  │                                                                  │      
                                                                                │                                                                 ╰──│ REFERENCES │──╯                                                                  │      
                                                                                │                                                                    ╰────────────╯                                                                     │      
                                                                                ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## COMPACT

*Since v3.0.0*

Performs storage compaction on a specific table keyspace. To compact other resources, use [ALTER SYSTEM](system.md) to compact the entire datastore, [ALTER NAMESPACE](namespace.md) to compact the current namespace keyspace, or [ALTER DATABASE](database.md) to compact the current database keyspace.

The actual compaction used will depend on the datastore, such as RocksDB or SurrealKV.

This clause will not work with in-memory storage which has nothing persistent to compact, producing the following error:

```surql
'The storage layer does not support compaction requests.'
```

A successful compaction will return `NONE`.

```surql
ALTER TABLE user COMPACT;
```

```surql title="Output"
NONE
```

## INLINE EDGES and INLINE REFERENCES

*Since v3.3.0*

`INLINE EDGES @number` and `INLINE REFERENCES @number` set or change the cap of a table's [adjacency and reference caches](../define/table.md#using-inline-edges-and-inline-references-to-cache-adjacency), from 0 to 256. `DROP INLINE EDGES` and `DROP INLINE REFERENCES` remove a cap, which turns that cache off. One statement can set one cap and drop the other:

```surql
ALTER TABLE person INLINE EDGES 8 DROP INLINE REFERENCES;
```

Any change to a cap discards the table's existing caches of that kind. They are rebuilt as edges or references are written.

## See also

* [`DEFINE TABLE`](../define/table.md)
