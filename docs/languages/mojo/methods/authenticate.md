---
position: 3
title: authenticate
description: The authenticate() method for the SurrealDB Mojo SDK authenticates the current connection with a token.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/authenticate.mdx"
---

# `authenticate()`

Authenticates the current connection with a token, and stores it on the client for subsequent requests.

```python title="Method Syntax"
client.authenticate(token, session)
```

### Arguments

<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Argument</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`token`</td>
            <td colspan="2" scope="row" data-label="Description">The JWT to authenticate with.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
client.authenticate("eyJhbGciOi...")
```

### See also

- [Authentication](../concepts/authentication.md)
- [`invalidate()`](invalidate.md)
