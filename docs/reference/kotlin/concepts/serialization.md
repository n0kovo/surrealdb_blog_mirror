---
position: 8
title: Serialization
description: Encode and decode records using kotlinx.serialization with the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/concepts/serialization.mdx"
---

# Serialization

The Kotlin SDK uses [`kotlinx.serialization`](https://github.com/Kotlin/kotlinx.serialization) as its data model. Payloads are sent and received as JSON, so you work with [`JsonElement`](value-types.md) values directly, or decode them into your own [`@Serializable`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-core/kotlinx.serialization/-serializable/) types.

## Defining serializable types

Annotate your data classes with `@Serializable`. Field names map directly to record fields; use `@SerialName` to map a different key.

```kotlin

@Serializable
data class Person(
    val name: String,
    val age: Int,
    @SerialName("created_at") val createdAt: String? = null,
)
```

## Decoding query results

The inline [`.queryAs<T>()`](../api/core/surreal-client.md#query-as) helper runs a query and decodes its result into `T`, while every fluent builder offers the typed [`.awaitAs<T>()`](../api/core/query-builder.md#await-as) terminal.

```kotlin

// Via raw SurrealQL
val people: List<Person> = client.queryAs("SELECT * FROM person")

// Via a builder
val sameAgain: List<Person> = client.select(Table("person")).awaitAs()
```

To decode an arbitrary [`JsonElement`](value-types.md) you already hold, use [`.decode<T>()`](../api/core/surreal-client.md#decode).

```kotlin
val element = client.query("SELECT * FROM person:ada")
val ada: Person = client.decode(element)
```

## Building payloads

When writing data, build a [`JsonObject`](value-types.md) with [`buildJsonObject`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/build-json-object.html), or encode a serializable instance with the client's [`json`](../api/core/surreal-client.md#json) instance.

```kotlin

val data = client.json.encodeToJsonElement(Person("Ada", 36))
client.create(com.surrealdb.kotlin.query.Table("person")).content(data).await()
```

## Customising the JSON format

The [`json`](../api/core/client-config.md#json) field on [`SurrealClientConfig`](../api/core/client-config.md) lets you supply a custom [`Json`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json/) instance, for example to register contextual serializers or change null handling. The default ignores unknown keys and is lenient.

```kotlin

val client = SurrealClient(
    SurrealClientConfig(
        url = "ws://localhost:8000",
        json = Json {
            ignoreUnknownKeys = true
            isLenient = true
            explicitNulls = false
        },
    ),
)
```

## Learn more

- [Value types](value-types.md) for `Table`, `RecordId`, and the JSON model
- [Executing queries](executing-queries.md) for `queryAs`
- [Query builder reference](../api/core/query-builder.md) for `awaitAs`
- [kotlinx.serialization](https://kotlinlang.org/docs/serialization.html) for the underlying library
