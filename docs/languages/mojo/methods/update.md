---
position: 25
title: update
description: The update() method for the SurrealDB Mojo SDK updates all records in a table, or a specific record.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/update.mdx"
---

# `update()`

Updates all records in a table, or a specific record, replacing their content. This is a convenience wrapper that runs `UPDATE <thing> CONTENT <content_json>;`.

```python title="Method Syntax"
client.update(thing, content_json, session, txn)
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
            <td colspan="2" scope="row" data-label="Description">The table or specific record to update.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`content_json`</td>
            <td colspan="2" scope="row" data-label="Description">The replacement content as a JSON string.</td>
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
var resp = client.update("person:chiru", '{ "age": 31 }')
```

### Translated query

```surql
UPDATE $thing CONTENT $content_json;
```
