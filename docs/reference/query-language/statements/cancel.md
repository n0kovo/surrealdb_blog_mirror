---
position: 6
title: CANCEL
description: The CANCEL statement can be used to cancel the statements within a transaction, reverting or rolling back any data modification made within the transaction as a whole.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/cancel.mdx"
---

# `CANCEL` statement

Each statement within SurrealDB is run within its own transaction. If a set of changes need to be made together, then groups of statements can be run together as a single transaction, either succeeding as a whole, or failing without leaving any residual data modifications. While a transaction will fail if any of its statements encounters an error, the `CANCEL` statement can also be used to cancel a transaction manually.

### Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
CANCEL [ TRANSACTION ];
```

  
**Railroad Diagram**

```
                     ╭───────────────────╮               
                     │                   │               
        ╭────────╮   │  ╭─────────────╮  │   ╭───╮       
├┼──────│ CANCEL │───╯──│ TRANSACTION │──╰───│ ; │─────┼┤
        ╰────────╯      ╰─────────────╯      ╰───╯
```

## Example usage

The following query shows example usage of this statement.

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
error = "The query was not executed due to a cancelled transaction"

[[test.results]]
error = "The query was not executed due to a cancelled transaction"

[[test.results]]
error = "The query was not executed due to a cancelled transaction"

[[test.results]]
error = "The query was not executed due to a cancelled transaction"

[[test.results]]
value = "NONE"

*/

BEGIN TRANSACTION;

-- Setup accounts
CREATE account:one SET balance = 135605.16;
CREATE account:two SET balance = 91031.31;

-- Move money
UPDATE account:one SET balance += 300.00;
UPDATE account:two SET balance -= 300.00;

-- Rollback all changes
CANCEL TRANSACTION;
```

`CANCEL` is not used to automatically cancel a transaction based on a condition such as inside an [IF..ELSE](if-else.md) block. Instead, a [THROW](throw.md) statement is used. THROW can be followed by any value, usually a string containing context behind the error.

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
error = "The query was not executed due to a failed transaction"

[[test.results]]
error = "The query was not executed due to a failed transaction"

[[test.results]]
error = "The query was not executed due to a failed transaction"

[[test.results]]
error = "The query was not executed due to a failed transaction"

[[test.results]]
error = "Specify a database to use"

[[test.results]]
error = "Cannot COMMIT: the transaction was aborted due to a prior error"

*/

BEGIN TRANSACTION;

-- Setup accounts
CREATE account:one SET balance = 135605.16;
CREATE account:two SET balance = 200.31;

-- Move money
UPDATE account:one SET balance += 300.00;
UPDATE account:two SET balance -= 300.00;

IF account:two.balance < 0 {
    THROW "Not enough funds";
};

COMMIT TRANSACTION;
```
