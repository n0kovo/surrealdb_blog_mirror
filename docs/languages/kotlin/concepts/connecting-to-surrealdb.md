---
position: 1
title: Connecting to SurrealDB
description: The Kotlin SDK connects to SurrealDB over WebSocket or HTTP, with automatic transport selection and reconnection.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/concepts/connecting-to-surrealdb.mdx"
---

# Connecting to SurrealDB

The first step towards interacting with [SurrealDB](https://surrealdb.com/docs/start) is to create a connection to a database instance. This involves constructing a [`SurrealClient`](../api/core/surreal-client.md) with a [`SurrealClientConfig`](../api/core/client-config.md), then selecting a namespace and database. The SDK supports remote connections over WebSocket and HTTP.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#constructor">`SurrealClient(config)`</a></td>
			<td scope="row" data-label="Description">Creates a new client from a configuration</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#connect">`client.connect()`</a></td>
			<td scope="row" data-label="Description">Establishes the connection explicitly</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#close">`client.close()`</a></td>
			<td scope="row" data-label="Description">Closes the connection and releases resources</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#use">`client.use(ns, db)`</a></td>
			<td scope="row" data-label="Description">Selects a namespace and database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#version">`client.version()`</a></td>
			<td scope="row" data-label="Description">Returns the server version</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#ping">`client.ping()`</a></td>
			<td scope="row" data-label="Description">Pings the server</td>
		</tr>
	</tbody>
</table>

## Opening a connection

Construct a [`SurrealClient`](../api/core/surreal-client.md) with a [`SurrealClientConfig`](../api/core/client-config.md) whose `url` points at your SurrealDB instance. By default (`autoConnect = true`) the client connects lazily on the first request, so you rarely need to call [`.connect()`](../api/core/surreal-client.md#connect) yourself.

```kotlin

val client = SurrealClient(SurrealClientConfig(url = "ws://localhost:8000"))
```

## Connection string protocols

The URL scheme determines the transport. For more on server configuration, see the [start command](../../../reference/cli/surrealdb-cli/commands/start.md) documentation.

| Protocol | Description |
|---|---|
| `ws://` | Plain WebSocket connection |
| `wss://` | Secure WebSocket connection (TLS) |
| `http://` | Plain HTTP connection |
| `https://` | Secure HTTP connection (TLS) |

The WebSocket engine maintains a single long-lived connection, while the HTTP engine issues a request per call.

## Feature support by protocol

Not all features are available on every transport. You can check support at runtime with [`.supports()`](../api/core/surreal-client.md#supports); unsupported calls throw [`SurrealFeatureNotSupportedException`](../api/errors/index.md).

| Feature | WebSocket | HTTP |
|---|---|---|
| Authentication | Yes | Yes |
| Queries | Yes | Yes |
| CRUD operations | Yes | Yes |
| Live queries | Yes | No |
| Transactions | Yes | No |
| Multiple sessions | Yes | No |
| Refresh tokens | Yes | No |
| Export / Import | Yes | Yes |
| SurrealML | Yes | Yes |

See [Features and events](../api/features/index.md) for the full [`SurrealFeature`](../api/features/index.md#feature) enum.

## Selecting a namespace and database

After connecting, select a [namespace](../../../reference/query-language/statements/define/namespace.md) and [database](../../../reference/query-language/statements/define/database.md) with [`.use()`](../api/core/surreal-client.md#use).

```kotlin
client.use("surrealdb", "docs")
```

## Reconnection

The WebSocket engine automatically reconnects with exponential backoff. Tune this through the [`ReconnectConfig`](../api/core/client-config.md#reconnect-config) on your [`SurrealClientConfig`](../api/core/client-config.md).

```kotlin

val client = SurrealClient(
    SurrealClientConfig(
        url = "wss://example.com",
        reconnect = ReconnectConfig(
            enabled = true,
            initialDelayMillis = 250,
            maxDelayMillis = 30_000,
            multiplier = 1.5,
            maxAttempts = null, // null means retry indefinitely
        ),
    ),
)
```

## Observing connection events

The client exposes a [`connectionEvents`](../api/features/index.md#connection-events) [`SharedFlow`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-shared-flow/) you can collect to react to lifecycle changes.

```kotlin

scope.launch {
    client.connectionEvents.collect { event ->
        when (event) {
            is SurrealConnectionEvent.Connected -> println("connected")
            is SurrealConnectionEvent.Reconnecting -> println("reconnecting, attempt ${event.attempt}")
            is SurrealConnectionEvent.Disconnected -> println("disconnected")
            is SurrealConnectionEvent.Error -> println("error: ${event.cause.message}")
            else -> {}
        }
    }
}
```

## Closing a connection

Call [`.close()`](../api/core/surreal-client.md#close) to release all resources associated with the connection.

```kotlin
client.close()
```

## Learn more

- [SurrealClient API reference](../api/core/surreal-client.md) for complete method signatures
- [Client configuration](../api/core/client-config.md) for all configuration options
- [Authentication](authentication.md) for signing in and managing sessions
- [Error handling](error-handling.md) for handling connection errors
