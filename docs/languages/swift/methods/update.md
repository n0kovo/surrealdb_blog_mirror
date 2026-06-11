---
position: 11
title: update
description: The update() method for the SurrealDB Swift SDK updates matching records, or a specific record.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/swift/methods/update.mdx"
---

# `update()` {#update}

Updates matching records of a model's table, or a single record by id.

```swift title="Method Syntax"
try await client.update(Model.self, content: content,
    where: predicate)
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
                The model type to update, e.g. `Person.self`.
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
                A [predicate](../concepts/predicates.md) selecting which records to update.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `recordID`
                <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                A [`SurrealRecordID`](../data-types.md#surrealrecordid) to update a single record.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
// Update matching records
let updated = try await client.update(
    Person.self,
    content: Person(id: nil, name: "Ada", age: 31),
    where: Person.Fields.name == "Ada"
)

// Update a specific record
let id = SurrealRecordID(table: "person", id: .string("ada"))
let record: Person? = try await client.update(
    recordID: id,
    content: Person(id: nil, name: "Ada", age: 31)
)
```
