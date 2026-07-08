---
position: 14
title: Utilities
description: SQON provides value comparison, conversion, and escaping utilities. The SDK adds query-building helpers on top.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/concepts/utilities.mdx"
---

# Utilities

Helpers are split across two packages. [`@surrealdb/sqon`](https://www.npmjs.com/package/@surrealdb/sqon) covers value comparison, conversion, and escaping. The `surrealdb` driver adds query-building tools for parameterised SurrealQL. Import from `surrealdb` when you use the driver and want both layers in one place.

```ts
// SQON (either package)

// SDK only
```

## SQON utilities

These live in `@surrealdb/sqon` alongside the [value types](value-types.md). You do not need the database client to use them.

<table>
	<thead>
		<tr>
			<th scope="col">Utility</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/equals"> ` equals(a, b) `</a></td>
			<td scope="row" data-label="Description">Deep equality comparison for all value types</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility">` jsonify(value) `</td>
			<td scope="row" data-label="Description">Converts value types to JSON-safe string representations</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/escape"> ` escapeIdent(name) `</a></td>
			<td scope="row" data-label="Description">Escapes table and field names for use in SurrealQL</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/escape"> ` escapeKey(key) `</a></td>
			<td scope="row" data-label="Description">Escapes object keys for use in queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/escape"> ` escapeRid(value) `</a></td>
			<td scope="row" data-label="Description">Escapes record ID components</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/escape"> ` escapeValue(value) `</a></td>
			<td scope="row" data-label="Description">Escapes arbitrary values for embedding in queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility">` toSurqlString(value) `</td>
			<td scope="row" data-label="Description">Converts a value tree to a SurrealQL string representation</td>
		</tr>
	</tbody>
</table>

### Comparing values with deep equality

`===` compares object references, so two `RecordId` instances with the same table and ID still fail an identity check. `equals()` walks the structure instead, including nested objects, arrays, SurrealDB value classes, `Date`, `RegExp`, and mixed `bigint`/`number` values.

```ts

const id1 = new RecordId('users', 'john');
const id2 = new RecordId('users', 'john');

console.log(id1 === id2);        // false (different references)
console.log(equals(id1, id2));    // true (same value)
```

Handy when you want to know whether a fetched record changed between two reads:

```ts
const user1 = await db.select(userId);
const user2 = await db.select(userId);

if (!equals(user1, user2)) {
    console.log('Record was modified');
}
```

> [!NOTE]
> Individual value classes also expose an `.equals()` instance method for single-type comparisons (e.g. `recordId.equals(other)`). Use the standalone `equals()` function for generic or cross-type comparisons.

### Jsonifying query results

`jsonify()` turns SurrealDB value classes in a result into the JSON string forms SurrealDB would use. Plain numbers, strings, and objects are left as they are. The return type reflects the conversion.

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

You can also call `.json()` on [query methods](executing-queries.md#converting-results-to-json) to jsonify the result in one step.

For JSON with explicit type wrappers (for example `{ "$recordId": ... }`), use [`JsonCodec`](codecs.md#json-codec) instead.

### Escaping identifiers and values

The escape helpers quote identifiers and values for hand-built SurrealQL. Prefer [bound queries](bound-queries.md) or [value classes](value-types.md) when you can.

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
> Escaping alone does not stop injection. Use [`surql`](bound-queries.md) or [`BoundQuery`](../api/utilities/bound-query.md) for dynamic values.

### Converting to SurrealQL strings

`toSurqlString()` walks a value tree (objects, arrays, SQON classes) and returns a SurrealQL literal string. Useful for logs, debugging, or SurrealQL snippets outside bound queries.

```ts

toSurqlString(new RecordId('person', 'tobie')); // r"person:tobie"
toSurqlString(new Decimal('3.14'));             // 3.14dec
```

## SDK utilities

These ship with the `surrealdb` driver and tie into its query engine. They are not exported from `@surrealdb/sqon`.

<table>
	<thead>
		<tr>
			<th scope="col">Utility</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/expr"> ` expr() `</a></td>
			<td scope="row" data-label="Description">Composes type-safe expressions for WHERE clauses and conditions</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/surql"> ` surql `</a></td>
			<td scope="row" data-label="Description">Tagged template for composing parameterised queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/bound-query"> ` BoundQuery `</a></td>
			<td scope="row" data-label="Description">Parameterised query class with manual control</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility">` s, d, r, u `</td>
			<td scope="row" data-label="Description">Tagged templates for SurrealQL string, datetime, record, and UUID prefixes</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/is-retryable-conflict"> ` isRetryableConflict(error) `</a></td>
			<td scope="row" data-label="Description">Default predicate used by `.retry()` to detect retryable write conflicts</td>
		</tr>
	</tbody>
</table>

### Building expressions

`expr()` and its operators build conditions for `.where()` and for `surql` templates. See [Bound queries](bound-queries.md#composing-expressions) for the full list.

```ts

const premiumAdults = expr(and(
    eq('tier', 'premium'),
    gte('age', 18),
));

const users = await db.select(new Table('users')).where(premiumAdults);
```

Operators cover comparisons (`eq`, `ne`, `gt`, `gte`, `lt`, `lte`), logic (`and`, `or`, `not`), strings and arrays (`contains`, `containsAny`, `containsAll`), geometry (`inside`, `outside`, `intersects`), and search (`matches`, `knn`).

### Composing parameterised queries

`surql` and `BoundQuery` bind parameters so you do not splice user input into query strings. See [Bound queries](bound-queries.md).

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

### String prefix templates

The `s`, `d`, `r`, and `u` templates build typed literals with SurrealQL's string prefixes. See [Value types](value-types.md#string-prefixes).

## Best practices

### Use surql for parameterisation

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
- [Codecs](codecs.md) for serialising value types over CBOR and JSON
- [Bound queries](bound-queries.md) for safe query composition
- [Value types](value-types.md) for SurrealDB-specific data classes
