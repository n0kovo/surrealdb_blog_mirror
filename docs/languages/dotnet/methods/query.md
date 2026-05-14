---
position: 1
title: Query
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/methods/query.mdx"
---

# `.Query()` {#query}

Runs a set of SurrealQL statements against the database.

```csharp title="Method Syntax"
await db.Query(sql)
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
                `sql`
                <label label="required" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                Specifies the SurrealQL statements.
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
// Execute query with params
const string table = "person";
var result = await db.Query($"CREATE person; SELECT * FROM type::table({table});");

// Get the first result from the first query
var created = result.GetValue<Person>(0);

// Get all of the results from the second query
var people = result.GetValue<List<Person>>(1);
```
