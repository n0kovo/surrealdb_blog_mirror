---
position: 3
title: ANALYZER
description: The ALTER ANALYZER statement can be used to modify an existing defined analyzer.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/analyzer.mdx"
---

# `ALTER ANALYZER` statement

*Since v3.0.5*

The `ALTER ANALYZER` statement can be used to modify an existing defined [analyzer](../define/analyzer.md).

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER ANALYZER [ IF EXISTS ] @name
  [ FUNCTION fn::@function | DROP FUNCTION ]
  [ TOKENIZERS @tokenizer, ... | DROP TOKENIZERS ]
  [ FILTERS @filter, ... | DROP FILTERS ]
  [ COMMENT @string | DROP COMMENT ]
```

  
**Railroad Diagram**

```
                                                                                                                      ╭──────────────────────────────────────────────────────────────────────────────────╮ ╭─────────────────────────────────────────────────────────────────────────╮                                              
                                                                                                                      │                                                                                  │ │                                                                         │                                              
                             ╭────────────────────────────╮               ╭─────────────────────────────────────────╮ │                                          ╭───────────────────────────────────╮   │ │                                    ╭────────────────────────────────╮   │ ╭──────────────────────────────────────╮     
                             │                            │               │                                         │ │                                          │                                   │   │ │                                    │                                │   │ │                                      │     
        ╭────────────────╮   │    ╭────╮     ╭────────╮   │   ┌───────┐   │      ╭──────────╮     ┌───────────┐     │ │      ╭────────────╮     ┌────────────┐   │      ╭───╮     ┌────────────┐     │   │ │      ╭─────────╮     ┌─────────┐   │      ╭───╮     ┌─────────┐     │   │ │      ╭─────────╮     ┌─────────┐     │     
├┼──────│ ALTER ANALYZER │───╯────│ IF │─────│ EXISTS │───╰───│ @name │───╯─╮────│ FUNCTION │─────│ @function │───╭─╰─╯─╮────│ TOKENIZERS │─────│ @tokenizer │───╯─╭────│ , │─────│ @tokenizer │───╮─╰─╭─╰─╯─╮────│ FILTERS │─────│ @filter │───╯─╭────│ , │─────│ @filter │───╮─╰─╭─╰─╯─╮────│ COMMENT │─────│ @string │───╭─╰───┼┤
        ╰────────────────╯        ╰────╯     ╰────────╯       └───────┘     │    ╰──────────╯     └───────────┘   │     │    ╰────────────╯     └────────────┘     │    ╰───╯     └────────────┘   │   │     │    ╰─────────╯     └─────────┘     │    ╰───╯     └─────────┘   │   │     │    ╰─────────╯     └─────────┘   │       
                                                                            │                                     │     │                                          ╰───────────────────────────────╯   │     │                                    ╰────────────────────────────╯   │     │                                  │       
                                                                            │      ╭──────╮     ╭──────────╮      │     │                                                                              │     │                                                                     │     │     ╭──────╮     ╭─────────╮     │       
                                                                            ╰──────│ DROP │─────│ FUNCTION │──────╯     │                          ╭──────╮     ╭────────────╮                         │     │                       ╭──────╮     ╭─────────╮                      │     ╰─────│ DROP │─────│ COMMENT │─────╯       
                                                                                   ╰──────╯     ╰──────────╯            ╰──────────────────────────│ DROP │─────│ TOKENIZERS │─────────────────────────╯     ╰───────────────────────│ DROP │─────│ FILTERS │──────────────────────╯           ╰──────╯     ╰─────────╯             
                                                                                                                                                   ╰──────╯     ╰────────────╯                                                       ╰──────╯     ╰─────────╯
```

## Example usage

```surql
-- Define an analyzer
DEFINE ANALYZER example_edgengram TOKENIZERS class FILTERS
  edgengram(1,3);

-- Shorten the edgengram
ALTER ANALYZER example_edgengram FILTERS edgengram(1,2);

-- Check the output
search::analyze("example_edgengram", "Apple banana!!");
```

```surql title="Output"
[
	'A',
	'Ap',
	'b',
	'ba',
	'!',
	'!!'
]
```
