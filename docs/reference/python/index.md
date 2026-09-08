---
position: 1
title: Python SDK
description: The SurrealDB SDK for Python enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/python/index.mdx"
---

# Python SDK

The SurrealDB SDK for Python lets you connect to SurrealDB from any Python application. It supports both synchronous and asynchronous workflows, connecting to remote instances over WebSocket or HTTP, and running embedded databases in-process. The SDK provides methods for querying, managing data and authentication, and subscribing to real-time updates with live queries.

> [!IMPORTANT]
> The SDK requires Python `3.10` or later, and is available as a [PyPI package](https://pypi.org/project/surrealdb/).

> [!NOTE]
> The latest version of the SDK is *(latest)*.
> The SDK works with SurrealDB versions `v2.0.0` and later, including the current release, *(latest)*.

## Getting started

- **[Installation](installation.md)** — Install the SDK and add it to your project.
- **[Getting started guide](../../languages/python.md)** — Connect to SurrealDB and run your first queries.

## Learn

- **[Concepts](concepts/connecting-to-surrealdb.md)** — Guides for connecting, authenticating, querying, and working with data.
- **[API Reference](api/core/surreal.md)** — Complete reference for the SDK's methods, types, and errors.

## Concepts

- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md) - open a connection over HTTP or WebSocket
- [Authentication](concepts/authentication.md) - sign up, sign in, and authenticate with a token
- [Multiple sessions](concepts/multiple-sessions.md) - run isolated sessions over a single connection
- [Executing queries](concepts/executing-queries.md) - send SurrealQL and read the results back
- [Data manipulation](concepts/data-manipulation.md) - create, select, update, upsert and delete records
- [Value types](concepts/value-types.md) - how SurrealDB's types map onto native ones
- [Transactions](concepts/transactions.md) - group statements so they succeed or fail together
- [Live queries](concepts/live-queries.md) - stream changes as they happen
- [Error handling](concepts/error-handling.md) - what a failure looks like, and how to catch it
- [Embedded databases](concepts/embedded-databases.md) - run SurrealDB in-process for tests and local use

## Contributing

To contribute to the SDK code, submit an Issue or Pull Request in the [surrealdb.py](https://github.com/surrealdb/surrealdb.py) repository. To contribute to this documentation, submit an Issue or Pull Request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.py)
- [PyPI package](https://pypi.org/project/surrealdb/)
