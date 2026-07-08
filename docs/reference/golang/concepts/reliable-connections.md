---
position: 10
title: Reliable connections
description: The Go SDK provides a contrib package for auto-reconnecting WebSocket connections with session restoration and live query persistence.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/golang/concepts/reliable-connections.mdx"
---

# Reliable connections

> [!WARNING]
> This feature is provided by the `contrib/rews` package, which is outside of the backward compatibility guarantees of the core SDK. Its API may change without following semantic versioning.

The `rews` (reliable WebSocket) package wraps a standard WebSocket connection and adds automatic reconnection when the connection is lost. On reconnect, it restores the previous session state including namespace, database, authentication, variables, and live queries.

This is useful for long-running applications that need to survive transient network failures without manual reconnection logic.

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
			<td scope="row" data-label="Function">`rews.New(newConn, interval, unmarshaler, logger)`</td>
			<td scope="row" data-label="Description">Creates a new auto-reconnecting WebSocket connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">`rews.NewExponentialBackoffRetryer()`</td>
			<td scope="row" data-label="Description">Creates a retryer with exponential backoff and jitter</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">`rews.NewFixedDelayRetryer(delay, maxRetries)`</td>
			<td scope="row" data-label="Description">Creates a retryer with a fixed delay between attempts</td>
		</tr>
	</tbody>
</table>

## Setting up a reliable connection

Create a `rews.Connection` by providing a factory function that constructs the underlying WebSocket connection, a check interval for detecting disconnections, a CBOR unmarshaler, and an optional logger.

```go
	"context"
	"net/url"
	"time"

	surrealdb "github.com/surrealdb/surrealdb.go"
	"github.com/surrealdb/surrealdb.go/contrib/rews"
	"github.com/surrealdb/surrealdb.go/pkg/connection"
	"github.com/surrealdb/surrealdb.go/pkg/connection/gorillaws"
	"github.com/surrealdb/surrealdb.go/surrealcbor"
)

endpoint, _ := url.Parse("ws://localhost:8000/rpc")
codec := surrealcbor.New()

conn := rews.New(
	func(ctx context.Context) (*gorillaws.WebSocket, error) {
		conf := connection.NewConfig(endpoint)
		conf.Marshaler = codec
		conf.Unmarshaler = codec
		return gorillaws.New(conf), nil
	},
	5*time.Second,
	codec,
	nil,
)
```

Then pass the connection to [`FromConnection`](../api/core/db.md#fromconnection) to create a [`*DB`](../api/core/db.md):

```go
db, err := surrealdb.FromConnection(ctx, conn)
if err != nil {
	log.Fatal(err)
}
defer db.Close(ctx)
```

## Configuring retry behavior

By default, connection attempts are not retried. Set the `Retryer` field to enable automatic retries on connection failure.

The `ExponentialBackoffRetryer` increases the delay between retries exponentially, with optional jitter to avoid thundering herd problems:

```go
retryer := rews.NewExponentialBackoffRetryer()
retryer.MaxRetries = 10
retryer.InitialDelay = 1 * time.Second
retryer.MaxDelay = 30 * time.Second
conn.Retryer = retryer
```

| Field | Default | Description |
|---|---|---|
| `InitialDelay` | 1s | Delay before the first retry |
| `MaxDelay` | 30s | Maximum delay between retries |
| `Multiplier` | 2.0 | Exponential backoff multiplier |
| `MaxRetries` | 0 (infinite) | Maximum retry attempts, 0 for unlimited |
| `Jitter` | `true` | Add randomness to avoid synchronised retries |
| `JitterFactor` | 0.3 | Maximum jitter as a fraction of the delay |

For simpler cases, `FixedDelayRetryer` uses a constant delay:

```go
conn.Retryer = rews.NewFixedDelayRetryer(2*time.Second, 5)
```

You can also implement the `Retryer` interface for custom strategies:

```go
type Retryer interface {
	NextDelay(attempt int, lastErr error) (time.Duration, bool)
	Reset()
}
```

## What gets restored on reconnect

When the connection is lost and re-established, `rews` automatically restores:

1. **Namespace and database** -- the last values passed to [`.Use()`](../api/core/db.md#use)
2. **Authentication** -- the last token from [`.SignIn()`](../api/core/db.md#signin), [`.SignUp()`](../api/core/db.md#signup), or [`.Authenticate()`](../api/core/db.md#authenticate)
3. **Connection variables** -- all variables set with [`.Let()`](../api/core/db.md#let) (and removed with [`.Unset()`](../api/core/db.md#unset))
4. **[Live queries](live-queries.md)** -- all active live queries are re-subscribed, and notification routing is restored

> [!NOTE]
> If the authentication token has expired by the time reconnection occurs, re-authentication will fail. The application is responsible for handling token expiry, for example by using [refresh tokens](authentication.md#using-refresh-tokens).

## Connection states

The `rews.Connection` tracks its state through a state machine:

| State | Description |
|---|---|
| `Disconnected` | Not connected, initial state |
| `Connecting` | Connection attempt in progress |
| `Connected` | Connection established and active |
| `Closing` | Close requested, shutting down |
| `Closed` | Fully closed, cannot be reused |

## Learn more

- [Connecting to SurrealDB](connecting-to-surrealdb.md) for standard connection setup
- [Live queries](live-queries.md) for live query setup that persists across reconnections
- [DB API reference](../api/core/db.md) for `FromConnection` usage
