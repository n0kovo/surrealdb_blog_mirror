---
position: 9
title: Value types
description: Work with record identifiers, tables, and the JSON value model in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/concepts/value-types.mdx"
---

# Value types

The Kotlin SDK represents data with [`kotlinx.serialization`](serialization.md) JSON values, plus a small set of dedicated types for referring to tables and records. These are the building blocks passed to the [CRUD builders](data-manipulation.md) and queries.

## Record and table types

| Type | Description |
|---|---|
| [`Table`](../api/values/table.md) | Refers to a table by name |
| [`RecordId`](../api/values/record-id.md) | Refers to a single record (`table:id`) |
| [`RecordIdRange`](../api/values/record-id-range.md) | Refers to a range of records within a table |

```kotlin

val table = Table("person")
val record = RecordId("person", "ada")
```

When these are bound into a query, the SDK renders them with the appropriate SurrealDB casting functions — `type::table(name)` for a [`Table`](../api/values/table.md) and `type::record(table, id)` for a [`RecordId`](../api/values/record-id.md) — so values are always passed safely.

## The JSON value model

Beyond the record types above, all data is modelled as [`JsonElement`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/-json-element/). Read methods return a [`JsonElement`](../api/values/value.md), and write methods accept a [`JsonObject`](../api/values/value.md). Build payloads with [`buildJsonObject`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/build-json-object.html).

```kotlin

val data = buildJsonObject {
    put("name", "Ada")
    put("age", 36)
}
```

> [!NOTE]
> The SDK does not ship dedicated wrapper classes for datetimes, durations, or geometries. Express these as SurrealQL literals in a query, or as the JSON values that SurrealDB expects, and decode results into your own [`@Serializable`](serialization.md) types.

## Learn more

- [`Table`](../api/values/table.md), [`RecordId`](../api/values/record-id.md), and [`RecordIdRange`](../api/values/record-id-range.md) references
- [Value (JSON model)](../api/values/value.md) reference
- [Serialization](serialization.md) for decoding into your own types
