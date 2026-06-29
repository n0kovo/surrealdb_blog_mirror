---
position: 3
title: Executing queries
description: The Java SDK provides methods for executing SurrealQL queries with optional parameter binding.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/concepts/executing-queries.mdx"
---

# Executing queries

The Java SDK provides methods for executing raw [SurrealQL](../../../reference/query-language/index.md) queries against SurrealDB. You can run single or multi-statement queries, bind [parameters](../../../reference/query-language/language-primitives/parameters.md) for safe variable injection, and call server-side [functions](../../../reference/query-language/statements/define/function.md).

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
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#query">`db.query(sql)`</a></td>
			<td scope="row" data-label="Description">Executes a SurrealQL query</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#query-bind">`db.queryBind(sql, params)`</a></td>
			<td scope="row" data-label="Description">Executes a parameterised query</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#run">`db.run(name, args)`</a></td>
			<td scope="row" data-label="Description">Runs a SurrealDB function</td>
		</tr>
	</tbody>
</table>

## Running a query

The [`.query()`](../api/core/surreal.md#query) method executes one or more SurrealQL statements and returns a [`Response`](../api/core/response.md). Use [`.take(int)`](../api/core/response.md#take) to extract the result of a specific statement by its zero-based index, or `.take(Class, int)` to deserialize the result into a typed Java object.

```java
Response response = db.query("SELECT * FROM users; SELECT * FROM posts;");

Value users = response.take(0);
List<Post> posts = response.take(Post.class, 1);
```

## Using query parameters

The [`.queryBind()`](../api/core/surreal.md#query-bind) method accepts a `Map<String, ?>` of parameters that are safely injected into the query. Parameterised queries prevent SurrealQL injection and ensure values are properly escaped.

```java
Map<String, Object> params = Map.of("min_age", 18);

Response response = db.queryBind(
    "SELECT * FROM users WHERE age > $min_age",
    params
);

List<User> users = response.take(User.class, 0);
```

Always prefer [`.queryBind()`](../api/core/surreal.md#query-bind) over string concatenation when incorporating user-provided values into queries.

## Working with query responses

The [`Response`](../api/core/response.md) object contains the results of all statements in the query. Use [`.take(int)`](../api/core/response.md#take) to get a raw [`Value`](../api/values/value.md), or `.take(Class, int)` to deserialize into a POJO. The `.size()` method returns the number of statement results.

```java
Response response = db.query(
    "CREATE users SET name = 'Alice'; SELECT * FROM users;"
);

int statementCount = response.size();

Value created = response.take(0);
List<User> users = response.take(User.class, 1);
```

See [Value types](value-types.md) for details on working with the [`Value`](../api/values/value.md) class and type conversions.

## Running SurrealDB functions

The [`.run()`](../api/core/surreal.md#run) method calls a server-side function defined with [`DEFINE FUNCTION`](../../../reference/query-language/statements/define/function.md). Pass the function name and any arguments.

```java
Value result = db.run("fn::calculate_total", 100, 0.2);
```

## Learn more

- [Surreal API reference](../api/core/surreal.md) for method signatures
- [Response API reference](../api/core/response.md) for response handling
- [Value types](value-types.md) for working with query results
- [SurrealQL](../../../reference/query-language/index.md) for query language reference
- [SurrealQL parameters](../../../reference/query-language/language-primitives/parameters.md) for parameter syntax in queries
- [DEFINE FUNCTION](../../../reference/query-language/statements/define/function.md) for defining server-side functions
