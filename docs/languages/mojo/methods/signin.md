---
position: 21
title: signin
description: The signin() method for the SurrealDB Mojo SDK signs in to the database with credentials.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/signin.mdx"
---

# `signin()`

Signs in to the database with CBOR-encoded credentials. On success, the returned token is stored on the client for subsequent requests.

```python title="Method Syntax"
client.signin(credentials_cbor, session)
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
            <td colspan="2" scope="row" data-label="Argument">`credentials_cbor`</td>
            <td colspan="2" scope="row" data-label="Description">The credentials, CBOR-encoded as a map, as a `List[UInt8]`.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
from surrealdb import CborCodec
from std.collections import List

var codec = CborCodec()
var pairs = List[Tuple[String, List[UInt8]]]()
pairs.append(Tuple(String("user"), codec.encode_text("root")))
pairs.append(Tuple(String("pass"), codec.encode_text("root")))

var resp = client.signin(codec.encode_map(pairs))
```

> [!NOTE]
> `signin` operates on a stateful session, which is provided by the WebSocket transport. WebSocket support is rolling out. Over HTTP, supply credentials with the `access_token` field on `ConnectOptions`.

### See also

- [Authentication](../concepts/authentication.md)
- [`signup()`](signup.md)
