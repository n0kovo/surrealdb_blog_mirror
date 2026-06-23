---
position: 23
title: transaction_multi
description: The transaction_multi() method for the SurrealDB Mojo SDK runs a list of statements as one atomic transaction.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/transaction-multi.mdx"
---

# `transaction_multi()`

Wraps a list of statements in `BEGIN TRANSACTION;` and `COMMIT TRANSACTION;` and sends them as a single atomic query. This works on any transport and is the recommended way to run a transaction over HTTP.

```python title="Method Syntax"
client.transaction_multi(statements, session)
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
            <td colspan="2" scope="row" data-label="Argument">`statements`</td>
            <td colspan="2" scope="row" data-label="Description">The statements to run, as a `List[String]`. A trailing semicolon is added to each if missing.</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">`session`</td>
            <td colspan="2" scope="row" data-label="Description">An optional session id.</td>
        </tr>
    </tbody>
</table>

### Example usage

```python
from std.collections import List

var stmts = List[String]()
stmts.append("CREATE car:a SET wheels = 4;")
stmts.append("CREATE car:b SET wheels = 4;")
var resp = client.transaction_multi(stmts)
```

If any statement fails, the whole transaction is rolled back.

### See also

- [Transactions](../concepts/transactions.md)
- [`begin_transaction()`](begin-transaction.md)
