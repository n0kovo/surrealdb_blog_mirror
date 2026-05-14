---
position: 1
title: Use
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/methods/use.mdx"
---

# `.Use()` {#use}

Switch to a specific namespace and database.

```csharp title="Method Syntax"
await db.Use(ns, db)
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
                `namespace`
                <label label="initially required" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                Switches to a specific namespace.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `database`
                <label label="initially required" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                Switches to a specific database.
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
await db.Use("main", "main");
```
