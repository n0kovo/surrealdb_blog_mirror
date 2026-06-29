---
position: 4
title: Datetime
description: Datetime wrapper for SurrealDB datetime values.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/api/values/datetime.mdx"
---

# `Datetime` {#datetime}

A `Datetime` wraps an ISO 8601 datetime string for use with SurrealDB's `datetime` type. It preserves the original string representation through serialization and deserialization.

```python title="Import"
from surrealdb import Datetime
```

---

## Constructor {#constructor}

```python title="Syntax"
Datetime(dt)
```

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`dt` *[required]*</td>
            <td>`str`</td>
            <td>An ISO 8601 datetime string.</td>
        </tr>
    </tbody>
</table>

### Examples

```python
dt = Datetime("2025-01-15T10:30:00Z")
```

```python
dt = Datetime("2025-06-01T14:00:00.000+02:00")
```

---

## Properties {#properties}

| Property | Type | Description |
|---|---|---|
| `dt` | `str` | The ISO 8601 datetime string. |

```python
dt = Datetime("2025-01-15T10:30:00Z")
print(dt.dt)  # "2025-01-15T10:30:00Z"
```

---

## Usage {#usage}

```python
from surrealdb import Surreal, RecordID, Datetime

db = Surreal("ws://localhost:8000")
db.connect()
db.use("my_ns", "my_db")
db.signin({"username": "root", "password": "root"})

db.create("events", {
    "title": "Launch",
    "scheduled_at": Datetime("2025-06-01T09:00:00Z"),
})
```

---

## See also

- [Data types](index.md), All SDK data types
- [Duration](duration.md), Duration type with unit conversion
