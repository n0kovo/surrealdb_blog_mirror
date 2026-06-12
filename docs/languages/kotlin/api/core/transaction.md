---
position: 6
title: SurrealTransaction
description: The transaction handle and helpers for atomic operations in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/api/core/transaction.mdx"
---

# `SurrealTransaction` {#surreal-transaction}

`SurrealTransaction` represents an in-progress [transaction](../../concepts/transactions.md). It is itself a queryable, so the [CRUD builders](query-builder.md) are available scoped to the transaction. Transactions are started with the extension functions on a [session](session.md) and require the **WebSocket** transport.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## `session.transaction { }` {#transaction-block}

Runs the block against a new `SurrealTransaction`, committing it if the block returns normally and cancelling it if the block throws.

```kotlin title="Method Syntax"
session.transaction { /* ... */ }
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`block` *[required]*</td>
            <td>`suspend SurrealTransaction.() -&gt; Unit`</td>
            <td>The operations to run inside the transaction.</td>
        </tr>
    </tbody>
</table>

**Returns:** `Unit`

```kotlin title="Example"
client.transaction {
    create(RecordId("person", "tx"))
        .content(buildJsonObject { put("name", "Tx") })
        .await()
}
```

## `session.beginTransaction()` {#begin-transaction}

Begins a transaction explicitly and returns a `SurrealTransaction` for manual commit or cancel.

```kotlin title="Method Syntax"
session.beginTransaction()
```

**Returns:** `SurrealTransaction`

```kotlin title="Example"
val tx = client.beginTransaction()
try {
    tx.create(Table("person")).content(buildJsonObject { put("name", "Ada") }).await()
    tx.commit()
} catch (cause: Throwable) {
    tx.cancel()
    throw cause
}
```

---

## Methods

### `.commit()` {#commit}

Commits the transaction, persisting all its operations.

```kotlin title="Method Syntax"
tx.commit()
```

**Returns:** `Unit`

### `.cancel()` {#cancel}

Cancels the transaction, discarding all its operations.

```kotlin title="Method Syntax"
tx.cancel()
```

**Returns:** `Unit`

## Properties

<table>
    <thead>
        <tr><th>Property</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`txnId`</td><td>`String`</td><td>The transaction's identifier.</td></tr>
    </tbody>
</table>

## Learn more

- [Transactions](../../concepts/transactions.md)
- [Session](session.md)
- [Query builders](query-builder.md)
