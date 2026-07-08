---
position: 6
title: Transactions
description: Group operations into atomic transactions with the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/concepts/transactions.mdx"
---

# Transactions

[Transactions](../../query-language/language-primitives/transactions.md) group multiple operations so they either all succeed or all fail together. The Kotlin SDK exposes transactions as extension functions on a [session](multiple-sessions.md): a block form that commits or cancels automatically, and an explicit form for manual control.

> [!NOTE]
> Transactions require a stateful connection and are only available over the **WebSocket** transport. Check support with [`client.supports(SurrealFeature.Transactions)`](../api/core/surreal-client.md#supports).

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
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/transaction#transaction-block">`session.transaction { }`</a></td>
			<td scope="row" data-label="Description">Runs a block, committing or cancelling automatically</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/transaction#begin-transaction">`session.beginTransaction()`</a></td>
			<td scope="row" data-label="Description">Begins a transaction explicitly</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/transaction#commit">`tx.commit()`</a></td>
			<td scope="row" data-label="Description">Commits the transaction</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/transaction#cancel">`tx.cancel()`</a></td>
			<td scope="row" data-label="Description">Cancels the transaction</td>
		</tr>
	</tbody>
</table>

## Block form

The [`transaction { }`](../api/core/transaction.md#transaction-block) builder runs your block against a [`SurrealTransaction`](../api/core/transaction.md), commits it if the block returns normally, and cancels it if the block throws. The transaction is itself a queryable, so all the [CRUD builders](data-manipulation.md) are available scoped to it.

```kotlin

client.transaction {
    create(RecordId("person", "tx"))
        .content(buildJsonObject { put("name", "Tx") })
        .await()

    update(RecordId("counter", "1"))
        .content(buildJsonObject { put("hits", 2) })
        .await()
}
```

## Explicit form

For finer control, begin a transaction with [`.beginTransaction()`](../api/core/transaction.md#begin-transaction) and commit or cancel it yourself.

```kotlin

val tx = client.beginTransaction()
try {
    tx.create(Table("person"))
        .content(buildJsonObject { put("name", "Ada") })
        .await()
    tx.commit()
} catch (cause: Throwable) {
    tx.cancel()
    throw cause
}
```

## Learn more

- [Transaction reference](../api/core/transaction.md) for the full API
- [Multiple sessions](multiple-sessions.md) — transactions run within a session
- [SurrealQL transactions](../../query-language/language-primitives/transactions.md) for transaction semantics
