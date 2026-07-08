---
position: 5
title: call
description: The call() method for the SurrealDB Mojo SDK runs a SurrealQL function.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/methods/call.mdx"
---

# `call()`

Runs a SurrealQL function, built-in or custom, and returns its result.

```python title="Method Syntax"
client.call(fn_name, args, session, txn)
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
            <td colspan="2" scope="row" data-label="Argument">`fn_name`</td>
            <td colspan="2" scope="row" data-label="Description">The function name, for example `fn::greet` or `time::now`.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`args`</td>
            <td colspan="2" scope="row" data-label="Description">The function arguments, each CBOR-encoded, as a `List[List[UInt8]]`.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`txn`</td>
            <td colspan="2" scope="row" data-label="Description">An optional transaction id.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
from surrealdb import CborCodec
from std.collections import List

var codec = CborCodec()
var args = List[List[UInt8]]()
args.append(codec.encode_text("Chiru"))

var resp = client.call("fn::greet", args)
```
