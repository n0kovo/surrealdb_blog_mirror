---
position: 2
title: Table
description: The Table type refers to a table by name in the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/kotlin/api/values/table.mdx"
---

# `Table` {#table}

`Table` refers to a table by name. Pass it to the [CRUD builders](../../concepts/data-manipulation.md) to target every record in the table.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Constructor

```kotlin title="Method Syntax"
Table(name)
```

<table>
    <thead>
        <tr><th>Parameter</th><th>Type</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`name` *[required]*</td><td>`String`</td><td>The table name.</td></tr>
    </tbody>
</table>

```kotlin title="Example"
val person = Table("person")

client.select(person).awaitAs<List<Person>>()
```

When bound into a query, a `Table` is rendered with `type::table(name)` so the value is always passed safely.

## Learn more

- [Value types](../../concepts/value-types.md)
- [`RecordId`](record-id.md) and [`RecordIdRange`](record-id-range.md)
