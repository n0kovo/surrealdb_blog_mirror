---
position: 2
title: Operators
description: A variety of operators in SurrealQL allow for complex manipulation of data, and advanced logic.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/language-primitives/operators.mdx"
---

# Operators

A variety of operators in SurrealQL allow for complex manipulation of data, and advanced logic.

<table>
	<thead>
		<tr>
			<th scope="col">Operator</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; gap: 0.5rem;">
					<a href="#-or-and">
						`&&`
					</a>
					<a href="#-or-and">
						`AND`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether both of two values are truthy
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; gap: 0.5rem;">
					<a href="#-or-or">
						`||`
					</a>
					<a href="#-or-or">
						`OR`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether either of two values is truthy
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#">
					`!`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Reverses the truthiness of a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-1">
					`!!`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Determines the truthiness of a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-2">
					`??`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether either of two values are truthy and not NULL
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-3">
					`?:`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether either of two values are truthy
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; gap: 0.5rem;">
					<a href="#-or-is">
						`=`
					</a>
					<a href="#-or-is">
						`IS`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Check whether two values are equal
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; gap: 0.5rem;">
					<a href="#-or-is-not">
						`!=`
					</a>
					<a href="#-or-is-not">
						`IS NOT`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Check whether two values are not equal
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-4">
					`==`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether two values are exactly equal
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-5">
					`?=`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether any value in a set is equal to a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-6">
					`*=`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether all values in a set are equal to a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#---">
					`~`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Compare two values for equality using fuzzy matching
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#---">
					`!~`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Compare two values for inequality using fuzzy matching
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#---">
					`?~`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether any value in a set is equal to a value using
				fuzzy matching
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#---">
					`*~`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether all values in a set are equal to a value using
				fuzzy matching
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-7">
					`&lt;`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether a value is less than another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-8">
					`&lt;=`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether a value is less than or equal to another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-9">
					`&gt;`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether a value is greater than another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-10">
					`&gt;=`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether a value is greater than or equal to another
				value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-11">
					`+`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Add two values together
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-">
					`-`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Subtract a value from another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; gap: 0.5rem;">
					<a href="#-or-">
						`*`
					</a>
					<a href="#-or-">
						`×`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Multiply two values together
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; gap: 0.5rem;">
					<a href="#-or--1">
						`/`
					</a>
					<a href="#-or--1">
						`÷`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Divide a value by another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#-12">
					`**`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Raises a base value by another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; gap: 0.5rem;">
					<a href="#contains-or-">
						`CONTAINS`
					</a>
					<a href="#contains-or-">
						`∋`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; gap: 0.5rem;">
					<a href="#containsnot-or-">
						`CONTAINSNOT`
					</a>
					<a href="#containsnot-or-">
						`∌`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value does not contain another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; gap: 0.5rem;">
					<a href="#containsall-or-">
						`CONTAINSALL`
					</a>
					<a href="#containsall-or-">
						`⊇`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains all other values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; gap: 0.5rem;">
					<a href="#containsany-or-">
						`CONTAINSANY`
					</a>
					<a href="#containsany-or-">
						`⊃`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains any other value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; gap: 0.5rem;">
					<a href="#containsnone-or-">
						`CONTAINSNONE`
					</a>
					<a href="#containsnone-or-">
						`⊅`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains none of the following values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
					<a href="#inside-or--or-in">
						`INSIDE`
					</a>
					<a href="#inside-or--or-in">
						`IN`
					</a>
					<a href="#inside-or--or-in">
						`∈`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value is contained within another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
					<a href="#notinside-or--or-not-in">
						`NOTINSIDE`
					</a>
					<a href="#notinside-or--or-not-in">
						`NOT IN`
					</a>
					<a href="#notinside-or--or-not-in">
						`∉`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value is not contained within another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
					<a href="#allinside-or-">
						`ALLINSIDE`
					</a>
					<a href="#allinside-or-">
						`⊆`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether all values are contained within other values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
					<a href="#anyinside-or-">
						`ANYINSIDE`
					</a>
					<a href="#anyinside-or-">
						`⊂`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether any value is contained within other values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
					<a href="#noneinside-or-">
					`NONEINSIDE`
					</a>
					<a href="#noneinside-or-">
						`⊄`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether no value is contained within other values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#outside">
					`OUTSIDE`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a geometry type is outside of another
				geometry type
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#intersects">
					`INTERSECTS`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a geometry type intersects another geometry
				type
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
					<a href="#matches">
						`@@`
					</a>
					<a href="#matches">
						`@[ref]@`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Checks whether the terms are found in a full-text indexed
				field
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<span style="display: flex; flex-direction: column; align-items: flex-start; gap: 0.5rem;">
					<a href="#knn">
						` &lt;|4|&gt; `
					</a>
					<a href="#knn">
						`&lt;|3,HAMMING| &gt;`
					</a>
				</span>
			</td>
			<td scope="row" data-label="Description">
				Performs a K-Nearest Neighbors (KNN) search to find a
				specified number of records closest to a given data point,
				optionally using a defined distance metric. Supports
				customising the number of results and choice of distance
				calculation method.
			</td>
		</tr>
	</tbody>
</table>

## `&&` or `AND`
The `and` operator checks whether both of two values are [truthy](data-types/values.md#values-and-truthiness).

```surql
/**[test]

[[test.results]]
value = "30"

*/

SELECT * FROM 10 AND 20 AND 30;
```

```surql title="Output"
30
```

  

## `||` or `OR`
The `or` operator checks whether either of two values are [truthy](data-types/values.md#values-and-truthiness).

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM 0 OR false OR 10;
```

```surql title="Output"
10
```

  

## `!`
The `not` operator reverses the truthiness of a value.

```surql
/**[test]

[[test.results]]
value = "[false]"

[[test.results]]
value = "[false]"

*/

SELECT * FROM !(TRUE OR FALSE);
//- false

SELECT * FROM !"Has a value";
//- false
```

  

## `!!`
The `not not` operator is simply an application of the `!` operator twice. It can be used to determine the truthiness of a value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM !!"Has a value";
```

```surql title="Output"
true
```

## `??`
The `null coalescing operator` checks whether either of two values are [truthy](data-types/values.md#values-and-truthiness) and not `NONE` or `NULL`.

```surql
/**[test]

[[test.results]]
value = "[0]"

*/

SELECT * FROM NULL ?? 0 ?? false ?? 10;
```

```surql title="Output"
0
```

  

## `?:`
The `truthy coalescing operator` checks whether either of two values are [truthy](data-types/values.md#values-and-truthiness).

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM NULL ?: 0 ?: false ?: 10;
```

```surql title="Output"
10
```

  

## `=` or `IS`
The `equal` operator checks whether two values are equal.

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM true = "true";
```

```surql title="Output"
false
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM 10 = "10";
```

```surql title="Output"
false
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 = 10.00;
```

```surql title="Output"
true
```
```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM 10 = "10.3";
```

```surql title="Output"
false
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [1, 2, 3] = [1, 2, 3];
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM [1, 2, 3] = [1, 2, 3, 4];
```

```surql title="Output"
false
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM { this: "object" } = { this: "object" };
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM { this: "object" } = { another: "object" };
```

```surql title="Output"
false
```

  

## `!=` or `IS NOT`
The `not equal` operator checks whether two values are not equal.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 != "15";
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 != "test";
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [1, 2, 3] != [3, 4, 5];
```

```surql title="Output"
true
```

  

## `==`
The `exact` operator checks whether two values are exact. This operator also checks that each value has the same type.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 == 10;
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM 10 == "10";
```

```surql title="Output"
false
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM true == "true";
```

```surql title="Output"
false
```

  

## `?=`
The `any equal` operator checks whether any value in an array equals another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 15, 20] ?= 10;
```

```surql title="Output"
true
```

  

## `*=`
The `all equal` operator checks whether all values in an array equals another value.

```surql
/**[test]

[[test.results]]
value = ""

*/

SELECT * FROM [10, 10, 10] *= 10;
```

```surql title="Output"
true
```

  

## `~` `?~` `!~` `*~`
These operators used to compare two values for equality using fuzzy matching. They have been removed since 3.0 to avoid implicitly preferring one algorithm over another, as the type of fuzzy matching to use will depend on each individual case.

Please use the `string::similarity::*` functions instead:

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "true"

*/

let $threshold = 10;

string::similarity::smithwaterman("test text", "Test") > $threshold;
```

```surql title="Output"
true
```

  

## `<`
The `less than` operator checks whether a value is less than another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 < 15;
```

```surql title="Output"
true
```

  

## `<=`
The `less than or equal` operator checks whether a value is less than or equal to another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 <= 15;
```

```surql title="Output"
true
```

  

## `>`
The `greater than` operator checks whether a value is less than another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 15 > 10;
```

```surql title="Output"
true
```

  

## `>=`
The `greater than or equal` operator checks whether a value is less than or equal to another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 15 >= 10;
```

```surql title="Output"
true
```

  

## `+`
The `add` operator adds two values together.

```surql
/**[test]

[[test.results]]
value = "[20]"

*/

SELECT * FROM 10 + 10;
```

```surql title="Output"
20
```

```surql
/**[test]

[[test.results]]
value = "['test this']"

*/

SELECT * FROM "test" + " " + "this";
```

```surql title="Output"
"test this"
```

```surql
/**[test]

[[test.results]]
value = "[13h30m]"

*/

SELECT * FROM 13h + 30m;
```

```surql title="Output"
"13h30m"
```

  

## `-`
The `subtract` operator subtracts a value from another value.

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM 20 - 10;
```

```surql title="Output"
10
```

```surql
/**[test]

[[test.results]]
value = "[1m]""

*/

SELECT * FROM 2m - 1m;
```

```surql title="Output"
1m
```

  

## `*` or `×`
The `multiply` operator multiplies a value by another value.

```surql
/**[test]

[[test.results]]
value = "[40]"

*/

SELECT * FROM 20 * 2;
```

```surql title="Output"
40
```

  

## `/` or `÷`
The `divide` operator divides a value by another value.

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM 20 / 2;
```

```surql title="Output"
10
```

  

## `**`
The `power` operator raises a base value by another value.

```surql
/**[test]

[[test.results]]
value = "[8000]"

*/

SELECT * FROM 20 ** 3;
```

```surql title="Output"
8000
```

  

## `CONTAINS` or `∋`
The `contains` operator checks whether a value contains another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINS 10;
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "this is some text" CONTAINS "text";
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM {
	type: "Polygon",
	coordinates: [[
		[-0.38314819, 51.37692386], [0.1785278, 51.37692386],
		[0.1785278, 51.61460570], [-0.38314819, 51.61460570],
		[-0.38314819, 51.37692386]
	]]
} CONTAINS (-0.118092, 51.509865);
```

```surql title="Output"
true
```

  

## `CONTAINSNOT` or `∌`
The `not contains` operator checks whether a value does not contain another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINSNOT 15;
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "this is some text" CONTAINSNOT "other";
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM {
	type: "Polygon",
	coordinates: [[
		[-0.38314819, 51.37692386], [0.1785278, 51.37692386],
		[0.1785278, 51.61460570], [-0.38314819, 51.61460570],
		[-0.38314819, 51.37692386]
	]]
} CONTAINSNOT (-0.518092, 53.509865);
```

```surql title="Output"
true
```

  

## `CONTAINSALL` or `⊇`
The `contains all` operator checks whether a value contains all of multiple values.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINSALL [10, 20, 10];
```

```surql title="Output"
true
```

  

## `CONTAINSANY` or `⊃`
The `contains any` operator checks whether a value contains any of multiple values.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINSANY [10, 15, 25];
```

```surql title="Output"
true
```

  

## `CONTAINSNONE` or `⊅`
The `contains none` operator checks whether a value contains none of multiple values.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINSNONE [15, 25, 35];
```

```surql title="Output"
true
```

  

## `INSIDE` or `∈` or `IN`
The `inside` operator checks whether a value is contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 INSIDE [10, 20, 30];
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "text" INSIDE "this is some text";
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM (-0.118092, 51.509865) INSIDE {
	type: "Polygon",
	coordinates: [[
		[-0.38314819, 51.37692386], [0.1785278, 51.37692386],
		[0.1785278, 51.61460570], [-0.38314819, 51.61460570],
		[-0.38314819, 51.37692386]
	]]
};

true
```

This operator can also be used to check for the existence of a key inside an [object](data-types/objects.md). To do so, precede `IN` with the field name as a string.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

"name" IN {
    name: "Riga",
    country: "Latvia"
};
```

```surql title="Output"
true
```

`IN` can also be used with a record ID as long as the ID is expanded to include the fields. Both of the following queries will return `true`.

```surql
/**[test]

[[test.results]]
value = "[{ country: 'Latvia', id: city:riga, name: 'Riga', population: 605273 }]"

[[test.results]]
value = "true"

[[test.results]]
value = "true"

*/

CREATE city:riga SET name = "Riga", country = "Latvia", population = 605273;

"name" IN city:riga.*;
"name" IN city:riga.{ name, country };
```

  

## `NOTINSIDE` or `∉` or `NOT IN`
The `not inside` operator checks whether a value is not contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 15 NOTINSIDE [10, 20, 30];
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "other" NOTINSIDE "this is some text";
```

```surql title="Output"
true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM (-0.518092, 53.509865) NOTINSIDE {
	type: "Polygon",
	coordinates: [[
		[-0.38314819, 51.37692386], [0.1785278, 51.37692386],
		[0.1785278, 51.61460570], [-0.38314819, 51.61460570],
		[-0.38314819, 51.37692386]
	]]
};
```

```surql title="Output"
true
```

  

## `ALLINSIDE` or `⊆`
The `all inside` operator checks whether all of multiple values are contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 10] ALLINSIDE [10, 20, 30];
```

```surql title="Output"
true
```

  

## `ANYINSIDE` or `⊂`
The `any inside` operator checks whether any of multiple values are contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 15, 25] ANYINSIDE [10, 20, 30];
```

```surql title="Output"
true
```

  

## `NONEINSIDE` or `⊄`
The `none inside` operator checks whether none of multiple values are contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [15, 25, 35] NONEINSIDE [10, 20, 30];
```

```surql title="Output"
true
```

  

## `OUTSIDE`
The `outside` operator checks whether a geometry value is outside another geometry value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM (-0.518092, 53.509865) OUTSIDE {
	type: "Polygon",
	coordinates: [[
		[-0.38314819, 51.37692386], [0.1785278, 51.37692386],
		[0.1785278, 51.61460570], [-0.38314819, 51.61460570],
		[-0.38314819, 51.37692386]
	]]
};
```

```surql title="Output"
true
```

  

## `INTERSECTS`
The `intersects` operator checks whether a geometry value intersects another geometry value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM {
	type: "Polygon",
	coordinates: [[
		[-0.38314819, 51.37692386], [0.1785278, 51.37692386],
		[0.1785278, 51.61460570], [-0.38314819, 51.61460570],
		[-0.38314819, 51.37692386]
	]]
} INTERSECTS {
	type: "Polygon",
	coordinates: [[
		[-0.11123657, 51.53160074], [-0.16925811, 51.51921169],
		[-0.11466979, 51.48223813], [-0.07381439, 51.51322956],
		[-0.11123657, 51.53160074]
	]]
};
```

```surql title="Output"
true
```

  

## `MATCHES`
The `matches` operator checks whether the terms are found in a full-text indexed field.

```surql
SELECT * FROM book WHERE title @@ 'rust web';

[
	{
		id: book:1,
		title: 'Rust Web Programming'
	}
]
```
Using the matches operator with a reference checks whether the terms are found, highlights the searched terms, and computes the full-text score.

```surql
SELECT id,
		search::highlight('<b>', '</b>', 1) AS title,
		search::score(1) AS score
FROM book
WHERE title @1@ 'rust web'
ORDER BY score DESC;

[
	{
		id: book:1,
		score: 0.9227996468544006f,
		title: '<b>Rust</b> <b>Web</b> Programming'
	}
]
```

*Since v3.0.0*

### `AND`, `OR`, and numeric operators inside `@@`

In addition to the `AND` keyword, the `OR` matches operator can also be used. This allows a single string to be compared against instead of needing to specify individual parts of the string.

```surql
/**[test]

[[test.results]]
value = "[{ id: document:1, text: 'It is rare that I find myself penning a personal note in my chronicles.' }]"

[[test.results]]
value = "NONE"

[[test.results]]
value = "NONE"

[[test.results]]
value = "[{ id: document:1, text: 'It is rare that I find myself penning a personal note in my chronicles.' }]"

[[test.results]]
value = "[{ id: document:1, text: 'It is rare that I find myself penning a personal note in my chronicles.' }]"

[[test.results]]
value = "[{ id: document:1, text: 'It is rare that I find myself penning a personal note in my chronicles.' }]"

[[test.results]]
value = "[{ id: document:1, text: 'It is rare that I find myself penning a personal note in my chronicles.' }]"

[[test.results]]
value = "[{ id: document:1, text: 'It is rare that I find myself penning a personal note in my chronicles.' }]"

*/

CREATE document:1 SET text = "It is rare that I find myself penning a personal note in my chronicles.";
DEFINE ANALYZER simple TOKENIZERS blank,class FILTERS lowercase;
DEFINE INDEX some_index ON document FIELDS text FULLTEXT ANALYZER simple;

-- @AND@ and @OR@: can use the entire string
SELECT * FROM document WHERE text @AND@ "personal rare";
SELECT * FROM document WHERE text @OR@ "personal nice weather today";

-- Separate AND and OR outside of matches operator:
-- Must specify parts of string to check for match
SELECT * FROM document WHERE text @@ "personal" AND text @@ "rare";
SELECT * FROM document WHERE text @@ "personal note";
SELECT * FROM document WHERE text @@ "personal"
  OR text @@ "nice weather today";
```

## `KNN`

K-Nearest Neighbors (KNN) is an algorithm used for classification or regression based on the closest data points in the feature space.

The efficiency and scalability of the KNN algorithm matter most when dealing with large datasets. Different implementations of KNN are tailored to optimise these aspects without compromising the accuracy of the results.

SurrealDB supports different K-Nearest Neighbors methods to perform KNN searches, each with unique requirements for syntax.
Below are the details for each method, including how to format your query with examples:

### Brute force method

Best for smaller datasets or when the highest accuracy is required.

```syntax title="SurrealQL Syntax"
<|K,DISTANCE_METRIC|>
```

- K: The number of nearest neighbors to retrieve.
- DISTANCE_METRIC: The metric used to calculate distances, such as EUCLIDEAN or MANHATTAN.

```surql
/**[test]

[[test.results]]
value = "[{ id: pts:3, point: [8, 9, 10, 11] }]"

[[test.results]]
value = "[{ id: pts:3 }]"

*/

CREATE pts:3 SET point = [8,9,10,11];
SELECT id FROM pts WHERE point <|2,EUCLIDEAN|> [2,3,4,5];
```

### Approximate graph indexes

**HNSW**

#### HNSW

Recommended for very large datasets where speed is essential and some loss of accuracy is acceptable, **while the graph fits in memory**.

```syntax title="SurrealQL Syntax"
<|K,EF|>
```

- K: The number of nearest neighbors.
- EF: The size of the dynamic candidate list during the search, affecting the search's accuracy and speed.

```surql
/**[test]

[[test.results]]
value = "[{ id: pts:3, point: [8, 9, 10, 11] }]"

[[test.results]]
value = "NONE"

[[test.results]]
value = "[{ id: pts:3 }]"

*/

CREATE pts:3 SET point = [8,9,10,11];
DEFINE INDEX mt_pts
  ON pts FIELDS point HNSW DIMENSION 4;
SELECT id FROM pts WHERE point <|10,40|> [2,3,4,5];
```

**DISKANN**

#### DISKANN

*Since v3.1.0*

Recommended when embeddings are too large to keep an HNSW graph resident in RAM as the graph lives on disk with caching. Note that WASM targets do not support DISKANN, so use HNSW or brute force there.

The query syntax matches HNSW: use the approximate form `<|K, L|>` where the second value bounds the search candidate list (see [`DEFINE INDEX … DISKANN`](../statements/define/indexes.md#diskann-disk-based-approximate-nearest-neighbours) for defaults and supported `TYPE` / `DIST` combinations).

```syntax title="SurrealQL Syntax"
<|K,L|>
```

```surql
CREATE pts:3 SET point = [8,9,10,11];
DEFINE INDEX diskann_pts ON pts FIELDS point DISKANN DIMENSION 4 DIST EUCLIDEAN TYPE F32 DEGREE 8 L_BUILD 20;
SELECT id FROM pts WHERE point <|10,40|> [2,3,4,5];
```

### Combining a KNN search with a filter

A KNN search over an indexed field can be combined with additional `WHERE` conditions. When the vector field is indexed (HNSW or DISKANN), such a condition is pushed into the index search and evaluated *during* the graph traversal, so non-matching candidates are rejected before they occupy one of the `K` slots - rather than being filtered out after the neighbours have been retrieved.

You can confirm this by using the [`EXPLAIN`](../statements/explain.md) clause after a query to see its plan. Here, the condition appears as a `predicate` attribute on the `KnnScan` operator in  the output. See [Filtering through vector search](../../../learn/data-models/vector-search/similarity-search.md#how-the-filter-is-applied) for a worked example.

  
  

## Using the `ANY`/`ALL` operators for string indexes

*Since v2.4.0*

An index on a string field is used by `=` and by `IN` with an array of values. The containment operators `CONTAINS`, `CONTAINSANY`, `ALLINSIDE` and `ANYINSIDE` return the same records on such a field, but they scan the table, because they only use an index defined on the elements of an array field (such as `tags.*`). `CONTAINS` on a string is a substring match.

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "NONE"

[[test.results]]
value = "[{ id: account:billy, name: 'Billy McConnell' }]"

[[test.results]]
value = "[{ id: account:billy, name: 'Billy McConnell' }]"

[[test.results]]
value = "[{ id: account:billy, name: 'Billy McConnell' }]"

[[test.results]]
value = "[{ id: account:billy, name: 'Billy McConnell' }], [{ detail: { direction: 'forward', table: 'account' }, operation: 'Iterate Table' }, { detail: { type: 'Memory' }, operation: 'Collector' }, { detail: { type: 'KeysAndValues' }, operation: 'RecordStrategy' }, { detail: { count: 1 }, operation: 'Fetch' }]"

[[test.results]]
value = "[{ detail: { plan: { index: 'name_index', operator: 'union', value: ['Billy McConnell'] }, table: 'account' }, operation: 'Iterate Index' }, { detail: { type: 'Memory' }, operation: 'Collector' }, { detail: { type: 'KeysAndValues' }, operation: 'RecordStrategy' }, { detail: { count: 1 }, operation: 'Fetch' }]"

*/

DEFINE FIELD name ON account TYPE string;
DEFINE INDEX name_index ON account FIELDS name;

CREATE account:billy SET name = "Billy McConnell";

-- IN uses the index
EXPLAIN SELECT * FROM account WHERE name IN ["Billy McConnell"];
//- "SelectProject [ctx: Db] [projections: *]\n    IndexScan [ctx: Db] [index: name_index, access: = 'Billy McConnell', direction: Forward]\n"

-- CONTAINSANY scans the table
EXPLAIN SELECT * FROM account WHERE name CONTAINSANY ["Billy McConnell"];
//- "SelectProject [ctx: Db] [projections: *]\n    TableScan [ctx: Db] [table: account, direction: Forward, predicate: name CONTAINSANY ['Billy McConnell'], pre_decode_filter: yes]\n"
```

> [!NOTE]
> In SurrealDB 2.4 and later 2.x releases, `CONTAINSANY`, `ALLINSIDE` and `ANYINSIDE` with the values in an array used an index on a string field, and `CONTAINS` did not. From 3.0.0, use `=` or `IN` to query a string index.

## Types of operators, order of operations and binding power

To determine which operator is executed first, a concept called "binding power" is used. Operators with greater binding power will operate directly on their neighbours before those with lower binding power. The following is a list of all operator types from greatest to lowest binding power.

<table>
	<thead>
		<tr>
			<th scope="col">Operator name</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Type">
				`Unary`
			</td>
			<td scope="row" data-label="Description">
				The `Unary` operators are `!`, `+`, and `-`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`Nullish`
			</td>
			<td scope="row" data-label="Description">
				The `Nullish` operators are `?:` and `??`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`Range`
			</td>
			<td scope="row" data-label="Description">
				The `Range` operator is `..`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`Cast`
			</td>
			<td scope="row" data-label="Description">
				The `Cast` operator is `<type_name>`, with `type_name` a stand in for the type to cast into. For example, `<string>` or `<number>`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`Power`
			</td>
			<td scope="row" data-label="Description">
				The only `Power` operator is `**`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`MulDiv`
			</td>
			<td scope="row" data-label="Description">
				The `MulDiv` (multiplication and division) operators are `*`, `/`, `÷`, and `%`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`AddSub`
			</td>
			<td scope="row" data-label="Description">
				The `AddSub` (addition and subtraction) operators are `+` and `-`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`Relation`
			</td>
			<td scope="row" data-label="Description">
				The `Relation` operators are `<=`, `>=`, `∋`, `CONTAINS`, `∌`, `CONTAINSNOT`, `∈`, `INSIDE`, `∉`, `NOTINSIDE`, `⊇`, `CONTAINSALL`, `⊃`, `CONTAINSANY`, `⊅`, `CONTAINSNONE`, `⊆`, `ALLINSIDE`, `⊂`, `ANYINSIDE`, `⊄`, `NONEINSIDE`, `OUTSIDE`, `INTERSECTS`, `NOT`, and `IN`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`Equality`
			</td>
			<td scope="row" data-label="Description">
				The `Equality` operators are `=`, `IS`, `==`, `!=`, `*=`, `?=`, and `@`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`And`
			</td>
			<td scope="row" data-label="Description">
				The `And` operators are `&&` and `AND`.
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Type">
				`Or`
			</td>
			<td scope="row" data-label="Description">
				The `Or` operators are `||` and `OR`.
			</td>
		</tr>
	</tbody>
</table>

## Examples of binding power

The following samples show examples of basic operations of varying binding power. The original example is followed by the same example with the parts with higher binding power in parentheses, then the final expression after the first bound portion is calculated, and finally the output.

```surql title="MulDiv first, then AddSub"
/**[test]

[[test.results]]
value = "13"

[[test.results]]
value = "13"

[[test.results]]
value = "13"

[[test.results]]
value = "13"

*/
 
1 + 3 * 4;
1 + (3 * 4);
-- Final expression
1 + 12;
-- Output
13
```

```surql title="Power first, then MulDiv"
/**[test]

[[test.results]]
value = "24"

[[test.results]]
value = "24"

[[test.results]]
value = "24"

[[test.results]]
value = "24"

*/
 
2**3 * 3;
(2**3) * 3;
-- Final expression
8*3;
-- Output
24
```

```surql title="Unary first, then cast"
/**[test]

[[test.results]]
value = "'-4'"

[[test.results]]
value = "'-4'"

[[test.results]]
value = "'-4'"

*/

<string>-4;
<string>(-4);
-- Output
"-4"
```

```surql title="Cast first, then Power"
/**[test]

[[test.results]]
value = "387420489"

[[test.results]]
value = "387420489"

[[test.results]]
value = "387420489"

[[test.results]]
value = "387420489"

*/
 
<number>"9"**9;
(<number>"9")**9;
-- Final expression
9**9;
-- Output
387420489
```

```surql title="AddSub first, then Relation"
/**[test]

[[test.results]]
value = "true"

[[test.results]]
value = "true"

[[test.results]]
value = "true"

[[test.results]]
value = "true"
*/
 
"c" + "at" IN "cats";
("c" + "at") IN "cats";
-- Final expression
"cat" IN "cats";
-- Output
true
```

```surql title="And first, then Or"
/**[test]

[[test.results]]
value = "true"

[[test.results]]
value = "true"

[[test.results]]
value = "true"

[[test.results]]
value = "true"

*/
 
true AND false OR true;
(true AND false) OR true;
-- Final expression
false OR true;
-- Output
true
```

```surql title="Unary, then Cast, then Power, then AddSub"
/**[test]

[[test.results]]
value = "20dec"

[[test.results]]
value = "20dec"

[[test.results]]
value = "20dec"

*/
 
<decimal>-4**2+4;
((<decimal>(-4))**2)+4;
-- Output
20dec
```
