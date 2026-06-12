---
position: 5
title: LiveQuerySubscription
description: The subscription handle returned by live queries in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/api/core/live-subscription.mdx"
---

# `LiveQuerySubscription` {#live-query-subscription}

`LiveQuerySubscription` is returned by [`.live()`](surreal-client.md#live). It exposes a coroutine [`Flow`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-flow/) of notifications and a method to stop the subscription. See [Live queries](../../concepts/live-queries.md) for the concept.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Members

### `id` {#id}

The server-assigned live query ID.

**Type:** `String`

### `events` {#events}

A flow of [`SurrealLiveNotification`](#notification) events for this subscription.

**Type:** `Flow<SurrealLiveNotification>`

```kotlin title="Example"
subscription.events.collect { event ->
    println("${event.action}: ${event.result}")
}
```

### `.cancel()` {#cancel}

Stops the subscription and kills the underlying live query on the server.

```kotlin title="Method Syntax"
subscription.cancel()
```

**Returns:** `Unit`

---

## `SurrealLiveNotification` {#notification}

The payload emitted on the [`events`](#events) flow.

```kotlin title="Import"
```

<table>
    <thead>
        <tr><th>Field</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`action`</td><td>`String`</td><td>The change kind: `"CREATE"`, `"UPDATE"`, or `"DELETE"`.</td></tr>
        <tr><td>`liveQueryId`</td><td>`String`</td><td>The ID of the originating live query.</td></tr>
        <tr><td>`result`</td><td>`JsonElement`</td><td>The changed record or diff.</td></tr>
    </tbody>
</table>

## Learn more

- [Live queries](../../concepts/live-queries.md)
- [SurrealClient API reference](surreal-client.md) for `.live()` and `.kill()`
