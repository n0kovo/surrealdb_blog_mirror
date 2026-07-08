---
position: 1
title: query
description: The ->query() method for the SurrealDB SDK for PHP runs a set of SurrealQL statements against the database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/php/v1/methods/query.mdx"
---

# `->query()` {#query}

Runs a set of [SurrealQL statements](../../../query-language/index.md) against the database.

```php title="Method Syntax"
$db->query($query, $vars)
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
                `$query`
                <label label="required" />
            </td>
			<td colspan="2" scope="row" data-label="Type">
				`string`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `$vars`
               <label label="optional" />
            </td>
			<td colspan="2" scope="row" data-label="Type">
				`associative array`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                Assigns variables which can be used in the query.
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php
// Assign the variable on the connection
$result = db->query(
	'CREATE person SET name = "John"; SELECT * FROM type::table($tb);',
	[ "tb" => "person" ]
);

// Get the first result from the first query
$created = $result[0]->result[0];

// Get all of the results from the second query
$people = $result[1]->result;
```
