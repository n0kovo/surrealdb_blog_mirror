---
position: 3
title: Transaction
description: The Transaction struct represents an interactive SurrealDB transaction that allows executing statements one at a time with commit or cancel control.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/api/core/transaction.mdx"
---

# `Transaction` {#transaction}

The `Transaction` struct represents an interactive SurrealDB transaction on a WebSocket connection. Unlike text-based transactions, interactive transactions allow executing statements one at a time and conditionally committing or canceling based on results. Transactions require SurrealDB v3+ and a WebSocket connection.

`Transaction` satisfies the [`sendable`](../types/index.md#sendable) constraint, so all generic functions like [`Query`](db.md#query), [`Select`](db.md#select), [`Create`](db.md#create), etc. accept `*Transaction` directly. However, transactions do not support session state changes (authentication, namespace selection, variables) or [live queries](../../concepts/live-queries.md).

**Source:** [transaction.go](https://github.com/surrealdb/surrealdb.go/blob/main/transaction.go)

---

## Creating a transaction

### `db.Begin()` {#db-begin}

Starts a transaction on the default session.

```go title="Syntax"
tx, err := db.Begin(ctx)
```

**Returns:** `(*Transaction, error)`

Returns [`ErrTransactionsNotSupported`](../errors/index.md#sentinel-errors) if the connection is not WebSocket.

### `session.Begin()` {#session-begin}

Starts a transaction within a specific session.

```go title="Syntax"
tx, err := session.Begin(ctx)
```

**Returns:** `(*Transaction, error)`

Returns [`ErrSessionClosed`](../errors/index.md#sentinel-errors) if the session has been detached.

#### Examples

```go
tx, err := db.Begin(ctx)
if err != nil {
    log.Fatal(err)
}
defer tx.Cancel(ctx)

_, err = surrealdb.Create[any](ctx, tx, models.Table("events"), map[string]any{
    "type": "transfer",
    "amount": 100,
})
if err != nil {
    log.Fatal(err)
}

if err := tx.Commit(ctx); err != nil {
    log.Fatal(err)
}
```

---

## Properties

### `.ID()` {#id}

Returns the transaction's UUID.

```go title="Syntax"
id := tx.ID()
```

**Returns:** [`*models.UUID`](../values/uuid.md)

### `.SessionID()` {#sessionid}

Returns the session UUID if the transaction was started within a [`Session`](session.md). Returns `nil` for transactions started on the default session.

```go title="Syntax"
sessionID := tx.SessionID()
```

**Returns:** [`*models.UUID`](../values/uuid.md)

### `.IsClosed()` {#isclosed}

Returns whether the transaction has been committed or canceled.

```go title="Syntax"
closed := tx.IsClosed()
```

**Returns:** `bool`

---

## Methods

### `.Commit()` {#commit}

Commits the transaction, making all changes permanent. After calling `.Commit()`, the transaction cannot be used.

```go title="Syntax"
err := tx.Commit(ctx)
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

**Returns:** `error`

Returns [`ErrTransactionClosed`](../errors/index.md#sentinel-errors) if the transaction has already been committed or canceled.

### `.Cancel()` {#cancel}

Cancels the transaction, discarding all changes. After calling `.Cancel()`, the transaction cannot be used.

It is safe to call `.Cancel()` on an already committed or canceled transaction. It returns [`ErrTransactionClosed`](../errors/index.md#sentinel-errors) but causes no harm, making it safe for use with `defer`.

```go title="Syntax"
err := tx.Cancel(ctx)
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

**Returns:** `error`

---

## See also

- [DB](db.md) for starting transactions from the main client
- [Session](session.md) for starting transactions from sessions
- [Transactions](../../concepts/transactions.md) for transaction usage patterns
- [Errors](../errors/index.md) for `ErrTransactionClosed` and `ErrTransactionsNotSupported`
