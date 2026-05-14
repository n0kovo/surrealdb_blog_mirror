---
position: 2
title: Authentication
description: The Python SDK supports multiple levels of authentication for signing in and managing user credentials.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/concepts/authentication.mdx"
---

# Authentication

The Python SDK supports signing in as a root, namespace, database, or record-level user. After signing in, the connection is authenticated for all subsequent operations until the session is invalidated or the connection is closed.

This page covers how to sign in, sign up, manage tokens, and inspect the current user.

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
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#signin">`db.signin(vars)`</a></td>
			<td scope="row" data-label="Description">Signs in as a root, namespace, database, or record user</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#signup">`db.signup(vars)`</a></td>
			<td scope="row" data-label="Description">Signs up a new record user via an access method</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#authenticate">`db.authenticate(token)`</a></td>
			<td scope="row" data-label="Description">Authenticates the connection with an existing JWT token</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#invalidate">`db.invalidate()`</a></td>
			<td scope="row" data-label="Description">Invalidates the current authentication session</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/python/api/core/surreal#info">`db.info()`</a></td>
			<td scope="row" data-label="Description">Returns the record data for the currently authenticated record user</td>
		</tr>
	</tbody>
</table>

## Signing in users

The `.signin()` method authenticates the connection. The fields you pass determine the authentication level. The method returns [Tokens](../api/types/index.md#tokens) on success, which contain the JWT access token and optional refresh token.

Refer to the [API reference](../api/core/surreal.md#signin) for the full list of parameters at each level.

	
**Root user**

A root user has full access to the SurrealDB instance. Only `username` and `password` are required.

		```python
		from surrealdb import Surreal

		db = Surreal("ws://localhost:8000")
		db.connect()

		tokens = db.signin({
		    "username": "root",
		    "password": "root",
		})
		```

	
**Namespace user**

A namespace user has access to all databases within a specific namespace. Provide the `namespace` alongside credentials.

		```python
		from surrealdb import Surreal

		db = Surreal("ws://localhost:8000")
		db.connect()

		tokens = db.signin({
		    "namespace": "surrealdb",
		    "username": "tobie",
		    "password": "123456",
		})
		```

	
**Database user**

A database user has access to a single database. Provide both `namespace` and `database` alongside credentials.

		```python
		from surrealdb import Surreal

		db = Surreal("ws://localhost:8000")
		db.connect()

		tokens = db.signin({
		    "namespace": "surrealdb",
		    "database": "docs",
		    "username": "tobie",
		    "password": "123456",
		})
		```

	
**Record access**

A record access user authenticates against a [`DEFINE ACCESS`](../../../reference/query-language/statements/define/access/record.md) method defined on a database. Provide `namespace`, `database`, `access`, and any variables required by the access definition.

		```python
		from surrealdb import Surreal

		db = Surreal("ws://localhost:8000")
		db.connect()

		tokens = db.signin({
		    "namespace": "surrealdb",
		    "database": "docs",
		    "access": "account",
		    "variables": {
		        "email": "info@surrealdb.com",
		        "password": "123456",
		    },
		})
		```

All examples above use the synchronous API. The async variant works the same way — prefix each call with `await`.

## Signing up users

The `.signup()` method registers a new record user through a [record access method](../../../reference/query-language/statements/define/access/record.md) and returns [Tokens](../api/types/index.md#tokens). Signup is only available for record-level access.

You must provide the `namespace`, `database`, and `access` fields, along with any `variables` expected by the access definition.

	
**Synchronous**

```python
		from surrealdb import Surreal

		db = Surreal("ws://localhost:8000")
		db.connect()

		tokens = db.signup({
		    "namespace": "surrealdb",
		    "database": "docs",
		    "access": "account",
		    "variables": {
		        "email": "newuser@surrealdb.com",
		        "password": "s3cureP@ss",
		    },
		})
		```

	
**Asynchronous**

```python
		from surrealdb import AsyncSurreal

		db = AsyncSurreal("ws://localhost:8000")
		await db.connect()

		tokens = await db.signup({
		    "namespace": "surrealdb",
		    "database": "docs",
		    "access": "account",
		    "variables": {
		        "email": "newuser@surrealdb.com",
		        "password": "s3cureP@ss",
		    },
		})
		```

## Authenticating with an existing token

If you already have a JWT token — for example, one returned from a previous `.signin()` or stored in a cookie — you can authenticate the connection directly with `.authenticate()`.

	
**Synchronous**

```python
		db.authenticate("eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9...")
		```

	
**Asynchronous**

```python
		await db.authenticate("eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9...")
		```

This is useful in server-side applications where the token is passed from a client request and needs to be forwarded to the database connection.

## Retrieving user information

The `.info()` method returns the record data for the currently authenticated record user. This is only available when signed in as a record-level user.

	
**Synchronous**

```python
		user = db.info()
		print(user)
		```

	
**Asynchronous**

```python
		user = await db.info()
		print(user)
		```

The return value is a [Value](../api/types/index.md#value) containing the fields of the authenticated user's record. If no record user is authenticated, the method returns `None`.

## Signing out

The `.invalidate()` method clears the authentication state for the current connection. After invalidation, subsequent operations will execute as an unauthenticated user.

	
**Synchronous**

```python
		db.invalidate()
		```

	
**Asynchronous**

```python
		await db.invalidate()
		```

## Learn more

- [Surreal API reference](../api/core/surreal.md) for complete method signatures and parameters
- [Tokens type reference](../api/types/index.md#tokens) for the structure of the returned tokens
- [Authentication in SurrealDB](../../../learn/security/authentication/authentication.md) for an overview of authentication concepts
- [DEFINE ACCESS](../../../reference/query-language/statements/define/access/index.md) for defining record and JWT access methods
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for connection setup and protocol options
