---
position: 26
title: upsert
description: The upsert() method for the SurrealDB Mojo SDK upserts all records in a table, or a specific record.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/upsert.mdx"
---

# `upsert()`

Creates a record if it does not exist, or updates it if it does. This is a convenience wrapper that runs `UPSERT <thing> CONTENT <content_json>;`.

```python title="Method Syntax"
client.upsert(thing, content_json, session, txn)
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
            <td colspan="2" scope="row" data-label="Description">The table or specific record to upsert.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`content_json`</td>
            <td colspan="2" scope="row" data-label="Description">The record content as a JSON string.</td>
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
var resp = client.upsert("person:chiru", '{ "name": "Chiru", "age": 31 }')
```

### Translated query

```surql
UPSERT $thing CONTENT $content_json;
```
