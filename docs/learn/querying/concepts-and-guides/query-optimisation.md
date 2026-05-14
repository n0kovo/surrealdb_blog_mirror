---
position: 2
title: Query optimisation
description: "Practical ideas for faster SurrealQL: EXPLAIN, record ranges, async events, denormalised flags, and indexes."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/concepts-and-guides/query-optimisation.mdx"
---

# Query optimisation

This page contains a number of tips you can use to optimise your queries in SurrealDB. For more details on each pattern, see the linked pages in the API documentation.

## Inspecting the plan with `EXPLAIN`

Prefix a read-only statement with `EXPLAIN` to see how the database plans to run it. Add `ANALYZE` if you want timing and row metrics as well. As the output of this statement is informational and may change between versions, be sure not to build tooling that depends on an exact shape.

```surql
EXPLAIN SELECT * FROM person WHERE email = 'user@example.com';
```

Full syntax and options can be found in the [`EXPLAIN` reference](../../../reference/query-language/statements/explain.md).

## Record ranges

When you can identify records by record ID order (for example numeric or time-ordered IDs), selecting with a range on the ID (`table:start..end`) avoids scanning the whole table. A `WHERE` filter over the same records can be much more expensive because it typically implies a wider scan.

```surql
SELECT * FROM person:1..1000;
```

See [record IDs](../../../reference/query-language/language-primitives/data-types/record-ids.md) and [record ranges in `SELECT`](../../../reference/query-language/statements/select.md#record-ranges).

## Async events

By default, events run in the same transaction as the write that triggers them, which keeps behaviour easy to reason about but can slow commits if event logic is heavy.

Using the [`ASYNC` clause in a `DEFINE EVENT` statement](../../../reference/query-language/statements/define/event.md#async-events) runs the handler **after** the triggering transaction. This leads to lower write latency, with the caveat that it is an opt out of the ACID guarantees by default in all transactions. As such, it should only be used when this tradeoff is acceptable.

More context: [Reactive patterns](../../schema-management/events-and-triggers/reactive-patterns.md).

## Pre-allocated fields (denormalised flags)

If a query repeatedly does a lookup or subquery only to answer a yes/no question (“is this user registered?”), consider storing the answer in a field. For example, an `is_registered` field updated when the user completes registration is more efficiently written ahead of time as a boolean value as opposed to using an extra `SELECT` inside another query.

This will still need a strategy to keep the flag up to date, but allows you to avoid paying the check cost on every read.

## Indexes and iterators

- Define indexes that match real filter and sort patterns; see [`DEFINE INDEX`](../../../reference/query-language/statements/define/indexes.md).
- The [`WITH`](../../../reference/query-language/clauses/with.md) clause can force or restrict which index the planner uses when you need predictable behaviour (for example comparing plans with `EXPLAIN`).

## Fast table counts

For `SELECT count() … GROUP ALL` over a whole table, a `COUNT` index maintains a running total instead of scanning every row each time. See the note under [`SELECT` — `COUNT` index](../../../reference/query-language/statements/select.md#using-a-count-index-to-speed-up-count-in-group-all-queries).
