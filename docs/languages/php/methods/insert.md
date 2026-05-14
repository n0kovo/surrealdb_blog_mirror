---
position: 1
title: insert
description: Insert one or multiple records in the database using the insert method with the SurrealDB PHP SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/methods/insert.mdx"
---

# `->insert()` {#insert}

Inserts one or multiple records in the database.

```php title="Method Syntax"
$db->insert($thing, $data)
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
                `thing`
                <label label="required" />
            </td>
			<td colspan="2" scope="row" data-label="Type">
				`string`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                The table name or [`RecordId`](../data-types.md#recordid) to insert to.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `data`
               <label label="optional" />
            </td>
			<td colspan="2" scope="row" data-label="Type">
				`associative array`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                Either a single document/record or an array of documents/records to insert
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php

// Insert a single record
[$person] = $db->insert('person', [
	"name" => 'Tobie',
	"settings" => [
		"active" => true,
		"marketing" => true,
	],
]);

$person = $db->insert(new RecordId('person', 'tobie'), [
	"name" => 'Tobie',
	"settings" => [
		"active" => true,
		"marketing" => true,
	],
]);

// Insert multiple records
$people = $db->insert('person', [
	[
		"name" => 'Tobie',
		"settings" => [
			"active" => true,
			"marketing" => true,
		],
	],
	[
		"name" => 'Jaime',
		"settings" => [
			"active" => true,
			"marketing" => true,
		],
	],
]);

// The content you are creating the record with might differ from the return type
$people = $db->insert('person', [
	[ "name" => 'Tobie' ],
	[ "name" => 'Jaime' ],
]);
```

### Translated query
This function will run the following query in the database.

```surql
INSERT INTO $thing $data;
```
