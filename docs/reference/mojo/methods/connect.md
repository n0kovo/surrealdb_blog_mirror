---
position: 7
title: connect
description: The connect() method for the SurrealDB Mojo SDK connects to a database endpoint.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/connect.mdx"
---

# `connect()`

Connects to a database endpoint. The URL scheme selects the transport (`http`, `https`, `ws`, or `wss`).

```python title="Method Syntax"
client.connect(endpoint, connect_options)
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
            <td colspan="2" scope="row" data-label="Argument">`endpoint`</td>
            <td colspan="2" scope="row" data-label="Description">The database endpoint to connect to, ending in `/rpc`.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`connect_options`</td>
            <td colspan="2" scope="row" data-label="Description">An optional `ConnectOptions` carrying the namespace, database, credentials, TLS setting, and wire format.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
from surrealdb import AsyncSurrealClient, ConnectOptions
from std.collections import Optional

def main():
    var client = AsyncSurrealClient()
    _ = client.connect(
        "http://localhost:8000/rpc",
        ConnectOptions(
            namespace=Optional(String("test")),
            database=Optional(String("test")),
            access_token=Optional(String("Basic cm9vdDpyb290")),
        ),
    )
```

`connect()` returns a `Bool`.

### See also

- [Connecting to SurrealDB](../concepts/connecting-to-surrealdb.md)
