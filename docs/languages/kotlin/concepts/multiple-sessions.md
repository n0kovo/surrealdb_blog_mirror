---
position: 7
title: Multiple sessions
description: Isolate authentication and state across concurrent sessions with the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/concepts/multiple-sessions.mdx"
---

# Multiple sessions

A single WebSocket connection can host multiple independent **sessions**, each with its own authentication, namespace, database, and parameters. This is useful for multi-tenant applications where requests act on behalf of different users over one shared connection. The [`SurrealClient`](../api/core/surreal-client.md) is itself the root session.

> [!NOTE]
> Multiple sessions require a stateful connection and are only available over the **WebSocket** transport. Check support with [`client.supports(SurrealFeature.Sessions)`](../api/core/surreal-client.md#supports).

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
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#new-session">`client.newSession()`</a></td>
			<td scope="row" data-label="Description">Creates a new isolated session</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#close-session">`client.closeSession(session)`</a></td>
			<td scope="row" data-label="Description">Closes a session</td>
		</tr>
	</tbody>
</table>

## Creating sessions

Each session created with [`.newSession()`](../api/core/surreal-client.md#new-session) is a [`SurrealSession`](../api/core/session.md) that exposes the same querying and authentication API as the client, but with isolated state.

```kotlin

val tenantA = client.newSession()
val tenantB = client.newSession()

tenantA.signin(buildJsonObject { put("user", "a"); put("pass", "a") })
tenantA.use("acme", "main")

tenantB.signin(buildJsonObject { put("user", "b"); put("pass", "b") })
tenantB.use("globex", "main")

// Each query runs as its own authenticated tenant, isolated from the other.
val aPeople = tenantA.query("SELECT * FROM person")
val bPeople = tenantB.query("SELECT * FROM person")
```

## Closing sessions

Close a session with [`.closeSession()`](../api/core/surreal-client.md#close-session) when you no longer need it. This does not close the underlying connection.

```kotlin
client.closeSession(tenantA)
```

## Learn more

- [Session reference](../api/core/session.md) for the session API
- [Authentication](authentication.md) for per-session credentials
- [Transactions](transactions.md) — transactions run within a session
