---
position: 1
title: Connecting to SurrealDB
description: The Go SDK supports connecting to SurrealDB over WebSocket or HTTP using a URL-based connection factory.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/concepts/connecting-to-surrealdb.mdx"
---

# Connecting to SurrealDB

The Go SDK supports connecting to SurrealDB over WebSocket or HTTP. The `FromEndpointURLString` factory function inspects the URL scheme and creates the appropriate connection automatically.

This page covers how to create, configure, and manage connections to a SurrealDB instance.

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
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#fromendpointurlstring">`surrealdb.FromEndpointURLString(ctx, url)`</a></td>
			<td scope="row" data-label="Description">Creates a connection from a URL string</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#fromconnection">`surrealdb.FromConnection(ctx, conn)`</a></td>
			<td scope="row" data-label="Description">Creates a client from a custom connection implementation</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#close">`db.Close(ctx)`</a></td>
			<td scope="row" data-label="Description">Closes the connection and releases resources</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#use">`db.Use(ctx, ns, db)`</a></td>
			<td scope="row" data-label="Description">Selects a namespace and database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/golang/api/core/db#version">`db.Version(ctx)`</a></td>
			<td scope="row" data-label="Description">Returns the version of the connected SurrealDB instance</td>
		</tr>
	</tbody>
</table>

## Opening a connection

Use `FromEndpointURLString` to create a new client and connect to a SurrealDB instance. The function accepts a `context.Context` for cancellation and a URL string that determines the connection type.

```go
ctx := context.Background()

db, err := surrealdb.FromEndpointURLString(ctx, "ws://localhost:8000")
if err != nil {
	log.Fatal(err)
}
defer db.Close(ctx)
```

The context controls how long the connection attempt blocks. You can use `context.WithTimeout` to limit the connection time on unreliable networks:

```go
ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
defer cancel()

db, err := surrealdb.FromEndpointURLString(ctx, "ws://localhost:8000")
```

## Connection string protocols

The URL scheme determines the connection type and its capabilities.

| Scheme | Connection type | Description |
|---|---|---|
| `ws://` | WebSocket | Unencrypted stateful connection |
| `wss://` | WebSocket | TLS-encrypted stateful connection |
| `http://` | HTTP | Unencrypted stateless connection |
| `https://` | HTTP | TLS-encrypted stateless connection |
| `mem://` | Memory | In-memory [embedded instance](../embedding.md) |

WebSocket connections are long-lived and stateful. They support all SDK features including [live queries](live-queries.md), [sessions](multiple-sessions.md), and [transactions](transactions.md).

HTTP connections are stateless. Each request is independent and requires its own authentication token. [Live queries](live-queries.md), [sessions](multiple-sessions.md), and [transactions](transactions.md) are not available over HTTP.

## Using a custom connection

If you need to configure the underlying connection (for example, custom TLS settings or a specific WebSocket implementation), you can create a connection manually and pass it to [`FromConnection`](../api/core/db.md#fromconnection):

```go
	"net/url"

	"github.com/surrealdb/surrealdb.go/pkg/connection"
	"github.com/surrealdb/surrealdb.go/pkg/connection/gorillaws"
)

endpoint, _ := url.Parse("ws://localhost:8000/rpc")
conf := connection.NewConfig(endpoint)
conn := gorillaws.New(conf)

db, err := surrealdb.FromConnection(ctx, conn)
```

[`FromConnection`](../api/core/db.md#fromconnection) calls `.Connect(ctx)` on the connection for you, so you do not need to call it separately. For auto-reconnecting connections, see [Reliable connections](reliable-connections.md).

## Selecting a namespace and database

After connecting, use `.Use()` to select the namespace and database you want to work with. Most operations require a namespace and database to be selected first.

```go
if err := db.Use(ctx, "my_namespace", "my_database"); err != nil {
	log.Fatal(err)
}
```

You can call `.Use()` multiple times to switch between namespaces and databases on the same connection.

## Effect of connection protocol on token and session duration

WebSocket connections (`ws://`, `wss://`) are long-lived and stateful. After authentication, the session persists for the lifetime of the connection. The session duration defaults to `NONE`, meaning it never expires unless configured otherwise.

HTTP connections (`http://`, `https://`) are stateless. Each request requires its own authentication token. The token duration defaults to 1 hour.

You can configure token and session durations using the `DURATION` clause in [`DEFINE ACCESS METHOD`](../../../reference/query-language/statements/define/access/index.md) or [`DEFINE USER`](../../../reference/query-language/statements/define/user.md) statements.

> [!NOTE]
> Learn more about token and session duration in the [security best practices](../../../learn/security/best-practices/security-best-practices.md#expiration) documentation.

## Closing a connection

Call `.Close()` to release the underlying connection resources when you are done.

```go
db.Close(ctx)
```

Use `defer db.Close(ctx)` immediately after creating the connection to ensure cleanup happens even when errors occur.

## Learn more

- [DB API reference](../api/core/db.md) for complete method signatures and parameters
- [Authentication](authentication.md) for signing in and managing user sessions
- [Error handling](error-handling.md) for handling connection and authentication errors
