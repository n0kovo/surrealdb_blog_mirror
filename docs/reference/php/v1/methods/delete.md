---
position: 1
title: delete
description: Delete records from a table in the database using the delete method with the SurrealDB PHP SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/php/v1/methods/delete.mdx"
---

# `->delete()` {#delete}

Deletes all records in a table, or a specific record, from the database.

```php title="Method Syntax"
$db->delete($thing)
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
                The table name or a [`RecordId`](../concepts/data-types.md#recordid) to delete.
            </td>
        </tr>
    </tbody>
</table>

### Example usage
```php
// Delete all records from a table
$db->delete('person');

// Delete a specific record from a table
$db->delete(new RecordId('person', 'h5wxrf2ewk8xjxosxtyc'));
```

### Translated query
This function will run the following query in the database.

```surql
DELETE $thing;
```
