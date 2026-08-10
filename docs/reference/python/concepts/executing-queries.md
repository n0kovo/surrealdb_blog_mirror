---
position: 3
title: Executing queries
description: The Python SDK provides methods for executing SurrealQL queries with parameter binding support.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/python/concepts/executing-queries.mdx"
---

# Executing queries

The Python SDK lets you execute [SurrealQL](../../query-language/index.md) statements directly against the database. You can run ad-hoc queries with parameter binding, retrieve processed results, or access the full raw response for advanced use cases.

This page covers how to run queries, bind variables, and work with raw results.

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
			<td scope="row" data-label="Method"><a href="/docs/reference/python/api/core/surreal#query">`db.query(query, vars?)`</a></td>
			<td scope="row" data-label="Description">Builds a SurrealQL query; trigger it with `.execute()`, `.first()` or `.into(cls)`</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/python/api/core/surreal#query-raw">`db.query_raw(query, vars?)`</a></td>
			<td scope="row" data-label="Description">Executes a SurrealQL query and returns the full raw response</td>
		</tr>
	</tbody>
</table>

## Running a query

The `.query()` method builds a SurrealQL query. It does not talk to the database on its own — you trigger it explicitly:

- `.execute()` returns a `list` of [Value](../api/types/index.md#value) with **one entry per statement**, always a list, even when the query contains a single statement.
- `.first()` returns just the first statement's result, which is what you usually want for a one-statement query.

On an async connection you can also `await` the builder directly, which is the same as awaiting `.execute()`.

	
**Synchronous**

```python
		from surrealdb import Surreal

		with Surreal("ws://localhost:8000") as db:
		    db.use("surrealdb", "docs")
		    db.signin({"username": "root", "password": "root"})

		    statements = db.query("SELECT * FROM users").execute()
		    print(statements)  # [[{...}, {...}]] - one entry, one statement

		    users = db.query("SELECT * FROM users").first()
		    print(users)       # [{...}, {...}]
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		async with AsyncSurreal("ws://localhost:8000") as db:
		    await db.use("surrealdb", "docs")
		    await db.signin({"username": "root", "password": "root"})

		    statements = await db.query("SELECT * FROM users").execute()
		    print(statements)  # [[{...}, {...}]] - one entry, one statement

		    users = await db.query("SELECT * FROM users").first()
		    print(users)       # [{...}, {...}]
		```

## Passing variables

You can pass a dictionary of variables as the second argument to `.query()`. Variables are referenced in SurrealQL using the `$` prefix and are safely bound, preventing injection attacks.

	
**Synchronous**

```python
		users = db.query(
		    "SELECT * FROM users WHERE age > $min_age AND active = $active",
		    {"min_age": 18, "active": True},
		).first()
		```

	
**Asynchronous**

```python
		users = await db.query(
		    "SELECT * FROM users WHERE age > $min_age AND active = $active",
		    {"min_age": 18, "active": True},
		).first()
		```

You can bind any Python value supported by the SDK, including strings, numbers, booleans, lists, dictionaries, and SurrealDB-specific types such as [RecordID](../api/values/record-id.md).

```python
from surrealdb import RecordID

users = db.query(
    "SELECT * FROM users WHERE id = $user_id",
    {"user_id": RecordID("users", "tobie")},
).first()
```

## Getting raw query results

The `.query_raw()` method returns the full response from the server, including metadata such as execution time and status for each statement. This is useful for debugging or when you need to inspect how the server processed the query.

	
**Synchronous**

```python
		response = db.query_raw("SELECT * FROM users; SELECT * FROM products")

		for statement in response["result"]:
		    print(statement["status"])
		    print(statement["time"])
		    print(statement["result"])
		```

	
**Asynchronous**

```python
		response = await db.query_raw("SELECT * FROM users; SELECT * FROM products")

		for statement in response["result"]:
		    print(statement["status"])
		    print(statement["time"])
		    print(statement["result"])
		```

The response is a `dict` containing the RPC envelope. Its `result` key holds one entry per statement in the query, each with `status`, `time`, and `result` fields. Unlike `.query()`, a failed statement is reported as `"status": "ERR"` rather than raised.

## Handling multiple statements

When a query string contains multiple semicolon-separated statements, `.execute()` returns one entry per statement, in order. Nothing is discarded, so you can unpack the results directly.

	
**Synchronous**

```python
		created, users = db.query("""
		    CREATE users CONTENT {"name": "Alice", "age": 30};
		    SELECT * FROM users;
		""").execute()

		# .first() would return only the CREATE result
		```

	
**Asynchronous**

```python
		created, users = await db.query("""
		    CREATE users CONTENT {"name": "Alice", "age": 30};
		    SELECT * FROM users;
		""").execute()

		# .first() would return only the CREATE result
		```

`.query_raw()` returns those same per-statement results wrapped in the raw RPC envelope, with each statement's `status` and `time` alongside its `result`. Reach for it when you need that metadata, or when you want failed statements reported rather than raised.

## Learn more

- [Surreal API reference](../api/core/surreal.md) for complete method signatures and parameters
- [Data manipulation](data-manipulation.md) for CRUD operations using dedicated methods
- [SurrealQL reference](../../query-language/index.md) for the full query language documentation
- [Value types](../api/types/index.md) for the types returned by query methods
