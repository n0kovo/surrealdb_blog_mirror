---
position: 2
title: Authentication
description: SurrealDB supports a number of methods for authenticating users and securing the database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/concepts/authentication.mdx"
---

# Authentication

SurrealDB supports multiple levels of authentication, from [system users](../../../learn/security/authentication/authentication.md#system-user) to fine-grained [record-level access](../../../learn/security/authentication/authentication.md#record-users). The JavaScript SDK provides methods for signing up and signing in users, managing tokens, and automatically restoring sessions on reconnect.

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
            <td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-session#signin"> ` db.signin(auth) `</a></td>
            <td scope="row" data-label="Description">Signs in as a root, namespace, database, or record user</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-session#signup"> ` db.signup(auth) `</a></td>
			<td scope="row" data-label="Description">Signs up a new record user using an access method</td>
		</tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-session#authenticate"> ` db.authenticate(token) `</a></td>
            <td scope="row" data-label="Description">Authenticates the session with an existing token or token pair</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-session#invalidate"> ` db.invalidate() `</a></td>
            <td scope="row" data-label="Description">Invalidates the current authentication, signing the user out</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/javascript/api/core/surreal-session#subscribe"> ` db.subscribe("auth", callback) `</a></td>
            <td scope="row" data-label="Description">Subscribes to authentication state changes</td>
        </tr>
	</tbody>
</table>

## Signing in users

The `.signin()` method authenticates an existing user. SurrealDB supports multiple authentication levels, and the properties you provide determine which level is used.

	
**Root user**

Authenticate as a root user with full access to all namespaces and databases.

		```ts
		const tokens = await db.signin({
			username: 'root',
			password: 'surrealdb',
		});
		```

	
**Namespace user**

Authenticate as a [namespace user](../../../reference/query-language/statements/define/user.md) with access to all databases in the specified namespace.

		```ts
		const tokens = await db.signin({
			namespace: 'surrealdb',
			username: 'tobie',
			password: 'surrealdb',
		});
		```

	
**Database user**

Authenticate as a [database user](../../../reference/query-language/statements/define/user.md) with access scoped to a specific database.

		```ts
		const tokens = await db.signin({
			namespace: 'surrealdb',
			database: 'docs',
			username: 'tobie',
			password: 'surrealdb',
		});
		```

	
**Record access**

Authenticate as a record user through a defined [record access method](../../../reference/query-language/statements/define/access/record.md). Pass any required variables under the `variables` key.

		```ts
		const tokens = await db.signin({
			namespace: 'surrealdb',
			database: 'docs',
			access: 'account',
			variables: {
				email: 'info@surrealdb.com',
				pass: '123456',
			},
		});
		```

On success, the method returns a [`Tokens`](../api/types/index.md#tokens) object containing the access token and an optional refresh token. The session is automatically authenticated after signing in.

## Signing up users

The `.signup()` method creates a new record user through a defined [record access method](../../../reference/query-language/statements/define/access/record.md). You must specify the namespace, database, and access method, along with any variables expected by the access definition.

```ts
const tokens = await db.signup({
    namespace: 'surrealdb',
    database: 'docs',
    access: 'account',
    variables: {
        email: 'info@surrealdb.com',
        pass: '123456',
    },
});
```

Much like the `.signin()` method, the `.signup()` method returns a [`Tokens`](../api/types/index.md#tokens) object containing the access token and an optional refresh token. The session is automatically authenticated after signing up.

## Authenticating with an existing token

If you already have an access token (for example, stored from a previous session), you can authenticate using the `.authenticate()` method instead of signing in again. This is useful for restoring a user's session without re-entering credentials.

```ts
await db.authenticate(accessToken);
```

When you have a refresh token available, you can pass both tokens as an object. The SDK will exchange the refresh token for a new token pair.

```ts
const newTokens = await db.authenticate({
    access: oldAccessToken,
    refresh: refreshToken,
});
```

## Providing credentials on connect

Rather than calling `.signin()` separately, you can pass authentication credentials directly to the `.connect()` method using the `authentication` option. This is the preferred approach for system users because it allows the SDK to automatically re-authenticate when the connection drops and reconnects.

```ts
await db.connect('ws://127.0.0.1:8000', {
    namespace: 'surrealdb',
    database: 'docs',
    authentication: {
        username: 'root',
        password: 'surrealdb',
    },
});
```

The `authentication` option also accepts an async function, allowing you to retrieve credentials dynamically.

```ts
await db.connect('ws://127.0.0.1:8000', {
    namespace: 'surrealdb',
    database: 'docs',
    authentication: async () => ({
        username: await getUsername(),
        password: await getPassword(),
    }),
});
```

See the full list of connection options in the [`ConnectOptions`](../api/types/index.md#connectoptions) type reference.

> [!NOTE]
> When you call `.signup()` or `.signin()` manually, the `authentication` property passed to `.connect()` is no longer used for automatic re-authentication. You become responsible for handling token expiry by listening to the [`auth`](../api/core/surreal-session.md#event-auth) event.

## Listening to authentication events

The SDK emits an `auth` event whenever the authentication state changes, including on sign in, sign up, token refresh, or invalidation. You can subscribe to this event using the `.subscribe()` method.

```ts
db.subscribe('auth', (tokens) => {
    if (tokens) {
        console.log('Authenticated:', tokens.access);
    } else {
        console.log('Signed out');
    }
});
```

This is particularly useful for record access, where you can subscribe to the `auth` event to automatically update UI or other components when the authentication state changes.

## Accessing authentication state

The SDK exposes the current authentication tokens through the `.accessToken` property on any [`Surreal`](../api/core/surreal.md) or [`SurrealSession`](../api/core/surreal-session.md) instance. This is useful for checking whether the current session is authenticated or for forwarding tokens to other services.

```ts
if (db.accessToken) {
    console.log('Session is authenticated');
}
```

## Signing out

The `.invalidate()` method signs the current user out by clearing the session's authentication state. After calling this method, any subsequent queries will run without authentication.

```ts
await db.invalidate();
```

## Using isolated sessions

You can create multiple isolated sessions within a single connection, each with their own namespace, database, variables, and authentication state. This is useful when different parts of your application need to operate under different credentials or contexts.

```ts
const session = await db.newSession();

await session.signin({
    namespace: 'surrealdb',
    database: 'docs',
    access: 'account',
    variables: {
        email: 'info@surrealdb.com',
        pass: '123456',
    },
});

const users = await session.select('users');

await session.closeSession();
```

## Learn more

- [SurrealSession API reference](../api/core/surreal-session.md) for authentication method signatures
- [Authentication types reference](../api/types/index.md#anyauth) for all credential type definitions
- [Authentication in SurrealDB](../../../learn/security/authentication/authentication.md) for how authentication works at the database level
- [Security best practices](../../../learn/security/best-practices/security-best-practices.md#authentication) for securing your application
- [DEFINE ACCESS](../../../reference/query-language/statements/define/access/index.md) for defining access methods with SurrealQL
- [DEFINE USER](../../../reference/query-language/statements/define/user.md) for creating system users
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for connection setup and reconnection behavior
- [Multiple sessions](multiple-sessions.md) for isolated session management
