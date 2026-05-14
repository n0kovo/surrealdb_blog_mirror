---
position: 1
title: DB
description: The DB struct is the main entry point for connecting to and interacting with a SurrealDB instance from Go.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/api/core/db.mdx"
---

# `DB` {#db}

The `DB` struct is the main client for interacting with SurrealDB. It holds the underlying connection and provides methods for [authentication](../../concepts/authentication.md), namespace selection, and [live query](../../concepts/live-queries.md) management. Data operations are performed through generic top-level functions that accept `*DB` as a parameter.

**Source:** [db.go](https://github.com/surrealdb/surrealdb.go/blob/main/db.go)

---

## Constructors

### `FromEndpointURLString` {#fromendpointurlstring}

Creates a new `*DB` and connects to a SurrealDB instance. The URL scheme determines the connection type (WebSocket or HTTP).

```go title="Syntax"
db, err := surrealdb.FromEndpointURLString(ctx, connectionURL)
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
            <td>Context for canceling the connection attempt.</td>
        </tr>
        <tr>
            <td>`connectionURL` *[required]*</td>
            <td>`string`</td>
            <td>The endpoint URL. Supported schemes: `ws://`, `wss://`, `http://`, `https://`.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*DB, error)`

#### Examples

```go title="WebSocket"
db, err := surrealdb.FromEndpointURLString(ctx, "ws://localhost:8000")
```

```go title="HTTPS"
db, err := surrealdb.FromEndpointURLString(ctx, "https://cloud.surrealdb.com")
```

### `FromConnection` {#fromconnection}

Creates a new `*DB` from a custom `connection.Connection` implementation. Calls `.Connect(ctx)` automatically.

```go title="Syntax"
db, err := surrealdb.FromConnection(ctx, conn)
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
            <td>Context for canceling the connection attempt.</td>
        </tr>
        <tr>
            <td>`conn` *[required]*</td>
            <td>`connection.Connection`</td>
            <td>A connection implementation (e.g., `gorillaws.New(conf)` or `http.New(conf)`).</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*DB, error)`

---

## Connection methods

### `.Close()` {#close}

Closes the underlying connection and releases resources.

```go title="Syntax"
err := db.Close(ctx)
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
            <td>Context for the close operation.</td>
        </tr>
    </tbody>
</table>

**Returns:** `error`

### `.Use()` {#use}

Selects the namespace and database to use for subsequent operations.

```go title="Syntax"
err := db.Use(ctx, ns, database)
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
        <tr>
            <td>`ns` *[required]*</td>
            <td>`string`</td>
            <td>The namespace to use.</td>
        </tr>
        <tr>
            <td>`database` *[required]*</td>
            <td>`string`</td>
            <td>The database to use.</td>
        </tr>
    </tbody>
</table>

**Returns:** `error`

### `.Version()` {#version}

Returns version information about the connected SurrealDB instance.

```go title="Syntax"
ver, err := db.Version(ctx)
```

**Returns:** `(*VersionData, error)`, see [`VersionData`](../types/index.md#versiondata)

#### Examples

```go
ver, err := db.Version(ctx)
if err != nil {
    log.Fatal(err)
}
fmt.Println(ver.Version)
```

---

## Authentication methods

### `.SignIn()` {#signin}

Signs in an existing user. The fields provided in `authData` determine the authentication level (root, namespace, database, or record).

```go title="Syntax"
token, err := db.SignIn(ctx, authData)
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
        <tr>
            <td>`authData` *[required]*</td>
            <td>`any`</td>
            <td>An <a href="/docs/languages/golang/api/types#auth">`Auth`</a> struct or `map[string]any` with credentials.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(string, error)` — the JWT token string

#### Examples

```go title="Root signin"
token, err := db.SignIn(ctx, surrealdb.Auth{
    Username: "root",
    Password: "root",
})
```

```go title="Record signin"
token, err := db.SignIn(ctx, map[string]any{
    "NS": "my_ns", "DB": "my_db", "AC": "user_access",
    "user": "tobie", "pass": "s3cret",
})
```

### `.SignInWithRefresh()` {#signinwithrefresh}

Signs in using a `TYPE RECORD` access method with `WITH REFRESH` enabled. Returns both an access token and a refresh token. SurrealDB v3+ only.

```go title="Syntax"
tokens, err := db.SignInWithRefresh(ctx, authData)
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
        <tr>
            <td>`authData` *[required]*</td>
            <td>`any`</td>
            <td>Credentials as `map[string]any`. Use `"refresh"` key for token refresh.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*Tokens, error)` — see [`Tokens`](../types/index.md#tokens)

#### Examples

```go title="Initial signin"
tokens, err := db.SignInWithRefresh(ctx, map[string]any{
    "NS": "my_ns", "DB": "my_db", "AC": "user_access",
    "user": "tobie", "pass": "s3cret",
})
```

```go title="Refresh"
newTokens, err := db.SignInWithRefresh(ctx, map[string]any{
    "NS": "my_ns", "DB": "my_db", "AC": "user_access",
    "refresh": tokens.Refresh,
})
```

### `.SignUp()` {#signup}

Signs up a new record user.

```go title="Syntax"
token, err := db.SignUp(ctx, authData)
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
        <tr>
            <td>`authData` *[required]*</td>
            <td>`any`</td>
            <td>An <a href="/docs/languages/golang/api/types#auth">`Auth`</a> struct or `map[string]any` with signup credentials.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(string, error)` — the JWT token string

### `.SignUpWithRefresh()` {#signupwithrefresh}

Signs up using a `TYPE RECORD` access method with `WITH REFRESH` enabled. SurrealDB v3+ only.

```go title="Syntax"
tokens, err := db.SignUpWithRefresh(ctx, authData)
```

**Returns:** `(*Tokens, error)` — see [`Tokens`](../types/index.md#tokens)

### `.Authenticate()` {#authenticate}

Authenticates the connection with a JWT token.

```go title="Syntax"
err := db.Authenticate(ctx, token)
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
        <tr>
            <td>`token` *[required]*</td>
            <td>`string`</td>
            <td>The JWT token to authenticate with.</td>
        </tr>
    </tbody>
</table>

**Returns:** `error`

### `.Invalidate()` {#invalidate}

Invalidates the current authentication, returning the connection to an unauthenticated state.

```go title="Syntax"
err := db.Invalidate(ctx)
```

**Returns:** `error`

### `.Info()` {#info}

Returns the record of the currently authenticated user.

```go title="Syntax"
info, err := db.Info(ctx)
```

**Returns:** `(map[string]any, error)`

---

## Variables

### `.Let()` {#let}

Defines a variable on the connection that can be used in subsequent queries.

```go title="Syntax"
err := db.Let(ctx, key, val)
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
        <tr>
            <td>`key` *[required]*</td>
            <td>`string`</td>
            <td>The variable name (without `$` prefix).</td>
        </tr>
        <tr>
            <td>`val` *[required]*</td>
            <td>`any`</td>
            <td>The value to assign.</td>
        </tr>
    </tbody>
</table>

**Returns:** `error`

### `.Unset()` {#unset}

Removes a previously defined variable from the connection.

```go title="Syntax"
err := db.Unset(ctx, key)
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
        <tr>
            <td>`key` *[required]*</td>
            <td>`string`</td>
            <td>The variable name to remove.</td>
        </tr>
    </tbody>
</table>

**Returns:** `error`

---

## Sessions and transactions

### `.Attach()` {#attach}

Creates a new session on the WebSocket connection. Sessions are only supported on WebSocket connections (SurrealDB v3+).

```go title="Syntax"
session, err := db.Attach(ctx)
```

**Returns:** `(*Session, error)` — see [`Session`](session.md)

### `.Begin()` {#begin}

Starts a new interactive transaction on the default session. Transactions are only supported on WebSocket connections (SurrealDB v3+).

```go title="Syntax"
tx, err := db.Begin(ctx)
```

**Returns:** `(*Transaction, error)` — see [`Transaction`](transaction.md)

---

## Query functions

These are top-level generic functions that accept [`*DB`](#db), [`*Session`](session.md), or [`*Transaction`](transaction.md) as the `s` parameter.

### `Query` {#query}

Executes a SurrealQL query string and returns typed results.

```go title="Syntax"
results, err := surrealdb.Query[TResult](ctx, s, sql, vars)
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
            <td>`TResult`</td>
            <td>type parameter</td>
            <td>The expected result type for each statement.</td>
        </tr>
        <tr>
            <td>`ctx` *[required]*</td>
            <td>`context.Context`</td>
            <td>Context for the operation.</td>
        </tr>
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session | *Transaction`</td>
            <td>The sender to execute the query on.</td>
        </tr>
        <tr>
            <td>`sql` *[required]*</td>
            <td>`string`</td>
            <td>The SurrealQL query string.</td>
        </tr>
        <tr>
            <td>`vars` *[required]*</td>
            <td>`map[string]any`</td>
            <td>Variables to bind into the query. Pass `nil` for no variables.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*[]QueryResult[TResult], error)` — see [`QueryResult`](../types/index.md#queryresult)

#### Examples

```go
results, err := surrealdb.Query[[]Person](ctx, db,
    "SELECT * FROM persons WHERE age > $min",
    map[string]any{"min": 18},
)
```

### `QueryRaw` {#queryraw}

Composes and executes a batch of query statements with per-statement results.

```go title="Syntax"
err := surrealdb.QueryRaw(ctx, s, queries)
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
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session | *Transaction`</td>
            <td>The sender to execute the query on.</td>
        </tr>
        <tr>
            <td>`queries` *[required]*</td>
            <td>`*[]QueryStmt`</td>
            <td>A pointer to a slice of <a href="/docs/languages/golang/api/types#querystmt">`QueryStmt`</a> objects. Results are written back to each statement.</td>
        </tr>
    </tbody>
</table>

**Returns:** `error`

---

## Data functions

These are top-level generic functions that accept [`*DB`](#db), [`*Session`](session.md), or [`*Transaction`](transaction.md) as the `s` parameter.

### `Select` {#select}

Retrieves records from the database.

```go title="Syntax"
result, err := surrealdb.Select[TResult](ctx, s, what)
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
            <td>`TResult`</td>
            <td>type parameter</td>
            <td>Use a slice type for tables, a single type for record IDs.</td>
        </tr>
        <tr>
            <td>`ctx` *[required]*</td>
            <td>`context.Context`</td>
            <td>Context for the operation.</td>
        </tr>
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session | *Transaction`</td>
            <td>The sender.</td>
        </tr>
        <tr>
            <td>`what` *[required]*</td>
            <td>`string |` <a href="/docs/languages/golang/api/values/table">`Table`</a> `|` <a href="/docs/languages/golang/api/values/record-id">`RecordID`</a></td>
            <td>The table or record to select.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*TResult, error)`

### `Create` {#create}

Creates a new record.

```go title="Syntax"
result, err := surrealdb.Create[TResult](ctx, s, what, data)
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
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session | *Transaction`</td>
            <td>The sender.</td>
        </tr>
        <tr>
            <td>`what` *[required]*</td>
            <td>`string |` <a href="/docs/languages/golang/api/values/table">`Table`</a> `|` <a href="/docs/languages/golang/api/values/record-id">`RecordID`</a></td>
            <td>The table or record ID to create.</td>
        </tr>
        <tr>
            <td>`data` *[required]*</td>
            <td>`any`</td>
            <td>The record data (struct or map).</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*TResult, error)`

### `Insert` {#insert}

Inserts one or more records into a table.

```go title="Syntax"
results, err := surrealdb.Insert[TResult](ctx, s, table, data)
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
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session | *Transaction`</td>
            <td>The sender.</td>
        </tr>
        <tr>
            <td>`table` *[required]*</td>
            <td><a href="/docs/languages/golang/api/values/table">`models.Table`</a></td>
            <td>The table to insert into.</td>
        </tr>
        <tr>
            <td>`data` *[required]*</td>
            <td>`any`</td>
            <td>A single record or slice of records to insert.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*[]TResult, error)`

### `Update` {#update}

Replaces the entire content of a record (like a PUT).

```go title="Syntax"
result, err := surrealdb.Update[TResult](ctx, s, what, data)
```

**Returns:** `(*TResult, error)`

### `Upsert` {#upsert}

Creates a record if it does not exist, or replaces it entirely.

```go title="Syntax"
result, err := surrealdb.Upsert[TResult](ctx, s, what, data)
```

**Returns:** `(*TResult, error)`

### `Merge` {#merge}

Merges data into an existing record, preserving unmentioned fields.

```go title="Syntax"
result, err := surrealdb.Merge[TResult](ctx, s, what, data)
```

**Returns:** `(*TResult, error)`

### `Patch` {#patch}

Applies JSON Patch operations to a record or table.

```go title="Syntax"
result, err := surrealdb.Patch(ctx, s, what, patches)
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
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session | *Transaction`</td>
            <td>The sender.</td>
        </tr>
        <tr>
            <td>`what` *[required]*</td>
            <td>`string |` <a href="/docs/languages/golang/api/values/table">`Table`</a> `|` <a href="/docs/languages/golang/api/values/record-id">`RecordID`</a></td>
            <td>The table or record to patch.</td>
        </tr>
        <tr>
            <td>`patches` *[required]*</td>
            <td>`[]PatchData`</td>
            <td>JSON Patch operations. See <a href="/docs/languages/golang/api/types#patchdata">`PatchData`</a>.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*[]PatchData, error)`

### `Delete` {#delete}

Removes records from the database.

```go title="Syntax"
result, err := surrealdb.Delete[TResult](ctx, s, what)
```

**Returns:** `(*TResult, error)`

### `Relate` {#relate}

Creates a relationship between two records with an auto-generated ID.

```go title="Syntax"
result, err := surrealdb.Relate[TResult](ctx, s, rel)
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
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session | *Transaction`</td>
            <td>The sender.</td>
        </tr>
        <tr>
            <td>`rel` *[required]*</td>
            <td>`*Relationship`</td>
            <td>The relationship to create. See <a href="/docs/languages/golang/api/types#relationship">`Relationship`</a>.</td>
        </tr>
    </tbody>
</table>

**Returns:** `(*TResult, error)`

### `InsertRelation` {#insertrelation}

Inserts a relation record, optionally with a specified ID.

```go title="Syntax"
result, err := surrealdb.InsertRelation[TResult](ctx, s, rel)
```

**Returns:** `(*TResult, error)`

---

## Live query methods

### `Live` {#live}

Starts a live query on a table. Only available on `*DB` and `*Session`.

```go title="Syntax"
liveID, err := surrealdb.Live(ctx, s, table, diff)
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
        <tr>
            <td>`s` *[required]*</td>
            <td>`*DB | *Session`</td>
            <td>The sender (not `*Transaction`).</td>
        </tr>
        <tr>
            <td>`table` *[required]*</td>
            <td><a href="/docs/languages/golang/api/values/table">`models.Table`</a></td>
            <td>The table to watch.</td>
        </tr>
        <tr>
            <td>`diff` *[required]*</td>
            <td>`bool`</td>
            <td>If `true`, notifications contain JSON Patch diffs.</td>
        </tr>
    </tbody>
</table>

**Returns:** [`(*models.UUID, error)`](../values/uuid.md)

### `Kill` {#kill}

Terminates a live query and closes its notification channel.

```go title="Syntax"
err := surrealdb.Kill(ctx, s, id)
```

**Returns:** `error`

### `.LiveNotifications()` {#livenotifications}

Returns the notification channel for a live query.

```go title="Syntax"
ch, err := db.LiveNotifications(liveQueryID)
```

**Returns:** `(chan` [`connection.Notification`](../types/index.md#notification)`, error)`

### `.CloseLiveNotifications()` {#closelivenotifications}

Closes the notification channel without killing the server-side live query.

```go title="Syntax"
err := db.CloseLiveNotifications(liveQueryID)
```

**Returns:** `error`

---

## Low-level RPC

### `Send` {#send}

Sends a raw RPC request to SurrealDB. Limited to data methods: `select`, `create`, `insert`, `insert_relation`, `kill`, `live`, `merge`, `relate`, `update`, `upsert`, `patch`, `delete`, `query`.

```go title="Syntax"
err := surrealdb.Send[Result](ctx, db, res, method, params...)
```

**Returns:** `error`

---

## See also

- [Session](session.md) for session management reference
- [Transaction](transaction.md) for transaction reference
- [Types](../types/index.md) for type definitions used by these methods
- [Errors](../errors/index.md) for error types
- [Connecting to SurrealDB](../../concepts/connecting-to-surrealdb.md) for connection patterns
