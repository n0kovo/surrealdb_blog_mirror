---
position: 1
title: create
description: Create a record in the database using the create method with the SurrealDB PHP SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/methods/create.mdx"
---

# `->create()` {#create}

Creates a record in the database.

```php title="Method Syntax"
$db->create($thing, $data)
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
				`string`, `RecordId` or `StringRecordId`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                The table name or a [`RecordId`](../data-types.md#recordid) to create.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `data`
               <label label="optional" />
            </td>
			<td colspan="2" scope="row" data-label="Type">
				`mixed`
			</td>
            <td colspan="2" scope="row" data-label="Description">
                The document / record data to create.
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php
// Create a record with a random ID
[$person] = $db->create('person');

// Create a record with a specific ID
$person = $db->create(new RecordId('person', 'tobie'), [
	"name" => 'Tobie',
	"settings" => [
		"active" => true,
		"marketing" => true,
	],
]);

// The content you are creating the record with might differ from the return type
[$record] = $db->create(
    new RecordId('person', 'tobie'),
    ["name" => "Tobie"]
);
```

### Translated query
This function will run the following query in the database.

```surql
CREATE $thing CONTENT $data;
```
