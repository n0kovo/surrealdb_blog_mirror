---
position: 8
title: Python
description: Connect to SurrealDB and run your first queries with the Python SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python.mdx"
---

# Getting started

The Python SDK for SurrealDB lets you connect to a database and query it from your application. This guide covers connecting, authenticating, and running your first queries.

## 1. Install the SDK

Follow the [installation guide](../reference/python/installation.md) to install the SDK as a dependency in your project. Once installed, import the SDK to start using it.

	
**Synchronous**

```python
		from surrealdb import Surreal

		db = Surreal("ws://localhost:8000")
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		db = AsyncSurreal("ws://localhost:8000")
		```

The `Surreal` and `AsyncSurreal` factory functions accept a connection URL and return the appropriate connection class based on the protocol.

## 2. Connect to SurrealDB

You can use the `.connect()` method to open the connection, then `.use()` to select a namespace and database, and `.signin()` to authenticate.

Supported connection protocols include:
- **WebSocket** (`ws://`, `wss://`) for long-lived stateful connections
- **HTTP** (`http://`, `https://`) for short-lived stateless connections
- **Embedded** (`mem://`, `file://`, `surrealkv://`) for in-process databases

	
**Synchronous**

```python
		from surrealdb import Surreal

		db = Surreal("ws://localhost:8000")
		db.connect()
		db.use("company_name", "project_name")
		db.signin({"username": "root", "password": "root"})
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		db = AsyncSurreal("ws://localhost:8000")
		await db.connect()
		await db.use("company_name", "project_name")
		await db.signin({"username": "root", "password": "root"})
		```

You can also use a context manager to automatically close the connection when you are done.

	
**Synchronous**

```python
		with Surreal("ws://localhost:8000") as db:
		    db.use("company_name", "project_name")
		    db.signin({"username": "root", "password": "root"})
		```

	
**Asynchronous**

```python
		async with AsyncSurreal("ws://localhost:8000") as db:
		    await db.use("company_name", "project_name")
		    await db.signin({"username": "root", "password": "root"})
		```

## 3. Inserting data into SurrealDB

Once connected, you can use the `.create()` method to create records. Pass a table name or a `RecordID` as the first argument and the record data as the second.

	
**Synchronous**

```python
		from surrealdb import RecordID

		user = db.create("users", {
		    "name": "John",
		    "email": "john@example.com",
		    "age": 32,
		})

		product = db.create(RecordID("products", "apple"), {
		    "name": "Apple",
		    "price": 1.50,
		    "category": "fruit",
		})
		```

	
**Asynchronous**

```python
		from surrealdb import RecordID

		user = await db.create("users", {
		    "name": "John",
		    "email": "john@example.com",
		    "age": 32,
		})

		product = await db.create(RecordID("products", "apple"), {
		    "name": "Apple",
		    "price": 1.50,
		    "category": "fruit",
		})
		```

## 4. Retrieving data from SurrealDB

### Selecting records

The `.select()` method retrieves all records from a table, or a single record by its `RecordID`.

	
**Synchronous**

```python
		users = db.select("users")

		apple = db.select(RecordID("products", "apple"))
		```

	
**Asynchronous**

```python
		users = await db.select("users")

		apple = await db.select(RecordID("products", "apple"))
		```

### Running SurrealQL queries

For more advanced use cases, you can use the `.query()` method to run [SurrealQL](../reference/query-language/index.md) statements directly. Use the `vars` parameter to safely pass dynamic values.

	
**Synchronous**

```python
		result = db.query(
		    "SELECT name, price FROM products WHERE price < $max_price ORDER BY price",
		    {"max_price": 5.00},
		)
		```

	
**Asynchronous**

```python
		result = await db.query(
		    "SELECT name, price FROM products WHERE price < $max_price ORDER BY price",
		    {"max_price": 5.00},
		)
		```

## 5. Closing the connection

Always close the connection when you are done to release resources. If you use a context manager, this happens automatically.

	
**Synchronous**

```python
		db.close()
		```

	
**Asynchronous**

```python
		await db.close()
		```

## Next steps

You have learned how to install the SDK, connect to SurrealDB, create records, and retrieve data. There is a lot more you can do with the SDK, including updating and deleting records, authentication, live queries, and transactions.

- **[Connection management](../reference/python/concepts/connecting-to-surrealdb.md)** — Learn how to manage your database connections, including protocols and context managers.
- **[Authentication](../reference/python/concepts/authentication.md)** — Read more about authentication and how to integrate it into your application.
- **[Data manipulation](../reference/python/concepts/data-manipulation.md)** — Learn how to create, read, update, and delete records using the SDK.
- **[API Reference](../reference/python/api/core/surreal.md)** — Complete reference for all classes, methods, types, and errors.

> [!NOTE]
> This getting-started guide covers the essentials. For the complete methods, API, and concept reference, see the [Python SDK reference](../reference/python/index.md).
