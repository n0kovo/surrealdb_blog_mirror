---
position: 6
title: Duration
description: "SurrealDB duration values map to Java's Duration class."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/api/values/duration.mdx"
---

# Duration {#duration}

SurrealDB [`duration`](../../../../reference/query-language/language-primitives/data-types/datetimes.md#durations-and-datetimes) values map to Java's `java.time.Duration`. The SDK handles conversion automatically when deserializing query results into [`Value`](value.md) objects or POJOs.

---

## Value methods

### `.isDuration()` {#is-duration}

Checks if the value is a duration.

```java title="Method Syntax"
value.isDuration()
```

**Returns:** `boolean`

### `.getDuration()` {#get-duration}

Returns the duration as a `java.time.Duration`.

```java title="Method Syntax"
value.getDuration()
```

**Returns:** `java.time.Duration`

---

## POJO mapping

When using typed methods, duration fields in your POJO should be declared as `Duration`.

```java

public class Task {
    public RecordId id;
    public String name;
    public Duration timeout;

    public Task() {}
}

Optional<Task> task = db.select(Task.class, new RecordId("task", "build"));
Duration timeout = task.get().timeout;
```

---

## Example

```java title="Working with duration values"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    Response response = db.query("RETURN 1h30m");
    Value result = response.take(0);

    if (result.isDuration()) {
        Duration d = result.getDuration();
    }
}
```

---

## See also

- [Value types](../../concepts/value-types.md) — Type mapping overview
- [Value](value.md) — The Value class reference
- [SurrealQL durations](../../../../reference/query-language/language-primitives/data-types/datetimes.md#durations-and-datetimes) — Duration types in SurrealDB
