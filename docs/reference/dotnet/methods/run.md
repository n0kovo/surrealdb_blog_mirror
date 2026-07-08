---
position: 1
title: Run
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/dotnet/methods/run.mdx"
---

# `.Run()` {#run}

Runs a [SurrealQL function](../../query-language/functions/database-functions/index.md).

```csharp title="Method Syntax"
await db.Run(name, version, args)
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
                `name`
                <label label="required" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The name of the [SurrealQL function](../../query-language/functions/database-functions/index.md).
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `version`
                <label label="optional" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The version of the [SurrealQL function](../../query-language/functions/database-functions/index.md).
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" scope="row" data-label="Arguments">
                `args`
                <label label="optional" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                The arguments used by the [SurrealQL function](../../query-language/functions/database-functions/index.md).
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
DateTime now = await db.Run<DateTime>("time::now");

string result = await db.Run<string>("string::repeat", ["test", 3]);
```
