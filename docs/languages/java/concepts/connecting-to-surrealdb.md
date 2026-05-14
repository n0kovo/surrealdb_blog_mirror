---
position: 1
title: Connecting to SurrealDB
description: The Java SDK supports WebSocket, HTTP, and embedded connections to SurrealDB instances.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/concepts/connecting-to-surrealdb.mdx"
---

# Connecting to SurrealDB

The first step towards interacting with [SurrealDB](https://surrealdb.com/docs/start) is to create a new connection to a database instance. This involves initializing a new [`Surreal`](../api/core/surreal.md) instance, connecting it to an endpoint, and selecting a namespace and database. The SDK supports remote connections over WebSocket and HTTP, as well as embedded in-process databases.

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
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#constructor">`new Surreal()`</a></td>
			<td scope="row" data-label="Description">Creates a new Surreal instance</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#connect">`db.connect(url)`</a></td>
			<td scope="row" data-label="Description">Connects to a SurrealDB instance</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#close">`db.close()`</a></td>
			<td scope="row" data-label="Description">Closes the active connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#use-ns">`db.useNs(namespace)`</a></td>
			<td scope="row" data-label="Description">Switches to a specific namespace</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#use-db">`db.useDb(database)`</a></td>
			<td scope="row" data-label="Description">Switches to a specific database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#use-defaults">`db.useDefaults()`</a></td>
			<td scope="row" data-label="Description">Uses the default namespace and database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#version">`db.version()`</a></td>
			<td scope="row" data-label="Description">Returns the server version</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#health">`db.health()`</a></td>
			<td scope="row" data-label="Description">Checks the server health</td>
		</tr>
	</tbody>
</table>

## Opening a connection

Create a new [`Surreal`](../api/core/surreal.md) instance and call [`.connect()`](../api/core/surreal.md#connect) with a connection string pointing to your SurrealDB instance. The `Surreal` class implements `AutoCloseable`, so you can use it in a try-with-resources block to ensure the connection is closed automatically.

```java
Surreal db = new Surreal();
db.connect("ws://localhost:8000");
```

## Connection string protocols

The connection string determines the protocol and transport used to communicate with SurrealDB. For more on server configuration, see the [start command](../../../reference/cli/surrealdb-cli/commands/start.md) documentation.

| Protocol | Description |
|---|---|
| `ws://` | Plain WebSocket connection |
| `wss://` | Secure WebSocket connection (TLS) |
| `http://` | Plain HTTP connection |
| `https://` | Secure HTTP connection (TLS) |
| `memory://` | In-memory embedded database |
| `surrealkv://` | Disk-based embedded database |

The `memory://` and `surrealkv://` protocols run SurrealDB in-process using JNI, which eliminates network overhead. See [Embedded databases](embedded-databases.md) for details on configuring embedded connections.

## Feature support by protocol

Not all features are available on every protocol. The table below summarizes what is supported for each connection type.

| Feature | WebSocket | HTTP | Embedded |
|---|---|---|---|
| Authentication | Yes | Yes | Yes |
| Queries | Yes | Yes | Yes |
| CRUD operations | Yes | Yes | Yes |
| Live queries | Yes | No | No |
| Transactions | Yes | No | Yes |
| Multiple sessions | Yes | No | Yes |
| Export / Import | Yes | Yes | Yes |

## Selecting a namespace and database

After connecting, select a [namespace](../../../reference/query-language/statements/define/namespace.md) and [database](../../../reference/query-language/statements/define/database.md) using [`.useNs()`](../api/core/surreal.md#use-ns) and [`.useDb()`](../api/core/surreal.md#use-db). These methods return the `Surreal` instance, so they can be chained.

```java
db.useNs("surrealdb").useDb("docs");
```

To reset the namespace and database to the server defaults, call [`.useDefaults()`](../api/core/surreal.md#use-defaults).

```java
db.useDefaults();
```

## Using try-with-resources

Since [`Surreal`](../api/core/surreal.md) implements `AutoCloseable`, Java's try-with-resources statement ensures that [`.close()`](../api/core/surreal.md#close) is called when the block exits, even if an exception is thrown. This is the recommended pattern for managing connections.

```java

public class Example {

    public static void main(String[] args) {
        try (Surreal db = new Surreal()) {
            db.connect("ws://localhost:8000");
            db.useNs("surrealdb").useDb("docs");
            db.signin(new RootCredential("root", "root"));

            String version = db.version();
            System.out.println("Connected to SurrealDB " + version);
        }
    }

}
```

## Effect of connection protocol on token and session duration

The connection protocol affects how authentication tokens and sessions behave.

- **WebSocket** connections are stateful and long-lived. After the initial authentication, the session persists for the lifetime of the connection. The session duration defaults to `NONE`, meaning it never expires unless explicitly configured.
- **HTTP** connections are stateless. Each request must include a valid token, and the server creates a short-lived session for the duration of that request. The token duration defaults to 1 hour.

You can configure token and session durations using the `DURATION` clause on [`DEFINE ACCESS`](../../../reference/query-language/statements/define/access/index.md) or [`DEFINE USER`](../../../reference/query-language/statements/define/user.md) statements. See the [security best practices](../../../learn/security/best-practices/security-best-practices.md#expiration) documentation for guidance on choosing appropriate durations.

## Closing a connection

The [`.close()`](../api/core/surreal.md#close) method releases all resources associated with the connection. If you are not using try-with-resources, call `.close()` explicitly when you are done with the connection.

```java
db.close();
```

## Learn more

- [Surreal API reference](../api/core/surreal.md) for complete method signatures
- [Authentication](authentication.md) for signing in and managing sessions
- [Embedded databases](embedded-databases.md) for running SurrealDB in-process
- [Error handling](error-handling.md) for handling connection errors
- [SurrealDB authentication](../../../learn/security/authentication/authentication.md) for an overview of authentication concepts
- [DEFINE NAMESPACE](../../../reference/query-language/statements/define/namespace.md) and [DEFINE DATABASE](../../../reference/query-language/statements/define/database.md) for namespace and database configuration
