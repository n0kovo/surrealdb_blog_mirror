---
position: 1
title: RecordId
description: The RecordId type identifies a single record in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/api/values/record-id.mdx"
---

# `RecordId` {#record-id}

`RecordId` identifies a single record by its table and ID, rendered as `table:id`. Pass it to the [CRUD builders](../../concepts/data-manipulation.md) to target one record.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Constructor

```kotlin title="Method Syntax"
RecordId(table, id)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`table` *[required]*</td><td>`String`</td><td>The table name.</td></tr>
        <tr><td>`id` *[required]*</td><td>`String`</td><td>The record identifier within the table.</td></tr>
    </tbody>
</table>

```kotlin title="Example"
val ada = RecordId("person", "ada")

client.select(ada).awaitAs<Person>()
```

When bound into a query, a `RecordId` is rendered with `type::record(table, id)` so the value is always passed safely.

## Learn more

- [Value types](../../concepts/value-types.md)
- [`Table`](table.md) and [`RecordIdRange`](record-id-range.md)
