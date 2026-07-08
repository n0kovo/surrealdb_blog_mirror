---
position: 7
title: Table
description: SurrealDB table values map to Java strings via Value methods.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/api/values/table.mdx"
---

# Table {#table}

SurrealDB table values represent table names and are returned as `String` values in the Java SDK. The [`Value`](value.md) class provides methods to check for and extract table values.

---

## Value methods

### `.isTable()` {#is-table}

Checks if the value is a table name.

```java title="Method Syntax"
value.isTable()
```

**Returns:** `boolean`

### `.getTable()` {#get-table}

Returns the table name as a `String`.

```java title="Method Syntax"
value.getTable()
```

**Returns:** `String`

---

## Example

```java title="Working with table values"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    Response response = db.query("RETURN <table> 'person'");
    Value result = response.take(0);

    if (result.isTable()) {
        String tableName = result.getTable();
    }
}
```

---

## See also

- [Value types](../../concepts/value-types.md) — Type mapping overview
- [Value](value.md) — The Value class reference
- [SurrealQL tables](../../../query-language/statements/define/table.md) — Table definitions in SurrealDB
