---
position: 1
title: Update
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/dotnet/methods/update.mdx"
---

# `.Update<T>()` {#update}

Updates all records in a table, or a specific record, in the database.

```csharp title="Method Syntax"
await db.Update<T>(thing, data)
```

> [!NOTE]
> This function replaces the current document / record data with the specified data.

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
                The table name or the specific [`RecordId`](../data-types.md#recordid) to update.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `data`
               <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The document / record data to update.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `cancellationToken`
                <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The cancellationToken enables graceful cancellation of asynchronous operations.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```csharp
var post = new Post
{
    Id = ("post", "another"),
    Title = "A new article",
    Content = "This is a new article created using the .NET SDK"
};

// Updates a single record
await db.Update(post);

var data = new Person
{
    Name = "Tobie",
    Settings = new Settings
    {
        Active = true,
        Marketing = true,
    },
};

// Updates all records inside the "person" table
await db.Update("person", data);
```
