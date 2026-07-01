---
position: 1
title: connect
description: Connect to a local or remote database endpoint using the connect method in the SurrealDB PHP SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v1/methods/connect.mdx"
---

# `->connect()` {#connect}

Connects to a local or remote database endpoint.

```php title="Method Syntax"
$db->connect($host, $options)
```

### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
			<th colspan="2" scope="col">Type</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>  
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `host`
            </td>
			<td colspan="2" scope="row" data-label="Type">
				`string`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                The url of the database endpoint to connect to.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `options`
            </td>
			<td colspan="2" scope="row" data-label="Type">
				`associative array`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                An object with options to initiate the connection to SurrealDB.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

There are several ways to connect to a database endpoint. You can connect to a local or remote endpoint, specify a namespace and database pair to use, authenticate with an existing token, authenticate using a pair of credentials, or use advanced custom logic to prepare the connection to the database.

```php
// Connect to a local endpoint
$db->connect('http://127.0.0.1:8000/rpc');

// Connect to a remote endpoint
$db->connect('https://cloud.surrealdb.com/rpc');

// Specify a namespace and database pair to use
$db->connect('https://cloud.surrealdb.com/rpc', [
	"namespace" => "surrealdb",
	"database" => "docs",
]);
```
