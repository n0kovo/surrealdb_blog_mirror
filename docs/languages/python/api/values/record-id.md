---
position: 2
title: RecordID
description: Record identifier with table name and ID components.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/python/api/values/record-id.mdx"
---

# `RecordID` {#recordid}

A `RecordID` represents a unique record identifier in SurrealDB, combining a table name with an ID value. It is the Python equivalent of SurrealDB's `record` type.

```python title="Import"
from surrealdb import RecordID
```

**Source:** [record_id.py](https://github.com/surrealdb/surrealdb.py/blob/main/src/surrealdb/data/types/record_id.py)

---

## Constructor {#constructor}

```python title="Syntax"
RecordID(table_name, identifier)
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
            <td>`table_name` *[required]*</td>
            <td>`str`</td>
            <td>The name of the table this record belongs to.</td>
        </tr>
        <tr>
            <td>`identifier` *[required]*</td>
            <td>`Any`</td>
            <td>The unique identifier for the record within the table.</td>
        </tr>
    </tbody>
</table>

### Examples

```python title="String ID"
record = RecordID("users", "john")
```

```python title="Numeric ID"
record = RecordID("products", 42)
```

```python title="List ID"
record = RecordID("events", ["2025", "01", "01"])
```

---

## Static methods {#static-methods}

### `RecordID.parse()` {#parse}

Parses a record ID from its string representation.

```python title="Syntax"
RecordID.parse(record_str)
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
            <td>`record_str` *[required]*</td>
            <td>`str`</td>
            <td>A record ID string in `table_name:id` format.</td>
        </tr>
    </tbody>
</table>

**Returns:** `RecordID`

```python
record = RecordID.parse("users:john")
print(record.table_name)  # "users"
print(record.id)          # "john"
```

---

## Properties {#properties}

| Property | Type | Description |
|---|---|---|
| `table_name` | `str` | The table name component of the record ID. |
| `id` | [`Value`](index.md#value) | The identifier component of the record ID. |

```python
record = RecordID("users", "john")
print(record.table_name)  # "users"
print(record.id)          # "john"
```

---

## Methods {#methods}

### `__str__()` {#str}

Returns the string representation in `table_name:id` format.

```python
record = RecordID("users", "john")
print(str(record))  # "users:john"
```

### `__eq__()` {#eq}

Compares two `RecordID` instances for equality based on both `table_name` and `id`.

```python
a = RecordID("users", "john")
b = RecordID("users", "john")
print(a == b)  # True
```

---

## Pydantic support {#pydantic}

When the `pydantic` extra is installed (`pip install surrealdb[pydantic]`), `RecordID` can be used as a field type in Pydantic models with automatic validation and serialization.

```python
from pydantic import BaseModel
from surrealdb import RecordID

class User(BaseModel):
    id: RecordID
    name: str

user = User(id=RecordID("users", "john"), name="John")
```

---

## `RecordIdType` {#recordidtype}

Methods that accept a record or table reference use the `RecordIdType` alias, which accepts a plain string, a [`Table`](table.md), or a `RecordID`.

```python title="Type Definition"
RecordIdType = str | Table | RecordID
```

See the [Data types overview](index.md#recordidtype) for details.

---

## See also

- [Data types](index.md) — All SDK data types
- [Table](table.md) — Table name wrapper
- [Surreal](../core/surreal.md) — Connection and query methods
