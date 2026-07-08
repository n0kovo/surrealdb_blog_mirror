---
position: 10
title: health
description: The health() method for the SurrealDB Mojo SDK runs a health check against the server.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/health.mdx"
---

# `health()`

Runs a health check to verify that the server is reachable and accepting commands.

```python title="Method Syntax"
client.health()
```

### Arguments

This method takes no arguments.

### Example usage

```python
client.health()
```

If the server is unreachable, the call raises a `ConnectionError`.
