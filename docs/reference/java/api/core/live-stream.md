---
position: 4
title: LiveStream
description: The LiveStream class provides a blocking interface for receiving real-time notifications from live queries.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/api/core/live-stream.mdx"
---

# `LiveStream` {#live-stream}

The `LiveStream` class provides a blocking interface for receiving real-time notifications from live queries. It implements `AutoCloseable`, so it can be used in a try-with-resources block. Live streams are created by calling [`.selectLive()`](surreal.md#select-live) on a `Surreal` instance.

> [!NOTE]
> Live queries require a WebSocket connection (`ws://` or `wss://`).

**Source:** [surrealdb.java](https://github.com/surrealdb/surrealdb.java)

---

## Methods

### `.next()` {#next}

Blocks until the next live query notification is available and returns it. Returns an empty `Optional` if the stream has been closed.

```java title="Method Syntax"
stream.next()
```

**Returns:** `Optional<LiveNotification>`

```java title="Example"
LiveStream stream = db.selectLive("person");
Optional<LiveNotification> notification = stream.next();
```

### `.close()` {#close}

Closes the live query subscription and releases associated resources. This is called automatically when using try-with-resources.

```java title="Method Syntax"
stream.close()
```

**Returns:** `void`

```java title="Example"
stream.close();
```

---

# `LiveNotification` {#live-notification}

The `LiveNotification` class represents a single real-time notification received from a live query. Each notification contains the action that triggered it, the affected record value, and the live query identifier.

---

## Methods

### `.getAction()` {#get-action}

Returns the type of action that triggered the notification.

```java title="Method Syntax"
notification.getAction()
```

**Returns:** `String` — one of `"CREATE"`, `"UPDATE"`, or `"DELETE"`

```java title="Example"
String action = notification.getAction();
```

### `.getValue()` {#get-value}

Returns the record value associated with the notification. For `CREATE` and `UPDATE` actions, this is the full record. For `DELETE` actions, this may be `null`.

```java title="Method Syntax"
notification.getValue()
```

**Returns:** `Value` (may be `null` for `DELETE` actions)

```java title="Example"
Value record = notification.getValue();
```

### `.getQueryId()` {#get-query-id}

Returns the UUID of the live query that produced this notification.

```java title="Method Syntax"
notification.getQueryId()
```

**Returns:** `String`

```java title="Example"
String queryId = notification.getQueryId();
```

---

## Complete example

```java title="Listening for live changes"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    try (LiveStream stream = db.selectLive("person")) {
        while (true) {
            Optional<LiveNotification> notification = stream.next();
            if (notification.isEmpty()) break;

            LiveNotification n = notification.get();
            System.out.println(n.getAction() + ": " + n.getValue());
        }
    }
}
```

---

## See also

- [Surreal](surreal.md) — Connection and method reference
- [Live queries](../../concepts/live-queries.md) — Live query concepts and patterns
- [SurrealQL LIVE SELECT](../../../query-language/statements/live-select.md) — Live query syntax
