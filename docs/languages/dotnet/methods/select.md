---
position: 1
title: Select
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/methods/select.mdx"
---

# `.Select<T>()` {#select}

Selects all records in a table, or a specific record, from the database.

```csharp title="Method Syntax"
await db.Select<T>(resource)
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
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The table name or a [`RecordId`](../data-types.md#recordid) to select.
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
// Select all records from a table
var people = await db.Select<Person>("person");

// Select a specific record from a table
var person = await db.Select<Person>(("person",
    "h5wxrf2ewk8xjxosxtyc"));
var person = await db.Select<Person>(new StringRecordId("person:h5wxrf2ewk8xjxosxtyc"));

// Select a specific record from a table, given a non-string id
var person = await db.Select<Person>(("person",
    new Guid("8424486b-85b3-4448-ac8d-5d51083391c7")));
```
