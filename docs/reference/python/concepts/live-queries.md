---
position: 6
title: Live queries
description: The Python SDK supports real-time live queries that stream changes from the database to your application.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/python/concepts/live-queries.mdx"
---

# Live queries

The Python SDK supports real-time live queries that stream changes from the database directly to your application. When records matching a live query are created, updated, or deleted, the SDK delivers notifications through a generator that you can iterate over.

This page covers how to start live queries, subscribe to change notifications, and stop queries when they are no longer needed.

> [!NOTE]
> Live queries require a WebSocket connection (`ws://` or `wss://`). HTTP and embedded connections do not support live queries.

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
			<td scope="row" data-label="Method"><a href="/docs/reference/python/api/core/surreal#live">`db.live(table, diff?)`</a></td>
			<td scope="row" data-label="Description">Starts a live query on a table and returns a query UUID</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/python/api/core/surreal#subscribe-live">`db.subscribe_live(query_uuid)`</a></td>
			<td scope="row" data-label="Description">Subscribes to notifications from a live query</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/python/api/core/surreal#kill">`db.kill(query_uuid)`</a></td>
			<td scope="row" data-label="Description">Stops a running live query</td>
		</tr>
	</tbody>
</table>

## Starting a live query

The `.live()` method registers a live query on a table and returns a UUID that identifies the query. You can optionally pass `diff=True` to receive changes in [JSON Patch (RFC 6902)](https://jsonpatch.com/) format instead of full record snapshots.

	
**Synchronous**

```python
		from surrealdb import Surreal

		with Surreal("ws://localhost:8000") as db:
		    db.use("surrealdb", "docs")
		    db.signin({"username": "root", "password": "root"})

		    query_uuid = db.live("users")
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		async with AsyncSurreal("ws://localhost:8000") as db:
		    await db.use("surrealdb", "docs")
		    await db.signin({"username": "root", "password": "root"})

		    query_uuid = await db.live("users")
		```

To receive JSON Patch diffs instead of full records, pass `diff=True`.

```python
query_uuid = db.live("users", diff=True)
```

## Subscribing to changes

After starting a live query, call `.subscribe_live()` with the returned UUID to obtain a stream of notifications. The async variant returns an `AsyncGenerator` and the sync variant returns a `Generator`. Each notification is a dictionary containing `action` and `result` keys.

The `action` field is one of `"CREATE"`, `"UPDATE"`, or `"DELETE"`, and the `result` field contains the affected record (or the JSON Patch operations when `diff=True` was used).

	
**Synchronous**

```python
		from surrealdb import Surreal

		with Surreal("ws://localhost:8000") as db:
		    db.use("surrealdb", "docs")
		    db.signin({"username": "root", "password": "root"})

		    query_uuid = db.live("users")

		    for notification in db.subscribe_live(query_uuid):
		        print(notification["action"])
		        print(notification["result"])
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		async with AsyncSurreal("ws://localhost:8000") as db:
		    await db.use("surrealdb", "docs")
		    await db.signin({"username": "root", "password": "root"})

		    query_uuid = await db.live("users")

		    async for notification in db.subscribe_live(query_uuid):
		        print(notification["action"])
		        print(notification["result"])
		```

## Stopping a live query

When you no longer need to receive notifications, call `.kill()` with the query UUID to stop the live query on the server. This also ends the generator returned by `.subscribe_live()`.

	
**Synchronous**

```python
		db.kill(query_uuid)
		```

	
**Asynchronous**

```python
		await db.kill(query_uuid)
		```

## Subscribing to live queries from SurrealQL

You can also initiate a live query using a [`LIVE SELECT`](../../query-language/statements/live-select.md) statement through the `.query()` method. The query returns a UUID that can be passed to `.subscribe_live()` in the same way as a UUID returned by `.live()`.

This approach is useful when you need the filtering capabilities of SurrealQL, such as selecting specific fields or applying `WHERE` clauses.

	
**Synchronous**

```python
		from surrealdb import Surreal

		with Surreal("ws://localhost:8000") as db:
		    db.use("surrealdb", "docs")
		    db.signin({"username": "root", "password": "root"})

		    query_uuid = db.query("LIVE SELECT * FROM users WHERE age > 18")

		    for notification in db.subscribe_live(query_uuid):
		        print(notification["action"])
		        print(notification["result"])
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		async with AsyncSurreal("ws://localhost:8000") as db:
		    await db.use("surrealdb", "docs")
		    await db.signin({"username": "root", "password": "root"})

		    query_uuid = await db.query("LIVE SELECT * FROM users WHERE age > 18")

		    async for notification in db.subscribe_live(query_uuid):
		        print(notification["action"])
		        print(notification["result"])
		```

## Learn more

- [Surreal API reference](../api/core/surreal.md) for method signatures and parameters
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for WebSocket connection setup
- [SurrealQL LIVE SELECT](../../query-language/statements/live-select.md) for the query language syntax
