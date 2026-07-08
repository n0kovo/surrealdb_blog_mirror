---
position: 3
title: SurrealSession
description: The SurrealSession class exposes querying and authentication with isolated per-session state.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/api/core/session.mdx"
---

# `SurrealSession` {#surreal-session}

`SurrealSession` is the base class of [`SurrealClient`](surreal-client.md) and the type returned by [`.newSession()`](surreal-client.md#new-session). It exposes the full querying, authentication, and CRUD API with state — authentication, namespace, database, and parameters — isolated to that session. See [Multiple sessions](../../concepts/multiple-sessions.md) for the concept.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

---

## Shared API

Because [`SurrealClient`](surreal-client.md) extends `SurrealSession`, every session — root or child — provides the same methods documented on the client:

- Connection: [`.use()`](surreal-client.md#use), [`.ping()`](surreal-client.md#ping), [`.version()`](surreal-client.md#version)
- Authentication: [`.signin()`](surreal-client.md#signin), [`.signup()`](surreal-client.md#signup), [`.authenticate()`](surreal-client.md#authenticate), [`.auth()`](surreal-client.md#auth), [`.invalidate()`](surreal-client.md#invalidate), [`.reset()`](surreal-client.md#reset)
- Queries: [`.query()`](surreal-client.md#query), [`.queryAs<T>()`](surreal-client.md#query-as), [`.let()`](surreal-client.md#let), [`.unset()`](surreal-client.md#unset)
- CRUD builders: [`.select()`](surreal-client.md#select), [`.create()`](surreal-client.md#create), [`.update()`](surreal-client.md#update), [`.upsert()`](surreal-client.md#upsert), [`.merge()`](surreal-client.md#merge), [`.patch()`](surreal-client.md#patch), [`.delete()`](surreal-client.md#delete), [`.relate()`](surreal-client.md#relate), [`.insert()`](surreal-client.md#insert)
- Live queries: [`.live()`](surreal-client.md#live), [`.kill()`](surreal-client.md#kill)

## Session state accessors

<table>
    <thead>
        <tr><th>Method</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`.namespace()`</td><td>`String?`</td><td>The session's current namespace.</td></tr>
        <tr><td>`.database()`</td><td>`String?`</td><td>The session's current database.</td></tr>
        <tr><td>`.accessToken()`</td><td>`String?`</td><td>The session's current access token, if authenticated.</td></tr>
    </tbody>
</table>

## Creating and closing sessions

```kotlin title="Example"
val session = client.newSession()
session.signin(buildJsonObject { put("user", "a"); put("pass", "a") })
session.use("acme", "main")

// ... use the session ...

client.closeSession(session)
```

## Transactions

Transactions are started on a session via the [`transaction { }`](transaction.md#transaction-block) and [`beginTransaction()`](transaction.md#begin-transaction) extension functions. See the [Transaction reference](transaction.md).

## Learn more

- [SurrealClient API reference](surreal-client.md)
- [Multiple sessions](../../concepts/multiple-sessions.md)
- [Transaction reference](transaction.md)
