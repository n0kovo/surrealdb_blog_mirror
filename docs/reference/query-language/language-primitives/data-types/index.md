---
position: 1
title: Data types
description: SurrealQL allows you to describe data with specific data types. These data types are used to validate data and to generate the appropriate database schema.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/language-primitives/data-types/index.mdx"
---

# Types

SurrealQL allows you to describe data with specific data types. These data types are used to validate data and to generate the appropriate database schema.

## Data types

<table>
    <thead>
        <tr>
            <th scope="col">Type</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Type">
                `any`
            </td>
            <td scope="row" data-label="Description">
                Use this when you explicitly don't want to specify the field's data type. The field will allow any data type supported by SurrealDB.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`array`](arrays.md)
            </td>
            <td scope="row" data-label="Description">
                An array of items.
                The array type also allows you to define which types can be stored in the array and the required length.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`bool`](booleans.md)
            </td>
            <td scope="row" data-label="Description">
                A value that can be either `true` or `false`.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                <a href="#bytes">[`bytes`](bytes.md)</a>
            </td>
            <td scope="row" data-label="Description">
                Stores a value in a byte array.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`datetime`](datetimes.md)
            </td>
            <td scope="row" data-label="Description">
                An [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) compliant data type that stores a date with time and time zone.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`decimal`](numbers.md#decimal-numbers)
            </td>
            <td scope="row" data-label="Description">
               Data type for storing [decimal floating point](https://en.wikipedia.org/wiki/Decimal128_floating-point_format) numbers.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`duration`](durations.md)
            </td>
            <td scope="row" data-label="Description">
                Store a value representing a length of time. Can be added or subtracted from datetimes or other durations.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`float`](numbers.md#floating-point-numbers)
            </td>
            <td scope="row" data-label="Description">
                Data type for storing [floating point](https://en.wikipedia.org/wiki/Double-precision_floating-point_format) numbers. Larger or extremely precise values should be stored as a decimal.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                <a href="#geometry">`geometry`</a>
            </td>
            <td scope="row" data-label="Description">
                <a href="https://www.rfc-editor.org/rfc/rfc7946" target="_blank" rel="noopener noreferrer" title="Link to RFC 7946">RFC 7946</a> compliant data type for storing geometry in the <a href="https://geojson.org/" target="_blank" rel="noopener noreferrer" title="Link to the GeoJson website">GeoJson format</a>.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`int`](numbers.md#integer-numbers)
            </td>
            <td scope="row" data-label="Description">
                Store a value in a 64 bit signed integer. Values can range between `-9223372036854775808` and `9223372036854775807` (inclusive). Larger values should be stored as a float or a decimal.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`number`](numbers.md)
            </td>
            <td scope="row" data-label="Description">
                Store numbers without specifying the type.
                SurrealDB will detect the type of number and store it using the minimal number of bytes.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`object`](https://surrealdb.com/docs/reference/query-language/language-primitives/data-types/object)
            </td>
            <td scope="row" data-label="Description">
                Store formatted objects containing values of any supported type including nested objects or arrays.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`range`](ranges.md)
            </td>
            <td scope="row" data-label="Description">
                A range of possible values. Lower and upper bounds can be set, in the absence of which the range becomes open-ended. A range of integers can be used in a FOR loop.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`regex`](regex.md)
            </td>
            <td scope="row" data-label="Description">
                A regular expression that can be used for matching strings.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`record`](record-ids.md)
            </td>
            <td scope="row" data-label="Description">
                A record ID. Table names can be added inside angle brackets to restrict to certain table names.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                [`set`](sets.md)
            </td>
            <td scope="row" data-label="Description">
                A set of items.
                The set type also allows you to define which types can be stored in the set and the required length.
                Items are automatically deduplicated and orderd.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
            [`string`](strings.md)
            </td>
            <td scope="row" data-label="Description">
                A value composed of text or text-like characters such as emojis.
            </td>
        </tr>
    </tbody>
</table>

### Examples

Examples of the `geometry` type:

```surql
-- Define a field with a single type
DEFINE FIELD location ON TABLE restaurant TYPE geometry<point>;
-- Define a field with any geometric type
DEFINE FIELD area ON TABLE restaurant TYPE geometry<feature>;
-- Define a field with specific geometric types
DEFINE FIELD area ON TABLE restaurant
    TYPE geometry<polygon|multipolygon|collection>;
```

Examples of the `bytes` type:

```surql
-- Define a field with a single type
DEFINE FIELD image ON TABLE product TYPE bytes;

-- Create a record with a bytes field and set the value
CREATE foo SET value = <bytes>"bar";
```

## Type expressions

Type expressions are not standalone types, but expressions to indicate which types are permitted.

<table>
    <thead>
        <tr>
            <th scope="col">Type</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Type">
                [literal](literals.md)
            </td>
            <td scope="row" data-label="Description">
                A value that may have multiple representations or formats, similar to an enum or a union type. Can be composed of strings, numbers, objects, arrays, or durations.
            </td>
        </tr>
        <tr>
            <td scope="row" data-label="Type">
                `option`
            </td>
            <td scope="row" data-label="Description">
                Makes types optional and guarantees the field to be either empty (NONE) or some other type. Syntactic sugar for `type_name | NONE`.
            </td>
        </tr>
    </tbody>
</table>

### Examples

Example of an `option` in a schema:

```surql
DEFINE FIELD friends ON TABLE person TYPE option<array<person>>;
```

Example of a literal type:

```surql
DEFINE FIELD error_msg ON TABLE log TYPE 
    { code: 200, message: string } | 
    { code: 404, message: string };
```

As an option is syntactic sugar for `type | NONE`, an option is also simply another type of literal. This field definition is identical to the `option` example above.

```surql
DEFINE FIELD friends ON TABLE person TYPE array<person> | NONE;
```
