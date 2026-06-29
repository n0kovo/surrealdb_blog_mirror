---
position: 7
title: COMMIT
description: The COMMIT statement is used to commit a set of statements within a transaction, ensuring that all data modifications become a permanent part of the database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/commit.mdx"
---

# `COMMIT` statement

Each statement within SurrealDB is run within its own transaction by default. If a set of changes need to be made together, then groups of statements can be run together as a single transaction, either succeeding as a whole, or failing without leaving any residual data modifications. A `COMMIT` statement is used at the end of such a transaction to make the data modifications a permanent part of the database.

### Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
COMMIT [ TRANSACTION ];
```

  
**Railroad Diagram**

```
                     ╭───────────────────╮               
                     │                   │               
        ╭────────╮   │  ╭─────────────╮  │   ╭───╮       
├┼──────│ COMMIT │───╯──│ TRANSACTION │──╰───│ ; │─────┼┤
        ╰────────╯      ╰─────────────╯      ╰───╯
```

## Example usage

The following query shows example usage of this statement.

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "[{ balance: 135605.16f, id: account:one }]"

[[test.results]]
value = "[{ balance: 91031.31f, id: account:two }]"

[[test.results]]
value = "[{ balance: 135905.16f, id: account:one }]"

[[test.results]]
value = "[{ balance: 90731.31f, id: account:two }]"

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

-- Finalise all changes
COMMIT TRANSACTION;
```

The following two options can be used at any point if a transaction must be cancelled without commiting the changes:

* [CANCEL](cancel.md) to manually cancel the transaction.
* [THROW](throw.md) to cancel a transaction with an optional error message. THROW is the only way to cancel a transaction based on a condition, such as inside an [IF..ELSE](if-else.md) block.

In addition, a `RETURN` statement can be used to return early from a successful transaction. This is often used in order to return a customized output.

```surql
/**[test]

[[test.results]]
value = "'Money sent! Status:
{ balance: 135905.16f, id: account:one }
{ balance: 90731.31f, id: account:two, wants_to_send_money: true }'"

[[test.results]]
value = "{ balance: 135905.16f, id: account:one }"

[[test.results]]
value = "{ balance: 90731.31f, id: account:two, wants_to_send_money: true }"

*/

BEGIN;

CREATE account:one SET balance = 135605.16;
CREATE account:two SET balance = 91031.31, wants_to_send_money = true;

IF !account:two.wants_to_send_money {
    THROW "Customer doesn't want to send any money!";
};

LET $first = UPDATE ONLY account:one SET balance += 300.00;
LET $second = UPDATE ONLY account:two SET balance -= 300.00;

RETURN "Money sent! Status:\n" + <string>$first + '\n' + <string>$second;

COMMIT;
```

```surql title="Output"
'Money sent! Status:
{ balance: 135905.16f, id: account:one }
{ balance: 90731.31f, id: account:two, wants_to_send_money: true }'
```
