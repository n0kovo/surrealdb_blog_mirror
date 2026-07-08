---
position: 9
title: Transactions
description: The Go SDK supports interactive transactions that let you execute statements one at a time and conditionally commit or cancel.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/golang/concepts/transactions.mdx"
---

# Transactions

Interactive transactions let you group multiple operations into an atomic unit. Unlike text-based transactions (`BEGIN TRANSACTION; ... COMMIT;` — see the [query builder](query-builder.md#building-text-based-transactions) for composing those), interactive transactions allow you to execute statements one at a time, inspect results, and conditionally decide whether to commit or cancel.

Transactions require a WebSocket connection (`ws://` or `wss://`) and SurrealDB v3 or later.

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
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/db#begin">`db.Begin(ctx)`</a></td>
			<td scope="row" data-label="Description">Starts a transaction on the default session</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/session#begin">`session.Begin(ctx)`</a></td>
			<td scope="row" data-label="Description">Starts a transaction within a session</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/transaction#commit">`tx.Commit(ctx)`</a></td>
			<td scope="row" data-label="Description">Commits the transaction, applying all changes</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/transaction#cancel">`tx.Cancel(ctx)`</a></td>
			<td scope="row" data-label="Description">Cancels the transaction, discarding all changes</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/transaction#id">`tx.ID()`</a></td>
			<td scope="row" data-label="Description">Returns the transaction's UUID</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/golang/api/core/transaction#isclosed">`tx.IsClosed()`</a></td>
			<td scope="row" data-label="Description">Returns whether the transaction has been committed or canceled</td>
		</tr>
	</tbody>
</table>

## Starting a transaction

Call [`.Begin()`](../api/core/db.md#begin) on a [`*DB`](../api/core/db.md) or [`*Session`](../api/core/session.md) to start a transaction. The transaction inherits the authentication and namespace context from the connection or session that started it.

```go
tx, err := db.Begin(ctx)
if err != nil {
	log.Fatal(err)
}
defer tx.Cancel(ctx)
```

> [!NOTE]
> Always use `defer tx.Cancel(ctx)` immediately after `.Begin()`. If the transaction has already been committed, [`.Cancel()`](../api/core/transaction.md#cancel) returns [`ErrTransactionClosed`](../api/errors/index.md#sentinel-errors) but does not cause any harm.

## Executing operations within a transaction

Transactions satisfy the [`sendable`](../api/types/index.md#sendable) constraint, so all generic functions like [`Query`](../api/core/db.md#query), [`Select`](../api/core/db.md#select), [`Create`](../api/core/db.md#create), [`Update`](../api/core/db.md#update), and [`Delete`](../api/core/db.md#delete) accept a [`*Transaction`](../api/core/transaction.md).

```go
tx, err := db.Begin(ctx)
if err != nil {
	log.Fatal(err)
}
defer tx.Cancel(ctx)

_, err = surrealdb.Create[any](ctx, tx, models.Table("accounts"), map[string]any{
	"name":    "Alice",
	"balance": 1000,
})
if err != nil {
	log.Fatal(err)
}

_, err = surrealdb.Create[any](ctx, tx, models.Table("accounts"), map[string]any{
	"name":    "Bob",
	"balance": 500,
})
if err != nil {
	log.Fatal(err)
}

if err := tx.Commit(ctx); err != nil {
	log.Fatal(err)
}
```

Changes made within a transaction are not visible to other connections or sessions until the transaction is committed.

## Conditional commit or cancel

Because interactive transactions let you inspect results between operations, you can decide whether to commit based on runtime conditions.

```go
tx, err := db.Begin(ctx)
if err != nil {
	log.Fatal(err)
}
defer tx.Cancel(ctx)

results, err := surrealdb.Query[[]map[string]any](ctx, tx,
	"SELECT * FROM accounts WHERE name = 'Alice'",
	nil,
)
if err != nil {
	log.Fatal(err)
}

balance, ok := (*results)[0].Result[0]["balance"].(float64)
if !ok || balance < 100 {
	fmt.Println("Insufficient balance, canceling")
	return
}

_, err = surrealdb.Query[[]any](ctx, tx,
	"UPDATE accounts SET balance -= 100 WHERE name = 'Alice'; UPDATE accounts SET balance += 100 WHERE name = 'Bob';",
	nil,
)
if err != nil {
	log.Fatal(err)
}

if err := tx.Commit(ctx); err != nil {
	log.Fatal(err)
}
```

## Transaction limitations

Transactions do not support session state changes. The following operations are not available on a [`*Transaction`](../api/core/transaction.md):

- [`.SignIn()`](../api/core/db.md#signin), [`.SignUp()`](../api/core/db.md#signup), [`.Authenticate()`](../api/core/db.md#authenticate), [`.Invalidate()`](../api/core/db.md#invalidate)
- [`.Use()`](../api/core/db.md#use)
- [`.Let()`](../api/core/db.md#let), [`.Unset()`](../api/core/db.md#unset)
- [Live queries](live-queries.md) ([`Live`](../api/core/db.md#live), [`Kill`](../api/core/db.md#kill))

The namespace, database, authentication, and variables are inherited from the `*DB` or `*Session` that started the transaction.

## Learn more

- [Transaction API reference](../api/core/transaction.md) for complete method signatures
- [Multiple sessions](multiple-sessions.md) for session-scoped transactions
- [Error handling](error-handling.md) for transaction error types
- [SurrealQL transactions](../../query-language/statements/begin.md) for text-based transaction syntax
