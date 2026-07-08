---
position: 8
title: Range
description: SurrealDB range values are accessed through Value methods for start and end bounds.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/api/values/range.mdx"
---

# Range {#range}

SurrealDB range values represent a bounded interval. In the Java SDK, ranges are accessed through [`Value`](value.md) methods that return the start and end bounds.

> [!NOTE]
> For record ID ranges used in CRUD operations (select, update, delete), see [`RecordIdRange`](record-id.md#record-id-range).

---

## Value methods

### `.isRange()` {#is-range}

Checks if the value is a range.

```java title="Method Syntax"
value.isRange()
```

**Returns:** `boolean`

### `.getRangeStart()` {#get-range-start}

Returns the start bound of the range, if present.

```java title="Method Syntax"
value.getRangeStart()
```

**Returns:** `Optional<`[`Value`](value.md)`>`

### `.getRangeEnd()` {#get-range-end}

Returns the end bound of the range, if present.

```java title="Method Syntax"
value.getRangeEnd()
```

**Returns:** `Optional<`[`Value`](value.md)`>`

---

## Example

```java title="Working with range values"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    Response response = db.query("RETURN 1..10");
    Value result = response.take(0);

    if (result.isRange()) {
        Optional<Value> start = result.getRangeStart();
        Optional<Value> end = result.getRangeEnd();
    }
}
```

---

## See also

- [Value types](../../concepts/value-types.md) — Type mapping overview
- [Value](value.md) — The Value class reference
- [RecordIdRange](record-id.md#record-id-range) — Range-based CRUD operations
