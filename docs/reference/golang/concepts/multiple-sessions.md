---
position: 8
title: Multiple sessions
description: The Go SDK supports creating multiple isolated sessions on a single WebSocket connection, each with its own authentication and namespace.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/golang/concepts/multiple-sessions.mdx"
---

# Multiple sessions

Sessions allow you to create isolated contexts on a single WebSocket connection. Each session has its own authentication state, namespace and database selection, and connection variables. This is useful when a single application needs to serve multiple users or tenants over one connection.

Sessions require a WebSocket connection (`ws://` or `wss://`) and SurrealDB v3 or later.

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
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/session#attach">`db.Attach(ctx)`</a></td>
			<td scope="row" data-label="Description">Creates a new session on the connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/session#detach">`session.Detach(ctx)`</a></td>
			<td scope="row" data-label="Description">Removes the session from the server</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/session#id">`session.ID()`</a></td>
			<td scope="row" data-label="Description">Returns the session's UUID</td>
		</tr>
	</tbody>
</table>

## Creating a session

Call `.Attach()` on the `*DB` to create a new session. The session starts unauthenticated and without a selected namespace or database, so you must configure it before making queries.

```go
session, err := db.Attach(ctx)
if err != nil {
	log.Fatal(err)
}
defer session.Detach(ctx)

_, err = session.SignIn(ctx, surrealdb.Auth{
	Username: "root",
	Password: "root",
})
if err != nil {
	log.Fatal(err)
}

if err := session.Use(ctx, "my_ns", "my_db"); err != nil {
	log.Fatal(err)
}
```

## Querying with a session

Sessions satisfy the [`sendable`](../api/types/index.md#sendable) constraint, so all generic functions like [`Query`](../api/core/db.md#query), [`Select`](../api/core/db.md#select), [`Create`](../api/core/db.md#create), etc. accept a [`*Session`](../api/core/session.md) directly.

```go
results, err := surrealdb.Query[[]Person](ctx, session,
	"SELECT * FROM persons",
	nil,
)
```

Each session maintains its own state. Changes to variables, authentication, or namespace on one session do not affect the parent [`*DB`](../api/core/db.md) or other sessions.

## Session isolation

Sessions are fully isolated from each other and from the parent connection:

- Authentication is independent: signing in on a session does not affect other sessions or the [`*DB`](../api/core/db.md).
- [`.Use()`](../api/core/session.md#use) on a session does not change the namespace/database of other sessions.
- Variables set with [`.Let()`](../api/core/session.md#let) are scoped to the session.
- [Live queries](live-queries.md) started on a session are scoped to that session.

```go
sessionA, _ := db.Attach(ctx)
defer sessionA.Detach(ctx)

sessionB, _ := db.Attach(ctx)
defer sessionB.Detach(ctx)

sessionA.SignIn(ctx, surrealdb.Auth{Username: "admin", Password: "admin"})
sessionA.Use(ctx, "ns_a", "db_a")

sessionB.SignIn(ctx, surrealdb.Auth{Namespace: "ns_b", Database: "db_b", Access: "user_access", Username: "user1", Password: "pass1"})
sessionB.Use(ctx, "ns_b", "db_b")
```

## Starting transactions from a session

Sessions can start their own transactions using `.Begin()`. The transaction inherits the session's authentication and namespace context.

```go
tx, err := session.Begin(ctx)
if err != nil {
	log.Fatal(err)
}
defer tx.Cancel(ctx)

surrealdb.Create[any](ctx, tx, models.Table("events"), map[string]any{"type": "login"})

if err := tx.Commit(ctx); err != nil {
	log.Fatal(err)
}
```

See [Transactions](transactions.md) for more on interactive transactions.

## Detaching a session

Call [`.Detach()`](../api/core/session.md#detach) to remove the session from the server. After detaching, the session cannot be used and any operations on it return [`ErrSessionClosed`](../api/errors/index.md#sentinel-errors).

```go
if err := session.Detach(ctx); err != nil {
	log.Fatal(err)
}
```

Use `defer session.Detach(ctx)` immediately after `.Attach()` to ensure cleanup.

## Learn more

- [Session API reference](../api/core/session.md) for complete method signatures
- [Transactions](transactions.md) for interactive transaction support
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for WebSocket connection requirements
- [Errors reference](../api/errors/index.md) for session-related error types
