---
position: 14
title: queryRaw
description: The queryRaw() method for the SurrealDB Swift SDK runs a raw SurrealQL query with bound parameters.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/swift/methods/query-raw.mdx"
---

# `queryRaw()` {#query-raw}

Executes a raw SurrealQL string with bound parameters and returns one [`RPCQueryResult`](../data-types.md#rpcqueryresult) per statement.

```swift title="Method Syntax"
try await client.queryRaw(sql, bindings: bindings)
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
                `sql`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The raw SurrealQL query to execute.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `bindings`
                <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                A dictionary of [`SurrealValue`](../data-types.md#surrealvalue) parameters referenced in the query.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
let results: [RPCQueryResult] = try await client.queryRaw(
    "SELECT * FROM person WHERE age > $minAge LIMIT $limit;",
    bindings: [
        "minAge": .int(18),
        "limit": .int(50)
    ]
)

for row in results {
    if row.status == .ok {
        print(row.result)
    }
}
```
