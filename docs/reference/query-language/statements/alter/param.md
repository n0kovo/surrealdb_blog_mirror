---
position: 13
title: PARAM
description: The ALTER statement can be used to change authentication access and behaviour, global parameters, table configurations, table events, schema definitions, and indexes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/param.mdx"
---

# `ALTER PARAM` statement

*Since v3.0.5*

The `ALTER PARAM` statement can be used to modify an existing defined [param](../define/param.md).

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER PARAM [ IF EXISTS ] $name
  [ VALUE @value ]
  [ COMMENT @string | DROP COMMENT ]
  [ PERMISSIONS [ NONE | FULL | WHERE @condition ] ]
```

  
**Railroad Diagram**

```
                                                                                                                                                  ╭────────────────────────────────────────────────────────────╮     
                                                                                                                                                  │                                                            │     
                                                                                                                                                  │                                    ╭──────╮                │     
                                                                                                                                                  │                      ╭─────────────│ NONE │──────────────╮ │     
                          ╭────────────────────────────╮               ╭───────────────────────────────╮ ╭──────────────────────────────────────╮ │                      │             ╰──────╯              │ │     
                          │                            │               │                               │ │                                      │ │                      │                                   │ │     
        ╭─────────────╮   │    ╭────╮     ╭────────╮   │   ╭───────╮   │    ╭───────╮     ┌────────┐   │ │      ╭─────────╮     ╭─────────╮     │ │    ╭─────────────╮   │             ╭──────╮              │ │     
├┼──────│ ALTER PARAM │───╯────│ IF │─────│ EXISTS │───╰───│ $name │───╯────│ VALUE │─────│ @value │───╰─╯─╮────│ COMMENT │─────│ @string │───╭─╰─╯────│ PERMISSIONS │───┼─────────────│ FULL │──────────────┼─╰───┼┤
        ╰─────────────╯        ╰────╯     ╰────────╯       ╰───────╯        ╰───────╯     └────────┘       │    ╰─────────╯     ╰─────────╯   │        ╰─────────────╯   │             ╰──────╯              │       
                                                                                                           │                                  │                          │                                   │       
                                                                                                           │     ╭──────╮     ╭─────────╮     │                          │    ╭───────╮     ┌────────────┐   │       
                                                                                                           ╰─────│ DROP │─────│ COMMENT │─────╯                          ╰────│ WHERE │─────│ @condition │───╯       
                                                                                                                 ╰──────╯     ╰─────────╯                                     ╰───────╯     └────────────┘
```

Note that `ALTER PARAM` does not support `DROP VALUE` as a parameter without a value is not valid.

## Example usage

```surql
DEFINE PARAM $MODE VALUE "production" COMMENT "Don't use this param yet";

ALTER PARAM $MODE DROP COMMENT;

-- Check the statement
(INFO FOR DB).params.MODE;
```

```surql title="Output: comment is gone"
"DEFINE PARAM $MODE VALUE 'production' PERMISSIONS FULL"
```
