---
position: 5
title: Live queries
description: The Go SDK supports real-time live queries that stream change notifications from the database through Go channels.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/concepts/live-queries.mdx"
---

# Live queries

Live queries allow your application to receive real-time notifications whenever records in a table are created, updated, or deleted. The Go SDK delivers notifications through Go channels, making it easy to integrate with goroutines and concurrent patterns.

Live queries require a WebSocket connection (`ws://` or `wss://`). They are available on [`*DB`](../api/core/db.md) and [`*Session`](../api/core/session.md) but not on [`*Transaction`](../api/core/transaction.md).

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Function</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#live">`surrealdb.Live(ctx, s, table, diff)`</a></td>
			<td scope="row" data-label="Description">Starts a live query on a table and returns its UUID</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#kill">`surrealdb.Kill(ctx, s, id)`</a></td>
			<td scope="row" data-label="Description">Stops a live query and closes its notification channel</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#livenotifications">`db.LiveNotifications(id)`</a></td>
			<td scope="row" data-label="Description">Returns the notification channel for a live query</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#closelivenotifications">`db.CloseLiveNotifications(id)`</a></td>
			<td scope="row" data-label="Description">Closes the notification channel without killing the server-side query</td>
		</tr>
	</tbody>
</table>

## Starting a live query

Use the [`Live`](../api/core/db.md#live) function to subscribe to changes on a table. It returns a [`UUID`](../api/values/uuid.md) that identifies the live query.

```go
liveID, err := surrealdb.Live(ctx, db, models.Table("persons"), false)
if err != nil {
	log.Fatal(err)
}
```

The `diff` parameter controls notification format. When `false`, notifications contain the full record. When `true`, they contain JSON Patch diffs instead.

## Receiving notifications

After starting a live query, call [`.LiveNotifications()`](../api/core/db.md#livenotifications) on the [`*DB`](../api/core/db.md) or [`*Session`](../api/core/session.md) to get a channel that receives [`Notification`](../api/types/index.md#notification) values.

```go
ch, err := db.LiveNotifications(liveID.String())
if err != nil {
	log.Fatal(err)
}

for notification := range ch {
	fmt.Printf("Action: %s, Result: %v\n", notification.Action, notification.Result)
}
```

Each notification includes:

| Field | Type | Description |
|---|---|---|
| `ID` | `*models.UUID` | The live query UUID |
| `Action` | `Action` | One of `CREATE`, `UPDATE`, or `DELETE` |
| `Result` | `interface{}` | The record data or JSON Patch diff |

## Processing notifications in a goroutine

A common pattern is to process live query notifications in a separate goroutine while the main goroutine continues other work.

```go
liveID, err := surrealdb.Live(ctx, db, models.Table("persons"), false)
if err != nil {
	log.Fatal(err)
}

ch, err := db.LiveNotifications(liveID.String())
if err != nil {
	log.Fatal(err)
}

go func() {
	for n := range ch {
		switch n.Action {
		case "CREATE":
			fmt.Println("New record:", n.Result)
		case "UPDATE":
			fmt.Println("Updated record:", n.Result)
		case "DELETE":
			fmt.Println("Deleted record:", n.Result)
		}
	}
}()
```

## Stopping a live query

Use the [`Kill`](../api/core/db.md#kill) function to terminate a live query on the server and close its notification channel.

```go
if err := surrealdb.Kill(ctx, db, liveID.String()); err != nil {
	log.Fatal(err)
}
```

[`Kill`](../api/core/db.md#kill) both sends the kill RPC to the server and closes the local notification channel. If you only want to close the channel without killing the server-side query, use [`.CloseLiveNotifications()`](../api/core/db.md#closelivenotifications) instead.

## Learn more

- [DB API reference](../api/core/db.md) for complete function signatures and parameters
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for WebSocket connection requirements
- [Multiple sessions](multiple-sessions.md) for session-scoped live queries
- [Reliable connections](reliable-connections.md) for live queries that persist across reconnections
- [SurrealQL LIVE statement](../../../reference/query-language/statements/live-select.md) for the underlying query language syntax
