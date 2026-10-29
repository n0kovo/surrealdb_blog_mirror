---
position: 9
title: ALTER FIELD
description: The ALTER FIELD statement is used to change or entirely drop clauses of a defined field on a table.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/field.mdx"
---

# `ALTER FIELD` statement

The `ALTER FIELD` statement is used to change or entirely drop clauses of a defined field on a table.

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER FIELD [ IF EXISTS ] @name ON [ TABLE ] @table 
[ 
    DROP TYPE |
    DROP FLEXIBLE |
    DROP READONLY |
    DROP INLINE |
    DROP VALUE |
    DROP ASSERT |
    DROP DEFAULT |
    DROP COMMENT |
    DROP REFERENCE |
    FLEXIBLE |
    READONLY |
    INLINE |
    REFERENCE |
    TYPE @type |
    VALUE @value |
    ASSERT @expression |
    DEFAULT [ ALWAYS ] @expression |
    [ PERMISSIONS [ NONE | FULL
		| FOR select @expression
		| FOR create @expression
		| FOR update @expression
		| FOR delete @expression
	] ]
    COMMENT @string |
    MIGRATE EXISTING ROWS AS @name USING @expression [ FALLBACK @value ]
]
```

  
**Railroad Diagram**

```
                                  ╭────────────────────────────╮                          ╭─────────────╮                                                                                                                                                     
                                  │                            │                          │             │                                                                                                                                                     
        ╭───────╮     ╭───────╮   │    ╭────╮     ╭────────╮   │   ┌───────┐     ╭────╮   │  ╭───────╮  │   ┌────────┐                                                     ╭──────╮        ╭──────╮                                                           
├┼──────│ ALTER │─────│ FIELD │───╯────│ IF │─────│ EXISTS │───╰───│ @name │─────│ ON │───╯──│ TABLE │──╰───│ @table │────╭─╮──────────────────────────────────────────────│ DROP │───╮────│ TYPE │─────╭────────────────────────────────────────────╭─╮────┼┤
        ╰───────╯     ╰───────╯        ╰────╯     ╰────────╯       └───────┘     ╰────╯      ╰───────╯      └────────┘    │ │                                              ╰──────╯   │    ╰──────╯     │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │  ╭──────────╮   │                                            │ │      
                                                                                                                          │ │                                                         ╰──│ FLEXIBLE │───╯                                            │ │      
                                                                                                                          │ │                                                         │  ╰──────────╯   │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │  ╭──────────╮   │                                            │ │      
                                                                                                                          │ │                                                         ╰──│ READONLY │───╯                                            │ │      
                                                                                                                          │ │                                                         │  ╰──────────╯   │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │   ╭────────╮    │                                            │ │      
                                                                                                                          │ │                                                         ╰───│ INLINE │────╯                                            │ │      
                                                                                                                          │ │                                                         │   ╰────────╯    │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │    ╭───────╮    │                                            │ │      
                                                                                                                          │ │                                                         ╰────│ VALUE │────╯                                            │ │      
                                                                                                                          │ │                                                         │    ╰───────╯    │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │   ╭────────╮    │                                            │ │      
                                                                                                                          │ │                                                         ╰───│ ASSERT │────╯                                            │ │      
                                                                                                                          │ │                                                         │   ╰────────╯    │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │   ╭─────────╮   │                                            │ │      
                                                                                                                          │ │                                                         ╰───│ DEFAULT │───╯                                            │ │      
                                                                                                                          │ │                                                         │   ╰─────────╯   │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │   ╭─────────╮   │                                            │ │      
                                                                                                                          │ │                                                         ╰───│ COMMENT │───╯                                            │ │      
                                                                                                                          │ │                                                         │   ╰─────────╯   │                                            │ │      
                                                                                                                          │ │                                                         │                 │                                            │ │      
                                                                                                                          │ │                                                         │  ╭───────────╮  │                                            │ │      
                                                                                                                          │ │                                                         ╰──│ REFERENCE │──╯                                            │ │      
                                                                                                                          │ │                                                            ╰───────────╯                                               │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                      ╭──────────╮                                                      │ │      
                                                                                                                          │ ╰──────────────────────────────────────────────────────│ FLEXIBLE │──────────────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                                      ╰──────────╯                                                      │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                      ╭──────────╮                                                      │ │      
                                                                                                                          │ ╰──────────────────────────────────────────────────────│ READONLY │──────────────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                                      ╰──────────╯                                                      │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                       ╭────────╮                                                       │ │      
                                                                                                                          │ ╰───────────────────────────────────────────────────────│ INLINE │───────────────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                                       ╰────────╯                                                       │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                     ╭───────────╮                                                      │ │      
                                                                                                                          │ ╰─────────────────────────────────────────────────────│ REFERENCE │──────────────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                                     ╰───────────╯                                                      │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                 ╭──────╮     ╭───────╮                                                 │ │      
                                                                                                                          │ ╰─────────────────────────────────────────────────│ TYPE │─────│ @type │─────────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                                 ╰──────╯     ╰───────╯                                                 │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                ╭───────╮     ╭────────╮                                                │ │      
                                                                                                                          │ ╰────────────────────────────────────────────────│ VALUE │─────│ @value │────────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                                ╰───────╯     ╰────────╯                                                │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                             ╭────────╮     ╭─────────────╮                                             │ │      
                                                                                                                          │ ╰─────────────────────────────────────────────│ ASSERT │─────│ @expression │─────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                             ╰────────╯     ╰─────────────╯                                             │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                  ╭──────────────╮                                                      │ │      
                                                                                                                          │ │                                                  │              │                                                      │ │      
                                                                                                                          │ │                                    ╭─────────╮   │  ╭────────╮  │   ╭─────────────╮                                    │ │      
                                                                                                                          │ ╰────────────────────────────────────│ DEFAULT │───╯──│ ALWAYS │──╰───│ @expression │────────────────────────────────────╯ │      
                                                                                                                          │ │                                    ╰─────────╯      ╰────────╯      ╰─────────────╯                                    │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                             ╭────────────────────────────────────────────────────────────╮                             │ │      
                                                                                                                          │ │                             │                                                            │                             │ │      
                                                                                                                          │ │                             │                                    ╭──────╮                │                             │ │      
                                                                                                                          │ │                             │                      ╭─────────────│ NONE │──────────────╮ │                             │ │      
                                                                                                                          │ │                             │                      │             ╰──────╯              │ │                             │ │      
                                                                                                                          │ │                             │                      │                                   │ │                             │ │      
                                                                                                                          │ │                             │    ╭─────────────╮   │             ╭──────╮              │ │                             │ │      
                                                                                                                          │ ╰─────────────────────────────╯────│ PERMISSIONS │───┼─────────────│ FULL │──────────────┼─╰─────────────────────────────╯ │      
                                                                                                                          │ │                                  ╰─────────────╯   │             ╰──────╯              │                               │ │      
                                                                                                                          │ │                                                    │                                   │                               │ │      
                                                                                                                          │ │                                                    │    ╭───────╮     ┌────────────┐   │                               │ │      
                                                                                                                          │ │                                                    ╰────│ WHERE │─────│ @condition │───╯                               │ │      
                                                                                                                          │ │                                                         ╰───────╯     └────────────┘                                   │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                               ╭─────────╮     ╭─────────╮                                              │ │      
                                                                                                                          │ ╰───────────────────────────────────────────────│ COMMENT │─────│ @string │──────────────────────────────────────────────╯ │      
                                                                                                                          │ │                                               ╰─────────╯     ╰─────────╯                                              │ │      
                                                                                                                          │ │                                                                                                                        │ │      
                                                                                                                          │ │                                                                                   ╭──────────────────────────────────╮ │ │      
                                                                                                                          │ │                                                                                   │                                  │ │ │      
                                                                                                                          │ │    ╭──────────────────────────╮     ┌───────┐     ╭───────╮     ┌─────────────┐   │    ╭──────────╮     ┌────────┐   │ │ │      
                                                                                                                          │ ╰────│ MIGRATE EXISTING ROWS AS │─────│ @name │─────│ USING │─────│ @expression │───╯────│ FALLBACK │─────│ @value │───╰─╯ │      
                                                                                                                          │      ╰──────────────────────────╯     └───────┘     ╰───────╯     └─────────────┘        ╰──────────╯     └────────┘       │      
                                                                                                                          ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Examples

As `ALTER FIELD` contains the same clauses available in a [`DEFINE FIELD`](../define/field.md) statement, be sure to see that page for more examples.

Here is one example in which the `name` field is defined for a record `user`:

```surql
DEFINE FIELD name ON user TYPE string;
```

Later on, a database-wide [parameter](../define/param.md) is defined to disallow certain user names. This can be followed up with an `ALTER FIELD` statement to add the `ASSERT` clause to it.

```surql
DEFINE PARAM $DISALLOWED_NAMES VALUE ["Lord British", "Lord Blackthorn"];
ALTER FIELD name ON user ASSERT $value NOT IN $DISALLOWED_NAMES;
CREATE user SET name = "Lord British";
```

```surql title="Output"
"Found 'Lord British' for field `name`, with record `user:yn4yttkg5w683q2937bq`, but field must conform to: $value NOTINSIDE $DISALLOWED_NAMES""
```

## Migrating existing records

*Since v4.0.0*

`MIGRATE EXISTING ROWS` converts the values that records already hold when `ALTER FIELD` changes the field's type. In a database at [compatibility level](../define/database.md#compatibility-level) 4, a `SCHEMAFULL` table that holds records refuses a type change without it unless the new type accepts every old value.

```surql
-- In a database at compatibility level 4
DEFINE TABLE person SCHEMAFULL;
DEFINE FIELD age ON person TYPE int;
CREATE person:1 SET age = 37;

ALTER FIELD age ON person TYPE string
    MIGRATE EXISTING ROWS AS age_to_string USING <string> $value FALLBACK '';
SELECT * FROM person;
```

```surql title="Output"
[{ age: '37', id: person:1 }]
```

The rules for the transform, the `FALLBACK` value and the fields that cannot be migrated are in [Migrating existing records](../define/field.md#migrating-existing-records).

## See also

* [`DEFINE FIELD`](../define/field.md)
