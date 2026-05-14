---
position: 17
title: Rand functions
description: These functions can be used when generating random data values.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/functions/database-functions/rand.mdx"
---

# Rand functions

These functions can be used when generating random data values.

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Function"><a href="#rand">`rand()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random floating point number</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randbool">`rand::bool()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random boolean</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randduration">`rand::duration()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randenum">`rand::enum()`</a></td>
      <td scope="row" data-label="Description">Randomly picks a value from the specified values</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randfloat">`rand::float()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random floating point number</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randid">`rand::id()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random id</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randint">`rand::int()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random integer</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randstring">`rand::string()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random string</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randtime">`rand::time()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random datetime</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randuuid">`rand::uuid()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random UUID</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randuuidv4">`rand::uuid::v4()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random Version 4 UUID</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#randulid">`rand::ulid()`</a></td>
      <td scope="row" data-label="Description">Generates and returns a random ULID</td>
    </tr>
  </tbody>
</table>

## `rand`

The rand function generates a random [`float`](../../language-primitives/data-types/numbers.md#floating-point-numbers), between 0 and 1.

```surql title="API DEFINITION"
rand() -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand();

0.7062321084863658
```

The following example shows this function being used in a [`SELECT`](../../statements/select.md) statement with an `ORDER BY` clause:

```surql
SELECT * FROM [{ age: 33 }, { age: 45 }, { age: 39 }] ORDER BY rand();

[
	{
		age: 45
	},
	{
		age: 39
	},
	{
		age: 33
	}
]
```

  

## `rand::bool`

The rand::bool function generates a random [`boolean`](../../language-primitives/data-types/booleans.md) value.

```surql title="API DEFINITION"
rand::bool() -> bool
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::bool();

true
```

  

## `rand::duration`

*Since v2.3.0*

The rand::duration function generates a random [`duration`](../../language-primitives/data-types/datetimes.md#durations-and-datetimes) value between two `duration` arguments.

```surql title="API DEFINITION"
rand::bool($from: duration, $to: duration) -> duration
```

Some examples of the function in use:

```surql
rand::duration(1ns, 1ms);

rand::duration(0ns, duration::max);
```

```surql title="Output"
-------- Query 1 --------
435µs884ns

-------- Query 2 --------
405337457164y36w2d5h54m8s16ms76µs191ns
```

  

## `rand::enum`

The `rand::enum` function generates a random value, from a multitude of values.

```surql title="API DEFINITION"
rand::enum(value...) -> any
rand::enum(array<value>) -> any
```

The argument to this function can take either comma-separated values or an array of values.

```surql
rand::enum('one', 'two', 3, 4.15385, 'five', true);
rand::enum(['one', 'two', 3, 4.15385, 'five', true]);

"five"
```

As nested values are not combined at greater levels of depth, the following example will return either `[8, 9]` or `[10, 11]`, but never an individual number.

```surql
RETURN rand::enum([
    [8,9],
    [10,11]
]);
```

  

## `rand::float`

The `rand::float` function generates a random [`float`](../../language-primitives/data-types/numbers.md#floating-point-numbers), between `0` and `1`.

```surql title="API DEFINITION"
rand::float() -> float
```

If two numbers are provided, then the function generates a random [`float`](../../language-primitives/data-types/numbers.md#floating-point-numbers), between two numbers.

```surql title="API DEFINITION"
rand::float($from: number, $to: number) -> float
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::float();

0.7812733136200293
```

```surql
RETURN rand::float(10, 15);

11.305355983514927
```

  

## `rand::id`

> [!NOTE]
> This function was known as `rand::guid` in versions of SurrealDB before 3.0.0-beta. The behaviour has not changed.

The `rand::id` function generates a random alphanumeric ID, defaulting to a length of 20 characters.

```surql title="API DEFINITION"
rand::id() -> string
```

If a number is provided, then the function generates a random ID with a specific length.

```surql title="API DEFINITION"
rand::id(number) -> string
```

If a second number is provided, then the function will generate a random id, with a length between the two numbers.

```surql title="API DEFINITION"
rand::id($min_len: int, $max_len: int) -> string
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql title="Default 20-char random id"
RETURN rand::id();

'4uqmrmtjhtjeg77et0dl'
```

```surql title="A 10-char random id"
RETURN rand::id(10);

'f3b6cjh0nt'
```

```surql title="A random id with a length between 1 and 9 chars"
RETURN rand::id(1, 9);

'894bqt4lp'
```

This function is used for default record ID keys in SurrealDB, and can be overridden to use a ULID or UUID instead by affixing `:ulid()` and `:uuid()` after the table name, respectively.

```surql
CREATE 
  person,
  person:ulid(),
  person:uuid()
-- Return only id values for nicer output
RETURN VALUE id;
```

Output:

```surql
[
	person:o9s1sl3ivckuxo0kglix,
	person:01K7JRP6KVAQGN2THR2T13X9WP,
	person:u'0199e58b-1a7b-7880-ad5b-01671678c11f'
]
```

  

## `rand::int`

The `rand::int` function generates a random int.

```surql title="API DEFINITION"
rand::int() -> int
```

If two numbers are provided, then the function generates a random int between two numbers.

```surql title="API DEFINITION"
rand::int($from: int, $to: int) -> int
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::int();

6841551695902514727
```

```surql
RETURN rand::int(10, 15);

13
```

  

## `rand::string`

The `rand::string` function generates a random string, with 32 characters.

```surql title="API DEFINITION"
rand::string() -> string
```

The `rand::string` function generates a random string, with a specific length.

```surql title="API DEFINITION"
rand::string(number) -> string
```

If two numbers are provided, then the function generates a random string, with a length between two numbers.

```surql title="API DEFINITION"
rand::string($from: int, $to: int) -> string
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::string();

"N8Q86mklN6U7kv0A2XCRh5UlpQMSvdoT"
```

```surql
RETURN rand::string(15);

"aSCtrfJj4pSJ7Xq"
```

```surql
RETURN rand::string(10, 15);

"rEUWFUMcx0YH"
```

  

## `rand::time`

The `rand::time` function generates a random [`datetime`](../../language-primitives/data-types/datetimes.md).

```surql title="API DEFINITION"
rand::time() -> datetime
rand::time($from: datetime|number, $to: datetime|number) -> datetime
```

The rand::time function generates a random [`datetime`](../../language-primitives/data-types/datetimes.md), either a completely random datetime when no arguments are passed in, or between two unix timestamps.

```surql
RETURN rand::time();

-- d'1327-07-12T01:00:32Z'

RETURN rand::time(198371, 1223138713);

-- d'1991-01-13T23:27:17Z'
```

*Since v2.2.0*

This function can take two datetimes, returning a random datetime in between the least and greatest of the two.

```surql
RETURN rand::time(d'1970-01-01', d'2000-01-01');

-- d'1999-05-29T17:02:16Z"
```

*Since v2.3.0*

Either of the arguments of this function can now be either a number or a datetime.

```surql
RETURN rand::time(0, d'1990-01-01');

-- d'1986-11-17T15:06:01Z'
```

As of this version, this function returns a datetime between 0000-01-01T00:00:00Z and 9999-12-31T23:59:59Z. Before this, the function returned a random datetime between 1970-01-01T00:00:00Z (0 seconds after the UNIX epoch) and +262142-12-31T23:59:59Z (the maximum possible value for a `datetime`).

## `rand::uuid`

The `rand::uuid` function generates a random Version 7 UUID.

```surql title="API DEFINITION"
rand::uuid() -> uuid
rand::uuid(datetime) -> uuid
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::uuid();

[u"e20b2836-e689-4643-998d-b17a16800323"]
```

The `rand::uuid` function can also generate a random UUID from a datetime.

```surql
RETURN rand::uuid(d"2021-09-07T04:27:53Z");
```

Note that a UUID has a precision of one millisecond, and thus one converted back to a datetime will truncate nanosecond precision.

```surql
LET $now = time::now();
[$now, time::from_uuid(rand::uuid($now))];

-- Output:
[
	d'2026-01-29T02:14:10.057075Z',
	d'2026-01-29T02:14:10.057Z'
]
```

The `rand::uuid` function can also be called using its alias `rand::uuid::v7`.

  

## `rand::uuid::v4`

The `rand::uuid::v4` function generates a random version 4 UUID.

```surql title="API DEFINITION"
rand::uuid::v4() -> uuid
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::uuid::v4();

[u"4def23a5-a847-4934-8dad-c64ccc48921b"]
```

  

## `rand::ulid`

The `rand::ulid` function generates a random ULID.

```surql title="API DEFINITION"
rand::ulid() -> uuid
rand::ulid(datetime) -> uuid
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::ulid();

[u"01H9QDG81Q7SB33RXB7BEZBK7G"]
```

The `rand::ulid` function can also generate a random ULID from a datetime type.

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN rand::ulid(d"2021-09-07T04:27:53Z");
```

Note that a ULID has a precision of one millisecond, and thus one converted back to a datetime will truncate nanosecond precision.

```surql
LET $now = time::now();
[$now, time::from_ulid(rand::ulid($now))];

-- Output:
[
	d'2026-01-29T02:14:10.057075Z',
	d'2026-01-29T02:14:10.057Z'
]
```
