---
position: 2
title: Transaction
description: The Transaction class provides methods for executing queries within an atomic transaction.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/api/core/transaction.mdx"
---

# `Transaction` {#transaction}

The `Transaction` class wraps a set of operations into an atomic unit. Changes made within a transaction are only applied when committed, and can be rolled back by cancelling. Transactions are created by calling [`.beginTransaction()`](surreal.md#begin-transaction) on a `Surreal` instance.

**Source:** [surrealdb.java](https://github.com/surrealdb/surrealdb.java)

---

## Methods

> [!NOTE]
> The `Transaction` class only supports `.query()` with raw SurrealQL strings. Parameterised queries via `.queryBind()` are not available inside transactions. To pass dynamic values, interpolate them directly in the SurrealQL string or use SurrealQL parameters defined earlier in the transaction.

### `.query(sql)` {#query}

Executes a SurrealQL query within the transaction. The query results are not visible outside the transaction until it is committed.

```java title="Method Syntax"
tx.query(sql)
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
            <td>`sql` *[required]*</td>
            <td>`String`</td>
            <td>The SurrealQL query string to execute within the transaction.</td>
        </tr>
    </tbody>
</table>

**Returns:** [`Response`](response.md)

```java title="Example"
Transaction tx = db.beginTransaction();
Response response = tx.query("CREATE person SET name = 'Alice'");
tx.commit();
```

### `.commit()` {#commit}

Commits the transaction, applying all changes made within it to the database. After committing, the transaction object should not be reused.

```java title="Method Syntax"
tx.commit()
```

**Returns:** `void`

```java title="Example"
Transaction tx = db.beginTransaction();
tx.query("CREATE person SET name = 'Alice'");
tx.query("CREATE person SET name = 'Bob'");
tx.commit();
```

### `.cancel()` {#cancel}

Cancels the transaction, discarding all changes made within it. No data is written to the database. After cancelling, the transaction object should not be reused.

```java title="Method Syntax"
tx.cancel()
```

**Returns:** `void`

```java title="Example"
Transaction tx = db.beginTransaction();
tx.query("DELETE person");
tx.cancel();
```

---

## Complete example

```java title="Atomic transfer"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("bank").useDb("ledger");
    db.signin(new RootCredential("root", "root"));

    Transaction tx = db.beginTransaction();
    try {
        tx.query("UPDATE accounts:alice SET balance = balance - 200");
        tx.query("UPDATE accounts:bob SET balance = balance + 200");
        tx.commit();
    } catch (Exception e) {
        tx.cancel();
        throw e;
    }
}
```

---

## See also

- [Surreal](surreal.md) — Connection and method reference
- [Response](response.md) — Query response reference
- [Transactions](../../concepts/transactions.md) — Transaction concepts and patterns
- [SurrealQL BEGIN](../../../query-language/statements/begin.md) — Server-side transaction syntax
