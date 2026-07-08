---
position: 7
title: Bound queries
description: The JavaScript SDK provides bound queries and template tags for safely composing parameterised SurrealQL queries.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/concepts/bound-queries.mdx"
---

# Bound queries

When composing dynamic queries, it is important to avoid string interpolation to prevent injection vulnerabilities. The JavaScript SDK provides bound queries and the `surql` template tag to safely parameterise values, along with an expressions API for composing dynamic conditions.

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
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/surql"> ` surql `</a></td>
			<td scope="row" data-label="Description">Tagged template literal for composing parameterised queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/bound-query"> ` BoundQuery `</a></td>
			<td scope="row" data-label="Description">Class for manually building parameterised queries</td>
		</tr>
		<tr>
			<td scope="row" data-label="Utility"><a href="/docs/reference/javascript/api/utilities/expr"> ` expr() `</a></td>
			<td scope="row" data-label="Description">Composes type-safe expressions for use in queries</td>
		</tr>
	</tbody>
</table>

## Using the surql template tag

The `surql` tagged template literal is the recommended way to compose parameterised queries. Interpolated values are automatically bound as parameters, preventing injection and preserving type safety.

```ts

const name = 'John';
const minAge = 18;

const query = surql`SELECT * FROM users WHERE name = ${name} AND age > ${minAge}`;
const [users] = await db.query(query);
```

The `surrealql` export is an alias for `surql` if you prefer the longer name.

```ts

const query = surrealql`CREATE person CONTENT ${{ name: 'Tobie' }}`;
```

> [!NOTE]
> The SurrealQL [VSCode extension](https://marketplace.visualstudio.com/items?itemName=surrealdb.surrealql) provides syntax highlighting for surql template literals.

## Building queries with boundquery

The `BoundQuery` class provides manual control over query composition. You can construct a query with initial bindings, and incrementally append fragments with additional parameters.

```ts

const query = new BoundQuery(
    'SELECT * FROM users WHERE status = $status',
    { status: 'active' },
);

await db.query(query);
```

### Appending query fragments

Use the `.append()` method to conditionally add SurrealQL fragments. The method uses the same tagged template literal syntax as `surql`, so interpolated values are automatically bound.

```ts
const query = new BoundQuery('SELECT * FROM person');
const filterName = 'Alice';

if (filterName) {
    query.append(surql` WHERE name = ${filterName}`);
}

const [results] = await db.query(query);
```

## Composing expressions

The [expressions API](../api/utilities/expr.md) provides functions for building dynamic conditions in a type-safe way. Expressions integrate with both `surql` and query builder methods like `.where()`.

```ts
const checkActive = true;

await db.query(surql`SELECT * FROM users WHERE ${eq('active', checkActive)}`);
```

## Learn more

- [surql API reference](../api/utilities/surql.md) for template tag details
- [BoundQuery API reference](../api/utilities/bound-query.md) for manual query building
- [expr API reference](../api/utilities/expr.md) for the full expressions API
- [Executing queries](executing-queries.md) for running queries against the database
