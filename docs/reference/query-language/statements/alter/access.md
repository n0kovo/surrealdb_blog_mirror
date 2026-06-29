---
position: 2
title: ALTER ACCESS
description: The ALTER ACCESS statement can be used to modify an existing defined access.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/access.mdx"
---

# `ALTER ACCESS` statement

*Since v3.0.5*

The `ALTER ACCESS` statement can be used to modify an existing defined [access](../define/access/index.md).

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER ACCESS [ IF EXISTS ] @name
  ON [ ROOT | NAMESPACE | DATABASE ]
  [ AUTHENTICATE @expression | DROP AUTHENTICATE ]
  [ DURATION
    [ FOR GRANT [ @duration | NONE ] ]
    [ FOR TOKEN [ @duration | NONE ] ]
    [ FOR SESSION [ @duration | NONE ] ]
  ]
  [ COMMENT @string | DROP COMMENT ]
```

  
**Railroad Diagram**

```
                                                                                                                                                         ╭──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮                                              
                                                                                                                                                         │                                                                                                                                                                              │                                              
                           ╭────────────────────────────╮                                              ╭───────────────────────────────────────────────╮ │                   ╭────────────────────────────────────────────────╮ ╭────────────────────────────────────────────────╮ ╭──────────────────────────────────────────────────╮ │ ╭──────────────────────────────────────╮     
                           │                            │                                              │                                               │ │                   │                                                │ │                                                │ │                                                  │ │ │                                      │     
        ╭──────────────╮   │    ╭────╮     ╭────────╮   │   ╭───────╮     ╭────╮        ╭──────╮       │      ╭──────────────╮     ┌─────────────┐     │ │    ╭──────────╮   │    ╭─────╮     ╭───────╮      ╭───────────╮    │ │    ╭─────╮     ╭───────╮      ╭───────────╮    │ │    ╭─────╮     ╭─────────╮      ╭───────────╮    │ │ │      ╭─────────╮     ╭─────────╮     │     
├┼──────│ ALTER ACCESS │───╯────│ IF │─────│ EXISTS │───╰───│ @name │─────│ ON │───╮────│ ROOT │─────╭─╯─╮────│ AUTHENTICATE │─────│ @expression │───╭─╰─╯────│ DURATION │───╯────│ FOR │─────│ GRANT │───╮──│ @duration │──╭─╰─╯────│ FOR │─────│ TOKEN │───╮──│ @duration │──╭─╰─╯────│ FOR │─────│ SESSION │───╮──│ @duration │──╭─╰─╰─╯─╮────│ COMMENT │─────│ @string │───╭─╰───┼┤
        ╰──────────────╯        ╰────╯     ╰────────╯       ╰───────╯     ╰────╯   │    ╰──────╯     │   │    ╰──────────────╯     └─────────────┘   │        ╰──────────╯        ╰─────╯     ╰───────╯   │  ╰───────────╯  │        ╰─────╯     ╰───────╯   │  ╰───────────╯  │        ╰─────╯     ╰─────────╯   │  ╰───────────╯  │       │    ╰─────────╯     ╰─────────╯   │       
                                                                                   │                 │   │                                           │                                                    │                 │                                │                 │                                  │                 │       │                                  │       
                                                                                   │  ╭───────────╮  │   │       ╭──────╮     ╭──────────────╮       │                                                    │    ╭──────╮     │                                │    ╭──────╮     │                                  │    ╭──────╮     │       │     ╭──────╮     ╭─────────╮     │       
                                                                                   ╰──│ NAMESPACE │──╯   ╰───────│ DROP │─────│ AUTHENTICATE │───────╯                                                    ╰────│ NONE │─────╯                                ╰────│ NONE │─────╯                                  ╰────│ NONE │─────╯       ╰─────│ DROP │─────│ COMMENT │─────╯       
                                                                                   │  ╰───────────╯  │           ╰──────╯     ╰──────────────╯                                                                 ╰──────╯                                           ╰──────╯                                             ╰──────╯                   ╰──────╯     ╰─────────╯             
                                                                                   │                 │                                                                                                                                                                                                                                                                                 
                                                                                   │  ╭──────────╮   │                                                                                                                                                                                                                                                                                 
                                                                                   ╰──│ DATABASE │───╯                                                                                                                                                                                                                                                                                 
                                                                                      ╰──────────╯
```

Note that this statement does not allow modification of the access type itself (`RECORD` / `JWT` / `BEARER`), only its duration, the `AUTHENTICATE` clause, and a `COMMENT`.

## Example usage

```surql
-- Define an access
DEFINE ACCESS account ON DATABASE TYPE RECORD
	SIGNUP ( CREATE user SET email = $email,
	  pass = crypto::argon2::generate($pass) )
	SIGNIN ( SELECT * FROM user WHERE email = $email
	  AND crypto::argon2::compare(pass, $pass) )
	DURATION FOR TOKEN 15m, FOR SESSION 12h;

-- Shorten the token duration
ALTER ACCESS account ON DATABASE DURATION FOR TOKEN 1m;
```
