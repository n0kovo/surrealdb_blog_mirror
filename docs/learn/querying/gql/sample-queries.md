---
position: 3
title: Sample queries
description: Compare common GQL graph patterns against similar SurrealQL queries on the same seed graph.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/gql/sample-queries.mdx"
---

# Sample GQL and SurrealQL queries

*Since v3.2.0*

The examples below use the same **person / knows / city** seed graph as the OpenGQL language tests. SurrealQL snippets return the **same or equivalent row shape**, but are not a mechanical translation of the GQL compiler; they are idiomatic reads you can compare while learning.

## Prerequisites

Start a local instance with OpenGQL enabled and load the seed graph — see [GQL via HTTP](via-http.md#load-sample-data).

## List nodes by label

**GQL**

```gql title="Query"
MATCH (n:person) RETURN n.name AS name ORDER BY name
```

```bash title="cURL"
curl -sS -X POST -u "root:secret" \
  -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json" -H "Content-Type: text/plain" \
  -d 'MATCH (n:person) RETURN n.name AS name ORDER BY name' \
  http://localhost:8000/gql
```

```json title="Output"
[
	{ "name": "A" },
	{ "name": "B" },
	{ "name": "C" }
]
```

**SurrealQL**

```surql title="Query"
SELECT name FROM person ORDER BY name;
```

```surql title="Output"
[
	{ name: 'A' },
	{ name: 'B' },
	{ name: 'C' }
]
```

## Traverse an edge with a property filter

Only **person → person** `knows` edges with `since > 2020`.

**GQL**

```gql title="Query"
MATCH (a:person)-[k:knows]->(b:person)
WHERE k.since > 2020
RETURN a.name, b.name
ORDER BY a.name
```

```bash title="cURL"
curl -sS -X POST -u "root:secret" \
  -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json" -H "Content-Type: text/plain" \
  -d 'MATCH (a:person)-[k:knows]->(b:person) WHERE k.since > 2020 RETURN a.name, b.name ORDER BY a.name' \
  http://localhost:8000/gql
```

```json title="Output"
[
	{ "a.name": "A", "b.name": "B" }
]
```

**SurrealQL**

```surql title="Query"
SELECT in.name AS `a.name`, out.name AS `b.name`
FROM knows
WHERE since > 2020 AND record::tb(out) = 'person'
ORDER BY in.name;
```

```surql title="Output"
[
	{ 'a.name': 'A', 'b.name': 'B' }
]
```

## Optional match

Every `person`, with an optional `knows` edge to a `city` when one exists.

**GQL**

```gql title="Query"
MATCH (a:person)
OPTIONAL MATCH (a)-[k:knows]->(b:city)
RETURN a.name AS name, b.name AS city
ORDER BY name
```

```bash title="cURL"
curl -sS -X POST -u "root:secret" \
  -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json" -H "Content-Type: text/plain" \
  -d 'MATCH (a:person) OPTIONAL MATCH (a)-[k:knows]->(b:city) RETURN a.name AS name, b.name AS city ORDER BY name' \
  http://localhost:8000/gql
```

```json title="Output"
[
	{ "name": "A", "city": "London" },
	{ "name": "B", "city": null },
	{ "name": "C", "city": null }
]
```

**SurrealQL**

```surql title="Query"
SELECT name, array::first(->knows->city.name) AS city
FROM person
ORDER BY name;
```

```surql title="Output"
[
	{ name: 'A', city: 'London' },
	{ name: 'B', city: NONE },
	{ name: 'C', city: NONE }
]
```

## Aggregation with GROUP BY

Count outgoing **person → person** `knows` edges per person.

**GQL**

```gql title="Query"
MATCH (a:person)-[:knows]->(b:person)
RETURN a.name AS name, count(*) AS c
GROUP BY a.name
ORDER BY name
```

```bash title="cURL"
curl -sS -X POST -u "root:secret" \
  -H "Surreal-NS: main" -H "Surreal-DB: main" \
  -H "Accept: application/json" -H "Content-Type: text/plain" \
  -d 'MATCH (a:person)-[:knows]->(b:person) RETURN a.name AS name, count(*) AS c GROUP BY a.name ORDER BY name' \
  http://localhost:8000/gql
```

```json title="Output"
[
	{ "name": "A", "c": 1 },
	{ "name": "B", "c": 2 },
	{ "name": "C", "c": 1 }
]
```

**SurrealQL**

```surql title="Query"
SELECT in.name AS name, count() AS c
FROM knows
WHERE record::tb(out) = 'person'
GROUP BY in.name
ORDER BY name;
```

```surql title="Output"
[
	{ name: 'A', c: 1 },
	{ name: 'B', c: 2 },
	{ name: 'C', c: 1 }
]
```

## What to try next

The language-test corpus under `language-tests/tests/opengql/` in the SurrealDB repository covers variable-length quantifiers (`->{1,3}`, `->*`), path search (`ALL SHORTEST`, `SHORTEST k`), and multi-pattern comma joins. Those patterns have no single-line SurrealQL equivalent — they are the main reason to reach for GQL on the wire.
