---
position: 3
title: Quickstart
description: Get started with the SurrealDB SDK for Python in minutes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/start.mdx"
---

# Quickstart

The Python SDK for SurrealDB makes it straightforward to connect to your instance and start querying data. This guide walks you through connecting, authenticating, and performing basic operations.

## 1. Install the SDK

Follow the [installation guide](installation.md) to install the SDK as a dependency in your project. Once installed, import the SDK to start using it.

	
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

For more advanced use cases, you can use the `.query()` method to run [SurrealQL](../../reference/query-language/index.md) statements directly. Use the `vars` parameter to safely pass dynamic values.

	
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

## What's next?

You have learned how to install the SDK, connect to SurrealDB, create records, and retrieve data. There is a lot more you can do with the SDK, including updating and deleting records, handling authentication, live queries, sessions, and transactions.

- **[Connection management](concepts/connecting-to-surrealdb.md)** — Learn how to manage your database connections, including protocols and context managers.
- **[Authentication](concepts/authentication.md)** — Read more about authentication and how to integrate it into your application.
- **[Data manipulation](concepts/data-manipulation.md)** — Learn how to create, read, update, and delete records using the SDK.
- **[API Reference](api/core/surreal.md)** — Complete reference for all classes, methods, types, and errors.
