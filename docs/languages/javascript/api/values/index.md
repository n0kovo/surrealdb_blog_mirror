---
position: 1
title: Data types
description: Type mapping between SurrealQL and JavaScript, and custom data type classes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/api/values/index.mdx"
---

# Data Types

The JavaScript SDK provides custom classes for SurrealDB-specific data types, ensuring type safety and data integrity when working with the database. For a conceptual overview with usage examples and best practices, see the [Value types concept page](https://surrealdb.com/docs/sdk/javascript/concepts/value-types).

## Custom Data Type Classes

- [**RecordId**](https://surrealdb.com/docs/sdk/javascript/api/values/record-id) - Type-safe record identifiers with table and ID components
  - `new RecordId(table, id)` - Create record ID
  - Also includes `RecordIdRange` for querying ranges

- [**Table**](https://surrealdb.com/docs/sdk/javascript/api/values/table) - Type-safe table references
  - `new Table<T>(name)` - Create typed table reference
  - Used in SELECT, CREATE, UPDATE, DELETE operations

- [**DateTime**](https://surrealdb.com/docs/sdk/javascript/api/values/datetime) - Datetime values with nanosecond precision
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

- [**Range**](https://surrealdb.com/docs/sdk/javascript/api/values/range) - Generic range values for numeric and date ranges

- [**FileRef**](https://surrealdb.com/docs/sdk/javascript/api/values/file-ref) - References to files stored in SurrealDB
  - `.bucket` - Storage bucket name
  - `.key` - File key within the bucket

## Geometric Types

- [**Geometry**](geometry.md) - Spatial/geometric data types
  - `GeometryPoint` - Single point
  - `GeometryLine` - Line between points
  - `GeometryPolygon` - Polygon shape
  - `GeometryMultiPoint`, `GeometryMultiLine`, `GeometryMultiPolygon`
  - `GeometryCollection` - Mixed geometry collection

## See Also

- [Value types concept page](https://surrealdb.com/docs/sdk/javascript/concepts/value-types) - Usage guide with type mapping, examples, and best practices
- [SurrealQL Data Types](https://surrealdb.com/docs/surrealql/datamodel) - Database data model
- [Utilities](https://surrealdb.com/docs/sdk/javascript/concepts/utilities) - Comparing and converting values
