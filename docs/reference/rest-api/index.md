---
position: 1
title: REST API
description: SurrealDB exposes an HTTP-based REST API for executing queries, managing authentication, and performing CRUD operations.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/rest-api/index.mdx"
---

# REST API

Any language or tool capable of making HTTP requests can interact with SurrealDB through this API. This is useful when an official SDK is not available for your stack, or when you need to integrate SurrealDB with infrastructure tooling, scripts, or third-party platforms.

## What the API provides

- **Query execution** — send SurrealQL statements over HTTP and receive results as JSON.
- **Authentication** — sign in, sign up, and manage tokens via dedicated endpoints.
- **CRUD operations** — create, read, update, and delete records using RESTful conventions.
- **Health and status** — check whether the server is running and accepting connections.

## Protocol details

The full HTTP protocol reference, including request and response formats, authentication headers, and endpoint specifications, is available in the [HTTP protocol](http-protocol.md) page.

## Alternative access methods

If you prefer a richer client experience, SurrealDB also supports:

- **WebSocket protocol** — persistent connections with real-time capabilities.
- **Official SDKs** — language-specific clients for [JavaScript](../../languages/javascript/overview.md), [Python](../../languages/python/index.md), [Rust](../../languages/rust/overview.md), [Go](../../languages/golang/index.md), [Java](../../languages/java/index.md), [.NET](../../languages/dotnet/index.md), and [PHP](../../languages/php/index.md).
