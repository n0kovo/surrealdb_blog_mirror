---
position: 1
title: Overview
description: Version 2 of the SurrealDB SDK for PHP is a rewrite with a fluent query builder, typed credentials, and a PSR-based transport layer.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v2/index.mdx"
---

# PHP SDK v2

Version 2 is a rewrite of the PHP SDK. It keeps the same goal as v1, connecting your PHP application to SurrealDB, but changes most of the public surface. Queries are built with a fluent builder (`$db->select($table)->where(...)->limit(10)`), credentials are typed value objects, and the transport layer is built on PSR HTTP interfaces so you can swap in your own client.

> [!IMPORTANT]
> Version 2 is published as `2.0.0-alpha.1`. It is an alpha with breaking changes against [v1](../v1/index.md), and the public API may still change before a stable release. Pin the exact version when installing.
>
> These docs are a work in progress. While the SDK is in alpha, expect them to change substantially as decisions about the public-facing API are settled.

The SDK requires PHP `8.4` or later and works with SurrealDB server versions `1.0.0` up to (but not including) `4.0.0`. The version is checked on connect unless you disable it.

If you are upgrading an existing project, start with the [migration guide](migration.md).

## Getting started

- **[Installation](installation.md)** — Install the alpha release with Composer and add a PSR-18 HTTP client.
- **[Quickstart](start.md)** — Connect to SurrealDB and run your first queries in a few minutes.

## Core concepts

- **[Connecting to SurrealDB](concepts/connecting-to-surrealdb.md)** — Open a connection over WebSocket or HTTP, select a namespace and database, and handle reconnection.
- **[Authentication](concepts/authentication.md)** — Sign in and sign up with typed credentials, then manage tokens.
- **[Executing queries](concepts/executing-queries.md)** — Run raw SurrealQL or use the fluent query builders for select, create, update, and delete.
- **[Live queries](concepts/live-queries.md)** — Subscribe to real-time changes over a WebSocket connection.

## Advanced

- **[Observability](concepts/observability.md)** — Emit traces and metrics through OpenTelemetry or PSR-3 adapters.
- **[Middleware](concepts/middleware.md)** — Intercept every RPC with built-in or custom middleware.
- **[Events](concepts/events.md)** — Observe lifecycle and RPC traffic with PSR-14 events.
- **[Sessions](concepts/sessions.md)** — Run multiple independent sessions over one connection.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.php)
- [Composer package](https://packagist.org/packages/surrealdb/surrealdb.php)
