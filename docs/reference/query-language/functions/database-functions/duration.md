---
position: 7
title: Duration
description: Functions and constants for working with duration-related data.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/functions/database-functions/duration.mdx"
---

# Duration functions and consts

This page contains built-in functions and constants for converting between numeric and [duration](../../language-primitives/data-types/durations.md) data.

> [!NOTE]
> Since version 3.0.0-beta, the `::from::` functions (e.g. `duration::from::millis()`) now use underscores (e.g. `duration::from_millis()`) to better match the intent of the function and method syntax.

## Duration functions

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationdays">`duration::days()`</a></td>
      <td scope="row" data-label="Description">Counts how many days fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationhours">`duration::hours()`</a></td>
      <td scope="row" data-label="Description">Counts how many hours fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationmicros">`duration::micros()`</a></td>
      <td scope="row" data-label="Description">Counts how many microseconds fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationmillis">`duration::millis()`</a></td>
      <td scope="row" data-label="Description">Counts how many milliseconds fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationmins">`duration::mins()`</a></td>
      <td scope="row" data-label="Description">Counts how many minutes fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationnanos">`duration::nanos()`</a></td>
      <td scope="row" data-label="Description">Counts how many nanoseconds fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationsecs">`duration::secs()`</a></td>
      <td scope="row" data-label="Description">Counts how many seconds fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationweeks">`duration::weeks()`</a></td>
      <td scope="row" data-label="Description">Counts how many weeks fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationyears">`duration::years()`</a></td>
      <td scope="row" data-label="Description">Counts how many years fit in a duration</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_days">`duration::from_days()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of days into a duration that represents days</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_hours">`duration::from_hours()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of hours into a duration that represents hours</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_micros">`duration::from_micros()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of microseconds into a duration that represents microseconds</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_millis">`duration::from_millis()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of milliseconds into a duration that represents milliseconds</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_mins">`duration::from_mins()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of minutes into a duration that represents minutes</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_nanos">`duration::from_nanos()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of nanoseconds into a duration that represents nanoseconds</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_secs">`duration::from_secs()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of seconds into a duration that represents seconds</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#durationfrom_weeks">`duration::from_weeks()`</a></td>
      <td scope="row" data-label="Description">Converts a numeric amount of weeks into a duration that represents weeks</td>
    </tr>
  </tbody>
</table>

## Duration constants

<table>
  <thead>
    <tr>
      <th scope="col">Constant</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Constant"><a href="#durationmax">`duration::max`</a></td>
      <td scope="row" data-label="Description">Constant representing the greatest possible duration</td>
    </tr>
  </tbody>
</table>

## `duration::days`

The `duration::days` function counts how many days fit into a duration.

```surql title="API DEFINITION"
duration::days(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "21"

*/

RETURN duration::days(3w);

-- 21
```

  

## `duration::hours`

The `duration::hours` function counts how many hours fit into a duration.

```surql title="API DEFINITION"
duration::hours(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql

/**[test]

[[test.results]]
value = "504"

*/
RETURN duration::hours(3w);

-- 504
```

  

## `duration::max`

*Since v2.3.0*

The `duration::max` constant represents the greatest possible duration that can be used.

```surql title="API DEFINITION"
duration::max -> duration
```

Some examples of the constant in use:

```surql
/**[test]

[[test.results]]
value = "584942417355y3w5d7h15s999ms999µs999ns"

[[test.results]]
error = "'Failed to compute: "584942417355y3w5d7h15s999ms999µs999ns + 1ns", as the operation results in an arithmetic overflow.'"

[[test.results]]
value = "true"

*/

duration::max;

duration::max + 1ns;

100y IN 0ns..duration::max
```

```surql title="Output"
-------- Query 1 --------

584942417355y3w5d7h15s999ms999µs999ns

-------- Query 2 --------
'Failed to compute: "584942417355y3w5d7h15s999ms999µs999ns + 1ns", as the operation results in an arithmetic overflow.'

-------- Query 3 --------
true
```

  

## `duration::micros`

The `duration::micros` function counts how many microseconds fit into a duration.

```surql title="API DEFINITION"
duration::micros(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "1814400000000"

*/
RETURN duration::micros(3w);

-- 1814400000000
```

  

## `duration::millis`

The `duration::millis` function counts how many milliseconds fit into a duration.

```surql title="API DEFINITION"
duration::millis(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "1814400000"

*/
RETURN duration::millis(3w);

-- 1814400000
```

  

## `duration::mins`

The `duration::mins` function counts how many minutes fit into a duration.

```surql title="API DEFINITION"
duration::mins(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "30240"

*/
RETURN duration::mins(3w);

-- 30240
```

  

## `duration::nanos`

The `duration::nanos` function counts how many nanoseconds fit into a duration.

```surql title="API DEFINITION"
duration::nanos(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "1814400000000000"

*/
RETURN duration::nanos(3w);

-- 1814400000000000
```

  

## `duration::secs`

The `duration::secs` function counts how many seconds fit into a duration.

```surql title="API DEFINITION"
duration::secs(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "1814400"

*/
RETURN duration::secs(3w);

-- 1814400
```

  

## `duration::weeks`

The `duration::weeks` function counts how many weeks fit into a duration.

```surql title="API DEFINITION"
duration::weeks(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql

/**[test]

[[test.results]]
value = "3"

*/
RETURN duration::weeks(3w);

-- 3
```

  

## `duration::years`

The `duration::years` function counts how many years fit into a duration.

```surql title="API DEFINITION"
duration::years(duration) -> number
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql

/**[test]

[[test.results]]
value = "5"

*/
RETURN duration::years(300w);

-- 5
```

  

## `duration::from_days`

The `duration::from_days` function counts how many years fit into a duration.

```surql title="API DEFINITION"
duration::from_days(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql

/**[test]

[[test.results]]
value = "3d"

*/
RETURN duration::from_days(3);

-- 3d
```

  

## `duration::from_hours`

The `duration::from_hours` function converts a numeric amount of hours into a duration that represents hours.

```surql title="API DEFINITION"
duration::from_hours(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "3h"

*/

RETURN duration::from_hours(3);

-- 3h
```

  

## `duration::from_micros`

The `duration::from_micros` function converts a numeric amount of microseconds into a duration that represents microseconds.

```surql title="API DEFINITION"
duration::from_micros(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "3µs"

*/
RETURN duration::from_micros(3);

-- 3μs
```

  

## `duration::from_millis`

The `duration::from_millis` function converts a numeric amount of milliseconds into a duration that represents milliseconds.

```surql title="API DEFINITION"
duration::from_millis(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "3ms"

*/

RETURN duration::from_millis(3);

-- 3ms
```

  

## `duration::from_mins`

The `duration::from_mins` function converts a numeric amount of minutes into a duration that represents minutes.

```surql title="API DEFINITION"
duration::from_mins(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "3m"

*/

RETURN duration::from_mins(3);

-- 3m
```

  

## `duration::from_nanos`

The `duration::from_nanos` function converts a numeric amount of nanoseconds into a duration that represents nanoseconds.

```surql title="API DEFINITION"
duration::from_nanos(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "3ns"

*/
RETURN duration::from_nanos(3);

-- 3ns
```

  

## `duration::from_secs`

The `duration::from_secs` function converts a numeric amount of seconds into a duration that represents seconds.

```surql title="API DEFINITION"
duration::from_secs(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "3s"

*/
RETURN duration::from_secs(3);

-- 3s
```

  

## `duration::from_weeks`

The `duration::from_weeks` function converts a numeric amount of weeks into a duration that represents weeks.

```surql title="API DEFINITION"
duration::from_weeks(number) -> duration
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
/**[test]

[[test.results]]
value = "3w"

*/
RETURN duration::from_weeks(3);

-- 3w
```

  
  

## Method chaining

*Since v2.0.0*

Method chaining allows functions to be called using the `.` dot operator on a value of a certain type instead of the full path of the function followed by the value.

```surql

/**[test]

[[test.results]]
value = "3240"

[[test.results]]
value = "3240"

*/

-- Traditional syntax
duration::mins(2d6h);

-- Method chaining syntax
2d6h.mins();
```

```surql title="Response"
3240
```

This is particularly useful for readability when a function is called multiple times.

```surql
/**[test]

[[test.results]]
value = "1645"

[[test.results]]
value = "1645"

*/

-- Traditional syntax
duration::mins(duration::from_millis(98734234));

-- Method chaining syntax
duration::from_millis(98734234).mins();
```

```surql title="Response"
1645
```
