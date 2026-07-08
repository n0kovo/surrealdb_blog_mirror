---
position: 1
title: Delete
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/dotnet/methods/delete.mdx"
---

# `.Delete()` {#delete}

```csharp title="Method Syntax"
await db.Delete(resource)
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
                `thing`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The table name or a [`RecordId`](../data-types.md#recordid) to delete.
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
// Delete all records from a table
await db.Delete("person");

// Delete a specific record from a table
await db.Delete(("person", "h5wxrf2ewk8xjxosxtyc"));
```
