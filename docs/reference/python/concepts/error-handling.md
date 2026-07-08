---
position: 8
title: Error handling
description: The Python SDK provides a structured error hierarchy for handling server and client-side failures.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/python/concepts/error-handling.mdx"
---

# Error handling

All errors raised by the Python SDK extend [`SurrealError`](../api/errors/index.md#surrealerror), so you can catch every SDK error with a single `except` clause. Server-originated errors use the [`ServerError`](../api/errors/index.md#servererror) subtree with structured kinds, details, and cause chains. SDK-side errors cover connection, parsing, and feature support failures.

See the [Errors reference](../api/errors/index.md) for the complete error hierarchy and all available properties.

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
			<td scope="row" data-label="Error class"><a href="/docs/reference/python/api/errors/#surrealerror">`SurrealError`</a></td>
			<td scope="row" data-label="Description">Base class for all SDK errors</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/python/api/errors/#servererror">`ServerError`</a></td>
			<td scope="row" data-label="Description">Structured server error with kind, details, and cause</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/python/api/errors/#notallowederror">`NotAllowedError`</a></td>
			<td scope="row" data-label="Description">Thrown when permission is denied</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/python/api/errors/#notfounderror">`NotFoundError`</a></td>
			<td scope="row" data-label="Description">Thrown when a resource is not found</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/python/api/errors/#connectionunavailableerror">`ConnectionUnavailableError`</a></td>
			<td scope="row" data-label="Description">Thrown when no connection is active</td>
		</tr>
		<tr>
			<td scope="row" data-label="Error class"><a href="/docs/reference/python/api/errors/#unsupportedfeatureerror">`UnsupportedFeatureError`</a></td>
			<td scope="row" data-label="Description">Thrown for features not supported by the connection type</td>
		</tr>
	</tbody>
</table>

## Catching all SDK errors

The simplest way to handle errors is to catch `SurrealError`, which is the base class for every exception the SDK raises.

```python
from surrealdb import Surreal, SurrealError

with Surreal("ws://localhost:8000") as db:
    db.use("my_ns", "my_db")
    db.signin({"username": "root", "password": "root"})

    try:
        result = db.query("SELECT * FROM users")
    except SurrealError as e:
        print("SDK error:", e)
```

This pattern is useful at the top level of your application where you want to ensure no SDK error goes unhandled.

## Handling server errors

Server errors carry structured information beyond the error message. A `ServerError` has a `.kind` string, an optional `.details` dictionary, and an optional `.server_cause` linking to the underlying error in the chain.

You can check whether an error is a `ServerError` and then inspect its kind using the constants defined on [`ErrorKind`](../api/errors/index.md#errorkind).

```python
from surrealdb import ServerError, ErrorKind

try:
    result = db.query("INVALID QUERY")
except ServerError as e:
    print("Kind:", e.kind)
    print("Details:", e.details)

    if e.kind == ErrorKind.VALIDATION:
        print("The query has a validation issue")
    elif e.kind == ErrorKind.NOT_ALLOWED:
        print("Permission denied")
```

The `ErrorKind` constants include `VALIDATION`, `CONFIGURATION`, `THROWN`, `QUERY`, `SERIALIZATION`, `NOT_ALLOWED`, `NOT_FOUND`, `ALREADY_EXISTS`, `CONNECTION`, and `INTERNAL`.

## Inspecting the error cause chain

Server errors can form a chain where one error caused another. The `.has_kind()` method checks whether this error or any error in its cause chain matches a given kind. The `.find_cause()` method returns the first matching error in the chain.

```python
from surrealdb import ServerError, ErrorKind

try:
    db.signin({"username": "user", "password": "wrong"})
except ServerError as e:
    if e.has_kind(ErrorKind.NOT_ALLOWED):
        print("Authentication failure somewhere in the chain")

    auth_cause = e.find_cause(ErrorKind.NOT_ALLOWED)
    if auth_cause:
        print("Root auth error:", auth_cause)
        print("Details:", auth_cause.details)
```

These methods are especially useful when a high-level error wraps a more specific cause, such as a query error that was ultimately caused by a permission denial.

## Catching specific error types

For fine-grained control, catch the specific error subclass you need. The SDK maps server error kinds to dedicated Python classes such as `ValidationError`, [`NotAllowedError`](../api/errors/index.md#notallowederror), and [`NotFoundError`](../api/errors/index.md#notfounderror).

```python
from surrealdb import NotAllowedError

try:
    db.signin({
        "namespace": "surrealdb",
        "database": "docs",
        "access": "account",
        "variables": {
            "email": "user@example.com",
            "password": "wrong_password",
        },
    })
except NotAllowedError as e:
    if e.is_invalid_auth:
        print("Invalid credentials")
    elif e.is_token_expired:
        print("Token expired, please re-authenticate")
```

You can also catch `NotFoundError` to handle missing resources.

```python
from surrealdb import NotFoundError, RecordID

try:
    user = db.select(RecordID("users", "nonexistent"))
except NotFoundError as e:
    if e.table_name:
        print(f"Table not found: {e.table_name}")
    elif e.record_id:
        print(f"Record not found: {e.record_id}")
```

## Handling SDK-side errors

Some errors originate from the SDK itself rather than the server. These cover situations like missing connections and unsupported features.

A [`ConnectionUnavailableError`](../api/errors/index.md#connectionunavailableerror) is raised when you try to perform an operation before establishing a connection.

```python
from surrealdb import Surreal, ConnectionUnavailableError

db = Surreal("ws://localhost:8000")

try:
    db.select("users")
except ConnectionUnavailableError:
    print("Not connected — call db.connect() first")
```

An [`UnsupportedFeatureError`](../api/errors/index.md#unsupportedfeatureerror) is raised when you attempt to use a feature that requires a specific connection type. For example, sessions and transactions require a WebSocket connection.

```python
from surrealdb import Surreal, UnsupportedFeatureError

with Surreal("http://localhost:8000") as db:
    db.use("my_ns", "my_db")
    db.signin({"username": "root", "password": "root"})

    try:
        session = db.new_session()
    except UnsupportedFeatureError:
        print("Sessions require a WebSocket connection")
```

An [`UnsupportedEngineError`](../api/errors/index.md#unsupportedengineerror) is raised when the URL scheme is not recognized.

```python
from surrealdb import Surreal, UnsupportedEngineError

try:
    db = Surreal("ftp://localhost:8000")
except UnsupportedEngineError as e:
    print(f"Unsupported protocol: {e.url}")
```

## Learn more

- [Errors reference](../api/errors/index.md) for complete error hierarchy
- [ErrorKind constants](../api/errors/index.md#errorkind) for error kind matching
- [Authentication](authentication.md) for auth-related error patterns
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for connection error patterns
