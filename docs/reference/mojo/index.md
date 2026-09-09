---
position: 1
title: Mojo SDK
description: The official SurrealDB SDK for Mojo. Simple and advanced querying of a remote database over HTTP, HTTPS, and WebSocket.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/index.mdx"
---

# Mojo SDK

The SurrealDB SDK for Mojo lets you connect to a SurrealDB instance from your Mojo applications and run queries, manage data, call database functions, authenticate, and subscribe to changes with live queries. It speaks both CBOR-RPC and JSON-RPC over the same `/rpc` endpoint, and ships transports for `http://`, `https://`, `ws://`, and `wss://`.

The SDK has no third-party Mojo dependencies. The transport sits on a small libc-socket layer, and TLS is backed by a thin OpenSSL FFI with certificate verification against the system root store.

> [!IMPORTANT]
> The SDK requires Mojo `>= 0.26.1.0, < 0.26.2.0`, and is managed with [pixi](https://pixi.sh/). The current SDK version is `0.2.0`.

> [!NOTE]
> The SDK works with SurrealDB `3.x`, ensuring compatibility with the latest version, *(latest)*.

## Getting started

- **[Installation](installation.md)** — Install the SDK and add it to your project.
- **[Getting started guide](../../languages/mojo.md)** — Connect to SurrealDB and run your first queries.

## Learn

- **[Concepts](concepts/connecting-to-surrealdb.md)** — Guides for connecting, authenticating, querying, and working with data.
- **[API Reference](methods/index.md)** — Complete reference for the SDK's methods, types, and errors.

## Concepts

- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md) - open a connection over HTTP or WebSocket
- [Authentication](concepts/authentication.md) - sign up, sign in, and authenticate with a token
- [Multiple sessions](concepts/multiple-sessions.md) - run isolated sessions over a single connection
- [Executing queries](concepts/executing-queries.md) - send SurrealQL and read the results back
- [Query builders](concepts/query-builders.md) - compose a query without writing the string yourself
- [Value types](concepts/value-types.md) - how SurrealDB's types map onto native ones
- [Transactions](concepts/transactions.md) - group statements so they succeed or fail together
- [Live queries](concepts/live-queries.md) - stream changes as they happen
- [Error handling](concepts/error-handling.md) - what a failure looks like, and how to catch it

## Choosing a client

The SDK provides two clients with the same surface:

- `AsyncSurrealClient` for asynchronous applications.
- `SurrealClient`, a thin blocking wrapper around the async client.

```python title="Async client"
from surrealdb import AsyncSurrealClient, ConnectOptions
from std.collections import Optional

def main():
    var client = AsyncSurrealClient()
    _ = client.connect(
        "http://localhost:8000/rpc",
        ConnectOptions(
            namespace=Optional(String("test")),
            database=Optional(String("test")),
            access_token=Optional(String("Basic cm9vdDpyb290")),  # root:secret
        ),
    )

    var resp = client.query("RETURN 1 + 1;")
    if resp.is_ok():
        print("result:", resp.result.value() if resp.result else "null")
    else:
        print("error:", resp.error_message().value())
```

## Transports

HTTP and HTTPS are the recommended transports for everyday querying, and are the most thoroughly tested path. WebSocket (`ws://` and `wss://`) unlocks SurrealDB's stateful features: authenticated sessions, server-side transactions that span multiple requests, and live-query notifications delivered out of band.

> [!NOTE]
> WebSocket support is rolling out. For request and response querying, including atomic multi-statement transactions, use the HTTP or HTTPS transport.

The wire format is configurable. CBOR is the default and the most compact on the wire; JSON is useful when you want to inspect traffic or proxy through a JSON-only gateway. See [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md) for the full set of options.

## Contributing
To contribute to the SDK code, submit an Issue or Pull Request in the [surrealdb.mojo](https://github.com/surrealdb/surrealdb.mojo) repository. To contribute to this documentation, submit an Issue or Pull Request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.

## Sources
- [GitHub repository](https://github.com/surrealdb/surrealdb.mojo)
