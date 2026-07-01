---
position: 3
title: Installation
description: Install version 1 of the SurrealDB PHP SDK with Composer.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v1/installation.mdx"
---

# Installation

Version 1 of the PHP SDK is installed with the [Composer](https://getcomposer.org/download/) package manager. It requires PHP `8.2` or later and the `curl` extension.

## Install the SDK

Run the following command in your project to install the latest stable release.

```bash
composer require surrealdb/surrealdb.php:^1.0
```

## Import the SDK

Include the [Composer autoloader](https://getcomposer.org/doc/01-basic-usage.md#autoloading), then import the `Surreal` class.

```php
require __DIR__ . '/vendor/autoload.php';

use Surreal\Surreal;
```

You can now create a `Surreal` instance and connect to your database.

## Next steps

- [Connecting to SurrealDB](concepts/connecting.md) to open a connection
- [Quickstart](start.md) to run your first queries
