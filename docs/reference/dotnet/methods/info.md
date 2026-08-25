---
position: 8
title: Info
description: This method returns the record of an authenticated scope user.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/dotnet/methods/info.mdx"
---

# `.Info<T>()`

This method returns the record of an authenticated scope user.

```csharp title="Method Syntax"
await db.Info<T>()
```

## Arguments

<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Properties</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Properties">
                `cancellationToken`
                <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The cancellationToken enables graceful cancellation of asynchronous operations.
            </td>
        </tr>
    </tbody>
</table>

## Example usage

```csharp
var currentUser = await db.Info<User>();
```
