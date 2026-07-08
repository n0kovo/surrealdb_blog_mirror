---
position: 11
title: insert
description: The insert() method for the SurrealDB Mojo SDK inserts one or more records into a table.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/insert.mdx"
---

# `insert()`

Inserts one or more records into a table. This is a convenience wrapper that runs `INSERT INTO <table> <data_json>;`.

```python title="Method Syntax"
client.insert(table, data_json, session, txn)
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
            <td colspan="2" scope="row" data-label="Argument">`table`</td>
            <td colspan="2" scope="row" data-label="Description">The table to insert into.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`data_json`</td>
            <td colspan="2" scope="row" data-label="Description">A single record or an array of records, as a JSON string.</td>
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
var resp = client.insert("person", '[{ "name": "Alice" }, { "name": "Bob" }]')
```

### Translated query

```surql
INSERT INTO $table $data_json;
```

### See also

- [`insert_relation()`](insert-relation.md)
