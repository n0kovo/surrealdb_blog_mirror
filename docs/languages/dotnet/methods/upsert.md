---
position: 1
title: Upsert
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/methods/upsert.mdx"
---

# `.Upsert<T>()` {#upsert}

Creates or updates a specific record.

```csharp title="Method Syntax"
await db.Upsert<T>(data)
```

> [!NOTE]
> This function creates a new document / record or replaces the current one with the specified data.

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
                `data`
                <label label="required" />
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
var person = new Person
{
        Id = ("person", "tobie"),
        // Id is mandatory to apply create or update
    Name = "Tobie",
    Settings = new Settings
    {
        Active = true,
        Marketing = true,
    },
};

// Create a new record when it doesn't exist
var created = await db.Upsert(person);

// Update an existing record when it does exist
var updated = await db.Upsert(person);
```
