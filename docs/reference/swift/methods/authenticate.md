---
position: 6
title: authenticate
description: The authenticate() method for the SurrealDB Swift SDK authenticates the connection with a JWT token.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/swift/methods/authenticate.mdx"
---

# `authenticate()` {#authenticate}

Authenticates the current connection with a previously issued JWT access token.

```swift title="Method Syntax"
try await client.authenticate(token)
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
                `token`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The JWT access token to authenticate the connection with.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
try await client.authenticate(tokens.access)
```

You can also resume a session by supplying a token through a [`SessionContext`](../concepts/authentication.md#resuming-a-session) when constructing the client.
