---
position: 1
title: Overview
description: The SurrealDB SDK for PHP lets you query a remote SurrealDB instance from any PHP application, with a stable v1 release and a v2 rewrite in alpha.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/index.mdx"
---

# PHP SDK

The SurrealDB SDK for PHP lets you connect to SurrealDB from server-side applications, APIs, and command-line tools. You can run queries, manage data and authentication, call database functions, and subscribe to real-time updates with live queries. When connecting over WebSocket, the SDK reconnects automatically if the connection drops.

The SDK ships in two lines. Version 1.x is the current stable release and uses direct RPC-style methods such as `$db->create($thing, $data)`. Version 2.x is a rewrite with a fluent query builder, typed credentials, and a PSR-based transport layer. It is in alpha and introduces breaking changes.

> [!NOTE]
> The latest stable release is *(latest)*, documented under [v1](v1/index.md).
> The `2.0.0-alpha.1` release is documented under [v2](v2/index.md). It is an alpha with breaking changes, so pin the exact version when installing it.

## Choose a version

- **[v1 (stable)](v1/index.md)** — The current stable release. Direct RPC-style methods over HTTP and WebSocket.
- **[v2 (alpha)](v2/index.md)** — The rewrite with fluent query builders and typed credentials. Alpha, breaking changes.
- **[Migration guide](v2/migration.md)** — Move an existing project from v1 to v2, with a method-by-method mapping.

## Ecosystem

- **[Surqlize (ORM)](https://surrealdb.com/docs/languages/php/ecosystem/surqlize)** — An object-relational mapper with attribute-driven models, a typed query builder, and graph relations.

## Frameworks

- **[Laravel](frameworks/laravel/index.md)** — A Laravel integration that wires the SDK and Surqlize into config, the service container, and Artisan.

## Contributing

To contribute to the SDK code, submit an issue or pull request in the [surrealdb.php](https://github.com/surrealdb/surrealdb.php) repository. To contribute to this documentation, submit an issue or pull request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.php)
- [Composer package](https://packagist.org/packages/surrealdb/surrealdb.php)
