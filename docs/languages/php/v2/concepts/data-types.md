---
position: 4
title: Data types
description: How version 2 of the PHP SDK maps SurrealQL data types to native PHP types and custom value classes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v2/concepts/data-types.mdx"
---

# Data types

SurrealDB has types that PHP does not, such as record IDs, nanosecond datetimes, durations, and arbitrary-precision decimals. Version 2 of the SDK represents these with value classes in the `SurrealDB\SDK\Types` namespace. Native PHP types pass through unchanged.

## Type mapping

| SurrealQL type | PHP type |
|----------------|----------|
| `bool` | `bool` |
| `int`, `float` | `int`, `float` |
| `string` | `string` |
| `null` | `null` |
| `none` | [`None`](../api/data-types.md#none) |
| `array` | `array` (list) |
| `object` | `array` (associative) |
| `set` | [`Set`](../api/data-types.md#set) |
| `bytes` | [`Bytes`](../api/data-types.md#bytes) |
| `datetime` | [`DateTime`](../api/data-types.md#datetime) |
| `duration` | [`Duration`](../api/data-types.md#duration) |
| `decimal` | [`Decimal`](../api/data-types.md#decimal) |
| `uuid` | [`Uuid`](../api/data-types.md#uuid) |
| `record` | [`RecordId`](../api/data-types.md#recordid) |
| `range` | [`Range`](../api/data-types.md#range) |
| `geometry` | [`Geometry`](../api/data-types.md#geometry) types |
| `file` | [`File`](../api/data-types.md#file) |

## Record IDs and tables

A [`RecordId`](../api/data-types.md#recordid) is a table name plus an ID. A [`Table`](../api/data-types.md#table) is a table reference on its own. The query builders accept either, so the SDK can tell a record from a table.

```php
use SurrealDB\SDK\Types\RecordId;
use SurrealDB\SDK\Types\Table;

$tobie = new RecordId('person', 'tobie');
$people = new Table('person');

$record = $db->select($tobie)->execute();
$all = $db->select($people)->execute();
```

The ID can be a string, integer, array, or object for composite keys.

```php
$metric = new RecordId('metric', ['service' => 'api', 'host' => 'server-01']);
```

To send a record ID that is already a string, wrap it in `StringRecordId` so the server parses it.

```php
use SurrealDB\SDK\Types\StringRecordId;

$db->select(new StringRecordId('person:tobie'))->execute();
```

## Datetimes and durations

A [`DateTime`](../api/data-types.md#datetime) keeps nanosecond precision, which PHP's native `DateTime` does not. A [`Duration`](../api/data-types.md#duration) follows SurrealQL duration syntax.

```php
use SurrealDB\SDK\Types\DateTime;
use SurrealDB\SDK\Types\Duration;

$now = DateTime::now();
$parsed = DateTime::fromString('2024-01-15T12:00:00.123456789Z');

$ttl = Duration::fromString('1h30m');
```

## Decimals

A [`Decimal`](../api/data-types.md#decimal) holds a number without floating-point rounding. Construct it from a string when precision matters.

```php
use SurrealDB\SDK\Types\Decimal;

$price = new Decimal('19.99');
```

## UUIDs

A [`Uuid`](../api/data-types.md#uuid) represents a universally unique identifier, with helpers for v4 (random) and v7 (time-ordered).

```php
use SurrealDB\SDK\Types\Uuid;

$random = Uuid::v4();
$timeOrdered = Uuid::v7();
```

## Geometries

The SDK provides classes for every [GeoJSON geometry type](../../../../reference/query-language/language-primitives/data-types/geometries.md): `GeometryPoint`, `GeometryLine`, `GeometryPolygon`, `GeometryMultiPoint`, `GeometryMultiLine`, `GeometryMultiPolygon`, and `GeometryCollection`.

```php
use SurrealDB\SDK\Types\GeometryPoint;
use SurrealDB\SDK\Types\GeometryLine;

$point = new GeometryPoint(-0.118092, 51.509865);
$line = new GeometryLine(
    new GeometryPoint(0, 0),
    new GeometryPoint(1, 1),
);
```

## Learn more

- [Data types API reference](../api/data-types.md) for every value class and its methods
- [SurrealQL data model](https://surrealdb.com/docs/reference/query-language/datamodel) for the database type system
