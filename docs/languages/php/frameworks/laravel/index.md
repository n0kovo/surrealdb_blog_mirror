---
position: 1
title: Overview
description: "The Laravel integration wires the SurrealDB PHP SDK and the Surqlize ORM into Laravel's config, service container, facades, and Artisan commands."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/frameworks/laravel/index.mdx"
---

# Laravel integration

The [Laravel integration](https://github.com/surrealdb/surrealdb.laravel) connects SurrealDB to a Laravel application. It wires [version 2 of the SDK](../../v2/index.md) and the [Surqlize ORM](https://surrealdb.com/docs/languages/php/ecosystem/surqlize) into Laravel's config, service container, facades, and Artisan commands.

Query execution and the database protocol are delegated to the SDK. Models, query compilation, graph relations, and schema definitions are delegated to Surqlize. The integration adds the Laravel glue: publishable config, container bindings, facades, schema commands, and testing helpers.

> [!IMPORTANT]
> The integration is published as `0.0.1-alpha.1` and is in early development. It requires PHP `8.4` and Laravel `11`, `12`, or `13`, and depends on the alpha SDK and ORM.

It does not replace Laravel's SQL database. SurrealDB runs alongside your existing connections, and the integration does not use Eloquent or `config/database.php`.

## Getting started

- **[Installation](installation.md)** — Install the package and publish its configuration.
- **[Configuration](configuration.md)** — Set connection details, auth modes, and multiple connections.

## Using the integration

- **[Container and facades](container-and-facades.md)** — The service providers, container bindings, and the SurrealDB, Surreal, and Surqlize facades.
- **[Queries and transactions](queries-and-transactions.md)** — Run model queries, raw SurrealQL, and transactions in Laravel.
- **[Schema commands](schema-commands.md)** — Dump and apply your Surqlize schema with Artisan.
- **[Testing](testing.md)** — Fake the executor and assert the queries your code sends.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.laravel)
- [Surqlize ORM](https://surrealdb.com/docs/languages/php/ecosystem/surqlize) for models and queries
- [PHP SDK v2](../../v2/index.md) for the underlying client
