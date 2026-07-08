---
position: 4
title: Data manipulation
description: The Go SDK provides generic functions for selecting, creating, updating, and deleting records in SurrealDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/golang/concepts/data-manipulation.mdx"
---

# Data manipulation

The Go SDK provides generic top-level functions for common CRUD operations on records and tables. These functions work with [`*DB`](../api/core/db.md), [`*Session`](../api/core/session.md), and [`*Transaction`](../api/core/transaction.md) through the [`sendable`](../api/types/index.md#sendable) constraint, and return typed results through Go generics.

This page covers how to target tables and records, and how to select, create, insert, update, merge, patch, and delete data.

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
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#select">`surrealdb.Select[T](ctx, s, what)`</a></td>
			<td scope="row" data-label="Description">Selects all records from a table, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#create">`surrealdb.Create[T](ctx, s, what, data)`</a></td>
			<td scope="row" data-label="Description">Creates a new record with optional data</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#insert">`surrealdb.Insert[T](ctx, s, table, data)`</a></td>
			<td scope="row" data-label="Description">Inserts one or multiple records into a table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#insertrelation">`surrealdb.InsertRelation[T](ctx, s, rel)`</a></td>
			<td scope="row" data-label="Description">Inserts a relation record between two records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#relate">`surrealdb.Relate[T](ctx, s, rel)`</a></td>
			<td scope="row" data-label="Description">Creates a relation with an auto-generated ID</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#update">`surrealdb.Update[T](ctx, s, what, data)`</a></td>
			<td scope="row" data-label="Description">Replaces the entire content of a record or all records in a table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#upsert">`surrealdb.Upsert[T](ctx, s, what, data)`</a></td>
			<td scope="row" data-label="Description">Creates a record if it does not exist, or replaces it entirely</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#merge">`surrealdb.Merge[T](ctx, s, what, data)`</a></td>
			<td scope="row" data-label="Description">Merges data into a record, preserving unmentioned fields</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#patch">`surrealdb.Patch(ctx, s, what, patches)`</a></td>
			<td scope="row" data-label="Description">Applies JSON Patch operations to a record or table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/golang/api/core/db#delete">`surrealdb.Delete[T](ctx, s, what)`</a></td>
			<td scope="row" data-label="Description">Deletes a specific record or all records from a table</td>
		</tr>
	</tbody>
</table>

## Targeting tables and records

Most data manipulation functions accept a `what` parameter that determines the scope of the operation. You can pass a [`Table`](../api/values/table.md) to target all records in a table, or a [`RecordID`](../api/values/record-id.md) to target a specific record.

```go

all, err := surrealdb.Select[[]Person](ctx, db, models.Table("persons"))

one, err := surrealdb.Select[Person](ctx, db, models.NewRecordID("persons", "tobie"))
```

When a [`Table`](../api/values/table.md) is passed, operations that return data return a slice. When a [`RecordID`](../api/values/record-id.md) is passed, they return a single value. Use the appropriate type parameter to match.

## Selecting records

[`Select`](../api/core/db.md#select) retrieves records from the database. Pass a [`Table`](../api/values/table.md) to get all records, or a [`RecordID`](../api/values/record-id.md) to get a single record.

```go
persons, err := surrealdb.Select[[]Person](ctx, db, models.Table("persons"))
if err != nil {
	log.Fatal(err)
}

tobie, err := surrealdb.Select[Person](ctx, db, models.NewRecordID("persons", "tobie"))
if err != nil {
	log.Fatal(err)
}
```

## Creating records

[`Create`](../api/core/db.md#create) creates a new record. Pass a [`Table`](../api/values/table.md) to generate a random ID, or a [`RecordID`](../api/values/record-id.md) to specify the ID explicitly. The data can be a struct or a map.

```go
person, err := surrealdb.Create[Person](ctx, db, models.Table("persons"), Person{
	Name:    "Tobie",
	Surname: "Morgan Hitchcock",
})

specific, err := surrealdb.Create[Person](ctx, db, models.NewRecordID("persons", "tobie"), map[string]any{
	"name":    "Tobie",
	"surname": "Morgan Hitchcock",
})
```

## Inserting records

[`Insert`](../api/core/db.md#insert) inserts one or more records into a table. This is useful for bulk operations.

```go
persons, err := surrealdb.Insert[Person](ctx, db, models.Table("persons"), []map[string]any{
	{"name": "Alice", "age": 30},
	{"name": "Bob", "age": 25},
})
```

## Creating relations

The SDK provides two ways to create graph edges between records.

[`Relate`](../api/core/db.md#relate) creates a relation with an auto-generated ID. The [`Relationship.ID`](../api/types/index.md#relationship) field is ignored.

```go
rel, err := surrealdb.Relate[map[string]any](ctx, db, &surrealdb.Relationship{
	In:       models.NewRecordID("persons", "tobie"),
	Out:      models.NewRecordID("posts", "first"),
	Relation: models.Table("wrote"),
	Data:     map[string]any{"created_at": "2026-01-01T00:00:00Z"},
})
```

[`InsertRelation`](../api/core/db.md#insertrelation) works like [`Insert`](../api/core/db.md#insert) but for relation tables. It allows you to specify the ID explicitly via the [`Relationship.ID`](../api/types/index.md#relationship) field.

```go
rel, err := surrealdb.InsertRelation[map[string]any](ctx, db, &surrealdb.Relationship{
	In:       models.NewRecordID("persons", "tobie"),
	Out:      models.NewRecordID("posts", "first"),
	Relation: models.Table("wrote"),
})
```

## Replacing records

[`Update`](../api/core/db.md#update) replaces the entire content of a record or all records in a table. Fields not included in the new data are removed.

```go
updated, err := surrealdb.Update[Person](ctx, db, models.NewRecordID("persons", "tobie"), Person{
	Name:    "Tobie",
	Surname: "Morgan Hitchcock",
})
```

> [!NOTE]
> Because [`Update`](../api/core/db.md#update) performs a full replacement, omitted fields are deleted from the record. Use [`Merge`](../api/core/db.md#merge) if you want to preserve existing fields.

## Upserting records

[`Upsert`](../api/core/db.md#upsert) creates a record if it does not already exist, or replaces it entirely if it does.

```go
person, err := surrealdb.Upsert[Person](ctx, db, models.NewRecordID("persons", "tobie"), Person{
	Name:    "Tobie",
	Surname: "Morgan Hitchcock",
})
```

## Merging data

[`Merge`](../api/core/db.md#merge) deep-merges the provided data into the existing record, preserving fields not mentioned in the merge payload.

```go
merged, err := surrealdb.Merge[Person](ctx, db, models.NewRecordID("persons", "tobie"), map[string]any{
	"age": 35,
})
```

## Applying patches

[`Patch`](../api/core/db.md#patch) applies [JSON Patch (RFC 6902)](https://jsonpatch.com/) operations to a record or all records in a table. Each operation is a [`PatchData`](../api/types/index.md#patchdata) with `Op`, `Path`, and `Value` fields.

```go
patches, err := surrealdb.Patch(ctx, db, models.NewRecordID("persons", "tobie"), []surrealdb.PatchData{
	{Op: "replace", Path: "/surname", Value: "Hitchcock"},
	{Op: "add", Path: "/verified", Value: true},
})
```

Supported operations include `add`, `remove`, `replace`, `move`, `copy`, and `test`.

## Deleting records

[`Delete`](../api/core/db.md#delete) removes a specific record or all records from a table. The function returns the deleted record(s).

```go
deleted, err := surrealdb.Delete[Person](ctx, db, models.NewRecordID("persons", "tobie"))

allDeleted, err := surrealdb.Delete[[]Person](ctx, db, models.Table("persons"))
```

## Learn more

- [DB API reference](../api/core/db.md) for complete function signatures and parameters
- [Executing queries](executing-queries.md) for running SurrealQL statements directly
- [Value types](value-types.md) for the types used by data manipulation functions
- [RecordID reference](../api/values/record-id.md) for constructing record identifiers
- [SurrealQL CRUD statements](../../query-language/statements/overview.md) for the underlying query language
