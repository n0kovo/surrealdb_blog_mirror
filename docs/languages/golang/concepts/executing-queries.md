---
position: 3
title: Executing queries
description: The Go SDK provides generic functions for executing SurrealQL queries with typed results and parameterised variables.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/concepts/executing-queries.mdx"
---

# Executing queries

The Go SDK provides two ways to execute SurrealQL queries: [`Query`](../api/core/db.md#query) for typed, parameterised queries and [`QueryRaw`](../api/core/db.md#queryraw) for composing multiple statements with per-statement results. Both are generic functions that work with [`*DB`](../api/core/db.md), [`*Session`](../api/core/session.md), and [`*Transaction`](../api/core/transaction.md).

This page covers running queries, parameterising them, handling multi-statement results, and managing connection-scoped variables.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Function</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#query">`surrealdb.Query[T](ctx, s, sql, vars)`</a></td>
			<td scope="row" data-label="Description">Executes a SurrealQL query with typed results</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#queryraw">`surrealdb.QueryRaw(ctx, s, queries)`</a></td>
			<td scope="row" data-label="Description">Executes a batch of query statements with per-statement results</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#let">`db.Let(ctx, key, val)`</a></td>
			<td scope="row" data-label="Description">Defines a variable on the connection for use in queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#unset">`db.Unset(ctx, key)`</a></td>
			<td scope="row" data-label="Description">Removes a previously defined connection variable</td>
		</tr>
	</tbody>
</table>

## Running a query

The [`Query`](../api/core/db.md#query) function executes a SurrealQL string and returns typed results. The first type parameter specifies the expected result type. The second parameter `s` can be a [`*DB`](../api/core/db.md), [`*Session`](../api/core/session.md), or [`*Transaction`](../api/core/transaction.md).

```go
results, err := surrealdb.Query[[]Person](ctx, db,
	"SELECT * FROM persons WHERE age > $min_age",
	map[string]any{"min_age": 18},
)
if err != nil {
	log.Fatal(err)
}

for _, qr := range *results {
	fmt.Println(qr.Status, qr.Result)
}
```

The function returns `*[]QueryResult[T]`, where each [`QueryResult`](../api/types/index.md#queryresult) contains the `Status`, execution `Time`, `Result`, and an optional `Error` for that statement.

## Parameterising queries

Always use parameters (`$name`) instead of string interpolation to prevent injection attacks and ensure correct CBOR encoding of [value types](value-types.md).

```go
results, err := surrealdb.Query[[]Person](ctx, db,
	"SELECT * FROM persons WHERE name = $name AND age > $age",
	map[string]any{
		"name": "Tobie",
		"age":  25,
	},
)
```

Pass `nil` for the variables map when no parameters are needed:

```go
results, err := surrealdb.Query[[]Person](ctx, db,
	"SELECT * FROM persons",
	nil,
)
```

## Handling multi-statement queries

When a query string contains multiple statements, `Query` returns a `QueryResult` for each statement. Check the `Error` field on each result to detect per-statement failures.

```go
results, err := surrealdb.Query[[]any](ctx, db,
	"CREATE person:tobie SET name = 'Tobie'; SELECT * FROM person;",
	nil,
)

for i, qr := range *results {
	if qr.Error != nil {
		fmt.Printf("Statement %d failed: %s\n", i, qr.Error.Message)
		continue
	}
	fmt.Printf("Statement %d: %v\n", i, qr.Result)
}
```

> [!NOTE]
> The `err` returned by `Query` is a joined error containing all per-statement [`QueryError`](../api/errors/index.md#queryerror) values. You can check individual statements via the `Error` field, or use `errors.Is(err, &surrealdb.QueryError{})` on the returned error.

## Composing queries with QueryRaw

`QueryRaw` lets you compose a batch of [`QueryStmt`](../api/types/index.md#querystmt) objects, each with its own SQL and variables. After execution, each statement's result is available via `.GetResult()`.

```go
stmts := []surrealdb.QueryStmt{
	{SQL: "CREATE person:alice SET name = $name", Vars: map[string]any{"name": "Alice"}},
	{SQL: "SELECT * FROM person", Vars: nil},
}

if err := surrealdb.QueryRaw(ctx, db, &stmts); err != nil {
	log.Fatal(err)
}

var persons []Person
if err := stmts[1].GetResult(&persons); err != nil {
	log.Fatal(err)
}
```

## Defining connection variables

Use `.Let()` to define a variable that persists on the connection and is available in all subsequent queries. Use `.Unset()` to remove it.

```go
if err := db.Let(ctx, "app_version", "1.0.0"); err != nil {
	log.Fatal(err)
}

results, err := surrealdb.Query[[]any](ctx, db,
	"RETURN $app_version",
	nil,
)

db.Unset(ctx, "app_version")
```

Connection variables are scoped to the connection (or [session](multiple-sessions.md) if using sessions). They do not affect other connections. You can also build queries programmatically using the [query builder](query-builder.md).

## Learn more

- [DB API reference](../api/core/db.md) for complete method signatures and parameters
- [Data manipulation](data-manipulation.md) for typed CRUD operations
- [Error handling](error-handling.md) for distinguishing between query errors and transport errors
- [Types reference](../api/types/index.md) for `QueryResult` and `QueryStmt` definitions
- [SurrealQL statements](../../../reference/query-language/statements/overview.md) for the query language syntax
