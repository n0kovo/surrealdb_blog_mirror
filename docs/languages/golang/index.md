---
position: 1
title: Go SDK
description: The SurrealDB SDK for Go enables simple and advanced querying of a remote database from server-side applications.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/index.mdx"
---

# Golang SDK

The SurrealDB SDK for Go enables you to interact with SurrealDB from server-side applications, systems, APIs, and [as an embedded instance](embedding.md). You can use the SDK to [execute queries](concepts/executing-queries.md), [manage data](concepts/data-manipulation.md), [authenticate users](concepts/authentication.md), subscribe to real-time changes with [live queries](concepts/live-queries.md), and work with interactive [sessions](concepts/multiple-sessions.md) and [transactions](concepts/transactions.md).

The SDK requires Go `1.23` or greater, is available as a [go.dev package](https://pkg.go.dev/github.com/surrealdb/surrealdb.go), and is compatible with SurrealDB `v2.x` and `v3.x`.

## Getting started

- [Installation](installation.md) to add the SDK to your project
- [Quick start](start.md) to build your first application

## Documentation

- [Concepts](concepts/connecting-to-surrealdb.md) for guides on connections, authentication, queries, and more
- [API Reference](api/core/db.md) for detailed method signatures, parameters, and return types

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.go)
- [go.dev package](https://pkg.go.dev/github.com/surrealdb/surrealdb.go)

To contribute to the SDK code, submit an Issue or Pull Request in the [surrealdb.go](https://github.com/surrealdb/surrealdb.go) repository. To contribute to this documentation, submit an Issue or Pull Request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.
