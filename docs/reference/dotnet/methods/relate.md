---
position: 1
title: Relate
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/dotnet/methods/relate.mdx"
---

# `.Relate()` {#relate}

Creates a relation between records.

```csharp title="Method Syntax"
await db.Relate(table, @in, @out, data)
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
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `thing`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The table name or a [`RecordId`](../data-types.md#recordid) to create.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `@in`
                <label label="required" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The edge of the relation.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `@out`
                <label label="required" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The other edge of the relation.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `data`
                <label label="optional" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The document / record data to insert.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `cancellationToken`
                <label label="optional" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The cancellationToken enables graceful cancellation of asynchronous operations.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```csharp
var data = new WroteRelation { CreatedAt = DateTime.UtcNow,
    NumberOfPages = 14 };

await db.Relate<WroteRelation, WroteRelation>(
    "wrote",
    ("user", "one"),
    ("post", "one"),
    data
);
```
