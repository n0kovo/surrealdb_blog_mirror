---
position: 13
title: query
description: The query() method for the SurrealDB Swift SDK runs a query built with the query DSL or macros.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/swift/methods/query.mdx"
---

# `query()` {#query}

Runs a query built with the [query DSL](../concepts/query-dsl.md), either a query macro such as `#select` or a `SurrealDSL` builder call.

```swift title="Method Syntax"
try await client.query(query)
```

### Arguments

<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `query`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                A query produced by a query macro or a `SurrealDSL` builder call.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
// Using a query macro
let selectQuery = #select(Person.self, where: Person.Fields.age > 18, limit: 10)
let people = try await client.query(selectQuery)

// Using the SurrealDSL builder
let query = SurrealDSL.select(Person.self, where: Person.Fields.age >= 21, limit: 50)
let result = try await client.query(query)
```

For arbitrary SurrealQL, see [`queryRaw`](query-raw.md).
