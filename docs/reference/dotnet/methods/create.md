---
position: 1
title: Create
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/dotnet/methods/create.mdx"
---

# `.Create<T>()` {#create}

Creates a record in the database.

```csharp title="Method Syntax"
await db.Create<T>(resource, data)
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
                The table name or a [`RecordId`](../data-types.md#recordid) to create.
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
// Create a record with a random ID
var person = await db.Create<Person>("person");

// Create a record with a random ID & specific fields
var person = await db.Create("person", new Person { Name = "Tobie" });

// Create a record with a specific ID
var personToCreate = new Person
{
    Id = ("person", "tobie"),
    Name = "Tobie",
    Settings = new Settings
    {
        Active = true,
        Marketing = true,
    },
};
var result = await db.Create(personToCreate);
```
