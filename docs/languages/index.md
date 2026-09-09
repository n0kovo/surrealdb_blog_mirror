---
position: 0
title: SDKs
description: One official SurrealDB SDK per language. Each has a quickstart that gets you connected and a reference covering every method.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/index.mdx"
---

SurrealDB has ten official SDKs. Each speaks the same RPC protocol over WebSocket or HTTP, so the concepts carry between them: connect, select a namespace and database, sign in, then query. What differs is the idiom - types, async model and error handling follow the host language.

Every SDK page opens with a quickstart that gets you connected, and continues into a reference for each method.

- **[Rust](rust.md)**
- **[JavaScript](javascript.md)**
- **[Python](python.md)**
- **[Go](golang.md)**
- **[.NET](dotnet.md)**
- **[Java](java.md)**
- **[Kotlin](kotlin.md)**
- **[PHP](php.md)**
- **[Swift](swift.md)**
- **[Mojo](mojo.md)**

[Community SDKs](community.md) cover further languages, and the [Expo](../frameworks/expo.md) and [React Native](../frameworks/react-native.md) guides cover mobile.

## Choosing between the interfaces

An SDK is the usual way in, but it is not the only one. The [RPC protocol](../reference/rest-api/rpc-protocol.md) keeps one connection open and is what the SDKs use themselves, so it is the interface that supports live queries. The [HTTP REST API](../reference/rest-api/http-protocol.md) opens a connection per request and suits environments where holding a socket is awkward. The [CLI](../reference/cli/index.md) covers import, export and one-off queries.
