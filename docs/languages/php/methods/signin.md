---
position: 1
title: signin
description: The ->signin() method for the SurrealDB SDK for PHP signs in to a specific access method.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/methods/signin.mdx"
---

# `->signin()` {#signin}

Signs in to a root, namespace, database or record user.

```php title="Method Syntax"
$db->signin([
    "namespace" => "main",
    "database" => "db",
    "access" => "account",
    // ... other variables
]);
```

### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Properties</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Properties">
                `username`
                <label label="REQUIRED FOR ROOT, NAMESPACE & DATABASE" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The username of the database user
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Properties">
                `password`
                <label label="REQUIRED FOR ROOT, NAMESPACE & DATABASE" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The password of the database user
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Properties">
                `namespace`
                <label label="REQUIRED FOR DATABASE & ACCESS" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The namespace to sign in to
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Properties">
                `database`
                <label label="REQUIRED FOR ACCESS" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The database to sign in to
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Properties">
                `access`
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The access method to sign in to. Also pass any variables used in the access definition.
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php
// Authenticate with a root user
$token = $db->signin([
	"username" => "root",
	"password" => "surrealdb",
]);

// Authenticate with a Namespace user
$token = $db->signin([
	"namespace" => "surrealdb",
	"username" => "tobie",
	"password" => "surrealdb",
]);

// Authenticate with a Database user
$token = $db->signin([
	"namespace" => "surrealdb",
	"database" => "docs",
	"username" => "tobie",
	"password" => "surrealdb",
]);

// Authenticate with a record access user
$token = $db->signin([
	"namespace" => "surrealdb",
	"database" => "docs",
	"access" => "user",

	// Also pass any properties required by the access definition
	"email" => "info@surrealdb.com",
	"pass" => "123456",
]);
```

You can invalidate the authentication for the current connection using the [`invalidate()` method](invalidate.md).
