---
position: 2
title: Using WASM plugins
description: How to load a pre-built Surrealism module archive into SurrealDB, register it, inspect exports, and call functions from SurrealQL.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/extensions/guides/using-wasm-plugins.mdx"
---

# Using WASM plugins

You do not have to author Rust yourself to benefit from Surrealism. Many teams consume a **pre-built `.surli` archive** produced by another team or pipeline. Authoring a module means writing Rust, configuring `surrealism.toml`, and running [`surreal module`](../../../reference/cli/surrealdb-cli/commands/module.md) yourself. This page focuses on the consumer workflow.

## Storing the module archive

SurrealDB needs access to the `.surli` binary. Use [`DEFINE BUCKET`](../../../reference/query-language/statements/define/bucket.md) to create or configure bucket storage, then upload the `.surli` file according to your environment’s path and permissions model.

## Registering the module

Once the binary is stored, [`DEFINE MODULE`](../../../reference/query-language/statements/define/module.md) associates that artefact with a module name and exposes the compiled functions to SurrealQL. The module definition must line up with the exported function names and signatures from the build.

## Inspecting exports before use

If you receive a module from another team, inspect it locally before upload:

```bash
surreal module info demo.surli
surreal module sig --fnc can_drive demo.surli
```

These commands let you verify function signatures and metadata (such as writeable/comment annotations) before registration.

## Calling functions from SurrealQL

After the module is defined, call its exported functions by qualifying the function with the registered module path. Consult your module’s documentation for exact names and parameters.

If you upgrade the module archive, repeat upload and module definition steps (or your deployment automation) so the running instance picks up the new build.

## Further reading

- [Surrealism overview](../plugins/overview.md) — how compilation, buckets, and modules fit together.
- [`DEFINE BUCKET` reference](../../../reference/query-language/statements/define/bucket.md) — file storage for WASM.
- [`DEFINE MODULE` reference](../../../reference/query-language/statements/define/module.md) — registering Surrealism functions.
