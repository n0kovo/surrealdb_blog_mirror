---
position: 5
title: Value types
description: The Python SDK provides custom types for representing SurrealDB-specific values like record identifiers, durations, and geometry.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/concepts/value-types.mdx"
---

# Value types

The Python SDK maps SurrealDB data types to Python types automatically. Standard Python types like `str`, `int`, `float`, `bool`, `None`, `dict`, and `list` map directly to their SurrealDB equivalents. For SurrealDB-specific types such as record identifiers, durations, and geometry, the SDK provides dedicated Python classes.

See the [Data Types reference](../api/values/index.md) for the full API details of each type.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Class</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/python/api/values/record-id">`RecordID(table_name, identifier)`</a></td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/python/api/values/table">`Table(table_name)`</a></td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/python/api/values/duration">`Duration(elapsed)`</a></td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/python/api/values/datetime">`Datetime(dt)`</a></td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/python/api/values/range">`Range(begin, end)`</a></td>
		</tr>
		<tr>
			<td scope="row" data-label="Class"><a href="/docs/languages/python/api/values/geometry">`GeometryPoint(...)`</a></td>
		</tr>
	</tbody>
</table>

## Type mapping between Python and SurrealDB

The following table shows how Python types correspond to SurrealDB types. Standard library types are used directly, while SurrealDB-specific types use the custom classes listed above.

| Python Type | SurrealDB Type |
|---|---|
| `str` | `string` |
| `int` | `int` |
| `float` | `float` |
| `bool` | `bool` |
| `None` | `NONE` / `NULL` |
| `bytes` | `bytes` |
| `UUID` | `uuid` |
| `Decimal` | `decimal` |
| `dict` | `object` |
| `list` | `array` |
| [`RecordID`](../api/values/record-id.md) | `record` |
| [`Table`](../api/values/table.md) | `table` |
| [`Duration`](../api/values/duration.md) | `duration` |
| [`Datetime`](../api/values/datetime.md) | `datetime` |
| [`Range`](../api/values/range.md) | `range` |
| [`Geometry*`](../api/values/geometry.md) | `geometry` |

## Working with record identifiers

A [`RecordID`](../api/values/record-id.md) uniquely identifies a single record in a table by combining a table name with an identifier value. You can construct one directly or parse it from a string.

```python
from surrealdb import RecordID

record = RecordID("users", "tobie")
print(record.table_name)  # "users"
print(record.id)          # "tobie"

parsed = RecordID.parse("users:tobie")
print(parsed.table_name)  # "users"
```

The identifier can be a string, integer, list, or any other supported value type. Use `RecordID` wherever the SDK expects a record reference, such as in `.select()`, `.create()`, or `.delete()`.

```python
from surrealdb import Surreal, RecordID

with Surreal("ws://localhost:8000") as db:
    db.use("my_ns", "my_db")
    db.signin({"username": "root", "password": "root"})

    db.create(RecordID("users", "tobie"), {
        "name": "Tobie",
        "email": "tobie@surrealdb.com",
    })

    user = db.select(RecordID("users", "tobie"))
```

See the [RecordID reference](../api/values/record-id.md) for the complete API, including equality checks and Pydantic support.

## Working with durations

A [`Duration`](../api/values/duration.md) represents a time span with nanosecond precision. The most common way to create one is by parsing a human-readable string using SurrealDB's duration syntax.

```python
from surrealdb import Duration

d = Duration.parse("1h30m")
print(d.hours)    # 1.5
print(d.minutes)  # 90.0

d2 = Duration.parse("500ms")
print(d2.milliseconds)  # 500.0
```

You can also construct a `Duration` directly from nanoseconds and convert it back to a string.

```python
d = Duration(5_000_000_000)
print(d.seconds)      # 5.0
print(d.to_string())  # "5s"
```

Durations are useful for setting intervals, timeouts, and TTLs in your data.

```python
from surrealdb import Surreal, Duration

with Surreal("ws://localhost:8000") as db:
    db.use("my_ns", "my_db")
    db.signin({"username": "root", "password": "root"})

    db.create("tasks", {
        "title": "Backup",
        "interval": Duration.parse("6h"),
    })
```

See the [Duration reference](../api/values/duration.md) for all unit properties and methods.

## Working with datetime values

A [`Datetime`](../api/values/datetime.md) wraps an ISO 8601 datetime string for use with SurrealDB's `datetime` type. It preserves the original string representation through serialization and deserialization.

```python
from surrealdb import Datetime

dt = Datetime("2025-06-01T09:00:00Z")
print(dt.dt)  # "2025-06-01T09:00:00Z"
```

Use `Datetime` when creating records that contain date or time fields.

```python
from surrealdb import Surreal, Datetime

with Surreal("ws://localhost:8000") as db:
    db.use("my_ns", "my_db")
    db.signin({"username": "root", "password": "root"})

    db.create("events", {
        "title": "Launch",
        "scheduled_at": Datetime("2025-06-01T09:00:00Z"),
    })
```

See the [Datetime reference](../api/values/datetime.md) for the full API.

## Working with ranges

A [`Range`](../api/values/range.md) represents a bounded interval with inclusive or exclusive endpoints. Each bound is wrapped in a `BoundIncluded` or `BoundExcluded` to specify whether the boundary value is part of the range.

```python
from surrealdb import Range
from surrealdb.data.types.range import BoundIncluded, BoundExcluded

inclusive = Range(
    begin=BoundIncluded(1),
    end=BoundIncluded(10),
)

half_open = Range(
    begin=BoundIncluded(1),
    end=BoundExcluded(10),
)
```

Ranges are commonly used in query parameters to filter results within a specific interval.

```python
from surrealdb import Surreal, Range
from surrealdb.data.types.range import BoundIncluded

with Surreal("ws://localhost:8000") as db:
    db.use("my_ns", "my_db")
    db.signin({"username": "root", "password": "root"})

    result = db.query(
        "SELECT * FROM events WHERE year IN $range",
        {"range": Range(BoundIncluded(2020), BoundIncluded(2025))},
    )
```

See the [Range reference](../api/values/range.md) for the full API and bound types.

## Working with geometry types

The SDK provides seven GeoJSON-compatible geometry types for working with SurrealDB's spatial data: `GeometryPoint`, `GeometryLine`, `GeometryPolygon`, `GeometryMultiPoint`, `GeometryMultiLine`, `GeometryMultiPolygon`, and `GeometryCollection`.

The most common type is `GeometryPoint`, which represents a single geographic coordinate.

```python
from surrealdb import Surreal, GeometryPoint

with Surreal("ws://localhost:8000") as db:
    db.use("my_ns", "my_db")
    db.signin({"username": "root", "password": "root"})

    db.create("locations", {
        "name": "London",
        "coordinates": GeometryPoint(-0.1278, 51.5074),
    })
```

More complex types compose from simpler ones — a `GeometryLine` is built from a list of points, a `GeometryPolygon` from a list of lines, and so on. See the [Geometry reference](../api/values/geometry.md) for constructors and examples of all seven types.

## Learn more

- [Data Types reference](../api/values/index.md) for complete API details
- [RecordID reference](../api/values/record-id.md) for record identifier API
- [Duration reference](../api/values/duration.md) for duration API
- [Python types](../api/types/index.md) for Value and RecordIdType definitions
- [Data manipulation](data-manipulation.md) for using types in queries
