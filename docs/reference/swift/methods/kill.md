---
position: 16
title: kill
description: The kill() method for the SurrealDB Swift SDK stops a running live query.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/swift/methods/kill.mdx"
---

# `kill()` {#kill}

Kills a running [live query](live.md) by its id, ending the associated `AsyncStream`.

```swift title="Method Syntax"
try await client.kill(liveQueryID: id)
```

### Arguments

<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `liveQueryID`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The id of the live query to kill, available as `event.queryID` on received events.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
try await client.kill(liveQueryID: event.queryID)
```
