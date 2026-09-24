---
position: 14
title: Reference
description: SurrealQL statements and functions, and the full API surface. The HTTP, RPC, CBOR and Postgres wire protocols, the command-line tools, and every official SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/reference.mdx"
---

# Reference

This section holds exhaustive material, organised for lookup rather than for reading through. Every SurrealQL statement, every built-in function, every protocol message and every SDK method is documented here. For the explanations behind them, see [Learn](learn.md).

## Core

- **[SurrealQL](reference/query-language/index.md)** — Statements, functions, operators, data types and language primitives.
- **[APIs and protocols](reference/rest-api/index.md)** — REST, HTTP, RPC, CBOR and Postgres wire protocols, and the shared error format.
- **[CLI tools](reference/cli/index.md)** — Command reference for surrealctl, surreal and surqlfmt.

## SDKs

Each SDK page covers installation, connecting, authentication and the full method list for that language.

- **[Rust](reference/rust/index.md)**
- **[JavaScript](reference/javascript/index.md)**
- **[Python](reference/python/index.md)**
- **[Go](reference/golang/index.md)**
- **[.NET](reference/dotnet/index.md)**
- **[Java](reference/java/index.md)**
- **[Kotlin](reference/kotlin/index.md)**
- **[PHP](reference/php/index.md)**
- **[Swift](reference/swift/index.md)**
- **[Mojo](reference/mojo/index.md)**

[Community SDKs](languages/community.md) cover further languages and runtimes, and the [Expo](frameworks/expo.md) and [React Native](frameworks/react-native.md) guides cover mobile.

## Markdown for agents

Every page in this section is also served as markdown: append `.md` to any path, or send `Accept: text/markdown`. The whole corpus is available at [llms-full.txt](https://surrealdb.com/docs/llms-full.txt), and the page index at [llms.txt](https://surrealdb.com/docs/llms.txt).
