---
position: 4
title: Data manipulation
description: Create, read, update, and delete records with the fluent builders in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/concepts/data-manipulation.mdx"
---

# Data manipulation

The Kotlin SDK provides fluent builders for the common CRUD operations. Each builder method (such as [`.select()`](../api/core/surreal-client.md#select) or [`.create()`](../api/core/surreal-client.md#create)) returns a [query builder](../api/core/query-builder.md) that you refine and then terminate with `await()` (raw [`JsonElement`](value-types.md)) or the typed [`awaitAs<T>()`](../api/core/query-builder.md#await-as) extension. Under the hood these compile to [SurrealQL](../../query-language/index.md) and dispatch through [`.query()`](executing-queries.md), mirroring the [JavaScript SDK](../../../languages/javascript.md).

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
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#select">`client.select(what)`</a></td>
			<td scope="row" data-label="Description">Selects records from a table or record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#create">`client.create(what)`</a></td>
			<td scope="row" data-label="Description">Creates a record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#update">`client.update(what)`</a></td>
			<td scope="row" data-label="Description">Replaces the content of records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#upsert">`client.upsert(what)`</a></td>
			<td scope="row" data-label="Description">Creates or updates records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#merge">`client.merge(what, data)`</a></td>
			<td scope="row" data-label="Description">Merges data into records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#patch">`client.patch(what, patches)`</a></td>
			<td scope="row" data-label="Description">Applies JSON patches to records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#delete">`client.delete(what)`</a></td>
			<td scope="row" data-label="Description">Deletes records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#relate">`client.relate(in, relation, out)`</a></td>
			<td scope="row" data-label="Description">Creates a graph edge between records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/kotlin/api/core/surreal-client#insert">`client.insert(into, data)`</a></td>
			<td scope="row" data-label="Description">Inserts one or more records</td>
		</tr>
	</tbody>
</table>

The `what` argument accepts a [`Table`](../api/values/table.md) to target every record in a table, a [`RecordId`](../api/values/record-id.md) to target a single record, or a [`RecordIdRange`](../api/values/record-id-range.md) to target a range.

## Creating records

Build content with [`buildJsonObject`](value-types.md) and finish with the typed [`awaitAs<T>()`](../api/core/query-builder.md#await-as).

```kotlin

@Serializable
data class Person(val name: String, val age: Int)

val ada: Person = client
    .create(RecordId("person", "ada"))
    .content(buildJsonObject {
        put("name", "Ada")
        put("age", 36)
    })
    .awaitAs()
```

## Selecting records

Refine a [`select`](../api/core/query-builder.md#select-query) with [`.where()`](../api/core/query-builder.md#where), [`.limit()`](../api/core/query-builder.md#limit), [`.start()`](../api/core/query-builder.md#start), [`.fetch()`](../api/core/query-builder.md#fetch), and others, using the [expression helpers](../api/core/query-builder.md#expressions).

```kotlin

val adults: List<Person> = client
    .select(Table("person"))
    .where(field("age") gte 18)
    .limit(50)
    .awaitAs()
```

## Updating and merging

Use [`.update()`](../api/core/surreal-client.md#update) to replace record content, [`.merge()`](../api/core/surreal-client.md#merge) to merge data, or [`.upsert()`](../api/core/surreal-client.md#upsert) to create or update. Control the returned payload with [`.returnMode()`](../api/core/query-builder.md#return-mode).

```kotlin

client
    .merge(RecordId("person", "ada"), buildJsonObject { put("age", 37) })
    .returnMode(ReturnMode.After)
    .await()
```

## Deleting records

```kotlin

client.delete(RecordId("person", "ada")).await()
```

## Relating records

Create a graph edge between two records with [`.relate()`](../api/core/surreal-client.md#relate).

```kotlin

client
    .relate(RecordId("person", "ada"), RecordId("wrote", "w1"), RecordId("article", "a1"))
    .content(buildJsonObject { put("year", 1843) })
    .await()
```

## Learn more

- [Query builder reference](../api/core/query-builder.md) for every builder method and expression helper
- [Executing queries](executing-queries.md) for raw SurrealQL
- [Value types](value-types.md) for `Table`, `RecordId`, and the JSON model
- [Serialization](serialization.md) for decoding into your own types
