---
position: 3
title: Error handling
description: The JavaScript SDK provides specific error classes for handling different types of failures when interacting with SurrealDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/concepts/error-handling.mdx"
---

# Error handling

The JavaScript SDK defines specific error classes for different failure scenarios. All SDK errors extend the base `SurrealError` class, making it easy to distinguish SDK errors from other JavaScript errors and to handle specific failure types with `instanceof` checks.

The error kinds, wire codes and structured shape behind these are documented once in [Errors](../../rest-api/errors.md), which applies to every SDK and protocol.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Error class</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/javascript/api/errors#surrealerror"> ` SurrealError `</a></td>
			<td scope="row" data-label="Description">Base class for all SDK errors</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/javascript/api/errors#connectionunavailableerror"> ` ConnectionUnavailableError `</a></td>
			<td scope="row" data-label="Description">Thrown when operating without an active connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/javascript/api/errors#authenticationerror"> ` AuthenticationError `</a></td>
			<td scope="row" data-label="Description">Thrown when authentication fails</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/javascript/api/errors#responseerror"> ` ResponseError `</a></td>
			<td scope="row" data-label="Description">Thrown when a database query returns an error</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/javascript/api/errors#unsupportedversionerror"> ` UnsupportedVersionError `</a></td>
			<td scope="row" data-label="Description">Thrown when the SurrealDB version is incompatible</td>
		</tr>
	</tbody>
</table>

A complete list of error classes is available in the [Errors API reference](../api/errors/index.md).

## Where an error surfaces

A query travels through two layers, and it is worth knowing which one a failure comes from.

The first is the request itself: a connection that is unavailable, a rejected sign-in, a query that will not parse. The second is the individual statements inside the query, which can fail while the request as a whole succeeds.

Awaiting a query collapses both into a rejection. It rejects on the first statement that fails, so a query whose earlier statements succeeded resolves to nothing at all: those results are lost along with the error.

Where the per-statement outcome matters, `.responses()` returns every statement instead of rejecting. Each entry carries a `success` flag, and a failing one carries an `error` with its `kind`.

```ts

const db = new Surreal({ engines: { ...createRemoteEngines() } });
await db.connect('http://localhost:8000');
await db.signin({ username: 'root', password: 'secret' });
await db.use({ namespace: 'test', database: 'test' });

// Awaiting the query rejects on the first statement that fails, so the
// result of the statement that succeeded is not returned.
try {
    await db.query("RETURN 1; THROW 'second'");
} catch (e) {
    if (e instanceof ThrownError) {
        console.log(`${e.kind}: ${e.message}`);
    }
}

// .responses() reports every statement instead of rejecting.
const responses = await db.query("RETURN 1; THROW 'second'").responses();
for (const [index, statement] of responses.entries()) {
    console.log(index, statement.success, statement.success ? statement.result : statement.error.kind);
}
```

```ts title="Output"
Thrown: An error occurred: second
0 true 1
1 false Thrown
```

## Error kinds

Every server error carries a `kind`, and the SDK throws a dedicated class for each of the kinds below. The meaning of each kind is described in [Errors](../../rest-api/errors.md#error-kinds). Match on the kind or the class rather than on the message text, which is free to change between releases.

| Kind | Error class |
| --- | --- |
| `Validation` | `ValidationError` |
| `Configuration` | `ConfigurationError` |
| `Query` | `QueryError` |
| `Serialization` | `SerializationError` |
| `NotAllowed` | `NotAllowedError` |
| `NotFound` | `NotFoundError` |
| `AlreadyExists` | `AlreadyExistsError` |
| `Thrown` | `ThrownError` |
| `Internal` | `InternalError` |

Any kind without a dedicated class, including one added by a newer server, arrives as the base `ServerError` with its `kind` intact. Catching `ServerError` therefore stays correct as the server grows new kinds.

## Catching SDK errors

All errors thrown by the SDK are instances of `SurrealError`. You can use `instanceof` checks to catch SDK errors broadly, or target specific error classes for fine-grained handling.

```ts

try {
    await db.signin({ username: 'user', password: 'pass' });
} catch (error) {
    if (error instanceof AuthenticationError) {
        console.error('Invalid credentials');
    } else if (error instanceof ConnectionUnavailableError) {
        console.error('Not connected to a database');
    } else if (error instanceof SurrealError) {
        console.error('SDK error:', error.message);
    }
}
```

## Handling connection errors

Connection errors occur when the SDK cannot establish or maintain a connection to the database. The most common are `ConnectionUnavailableError` (thrown when you attempt an operation without a connection) and `HttpConnectionError` (thrown when an HTTP request fails).

```ts

try {
    await db.connect('ws://localhost:8000');
} catch (error) {
    if (error instanceof HttpConnectionError) {
        console.error(`HTTP ${error.status}: ${error.statusText}`);
    }
}
```

If you attempt to use an engine protocol that has not been registered, the SDK throws an `UnsupportedEngineError` with the name of the unsupported engine.

```ts

try {
    await db.connect('mem://');
} catch (error) {
    if (error instanceof UnsupportedEngineError) {
        console.error(`Engine "${error.engine}" is not registered`);
    }
}
```

## Handling authentication errors

An `AuthenticationError` is thrown when a sign-in or sign-up attempt fails. A `MissingNamespaceDatabaseError` is thrown when you attempt an operation that requires a namespace and database without having selected one.

```ts

try {
    await db.use({ namespace: 'main', database: 'main' });
    await db.signin({ username: 'admin', password: 'secret' });
} catch (error) {
    if (error instanceof MissingNamespaceDatabaseError) {
        console.error('No namespace or database selected');
    } else if (error instanceof AuthenticationError) {
        console.error('Authentication failed:', error.cause);
    }
}
```

## Handling query errors

When a SurrealQL query fails, the SDK throws a `ResponseError` containing the error code and message from the database.

```ts

try {
    await db.query('INVALID QUERY');
} catch (error) {
    if (error instanceof ResponseError) {
        console.error(`Database error [${error.code}]: ${error.message}`);
    }
}
```

## Handling version mismatches

The SDK performs a version check when connecting to a SurrealDB instance by default. If the connected version is outside the supported range, an `UnsupportedVersionError` is thrown. You can disable this check using the `versionCheck` option on [`.connect()`](connecting-to-surrealdb.md#connection-options).

```ts

try {
    await db.connect('ws://localhost:8000');
} catch (error) {
    if (error instanceof UnsupportedVersionError) {
        console.error(
            `Version ${error.version} is not supported. ` +
            `Requires >= ${error.minimum} and < ${error.maximum}`
        );
    }
}
```

## Handling feature availability

Some features are only available with specific engines or SurrealDB versions. An `UnsupportedFeatureError` is thrown when a feature is not supported by the configured engine, while an `UnavailableFeatureError` is thrown when the connected SurrealDB version does not support it.

You can proactively check for feature support using the [`isFeatureSupported()`](connecting-to-surrealdb.md#testing-for-features) method to avoid these errors entirely.

```ts

if (db.isFeatureSupported(Features.LiveQueries)) {
    const live = await db.live(new Table('users'));
}
```

## Listening to connection errors

The SDK emits an `error` event for errors that occur outside of direct method calls, such as reconnection failures. You can subscribe to these events using the [`.subscribe()`](../api/core/surreal.md#subscribe) method.

```ts

db.subscribe('error', (error) => {
    if (error instanceof ReconnectExhaustionError) {
        console.error('All reconnection attempts failed');
    } else if (error instanceof UnexpectedConnectionError) {
        console.error('Connection error:', error.cause);
    }
});
```

## Recovering from errors

For operations that may fail transiently, you can implement retry logic. Combine specific error checks with a retry loop to handle recoverable failures gracefully.

```ts

async function withRetry<T>(fn: () => Promise<T>, maxRetries = 3): Promise<T> {
    for (let attempt = 0; attempt < maxRetries; attempt++) {
        try {
            return await fn();
        } catch (error) {
            if (error instanceof ConnectionUnavailableError) {
                await db.connect('ws://localhost:8000');
                continue;
            }
            if (error instanceof ResponseError && attempt < maxRetries - 1) {
                continue;
            }
            throw error;
        }
    }
    throw new Error('Max retries exceeded');
}

const users = await withRetry(() => db.select(new Table('users')));
```

For the specific case of write conflicts under concurrent load, prefer the SDK's built-in [`.retry()`](../api/queries/query.md#retry) over a hand-rolled loop - it applies exponential backoff and only replays work known to be safely retryable.

```ts
const [n] = await db
    .query<[number]>('UPDATE counter:c SET n += 1 RETURN n')
    .retry({ attempts: 3 })
    .collect();
```

## Learn more

- [Errors API reference](../api/errors/index.md) for a complete list of error classes and their properties
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for connection and reconnection configuration
- [Retrying on write conflict](connecting-to-surrealdb.md#retrying-on-write-conflict) for configuring built-in query retry
- [Authentication](authentication.md) for handling authentication flows
