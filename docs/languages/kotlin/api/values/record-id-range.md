---
position: 3
title: RecordIdRange
description: The RecordIdRange type targets a range of records within a table in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/api/values/record-id-range.mdx"
---

# `RecordIdRange` {#record-id-range}

`RecordIdRange` targets a contiguous range of records within a table by their IDs. Pass it to the [CRUD builders](../../concepts/data-manipulation.md) to operate on a [range of records](https://surrealdb.com/docs/surrealql/datamodel/ids#record-ranges).

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Constructor

```kotlin title="Method Syntax"
RecordIdRange(table, start, end, includeEnd)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Default</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`table` *[required]*</td><td>`String`</td><td>—</td><td>The table name.</td></tr>
        <tr><td>`start`</td><td>`String?`</td><td>`null`</td><td>The inclusive start ID, or `null` for unbounded.</td></tr>
        <tr><td>`end`</td><td>`String?`</td><td>`null`</td><td>The end ID, or `null` for unbounded.</td></tr>
        <tr><td>`includeEnd`</td><td>`Boolean`</td><td>`false`</td><td>Whether the `end` ID is inclusive.</td></tr>
    </tbody>
</table>

```kotlin title="Example"
val range = RecordIdRange("person", start = "a", end = "m", includeEnd = true)

client.select(range).awaitAs<List<Person>>()
```

## Learn more

- [Value types](../../concepts/value-types.md)
- [`RecordId`](record-id.md) and [`Table`](table.md)
- [Record ranges](https://surrealdb.com/docs/surrealql/datamodel/ids#record-ranges) in SurrealQL
