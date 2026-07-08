---
position: 6
title: Transactions
description: Run multiple statements atomically with version 2 of the PHP SDK, using a SurrealQL transaction block or explicit transaction handles.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/php/v2/concepts/transactions.mdx"
---

# Transactions

A transaction groups statements so they either all succeed or all fail. This keeps related changes consistent, for example when transferring a value between two records.

## Transaction blocks

The simplest approach wraps statements in [`BEGIN TRANSACTION`](../../../query-language/statements/begin.md) and [`COMMIT TRANSACTION`](../../../query-language/statements/commit.md) and runs them as a single query with `run()`. SurrealDB rolls back the whole block if any statement fails. This works over both WebSocket and HTTP.

```php
$db->run('
    BEGIN TRANSACTION;
    UPDATE account:one SET balance -= 100;
    UPDATE account:two SET balance += 100;
    COMMIT TRANSACTION;
');
```

Use [`CANCEL TRANSACTION`](../../../query-language/statements/cancel.md) inside the block, or a [`THROW`](../../../query-language/statements/throw.md) expression, to abort and roll back from within SurrealQL.

## Explicit transaction handles

For finer control over a WebSocket connection, the [`ConnectionController`](../api/core.md#connectioncontroller) exposes explicit transaction handles through `connection()`. Call `begin()` to start one, then `commit()` or `cancel()` with the returned handle.

```php
$txn = $db->connection()->begin();

try {
    // ... run statements bound to $txn ...
    $db->connection()->commit($txn);
} catch (\Throwable $error) {
    $db->connection()->cancel($txn);
    throw $error;
}
```

> [!NOTE]
> Explicit handles require the transactions feature, which depends on the WebSocket engine and a compatible server version. For most applications, a transaction block run with `run()` is simpler and works everywhere.

## Learn more

- [Surreal API reference](../api/core.md#connectioncontroller) for the transaction methods
- [Executing queries](executing-queries.md) for running statements
- [BEGIN](../../../query-language/statements/begin.md) and [COMMIT](../../../query-language/statements/commit.md) for the SurrealQL statements
