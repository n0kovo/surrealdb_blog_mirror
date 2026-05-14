---
position: 10
title: FUNCTION
description: The ALTER statement can be used to change authentication access and behaviour, global parameters, table configurations, table events, schema definitions, and indexes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/function.mdx"
---

# `ALTER FUNCTION` statement

*Since v3.0.5*

The `ALTER FUNCTION` statement can be used to modify an existing defined [function](../define/function.md).

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER FUNCTION [ IF EXISTS ] fn::@name
  [ ( [ $argument: @type, ... ] ) ] [ -> @type | DROP RETURNS ]
  [ { @query ... } ]
  [ COMMENT @string | DROP COMMENT ]
  [ PERMISSIONS [ NONE | FULL | WHERE @condition ] ] 
```

  
**Railroad Diagram**

```
                                                                              ╭─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮                                                                                                                                    ╭────────────────────────────────────────────────────────────╮     
                                                                              │                                                                                                                                     │                                                                                                                                    │                                                            │     
                                                                              │            ╭────────────────────────────────────────────────────────────────────────────────────────────────────────────╮           │                                                                                                                                    │                                    ╭──────╮                │     
                                                                              │            │                                                                                                            │           │                                                                                                                                    │                      ╭─────────────│ NONE │──────────────╮ │     
                             ╭────────────────────────────╮                   │            │                                               ╭──────────────────────────────────────────────────────────╮ │           │ ╭───────────────────────────────────╮ ╭─────────────────────────────────────────────────╮ ╭──────────────────────────────────────╮ │                      │             ╰──────╯              │ │     
                             │                            │                   │            │                                               │                                                          │ │           │ │                                   │ │                                                 │ │                                      │ │                      │                                   │ │     
        ╭────────────────╮   │    ╭────╮     ╭────────╮   │   ╭───────────╮   │    ╭───╮   │      ╭───────────╮     ╭───╮     ╭───────╮    │      ╭───╮     ╭───────────╮     ╭───╮     ╭───────╮     │ │   ╭───╮   │ │        ╭────╮     ╭───────╮       │ │    ╭───╮     ┌────────┐     ╭─────╮     ╭───╮   │ │      ╭─────────╮     ╭─────────╮     │ │    ╭─────────────╮   │             ╭──────╮              │ │     
├┼──────│ ALTER FUNCTION │───╯────│ IF │─────│ EXISTS │───╰───│ fn::@name │───╯────│ ( │───╯──────│ $argument │─────│ : │─────│ @type │────╯─╭────│ , │─────│ $argument │─────│ : │─────│ @type │───╮─╰─╰───│ ) │───╰─╯─╮──────│ -&gt; │─────│ @type │─────╭─╰─╯────│ { │─────│ @query │─────│ ... │─────│ } │───╰─╯─╮────│ COMMENT │─────│ @string │───╭─╰─╯────│ PERMISSIONS │───┼─────────────│ FULL │──────────────┼─╰───┼┤
        ╰────────────────╯        ╰────╯     ╰────────╯       ╰───────────╯        ╰───╯          ╰───────────╯     ╰───╯     ╰───────╯      │    ╰───╯     ╰───────────╯     ╰───╯     ╰───────╯   │       ╰───╯       │      ╰────╯     ╰───────╯     │        ╰───╯     └────────┘     ╰─────╯     ╰───╯       │    ╰─────────╯     ╰─────────╯   │        ╰─────────────╯   │             ╰──────╯              │       
                                                                                                                                             ╰──────────────────────────────────────────────────────╯                   │                               │                                                         │                                  │                          │                                   │       
                                                                                                                                                                                                                        │    ╭──────╮     ╭─────────╮   │                                                         │     ╭──────╮     ╭─────────╮     │                          │    ╭───────╮     ┌────────────┐   │       
                                                                                                                                                                                                                        ╰────│ DROP │─────│ RETURNS │───╯                                                         ╰─────│ DROP │─────│ COMMENT │─────╯                          ╰────│ WHERE │─────│ @condition │───╯       
                                                                                                                                                                                                                             ╰──────╯     ╰─────────╯                                                                   ╰──────╯     ╰─────────╯                                     ╰───────╯     └────────────┘
```

## Example usage

```surql
-- Declare a function
DEFINE FUNCTION fn::get_message($input: any) {
    $input.message
};

-- No `message` field, returns nothing
fn::get_message("wrong input");

-- Tighten up the valid input for the function
ALTER FUNCTION fn::get_message($input: { error_code: 200, message: string } | {error_code: 404, message: string} ) {
    $input.message
};

-- Returns an error now
fn::get_message("wrong input");

-- Okay, returns 'Looks good'
fn::get_message({ error_code: 200, message: "Looks good" });
```
