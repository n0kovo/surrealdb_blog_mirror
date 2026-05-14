---
position: 4
title: Bytes
description: These functions can be used when working with bytes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/functions/database-functions/bytes.mdx"
---

# Bytes functions

These functions can be used when working with bytes in SurrealQL.

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Function"><a href="#byteslen">`bytes::len()`</a></td>
      <td scope="row" data-label="Description">Gives the length in bytes</td>
    </tr>
  </tbody>
</table>

## `bytes::len`

The `bytes::len` function returns the length in bytes of a `bytes` value.

```surql title="API DEFINITION"
bytes::len(bytes) -> int
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "[19, 67, 25]"

*/

RETURN [
    bytes::len(<bytes>"Simple ASCII string"),
    bytes::len(<bytes>"οὐ γὰρ δυνατόν ἐστιν ἔτι καθεύδειν"),
    bytes::len(<bytes>"청춘예찬 靑春禮讚")
];
```

```surql title="Output"
[ 19, 67, 25 ]
```
