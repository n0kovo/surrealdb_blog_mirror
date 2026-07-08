---
position: 4
title: Geometry
description: The Geometry class represents SurrealDB geometric data types.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/api/values/geometry.mdx"
---

# `Geometry` {#geometry}

The `Geometry` class represents [SurrealDB geometric data types](../../../query-language/language-primitives/data-types/geometries.md). It currently supports point geometry, mapping to Java's `Point2D.Double` from `java.awt.geom`.

**Source:** [surrealdb.java](https://github.com/surrealdb/surrealdb.java)

---

## Methods

### `.isPoint()` {#is-point}

Checks if the geometry value is a point.

```java title="Method Syntax"
geometry.isPoint()
```

**Returns:** `boolean`

### `.getPoint()` {#get-point}

Returns the point coordinates as a `Point2D.Double`. The `x` coordinate represents longitude and `y` represents latitude.

```java title="Method Syntax"
geometry.getPoint()
```

**Returns:** `Point2D.Double` (`java.awt.geom`)

---

## Example

```java title="Working with geometry values"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    Response response = db.query(
        "RETURN <geometry> { type: 'Point', coordinates: [10.0, 20.0] }"
    );
    Value result = response.take(0);
    Geometry geo = result.getGeometry();

    if (geo.isPoint()) {
        Point2D.Double point = geo.getPoint();
    }
}
```

---

## See also

- [Value types](../../concepts/value-types.md) — Type mapping overview
- [Value](value.md) — The Value class reference
- [SurrealQL geometries](../../../query-language/language-primitives/data-types/geometries.md) — Geometry types in SurrealDB
