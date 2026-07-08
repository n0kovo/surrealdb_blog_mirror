---
position: 5
title: Value types
description: The Java SDK maps SurrealDB data types to native Java types and provides custom classes for complex values.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/concepts/value-types.mdx"
---

# Value types

The Java SDK maps SurrealDB data types to native Java types where possible and provides custom classes for types that have no direct Java equivalent. You can work with results as untyped [`Value`](../api/values/value.md) objects or pass a `Class<T>` to SDK methods for automatic deserialization into POJOs.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Class</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/value">`Value`</a></td>
			<td scope="row" data-label="Description">Represents any SurrealDB value</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/record-id">`RecordId`</a></td>
			<td scope="row" data-label="Description">Represents a record identifier</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/geometry">`Geometry`</a></td>
			<td scope="row" data-label="Description">Represents geometric data</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/file-ref">`FileRef`</a></td>
			<td scope="row" data-label="Description">Represents a file reference</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/datetime">`Datetime`</a></td>
			<td scope="row" data-label="Description">Maps to `java.time.ZonedDateTime`</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/duration">`Duration`</a></td>
			<td scope="row" data-label="Description">Maps to `java.time.Duration`</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/table">`Table`</a></td>
			<td scope="row" data-label="Description">Table name value, maps to `String`</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/reference/java/api/values/range">`Range`</a></td>
			<td scope="row" data-label="Description">Range value with start and end bounds</td>
		</tr>
	</tbody>
</table>

## Type mapping

SurrealDB types map to Java types as follows:

| SurrealDB Type | Java Type | Notes |
|---|---|---|
| `string` | `String` | |
| `int` | `long` | |
| `float` | `double` | |
| `bool` | `boolean` | |
| `null` | `null` | |
| `none` | `Value.isNone()` | Check via [`Value`](../api/values/value.md) |
| [`datetime`](../../query-language/language-primitives/data-types/datetimes.md) | `ZonedDateTime` | `java.time` |
| [`duration`](../../query-language/language-primitives/data-types/datetimes.md#durations-and-datetimes) | `Duration` | `java.time` |
| `decimal` | `BigDecimal` | `java.math` |
| `uuid` | `UUID` | `java.util` |
| `bytes` | `byte[]` | |
| `array` | [`Array`](../api/values/value.md#array) | SDK custom class |
| `object` | [`Object`](../api/values/value.md#object) | SDK custom class |
| [`record`](../../query-language/language-primitives/data-types/record-ids.md) | [`RecordId`](../api/values/record-id.md) | SDK custom class |
| [`geometry`](../../query-language/language-primitives/data-types/geometries.md) | [`Geometry`](../api/values/geometry.md) | SDK custom class |
| [`file`](../../query-language/language-primitives/data-types/files.md) | [`FileRef`](../api/values/file-ref.md) | SDK custom class |
| `table` | `String` | Via `Value.getTable()` |
| `range` | [`Value`](../api/values/value.md) | Via `Value.getRangeStart()` / `Value.getRangeEnd()` |

## Working with the Value class

[`Value`](../api/values/value.md) is the untyped representation of any SurrealDB value. It provides type-checking methods and getters for extracting the underlying Java value.

```java
Value value = response.take(0);

if (value.isLong()) {
    long count = value.getLong();
}

if (value.isString()) {
    String name = value.getString();
}

if (value.isArray()) {
    Array items = value.getArray();
}
```

To convert a `Value` directly into a POJO, use `.get(Class)`.

```java
Person person = value.get(Person.class);
```

## Using POJOs for type-safe access

Instead of working with raw [`Value`](../api/values/value.md) objects, you can pass a `Class<T>` to most SDK methods to get automatic deserialization. POJOs need a public no-argument constructor, and their fields map directly to SurrealDB object keys.

```java
public class Person {
    public RecordId id;
    public String name;
    public int age;

    public Person() {}
}

List<Person> people = db.create(Person.class, "person", newPerson);
Optional<Person> tobie = db.select(Person.class, new RecordId("person", "tobie"));
```

## Constructing record identifiers

[`RecordId`](../api/values/record-id.md) represents a SurrealDB record identifier consisting of a table name and an ID value. The ID can be a `long`, `String`, `UUID`, `Array`, or `Object`.

```java
RecordId numericId = new RecordId("person", 1L);
RecordId stringId = new RecordId("person", "tobie");
RecordId uuidId = new RecordId("person", UUID.randomUUID());

Array compositeKey = new Array(2026, "Q1");
RecordId arrayId = new RecordId("report", compositeKey);

Object objectKey = new Object();
objectKey.put("region", "eu");
objectKey.put("year", 2026);
RecordId objectId = new RecordId("report", objectKey);
```

## Iterating arrays and objects

The SDK's `Array` class implements `Iterable<Value>`, and the `Object` class implements `Iterable<Entry>`. You can iterate over them using standard Java for-each loops.

```java
Array items = value.getArray();
for (Value item : items) {
    System.out.println(item.getString());
}

Object obj = value.getObject();
for (Entry entry : obj) {
    System.out.println(entry.getKey() + ": " + entry.getValue());
}
```

When iterating from multiple threads, use `synchronizedIterator()` to get a thread-safe iterator.

```java
Iterator<Value> safeIterator = items.synchronizedIterator();
```

## Learn more

- [Value API reference](../api/values/value.md) for complete Value class documentation
- [RecordId API reference](../api/values/record-id.md) for record identifier details
- [Geometry API reference](../api/values/geometry.md) for geometric data types
- [FileRef API reference](../api/values/file-ref.md) for file references
- [Datetime API reference](../api/values/datetime.md) for datetime handling
- [Duration API reference](../api/values/duration.md) for duration handling
- [Table API reference](../api/values/table.md) for table name values
- [Range API reference](../api/values/range.md) for range values
- [Data manipulation](data-manipulation.md) for using types with CRUD operations
- [SurrealQL data model](https://surrealdb.com/docs/reference/query-language/datamodel) for the full list of SurrealDB data types
