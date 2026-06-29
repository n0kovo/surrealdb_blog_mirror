---
position: 3
title: SurrealTransaction
description: Transaction scope for executing multiple operations atomically.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/api/core/surreal-transaction.mdx"
---

# `AsyncSurrealTransaction` / `BlockingSurrealTransaction` {#surreal-transaction}

A transaction wraps a connection with both a session ID and a transaction ID, scoping all operations to a single atomic unit. Changes are applied only when the transaction is committed, and can be rolled back with cancel.

Transactions are created by calling [`.begin_transaction()`](surreal-session.md#begin-transaction) on a session. They are **not** available on HTTP or embedded connections.

> [!NOTE]
> Transactions require a WebSocket connection (`ws://` or `wss://`). They must be created from a session via `.begin_transaction()`.

**Source:** [`async_ws.py`](https://github.com/surrealdb/surrealdb.py/blob/main/src/surrealdb/connections/async_ws.py) · [`blocking_ws.py`](https://github.com/surrealdb/surrealdb.py/blob/main/src/surrealdb/connections/blocking_ws.py)

---

## Creating a transaction {#creating}

```python title="Method Syntax"
txn = session.begin_transaction()
```

**Returns (sync):** `BlockingSurrealTransaction`
**Returns (async):** `AsyncSurrealTransaction`

### Examples

```python title="Synchronous"
from surrealdb import Surreal

db = Surreal("ws://localhost:8000")
db.connect()
db.signin({"username": "root", "password": "root"})
db.use("my_namespace", "my_database")

session = db.new_session()
session.use("my_namespace", "my_database")

txn = session.begin_transaction()
txn.create("users", {"name": "Alice"})
txn.commit()
```

```python title="Asynchronous"
from surrealdb import AsyncSurreal

db = AsyncSurreal("ws://localhost:8000")
await db.connect()
await db.signin({"username": "root", "password": "root"})
await db.use("my_namespace", "my_database")

session = await db.new_session()
await session.use("my_namespace", "my_database")

txn = await session.begin_transaction()
await txn.create("users", {"name": "Alice"})
await txn.commit()
```

---

## Inherited methods {#inherited-methods}

A transaction exposes query and CRUD methods that mirror the parent connection's interface. All operations are scoped to this transaction and are not visible outside it until committed. For full parameter tables and examples, see the [Surreal](surreal.md) reference.

| Method | Returns | Description |
|---|---|---|
| [`.query(query, vars)`](surreal.md#query) | Awaitable / lazy `Value` or `tuple[Value, ...]` builder | Execute one or more SurrealQL statements within the transaction. |
| [`.select(record)`](surreal.md#select) | [`Value`](../types/index.md#value) | Select records. |
| [`.create(record, data)`](surreal.md#create) | CRUD builder -> `dict[str, Value]` | Create a record (chain `.content/.replace/.merge/.patch`). |
| [`.update(record, data)`](surreal.md#update) | CRUD builder -> `dict` or `list` | Update records (chain `.content/.replace/.merge/.patch`). |
| [`.upsert(record, data)`](surreal.md#upsert) | CRUD builder -> `dict` or `list` | Upsert a record (chain `.content/.replace/.merge/.patch`). |
| [`.delete(record)`](surreal.md#delete) | CRUD builder -> `dict` or `list` | Delete records. |
| [`.insert(table, data, relation=False)`](surreal.md#insert) | Insert builder -> `list[Value]` | Insert records. Pass `relation=True` or chain `.relation()` for `INSERT RELATION`. |
| [`.run(name, args, version)`](surreal.md#run) | [`Value`](../types/index.md#value) | Call a SurrealDB function within the transaction. |
| [`.let(key, value)`](surreal.md#let) | `None` | Set a transaction-scoped variable. |
| [`.unset(key)`](surreal.md#unset) | `None` | Unset a transaction-scoped variable. |

---

## Transaction-specific methods

### `.commit()` {#commit}

Commits the transaction, applying all changes made within it to the database. After committing, the transaction object should not be used.

```python title="Method Syntax"
txn.commit()
```

**Returns:** `None`

#### Examples

```python title="Synchronous"
txn = session.begin_transaction()
txn.create("users", {"name": "Alice", "email": "alice@example.com"})
txn.create("users", {"name": "Bob", "email": "bob@example.com"})
txn.commit()
```

```python title="Asynchronous"
txn = await session.begin_transaction()
await txn.create("users", {"name": "Alice", "email": "alice@example.com"})
await txn.create("users", {"name": "Bob", "email": "bob@example.com"})
await txn.commit()
```

### `.cancel()` {#cancel}

Cancels the transaction, discarding all changes made within it. No data is written to the database. After cancelling, the transaction object should not be used.

```python title="Method Syntax"
txn.cancel()
```

**Returns:** `None`

#### Examples

```python title="Synchronous"
txn = session.begin_transaction()
txn.delete("users")
txn.cancel()
```

```python title="Asynchronous"
txn = await session.begin_transaction()
await txn.delete("users")
await txn.cancel()
```

```python title="Rollback on error"
txn = session.begin_transaction()
try:
    txn.create("orders", {"product": "Laptop", "qty": 1})
    txn.update(RecordID("inventory", "laptop"), {"stock": -1})
    txn.commit()
except Exception:
    txn.cancel()
```

---

## Complete example

```python title="Atomic transfer (sync)"
from surrealdb import Surreal, RecordID

with Surreal("ws://localhost:8000") as db:
    db.use("bank", "ledger")
    db.signin({"username": "root", "password": "root"})

    session = db.new_session()
    session.use("bank", "ledger")

    session.create(RecordID("accounts", "alice"), {"balance": 1000})
    session.create(RecordID("accounts", "bob"), {"balance": 500})

    txn = session.begin_transaction()
    try:
        txn.query(
            "UPDATE accounts:alice SET balance = balance - $amount",
            {"amount": 200},
        )
        txn.query(
            "UPDATE accounts:bob SET balance = balance + $amount",
            {"amount": 200},
        )
        txn.commit()
        print("Transfer committed")
    except Exception:
        txn.cancel()
        print("Transfer rolled back")

    accounts = session.select("accounts")
    print("Accounts:", accounts)

    session.close_session()
```

```python title="Atomic transfer (async)"
from surrealdb import AsyncSurreal, RecordID

async def main():
    async with AsyncSurreal("ws://localhost:8000") as db:
        await db.use("bank", "ledger")
        await db.signin({"username": "root", "password": "root"})

        session = await db.new_session()
        await session.use("bank", "ledger")

        await session.create(RecordID("accounts", "alice"), {"balance": 1000})
        await session.create(RecordID("accounts", "bob"), {"balance": 500})

        txn = await session.begin_transaction()
        try:
            await txn.query(
                "UPDATE accounts:alice SET balance = balance - $amount",
                {"amount": 200},
            )
            await txn.query(
                "UPDATE accounts:bob SET balance = balance + $amount",
                {"amount": 200},
            )
            await txn.commit()
            print("Transfer committed")
        except Exception:
            await txn.cancel()
            print("Transfer rolled back")

        accounts = await session.select("accounts")
        print("Accounts:", accounts)

        await session.close_session()

asyncio.run(main())
```

---

## See also

- [SurrealSession](surreal-session.md) — Session management reference
- [Surreal](surreal.md) — Connection reference with full method documentation
- [Data types](../types/index.md) — Type aliases and value types
- [Errors](../errors/index.md) — Error classes reference
