---
position: 14
title: kill
description: The kill() method for the SurrealDB Mojo SDK stops a running live query.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/kill.mdx"
---

# `kill()`

Stops a running live query, using the query id returned by [`live_query()`](live.md).

```python title="Method Syntax"
client.kill(query_id, session)
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
            <td colspan="2" scope="row" data-label="Argument">`query_id`</td>
            <td colspan="2" scope="row" data-label="Description">The id of the live query to stop.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
var query_id = client.live_query("person")
# ... later ...
client.kill(query_id)
```

> [!NOTE]
> Live queries run over a stateful WebSocket session. WebSocket support is rolling out. On the HTTP transport, the SDK raises an `UnsupportedFeatureError`.

### See also

- [Live queries](../concepts/live-queries.md)
- [`live_query()`](live.md)
