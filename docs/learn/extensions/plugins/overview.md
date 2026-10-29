---
position: 1
title: Surrealism plugins
description: Compile Rust into Surrealism extensions, WebAssembly archives whose functions are callable from SurrealQL.
priority: 1
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/extensions/plugins/overview.mdx"
---

# Surrealism extensions

Surrealism extensions are written in Rust, compiled into `.surli` archives, and loaded into a running SurrealDB instance. This gives you access to the Rust ecosystem while keeping extensions sandboxed within the database.

Surrealism was built in order to allow users to extend SurrealDB in ways that benefit them, without needing to make any changes to the code of SurrealDB itself. Some potential use cases are:

* Adding functions to create fake / mock data for testing.
* Accessing functionality in Rust crates that are too specific to merge into SurrealDB itself, such as [language-specific functionality](https://crates.io/crates/hangeul), [custom case conversions](https://docs.rs/convert_case/latest/convert_case/enum.Case.html), or [quantitative finance](https://docs.rs/crate/RustQuant/latest).
* Anything else you have built in your own code that you would like to access inside SurrealDB.

## How Surrealism works

Surrealism works by using the following steps:

* Use the [`surreal ext init`](../../../reference/cli/ext.md#ext-init) command to begin a new project. This command works in a similar manner to `cargo new` in scaffolding a new project with its own `toml` file (`package.toml`).
* Annotate functions to export with `#[surrealism]`.
* Use the `surreal ext build` command to build the extension, and optionally `surreal ext sign` to sign it.
* In SurrealDB, [allow access to the archive](../../../reference/query-language/statements/define/bucket.md) and [define the extension](../../../reference/query-language/statements/define/extension.md) to access the functions.

![A flowchart showing the steps involved to turn regular Rust code into a compiled WASM binary that can be accessed from a running SurrealDB instance.](../../../assets/img/surrealdb/extension/surrealism_flow-light.png)

## What is available in Surrealism

Current Surrealism releases include:

* function-level metadata such as `comment` via `#[surrealism(...)]`, and read-only or read-write database access through a `Transaction` parameter;
* one-time initialisation with `#[surrealism(init)]`, run when the extension is built;
* namespaced exports with `#[surrealism] mod ...`;
* optional read-only attached filesystem data packaged into the archive;
* signed archives, and capabilities granted per extension when it is defined;
* server-side resource controls for execution time, memory, and the number of calls that run at once.

The next pages walk through the workflow and APIs:

- [Quick tutorial](quick-tutorial.md)
- [Creating custom extensions](../guides/creating-custom-extensions.md)
- [Surrealism attribute reference](../guides/surrealism-attribute-reference.md)

## More examples

- [Further examples](further-examples.md) - additional plugins to read through
