---
position: 2
title: Installation
description: In this section, you will learn how to install the Python SDK in your project.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/python/installation.mdx"
---

# Installation

In this section, you will learn how to install the Python SDK in your project.

### Install the SDK

Install the [SurrealDB SDK](https://pypi.org/project/surrealdb/) from PyPI:

```bash
pip install surrealdb
```

If you want [pydantic](https://docs.pydantic.dev/) validation and serialization support for `RecordID`, install the optional extra:

```bash
pip install surrealdb[pydantic]
```

### Import the SDK into your project

The SDK provides two entry points depending on whether you need synchronous or asynchronous access.

```python
from surrealdb import Surreal
```

For asynchronous applications using `asyncio`:

```python
from surrealdb import AsyncSurreal
```

Both `Surreal` and `AsyncSurreal` are factory functions that accept a connection URL and return the appropriate connection class based on the protocol scheme.

## Next steps

- [Getting started](../../languages/python.md) for a complete working example
- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md) for connection options and protocols
- [Authentication](concepts/authentication.md) for signing in and managing credentials
