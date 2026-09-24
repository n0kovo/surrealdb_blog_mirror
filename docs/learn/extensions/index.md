---
position: 1
title: Extensions
description: Extend SurrealDB with custom modules and WASM plugins. Done through the Surrealism extension system.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/extensions/index.mdx"
---

# Extensions

*Since v3.0.0*

>[!NOTE]
> Surrealism plugins remain an experimental functionality under active development. This guide assumes SurrealDB 3.1.0 or later. Version 3.1.0 made [many additions](https://github.com/surrealdb/surrealdb/pull/7082) to Surrealism's core functionality. We look forward to feedback on the plugin system, either via raising an issue or PR on the [SurrealDB repo](https://github.com/surrealdb/surrealdb), or on our [Discord server](https://discord.gg/surrealdb) - the `#surrealism` channel is a good place to start.

SurrealDB's extension system, known as Surrealism, lets you add custom functionality to the database engine without modifying its core. Extensions are compiled to WebAssembly (WASM) and loaded at runtime, which means they run in a sandboxed environment with predictable performance characteristics.

This section covers:

- [Plugins](plugins/overview.md) - an overview of the plugin architecture, how plugins are discovered and loaded, and the types of extensions you can create.
- [Guides](guides/creating-custom-modules.md) - step-by-step walkthroughs for creating custom modules, understanding the module architecture, and working with WASM plugins.
- [Attribute reference](guides/surrealism-attribute-reference.md) - options for the `#[surrealism]` attribute used to mark functions as Surrealism functions, such as `writeable`, `comment`, `init`, and namespaced exports.

## Guides

- [Using WASM plugins](guides/using-wasm-plugins.md) - load and call a compiled plugin
