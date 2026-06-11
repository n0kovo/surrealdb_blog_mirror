---
position: 5
title: Datetime
description: "SurrealDB datetime values map to Java's ZonedDateTime class."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/api/values/datetime.mdx"
---

# Datetime {#datetime}

SurrealDB [`datetime`](../../../../reference/query-language/language-primitives/data-types/datetimes.md) values map to Java's `java.time.ZonedDateTime`. The SDK handles conversion automatically when deserializing query results into [`Value`](value.md) objects or POJOs.

---

## Value methods

### `.isDateTime()` {#is-datetime}

Checks if the value is a datetime.

```java title="Method Syntax"
value.isDateTime()
```

**Returns:** `boolean`

### `.getDateTime()` {#get-datetime}

Returns the datetime as a `ZonedDateTime`.

```java title="Method Syntax"
value.getDateTime()
```

**Returns:** `java.time.ZonedDateTime`

---

## POJO mapping

When using typed methods, datetime fields in your POJO should be declared as `ZonedDateTime` for reads unless you need a narrower type (`Instant`, `OffsetDateTime`, or `LocalDateTime`). When writing records, you can also use those types plus `java.util.Date` — see [Class converters](../../concepts/class-converters.md#temporal-types).

```java

public class Event {
    public RecordId id;
    public String title;
    public ZonedDateTime createdAt;

    public Event() {}
}

Optional<Event> event = db.select(Event.class, new RecordId("event", "conf"));
ZonedDateTime when = event.get().createdAt;
```

---

## Example

```java title="Working with datetime values"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    Response response = db.query("RETURN time::now()");
    Value result = response.take(0);

    if (result.isDateTime()) {
        ZonedDateTime now = result.getDateTime();
    }
}
```

---

## See also

- [Value types](../../concepts/value-types.md) — Type mapping overview
- [Value](value.md) — The Value class reference
- [SurrealQL datetimes](../../../../reference/query-language/language-primitives/data-types/datetimes.md) — Datetime types in SurrealDB
