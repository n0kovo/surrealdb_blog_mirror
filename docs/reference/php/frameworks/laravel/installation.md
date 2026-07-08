---
position: 2
title: Installation
description: Install the SurrealDB Laravel integration with Composer and publish the SDK and ORM configuration files.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/php/frameworks/laravel/installation.mdx"
---

# Installation

Install the integration with [Composer](https://getcomposer.org/download/). It requires PHP `8.4` or later and Laravel `11`, `12`, or `13`, and pulls in the alpha [SDK](../../v2/index.md) and [Surqlize ORM](https://surrealdb.com/docs/reference/php/ecosystem/surqlize).

## Install the package

```bash
composer require surrealdb/laravel
```

The integration depends on alpha releases, so your project must allow them. If Composer cannot resolve the dependencies under the default `stable` minimum stability, lower it.

```bash
composer config minimum-stability alpha
composer config prefer-stable true
```

## Publish the configuration

The SDK and ORM keep their configuration separate. Publish both files.

```bash
php artisan vendor:publish --tag=surrealdb-config
php artisan vendor:publish --tag=surqlize-config
```

This creates `config/surrealdb.php` for the SDK client and `config/surqlize.php` for the ORM.

## Service provider discovery

Laravel auto-discovers the two service providers, so there is nothing to register manually. See [Container and facades](container-and-facades.md) for what they bind.

## Next steps

- **[Configuration](configuration.md)** — Set your connection details and authentication.
- **[Queries and transactions](queries-and-transactions.md)** — Run your first model queries.
