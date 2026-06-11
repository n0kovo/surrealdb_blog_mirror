---
position: 2
title: Sample queries
description: Compare common GraphQL queries against similar SurrealQL SELECT patterns
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/graphql/sample-queries.mdx"
---

# Sample GraphQL and SurrealQL queries

*Since v3.1.0*

From SurrealDB 3.1.0, SurrealDB’s GraphQL layer uses **Apollo-style** names: a **pluralised list** field (for example `people` for table `person`), a **singular fetch** field `person(id: …)`, and `people_aggregate` for aggregates. Under the hood these map to SurrealQL-style reads (typically `SELECT`). The SurrealQL here is a rough equivalent for the same or similar data shape. See [GraphQL overview](overview.md#schema-naming) for the full naming table.

Before trying the examples, enable GraphQL and define data in the current namespace and database (see [GraphQL overview](overview.md) using [`DEFINE CONFIG GRAPHQL AUTO`](../../../reference/query-language/statements/define/config.md)). The snippets below assume:

- Namespace **`main`**, database **`main`**
- Root authentication **`root`** / **`secret`**
- A `person` table with `name` and `age`, and records `person:simon` and `person:marcus` as in [GraphQL via HTTP](via-http.md)

```surql title="Schema and sample data"
DEFINE TABLE person SCHEMAFULL;
DEFINE FIELD name ON TABLE person TYPE string;
DEFINE FIELD age ON TABLE person TYPE number;
CREATE person:simon SET name = "Simon", age = 23;
CREATE person:marcus SET name = "Marcus", age = 28;
DEFINE CONFIG GRAPHQL AUTO;
```

## List records and choose fields

GraphQL here returns a list of objects, similar to `SELECT` without `ONLY`.

**GraphQL**

```graphql title="Query"
query {
	people {
		name
		age
	}
}
```

```graphql title="Output"
{
	"data": {
		"people": [
			{
				"age": 28,
				"name": "Marcus"
			},
			{
				"age": 23,
				"name": "Simon"
			}
		]
	}
}
```

**SurrealQL**

```surql title="Query"
SELECT name, age FROM person;
```

```surql title="Output"
[
	{
		age: 28,
		name: 'Marcus'
	},
	{
		age: 23,
		name: 'Simon'
	}
]
```

**cURL (HTTP)**

```bash
curl -X POST -u "root:secret" -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json"
  -d '{ "query": "query { people { name age } }" }' http://localhost:8000/graphql
```

## Fetch a single record by id

Use **`person(id: …)`** with the **record key** (`simon`, not `person:simon` in the argument). The GraphQL `id` field on the result is the full record id.

**GraphQL**

```graphql title="Query"
query {
	person(id: "simon") {
		id
		name
		age
	}
}
```

```graphql title="Output"
{
	"data": {
		"person": {
			"id": "person:simon",
			"name": "Simon",
			"age": 23
		}
	}
}
```

**SurrealQL**

```surql title="Query"
SELECT * FROM ONLY person:simon;
```

```surql title="Output"
{
	age: 23,
	id: person:simon,
	name: 'Simon'
}
```

**cURL (HTTP)**

```bash
curl -X POST -u "root:secret" -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json"
  -d '{ "query": "query { person(id: \"simon\") { id name age } }" }' http://localhost:8000/graphql
```

## Limit how many records are returned

GraphQL uses **`limit`** (and optional **`start`** for offset). SurrealQL uses `LIMIT` / `START` and `ONLY` to return a single record as opposed to an array containing a single record.

**GraphQL**

```graphql title="Query"
query {
	people(limit: 1) {
		name
		age
	}
}
```

```graphql title="Output"
{
	"data": {
		"people": [
			{
				"age": 28,
				"name": "Marcus"
			}
		]
	}
}
```

**SurrealQL**

```surql title="Query"
SELECT name, age FROM ONLY person LIMIT 1;
```

```surql title="Output"
{
	age: 28,
	name: 'Marcus'
}
```

**cURL (HTTP)**

```bash
curl -X POST -u "root:secret" -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json"
  -d '{ "query": "query { people(limit: 1) { name age } }" }' http://localhost:8000/graphql
```

## Filter records

GraphQL accepts **`filter`** or **`where`** with the generated input type for the table. For a scalar field, use comparison keys such as **`eq`**, **`ne`**, **`gt`**, and **`lt`** where the schema allows them.

**GraphQL**

```graphql title="Query"
query {
	people(where: { age: { eq: 23 } }) {
		name
	}
}
```

```graphql title="Output"
{
	"data": {
		"people": [
			{
				"name": "Simon"
			}
		]
	}
}
```

**SurrealQL**

```surql title="Query"
SELECT name FROM person WHERE age = 23;
```

```surql title="Output"
[
	{
		name: 'Simon'
	}
]
```

**cURL (HTTP)**

```bash
curl -X POST -u "root:secret" -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json"
  -d '{ "query": "query { people(where: { age: { eq: 23 } }) { name } }" }' http://localhost:8000/graphql
```

## Order results

Use an **`order`** argument with **`asc`** or **`desc`** and a field name.

**GraphQL**

```graphql title="Query"
query {
	people(order: { asc: age }) {
		name
		age
	}
}
```

```graphql title="Output"
{
	"data": {
		"people": [
			{
				"age": 23,
				"name": "Simon"
			},
			{
				"age": 28,
				"name": "Marcus"
			}
		]
	}
}
```

**SurrealQL**

```surql title="Query"
SELECT name, age FROM person ORDER BY name ASC;
```

```surql title="Output"
[
	{
		age: 23,
		name: 'Simon'
	},
	{
		age: 28,
		name: 'Marcus'
	}
]
```

**cURL (HTTP)**

```bash
curl -X POST -u "root:secret" -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json"
  -d '{ "query": "query { people(order: { asc: age }) { name age } }" }' http://localhost:8000/graphql
```

## Next steps

- Query the same endpoint from HTTP clients: [GraphQL via HTTP](via-http.md)
- Optional: [Bruno](via-bruno.md) or [Surrealist](via-surrealist.md)

For the full configuration surface (tables, functions, limits), see [`DEFINE CONFIG GRAPHQL`](../../../reference/query-language/statements/define/config.md).
