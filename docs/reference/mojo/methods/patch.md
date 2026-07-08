---
position: 17
title: patch
description: The patch() method for the SurrealDB Mojo SDK applies a JSON Patch to a record.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/patch.mdx"
---

# `patch()`

Applies a JSON Patch to all records in a table, or a specific record. This is a convenience wrapper that runs `UPDATE <thing> PATCH <patch_json>;`.

```python title="Method Syntax"
client.patch(thing, patch_json, session, txn)
```

### Arguments

<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Argument</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`thing`</td>
            <td colspan="2" scope="row" data-label="Description">The table or specific record to patch.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`patch_json`</td>
            <td colspan="2" scope="row" data-label="Description">A JSON Patch array as a JSON string.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`txn`</td>
            <td colspan="2" scope="row" data-label="Description">An optional transaction id.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
var resp = client.patch("person:chiru", '[{ "op": "replace", "path": "/age", "value": 31 }]')
```

### Translated query

```surql
UPDATE $thing PATCH $patch_json;
```
