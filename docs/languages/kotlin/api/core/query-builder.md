---
position: 4
title: Query builders
description: The fluent query builders, expression helpers, and surql DSL of the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/api/core/query-builder.mdx"
---

# Query builders {#query-builders}

The CRUD methods on [`SurrealClient`](surreal-client.md) return fluent builders that compile to [SurrealQL](../../../../reference/query-language/index.md). Each builder is refined with chainable methods and terminated with [`await()`](#await) (raw [`JsonElement`](../values/value.md)) or the typed [`awaitAs<T>()`](#await-as) extension.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Terminal methods

### `.await()` {#await}

Executes the builder and returns the unwrapped result of the first statement as a [`JsonElement`](../values/value.md).

```kotlin title="Method Syntax"
builder.await()
```

**Returns:** `JsonElement`

### `.awaitRaw()` {#await-raw}

Executes the builder and returns the raw `[{ status, result, time, type }]` response envelope.

```kotlin title="Method Syntax"
builder.awaitRaw()
```

**Returns:** `JsonElement`

### `.awaitAs<T>()` {#await-as}

An inline extension that executes the builder and decodes the result into `T` using [`kotlinx.serialization`](../../concepts/serialization.md). Available on every builder.

```kotlin title="Method Syntax"
builder.awaitAs<T>()
```

**Returns:** `T`

```kotlin title="Example"
val people: List<Person> = client.select(Table("person")).awaitAs()
```

### `.compile()` {#compile}

Compiles the builder to a `BoundQuery` without executing it — useful for inspection or composing with [`.query()`](surreal-client.md#query).

```kotlin title="Method Syntax"
builder.compile()
```

**Returns:** `BoundQuery`

---

## `SelectQuery` {#select-query}

Returned by [`.select(what)`](surreal-client.md#select).

<table>
    <thead>
        <tr><th>Method</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td id="fields">`.fields(vararg names)`</td><td>Selects specific fields.</td></tr>
        <tr><td>`.value(field)`</td><td>Selects a single field's value.</td></tr>
        <tr><td id="where">`.where(expr)`</td><td>Filters with an <a href="#expressions">expression</a>.</td></tr>
        <tr><td id="start">`.start(n)`</td><td>Skips the first `n` records.</td></tr>
        <tr><td id="limit">`.limit(n)`</td><td>Limits the number of records.</td></tr>
        <tr><td id="fetch">`.fetch(vararg fields)`</td><td>Fetches related records.</td></tr>
        <tr><td>`.timeout(seconds)`</td><td>Sets a query timeout.</td></tr>
        <tr><td>`.version(literal)`</td><td>Reads at a specific version.</td></tr>
    </tbody>
</table>

```kotlin title="Example"
val adults: List<Person> = client
    .select(Table("person"))
    .where(field("age") gte 18)
    .limit(50)
    .awaitAs()
```

## Content builders

[`CreateQuery`](surreal-client.md#create), [`UpdateQuery`](surreal-client.md#update), [`UpsertQuery`](surreal-client.md#upsert), and [`RelateQuery`](surreal-client.md#relate) accept content and a return mode.

<table>
    <thead>
        <tr><th>Method</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`.content(data)`</td><td>Sets the record content (a `JsonElement`).</td></tr>
        <tr><td>`.where(expr)`</td><td>Filters affected records (update, upsert, merge, patch, delete).</td></tr>
        <tr><td id="return-mode">`.returnMode(mode)`</td><td>Controls the returned payload (see <a href="#return-mode-type">ReturnMode</a>).</td></tr>
    </tbody>
</table>

## `ReturnMode` {#return-mode-type}

```kotlin title="Import"
```

<table>
    <thead>
        <tr><th>Value</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`ReturnMode.None`</td><td>Returns nothing.</td></tr>
        <tr><td>`ReturnMode.Before`</td><td>Returns records as they were before the change.</td></tr>
        <tr><td>`ReturnMode.After`</td><td>Returns records after the change.</td></tr>
        <tr><td>`ReturnMode.Diff`</td><td>Returns a JSON Patch diff.</td></tr>
        <tr><td>`ReturnMode.Fields(names)`</td><td>Returns only the named fields.</td></tr>
    </tbody>
</table>

## `RunQuery` {#run-query}

Returned by [`.run(function)`](surreal-client.md#run).

<table>
    <thead>
        <tr><th>Method</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`.args(vararg args)`</td><td>Sets the function arguments.</td></tr>
        <tr><td>`.version(version)`</td><td>Selects a function version.</td></tr>
    </tbody>
</table>

---

## Expression helpers {#expressions}

Build `WHERE` expressions with the helper functions and infix operators from `com.surrealdb.kotlin.query`.

```kotlin title="Import"
```

<table>
    <thead>
        <tr><th>Helper</th><th>SurrealQL</th></tr>
    </thead>
    <tbody>
        <tr><td>`field(name)`</td><td>A validated field reference.</td></tr>
        <tr><td>`value(any)`</td><td>A literal value.</td></tr>
        <tr><td>`raw(boundQuery)`</td><td>A raw fragment.</td></tr>
        <tr><td>`a eq b`</td><td>`=`</td></tr>
        <tr><td>`a neq b`</td><td>`!=`</td></tr>
        <tr><td>`a lt b`</td><td>`&lt;`</td></tr>
        <tr><td>`a lte b`</td><td>`&lt;=`</td></tr>
        <tr><td>`a gt b`</td><td>`&gt;`</td></tr>
        <tr><td>`a gte b`</td><td>`&gt;=`</td></tr>
        <tr><td>`a contains b`</td><td>`CONTAINS`</td></tr>
        <tr><td>`a inside b`</td><td>`IN`</td></tr>
        <tr><td>`a and b`</td><td>`AND`</td></tr>
        <tr><td>`a or b`</td><td>`OR`</td></tr>
        <tr><td>`not(expr)`</td><td>`!`</td></tr>
    </tbody>
</table>

> [!NOTE]
> Inequality is `neq` (not `ne`) and membership is `inside` (not `in`, which is a reserved Kotlin keyword).

```kotlin title="Example"

val expr = (field("age") gte 18) and (field("active") eq true)
val results = client.select(Table("person")).where(expr).awaitAs<List<Person>>()
```

---

## `surql` DSL {#surql}

The `surql` helpers build a parameterised `BoundQuery` with automatic, injection-safe binding of values and record identifiers.

```kotlin title="Import"
```

```kotlin title="Example"
// Vararg bindings
val a = surql("SELECT * FROM person WHERE age > \$min", "min" to 25)

// Builder block
val b = surql {
    +"SELECT * FROM person WHERE age > "
    param("min", 25)
}

val result = client.query(a)
```

## Learn more

- [SurrealClient API reference](surreal-client.md) for the CRUD methods
- [Data manipulation](../../concepts/data-manipulation.md) for the concepts
- [Serialization](../../concepts/serialization.md) for `awaitAs`
