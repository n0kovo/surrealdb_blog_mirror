---
position: 4
title: Value (JSON model)
description: How the SurrealDB Kotlin SDK models values using kotlinx.serialization JSON types.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/api/values/value.mdx"
---

# Value (JSON model) {#value}

The Kotlin SDK models all data — beyond the dedicated [record types](record-id.md) — using [`kotlinx.serialization`](../../concepts/serialization.md) JSON types. Read methods return a [`JsonElement`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/); write methods accept a [`JsonObject`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-object/).

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Building values

Construct objects with [`buildJsonObject`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/build-json-object.html).

```kotlin title="Example"
val data = buildJsonObject {
    put("name", "Ada")
    put("age", 36)
}
```

## Decoding values

Rather than navigating raw `JsonElement` trees, decode results into your own [`@Serializable`](../../concepts/serialization.md) types with [`.queryAs<T>()`](../core/surreal-client.md#query-as), [`.awaitAs<T>()`](../core/query-builder.md#await-as), or [`.decode<T>()`](../core/surreal-client.md#decode).

```kotlin title="Example"
val people: List<Person> = client.queryAs("SELECT * FROM person")
```

> [!NOTE]
> The SDK does not provide dedicated wrapper classes for datetimes, durations, or geometries. Express these as SurrealQL literals or the JSON values SurrealDB expects, and decode results into your own types.

## Learn more

- [Value types](../../concepts/value-types.md)
- [Serialization](../../concepts/serialization.md)
