---
position: 4
title: surreal mod
description: The mod component of the surreal launcher, for building and running WebAssembly modules. Its status, and the surreal db module commands that provide the same workflow today.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/modules.mdx"
---

`mod` is the launcher component for WebAssembly module tooling: scaffolding, building, inspecting and running Surrealism modules. It is installed and versioned separately from the database, like every other component.

<Synopsis>
surreal mod <COMMAND>
</Synopsis>

> [!NOTE]
> The first release of the `mod` component is not published yet, so `surreal install mod` does not succeed. Until it is, the commands are available as [`surreal db module`](db/commands/module.md), from the database component. The top-level form `surreal module` is deprecated in favour of `surreal mod` and prints a warning.

## Commands available today

| Command | Purpose |
| --- | --- |
| `surreal db module init [PATH]` | Scaffold a new Surrealism module project. |
| `surreal db module build [SOURCE_PATH]` | Build a WASM module. |
| `surreal db module run <FILE> --fnc <NAME>` | Run a function with arguments. |
| `surreal db module sig <FILE> --fnc <NAME>` | Show a function's signature. |
| `surreal db module info <FILE>` | Show the module's information. |

Flags and examples are on the [`surreal db module`](db/commands/module.md) page. For a walkthrough, see [Working with modules](../../explore/cli/modules.md).
