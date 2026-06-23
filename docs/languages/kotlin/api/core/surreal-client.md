---
position: 1
title: SurrealClient
description: The SurrealClient class is the main entry point for connecting to and interacting with a SurrealDB instance from Kotlin.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/api/core/surreal-client.mdx"
---

# `SurrealClient` {#surreal-client}

The `SurrealClient` class is the main entry point for the Kotlin SDK. It connects to a SurrealDB instance, authenticates, queries, and manages data. It extends [`SurrealSession`](session.md) and implements `AutoCloseable`. Almost every networked method is a `suspend` function and has a `...Result` companion that returns a [`Result`](https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-result/) instead of throwing.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Connection methods

### `SurrealClient(config)` {#constructor}

Creates a new client from a [`SurrealClientConfig`](client-config.md). With `autoConnect = true` (the default) the client connects lazily on the first request.

```kotlin title="Method Syntax"
SurrealClient(config)
```

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
            <td>`config` *[required]*</td>
            <td>`SurrealClientConfig`</td>
            <td>The client configuration, including the connection `url`.</td>
        </tr>
    </tbody>
</table>

**Returns:** `SurrealClient`

```kotlin title="Example"
val client = SurrealClient(SurrealClientConfig(url = "ws://localhost:8000"))
```

### `.connect()` {#connect}

Establishes the connection explicitly. Rarely needed when `autoConnect` is enabled.

```kotlin title="Method Syntax"
client.connect()
```

**Returns:** `Unit`

```kotlin title="Example"
client.connect()
```

### `.close()` {#close}

Closes the active connection and releases all associated resources.

```kotlin title="Method Syntax"
client.close()
```

**Returns:** `Unit`

```kotlin title="Example"
client.close()
```

### `.use(namespace, database)` {#use}

Selects the namespace and database for subsequent operations.

```kotlin title="Method Syntax"
client.use(namespace, database)
```

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
            <td>`namespace` *[required]*</td>
            <td>`String`</td>
            <td>The namespace to select.</td>
        </tr>
        <tr>
            <td>`database` *[required]*</td>
            <td>`String`</td>
            <td>The database to select.</td>
        </tr>
    </tbody>
</table>

**Returns:** `JsonElement`

```kotlin title="Example"
client.use("surrealdb", "docs")
```

### `.ping()` {#ping}

Pings the server to verify connectivity.

```kotlin title="Method Syntax"
client.ping()
```

**Returns:** `JsonElement`

### `.version()` {#version}

Returns the version of the connected SurrealDB server.

```kotlin title="Method Syntax"
client.version()
```

**Returns:** `JsonElement`

```kotlin title="Example"
val version = client.version()
```

### `.supports(feature)` {#supports}

Returns whether the current transport supports the given [`SurrealFeature`](../features/index.md#feature).

```kotlin title="Method Syntax"
client.supports(feature)
```

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
            <td>`feature` *[required]*</td>
            <td>`SurrealFeature`</td>
            <td>The feature to check.</td>
        </tr>
    </tbody>
</table>

**Returns:** `Boolean`

```kotlin title="Example"
if (client.supports(SurrealFeature.LiveQueries)) { /* ... */ }
```

---

## Authentication methods

### `.signup(params)` {#signup}

Signs up against a [record access](../../../../reference/query-language/statements/define/access/record.md) method and returns a token.

```kotlin title="Method Syntax"
client.signup(params)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`params` *[required]*</td>
            <td>`JsonObject`</td>
            <td>The sign-up parameters (namespace, database, access, and any record variables).</td>
        </tr>
    </tbody>
</table>

**Returns:** `JsonElement`

### `.signin(params)` {#signin}

Signs in with the given credentials and returns a token.

```kotlin title="Method Syntax"
client.signin(params)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`params` *[required]*</td>
            <td>`JsonObject`</td>
            <td>The sign-in credentials.</td>
        </tr>
    </tbody>
</table>

**Returns:** `JsonElement`

```kotlin title="Example"
client.signin(buildJsonObject {
    put("user", "root")
    put("pass", "root")
})
```

### `.authenticate(token)` {#authenticate}

Authenticates the session with an existing token.

```kotlin title="Method Syntax"
client.authenticate(token)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`token` *[required]*</td>
            <td>`String`</td>
            <td>A JWT previously issued by SurrealDB.</td>
        </tr>
    </tbody>
</table>

**Returns:** `JsonElement`

### `.auth()` {#auth}

Returns the record of the currently authenticated user.

```kotlin title="Method Syntax"
client.auth()
```

**Returns:** `JsonElement`

### `.invalidate()` {#invalidate}

Invalidates the current authentication for the session.

```kotlin title="Method Syntax"
client.invalidate()
```

**Returns:** `JsonElement`

### `.reset()` {#reset}

Resets the session to its initial, unauthenticated state.

```kotlin title="Method Syntax"
client.reset()
```

**Returns:** `JsonElement`

---

## Query methods

### `.query(sql, vars)` {#query}

Runs a raw [SurrealQL](../../../../reference/query-language/index.md) statement with optional bound parameters.

```kotlin title="Method Syntax"
client.query(sql, vars)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`sql` *[required]*</td>
            <td>`String`</td>
            <td>The SurrealQL to execute.</td>
        </tr>
        <tr>
            <td>`vars`</td>
            <td>`JsonObject?`</td>
            <td>Optional parameters bound as `$name` in the query.</td>
        </tr>
    </tbody>
</table>

**Returns:** `JsonElement`

```kotlin title="Example"
val result = client.query(
    "SELECT * FROM person WHERE age > \$min",
    buildJsonObject { put("min", 18) },
)
```

There is also an overload that accepts a `BoundQuery` built with the [`surql`](query-builder.md#surql) DSL.

### `.queryAs<T>(sql, vars)` {#query-as}

Runs SurrealQL and decodes the result into `T` using [`kotlinx.serialization`](../../concepts/serialization.md).

```kotlin title="Method Syntax"
client.queryAs<T>(sql, vars)
```

**Returns:** `T`

```kotlin title="Example"
val people: List<Person> = client.queryAs("SELECT * FROM person")
```

### `.decode<T>(element)` {#decode}

Decodes a [`JsonElement`](../values/value.md) into `T` using the client's configured `Json` instance.

```kotlin title="Method Syntax"
client.decode<T>(element)
```

**Returns:** `T`

### `.let(key, value)` {#let}

Defines a session parameter referenced as `$key` in subsequent queries.

```kotlin title="Method Syntax"
client.let(key, value)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`key` *[required]*</td>
            <td>`String`</td>
            <td>The parameter name.</td>
        </tr>
        <tr>
            <td>`value` *[required]*</td>
            <td>`JsonElement`</td>
            <td>The parameter value.</td>
        </tr>
    </tbody>
</table>

**Returns:** `JsonElement`

### `.unset(key)` {#unset}

Removes a previously defined session parameter.

```kotlin title="Method Syntax"
client.unset(key)
```

**Returns:** `JsonElement`

---

## CRUD methods

These methods return a [query builder](query-builder.md) that you refine and terminate with `await()` or [`awaitAs<T>()`](query-builder.md#await-as). The `what` argument accepts a [`Table`](../values/table.md), [`RecordId`](../values/record-id.md), or [`RecordIdRange`](../values/record-id-range.md).

### `.select(what)` {#select}

Returns a [`SelectQuery`](query-builder.md#select-query) for reading records.

```kotlin title="Method Syntax"
client.select(what)
```

**Returns:** `SelectQuery`

```kotlin title="Example"
val all: List<Person> = client.select(Table("person")).awaitAs()
```

### `.create(what)` {#create}

Returns a [`CreateQuery`](query-builder.md#create-query) for inserting a record.

```kotlin title="Method Syntax"
client.create(what)
```

**Returns:** `CreateQuery`

### `.update(what)` {#update}

Returns an `UpdateQuery` for replacing record content.

```kotlin title="Method Syntax"
client.update(what)
```

**Returns:** `UpdateQuery`

### `.upsert(what)` {#upsert}

Returns an `UpsertQuery` for creating or updating records.

```kotlin title="Method Syntax"
client.upsert(what)
```

**Returns:** `UpsertQuery`

### `.merge(what, data)` {#merge}

Returns a `MergeQuery` that merges `data` into the matched records.

```kotlin title="Method Syntax"
client.merge(what, data)
```

**Returns:** `MergeQuery`

### `.patch(what, patches, diff)` {#patch}

Returns a `PatchQuery` that applies [JSON Patch](https://jsonpatch.com/) operations.

```kotlin title="Method Syntax"
client.patch(what, patches, diff = false)
```

**Returns:** `PatchQuery`

### `.delete(what)` {#delete}

Returns a `DeleteQuery` for removing records.

```kotlin title="Method Syntax"
client.delete(what)
```

**Returns:** `DeleteQuery`

### `.relate(in, relation, out)` {#relate}

Returns a `RelateQuery` that creates a graph edge between two records.

```kotlin title="Method Syntax"
client.relate(`in`, relation, out)
```

**Returns:** `RelateQuery`

### `.insert(into, data)` {#insert}

Returns an `InsertQuery` that inserts one or more records into a [`Table`](../values/table.md).

```kotlin title="Method Syntax"
client.insert(into, data)
```

**Returns:** `InsertQuery`

### `.insertRelation(into, data)` {#insert-relation}

Returns an `InsertRelationQuery` that inserts relation records into a [`Table`](../values/table.md).

```kotlin title="Method Syntax"
client.insertRelation(into, data)
```

**Returns:** `InsertRelationQuery`

### `.run(function)` {#run}

Returns a `RunQuery` that invokes a built-in or custom [function](../../../../reference/query-language/functions/database-functions/index.md).

```kotlin title="Method Syntax"
client.run(function)
```

**Returns:** `RunQuery`

---

## Live query methods

### `.live(table, diff)` {#live}

Starts a [live query](../../concepts/live-queries.md) and returns a [`LiveQuerySubscription`](live-subscription.md). **WebSocket only.**

```kotlin title="Method Syntax"
client.live(table, diff = null)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`table` *[required]*</td>
            <td>`String`</td>
            <td>The table to watch.</td>
        </tr>
        <tr>
            <td>`diff`</td>
            <td>`Boolean?`</td>
            <td>When `true`, emit JSON Patch diffs instead of full records.</td>
        </tr>
    </tbody>
</table>

**Returns:** `LiveQuerySubscription`

### `.kill(liveQueryId)` {#kill}

Kills a live query by its ID. **WebSocket only.**

```kotlin title="Method Syntax"
client.kill(liveQueryId)
```

**Returns:** `JsonElement`

---

## Sessions

### `.newSession()` {#new-session}

Creates a new isolated [`SurrealSession`](session.md) over the same connection. **WebSocket only.**

```kotlin title="Method Syntax"
client.newSession()
```

**Returns:** `SurrealSession`

### `.closeSession(session)` {#close-session}

Closes a session previously created with [`.newSession()`](#new-session).

```kotlin title="Method Syntax"
client.closeSession(session)
```

**Returns:** `Unit`

---

## Properties

<table>
    <thead>
        <tr><th>Property</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`config`</td>
            <td>`SurrealClientConfig`</td>
            <td>The configuration the client was created with.</td>
        </tr>
        <tr>
            <td>`features`</td>
            <td>`Set&lt;SurrealFeature&gt;`</td>
            <td>The features supported by the active transport.</td>
        </tr>
        <tr>
            <td>`connectionEvents`</td>
            <td>`SharedFlow&lt;SurrealConnectionEvent&gt;`</td>
            <td>A flow of connection lifecycle events.</td>
        </tr>
        <tr>
            <td id="json">`json`</td>
            <td>`Json`</td>
            <td>The `kotlinx.serialization` instance used for encoding and decoding.</td>
        </tr>
    </tbody>
</table>

## Learn more

- [Client configuration](client-config.md)
- [Session](session.md)
- [Query builder](query-builder.md)
- [Features and events](../features/index.md)
- [Errors](../errors/index.md)
