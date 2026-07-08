---
position: 2
title: api
description: The api() method for the SurrealDB Mojo SDK calls a custom API handler defined on the database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/api.mdx"
---

# `api()`

Calls a custom API handler defined on the database with [`DEFINE API`](https://surrealdb.com/docs/surrealql/statements/define/api).

```python title="Method Syntax"
client.api(path, method, session, txn)
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
            <td colspan="2" scope="row" data-label="Argument">`path`</td>
            <td colspan="2" scope="row" data-label="Description">The API path to call.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`method`</td>
            <td colspan="2" scope="row" data-label="Description">The HTTP method. Defaults to `"GET"`.</td>
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
var resp = client.api("/users", "GET")
```

> [!NOTE]
> The API endpoint is checked against the active transport's capabilities. If the transport does not support it, the SDK raises an `UnsupportedFeatureError`.
