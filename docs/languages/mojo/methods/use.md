---
position: 27
title: use
description: The use() method for the SurrealDB Mojo SDK switches to a specific namespace and database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/use.mdx"
---

# `use()`

Switches the connection to a specific namespace and database.

```python title="Method Syntax"
client.use(namespace, database, session)
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
            <td colspan="2" scope="row" data-label="Argument">`namespace`</td>
            <td colspan="2" scope="row" data-label="Description">The namespace to switch to.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`database`</td>
            <td colspan="2" scope="row" data-label="Description">The database to switch to.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id to scope the change to a specific session.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
client.use("test", "test")
```
