---
position: 1
title: Go SDK
description: The SurrealDB SDK for Go enables simple and advanced querying of a remote database from server-side applications.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/golang/index.mdx"
---

# Go SDK

The SurrealDB SDK for Go enables you to interact with SurrealDB from server-side applications, systems, APIs, and [as an embedded instance](embedding.md). You can use the SDK to [execute queries](concepts/executing-queries.md), [manage data](concepts/data-manipulation.md), [authenticate users](concepts/authentication.md), subscribe to real-time changes with [live queries](concepts/live-queries.md), and work with interactive [sessions](concepts/multiple-sessions.md) and [transactions](concepts/transactions.md).

> [!IMPORTANT]
> The SDK requires Go `1.23` or greater, and is available as a [go.dev package](https://pkg.go.dev/github.com/surrealdb/surrealdb.go).

> [!NOTE]
> The latest version of the SDK is *(latest)*.
> The SDK works with SurrealDB versions `v2.0.0` to *(latest)*, ensuring compatibility with the latest version.

## Getting started

- **[Installation](installation.md)** — Install the SDK and add it to your project.
- **[Getting started guide](../../languages/golang.md)** — Connect to SurrealDB and run your first queries.

## Learn

- **[Concepts](concepts/connecting-to-surrealdb.md)** — Guides for connecting, authenticating, querying, and working with data.
- **[API Reference](api/core/db.md)** — Complete reference for the SDK's methods, types, and errors.

## Contributing

To contribute to the SDK code, submit an Issue or Pull Request in the [surrealdb.go](https://github.com/surrealdb/surrealdb.go) repository. To contribute to this documentation, submit an Issue or Pull Request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.go)
- [go.dev package](https://pkg.go.dev/github.com/surrealdb/surrealdb.go)
