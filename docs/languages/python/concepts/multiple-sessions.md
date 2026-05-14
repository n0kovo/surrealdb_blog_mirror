---
position: 9
title: Multiple sessions
description: The Python SDK supports creating multiple isolated sessions within a single WebSocket connection.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/concepts/multiple-sessions.mdx"
---

# Multiple sessions

The Python SDK supports creating multiple isolated sessions within a single WebSocket connection. Each session maintains its own namespace, database, and authentication state, allowing you to perform independent operations without opening additional connections.

This page covers how to create sessions, isolate their scope, authenticate independently, and close them when no longer needed.

> [!NOTE]
> Multiple sessions require a WebSocket connection (`ws://` or `wss://`). HTTP and embedded connections do not support sessions.

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
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#new-session">`db.new_session()`</a></td>
			<td scope="row" data-label="Description">Creates a new isolated session on the current connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal-session#close-session">`session.close_session()`</a></td>
			<td scope="row" data-label="Description">Closes the session and detaches it from the connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal-session#use">`session.use(namespace, database)`</a></td>
			<td scope="row" data-label="Description">Switches the session to a specific namespace and database</td>
		</tr>
	</tbody>
</table>

## Creating a session

Call `.new_session()` on an existing connection to create a new session. The async variant returns an `AsyncSurrealSession` and the sync variant returns a `BlockingSurrealSession`. Each session operates independently from the parent connection and other sessions.

	
**Synchronous**

```python
		from surrealdb import Surreal

		with Surreal("ws://localhost:8000") as db:
		    db.use("surrealdb", "docs")
		    db.signin({"username": "root", "password": "root"})

		    session = db.new_session()
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		async with AsyncSurreal("ws://localhost:8000") as db:
		    await db.use("surrealdb", "docs")
		    await db.signin({"username": "root", "password": "root"})

		    session = await db.new_session()
		```

A newly created session does not inherit the namespace, database, or authentication state of the parent connection. You must configure these explicitly on the session.

## Isolating namespace and database

Each session can target a different namespace and database by calling `.use()`. Changes to one session's scope do not affect the parent connection or any other session.

	
**Synchronous**

```python
		session_a = db.new_session()
		session_a.use("surrealdb", "docs")

		session_b = db.new_session()
		session_b.use("surrealdb", "staging")

		docs_users = session_a.select("users")
		staging_users = session_b.select("users")
		```

	
**Asynchronous**

```python
		session_a = await db.new_session()
		await session_a.use("surrealdb", "docs")

		session_b = await db.new_session()
		await session_b.use("surrealdb", "staging")

		docs_users = await session_a.select("users")
		staging_users = await session_b.select("users")
		```

In the example above, `session_a` reads from the `docs` database while `session_b` reads from `staging`, both over the same underlying WebSocket connection.

## Independent authentication

Each session can authenticate as a different user. This is useful when you need to perform operations on behalf of multiple users without managing separate connections.

	
**Synchronous**

```python
		session_admin = db.new_session()
		session_admin.use("surrealdb", "docs")
		session_admin.signin({"username": "root", "password": "root"})

		session_user = db.new_session()
		session_user.use("surrealdb", "docs")
		session_user.signin({
		    "namespace": "surrealdb",
		    "database": "docs",
		    "access": "account",
		    "variables": {
		        "email": "info@surrealdb.com",
		        "password": "123456",
		    },
		})

		all_records = session_admin.select("users")

		own_record = session_user.info()
		```

	
**Asynchronous**

```python
		session_admin = await db.new_session()
		await session_admin.use("surrealdb", "docs")
		await session_admin.signin({"username": "root", "password": "root"})

		session_user = await db.new_session()
		await session_user.use("surrealdb", "docs")
		await session_user.signin({
		    "namespace": "surrealdb",
		    "database": "docs",
		    "access": "account",
		    "variables": {
		        "email": "info@surrealdb.com",
		        "password": "123456",
		    },
		})

		all_records = await session_admin.select("users")

		own_record = await session_user.info()
		```

In the example above, `session_admin` has root-level access while `session_user` is authenticated as a record user. Each session's permissions are enforced independently.

## Closing a session

When a session is no longer needed, call `.close_session()` to detach it from the connection and release its resources. The parent connection and other sessions remain active.

	
**Synchronous**

```python
		session.close_session()
		```

	
**Asynchronous**

```python
		await session.close_session()
		```

Closing the parent connection automatically closes all sessions associated with it.

## Learn more

- [SurrealSession API reference](../api/core/surreal-session.md) for session method signatures
- [Transactions](transactions.md) for transaction support within sessions
- [Authentication](authentication.md) for signing in within sessions
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for WebSocket connection setup
