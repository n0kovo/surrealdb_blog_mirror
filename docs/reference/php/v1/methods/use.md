---
position: 1
title: use
description: The ->use() method for the SurrealDB SDK for PHP switches to a specific namespace and database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/php/v1/methods/use.mdx"
---

# `->use()` {#use}

Switch to a specific namespace and database. If only the ns or db property is specified, the current connection details will be used to fill the other property.

```php title="Method Syntax"
$db->use([ "namespace" => "...", "database" => "..." ]);
```

### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `namespace`
                <label label="initially required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Switches to a specific namespace.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `database`
                <label label="initially required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Switches to a specific database.
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php
$db->use([
    "namespace" => "surrealdb",
    "database" => "docs"
]);
```
