---
position: 19
title: Sequence
description: Functions to work with sequences.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/functions/database-functions/sequence.mdx"
---

# Sequence functions

*Since v3.0.0*

These functions can be used to work with [sequences](../../statements/define/sequence.md).

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Function"><a href="#sequencenext">`sequence::next()`</a></td>
      <td scope="row" data-label="Description">Returns the next value in a sequence.</td>
    </tr>
  </tbody>
</table>

## `sequence::next`

The `sequence::next` function returns the next value in a sequence.

```surql title="API DEFINITION"
sequence::next($seq_name: string) -> int
```

```surql 
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "100"

*/

DEFINE SEQUENCE mySeq2 BATCH 1000 START 100 TIMEOUT 5s;
sequence::nextval('mySeq2');

-- 100
```
