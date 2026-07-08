---
position: 7
title: Transactions
description: The Java SDK supports client-side transactions for grouping multiple queries into an atomic unit.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/concepts/transactions.mdx"
---

# Transactions

The Java SDK supports client-side [transactions](../../query-language/statements/begin.md) for grouping multiple queries into an atomic unit. All queries within a [`Transaction`](../api/core/transaction.md) are isolated from other operations and are either applied together on commit or discarded entirely on cancel.

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
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/surreal#begin-transaction">`db.beginTransaction()`</a></td>
			<td scope="row" data-label="Description">Starts a new transaction</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/transaction#query">`tx.query(sql)`</a></td>
			<td scope="row" data-label="Description">Executes a query within the transaction</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/transaction#commit">`tx.commit()`</a></td>
			<td scope="row" data-label="Description">Commits the transaction</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/transaction#cancel">`tx.cancel()`</a></td>
			<td scope="row" data-label="Description">Cancels (rolls back) the transaction</td>
		</tr>
	</tbody>
</table>

## Starting a transaction

The [`.beginTransaction()`](../api/core/surreal.md#begin-transaction) method returns a [`Transaction`](../api/core/transaction.md) object. All queries executed through this object are isolated until the transaction is committed or cancelled.

```java
Transaction tx = db.beginTransaction();
```

## Executing queries in a transaction

The [`tx.query()`](../api/core/transaction.md#query) method works like `db.query()` but executes within the transaction scope. Each call returns a [`Response`](../api/core/response.md) that you can inspect immediately, but the underlying changes are not visible outside the transaction until it is committed.

> [!NOTE]
> Parameterised queries via `.queryBind()` are not available inside transactions. To pass dynamic values, use SurrealQL `LET` statements or inline the values in the query string.

```java
Transaction tx = db.beginTransaction();
tx.query("CREATE account:one SET balance = 100");
tx.query("CREATE account:two SET balance = 0");
```

## Committing a transaction

Call [`.commit()`](../api/core/transaction.md#commit) to apply all changes atomically. Once committed, the changes become visible to other connections and queries.

```java
tx.commit();
```

## Cancelling a transaction

Call [`.cancel()`](../api/core/transaction.md#cancel) to discard all changes made within the transaction. Use a try-catch pattern to ensure the transaction is rolled back if any query fails.

```java
Transaction tx = db.beginTransaction();
try {
    tx.query("CREATE account:one SET balance = 100");
    tx.query("CREATE account:two SET balance = 0");
    tx.query("UPDATE account:one SET balance -= 50");
    tx.query("UPDATE account:two SET balance += 50");
    tx.commit();
} catch (SurrealException e) {
    tx.cancel();
    throw e;
}
```

## Learn more

- [Transaction API reference](../api/core/transaction.md) for complete method signatures
- [Executing queries](executing-queries.md) for query execution outside transactions
- [Error handling](error-handling.md) for handling transaction errors
- [SurrealQL BEGIN](../../query-language/statements/begin.md) for server-side transaction syntax
- [SurrealQL COMMIT](../../query-language/statements/commit.md) and [CANCEL](../../query-language/statements/cancel.md) for transaction control
