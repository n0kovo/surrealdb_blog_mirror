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
    [ MIGRATE EXISTING ROWS AS @name REMOVE UNDECLARED FIELDS ]
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
                                                                                │ │                                                  ╰────────╯   │    ╰───────╯     │   └─────────┘                                                  │ │      
                                                                                │ │                                                               │                  │                                                                │ │      
                                                                                │ │                                                               │  ╭────────────╮  │                                                                │ │      
                                                                                │ │                                                               ╰──│ REFERENCES │──╯                                                                │ │      
                                                                                │ │                                                                  ╰────────────╯                                                                   │ │      
                                                                                │ │                                                                                                                                                   │ │      
                                                                                │ │                                    ╭──────────────────────────╮     ┌───────┐     ╭──────────────────────────╮                                    │ │      
                                                                                │ ╰────────────────────────────────────│ MIGRATE EXISTING ROWS AS │─────│ @name │─────│ REMOVE UNDECLARED FIELDS │────────────────────────────────────╯ │      
                                                                                │                                      ╰──────────────────────────╯     └───────┘     ╰──────────────────────────╯                                      │      
                                                                                ╰───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## COMPACT

*Since v3.0.0*

Performs storage compaction on a specific table keyspace. To compact other resources, use [ALTER SYSTEM](system.md) to compact the entire datastore, [ALTER NAMESPACE](namespace.md) to compact the current namespace keyspace, or [ALTER DATABASE](database.md) to compact the current database keyspace.

The storage engine carries out the compaction. In SurrealDB 4.0, SurrealKV supports it: it writes recent changes to disk, merges the data files that hold the keys, and drops deleted data and old versions that no reader can see, which frees their space. The statement returns once the compaction is done, and reads and writes carry on meanwhile. Before 4.0, RocksDB was the only engine that supported compaction requests. The in-memory engine and TiKV do not support them, and return the following error:

```surql
'There was a problem with the key-value store: The storage layer does not support compaction requests.'
```

A successful compaction returns `NONE`.

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

## Changing the table type

`TYPE` changes what kind of records the table holds. A table that holds records of the other kind cannot change to a type that excludes them: `TYPE RELATION` is refused while the table holds a record that is not an edge, and `TYPE NORMAL` while it holds an edge. The error names the first record that does not fit:

```surql
CREATE note:1;
ALTER TABLE note TYPE RELATION;
```

```surql title="Error output"
'Cannot make `note` TYPE RELATION: it holds note:1, which is not an edge. Delete the record first, or define the table TYPE ANY'
```

`TYPE ANY` holds both kinds of record, so a change to it is always accepted. The same check applies to `DEFINE TABLE OVERWRITE` with a new type. Before SurrealDB 4.0 the change was accepted, and an export of the table then failed to import.

## MIGRATE EXISTING ROWS ... REMOVE UNDECLARED FIELDS

*Since v4.0.0*

`REMOVE UNDECLARED FIELDS` removes every field that the table does not define from every record of the table. It is a named migration, so it runs once for a given name, in the background, and a record is cleaned the first time it is read.

```surql
DEFINE TABLE person SCHEMALESS;
CREATE person:1 SET name = 'Ada', nickname = 'A';
DEFINE FIELD name ON person TYPE string;
ALTER TABLE person SCHEMAFULL;

ALTER TABLE person MIGRATE EXISTING ROWS AS drop_undeclared REMOVE UNDECLARED FIELDS;
SELECT * FROM person;
```

```surql title="Output"
[{ id: person:1, name: 'Ada' }]
```

See [Migrating existing records](../define/field.md#migrating-existing-records) for migrations that convert the values of one field.

## See also

* [`DEFINE TABLE`](../define/table.md)
