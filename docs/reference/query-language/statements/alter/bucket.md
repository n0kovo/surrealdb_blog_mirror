---
position: 5
title: BUCKET
description: The ALTER BUCKET statement can be used to modify an existing defined bucket.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/bucket.mdx"
---

# `ALTER BUCKET` statement

*Since v3.0.5*

The `ALTER BUCKET` statement can be used to modify an existing defined [bucket](../define/bucket.md).

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER BUCKET [ IF EXISTS ] @name
  [ READONLY | DROP READONLY ]
  [ BACKEND @string | DROP BACKEND ]
  [ PERMISSIONS @expression ]
  [ COMMENT @string | DROP COMMENT ]
```

  
**Railroad Diagram**

```
                           ╭────────────────────────────╮               ╭────────────────────────────────────╮ ╭──────────────────────────────────────╮ ╭──────────────────────────────────────────╮ ╭──────────────────────────────────────╮     
                           │                            │               │                                    │ │                                      │ │                                          │ │                                      │     
        ╭──────────────╮   │    ╭────╮     ╭────────╮   │   ╭───────╮   │            ╭──────────╮            │ │      ╭─────────╮     ╭─────────╮     │ │    ╭─────────────╮     ┌─────────────┐   │ │      ╭─────────╮     ╭─────────╮     │     
├┼──────│ ALTER BUCKET │───╯────│ IF │─────│ EXISTS │───╰───│ @name │───╯─╮──────────│ READONLY │──────────╭─╰─╯─╮────│ BACKEND │─────│ @string │───╭─╰─╯────│ PERMISSIONS │─────│ @expression │───╰─╯─╮────│ COMMENT │─────│ @string │───╭─╰───┼┤
        ╰──────────────╯        ╰────╯     ╰────────╯       ╰───────╯     │          ╰──────────╯          │     │    ╰─────────╯     ╰─────────╯   │        ╰─────────────╯     └─────────────┘       │    ╰─────────╯     ╰─────────╯   │       
                                                                          │                                │     │                                  │                                                  │                                  │       
                                                                          │    ╭──────╮     ╭──────────╮   │     │     ╭──────╮     ╭─────────╮     │                                                  │     ╭──────╮     ╭─────────╮     │       
                                                                          ╰────│ DROP │─────│ READONLY │───╯     ╰─────│ DROP │─────│ BACKEND │─────╯                                                  ╰─────│ DROP │─────│ COMMENT │─────╯       
                                                                               ╰──────╯     ╰──────────╯               ╰──────╯     ╰─────────╯                                                              ╰──────╯     ╰─────────╯
```

## Example usage

```surql
DEFINE BUCKET my_bucket BACKEND "memory";

ALTER BUCKET my_bucket COMMENT "Should we make this read-only too??";
```
