---
position: 16
title: merge
description: The merge() method for the SurrealDB Mojo SDK merges data into a record.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/merge.mdx"
---

# `merge()`

Merges data into all records in a table, or a specific record, leaving unspecified fields untouched. This is a convenience wrapper that runs `UPDATE <thing> MERGE <data_json>;`.

```python title="Method Syntax"
client.merge(thing, data_json, session, txn)
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
            <td colspan="2" scope="row" data-label="Description">The table or specific record to merge into.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`data_json`</td>
            <td colspan="2" scope="row" data-label="Description">The data to merge, as a JSON string.</td>
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
var resp = client.merge("person:chiru", '{ "age": 31 }')
```

### Translated query

```surql
UPDATE $thing MERGE $data_json;
```
