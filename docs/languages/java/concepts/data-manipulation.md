---
position: 4
title: Data manipulation
description: The Java SDK provides type-safe methods for creating, selecting, updating, upserting, and deleting records.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/concepts/data-manipulation.mdx"
---

# Data manipulation

The Java SDK provides dedicated methods for common CRUD operations on records and tables. These methods offer a structured alternative to writing raw [SurrealQL](../../../reference/query-language/index.md), with built-in type safety through Java generics and POJO deserialization.

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
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#create">`db.create(target, content)`</a></td>
			<td scope="row" data-label="Description">Creates one or more records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#select">`db.select(target)`</a></td>
			<td scope="row" data-label="Description">Selects records from a table or by ID</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#insert">`db.insert(target, content)`</a></td>
			<td scope="row" data-label="Description">Inserts one or more records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#update">`db.update(target, upType, content)`</a></td>
			<td scope="row" data-label="Description">Updates records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#upsert">`db.upsert(target, upType, content)`</a></td>
			<td scope="row" data-label="Description">Updates or creates records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#delete">`db.delete(target)`</a></td>
			<td scope="row" data-label="Description">Deletes records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#relate">`db.relate(from, table, to)`</a></td>
			<td scope="row" data-label="Description">Creates a graph relation</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#insert-relation">`db.insertRelation(target, content)`</a></td>
			<td scope="row" data-label="Description">Inserts a relation record</td>
		</tr>
	</tbody>
</table>

## Defining model classes

Data manipulation methods can work with POJOs (Plain Old Java Objects) for type-safe access. Model classes need a public no-argument constructor and fields that map to SurrealDB object keys. Use a [`RecordId`](../api/values/record-id.md) field named `id` to hold the record identifier.

```java
public class Person {
    public RecordId id;
    public String name;
    public int age;

    public Person() {}
}
```

## Creating records

The [`.create()`](../api/core/surreal.md#create) method creates new records. When called with a table name, SurrealDB generates a random ID and returns a list. When called with a [`RecordId`](../api/values/record-id.md), the record is created with that specific ID and a single result is returned.

```java
Person alice = new Person();
alice.name = "Alice";
alice.age = 30;

// Create with a generated ID — returns List<Value>
List<Value> created = db.create("person", alice);

// Create with a specific ID — returns Value
Value tobie = db.create(new RecordId("person", "tobie"), alice);

// Typed variant — returns List<Person>
List<Person> typed = db.create(Person.class, "person", alice);
```

## Selecting records

The [`.select()`](../api/core/surreal.md#select) method reads records from the database. When called with a table name, it returns an `Iterator`. When called with a `RecordId`, it returns an `Optional`.

```java
// Select all records from a table
Iterator<Value> all = db.select("person");

// Select a specific record
Optional<Value> one = db.select(new RecordId("person", "tobie"));

// Typed variants
Iterator<Person> allTyped = db.select(Person.class, "person");
Optional<Person> oneTyped = db.select(Person.class, new RecordId("person", "tobie"));
```

Use `selectSync()` instead of `select()` when you need thread-safe iteration over the results.

## Inserting records

The [`.insert()`](../api/core/surreal.md#insert) method inserts one or more records into a table using varargs. This is more efficient than calling `.create()` in a loop for bulk operations.

```java
Person alice = new Person();
alice.name = "Alice";
alice.age = 30;

Person bob = new Person();
bob.name = "Bob";
bob.age = 25;

List<Value> inserted = db.insert("person", alice, bob);
```

Use [`.insertRelation()`](../api/core/surreal.md#insert-relation) to insert graph edge records. See [Creating graph relations](#creating-graph-relations) for details.

## Updating records

The [`.update()`](../api/core/surreal.md#update) method modifies existing records. You specify the update strategy using the [`UpType`](../api/types/index.md#up-type) enum:

| UpType | Behavior |
|---|---|
| `UpType.CONTENT` | Replaces the entire record with the new content |
| `UpType.MERGE` | Merges new fields into the existing record |
| `UpType.PATCH` | Applies a JSON Patch to the record |

```java
Person updated = new Person();
updated.name = "Alice Smith";
updated.age = 31;

// Replace the entire record
db.update(new RecordId("person", "alice"), UpType.CONTENT, updated);

// Merge fields into the existing record
db.update(new RecordId("person", "alice"), UpType.MERGE, Map.of("age", 31));

// Update all records in a table
db.update("person", UpType.MERGE, Map.of("active", true));

// Typed variant
Person result = db.update(
    Person.class, new RecordId("person", "alice"), UpType.CONTENT, updated
);
```

## Upserting records

The [`.upsert()`](../api/core/surreal.md#upsert) method works like `.update()` but creates the record if it does not already exist. It accepts the same [`UpType`](../api/types/index.md#up-type) strategies.

```java
Person person = new Person();
person.name = "Charlie";
person.age = 28;

db.upsert(new RecordId("person", "charlie"), UpType.CONTENT, person);
```

## Deleting records

The [`.delete()`](../api/core/surreal.md#delete) method removes records from the database. You can delete a single record by [`RecordId`](../api/values/record-id.md), multiple records by passing several `RecordId` values, a range of records with [`RecordIdRange`](../api/values/record-id.md#record-id-range), or all records in a table by passing the table name.

```java
// Delete a single record
db.delete(new RecordId("person", "tobie"));

// Delete multiple specific records
db.delete(new RecordId("person", "alice"), new RecordId("person", "bob"));

// Delete a range of records
db.delete(new RecordIdRange("person", Id.from("a"), Id.from("f")));

// Delete all records in a table
db.delete("person");
```

## Creating graph relations

The [`.relate()`](../api/core/surreal.md#relate) method creates edges between records in SurrealDB's [graph model](../../../reference/query-language/statements/relate.md). You specify the source record, the edge table, and the target record. Optionally, you can attach content to the edge.

```java
db.relate(
    new RecordId("person", "tobie"),
    "likes",
    new RecordId("post", 1)
);

// With content on the edge
db.relate(
    new RecordId("person", "tobie"),
    "likes",
    new RecordId("post", 1),
    Map.of("timestamp", "2026-02-27T12:00:00Z")
);
```

You can also use [`.insertRelation()`](../api/core/surreal.md#insert-relation) to insert relation records with `in` and `out` fields, similar to how `.insert()` works for regular records.

```java
public class Likes extends InsertRelation {
    public String timestamp;

    public Likes() {}
}

Likes like = new Likes();
like.in = new RecordId("person", "tobie");
like.out = new RecordId("post", 1);
like.timestamp = "2026-02-27T12:00:00Z";

db.insertRelation(Likes.class, "likes", like);
```

## Learn more

- [Surreal API reference](../api/core/surreal.md) for complete method signatures
- [Value types](value-types.md) for type mappings and the Value class
- [Executing queries](executing-queries.md) for custom SurrealQL queries
- [RecordId reference](../api/values/record-id.md) for record identifier details
- [SurrealQL SELECT](../../../reference/query-language/statements/select.md), [CREATE](../../../reference/query-language/statements/create.md), [UPDATE](../../../reference/query-language/statements/update.md), [DELETE](../../../reference/query-language/statements/delete.md) for the underlying query statements
- [SurrealQL RELATE](../../../reference/query-language/statements/relate.md) for graph relation syntax
- [Record IDs](../../../reference/query-language/language-primitives/data-types/record-ids.md) for SurrealDB record identifier formats
