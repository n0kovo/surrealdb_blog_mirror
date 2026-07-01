---
position: 1
title: merge
description: The ->merge() method for the SurrealDB SDK for PHP merges record data with the specified data.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v1/methods/merge.mdx"
---

# `->merge()` {#merge}

Modifies all records in a table, or a specific record, in the database.

```php title="Method Syntax"
$db->merge($thing, $data)
```

> [!NOTE]
> This function merges the current document / record data with the specified data.

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
                The table name or the specific [`RecordId`](../concepts/data-types.md#recordid) to merge.
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
                The document / record data to merge.
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php

// Update all records in a table
$people = $db->merge('person', [
	"updated_at" => new Date(),
]);

// Update a record with a specific ID
$person = $db->merge(new RecordId('person', 'tobie'), [
	"updated_at" => new Date(),
	"settings" => [
		"active" => true,
	],
]);

// The content you are merging the record with might differ from the return type
$record = $db->merge(new RecordId('person', 'tobie'), [
	"name" => 'Tobie',
]);
```

### Translated query
This function will run the following query in the database.

```surql
UPDATE $thing MERGE $data;
```
