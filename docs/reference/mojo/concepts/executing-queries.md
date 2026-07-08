---
position: 3
title: Executing queries
description: Learn how to run SurrealQL with the Mojo SDK, use the CRUD convenience methods, and read responses.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/mojo/concepts/executing-queries.mdx"
---

# Executing queries

The primary way to run SurrealQL with the Mojo SDK is `query()`, which sends one or more statements and returns an `RpcResponse`.

```python
var resp = client.query("SELECT * FROM person WHERE age > 18;")
```

## Reading the response

Every call returns an `RpcResponse`. Check `is_ok()` before reading the result. The decoded text representation is available on `result`, and the raw bytes on `result_raw`.

```python
if resp.is_ok():
    # CBOR-decoded text representation for convenience
    if resp.result:
        print(resp.result.value())
    # Raw CBOR bytes if you need them
    print("bytes:", len(resp.result_raw))
else:
    print("code:", resp.error_code().value())
    print("message:", resp.error_message().value())
```

`RpcResponse` exposes the following:

<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Member</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Member">`is_ok()`</td>
            <td colspan="2" scope="row" data-label="Description">Returns `True` when there is no error.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Member">`is_error()`</td>
            <td colspan="2" scope="row" data-label="Description">Returns `True` when the response carries an error.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Member">`has_result()`</td>
            <td colspan="2" scope="row" data-label="Description">Returns `True` when a result is present.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Member">`result`</td>
            <td colspan="2" scope="row" data-label="Description">The decoded text representation, as `Optional[String]`.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Member">`result_raw`</td>
            <td colspan="2" scope="row" data-label="Description">The raw CBOR or JSON bytes, as `List[UInt8]`.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Member">`error_message()`</td>
            <td colspan="2" scope="row" data-label="Description">The error message, as `Optional[String]`.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Member">`error_code()`</td>
            <td colspan="2" scope="row" data-label="Description">The error code, as `Optional[Int]`.</td>
        </tr>
    </tbody>
</table>

## Convenience methods

The SDK wraps the most common statements so you do not have to write the SurrealQL by hand. Each takes the table or record to act on and a JSON document.

```python
client.create("person", '{ "name": "Chiru", "age": 30 }')
client.select("person:chiru")
client.update("person:chiru", '{ "age": 31 }')
client.delete("person:chiru")
client.insert("person", '[{ "name": "Alice" }, { "name": "Bob" }]')
```

These build a SurrealQL statement under the hood. For example, `create("person", data)` runs `CREATE person CONTENT <data>;`. See the method reference for the full list, including [`upsert`](../methods/upsert.md), [`merge`](../methods/merge.md), [`patch`](../methods/patch.md), and [`insert_relation`](../methods/insert-relation.md).

## Bindings

`query()` accepts a `bindings_json` argument.

```python
var resp = client.query("SELECT * FROM person;", "{}")
```

> [!NOTE]
> A dedicated API for passing arbitrary CBOR bindings is on the roadmap. Today, CBOR connections support the default `"{}"`, while JSON-RPC connections accept raw JSON strings via `bindings_json`.

## Sessions and transactions

Each `query` is wrapped in its own implicit transaction by the server. To run several statements atomically, use [`transaction_multi`](../methods/transaction-multi.md), or the [transactions](transactions.md) concept page for the full picture.
