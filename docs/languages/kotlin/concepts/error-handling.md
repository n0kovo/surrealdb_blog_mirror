---
position: 10
title: Error handling
description: Handle exceptions and feature-support errors raised by the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/concepts/error-handling.mdx"
---

# Error handling

Networked operations on the SDK throw a [`SurrealException`](../api/errors/index.md) on failure, or you can use the [`Result` variants](executing-queries.md#result-variants) to handle failures functionally without exceptions.

## Exception hierarchy

All SDK exceptions extend the sealed base [`SurrealException`](../api/errors/index.md).

| Exception | Raised when |
|---|---|
| [`SurrealTransportException`](../api/errors/index.md#transport) | The connection fails or drops |
| [`SurrealProtocolException`](../api/errors/index.md#protocol) | A malformed or unexpected protocol message is received |
| [`SurrealRpcException`](../api/errors/index.md#rpc) | The server returns an RPC error (carries `code` and `data`) |
| [`SurrealAuthenticationException`](../api/errors/index.md#authentication) | Authentication fails (a subclass of `SurrealRpcException`) |
| [`SurrealFeatureNotSupportedException`](../api/errors/index.md#feature-not-supported) | A feature is unavailable on the current transport |

## Catching exceptions

Because [`SurrealException`](../api/errors/index.md) is a sealed class, you can exhaustively branch on it with `when`.

```kotlin

try {
    client.signin(buildJsonObject {
        put("user", "root")
        put("pass", "wrong")
    })
} catch (e: SurrealAuthenticationException) {
    println("bad credentials: ${e.message}")
} catch (e: SurrealRpcException) {
    println("server error ${e.code}: ${e.message}")
} catch (e: SurrealTransportException) {
    println("connection problem: ${e.message}")
} catch (e: SurrealException) {
    println("unexpected: ${e.message}")
}
```

## Feature support errors

Calling a feature that the current transport does not support — for example a [live query](live-queries.md) over HTTP — throws [`SurrealFeatureNotSupportedException`](../api/errors/index.md#feature-not-supported). Guard against this with [`.supports()`](../api/core/surreal-client.md#supports).

```kotlin

if (client.supports(SurrealFeature.LiveQueries)) {
    val subscription = client.live("person")
}
```

## Using Result variants

Each networked method has a `...Result` companion that wraps the outcome in a [`Result`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-result/) instead of throwing.

```kotlin
client.queryResult("SELECT * FROM person")
    .onSuccess { println("got $it") }
    .onFailure { println("failed: ${it.message}") }
```

## Learn more

- [Errors reference](../api/errors/index.md) for every exception type
- [Features and events](../api/features/index.md) for checking transport support
- [Executing queries](executing-queries.md) for the `Result` variants
