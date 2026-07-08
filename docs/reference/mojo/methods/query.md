---
position: 18
title: query
description: The query() method for the SurrealDB Mojo SDK runs one or more SurrealQL statements against the database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/query.mdx"
---

# `query()`

Runs one or more SurrealQL statements against the database and returns an `RpcResponse`.

```python title="Method Syntax"
client.query(query, bindings_json, session, txn)
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
            <td colspan="2" scope="row" data-label="Argument">`query`</td>
            <td colspan="2" scope="row" data-label="Description">The SurrealQL statements to run.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`bindings_json`</td>
            <td colspan="2" scope="row" data-label="Description">Optional bindings as a JSON string. Defaults to `"{}"`.</td>
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
var resp = client.query("SELECT * FROM person WHERE age > 18;")

if resp.is_ok():
    if resp.result:
        print(resp.result.value())
else:
    print("error:", resp.error_message().value())
```

> [!NOTE]
> A dedicated API for passing arbitrary CBOR bindings is on the roadmap. Today, CBOR connections support the default `"{}"`, while JSON-RPC connections accept raw JSON strings via `bindings_json`.

### See also

- [Executing queries](../concepts/executing-queries.md)
