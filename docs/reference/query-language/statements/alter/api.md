---
position: 4
title: ALTER API
description: The ALTER API statement can be used to modify an existing defined API.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/alter/api.mdx"
---

# `ALTER API` statement

*Since v3.0.5*

The `ALTER API` statement can be used to modify an existing defined [API](../define/api.md).

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
ALTER API [ IF EXISTS ] @endpoint
  [ FOR any [ @api_config ] [ THEN @expression | DROP THEN ] ]
  [ FOR @http_method, ... [ MIDDLEWARE @function, ... ] [ THEN @expression ] ]
  [ FOR @http_method, ... DROP THEN ]
  [ SECURITY DEFINER | SECURITY INVOKER ]
  [ COMMENT @string | DROP COMMENT ]
```

  
**Railroad Diagram**

```
                                                                         ╭────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮                                                                                      
                                                                         │                                                                                                                                                                                                        │                                                                                      
                        ╭────────────────────────────╮                   │                                                                                 ╭───────────────────╮ ╭───────────────────────────────────────╮                                                        │ ╭─────────────────────────────────────╮ ╭──────────────────────────────────────╮     
                        │                            │                   │                                                                                 │                   │ │                                       │                                                        │ │                                     │ │                                      │     
        ╭───────────╮   │    ╭────╮     ╭────────╮   │   ╭───────────╮   │                                                           ╭─────╮     ╭─────╮   │  ┌─────────────┐  │ │      ╭──────╮     ┌─────────────┐     │                                                        │ │    ╭──────────╮      ╭─────────╮    │ │      ╭─────────╮     ╭─────────╮     │     
├┼──────│ ALTER API │───╯────│ IF │─────│ EXISTS │───╰───│ @endpoint │───╯─╭─╮───────────────────────────────────────────────────────│ FOR │─────│ any │───╯──│ @api_config │──╰─╯─╮────│ THEN │─────│ @expression │───╭─╰────────────────────────────────────────────────────╭─╮─╰─╯────│ SECURITY │───╮──│ DEFINER │──╭─╰─╯─╮────│ COMMENT │─────│ @string │───╭─╰───┼┤
        ╰───────────╯        ╰────╯     ╰────────╯       ╰───────────╯     │ │                                                       ╰─────╯     ╰─────╯      └─────────────┘      │    ╰──────╯     └─────────────┘   │                                                      │ │        ╰──────────╯   │  ╰─────────╯  │     │    ╰─────────╯     ╰─────────╯   │       
                                                                           │ │                                                                                                     │                                   │                                                      │ │                       │               │     │                                  │       
                                                                           │ │                                                                                                     │       ╭──────╮     ╭──────╮       │                                                      │ │                       │  ╭─────────╮  │     │     ╭──────╮     ╭─────────╮     │       
                                                                           │ │                                                                                                     ╰───────│ DROP │─────│ THEN │───────╯                                                      │ │                       ╰──│ INVOKER │──╯     ╰─────│ DROP │─────│ COMMENT │─────╯       
                                                                           │ │                                                                                                             ╰──────╯     ╰──────╯                                                              │ │                          ╰─────────╯              ╰──────╯     ╰─────────╯             
                                                                           │ │                                                                                                                                                                                                │ │                                                                                        
                                                                           │ │                                                                           ╭────────────────────────────────────────────────────────────────────────────╮                                       │ │                                                                                        
                                                                           │ │                                                                           │                                                                            │                                       │ │                                                                                        
                                                                           │ │                                   ╭─────────────────────────────────────╮ │                                       ╭──────────────────────────────────╮ │ ╭───────────────────────────────────╮ │ │                                                                                        
                                                                           │ │                                   │                                     │ │                                       │                                  │ │ │                                   │ │ │                                                                                        
                                                                           │ │    ╭─────╮     ┌──────────────┐   │      ╭───╮     ┌──────────────┐     │ │    ╭────────────╮     ┌───────────┐   │      ╭───╮     ┌───────────┐     │ │ │    ╭──────╮     ┌─────────────┐   │ │ │                                                                                        
                                                                           │ ╰────│ FOR │─────│ @http_method │───╯─╭────│ , │─────│ @http_method │───╮─╰─╯────│ MIDDLEWARE │─────│ @function │───╯─╭────│ , │─────│ @function │───╮─╰─╰─╯────│ THEN │─────│ @expression │───╰─╯ │                                                                                        
                                                                           │ │    ╰─────╯     └──────────────┘     │    ╰───╯     └──────────────┘   │        ╰────────────╯     └───────────┘     │    ╰───╯     └───────────┘   │          ╰──────╯     └─────────────┘     │ │                                                                                        
                                                                           │ │                                     ╰─────────────────────────────────╯                                             ╰──────────────────────────────╯                                           │ │                                                                                        
                                                                           │ │                                                                                                                                                                                                │ │                                                                                        
                                                                           │ │                                                                                ╭─────────────────────────────────────╮                                                                         │ │                                                                                        
                                                                           │ │                                                                                │                                     │                                                                         │ │                                                                                        
                                                                           │ │                                                 ╭─────╮     ┌──────────────┐   │      ╭───╮     ┌──────────────┐     │   ╭──────╮     ╭──────╮                                                 │ │                                                                                        
                                                                           │ ╰─────────────────────────────────────────────────│ FOR │─────│ @http_method │───╯─╭────│ , │─────│ @http_method │───╮─╰───│ DROP │─────│ THEN │─────────────────────────────────────────────────╯ │                                                                                        
                                                                           │                                                   ╰─────╯     └──────────────┘     │    ╰───╯     └──────────────┘   │     ╰──────╯     ╰──────╯                                                   │                                                                                        
                                                                           │                                                                                    ╰─────────────────────────────────╯                                                                             │                                                                                        
                                                                           ╰────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
```

## Example usage

```surql
-- Define a simple API
DEFINE API "/test"
    FOR get
        THEN {
            {
                body: {
                    some: "data"
                }
            };
        };

-- Make a random function
DEFINE FUNCTION fn::feeling_lucky() -> int {
    rand::enum(200, 404)
};

-- Set it as the HTTP status
ALTER API "/test" FOR get THEN {
    {
        status: fn::feeling_lucky(),
        body: {
            some: "data"
        }
    }
};

-- status is either 200 or 404
api::invoke("/test");
```

```surql title="Possible output"
{
	body: {
		some: 'data'
	},
	headers: {
		"x-surreal-request-id": '95fd0577-5b97-4dc1-b98e-c284f0e36a63'
	},
	request_id: '95fd0577-5b97-4dc1-b98e-c284f0e36a63',
	status: 404
}
```

### Changing the security mode

From SurrealDB 4.0, the `SECURITY` clause changes whether the endpoint's body runs with the permissions of the user who defined it (`SECURITY DEFINER`) or with those of the caller (`SECURITY INVOKER`), and leaves the rest of the definition as it is. An `ALTER API` statement without the clause keeps the current mode. See [Running the body with the caller's permissions](../define/api.md#running-the-body-with-the-callers-permissions) for how the two modes differ.

```surql
ALTER API "/test" SECURITY INVOKER;
```
