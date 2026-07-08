---
position: 2
title: SurrealSession
description: The SurrealSession class provides session-scoped context with authentication and query execution capabilities.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/api/core/surreal-session.mdx"
---

# `SurrealSession` {#surrealsession}

The `SurrealSession` class represents a scoped contextual session attached to a SurrealDB connection. It provides authentication, session configuration, and inherits all query execution methods from [`SurrealQueryable`](surreal-queryable.md).

Sessions allow you to maintain isolated contexts with their own namespace, database, variables, and authentication state, while sharing the underlying connection.

**Extends:** [`SurrealQueryable`](surreal-queryable.md)

**Extended by:** [`Surreal`](surreal.md)

**Source:** [api/session.ts](https://github.com/surrealdb/surrealdb.js/blob/main/packages/sdk/src/api/session.ts)

## Constructor

The constructor is typically not called directly. Use [`Surreal.newSession()`](surreal.md#newsession) or [`forkSession()`](#forksession) to create new sessions.

## Properties

### `namespace` {#namespace}

Returns the currently selected namespace for this session.

**Type:** `string | undefined`

**Example:**
```ts
console.log(session.namespace); // "my_namespace"
```

### `database` {#database}

Returns the currently selected database for this session.

**Type:** `string | undefined`

**Example:**
```ts
console.log(session.database); // "my_database"
```

### `accessToken` {#accesstoken}

Returns the current authentication access token for this session.

**Type:** `string | undefined`

**Example:**
```ts
if (session.accessToken) {
    console.log('Session is authenticated');
}
```

### `parameters` {#parameters}

Returns all parameters currently defined on the session.

**Type:** `Record<string, unknown>`

**Example:**
```ts
console.log(session.parameters); // { user_id: '123', role: 'admin' }
```

### `session` {#session}

Returns the unique session ID. For the default session, `undefined` is returned.

**Type:** [`Uuid`](../values/uuid.md) `| undefined`

**Example:**
```ts
const sessionId = session.session;
console.log('Session ID:', sessionId);
```

### `isValid` {#isvalid}

Returns whether the session is valid and can be used. This is always `true` for the default session, but will be `false` for sessions that have been disposed via [`reset()`](#reset) or [`closeSession()`](#closesession).

**Type:** `boolean`

**Example:**
```ts
if (session.isValid) {
    await session.select('users');
} else {
    console.log('Session has been closed');
}
```

## Session management methods

### `.forkSession()` {#forksession}

Create a new session by cloning the current session. The new session inherits all properties from the parent session including namespace, database, variables, and authentication state.

Sessions are automatically restored when the connection reconnects. Call [`reset()`](#reset) on the created session to destroy it.

```ts title="Method Syntax"
session.forkSession()
```

#### Returns
[`Promise<SurrealSession>`](surreal-session.md) - A new session instance

#### Example
```ts
// Create a forked session that inherits parent state
const childSession = await session.forkSession();

// The child inherits parent's namespace and database
console.log(childSession.namespace); // Same as parent
console.log(childSession.database); // Same as parent

// But can be changed independently
await childSession.use({ database: 'other_db' });

// Parent session remains unchanged
console.log(session.database); // Original database
console.log(childSession.database); // 'other_db'

// Clean up when done
await childSession.reset();
```

### `.closeSession()` {#closesession}

Closes the current session and disposes of it. After this method is called, the session cannot be used again, and [`isValid`](#isvalid) will return `false`.

```ts title="Method Syntax"
session.closeSession()
```

#### Returns
`Promise<void>` - Resolves when the session is closed

#### Example
```ts
await session.closeSession();
console.log(session.isValid); // false
```

## Transaction methods

### `.beginTransaction()` {#begintransaction}

Create a new transaction scoped to the current session. Transactions allow you to execute multiple queries atomically.

Call [`commit()`](surreal-transaction.md#commit) on the transaction to apply changes, or [`cancel()`](surreal-transaction.md#cancel) to discard them.

```ts title="Method Syntax"
session.beginTransaction()
```

#### Returns
`Promise<SurrealTransaction>` - A new [`SurrealTransaction`](surreal-transaction.md) instance

#### Example
```ts
// Start a transaction
const txn = await session.beginTransaction();

try {
    // Execute queries within the transaction
    await txn.create(new RecordId('users', 'john'), {
        content: { name: 'John Doe', email: 'john@example.com' }
    });
    
    await txn.create(new RecordId('posts', '1'), {
                content: { author: new RecordId('users', 'john'),
            title: 'Hello' }
    });
    
    // Commit all changes atomically
    await txn.commit();
    console.log('Transaction committed successfully');
} catch (error) {
    // Roll back on error
    await txn.cancel();
    console.error('Transaction cancelled:', error);
}
```

## Session configuration methods

### `.use()` {#use}

Switch to the specified namespace and/or database for this session.

Leaving the namespace or database `undefined` will leave the current value unchanged, while passing `null` will unset the selected namespace or database.

```ts title="Method Syntax"
session.use(what)
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`what` <label label="optional" /></td>
            <td>`Nullable&lt;<a href="/docs/reference/javascript/api/types/#namespacedatabase">NamespaceDatabase</a>&gt;`</td>
            <td>Object specifying namespace and/or database to switch to. If omitted, returns the current namespace and database.</td>
        </tr>
    </tbody>
</table>

#### Returns
[`Promise<NamespaceDatabase>`](../types/index.md#namespacedatabase) - The current or newly selected namespace and database

#### Examples

```ts title="Switch Both Namespace and Database"
await session.use({ 
    namespace: 'production', 
    database: 'main' 
});
```

```ts title="Switch Only Database"
await session.use({ 
    database: 'analytics' 
});
// Namespace remains unchanged
```

```ts title="Unset Database"
await session.use({ 
    database: null 
});
// Database is now undefined
```

### `.set()` {#set}

Define a variable for the current session. Variables can be used in SurrealQL queries with the `$` prefix.

```ts title="Method Syntax"
session.set(variable, value)
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`variable` <label label="required" /></td>
            <td>`string`</td>
            <td>The name of the variable (without the $ prefix).</td>
        </tr>
        <tr>
            <td>`value` <label label="required" /></td>
            <td>`unknown`</td>
            <td>The value to assign to the variable.</td>
        </tr>
    </tbody>
</table>

#### Returns
`Promise<void>` - Resolves when the variable is set

#### Example
```ts
// Set a variable
await session.set('user_id', '12345');

// Use it in a query
const result = await session.query(
    'SELECT * FROM posts WHERE author = $user_id'
).collect();
```

### `.unset()` {#unset}

Remove a variable from the current session.

```ts title="Method Syntax"
session.unset(variable)
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`variable` <label label="required" /></td>
            <td>`string`</td>
            <td>The name of the variable to remove (without the $ prefix).</td>
        </tr>
    </tbody>
</table>

#### Returns
`Promise<void>` - Resolves when the variable is removed

#### Example
```ts
await session.unset('user_id');
```

### `.reset()` {#reset}

Resets the current session to its initial state, clearing authentication state, variables, and selected namespace/database.

For non-default sessions, this also closes and disposes of the session.

```ts title="Method Syntax"
session.reset()
```

#### Returns
`Promise<void>` - Resolves when the session is reset

#### Example
```ts
// Reset session to clean state
await session.reset();

// Session is now cleared
console.log(session.namespace); // undefined
console.log(session.accessToken); // undefined
console.log(session.parameters); // {}
```

## Authentication methods

### `.signup()` {#signup}

Sign up a new record user to the SurrealDB instance.

> [!NOTE]
> When this method is called, the `authentication` property passed to [`connect()`](surreal.md#connect) will be ignored. You are responsible for handling session invalidation by listening to the [`auth`](#event-auth) event.

```ts title="Method Syntax"
session.signup(auth)
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`auth` <label label="required" /></td>
            <td>`<a href="/docs/reference/javascript/api/types/#accessrecordauth">AccessRecordAuth</a>`</td>
            <td>The authentication details including access method and record data.</td>
        </tr>
    </tbody>
</table>

#### Returns
[`Promise<Tokens>`](../types/index.md#tokens) - The authentication tokens (access and refresh tokens)

#### Example
```ts
const tokens = await session.signup({
    namespace: 'my_namespace',
    database: 'my_database',
    access: 'user_access',
    variables: {
        email: 'user@example.com',
        password: 'secure_password',
        name: 'John Doe'
    }
});

console.log('Access token:', tokens.access);
console.log('Refresh token:', tokens.refresh);
```

### `.signin()` {#signin}

Sign in to the SurrealDB instance with authentication credentials.

> [!NOTE]
> When this method is called, the `authentication` property passed to [`connect()`](surreal.md#connect) will be ignored. You are responsible for handling session invalidation by listening to the [`auth`](#event-auth) event.

```ts title="Method Syntax"
session.signin(auth)
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`auth` <label label="required" /></td>
            <td>`<a href="/docs/reference/javascript/api/types/#anyauth">AnyAuth</a>`</td>
            <td>Authentication details (system user, record user, or access method).</td>
        </tr>
    </tbody>
</table>

#### Returns
[`Promise<Tokens>`](../types/index.md#tokens) - The authentication tokens

#### Examples

```ts title="System User Authentication"
const tokens = await session.signin({
    username: 'root',
    password: 'root'
});
```

```ts title="Record User Authentication"
const tokens = await session.signin({
    namespace: 'my_namespace',
    database: 'my_database',
    access: 'user_access',
    variables: {
        email: 'user@example.com',
        password: 'secure_password'
    }
});
```

### `.authenticate()` {#authenticate}

Authenticate the session using an existing access token or access and refresh token combination.

When authenticating with a refresh token, a new refresh token will be issued and returned.

> [!NOTE]
> When this method is called, the `authentication` property passed to [`connect()`](surreal.md#connect) will be ignored. You are responsible for handling session invalidation by listening to the [`auth`](#event-auth) event.

```ts title="Method Syntax"
session.authenticate(token)
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`token` <label label="required" /></td>
            <td>`<a href="/docs/reference/javascript/api/types/#token">Token</a> | <a href="/docs/reference/javascript/api/types/#tokens">Tokens</a>`</td>
            <td>The access token or tokens object with access and refresh tokens.</td>
        </tr>
    </tbody>
</table>

#### Returns
[`Promise<Tokens>`](../types/index.md#tokens) - The authentication tokens (may include new refresh token)

#### Examples

```ts title="Authenticate with Access Token"
await session.authenticate(accessToken);
```

```ts title="Authenticate with Refresh Token"
const newTokens = await session.authenticate({
    access: oldAccessToken,
    refresh: refreshToken
});

// Store new tokens
console.log('New access token:', newTokens.access);
console.log('New refresh token:', newTokens.refresh);
```

### `.invalidate()` {#invalidate}

Invalidate the authentication for the current session, signing the user out.

```ts title="Method Syntax"
session.invalidate()
```

#### Returns
`Promise<void>` - Resolves when authentication is invalidated

#### Example
```ts
await session.invalidate();
console.log('User signed out');
```

## Events

The `SurrealSession` class emits events that you can subscribe to for tracking session state changes.

### `auth` {#event-auth}

Emitted when the authentication state changes for this session.

**Payload:** `[tokens:` [`Tokens`](../types/index.md#tokens) `| null]` - The new authentication tokens, or `null` if invalidated

**Example:**
```ts
session.subscribe('auth', (tokens) => {
    if (tokens) {
        console.log('Authenticated with token:', tokens.access);
    } else {
        console.log('Authentication invalidated');
    }
});
```

### `using` {#event-using}

Emitted when the namespace or database changes for this session.

**Payload:** `[using:` [`NamespaceDatabase`](../types/index.md#namespacedatabase)`]` - Object containing the new namespace and database

**Example:**
```ts
session.subscribe('using', (using) => {
    console.log('Now using:', using.namespace, '/', using.database);
});
```

### `.subscribe()` {#subscribe}

Subscribe to session events.

```ts title="Method Syntax"
session.subscribe(event, listener)
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`event` <label label="required" /></td>
            <td>`keyof <a href="/docs/reference/javascript/api/types/#sessionevents">SessionEvents</a>`</td>
            <td>The event name to subscribe to (`"auth"` or `"using"`).</td>
        </tr>
        <tr>
            <td>`listener` <label label="required" /></td>
            <td>`Function`</td>
            <td>Callback function invoked when the event is emitted.</td>
        </tr>
    </tbody>
</table>

#### Returns
`() => void` - An unsubscribe function

#### Example
```ts
const unsubscribe = session.subscribe('auth', (tokens) => {
    console.log('Auth changed:', tokens);
});

// Later, unsubscribe
unsubscribe();
```

## Inherited methods

As `SurrealSession` extends [`SurrealQueryable`](surreal-queryable.md), it inherits all query execution methods:

- [`query()`](surreal-queryable.md#query) - Execute raw SurrealQL
- [`select()`](surreal-queryable.md#select) - Select records
- [`create()`](surreal-queryable.md#create) - Create records
- [`insert()`](surreal-queryable.md#insert) - Insert records
- [`update()`](surreal-queryable.md#update) - Update records
- [`upsert()`](surreal-queryable.md#upsert) - Upsert records
- [`delete()`](surreal-queryable.md#delete) - Delete records
- [`relate()`](surreal-queryable.md#relate) - Create graph relationships
- [`live()`](surreal-queryable.md#live) - Subscribe to live queries
- [`liveOf()`](surreal-queryable.md#liveof) - Subscribe to existing live queries
- [`run()`](surreal-queryable.md#run) - Execute functions
- [`auth()`](surreal-queryable.md#auth) - Get authenticated record user
- [`api()`](surreal-queryable.md#api) - Access user-defined APIs

## Async disposal

### `[Symbol.asyncDispose]()` {#symbol-asyncdispose}

Supports the [async disposal](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Symbol/asyncDispose) protocol, allowing sessions to be used with `await using` for automatic cleanup.

```ts title="Method Syntax"
session[Symbol.asyncDispose]()
```

#### Returns
`Promise<void>` - Resolves when the session is disposed

#### Example
```ts
{
    await using session = await db.newSession();
    await session.use({ namespace: 'main', database: 'main' });
    const users = await session.select('users');
}
// Session is automatically disposed when leaving the block
```

## Complete example

```ts

const db = new Surreal();
await db.connect('ws://localhost:8000');

// Use the default session
await db.use({ namespace: 'main', database: 'main' });

// Sign in
await db.signin({
    username: 'root',
    password: 'root'
});

// Create an isolated session
const session = await db.newSession();

// Configure the session
await session.use({ 
    namespace: 'main', 
    database: 'main' 
});

// Set session variables
await session.set('user_role', 'admin');

// Subscribe to session events
session.subscribe('auth', (tokens) => {
        console.log('Session auth changed:',
        tokens ? 'authenticated' : 'signed out');
});

session.subscribe('using', (using) => {
    console.log('Using:', using);
});

// Authenticate as a record user
const tokens = await session.signin({
    namespace: 'main',
    database: 'main',
    access: 'user_access',
    variables: {
        email: 'user@example.com',
        password: 'password'
    }
});

// Execute queries in the session context
const users = await session.select('users');

// Start a transaction
const txn = await session.beginTransaction();
await txn.create('logs:1',
    { content: { message: 'User logged in' } });
await txn.commit();

// Fork the session to create an isolated copy
const childSession = await session.forkSession();
await childSession.use({ database: 'analytics' });

// Clean up
await childSession.reset();
await session.closeSession();
```

## See also

- [Surreal](surreal.md) - Main connection class
- [SurrealQueryable](surreal-queryable.md) - Query execution methods
- [SurrealTransaction](surreal-transaction.md) - Transaction support
- [Authentication Types](../types/index.md#anyauth) - Authentication type definitions
