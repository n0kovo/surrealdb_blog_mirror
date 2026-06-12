---
position: 3
title: Executing queries
description: Run raw SurrealQL with bound parameters and decode results with the Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/concepts/executing-queries.mdx"
---

# Executing queries

The [`.query()`](../api/core/surreal-client.md#query) family runs raw [SurrealQL](../../../reference/query-language/index.md) and is the foundation of the SDK — the [CRUD builders](data-manipulation.md) compile to SurrealQL and dispatch through it. Queries can be supplied as a string with a [`JsonObject`](value-types.md) of bound parameters, or built with the [`surql`](#building-queries) DSL.

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
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#query">`client.query(sql, vars)`</a></td>
			<td scope="row" data-label="Description">Runs SurrealQL and returns the raw result</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#query-as">`client.queryAs&lt;T&gt;(sql, vars)`</a></td>
			<td scope="row" data-label="Description">Runs SurrealQL and decodes the result to `T`</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#query-result">`client.queryResult(sql, vars)`</a></td>
			<td scope="row" data-label="Description">Runs SurrealQL and returns a `Result`</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#let">`client.let(key, value)`</a></td>
			<td scope="row" data-label="Description">Defines a session parameter</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#unset">`client.unset(key)`</a></td>
			<td scope="row" data-label="Description">Removes a session parameter</td>
		</tr>
	</tbody>
</table>

## Running a query

Pass SurrealQL and, optionally, a [`JsonObject`](value-types.md) of bound parameters. The result is returned as a [`JsonElement`](value-types.md).

```kotlin

val result = client.query(
    "SELECT * FROM person WHERE age > \$min_age",
    buildJsonObject { put("min_age", 25) },
)
```

> [!NOTE]
> Always bind variables with the `vars` argument rather than interpolating values into the query string. This avoids SurrealQL injection and lets the server cache query plans.

## Decoding results

To decode a query result straight into your own types, use the inline [`.queryAs<T>()`](../api/core/surreal-client.md#query-as) helper with a [`@Serializable`](serialization.md) type.

```kotlin

@Serializable
data class Person(val name: String, val age: Int)

val people: List<Person> = client.queryAs(
    "SELECT * FROM person WHERE age > \$min_age",
    buildJsonObject { put("min_age", 25) },
)
```

You can also decode an arbitrary [`JsonElement`](value-types.md) yourself with [`.decode<T>()`](../api/core/surreal-client.md#decode).

## Result variants

Every networked call has a `...Result` companion that returns a [`Result`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-result/) instead of throwing, which is useful when you prefer to handle failures functionally.

```kotlin
val outcome = client.queryResult("SELECT * FROM person")
outcome
    .onSuccess { println("got $it") }
    .onFailure { println("query failed: ${it.message}") }
```

See [Error handling](error-handling.md) for the exception hierarchy thrown by the non-`Result` variants.

## Session parameters

Define parameters that persist for the session with [`.let()`](../api/core/surreal-client.md#let), and remove them with [`.unset()`](../api/core/surreal-client.md#unset). These are referenced as `$name` in subsequent queries.

```kotlin

client.let("min_age", JsonPrimitive(18))
client.query("SELECT * FROM person WHERE age > \$min_age")
client.unset("min_age")
```

## Building queries

The [`surql`](../api/core/query-builder.md#surql) DSL builds a parameterised `BoundQuery` with automatic binding of values and record identifiers.

```kotlin

val bound = surql("SELECT * FROM person WHERE age > \$min", "min" to 25)
val result = client.query(bound)
```

## Learn more

- [SurrealClient API reference](../api/core/surreal-client.md) for complete method signatures
- [Query builder reference](../api/core/query-builder.md) for the fluent builders and `surql` DSL
- [Data manipulation](data-manipulation.md) for CRUD with the builders
- [Serialization](serialization.md) for working with `@Serializable` types
