---
position: 1
title: Data types
description: Type mapping between SurrealQL and JavaScript, and custom data type classes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/api/values/index.mdx"
---

# Data types

The JavaScript SDK provides custom classes for SurrealDB-specific data types, ensuring type safety and data integrity when working with the database. For a conceptual overview with usage examples and best practices, see the [Value types concept page](../../concepts/value-types.md).

## Custom data type classes

- [**RecordId**](record-id.md) - Type-safe record identifiers with table and ID components
  - `new RecordId(table, id)` - Create record ID
  - Also includes `RecordIdRange` for querying ranges

- [**Table**](table.md) - Type-safe table references
  - `new Table<T>(name)` - Create typed table reference
  - Used in SELECT, CREATE, UPDATE, DELETE operations

- [**DateTime**](datetime.md) - Datetime values with nanosecond precision
  - `DateTime.now()` - Current datetime
  - `new DateTime(string)` - Parse from ISO string
  - `.toDate()` - Convert to JavaScript Date

- [**Duration**](duration.md) - Time duration with support for multiple units
  - `new Duration('5h30m')` - Parse from string
  - `.milliseconds` - Get duration in milliseconds

- [**Decimal**](decimal.md) - Arbitrary precision decimal numbers
  - `new Decimal('19.99')` - Create precise decimal
  - Preserves precision during operations

- [**Uuid**](uuid.md) - Universally unique identifiers
  - `Uuid.v4()` - Generate random UUID
  - `Uuid.v7()` - Generate time-ordered UUID

- [**Range**](range.md) - Generic range values for numeric and date ranges

- [**FileRef**](file-ref.md) - References to files stored in SurrealDB
  - `.bucket` - Storage bucket name
  - `.key` - File key within the bucket

## Geometric types

- [**Geometry**](geometry.md) - Spatial/geometric data types
  - `GeometryPoint` - Single point
  - `GeometryLine` - Line between points
  - `GeometryPolygon` - Polygon shape
  - `GeometryMultiPoint`, `GeometryMultiLine`, `GeometryMultiPolygon`
  - `GeometryCollection` - Mixed geometry collection

## See also

- [Value types concept page](../../concepts/value-types.md) - Usage guide with type mapping, examples, and best practices
- [SurrealQL data types](../../../query-language/language-primitives/data-types/index.md) - Database data model
- [Utilities](../../concepts/utilities.md) - Comparing and converting values
