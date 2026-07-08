---
position: 1
title: Features & Events
description: Transport feature flags and connection lifecycle events in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/api/features/index.mdx"
---

# Features and events {#features-and-events}

The SDK exposes the capabilities of the active transport as a set of [`SurrealFeature`](#feature) values, and the lifecycle of the connection as a stream of [`SurrealConnectionEvent`](#connection-events).

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## `SurrealFeature` {#feature}

An enum of the features a transport may support. Inspect the active set via the [`features`](../core/surreal-client.md#properties) property, or check a single feature with [`.supports()`](../core/surreal-client.md#supports).

<table>
    <thead>
        <tr><th>Value</th><th>Available on</th></tr>
    </thead>
    <tbody>
        <tr><td>`LiveQueries`</td><td>WebSocket</td></tr>
        <tr><td>`Transactions`</td><td>WebSocket</td></tr>
        <tr><td>`Sessions`</td><td>WebSocket</td></tr>
        <tr><td>`RefreshTokens`</td><td>WebSocket</td></tr>
        <tr><td>`ExportImport`</td><td>WebSocket, HTTP</td></tr>
        <tr><td>`SurrealML`</td><td>WebSocket, HTTP</td></tr>
    </tbody>
</table>

```kotlin title="Example"
if (client.supports(SurrealFeature.LiveQueries)) {
    val subscription = client.live("person")
}
```

---

## `SurrealConnectionEvent` {#connection-events}

A sealed class emitted on the client's [`connectionEvents`](../core/surreal-client.md#properties) [`SharedFlow`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-shared-flow/).

<table>
    <thead>
        <tr><th>Variant</th><th>Payload</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`Connecting`</td><td>—</td><td>A connection attempt has started.</td></tr>
        <tr><td>`Connected`</td><td>—</td><td>The connection is established.</td></tr>
        <tr><td>`Disconnected`</td><td>—</td><td>The connection has dropped.</td></tr>
        <tr><td>`Reconnecting`</td><td>`attempt: Int`, `delayMillis: Long`</td><td>A reconnect is scheduled.</td></tr>
        <tr><td>`Error`</td><td>`cause: Throwable`</td><td>A connection error occurred.</td></tr>
    </tbody>
</table>

```kotlin title="Example"
client.connectionEvents.collect { event ->
    when (event) {
        is SurrealConnectionEvent.Connected -> println("connected")
        is SurrealConnectionEvent.Reconnecting -> println("attempt ${event.attempt}")
        is SurrealConnectionEvent.Error -> println("error: ${event.cause.message}")
        else -> {}
    }
}
```

## Learn more

- [Connecting to SurrealDB](../../concepts/connecting-to-surrealdb.md)
- [SurrealClient API reference](../core/surreal-client.md)
