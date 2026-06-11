---
position: 15
title: live
description: The live() method for the SurrealDB Swift SDK subscribes to changes via a live query.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/swift/methods/live.mdx"
---

# `live()` {#live}

Subscribes to changes on a table and returns an `AsyncStream<LiveEvent<T>>` of events.

> [!IMPORTANT]
> Live queries require the [WebSocket client](../concepts/connecting.md#websocket-client).

```swift title="Method Syntax"
try await client.live(query)
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
                `query`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                A live query built with `SurrealDSL.live(_:)` or the `#live` macro.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

```swift
let stream = try await client.live(SurrealDSL.live(Person.self))

for await event in stream {
    switch event.action {
    case .create:
        print("Created:", event.decoded as Any)
    case .update:
        print("Updated:", event.decoded as Any)
    case .delete:
        print("Deleted record:", event.recordID)
    case .killed:
        print("Live query was killed")
    }
}
```

See [Live queries](../concepts/live-queries.md) for a full walkthrough, and [`kill`](kill.md) to stop a subscription.
