---
position: 1
title: update
description: The ->update() method for the SurrealDB SDK for Rust updates all or specific records in the database if they exist.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/php/v1/methods/update.mdx"
---

# `->update()` {#update}

Updates all records in a table, or a specific record, in the database.

```php title="Method Syntax"
$db->update($thing, $data)
```

> [!NOTE]
> This function replaces the current document / record data with the specified data.

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
                The table name or the specific [`RecordId`](../concepts/data-types.md#recordid) to update.
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
                The document / record data to update.
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php
// Update all records in a table
$people = $db->update('person');

// Update a record with a specific ID
$person = $db->update(new RecordId('person', 'tobie'), [
	"name" => 'Tobie',
	"settings" => [
		"active" => true,
		"marketing" => true,
	],
]);

// The content you are updating the record with might differ from the return type
$record = $db->update(new RecordId('person', 'tobie'), [
	"name" => 'Tobie',
]);
```

### Translated query
This function will run the following query in the database.

```surql
UPDATE $thing CONTENT $data;
```
