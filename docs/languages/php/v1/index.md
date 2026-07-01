---
position: 1
title: Overview
description: Version 1 is the current stable release of the SurrealDB PHP SDK, with direct RPC-style methods for querying a remote database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v1/index.mdx"
---

# PHP SDK v1

Version 1 is the current stable release of the PHP SDK. It exposes a single `Surreal` class with direct, RPC-style methods such as `create()`, `select()`, `query()`, and `signin()`. Each method maps closely to a SurrealDB RPC call.

> [!NOTE]
> The latest stable release is *(latest)*. A rewrite is available as [v2 (alpha)](../v2/index.md). If you are starting a new project and can accept alpha software, see the [migration guide](../v2/migration.md) for the differences.

The SDK requires PHP `8.2` or later and the `curl` extension. It connects to a remote SurrealDB instance over HTTP or WebSocket.

## Getting started

- **[Installation](installation.md)** — Install the SDK with Composer.
- **[Quickstart](start.md)** — Connect to SurrealDB and run your first queries.

## Concepts

- **[Connecting to SurrealDB](concepts/connecting.md)** — Initialize the SDK, connect, and select a namespace and database.
- **[Authentication](concepts/authentication.md)** — Sign up and sign in users with scopes, credentials, and tokens.
- **[Executing queries](concepts/executing-queries.md)** — Create, select, update, and delete records.
- **[Methods](methods/index.md)** — The full reference of methods on the Surreal class.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.php)
- [Composer package](https://packagist.org/packages/surrealdb/surrealdb.php)
