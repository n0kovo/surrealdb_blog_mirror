---
position: 14
title: Utilities
description: The JavaScript SDK provides utility functions for comparing values, converting to JSON, escaping identifiers, and building expressions.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/concepts/utilities.mdx"
---

# Utilities

The JavaScript SDK provides a set of utility functions for common tasks like deep value comparison, JSON conversion, SurrealQL string serialization, identifier escaping, and expression building. These complement the SDK's core query methods and [value types](value-types.md).

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Utility</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/equals"> ` equals(a, b) `</a></td>
			<td scope="row" data-label="Description">Deep equality comparison for all value types</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/expr"> ` expr() `</a></td>
			<td scope="row" data-label="Description">Composes type-safe expressions for WHERE clauses and conditions</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/surql"> ` surql `</a></td>
			<td scope="row" data-label="Description">Tagged template for composing parameterized queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/bound-query"> ` BoundQuery `</a></td>
			<td scope="row" data-label="Description">Parameterized query class with manual control</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/escape"> ` escapeIdent(name) `</a></td>
			<td scope="row" data-label="Description">Escapes table and field names for use in SurrealQL</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/escape"> ` escapeKey(key) `</a></td>
			<td scope="row" data-label="Description">Escapes object keys for use in queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/escape"> ` escapeRid(value) `</a></td>
			<td scope="row" data-label="Description">Escapes record ID components</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/languages/javascript/api/utilities/escape"> ` escapeValue(value) `</a></td>
			<td scope="row" data-label="Description">Escapes arbitrary values for embedding in queries</td>
		</tr>
	</tbody>
</table>

## Comparing values with deep equality

JavaScript's `===` operator compares objects by reference, which means two `RecordId` instances with the same table and ID are not considered equal. The `equals()` function performs deep structural comparison across all value types, including SurrealDB's custom classes, nested objects, arrays, `Date`, `RegExp`, and `bigint`/`number` normalization.

```ts

const id1 = new RecordId('users', 'john');
const id2 = new RecordId('users', 'john');

console.log(id1 === id2);        // false (different references)
console.log(equals(id1, id2));    // true (same value)
```

This is particularly useful for detecting changes in query results.

```ts
const user1 = await db.select(userId);
const user2 = await db.select(userId);

if (!equals(user1, user2)) {
    console.log('Record was modified');
}
```

> [!NOTE]
> Individual value classes also expose an `.equals()` instance method for single-type comparisons (e.g. `recordId.equals(other)`). Use the standalone `equals()` function for generic or cross-type comparisons.

## Jsonifying query results

The `jsonify()` function converts SurrealDB value types in a result to their JSON representations, in the same manner that SurrealDB would serialize them. It only transforms SurrealDB-specific classes, leaving all other values untouched, and is fully type-safe.

```ts

const result = jsonify({
    rid: new RecordId('person', 'tobie'),
    dec: new Decimal('3.333333'),
    dur: new Duration('1d2h'),
    num: 123,
    str: 'hello',
});
```

```json
{
    "rid": "person:tobie",
    "dec": "3.333333",
    "dur": "1d2h",
    "num": 123,
    "str": "hello"
}
```

You can also jsonify query results directly using the `.json()` chain on [query methods](executing-queries.md#converting-results-to-json).

## Building expressions

The `expr()` function and its companion operators allow you to compose dynamic, type-safe conditions for use in query builder methods like `.where()` and in `surql` templates. See [Bound queries](bound-queries.md#composing-expressions) for the full guide.

```ts

const premiumAdults = expr(and(
    eq('tier', 'premium'),
    gte('age', 18),
));

const users = await db.select(new Table('users')).where(premiumAdults);
```

Available operators include comparison (`eq`, `ne`, `gt`, `gte`, `lt`, `lte`), logical (`and`, `or`, `not`), string/array (`contains`, `containsAny`, `containsAll`), geometry (`inside`, `outside`, `intersects`), and search (`matches`, `knn`).

## Composing parameterized queries

The `surql` tagged template and `BoundQuery` class provide safe parameterization for dynamic queries. See [Bound queries](bound-queries.md) for the full guide.

```ts

const minAge = 18;
const query = surql`SELECT * FROM users WHERE age >= ${minAge}`;
const [users] = await db.query(query);

const bound = new BoundQuery(
    'SELECT * FROM users WHERE status = $status',
    { status: 'active' },
);
bound.bind('tier', 'premium');
const [results] = await db.query(bound);
```

## Escaping identifiers and values

When you need to construct SurrealQL strings manually, the escape functions ensure that identifiers and values are properly quoted. In most cases, you should prefer [bound queries](bound-queries.md) or the [value type classes](value-types.md) instead of manual escaping.

```ts

escapeIdent('users');           // 'users'
escapeIdent('user-table');      // '`user-table`'
escapeIdent('select');          // '`select`'

escapeKey('user-property');     // properly escaped for object notation

escapeRid('john');              // 'john'
escapeRid('user@email.com');    // '`user@email.com`'

escapeValue('hello');           // "'hello'"
escapeValue(42);                // '42'
escapeValue(null);              // 'null'
escapeValue(undefined);         // 'none'
```

> [!WARNING]
> Escape functions are not a complete defense against injection. Always prefer parameterized queries using [`surql`](bound-queries.md) or [`BoundQuery`](../api/utilities/bound-query.md).

## Best practices

### Use surql for parameterization

```ts
const query = surql`SELECT * FROM users WHERE name = ${userName}`;

// Avoid string concatenation (injection risk)
const query = `SELECT * FROM users WHERE name = '${userName}'`;
```

### Use expr for complex conditions

```ts
const condition = expr(and(
    eq('status', 'active'),
    gte('age', 18),
));

await db.select(new Table('users')).where(condition);
```

### Use equals for deep comparison

```ts
if (equals(recordId1, recordId2)) {
    // Same value
}

// Avoid reference comparison (only true if same instance)
if (recordId1 === recordId2) { ... }
```

## Learn more

- [equals API reference](../api/utilities/equals.md) for deep comparison details
- [expr API reference](../api/utilities/expr.md) for expression builder operators
- [surql API reference](../api/utilities/surql.md) for template tag details
- [BoundQuery API reference](../api/utilities/bound-query.md) for manual query building
- [Escape functions API reference](../api/utilities/escape.md) for all escape utilities
- [Bound queries](bound-queries.md) for safe query composition
- [Value types](value-types.md) for SurrealDB-specific data classes
