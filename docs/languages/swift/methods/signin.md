---
position: 4
title: signin
description: The signin() method for the SurrealDB Swift SDK signs in to a specific authentication level.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/swift/methods/signin.mdx"
---

# `signin()` {#signin}

Signs this connection in to a specific authentication level and returns the issued tokens.

```swift title="Method Syntax"
let tokens = try await client.signin(credentials)
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
                `credentials`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The credentials to authenticate with: one of `.root`, `.namespace`, `.database`, `.accessVariables` or `.accessBearer`.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
// Root user
let tokens = try await client.signin(.root(username: "root",
    password: "root"))

// Database user
let tokens = try await client.signin(.database(
    namespace: "myapp",
    database: "mydb",
    username: "db_user",
    password: "secret"
))

// Record access with variables
let tokens = try await client.signin(.accessVariables(
    namespace: "myapp",
    database: "mydb",
    access: "account",
        variables: ["email": .string("user@example.com"),
        "pass": .string("secret")]
))
```

See [Authentication](../concepts/authentication.md) for every supported credentials variant.
