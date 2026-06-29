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
        [ COMPACT ]
		[ SCHEMAFULL | SCHEMALESS ]
		[ PERMISSIONS [ NONE | FULL
			| FOR select @expression
			| FOR create @expression
			| FOR update @expression
			| FOR delete @expression
		] ]
    [ CHANGEFEED @duration ]
    [ COMMENT @string ] 
    [ CHANGEFEED ]
]
```

  
**Railroad Diagram**

```
                          ╭────────────────────────────╮                                                                                                                                                              
                          │                            │                                                                                                                                                              
        ╭─────────────╮   │    ╭────╮     ╭────────╮   │   ╭────────╮                                                         ╭──────╮       ╭─────────╮                                                              
├┼──────│ ALTER TABLE │───╯────│ IF │─────│ EXISTS │───╰───│ @table │────╭─╮──────────────────────────────────────────────────│ DROP │───╮───│ COMMENT │────╭────────────────────────────────────────────────╭─╮────┼┤
        ╰─────────────╯        ╰────╯     ╰────────╯       ╰────────╯    │ │                                                  ╰──────╯   │   ╰─────────╯    │                                                │ │      
                                                                         │ │                                                             │                  │                                                │ │      
                                                                         │ │                                                             │  ╭────────────╮  │                                                │ │      
                                                                         │ │                                                             ╰──│ CHANGEFEED │──╯                                                │ │      
                                                                         │ │                                                                ╰────────────╯                                                   │ │      
                                                                         │ │                                                                                                                                 │ │      
                                                                         │ │                                                           ╭─────────╮                                                           │ │      
                                                                         │ ╰───────────────────────────────────────────────────────────│ COMPACT │───────────────────────────────────────────────────────────╯ │      
                                                                         │ │                                                           ╰─────────╯                                                           │ │      
                                                                         │ │                                                                                                                                 │ │      
                                                                         │ │ ╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮ │ │      
                                                                         │ │ │                                                                                                                             │ │ │      
                                                                         │ │ │                                                                  ╭─────╮                                                    │ │ │      
                                                                         │ │ │               ╭──────────────────────────────────────────────────│ ANY │──────────────────────────────────────────────────╮ │ │ │      
                                                                         │ │ │               │                                                  ╰─────╯                                                  │ │ │ │      
                                                                         │ │ │               │                                                                                                           │ │ │ │      
                                                                         │ │ │    ╭──────╮   │                                                ╭────────╮                                                 │ │ │ │      
                                                                         │ ╰─╯────│ TYPE │───┼────────────────────────────────────────────────│ NORMAL │─────────────────────────────────────────────────┼─╰─╯ │      
                                                                         │ │      ╰──────╯   │                                                ╰────────╯                                                 │   │ │      
                                                                         │ │                 │                                                                                                           │   │ │      
                                                                         │ │                 │                   ╭────────────────────────────────╮ ╭───────────────────────────────╮                    │   │ │      
                                                                         │ │                 │                   │                                │ │                               │                    │   │ │      
                                                                         │ │                 │                   │      ╭────╮                    │ │     ╭─────╮                   │                    │   │ │      
                                                                         │ │                 │                   │  ╭───│ IN │───╮                │ │  ╭──│ OUT │──╮                │                    │   │ │      
                                                                         │ │                 │                   │  │   ╰────╯   │                │ │  │  ╰─────╯  │                │ ╭────────────────╮ │   │ │      
                                                                         │ │                 │                   │  │            │                │ │  │           │                │ │                │ │   │ │      
                                                                         │ │                 │    ╭──────────╮   │  │  ╭──────╮  │   ┌────────┐   │ │  │  ╭────╮   │   ┌────────┐   │ │  ╭──────────╮  │ │   │ │      
                                                                         │ │                 ╰────│ RELATION │───╯──╯──│ FROM │──╰───│ @table │───╰─╯──╯──│ TO │───╰───│ @table │───╰─╯──│ ENFORCED │──╰─╯   │ │      
                                                                         │ │                      ╰──────────╯         ╰──────╯      └────────┘           ╰────╯       └────────┘        ╰──────────╯        │ │      
                                                                         │ │                                                                                                                                 │ │      
                                                                         │ │                                                     ╭───────╮     ╭────────╮                                                    │ │      
                                                                         │ ╰─────────────────────────────────────────────────────│ VALUE │─────│ @value │────────────────────────────────────────────────────╯ │      
                                                                         │ │                                                     ╰───────╯     ╰────────╯                                                    │ │      
                                                                         │ │                                                                                                                                 │ │      
                                                                         │ │                                                  ╭────────╮     ╭─────────────╮                                                 │ │      
                                                                         │ ╰──────────────────────────────────────────────────│ ASSERT │─────│ @expression │─────────────────────────────────────────────────╯ │      
                                                                         │ │                                                  ╰────────╯     ╰─────────────╯                                                 │ │      
                                                                         │ │                                                                                                                                 │ │      
                                                                         │ │                                                       ╭──────────────╮                                                          │ │      
                                                                         │ │                                                       │              │                                                          │ │      
                                                                         │ │                                         ╭─────────╮   │  ╭────────╮  │   ╭─────────────╮                                        │ │      
                                                                         │ ╰─────────────────────────────────────────│ DEFAULT │───╯──│ ALWAYS │──╰───│ @expression │────────────────────────────────────────╯ │      
                                                                         │ │                                         ╰─────────╯      ╰────────╯      ╰─────────────╯                                        │ │      
                                                                         │ │                                                                                                                                 │ │      
                                                                         │ │                                 ╭────────────────────────────────────────────────────────────╮                                  │ │      
                                                                         │ │                                 │                                                            │                                  │ │      
                                                                         │ │                                 │                                    ╭──────╮                │                                  │ │      
                                                                         │ │                                 │                      ╭─────────────│ NONE │──────────────╮ │                                  │ │      
                                                                         │ │                                 │                      │             ╰──────╯              │ │                                  │ │      
                                                                         │ │                                 │                      │                                   │ │                                  │ │      
                                                                         │ │                                 │    ╭─────────────╮   │             ╭──────╮              │ │                                  │ │      
                                                                         │ ╰─────────────────────────────────╯────│ PERMISSIONS │───┼─────────────│ FULL │──────────────┼─╰──────────────────────────────────╯ │      
                                                                         │ │                                      ╰─────────────╯   │             ╰──────╯              │                                    │ │      
                                                                         │ │                                                        │                                   │                                    │ │      
                                                                         │ │                                                        │    ╭───────╮     ┌────────────┐   │                                    │ │      
                                                                         │ │                                                        ╰────│ WHERE │─────│ @condition │───╯                                    │ │      
                                                                         │ │                                                             ╰───────╯     └────────────┘                                        │ │      
                                                                         │ │                                                                                                                                 │ │      
                                                                         │ │                                                   ╭─────────╮     ╭─────────╮                                                   │ │      
                                                                         │ ╰───────────────────────────────────────────────────│ COMMENT │─────│ @string │───────────────────────────────────────────────────╯ │      
                                                                         │                                                     ╰─────────╯     ╰─────────╯                                                     │      
                                                                         ╰─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
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
-- NONE
```

## See also

* [`DEFINE TABLE`](../define/table.md)
