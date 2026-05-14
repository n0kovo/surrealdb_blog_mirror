---
position: 1
title: Java SDK
description: The SurrealDB SDK for Java enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/index.mdx"
---

# Java SDK

The SurrealDB SDK for Java lets you connect to [SurrealDB](https://surrealdb.com/docs/start) from any Java application. It supports connecting to remote instances over WebSocket or HTTP, and running embedded databases in-process. The SDK provides methods for querying with [SurrealQL](../../reference/query-language/index.md), managing data, [authentication](../../learn/security/authentication/authentication.md), live queries, and transactions. It uses JNI to call native Rust code for high performance.

## Getting started

- **[Installation](installation.md)** — Install the SDK using Gradle or Maven and import it into your project.
- **[Quickstart](start.md)** — Connect to SurrealDB and perform your first queries in minutes.

## Learn

- **[Concepts](concepts/connecting-to-surrealdb.md)** — Understand how to connect, authenticate, query, and work with data types.
- **[API Reference](api/core/surreal.md)** — Complete reference for all classes, methods, types, and errors.

## Contributing

To contribute to the SDK code, submit an Issue or Pull Request in the [surrealdb.java](https://github.com/surrealdb/surrealdb.java) repository. To contribute to this documentation, submit an Issue or Pull Request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.java)
- [JavaDoc](https://surrealdb.github.io/surrealdb.java/javadoc/)
- [Maven package](https://mvnrepository.com/artifact/com.surrealdb/surrealdb)
