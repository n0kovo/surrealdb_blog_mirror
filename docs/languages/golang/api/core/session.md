---
position: 2
title: Session
description: The Session struct represents an isolated SurrealDB session on a WebSocket connection with its own authentication and namespace state.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/api/core/session.mdx"
---

# `Session` {#session}

The `Session` struct represents an additional SurrealDB session on a WebSocket connection. Each session has its own authentication state, namespace and database selection, and connection variables. Sessions require SurrealDB v3+ and a WebSocket connection.

`Session` satisfies the [`sendable`](../types/index.md#sendable) constraint, so all generic functions like [`Query`](db.md#query), [`Select`](db.md#select), [`Create`](db.md#create), etc. accept `*Session` directly.

**Source:** [session.go](https://github.com/surrealdb/surrealdb.go/blob/main/session.go)

---

## Creating a session

### `db.Attach()` {#attach}

Creates a new session on the WebSocket connection. The session starts unauthenticated and without a selected namespace or database.

```go title="Syntax"
session, err := db.Attach(ctx)
```

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`ctx` *[required]*</td>
            <td>`context.Context`</td>
            <td>Context for the operation.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*Session, error)`

Returns `ErrSessionsNotSupported` if the connection is not WebSocket.

#### Examples

```go
session, err := db.Attach(ctx)
if err != nil {
    log.Fatal(err)
}
defer session.Detach(ctx)

session.SignIn(ctx, surrealdb.Auth{Username: "root",
    Password: "root"})
session.Use(ctx, "my_ns", "my_db")

results, err := surrealdb.Query[[]Person](ctx, session,
    "SELECT * FROM persons", nil)
```

---

## Properties

### `.ID()` {#id}

Returns the session's UUID.

```go title="Syntax"
id := session.ID()
```

**Returns:** [`*models.UUID`](../values/uuid.md)

---

## Methods

### `.Detach()` {#detach}

Removes the session from the server. After calling `.Detach()`, the session cannot be used.

```go title="Syntax"
err := session.Detach(ctx)
```

**Returns:** `error`

Returns [`ErrSessionClosed`](../errors/index.md#sentinel-errors) if the session has already been detached.

### `.Begin()` {#begin}

Starts a new interactive transaction within this session.

```go title="Syntax"
tx, err := session.Begin(ctx)
```

**Returns:** `(*Transaction, error)` — see [`Transaction`](transaction.md)

Returns [`ErrSessionClosed`](../errors/index.md#sentinel-errors) if the session has been detached.

### `.SignIn()` {#signin}

Signs in an existing user within this session.

```go title="Syntax"
token, err := session.SignIn(ctx, authData)
```

**Returns:** `(string, error)`

### `.SignInWithRefresh()` {#signinwithrefresh}

Signs in with refresh token support within this session. SurrealDB v3+ only.

```go title="Syntax"
tokens, err := session.SignInWithRefresh(ctx, authData)
```

**Returns:** [`(*Tokens, error)`](../types/index.md#tokens)

### `.SignUp()` {#signup}

Signs up a new record user within this session.

```go title="Syntax"
token, err := session.SignUp(ctx, authData)
```

**Returns:** `(string, error)`

### `.SignUpWithRefresh()` {#signupwithrefresh}

Signs up with refresh token support within this session. SurrealDB v3+ only.

```go title="Syntax"
tokens, err := session.SignUpWithRefresh(ctx, authData)
```

**Returns:** [`(*Tokens, error)`](../types/index.md#tokens)

### `.Authenticate()` {#authenticate}

Authenticates this session with a JWT token.

```go title="Syntax"
err := session.Authenticate(ctx, token)
```

**Returns:** `error`

### `.Invalidate()` {#invalidate}

Invalidates the current authentication for this session.

```go title="Syntax"
err := session.Invalidate(ctx)
```

**Returns:** `error`

### `.Use()` {#use}

Selects the namespace and database for this session.

```go title="Syntax"
err := session.Use(ctx, ns, database)
```

**Returns:** `error`

### `.Let()` {#let}

Defines a variable scoped to this session.

```go title="Syntax"
err := session.Let(ctx, key, val)
```

**Returns:** `error`

### `.Unset()` {#unset}

Removes a variable from this session.

```go title="Syntax"
err := session.Unset(ctx, key)
```

**Returns:** `error`

### `.Info()` {#info}

Returns the record of the currently authenticated user in this session.

```go title="Syntax"
info, err := session.Info(ctx)
```

**Returns:** `(map[string]any, error)`

### `.Version()` {#version}

Returns the SurrealDB version information.

```go title="Syntax"
ver, err := session.Version(ctx)
```

**Returns:** [`(*VersionData, error)`](../types/index.md#versiondata)

### `.LiveNotifications()` {#livenotifications}

Returns the notification channel for a live query.

```go title="Syntax"
ch, err := session.LiveNotifications(liveQueryID)
```

**Returns:** `(chan` [`connection.Notification`](../types/index.md#notification)`, error)`

### `.CloseLiveNotifications()` {#closelivenotifications}

Closes the notification channel for a live query.

```go title="Syntax"
err := session.CloseLiveNotifications(liveQueryID)
```

**Returns:** `error`

---

## See also

- [DB](db.md) for the main client reference
- [Transaction](transaction.md) for session-scoped transactions
- [Multiple sessions](../../concepts/multiple-sessions.md) for session usage patterns
- [Errors](../errors/index.md) for `ErrSessionClosed` and `ErrSessionsNotSupported`
