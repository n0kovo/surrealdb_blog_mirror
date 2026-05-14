---
position: 12
title: DEFINE MODULE
description: A DEFINE MODULE statement can be used to define a module through which Surrealism extension functions can be called.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/define/module.mdx"
---

# `DEFINE MODULE` statement

*Since v3.0.0*

A `DEFINE MODULE` statement is used to define a module via which [Surrealism](../../../../learn/extensions/plugins/overview.md) extensions functions can be called.

> [!NOTE]
> The [`surrealism` experimental](../../../cli/surrealdb-cli/commands/module.md) feature must be enabled before you can use a `DEFINE MODULE` statement.

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
DEFINE MODULE [ OVERWRITE | IF NOT EXISTS ] @mod::@sub AS @file_name
```

  
**Railroad Diagram**

```
                                    ╭────────────────────────────────────────────╮                                                                                           
                                    │                                            │                                                                                           
                                    │               ╭───────────╮                │                                                                                           
                                    │ ╭─────────────│ OVERWRITE │──────────────╮ │                                                                                           
                                    │ │             ╰───────────╯              │ │                                                  ╭──────────────────────────────────╮     
                                    │ │                                        │ │                                                  │                                  │     
        ╭────────╮     ╭────────╮   │ │    ╭────╮     ╭─────╮     ╭────────╮   │ │   ┌────────────┐     ╭────╮     ┌────────────┐   │    ╭─────────╮     ┌─────────┐   │     
├┼──────│ DEFINE │─────│ MODULE │───╯─╯────│ IF │─────│ NOT │─────│ EXISTS │───╰─╰───│ @mod::@sub │─────│ AS │─────│ @file_name │───╯────│ COMMENT │─────│ @string │───╰───┼┤
        ╰────────╯     ╰────────╯          ╰────╯     ╰─────╯     ╰────────╯         └────────────┘     ╰────╯     └────────────┘        ╰─────────╯     └─────────┘
```

## Example

A module includes a module and a sub, followed by `AS` and a pointer to the `.surli` file containing the Rust code compiled to WASM through the Surrealism CLI.

```surql
DEFINE MODULE mod::test AS f"test:/demo.surli";
```

Once the module is defined, functions can be accessed through this path.

Assuming these two functions in the Rust code before compilation to WASM via the Surrealism CLI:

```rust
#[surrealism]
fn returns_true() -> bool { true };

#[surrealism]
fn check_num_size(num: i32) -> Result<i32, &'static str> {
    if num >= 500 {
        Err("Number is too big!")
    } else {
        Ok(num)
    }
}
```

They will then be accessible using the following paths.

```surql
RETURN mod::test::returns_true();
-- true

RETURN mod::test::check_num_size(100);
-- 100
```
