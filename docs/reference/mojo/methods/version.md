---
position: 28
title: version
description: The version() method for the SurrealDB Mojo SDK returns the database version.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/version.mdx"
---

# `version()`

Returns the version of the connected SurrealDB server as an `RpcResponse`.

```python title="Method Syntax"
client.version()
```

### Arguments

This method takes no arguments.

### Example usage

```python
var resp = client.version()
if resp.is_ok() and resp.result:
    print(resp.result.value())
```
