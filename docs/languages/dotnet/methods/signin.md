---
position: 1
title: SignIn
description: The .NET SDK for SurrealDB enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/methods/signin.mdx"
---

# `.SignIn()` {#signin}

Signs in to a root, namespace, database or scope user.

```csharp title="Method Syntax"
await db.SignIn(credentials)
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
                `credentials`
                <label label="required" />
            </td>
            <td colspan="2" scope="col" scope="row" data-label="Description">
                Variables used in a signin query.
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

**Root user**

```csharp
// Sign in as root user
await db.SignIn(new RootAuth { Username = "root",
    Password = "secret" });
```

**Namespace user**

```csharp
// Sign in using namespace auth
await db.SignIn(
    new NamespaceAuth
    {
        Namespace = "main", 
        Username = "johndoe", 
        Password = "password123" 
    }
);
```

**Database user**

```csharp
// Sign in using database auth
await db.SignIn(
    new DatabaseAuth
    {
        Namespace = "main", 
        Database = "main", 
        Username = "johndoe", 
        Password = "password123" 
    }
);
```

**Record Access**

```csharp
// Sign in with Record Access
var authParams = new AuthParams
{
    Namespace = "main",
    Database = "main",
    Access = "user",
    Email = "info@surrealdb.com",
    Password = "123456"
};

Jwt jwt = await db.SignIn(authParams);

public class AuthParams : ScopeAuth
{
	public string? Username { get; set; }
	public string? Email { get; set; }
	public string? Password { get; set; }
}
```

**Scopes**

```csharp
// Sign in as a scoped user
var authParams = new AuthParams
{
    Namespace = "main",
    Database = "main",
    Scope = "user",
    Email = "info@surrealdb.com",
    Password = "123456"
};

Jwt jwt = await db.SignIn(authParams);

public class AuthParams : ScopeAuth
{
	public string? Username { get; set; }
	public string? Email { get; set; }
	public string? Password { get; set; }
}
```

You can invalidate the authentication for the current connection using the [`Invalidate()` method](invalidate.md).
