---
position: 4
title: Executing queries
description: The JavaScript SDK provides query builder methods and a raw query API for interacting with SurrealDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/concepts/executing-queries.mdx"
---

# Executing queries

The JavaScript SDK provides two ways to execute queries against SurrealDB: raw SurrealQL using the `.query()` method, and structured query builder methods like `.select()`, `.create()`, `.update()`, and `.delete()`. Both approaches support type-safe generics, chainable configuration, and multiple result formats.

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
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#query"> ` db.query(query, bindings?) `</a></td>
			<td scope="row" data-label="Description">Executes raw SurrealQL statements</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#select"> ` db.select(target) `</a></td>
			<td scope="row" data-label="Description">Selects records from the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#create"> ` db.create(target) `</a></td>
			<td scope="row" data-label="Description">Creates new records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#insert"> ` db.insert(target, data) `</a></td>
			<td scope="row" data-label="Description">Inserts one or multiple records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#update"> ` db.update(target) `</a></td>
			<td scope="row" data-label="Description">Updates existing records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#upsert"> ` db.upsert(target) `</a></td>
			<td scope="row" data-label="Description">Inserts or replaces records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#delete"> ` db.delete(target) `</a></td>
			<td scope="row" data-label="Description">Deletes records from the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#relate"> ` db.relate(from, edge, to) `</a></td>
			<td scope="row" data-label="Description">Creates graph relationships between records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-queryable#run"> ` db.run(name, args?) `</a></td>
			<td scope="row" data-label="Description">Executes a SurrealDB function or SurrealML model</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-session#set"> ` db.set(key, value) `</a></td>
			<td scope="row" data-label="Description">Defines a parameter on the session</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-session#unset"> ` db.unset(key) `</a></td>
			<td scope="row" data-label="Description">Removes a parameter from the session</td>
		</tr>
	</tbody>
</table>

## Running raw SurrealQL

The `.query()` method executes raw [SurrealQL statements](../../../reference/query-language/statements/overview.md) against the database. You can pass bindings as a second argument to safely inject variables into the query.

```ts
const [users] = await db.query<[User[]]>(
    'SELECT * FROM users WHERE age > $min_age',
    { min_age: 18 }
);
```

When executing multiple statements, each result maps to a position in the generic type parameter.

```ts
const [users, posts] = await db.query<[User[], Post[]]>(`
    SELECT * FROM users;
    SELECT * FROM posts;
`);
```

You can also pass a [bound query](bound-queries.md) for automatic parameterisation using the `surql` template tag.

```ts

const minAge = 18;
const [users] = await db.query<[User[]]>(
	surql`SELECT * FROM users WHERE age > ${minAge}`
);
```

## Selecting records

The `.select()` method reads records from the database. You can pass a [`Table`](../api/values/table.md) to select all records, a [`RecordId`](../api/values/record-id.md) to select a specific record, or a `RecordIdRange` to select a range.

```ts

const allUsers = await db.select(new Table('users'));

const user = await db.select(new RecordId('users', 'john'));
```

Query builder methods return chainable promises, allowing you to configure the query before it executes.

```ts

const users = await db.select(new Table('users'))
    .fields('name', 'email', 'age')
    .where(gt('age', 18))
    .limit(10)
    .start(0)
    .fetch('posts');
```

In the above example, we use the `gt()` function to create a greater than condition. This function is part of the [expression utilities](../api/utilities/expr.md) that are available in the SDK.
If you prefer to write raw condition, you can use the `raw()` function to insert the condition directly into the query.

```ts

const users = await db.select(new Table('users'))
    .fields('name', 'email', 'age')
    .where(raw('age > 18'))
    .limit(10)
    .start(0)
    .fetch('posts');
```

## Creating records

The `.create()` method creates new records. Use `.content()` to set the record data. When passed a `Table`, SurrealDB generates a random ID. When passed a `RecordId`, the record is created with that specific ID.

```ts
const user = await db.create(new RecordId('users', 'john'))
    .content({
        name: 'John Doe',
        email: 'john@example.com',
    });

const autoId = await db.create(new Table('users'))
    .content({ name: 'Jane Doe' });
```

## Inserting records

The `.insert()` method inserts one or multiple records at once. This is more efficient than calling `.create()` in a loop when working with bulk data.

```ts
const users = await db.insert(new Table('users'), [
    { name: 'Alice', email: 'alice@example.com' },
    { name: 'Bob', email: 'bob@example.com' },
]);
```

## Updating records

The `.update()` and `.upsert()` methods modify existing records. Instead of passing content as a second argument, you choose an update strategy by chaining `.content()`, `.merge()`, `.replace()`, or `.patch()`.

**Replace content**

Replace the entire record with new data. Any existing fields not included in the new data will be removed.

```ts
await db.update(new RecordId('users', 'john'))
    .content({
        name: 'John Smith',
        email: 'john.smith@example.com',
    });
```

**Merge fields**

Merge new fields into the existing record. Existing fields that are not specified remain unchanged.

```ts
await db.update(new RecordId('users', 'john'))
    .merge({ email: 'new@example.com' });
```

**JSON Patch**

Apply [JSON Patch](https://jsonpatch.com) operations for fine-grained modifications.

```ts
await db.update(new RecordId('users', 'john'))
    .patch([
        { op: 'replace', path: '/email', value: 'new@example.com' },
        { op: 'add', path: '/verified', value: true },
    ]);
```

You can also filter which records to update using `.where()`.

```ts
await db.update(new Table('users'))
    .merge({ verified: true })
    .where('age >= 18');
```

## Deleting records

The `.delete()` method removes records from the database. Like other query methods, it accepts a `Table`, `RecordId`, or `RecordIdRange`.

```ts
await db.delete(new RecordId('users', 'john'));

await db.delete(new Table('users'));
```

## Creating graph relationships

The `.relate()` method creates edges between records in SurrealDB's [graph model](../../../reference/query-language/statements/relate.md). You specify the source record(s), the edge table, and the target record(s).

```ts
await db.relate(
    new RecordId('users', 'john'),
    new Table('likes'),
    new RecordId('posts', '1'),
    { timestamp: new Date() },
);
```

## Running functions

The `.run()` method executes [SurrealDB functions](../../../reference/query-language/statements/define/function.md) or SurrealML models by name. You can pass arguments and optionally specify a model version.

```ts
const result = await db.run('fn::calculate_total', [100, 0.2]);

const prediction = await db.run('ml::predict', '1.0.0', [inputData]);
```

## Setting session parameters

You can define parameters on the current session using `.set()` and remove them with `.unset()`. Session parameters are available in all subsequent queries as `$name` variables and persist for the lifetime of the session.

```ts
await db.set('current_user', {
    first: 'Tobie',
    last: 'Morgan Hitchcock',
});

await db.query('CREATE post SET author = $current_user');

await db.unset('current_user');
```

## Collecting specific results

When running multi-statement queries, you can use `.collect()` to pick specific result indexes rather than receiving all results.

```ts
const [foo, bar] = await db.query(`
    LET $a = 1;
    LET $b = 2;
    SELECT * FROM users;
    SELECT * FROM posts;
`).collect<[User[], Post[]]>(2, 3);
```

## Streaming query responses

The `.stream()` method returns an async iterable of response frames, allowing you to process results incrementally. Each frame is either a value, a completion signal with query stats, or an error.

```ts
const stream = db.query('SELECT * FROM large_table').stream();

for await (const frame of stream) {
    if (frame.isValue<User>()) {
        processUser(frame.value);
    } else if (frame.isDone()) {
        console.log('Duration:', frame.stats.duration);
    } else if (frame.isError()) {
        console.error(frame.error);
    }
}
```

> [!NOTE]
> Streaming is currently not yet supported by SurrealDB, and this API exists primarily for future server-side record streaming.

## Serializing results

The `.json()` method converts SurrealDB value types in query results to their JSON representations. This is useful when you need to serialize results for APIs or tools that don't understand SurrealDB's custom types.

```ts
const [products] = await db.query<[Product[]]>('SELECT * FROM product').json();
```

Learn more about the `jsonify` utility in the [Utilities](utilities.md) concept page.

## Accessing response metadata

The `.responses()` method returns the full response objects including success status, query stats, and error information for each statement.

```ts
const responses = await db.query('SELECT * FROM users; SELECT * FROM posts').responses();

for (const response of responses) {
    if (response.success) {
        console.log('Result:', response.result);
        console.log('Duration:', response.stats?.duration);
    } else {
        console.error('Error:', response.error.message);
    }
}
```

## Retrying on write conflict

Under concurrent write load, a query can fail with a read/write conflict when another transaction touched the same data. Chain `.retry()` onto `.query()` or any query builder method to replay the operation automatically with exponential backoff.

```ts
const [n] = await db
    .query<[number]>('UPDATE counter:c SET n += 1 RETURN n')
    .retry({ attempts: 3 })
    .collect();

await db.delete(new RecordId('users', 'john')).retry();
```

Retry is off by default, and only applies to `.collect()` (or awaiting the query directly) — not `.responses()` or `.stream()`. For raw queries with multiple statements, only enable it when the statements are safe to apply more than once, since a retried query re-sends the whole thing.

You can also set a connection-wide default with the `retry` option on [`.connect()`](connecting-to-surrealdb.md#retrying-on-write-conflict), which `.retry()` overrides per call.

## Learn more

- [Bound queries](bound-queries.md) for parameterised query building with `surql` and `BoundQuery`
- [Live queries](live-queries.md) for real-time subscriptions
- [Transactions](transactions.md) for atomic multi-query operations
- [Connecting to SurrealDB](connecting-to-surrealdb.md#retrying-on-write-conflict) for connection-wide retry configuration
- [Query builders API reference](../api/queries/index.md) for detailed method signatures
- [SurrealQL statements](../../../reference/query-language/statements/overview.md) for the query language reference
