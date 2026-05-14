---
position: 13
title: Value types
description: The JavaScript SDK provides custom classes for SurrealDB-specific data types, ensuring type safety and data integrity.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/concepts/value-types.mdx"
---

# Value types

The JavaScript SDK provides custom classes for SurrealDB-specific data types that don't have direct JavaScript equivalents. These classes ensure type safety, preserve database precision, validate input, and integrate with the SDK's query methods.

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
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/record-id"> ` RecordId `</a></td>
			<td scope="row" data-label="Description">Type-safe record identifiers with table and ID components</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/table"> ` Table `</a></td>
			<td scope="row" data-label="Description">Type-safe table references for query methods</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/datetime"> ` DateTime `</a></td>
			<td scope="row" data-label="Description">Datetime values with nanosecond precision</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/duration"> ` Duration `</a></td>
			<td scope="row" data-label="Description">Time duration values with multiple unit support</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/decimal"> ` Decimal `</a></td>
			<td scope="row" data-label="Description">Arbitrary precision decimal numbers</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/uuid"> ` Uuid `</a></td>
			<td scope="row" data-label="Description">Universally unique identifiers (v4 and v7)</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/range"> ` Range `</a></td>
			<td scope="row" data-label="Description">Bounded or unbounded range values</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/file-ref"> ` FileRef `</a></td>
			<td scope="row" data-label="Description">References to files stored in SurrealDB</td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/javascript/api/values/geometry"> ` Geometry* `</a></td>
			<td scope="row" data-label="Description">GeoJSON geometry types (Point, Line, Polygon, etc.)</td>
		</tr>
	</tbody>
</table>

## Type mapping

SurrealQL types map to JavaScript types as follows:

<table>
	<thead>
		<tr>
			<th scope="col">SurrealQL type</th>
			<th scope="col">JavaScript type</th>
			<th scope="col">Example</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>`bool`</td>
			<td>`boolean`</td>
			<td>`true`, `false`</td>
		</tr>
		<tr>
			<td>`int`, `float`</td>
			<td>`number`</td>
			<td>`42`, `3.14`</td>
		</tr>
		<tr>
			<td>`string`</td>
			<td>`string`</td>
			<td>`"hello"`</td>
		</tr>
		<tr>
			<td>`null`</td>
			<td>`null`</td>
			<td>`null`</td>
		</tr>
		<tr>
			<td>`none`</td>
			<td>`undefined`</td>
			<td>`undefined`</td>
		</tr>
		<tr>
			<td>`array`</td>
			<td>`Array`</td>
			<td>`[1, 2, 3]`</td>
		</tr>
		<tr>
			<td>`object`</td>
			<td>`Object`</td>
			<td>`{`{ key: "value" }`}`</td>
		</tr>
		<tr>
			<td>`set`</td>
			<td>`Set`</td>
			<td>`new Set([1, 2, 3])`</td>
		</tr>
		<tr>
			<td>`bytes`</td>
			<td>`Uint8Array`</td>
			<td>`new Uint8Array([...])`</td>
		</tr>
		<tr>
			<td>`record`</td>
			<td><a href="/docs/languages/javascript/api/values/record-id">`RecordId`</a></td>
			<td>`new RecordId('users', 'john')`</td>
		</tr>
		<tr>
			<td>—</td>
			<td><a href="/docs/languages/javascript/api/values/table">`Table`</a></td>
			<td>`new Table('users')`</td>
		</tr>
		<tr>
			<td>`datetime`</td>
			<td><a href="/docs/languages/javascript/api/values/datetime">`DateTime`</a></td>
			<td>`DateTime.now()`</td>
		</tr>
		<tr>
			<td>`duration`</td>
			<td><a href="/docs/languages/javascript/api/values/duration">`Duration`</a></td>
			<td>`Duration.parse('1h30m')`</td>
		</tr>
		<tr>
			<td>`decimal`</td>
			<td><a href="/docs/languages/javascript/api/values/decimal">`Decimal`</a></td>
			<td>`new Decimal('19.99')`</td>
		</tr>
		<tr>
			<td>`uuid`</td>
			<td><a href="/docs/languages/javascript/api/values/uuid">`Uuid`</a></td>
			<td>`Uuid.v7()`</td>
		</tr>
		<tr>
			<td>`geometry`</td>
			<td><a href="/docs/languages/javascript/api/values/geometry">`Geometry*`</a></td>
			<td>`new GeometryPoint([1, 2])`</td>
		</tr>
		<tr>
			<td>`range`</td>
			<td><a href="/docs/languages/javascript/api/values/range">`Range`</a></td>
			<td>`new Range(1, 10)`</td>
		</tr>
		<tr>
			<td>`file`</td>
			<td><a href="/docs/languages/javascript/api/values/file-ref">`FileRef`</a></td>
			<td>`record.avatar`</td>
		</tr>
	</tbody>
</table>

## RecordId and Table

A [`RecordId`](../api/values/record-id.md) represents a unique record identifier consisting of a table name and an ID value. A [`Table`](../api/values/table.md) represents a table reference. In the v2 SDK, query methods no longer accept plain strings as table names — you must use the `Table` class to avoid ambiguity between table names and record IDs.

```ts

const userId = new RecordId('users', 'john');
const user = await db.select(userId);

const usersTable = new Table('users');
const allUsers = await db.select(usersTable);

const parsed = RecordId.parse('users:john');
```

The ID component of a `RecordId` can be a `string`, `number`, `bigint`, `Uuid`, array, or object. The `Table` class also supports a type parameter for type-safe query results.

```ts
const users = new Table<User>('users');
const results: User[] = await db.select(users);
```

## DateTime and Duration

A [`DateTime`](../api/values/datetime.md) represents a point in time with nanosecond precision. Unlike JavaScript's native `Date` which is limited to millisecond precision, `DateTime` preserves the full precision of SurrealDB timestamps. A [`Duration`](../api/values/duration.md) represents a span of time using SurrealQL duration syntax.

```ts

const now = DateTime.now();
const parsed = DateTime.parse('2024-01-15T12:00:00.123456789Z');
const jsDate = now.toDate();
const iso = now.toString();

const duration = Duration.parse('1h30m45s');
const ms = duration.toMilliseconds();
const seconds = duration.toSeconds();
```

## Decimal

A [`Decimal`](../api/values/decimal.md) represents an arbitrary-precision decimal number. This avoids the floating-point precision issues that occur with JavaScript's `number` type.

```ts

const price = new Decimal('19.99');
const display = price.toString();
const number = price.toNumber();
```

> [!NOTE]
> Converting a `Decimal` to a `number` with `.toNumber()` may lose precision. Use `.toString()` when precision matters.

## Uuid

A [`Uuid`](../api/values/uuid.md) represents a universally unique identifier. The class supports generating both v4 (random) and v7 (time-ordered) UUIDs.

```ts

const random = Uuid.v4();
const timeOrdered = Uuid.v7();
const parsed = Uuid.parse('550e8400-e29b-41d4-a716-446655440000');
```

## Range

A [`Range`](../api/values/range.md) represents a bounded or unbounded range of values. Ranges are used in SurrealQL for selecting slices of records by ID or filtering numeric and temporal values. A `RecordIdRange` is a specialization for querying a range of records from a table.

```ts

const numericRange = new Range(1, 10);

const idRange = new RecordIdRange('users', { begin: 'a', end: 'f' });
const slice = await db.select(idRange);
```

## FileRef

A `FileRef` represents a reference to a file stored in SurrealDB. File references are returned when working with [file uploads](../../../reference/query-language/language-primitives/data-types/files.md) and contain metadata about the stored file.

```ts
const [record] = await db.query('SELECT avatar FROM user:john');

if (record.avatar instanceof FileRef) {
    console.log(record.avatar.bucket);
    console.log(record.avatar.key);
}
```

## Geometry types

The SDK provides classes for all [GeoJSON geometry types](../../../reference/query-language/language-primitives/data-types/geometries.md): `GeometryPoint`, `GeometryLine`, `GeometryPolygon`, `GeometryMultiPoint`, `GeometryMultiLine`, `GeometryMultiPolygon`, and `GeometryCollection`.

```ts

const point = new GeometryPoint([longitude, latitude]);
const line = new GeometryLine([
    new GeometryPoint([1, 2]),
    new GeometryPoint([3, 4]),
]);
```

## Parsing from strings

Most value classes support parsing from string representations, matching the syntax used in SurrealQL.

```ts
const recordId = RecordId.parse('users:john');
const datetime = DateTime.parse('2024-01-15T12:00:00Z');
const duration = Duration.parse('1h30m45s');
const uuid = Uuid.parse('550e8400-e29b-41d4-a716-446655440000');
```

Parsing validates the input format and throws an error if the string is invalid.

## Using native dates

By default, the SDK returns `DateTime` instances for datetime values. If you prefer native JavaScript `Date` objects (at the cost of nanosecond precision), you can enable `useNativeDates` in the codec options.

```ts
const db = new Surreal({
    codecOptions: {
        useNativeDates: true,
    },
});
```

## String prefixes

The SDK provides tagged template functions that replicate SurrealQL's string prefixes in JavaScript. These create the corresponding value class from a template literal.

```ts

const string = s`I am a string`;
const date = d`2024-05-06T17:44:57.085Z`;
const record = r`person:tobie`;
const uuid = u`92b84bde-39c8-4b4b-92f7-626096d6c4d9`;
```

## Best practices

### Use type parameters for type-safe queries

```ts
const users = new Table<User>('users');
const results: User[] = await db.select(users);

const userId = new RecordId<'users', string>('users', 'john');
```

### Prefer value classes over raw strings

```ts
await db.select(new RecordId('users', 'john'));

// Avoid string-based queries when possible
await db.query('SELECT * FROM users:john');
```

### Validate parsed input

```ts
try {
    const uuid = Uuid.parse(userInput);
} catch (error) {
    console.error('Invalid UUID format');
}
```

## Learn more

- [Data Types API reference](../api/values/index.md) for the full list of value class documentation
- [SurrealQL data model](https://surrealdb.com/docs/reference/query-language/datamodel) for the database-level type system
- [Utilities](utilities.md) for comparing and converting values
