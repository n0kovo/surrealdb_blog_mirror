---
position: 7
title: isRetryableConflict
description: Default predicate used to detect retryable write conflicts.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/api/utilities/is-retryable-conflict.mdx"
---

# `isRetryableConflict()` {#isretryableconflict}

The `isRetryableConflict()` function is the default predicate used by [`.retry()`](../queries/query.md#retry) to decide whether a failed query should be retried. SurrealDB does not currently expose a structured retryable error kind, so the predicate matches on the error message.

**Import:**
```ts
```

**Source:** [utils/index.ts](https://github.com/surrealdb/surrealdb.js/blob/main/packages/sdk/src/utils/index.ts)

## Function signature

```ts
function isRetryableConflict(error: Error): boolean
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`error` <label label="required" /></td>
            <td>`Error`</td>
            <td>The error thrown by a failed query.</td>
        </tr>
    </tbody>
</table>

#### Returns
`boolean` - `true` if the error looks like a retryable write conflict (its message contains "conflict" or "can be retried"), `false` otherwise

## Overriding the default predicate

Pass a custom `retryable` function in [`RetryOptions`](../types/index.md#retryoptions) to change what counts as retryable, optionally reusing `isRetryableConflict` as a base:

```ts

await db.query('UPDATE counter:c SET n += 1 RETURN n')
    .retry({
        attempts: 5,
        retryable: (error) => isRetryableConflict(error) || error.message.includes('busy')
    })
    .collect();
```

> [!NOTE]
> Confirm the exact conflict message against the SurrealDB server version you target — the heuristic matches on message text rather than a structured error kind.

## See also

- [Query.retry()](../queries/query.md#retry) - Retry queries on write conflict
- [RetryOptions](../types/index.md#retryoptions) - Retry configuration type
- [Error handling](../../concepts/error-handling.md) - Handling SDK errors
