---
position: 5
title: Kotlin
description: Connect to SurrealDB and run your first queries with the Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin.mdx"
---

# Getting started

The Kotlin SDK for SurrealDB lets you connect to a database and query it from your application with coroutines. This guide covers connecting, authenticating, and running your first queries.

> [!NOTE]
> Every network operation on the SDK is a `suspend` function, so the examples below run inside a coroutine (for example, a [`runBlocking`](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines/run-blocking.html) block or a `CoroutineScope`).

## 1. Install the SDK

Follow the [installation guide](../reference/kotlin/installation.md) to add the SDK as a dependency in your project. Once installed, import the client to start using it.

```kotlin
```

## 2. Connect to SurrealDB

Create a [`SurrealClient`](../reference/kotlin/api/core/surreal-client.md) with a [`SurrealClientConfig`](../reference/kotlin/api/core/client-config.md), then call [`.use()`](../reference/kotlin/api/core/surreal-client.md#use) to select a namespace and database, and [`.signin()`](../reference/kotlin/api/core/surreal-client.md#signin) to authenticate.

The transport is selected automatically from the URL scheme:
- **WebSocket** (`ws://`, `wss://`) for long-lived stateful connections that support live queries, transactions, and multiple sessions
- **HTTP** (`http://`, `https://`) for short-lived stateless connections

```kotlin

fun main() = runBlocking {
    val client = SurrealClient(SurrealClientConfig(url = "ws://localhost:8000"))

    client.signin(buildJsonObject {
        put("user", "root")
        put("pass", "root")
    })
    client.use("surrealdb", "docs")

    // ...

    client.close()
}
```

The client connects automatically on first use (`autoConnect` defaults to `true`). Call [`.close()`](../reference/kotlin/api/core/surreal-client.md#close) when you are finished to release resources.

## 3. Inserting data into SurrealDB

To represent records in your application, define [`@Serializable`](../reference/kotlin/concepts/serialization.md) data classes that match your table structure.

```kotlin

@Serializable
data class Person(val name: String, val age: Int)
```

Use the [`.create()`](../reference/kotlin/api/core/surreal-client.md#create) builder to insert a record. Pass a [`Table`](../reference/kotlin/api/values/table.md) to create in a table with a generated ID, or a [`RecordId`](../reference/kotlin/api/values/record-id.md) to create a record with a specific ID. Builders are terminated with `await()` (raw JSON) or the typed [`awaitAs<T>()`](../reference/kotlin/api/core/query-builder.md#await-as) extension.

```kotlin

val created: Person = client
    .create(RecordId("person", "john"))
    .content(buildJsonObject {
        put("name", "John")
        put("age", 32)
    })
    .awaitAs()
```

## 4. Retrieving data from SurrealDB

### Selecting records

The [`.select()`](../reference/kotlin/api/core/surreal-client.md#select) builder retrieves records from a table or a single record by its [`RecordId`](../reference/kotlin/api/values/record-id.md). Refine it with [`.where()`](../reference/kotlin/api/core/query-builder.md#where) using the [expression helpers](../reference/kotlin/api/core/query-builder.md#expressions).

```kotlin

val adults: List<Person> = client
    .select(Table("person"))
    .where(field("age") gte 18)
    .limit(50)
    .awaitAs()
```

### Running SurrealQL queries

For more advanced use cases, use [`.query()`](../reference/kotlin/api/core/surreal-client.md#query) to execute [SurrealQL](../reference/query-language/index.md) statements with bound [parameters](../reference/query-language/language-primitives/parameters.md), or [`.queryAs<T>()`](../reference/kotlin/api/core/surreal-client.md#query-as) to decode the result directly.

```kotlin

val people: List<Person> = client.queryAs(
    "SELECT * FROM person WHERE age > \$min_age",
    buildJsonObject { put("min_age", 25) },
)
```

## 5. Closing the connection

Call [`.close()`](../reference/kotlin/api/core/surreal-client.md#close) to release the connection and all associated resources.

```kotlin
client.close()
```

## Next steps

You have learned how to install the SDK, connect to SurrealDB, create records, and retrieve data. There is a lot more you can do with the SDK, including updating and deleting records, authentication, live queries, and transactions.

- **[Connecting to SurrealDB](../reference/kotlin/concepts/connecting-to-surrealdb.md)** — Learn how to manage connections, protocols, and reconnection.
- **[Authentication](../reference/kotlin/concepts/authentication.md)** — Read more about authentication and how to integrate it into your application.
- **[Data manipulation](../reference/kotlin/concepts/data-manipulation.md)** — Learn how to create, read, update, and delete records using the builders.
- **[API Reference](../reference/kotlin/api/core/surreal-client.md)** — Complete reference for the client, builders, types, and errors.

> [!NOTE]
> This getting-started guide covers the essentials. For the complete methods, API, and concept reference, see the [Kotlin SDK reference](../reference/kotlin/index.md).
