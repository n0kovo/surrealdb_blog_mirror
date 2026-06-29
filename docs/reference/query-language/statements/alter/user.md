---
position: 17
title: ALTER USER
description: The ALTER statement can be used to change authentication access and behaviour, global parameters, table configurations, table events, schema definitions, and indexes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/user.mdx"
---

# `ALTER USER` statement

*Since v3.0.5*

The `ALTER USER` statement can be used to modify an existing defined database [user](../define/user.md).

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER USER [ IF EXISTS ] @name
  ON [ ROOT | NAMESPACE | DATABASE ]
  [ PASSWORD @pass | PASSHASH @hash ]
  [ ROLES @role, ... ]
  [ DURATION FOR TOKEN [ @duration | NONE ] ]
  [ DURATION FOR SESSION [ @duration | NONE ] ]
  [ COMMENT @string | DROP COMMENT ]
```

  
**Railroad Diagram**

```
                                                                                                                                             ╭───────────────────────────────────────────────────────────────╮                                                                                                                                                                                        
                                                                                                                                             │                                                               │                                                                                                                                                                                        
                         ╭────────────────────────────╮                                              ╭─────────────────────────────────────╮ │                              ╭──────────────────────────────╮ │ ╭─────────────────────────────────────────────────────────────────╮ ╭───────────────────────────────────────────────────────────────────╮ ╭──────────────────────────────────────╮     
                         │                            │                                              │                                     │ │                              │                              │ │ │                                                                 │ │                                                                   │ │                                      │     
        ╭────────────╮   │    ╭────╮     ╭────────╮   │   ╭───────╮     ╭────╮        ╭──────╮       │      ╭──────────╮     ┌───────┐     │ │    ╭───────╮     ┌───────┐   │      ╭───╮     ┌───────┐     │ │ │    ╭──────────╮     ╭─────╮     ╭───────╮      ┌───────────┐    │ │    ╭──────────╮     ╭─────╮     ╭─────────╮      ┌───────────┐    │ │      ╭─────────╮     ╭─────────╮     │     
├┼──────│ ALTER USER │───╯────│ IF │─────│ EXISTS │───╰───│ @name │─────│ ON │───╮────│ ROOT │─────╭─╯─╮────│ PASSWORD │─────│ @pass │───╭─╰─╯────│ ROLES │─────│ @role │───╯─╭────│ , │─────│ @role │───╮─╰─╰─╯────│ DURATION │─────│ FOR │─────│ TOKEN │───╮──│ @duration │──╭─╰─╯────│ DURATION │─────│ FOR │─────│ SESSION │───╮──│ @duration │──╭─╰─╯─╮────│ COMMENT │─────│ @string │───╭─╰───┼┤
        ╰────────────╯        ╰────╯     ╰────────╯       ╰───────╯     ╰────╯   │    ╰──────╯     │   │    ╰──────────╯     └───────┘   │        ╰───────╯     └───────┘     │    ╰───╯     └───────┘   │          ╰──────────╯     ╰─────╯     ╰───────╯   │  └───────────┘  │        ╰──────────╯     ╰─────╯     ╰─────────╯   │  └───────────┘  │     │    ╰─────────╯     ╰─────────╯   │       
                                                                                 │                 │   │                                 │                                    ╰──────────────────────────╯                                                   │                 │                                                   │                 │     │                                  │       
                                                                                 │  ╭───────────╮  │   │    ╭──────────╮     ┌───────┐   │                                                                                                                   │    ╭──────╮     │                                                   │    ╭──────╮     │     │     ╭──────╮     ╭─────────╮     │       
                                                                                 ╰──│ NAMESPACE │──╯   ╰────│ PASSHASH │─────│ @hash │───╯                                                                                                                   ╰────│ NONE │─────╯                                                   ╰────│ NONE │─────╯     ╰─────│ DROP │─────│ COMMENT │─────╯       
                                                                                 │  ╰───────────╯  │        ╰──────────╯     └───────┘                                                                                                                            ╰──────╯                                                              ╰──────╯                 ╰──────╯     ╰─────────╯             
                                                                                 │                 │                                                                                                                                                                                                                                                                                                  
                                                                                 │  ╭──────────╮   │                                                                                                                                                                                                                                                                                                  
                                                                                 ╰──│ DATABASE │───╯                                                                                                                                                                                                                                                                                                  
                                                                                    ╰──────────╯
```

## Example usage

```surql
-- Define a user with viewer role
DEFINE USER billy ON DATABASE PASSWORD "example" ROLES VIEWER;

-- Congrats on your promotion billy,
-- be sure to use this power for good
ALTER USER billy ON DATABASE ROLES EDITOR;
```
