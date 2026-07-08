---
position: 2
title: Authentication
description: The Java SDK provides methods for signing in, signing up, and managing authentication tokens.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/concepts/authentication.mdx"
---

# Authentication

The Java SDK supports signing in as a root, namespace, database, or [record-level user](../../../learn/security/authentication/authentication.md#record-users). After signing in, the connection is [authenticated](../../../learn/security/authentication/authentication.md) for all subsequent operations until the session is invalidated or the connection is closed.

You can configure authentication in your SurrealDB database using the [`DEFINE USER`](../../query-language/statements/define/user.md) or [`DEFINE ACCESS`](../../query-language/statements/define/access/index.md) statements.

## API References

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/surreal#signin">`db.signin(credential)`</a></td>
			<td scope="row" data-label="Description">Authenticates with the provided credentials</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/surreal#signup">`db.signup(credential)`</a></td>
			<td scope="row" data-label="Description">Signs up a new record user</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/surreal#authenticate">`db.authenticate(token)`</a></td>
			<td scope="row" data-label="Description">Authenticates with a JWT token</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/java/api/core/surreal#invalidate">`db.invalidate()`</a></td>
			<td scope="row" data-label="Description">Invalidates the current authentication</td>
		</tr>
	</tbody>
</table>

## Signing in as a system user

[System users](../../../learn/security/authentication/authentication.md#system-user) are defined with the [`DEFINE USER`](../../query-language/statements/define/user.md) statement and have access at the root, namespace, or database level. Use the corresponding [credential class](../api/types/index.md) to sign in.

```java

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");

    // Root user — full access to the entire instance
    db.signin(new RootCredential("root", "root"));

    // Namespace user — access to all databases in the namespace
    db.signin(new NamespaceCredential("tobie", "123456", "surrealdb"));

    // Database user — access to a single database
    db.signin(new DatabaseCredential("tobie", "123456", "surrealdb", "docs"));
}
```

## Signing in as a record user

Record users authenticate against a [`DEFINE ACCESS`](../../query-language/statements/define/access/index.md) method defined on a database. Use [`RecordCredential`](../api/types/index.md#record-credential) with the access method name and any parameters required by the access definition.

```java

Map<String, Object> params = Map.of(
    "email", "info@surrealdb.com",
    "password", "123456"
);

Token token = db.signin(new RecordCredential(
    "surrealdb", "docs", "account", params
));
```

## Signing up a record user

The [`.signup()`](../api/core/surreal.md#signup) method registers a new record user through a record access method and returns a [`Token`](../api/types/index.md#token). Signup is only available for record-level access.

```java

Map<String, Object> params = Map.of(
    "email", "newuser@surrealdb.com",
    "password", "s3cureP@ss"
);

Token token = db.signup(new RecordCredential(
    "surrealdb", "docs", "account", params
));
```

## Using authentication tokens

The [`.signin()`](../api/core/surreal.md#signin) and [`.signup()`](../api/core/surreal.md#signup) methods return a [`Token`](../api/types/index.md#token) object. Use `.getAccess()` to retrieve the JWT [access token](../../../learn/security/authentication/authentication.md#token) and `.getRefresh()` to retrieve the optional refresh token. You can store these tokens and use them later to re-authenticate without credentials.

```java
Token token = db.signin(new RootCredential("root", "root"));

String accessToken = token.getAccess();
String refreshToken = token.getRefresh();

// Later, re-authenticate with the stored token
db.authenticate(accessToken);
```

## Authenticating with a bearer token

If you have a bearer key — for example, one defined with a bearer access method — use [`BearerCredential`](../api/types/index.md#bearer-credential) to authenticate.

```java

db.signin(new BearerCredential("eyJhbGciOiJIUzI1NiIs..."));
```

## Invalidating authentication

The [`.invalidate()`](../api/core/surreal.md#invalidate) method clears the authentication state for the current connection. After invalidation, subsequent operations execute as an unauthenticated user.

```java
db.invalidate();
```

## Learn more

- [Surreal API reference](../api/core/surreal.md) for method signatures
- [Java Types reference](../api/types/index.md) for credential class details
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for connection setup
- [DEFINE USER](../../query-language/statements/define/user.md) for configuring system users
- [DEFINE ACCESS](../../query-language/statements/define/access/index.md) for configuring record access
- [Security best practices](../../../learn/security/best-practices/security-best-practices.md) for token management
- [SurrealDB authentication overview](../../../learn/security/authentication/authentication.md) for system users, record users, and token concepts
