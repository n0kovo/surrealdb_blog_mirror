---
position: 1
title: Embedding SurrealDB
description: In this section, you will find detailed instructions on how to embed SurrealDB into your application depending on your programming language.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/embedding/index.mdx"
---

# Embedding SurrealDB

Instead of connecting to a remote server, you can run SurrealDB directly inside your application process. Embedded mode gives you the full query engine with no network overhead, which is useful for local-first applications, edge deployments, and testing.

## Embedding languages

The following languages are supported:

- [.NET](by-language/dotnet.md)
- [Go](by-language/golang.md)
- [JavaScript](by-language/javascript.md)
- [Python](by-language/python.md)
- [Rust](by-language/rust.md)

## Browser embedding options

When embedding SurrealDB in web browsers, you have two options:

- **IndexedDB**: SurrealDB can be configured to use IndexedDB to store and persist data within the web browser. SurrealDB first serializes both keys and values into a Uint8Array, utilizing IndexedDB as a binary key-value store - offering good performance, and with the ability to offer all of the functionality and features that SurrealDB offers when running in alternative ways.

- **SDK**: Alternatively, you can use the SurrealDB SDK to connect to a remote SurrealDB instance instead of using IndexedDB for local persistence.
