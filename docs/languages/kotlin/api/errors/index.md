---
position: 1
title: Errors
description: The exception hierarchy raised by the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/api/errors/index.mdx"
---

# Errors {#errors}

The Kotlin SDK raises exceptions that all extend the sealed base class `SurrealException`. Because the hierarchy is sealed, you can branch over it exhaustively with `when`. See [Error handling](../../concepts/error-handling.md) for usage patterns and the [`Result` variants](../../concepts/executing-queries.md#result-variants) that avoid exceptions altogether.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## `SurrealException` {#surreal-exception}

The sealed base class of all SDK exceptions. Extends `RuntimeException`.

## `SurrealTransportException` {#transport}

Raised when the underlying connection fails, drops, or cannot be established.

## `SurrealProtocolException` {#protocol}

Raised when a malformed or unexpected message is received from the server.

## `SurrealRpcException` {#rpc}

Raised when the server returns an RPC error.

<table>
    <thead>
        <tr><th>Property</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`code`</td><td>`Int?`</td><td>The RPC error code.</td></tr>
        <tr><td>`data`</td><td>`JsonElement?`</td><td>Additional error data from the server.</td></tr>
    </tbody>
</table>

## `SurrealAuthenticationException` {#authentication}

A subclass of [`SurrealRpcException`](#rpc) raised when authentication fails (for example, invalid credentials or an expired token).

## `SurrealFeatureNotSupportedException` {#feature-not-supported}

Raised when a feature is invoked that the current transport does not support — for example a [live query](../../concepts/live-queries.md) or [transaction](../../concepts/transactions.md) over HTTP. Extends the base [`SurrealException`](#surreal-exception). Guard against it with [`.supports()`](../core/surreal-client.md#supports).

```kotlin title="Example"

try {
    client.signin(buildJsonObject { put("user", "root"); put("pass", "wrong") })
} catch (e: SurrealAuthenticationException) {
    println("authentication failed: ${e.message}")
} catch (e: SurrealException) {
    println("error: ${e.message}")
}
```

## Learn more

- [Error handling](../../concepts/error-handling.md)
- [Features and events](../features/index.md)
