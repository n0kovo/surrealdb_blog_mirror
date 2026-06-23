---
position: 24
title: unset
description: The unset() method for the SurrealDB Mojo SDK removes a parameter for this connection.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/unset.mdx"
---

# `unset()`

Removes a parameter previously assigned with [`set()`](set.md).

```python title="Method Syntax"
client.unset(name, session)
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
            <td colspan="2" scope="row" data-label="Argument">`name`</td>
            <td colspan="2" scope="row" data-label="Description">The parameter name to remove.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
client.unset("name")
```
