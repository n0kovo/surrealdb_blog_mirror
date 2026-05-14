---
position: 2
title: SurrealSession
description: Isolated session for running queries with independent namespace, database, and authentication state.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/api/core/surreal-session.mdx"
---

# `AsyncSurrealSession` / `BlockingSurrealSession` {#surreal-session}

A session wraps a WebSocket connection with an isolated session ID. Each session maintains its own namespace, database, variables, and authentication state, independent of other sessions on the same connection.

Sessions are created by calling [`.new_session()`](surreal.md#new-session) on a WebSocket connection. They are **not** available on HTTP or embedded connections.

> [!NOTE]
> Sessions require a WebSocket connection (`ws://` or `wss://`). Attempting to create a session on an HTTP or embedded connection raises `UnsupportedFeatureError`.

**Source:** [`async_ws.py`](https://github.com/surrealdb/surrealdb.py/blob/main/src/surrealdb/connections/async_ws.py) · [`blocking_ws.py`](https://github.com/surrealdb/surrealdb.py/blob/main/src/surrealdb/connections/blocking_ws.py)

---

## Creating a session {#creating}

```python title="Method Syntax"
session = db.new_session()
```

**Returns (sync):** `BlockingSurrealSession`
**Returns (async):** `AsyncSurrealSession`

### Examples

```python title="Synchronous"
from surrealdb import Surreal

db = Surreal("ws://localhost:8000")
db.connect()
db.signin({"username": "root", "password": "root"})

session = db.new_session()
session.use("my_namespace", "my_database")
```

```python title="Asynchronous"
from surrealdb import AsyncSurreal

db = AsyncSurreal("ws://localhost:8000")
await db.connect()
await db.signin({"username": "root", "password": "root"})

session = await db.new_session()
await session.use("my_namespace", "my_database")
```

---

## Inherited methods {#inherited-methods}

A session exposes the same interface as the parent connection. All methods below delegate to the underlying connection, scoped to this session's ID. For full parameter tables and examples, see the [Surreal](surreal.md) reference.

| Method | Returns | Description |
|---|---|---|
| [`.use(namespace, database)`](surreal.md#use) | `None` | Switch namespace and database for this session. |
| [`.query(query, vars)`](surreal.md#query) | [`Value`](../types/index.md#value) | Execute a SurrealQL query. |
| [`.signin(vars)`](surreal.md#signin) | [`Tokens`](../types/index.md#tokens) | Sign in within this session. |
| [`.signup(vars)`](surreal.md#signup) | [`Tokens`](../types/index.md#tokens) | Sign up within this session. |
| [`.authenticate(token)`](surreal.md#authenticate) | `None` | Authenticate this session with a JWT. |
| [`.invalidate()`](surreal.md#invalidate) | `None` | Invalidate this session's authentication. |
| [`.let(key, value)`](surreal.md#let) | `None` | Define a session-scoped variable. |
| [`.unset(key)`](surreal.md#unset) | `None` | Remove a session-scoped variable. |
| [`.select(record)`](surreal.md#select) | [`Value`](../types/index.md#value) | Select records. |
| [`.create(record, data)`](surreal.md#create) | [`Value`](../types/index.md#value) | Create a record. |
| [`.update(record, data)`](surreal.md#update) | [`Value`](../types/index.md#value) | Replace a record. |
| [`.merge(record, data)`](surreal.md#merge) | [`Value`](../types/index.md#value) | Merge data into a record. |
| [`.patch(record, data)`](surreal.md#patch) | [`Value`](../types/index.md#value) | Apply JSON Patch operations. |
| [`.delete(record)`](surreal.md#delete) | [`Value`](../types/index.md#value) | Delete records. |
| [`.insert(table, data)`](surreal.md#insert) | [`Value`](../types/index.md#value) | Insert records. |
| [`.insert_relation(table, data)`](surreal.md#insert-relation) | [`Value`](../types/index.md#value) | Insert relation records. |
| [`.upsert(record, data)`](surreal.md#upsert) | [`Value`](../types/index.md#value) | Upsert a record. |
| [`.live(table, diff)`](surreal.md#live) | `UUID` | Start a live query. |
| [`.kill(query_uuid)`](surreal.md#kill) | `None` | Kill a live query. |

---

## Session-specific methods

### `.begin_transaction()` {#begin-transaction}

Begins a new transaction scoped to this session. Returns a transaction object that provides query and CRUD methods within the transaction boundary.

```python title="Method Syntax"
txn = session.begin_transaction()
```

**Returns (sync):** `BlockingSurrealTransaction`
**Returns (async):** `AsyncSurrealTransaction`

#### Examples

```python title="Synchronous"
session = db.new_session()
session.use("my_namespace", "my_database")

txn = session.begin_transaction()
txn.create("users", {"name": "Alice", "email": "alice@example.com"})
txn.create("users", {"name": "Bob", "email": "bob@example.com"})
txn.commit()
```

```python title="Asynchronous"
session = await db.new_session()
await session.use("my_namespace", "my_database")

txn = await session.begin_transaction()
await txn.create("users", {"name": "Alice", "email": "alice@example.com"})
await txn.create("users", {"name": "Bob", "email": "bob@example.com"})
await txn.commit()
```

### `.close_session()` {#close-session}

Closes this session on the server, releasing its session ID and any associated state. After calling this method, the session object should not be used.

```python title="Method Syntax"
session.close_session()
```

**Returns:** `None`

#### Examples

```python title="Synchronous"
session = db.new_session()
session.use("my_namespace", "my_database")
result = session.select("users")

session.close_session()
```

```python title="Asynchronous"
session = await db.new_session()
await session.use("my_namespace", "my_database")
result = await session.select("users")

await session.close_session()
```

---

## Complete example

```python title="Isolated sessions (sync)"
from surrealdb import Surreal, RecordID

with Surreal("ws://localhost:8000") as db:
    db.use("shop", "inventory")
    db.signin({"username": "root", "password": "root"})

    # Session A works with the "shop" namespace
    session_a = db.new_session()
    session_a.use("shop", "inventory")
    session_a.create("products", {"name": "Laptop", "price": 999.99})

    # Session B works with a different namespace independently
    session_b = db.new_session()
    session_b.use("analytics", "events")
    session_b.create("page_views", {"page": "/products", "count": 1})

    # Each session has its own authentication state
    session_a.signin({"username": "root", "password": "root"})
    products = session_a.select("products")
    print("Products:", products)

    # Transactions within a session
    txn = session_a.begin_transaction()
    txn.create("products", {"name": "Mouse", "price": 29.99})
    txn.create("products", {"name": "Keyboard", "price": 59.99})
    txn.commit()

    session_a.close_session()
    session_b.close_session()
```

```python title="Isolated sessions (async)"
from surrealdb import AsyncSurreal, RecordID

async def main():
    async with AsyncSurreal("ws://localhost:8000") as db:
        await db.use("shop", "inventory")
        await db.signin({"username": "root", "password": "root"})

        session = await db.new_session()
        await session.use("shop", "inventory")
        await session.signin({"username": "root", "password": "root"})

        await session.create("products", {"name": "Laptop", "price": 999.99})

        txn = await session.begin_transaction()
        await txn.create("products", {"name": "Mouse", "price": 29.99})
        await txn.create("products", {"name": "Keyboard", "price": 59.99})
        await txn.commit()

        products = await session.select("products")
        print("Products:", products)

        await session.close_session()

asyncio.run(main())
```

---

## See also

- [Surreal](surreal.md) — Connection reference with full method documentation
- [SurrealTransaction](surreal-transaction.md) — Transaction reference
- [Data Types](../types/index.md) — Type aliases and value types
- [Errors](../errors/index.md) — Error classes reference
