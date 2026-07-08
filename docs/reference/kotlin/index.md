---
position: 1
title: Kotlin SDK
description: The SurrealDB SDK for Kotlin is a coroutine-based, Kotlin Multiplatform client for querying a remote SurrealDB instance.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/index.mdx"
---

# Kotlin SDK

The SurrealDB SDK for Kotlin lets you connect to [SurrealDB](https://surrealdb.com/docs/start) from any Kotlin application. It is a [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html) library targeting the JVM, Android, and iOS, with a coroutine-based, `suspend`-friendly API. The SDK connects to remote instances over WebSocket or HTTP and provides methods for querying with [SurrealQL](../query-language/index.md), managing data, [authentication](../../learn/security/authentication/authentication.md), live queries, transactions, and multiple sessions. Its design closely mirrors the [JavaScript SDK](../../languages/javascript.md).

> [!NOTE]
> The Kotlin SDK is currently in early development. The latest version is `0.1.0-SNAPSHOT`, and it is not yet published to Maven Central. The coordinates and APIs documented here are provisional and may change before the first stable release.

## Getting started

- **[Installation](installation.md)** — Install the SDK and add it to your project.
- **[Getting started guide](../../languages/kotlin.md)** — Connect to SurrealDB and run your first queries.

## Learn

- **[Concepts](concepts/connecting-to-surrealdb.md)** — Guides for connecting, authenticating, querying, and working with data.
- **[API Reference](api/core/surreal-client.md)** — Complete reference for the SDK's methods, types, and errors.

## Contributing

To contribute to the SDK code, submit an Issue or Pull Request in the [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin) repository. To contribute to this documentation, submit an Issue or Pull Request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.kotlin)
