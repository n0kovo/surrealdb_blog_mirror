---
position: 9
title: create
description: The create() method for the SurrealDB Swift SDK creates a record in the database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/swift/methods/create.mdx"
---

# `create()` {#create}

Creates a record in the database, either with an auto-generated id or a specific id.

```swift title="Method Syntax"
try await client.create(content)
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
                `content`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The model instance to create. The table is derived from the model.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `recordID`
                <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                A [`SurrealRecordID`](../data-types.md#surrealrecordid) to create the record with a specific id.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
// Create with an auto-generated id
let created: [Person] = try await client.create(Person(id: nil, name: "Ada", age: 30))

// Create with a specific id
let id = SurrealRecordID(table: "person", id: .string("ada"))
let record: Person? = try await client.create(
    recordID: id,
    content: Person(id: nil, name: "Ada", age: 30)
)
```
