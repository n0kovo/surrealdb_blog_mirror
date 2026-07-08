---
position: 6
title: Live queries
description: The Java SDK supports real-time live queries that stream changes from the database to your application.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/concepts/live-queries.mdx"
---

# Live queries

The Java SDK supports real-time [live queries](../../query-language/statements/live-select.md) that stream changes from the database to your application. When records in a table are created, updated, or deleted, the SDK delivers notifications through a [`LiveStream`](../api/core/live-stream.md) that you can consume in a loop or process asynchronously.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/surreal#select-live">`db.selectLive(table)`</a></td>
			<td scope="row" data-label="Description">Starts a live query on a table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/live-stream#next">`stream.next()`</a></td>
			<td scope="row" data-label="Description">Returns the next notification</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/live-stream#close">`stream.close()`</a></td>
			<td scope="row" data-label="Description">Closes the live query</td>
		</tr>
	</tbody>
</table>

## Starting a live query

The [`.selectLive()`](../api/core/surreal.md#select-live) method subscribes to changes on a table and returns a [`LiveStream`](../api/core/live-stream.md). Live queries require a WebSocket connection (`ws://` or `wss://`) because the server pushes notifications over the persistent connection.

```java
try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    LiveStream stream = db.selectLive("users");
}
```

## Receiving notifications

Call [`.next()`](../api/core/live-stream.md#next) on the `LiveStream` to block until the next notification arrives. It returns an `Optional<LiveNotification>` — the optional is empty if the stream has been closed.

Each [`LiveNotification`](../api/core/live-stream.md#live-notification) provides:
- `.getAction()` — the type of change: `CREATE`, `UPDATE`, or `DELETE`
- `.getValue()` — the record data as a [`Value`](../api/values/value.md)
- `.getQueryId()` — the unique identifier of the live query

```java
LiveStream stream = db.selectLive("users");

while (true) {
    Optional<LiveNotification> notification = stream.next();
    if (notification.isEmpty()) break;

    LiveNotification n = notification.get();
    System.out.println(n.getAction() + ": " + n.getValue());
}
```

## Closing a live query

Call [`.close()`](../api/core/live-stream.md#close) to unsubscribe from the live query and release the server-side subscription. `LiveStream` implements `AutoCloseable`, so you can use try-with-resources to ensure the stream is closed automatically.

```java
try (LiveStream stream = db.selectLive("users")) {
    Optional<LiveNotification> notification = stream.next();
    notification.ifPresent(n ->
        System.out.println(n.getAction() + ": " + n.getValue())
    );
}
```

## Learn more

- [Surreal API reference](../api/core/surreal.md#select-live) for the selectLive method
- [LiveStream API reference](../api/core/live-stream.md) for stream and notification details
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for WebSocket connection setup
- [SurrealQL LIVE SELECT](../../query-language/statements/live-select.md) for the underlying query syntax
- [DEFINE TABLE ... CHANGEFEED](../../query-language/statements/define/table.md) for configuring changefeeds on tables
