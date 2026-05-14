---
position: 3
title: Executing queries
description: The Python SDK provides methods for executing SurrealQL queries with parameter binding support.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/concepts/executing-queries.mdx"
---

# Executing queries

The Python SDK lets you execute [SurrealQL](../../../reference/query-language/index.md) statements directly against the database. You can run ad-hoc queries with parameter binding, retrieve processed results, or access the full raw response for advanced use cases.

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
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#query">`db.query(query, vars?)`</a></td>
			<td scope="row" data-label="Description">Executes a SurrealQL query and returns the processed result</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#query-raw">`db.query_raw(query, params?)`</a></td>
			<td scope="row" data-label="Description">Executes a SurrealQL query and returns the full raw response</td>
		</tr>
	</tbody>
</table>

## Running a query

The `.query()` method executes a SurrealQL statement and returns the result directly as a [Value](../api/types/index.md#value). This is the simplest way to run queries when you need only the result data.

	
**Synchronous**

```python
		from surrealdb import Surreal

		with Surreal("ws://localhost:8000") as db:
		    db.use("surrealdb", "docs")
		    db.signin({"username": "root", "password": "root"})

		    result = db.query("SELECT * FROM users")
		    print(result)
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		async with AsyncSurreal("ws://localhost:8000") as db:
		    await db.use("surrealdb", "docs")
		    await db.signin({"username": "root", "password": "root"})

		    result = await db.query("SELECT * FROM users")
		    print(result)
		```

## Passing variables

You can pass a dictionary of variables as the second argument to `.query()`. Variables are referenced in SurrealQL using the `$` prefix and are safely bound, preventing injection attacks.

	
**Synchronous**

```python
		result = db.query(
		    "SELECT * FROM users WHERE age > $min_age AND active = $active",
		    {"min_age": 18, "active": True},
		)
		```

	
**Asynchronous**

```python
		result = await db.query(
		    "SELECT * FROM users WHERE age > $min_age AND active = $active",
		    {"min_age": 18, "active": True},
		)
		```

You can bind any Python value supported by the SDK, including strings, numbers, booleans, lists, dictionaries, and SurrealDB-specific types such as [RecordID](../api/values/record-id.md).

```python
from surrealdb import RecordID

result = db.query(
    "SELECT * FROM users WHERE id = $user_id",
    {"user_id": RecordID("users", "tobie")},
)
```

## Getting raw query results

The `.query_raw()` method returns the full response from the server, including metadata such as execution time and status for each statement. This is useful for debugging or when you need to inspect how the server processed the query.

	
**Synchronous**

```python
		response = db.query_raw("SELECT * FROM users; SELECT * FROM products")

		for statement in response:
		    print(statement["status"])
		    print(statement["time"])
		    print(statement["result"])
		```

	
**Asynchronous**

```python
		response = await db.query_raw("SELECT * FROM users; SELECT * FROM products")

		for statement in response:
		    print(statement["status"])
		    print(statement["time"])
		    print(statement["result"])
		```

Each element in the response corresponds to one statement in the query and contains the `status`, `time`, and `result` fields.

## Handling multiple statements

When a query string contains multiple semicolon-separated statements, `.query()` returns only the result of the **last** statement. If you need the results from every statement, use `.query_raw()` instead.

The following example demonstrates the difference between the two methods for multi-statement queries.

	
**Synchronous**

```python
		last_result = db.query("""
		    CREATE users CONTENT {"name": "Alice", "age": 30};
		    SELECT * FROM users;
		""")

		all_results = db.query_raw("""
		    CREATE users CONTENT {"name": "Alice", "age": 30};
		    SELECT * FROM users;
		""")
		```

	
**Asynchronous**

```python
		last_result = await db.query("""
		    CREATE users CONTENT {"name": "Alice", "age": 30};
		    SELECT * FROM users;
		""")

		all_results = await db.query_raw("""
		    CREATE users CONTENT {"name": "Alice", "age": 30};
		    SELECT * FROM users;
		""")
		```

In the example above, `last_result` contains only the `SELECT` output, while `all_results` contains the full response for both the `CREATE` and `SELECT` statements.

## Learn more

- [Surreal API reference](../api/core/surreal.md) for complete method signatures and parameters
- [Data manipulation](data-manipulation.md) for CRUD operations using dedicated methods
- [SurrealQL reference](../../../reference/query-language/index.md) for the full query language documentation
- [Value types](../api/types/index.md) for the types returned by query methods
