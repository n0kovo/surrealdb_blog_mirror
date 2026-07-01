---
position: 2
title: Quickstart
description: Connect to SurrealDB with version 1 of the PHP SDK and run your first queries.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v1/start.mdx"
---

# Quickstart

This guide connects to a SurrealDB instance with version 1 of the PHP SDK and runs a few basic operations.

## 1. Install the SDK

Follow the [installation guide](installation.md) to add the SDK to your project, then include the autoloader and import the `Surreal` class.

```php
require __DIR__ . '/vendor/autoload.php';

use Surreal\Surreal;

$db = new Surreal();
```

## 2. Connect and select a namespace

Connect to the instance, then select a namespace and database with `use()`.

```php
$db->connect("ws://127.0.0.1:8000/rpc");

$db->use([
    "namespace" => "surrealdb",
    "database" => "docs",
]);
```

## 3. Authenticate

Sign in with your credentials. See [Authentication](concepts/authentication.md) for namespace, database, and record access.

```php
$token = $db->signin([
    "username" => "root",
    "password" => "root",
]);
```

## 4. Create and read records

Use `create()` to add a record and `select()` to read it back.

```php
$person = $db->create("person:tobie", [
    "name" => "Tobie",
    "age" => 32,
]);

$everyone = $db->select("person");
```

## 5. Run SurrealQL

Use `query()` for raw [SurrealQL](../../../reference/query-language/index.md), passing variables as the second argument.

```php
$result = $db->query(
    'SELECT * FROM person WHERE age > $min',
    ["min" => 18]
);
```

## 6. Close the connection

```php
$db->close();
```

## What's next?

- **[Executing queries](concepts/executing-queries.md)** — Create, select, update, and delete records in depth.
- **[Authentication](concepts/authentication.md)** — Sign up and sign in users with scopes and tokens.
- **[Methods](methods/index.md)** — The full method reference for the Surreal class.
