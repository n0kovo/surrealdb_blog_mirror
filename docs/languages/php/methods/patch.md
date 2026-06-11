---
position: 1
title: patch
description: The ->patch() method for the SurrealDB SDK for PHP applies JSON patch changes to records in the database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/methods/patch.mdx"
---

# `->patch()` {#patch}

Applies JSON Patch changes to all records, or a specific record, in the database.

```php title="Method Syntax"
$db->patch($thing, $data, $diff)
```

> [!NOTE]
> This function patches the current document / record data with the specified JSON Patch data.

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
                The table name or the specific [`RecordId`](../data-types.md#recordid) to patch.
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
                The JSON Patch data with which to patch the records.
            </td>
        </tr>
		<tr>
			<td colspan="2" scope="row" data-label="Arguments">
				`diff`
			   <label label="optional" />
			</td>
			<td colspan="2" scope="row" data-label="Type">
				`boolean`
			</td>
			<td colspan="2" scope="row" data-label="Description">
				Whether to return the diff of the patched record.
			</td>
		</tr>
    </tbody>
</table>

### Example usage
```php
// Update all records in a table
$people = $db->patch('person', [
		[ "op" => 'replace', "path" => '/created_at',
	    "value" => new Date() ],
]);

// Update a record with a specific ID
$person = $db->patch(new RecordId('person', 'tobie'), [
		[ "op" => 'replace', "path" => '/settings/active',
	    "value" => false ],
		[ "op" => 'add', "path" => '/tags', "value" => ['developer',
	    'engineer'] ],
	[ "op" => 'remove', "path" => '/temp' ],
]);
```

### Translated query
This function will run the following query in the database.

```surql
UPDATE $thing PATCH $data;
```
