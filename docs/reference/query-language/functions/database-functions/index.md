---
position: 1
title: Database Functions
description: SurrealDB comes with a large number of in-built functions for checking, manipulating, and working with many different types of data.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/functions/database-functions/index.mdx"
---

# Database functions

SurrealDB has many built-in functions designed to handle many common database tasks and work with SurrealDB's various data types, grouped into modules based on their purpose and the data types they are designed to work with. The table below lists all of SurrealDB's function modules, with descriptions and links to their own detailed documentation.

<table>
	<thead>
		<tr>
			<th scope="col" class="w-40">
				Function
			</th>
			<th scope="col">Description and Example</th>
		</tr>
	</thead>
	<tbody>
	<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/api">
					`API`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used to add middleware to a defined API endpoint.
				
				Example: `api::timeout(1s)`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/array">
					`Array`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when working with, and
				manipulating arrays of data.
				
				Example: `array::len([1,2,3])`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/bytes">
					`Bytes`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when working with bytes in
				SurrealQL.
				
				Example: `bytes::len("SurrealDB".to_bytes());`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/count">
					`Count`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				This function can be used when counting field values and
				expressions.
				
				Example: `count([1,2,3])`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/crypto">
					`Crypto`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when hashing data, encrypting
				data, and for securely authenticating users into the
				database.
				
				Example: `crypto::argon2::generate("MyPaSSw0RD")`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/duration">
					`Duration`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				Funcions and constants for converting between numeric values
				and duration data.
				
				Example: `duration::days(90h30m)`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/encoding">
					`Encoding`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used to encode and decode data in{' '}
				`base64`.
				Example: `encoding::base64::decode("aGVsbG8")`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/file">
					`Files`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used to work with files.
				Example: `f"my_bucket:/my_book.txt".get()`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/geo">
					`Geo`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when working with and analysing
				geospatial data.
				
				Example:{' '}
				`geo::distance((-0.04, 51.55), (30.46, -17.86))`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/http">
					`HTTP`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when opening and submitting
				remote web requests, and webhooks.
				
				Example: `http::get('https://surrealdb.com')`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/math">
					`Math`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				Functions and constants for
				analysing numeric data and numeric collections.
				
				Example:{' '}
				`
					math::max([ 26.164, 13.746189, 23, 16.4, 41.42 ])
				`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/meta">
					`Meta`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used to retrieve specific metadata
				from a SurrealDB Record ID. As of version 2.0, these
				functions are deprecated and replaced with SurrealDB's{' '}
				`record` functions.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/not">
					`Not`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				This function reverses the truthiness of a value.
				
				Example: `not(true)`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/object">
					`Object`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when working with, and
				manipulating data objects.
				
				Example:{' '}
				`
					object::from_entries([[ "a", 1 ],[ "b", true ]])
				`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/parse">
					`Parse`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when parsing email addresses and
				URL web addresses.
				
				Example:{' '}
				`
					parse::url::domain("http://127.0.0.1/index.html")
				`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/rand">
					`Rand`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when generating random data
				values.
				
				Example:{' '}
				`
					rand::enum('one', 'two', 3, 4.15385, 'five', true)
				`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/record">
					`Record`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used to retrieve specific metadata
				from a SurrealDB Record ID.
				
				Example: `record::id(person:tobie)`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/search">
					`Search`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions are used in conjunction with the{' '}
				`@@` operator (the 'matches' operator) to either
				collect the relevance score or highlight the searched
				keywords within the content.
				
				Example:{' '}
				`
					SELECT search::score(1) AS score FROM book WHERE title
					@1@ 'rust web'
				`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/sequence">
					`Sequence`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used to work with a defined sequence.
				
				Example: `sequence::nextval('mySeq2')`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/session">
					`Session`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions return information about the current
				SurrealDB session.
				
				Example: `session::db()`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/set">
					`Set`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when working with, and
				manipulating sets of data.
				
				Example: ``set::len({1,2,3})``
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/sleep">
					`Sleep`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				This function can be used to introduce a delay or pause in
				the execution of a query or a batch of queries for a
				specific amount of time.
				
				Example: `sleep(900ms)`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/string">
					`String`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used when working with and
				manipulating text and string values.
				
				Example:{' '}
				`string::reverse('emosewa si 0.2 BDlaerruS')`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/time">
					`Time`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				Functions and constants for
				working with and manipulating datetime values.
				
				Example: `time::timezone()`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/type">
					`Type`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				These functions can be used for generating and coercing data
				to specific data types.
				
				Example: `type::is_number(500)`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/value">
					`Value`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				This module contains several miscellaneous functions that
				can be used with values of any type.
				
				Example:{' '}
				`value::diff([true, false], [true, true])`
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function">
				<a href="/docs/reference/query-language/functions/database-functions/vector">
					`Vector`
				</a>
			</td>
			<td scope="row" data-label="Description and Example">
				A collection of essential vector operations that provide
				foundational functionality for numerical computation,
				machine learning, and data analysis.
				
				Example: `vector::add([1, 2, 3], [1, 2, 3])`
			</td>
		</tr>
	</tbody>
</table>

## How to use database functions

### Classic syntax

Functions in SurrealDB can always be called using their full path names beginning with the package names indicated above, followed by the function arguments.

```surql
string::split("SurrealDB 2.0 is on its way!", " ");
array::len([1,2,3]);
type::is_number(10);
type::record("cat", "mr_meow");
```

```surql title="Response"
-------- Query --------

[
	'SurrealDB',
	'2.0',
	'is',
	'on',
	'its',
	'way!'
]

-------- Query --------

3

-------- Query --------

true

-------- Query --------

cat:mr_meow
```

### Method syntax

*Since v2.0.0*

Functions that are called on an existing value can be called using method syntax, using the `.` (dot) operator.

The following functions will produce the same output as the classic syntax above. `type::record()` cannot be called with method syntax because it is used to outright create a record ID from nothing, rather than being called on an existing value.

```surql
"SurrealDB 2.0 is on its way!".split(" ");
[1,2,3].len();
10.is_number();
```

The method syntax is particularly useful when calling a number of functions inside a single query.

```surql
array::len(array::windows(array::distinct(array::flatten([[1,2,3],[1,4,6],[4,2,4]])), 2));
```

Readability before `2.0` could be improved to a certain extent by moving a query of this type over multiple lines.

```surql
array::len(
    array::clump(
        array::distinct(
            array::flatten([[1,2,3],[1,4,6],[4,2,4]])
        )
    , 2)
);
```

However, method chaining syntax allows queries of this type to be read from left to right in a functional manner. This is known as method chaining. As each of the methods below except the last return an array, further array methods can thus be called by using the `.` operator. The final method then returns an integer.

```surql
[[1,2,3],[1,4,6],[4,2,4],2].flatten().distinct().windows(2).len();
```

This can be made even more readable by splitting over multiple lines.

```surql
[[1,2,3],[1,4,6],[4,2,4]]
    .flatten()
    .distinct()
    .windows(2)
    .len();
```

### Conversion from `::` (double colon) to `_` (underscore) syntax

*Since v3.0.0*

Full function paths in SurrealDB were converted to match the method syntax detailed above.

```surql
-- Old syntax
type::is::record(person:one);
-- Method syntax
person:one.is_record();
-- New syntax now matches method syntax
type::is_record(person:one);
```

### Built-in constants

Some modules expose constants (fixed values) as well as functions. Consts use the same `module::name` path syntax as for functions, but omit parentheses because they access direct values instead of a function to be called.

- **[Math](math.md#math-constants)** — numeric constants (π, e, τ, infinities, and related values).
- **[Time](time.md#time-constants)** — `time::epoch`, `time::minimum`, and `time::maximum`.
- **[Duration](duration.md#duration-constants)** — `duration::max`.

```surql
RETURN [math::pi, math::tau, math::e];
```

```surql title="Response"
[
	3.141592653589793f,
	6.283185307179586f,
	2.718281828459045f
]
```

## Aggregate functions

A few functions can be used not just on their own but with a [`GROUP BY`](https://surrealdb.com/docs/reference/query-language/clauses/group-by) clause including as part of a [pre-computed table view](../../statements/define/table.md#pre-computed-table-views).

These functions are:

* [`count()`](count.md)
* [`math::max()`](math.md#mathmax)
* [`math::min()`](math.md#mathmin)
* [`math::sum()`](math.md#mathsum)
* [`math::mean()`](math.md#mathmean)
* [`math::stddev()`](math.md#mathstddev)
* [`math::variance()`](math.md#mathvariance)
* [`time::max()`](time.md#timemax)
* [`time::min()`](time.md#timemin)

## Anonymous functions

*Since v2.0.0*

SurrealDB also allows for the creation of anonymous functions (also known as closures) that do not need to be defined on the database. See [the page on closures](../../language-primitives/data-types/closures.md) for more details.
