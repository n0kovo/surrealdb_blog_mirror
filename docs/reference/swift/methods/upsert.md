---
position: 10
title: upsert
description: The upsert() method for the SurrealDB Swift SDK creates or updates matching records.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/swift/methods/upsert.mdx"
---

# `upsert()` {#upsert}

Creates matching records if they do not exist, or updates them if they do.

```swift title="Method Syntax"
try await client.upsert(Model.self, content: content, where: predicate)
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
                `model`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The model type to upsert, e.g. `Person.self`.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `content`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The content to write to matching records.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `where`
                <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                A [predicate](../concepts/predicates.md) selecting which records to upsert.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
let upserted = try await client.upsert(
    Person.self,
    content: Person(id: nil, name: "Ada", age: 31),
    where: Person.Fields.name == "Ada"
)
```
