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
			<th scope="col" class="w-48">Operator</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex gap-2">
					<a href="#and">
						`&&`
					</a>
					<a href="#and">
						`AND`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether both of two values are truthy
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex gap-2">
					<a href="#or">
						`||`
					</a>
					<a href="#or">
						`OR`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether either of two values is truthy
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#not">
					`!`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Reverses the truthiness of a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#not_not">
					`!!`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Determines the truthiness of a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#nco">
					`??`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether either of two values are truthy and not NULL
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#tco">
					`?:`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether either of two values are truthy
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex gap-2">
					<a href="#equal">
						`=`
					</a>
					<a href="#equal">
						`IS`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Check whether two values are equal
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex gap-2">
					<a href="#notequal">
						`!=`
					</a>
					<a href="#notequal">
						`IS NOT`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Check whether two values are not equal
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#exact">
					`==`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether two values are exactly equal
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#anyequal">
					`?=`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether any value in a set is equal to a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#allequal">
					`*=`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether all values in a set are equal to a value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#match">
					`~`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Compare two values for equality using fuzzy matching
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#match">
					`!~`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Compare two values for inequality using fuzzy matching
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#match">
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
				<a href="#match">
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
				<a href="#lessthan">
					`&lt;`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether a value is less than another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#lessthanorequal">
					`&lt;=`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether a value is less than or equal to another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#greaterthan">
					`&gt;`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Check whether a value is greater than another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#greaterthanorequal">
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
				<a href="#add">
					`+`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Add two values together
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#sub">
					`-`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Subtract a value from another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex gap-2">
					<a href="#mul">
						`*`
					</a>
					<a href="#mul">
						`×`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Multiply two values together
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex gap-2">
					<a href="#div">
						`/`
					</a>
					<a href="#div">
						`÷`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Divide a value by another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<a href="#pow">
					`**`
				</a>
			</td>
			<td scope="row" data-label="Description">
				Raises a base value by another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col gap-2">
					<a href="#contains">
						`CONTAINS`
					</a>
					<a href="#contains">
						`∋`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col gap-2">
					<a href="#containsnot">
						`CONTAINSNOT`
					</a>
					<a href="#containsnot">
						`∌`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value does not contain another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col gap-2">
					<a href="#containsall">
						`CONTAINSALL`
					</a>
					<a href="#containsall">
						`⊇`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains all other values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col gap-2">
					<a href="#containsany">
						`CONTAINSANY`
					</a>
					<a href="#containsany">
						`⊃`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains any other value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col gap-2">
					<a href="#containsnone">
						`CONTAINSNONE`
					</a>
					<a href="#containsnone">
						`⊅`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value contains none of the following values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col items-start gap-2">
					<a href="#inside">
						`INSIDE`
					</a>
					<a href="#inside">
						`IN`
					</a>
					<a href="#inside">
						`∈`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value is contained within another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col items-start gap-2">
					<a href="#notinside">
						`NOTINSIDE`
					</a>
					<a href="#notinside">
						`NOT IN`
					</a>
					<a href="#notinside">
						`∉`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether a value is not contained within another value
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col items-start gap-2">
					<a href="#allinside">
						`ALLINSIDE`
					</a>
					<a href="#allinside">
						`⊆`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether all values are contained within other values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col items-start gap-2">
					<a href="#anyinside">
						`ANYINSIDE`
					</a>
					<a href="#anyinside">
						`⊂`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether any value is contained within other values
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col items-start gap-2">
					<a href="#noneinside">
					`NONEINSIDE`
					</a>
					<a href="#noneinside">
						`⊄`
					</a>
				</div>
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
				<div class="flex flex-col items-start gap-2">
					<a href="#matches">
						`@@`
					</a>
					<a href="#matches">
						`@[ref]@`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Checks whether the terms are found in a full-text indexed
				field
			</td>
		</tr>
		<tr>
			<td scope="row" data-label="Operator">
				<div class="flex flex-col items-start gap-2">
					<a href="#knn">
						` &lt;|4|&gt; `
					</a>
					<a href="#knn">
						`&lt;|3,HAMMING| &gt;`
					</a>
				</div>
			</td>
			<td scope="row" data-label="Description">
				Performs a K-Nearest Neighbors (KNN) search to find a
				specified number of records closest to a given data point,
				optionally using a defined distance metric. Supports
				customizing the number of results and choice of distance
				calculation method.
			</td>
		</tr>
	</tbody>
</table>

## `&&` or `AND` <a id="and"></a>

The `and` operator checks whether both of two values are [truthy](data-types/values.md#values-and-truthiness).

```surql
/**[test]

[[test.results]]
value = "30"

*/

SELECT * FROM 10 AND 20 AND 30;

-- 30
```

  

## `||` or `OR` <a id="or"></a>

The `or` operator checks whether either of two values are [truthy](data-types/values.md#values-and-truthiness).

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM 0 OR false OR 10;

-- 10
```

  

## `!` <a id="not"></a>

The `not` operator reverses the truthiness of a value.

```surql
/**[test]

[[test.results]]
value = "[false]"

[[test.results]]
value = "[false]"

*/

SELECT * FROM !(TRUE OR FALSE);
-- false

SELECT * FROM !"Has a value";
-- false
```

  

## `!!` <a id="not_not"></a>

The `not not` operator is simply an application of the `!` operator twice. It can be used to determines the truthiness of a value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM !!"Has a value";
-- true
```

## `??` <a id="nco"></a>

The `null coalescing operator` checks whether either of two values are [truthy](data-types/values.md#values-and-truthiness) and not `NONE` or `NULL`.

```surql
/**[test]

[[test.results]]
value = "[0]"

*/

SELECT * FROM NULL ?? 0 ?? false ?? 10;

-- 0
```

  

## `?:` <a id="tco"></a>

The `truthy coalescing operator` checks whether either of two values are [truthy](data-types/values.md#values-and-truthiness).

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM NULL ?: 0 ?: false ?: 10;

-- 10
```

  

## `=` or `IS` <a id="equal"></a>

The `equal` operator checks whether two values are equal.

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM true = "true";
-- false
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM 10 = "10";
-- false
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 = 10.00;
-- true
```
```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM 10 = "10.3";
-- false
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [1, 2, 3] = [1, 2, 3];
-- true
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM [1, 2, 3] = [1, 2, 3, 4];
-- false
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM { this: "object" } = { this: "object" };
-- true
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM { this: "object" } = { another: "object" };
-- false
```

  

## `!=` or `IS NOT` <a id="notequal"></a>

The `not equal` operator checks whether two values are not equal.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 != "15";
-- true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 != "test";
-- true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [1, 2, 3] != [3, 4, 5];
-- true
```

  

## `==` <a id="exact"></a>

The `exact` operator checks whether two values are exact. This operator also checks that each value has the same type.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 == 10;
-- true
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM 10 == "10";
-- false
```

```surql
/**[test]

[[test.results]]
value = "[false]"

*/

SELECT * FROM true == "true";
-- false
```

  

## `?=` <a id="anyequal"></a>

The `any equal` operator checks whether any value in an array equals another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 15, 20] ?= 10;
-- true
```

  

## `*=` <a id="allequal"></a>

The `all equal` operator checks whether all values in an array equals another value.

```surql
/**[test]

[[test.results]]
value = ""

*/

SELECT * FROM [10, 10, 10] *= 10;
-- true
```

  

## `~` `?~` `!~` `*~` <a id="match"></a>

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
-- true
```

  

## `<` <a id="lessthan"></a>

The `less than` operator checks whether a value is less than another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 < 15;
-- true
```

  

## `<=` <a id="lessthanorequal"></a>

The `less than or equal` operator checks whether a value is less than or equal to another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 <= 15;
-- true
```

  

## `>` <a id="greaterthan"></a>

The `greater than` operator checks whether a value is less than another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 15 > 10;
-- true
```

  

## `>=` <a id="greaterthanorequal"></a>

The `greater than or equal` operator checks whether a value is less than or equal to another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 15 >= 10;
-- true
```

  

## `+` <a id="add"></a>

The `add` operator adds two values together.

```surql
/**[test]

[[test.results]]
value = "[20]"

*/

SELECT * FROM 10 + 10;
-- 20
```

```surql
/**[test]

[[test.results]]
value = "['test this']"

*/

SELECT * FROM "test" + " " + "this";
-- "test this"
```

```surql
/**[test]

[[test.results]]
value = "[13h30m]"

*/

SELECT * FROM 13h + 30m;
-- "13h30m"
```

  

## `-` <a id="sub"></a>

The `subtract` operator subtracts a value from another value.

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM 20 - 10;
-- 10
```

```surql
/**[test]

[[test.results]]
value = "[1m]""

*/

SELECT * FROM 2m - 1m;
-- 1m
```

  

## `*` or `×` <a id="mul"></a>

The `multiply` operator multiplies a value by another value.

```surql
/**[test]

[[test.results]]
value = "[40]"

*/

SELECT * FROM 20 * 2;
-- 40
```

  

## `/` or `÷` <a id="div"></a>

The `divide` operator divides a value by another value.

```surql
/**[test]

[[test.results]]
value = "[10]"

*/

SELECT * FROM 20 / 2;
-- 10
```

  

## `**` <a id="pow"></a>

The `power` operator raises a base value by another value.

```surql
/**[test]

[[test.results]]
value = "[8000]"

*/

SELECT * FROM 20 ** 3;
-- 8000
```

  

## `CONTAINS` or `∋` <a id="contains"></a>

The `contains` operator checks whether a value contains another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINS 10;
-- true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "this is some text" CONTAINS "text";
-- true
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

-- true
```

  

## `CONTAINSNOT` or `∌` <a id="containsnot"></a>

The `not contains` operator checks whether a value does not contain another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINSNOT 15;
-- true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "this is some text" CONTAINSNOT "other";
-- true
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

-- true
```

  

## `CONTAINSALL` or `⊇` <a id="containsall"></a>

The `contains all` operator checks whether a value contains all of multiple values.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINSALL [10, 20, 10];
-- true
```

  

## `CONTAINSANY` or `⊃` <a id="containsany"></a>

The `contains any` operator checks whether a value contains any of multiple values.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 30] CONTAINSANY [10, 15, 25];
-- true
```

  

## `INSIDE` or `∈` or `IN` <a id="inside"></a>

The `inside` operator checks whether a value is contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 10 INSIDE [10, 20, 30];
-- true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "text" INSIDE "this is some text";
-- true
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

*Since v2.1.0*

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

-- true
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

  

## `NOTINSIDE` or `∉` or `NOT IN` <a id="notinside"></a>

The `not inside` operator checks whether a value is not contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM 15 NOTINSIDE [10, 20, 30];
-- true
```

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM "other" NOTINSIDE "this is some text";
-- true
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

-- true
```

  

## `ALLINSIDE` or `⊆` <a id="allinside"></a>

The `all inside` operator checks whether all of multiple values are contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 20, 10] ALLINSIDE [10, 20, 30];
-- true
```

  

## `ANYINSIDE` or `⊂` <a id="anyinside"></a>

The `any inside` operator checks whether any of multiple values are contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [10, 15, 25] ANYINSIDE [10, 20, 30];
-- true
```

  

## `NONEINSIDE` or `⊄` <a id="noneinside"></a>

The `none inside` operator checks whether none of multiple values are contained within another value.

```surql
/**[test]

[[test.results]]
value = "[true]"

*/

SELECT * FROM [15, 25, 35] NONEINSIDE [10, 20, 30];
-- true
```

  

## `OUTSIDE` <a id="outside"></a>

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

-- true
```

  

## `INTERSECTS` <a id="intersects"></a>

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

-- true
```

  

## `MATCHES` <a id="matches"></a>

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

In addition to the `AND` keyword, the `OR` matches operator can also be used as of 3.0.0-beta. This allows a single string to be compared against instead of needing to specify individual parts of the string.

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
SELECT * FROM document WHERE text @@ "personal" OR text @@ "nice weather today";
```

## `KNN`

K-Nearest Neighbors (KNN) is a fundamental algorithm used for classifying or regressing based on the closest data points in the feature space, with its performance and scalability critical in applications involving large datasets.

In practice, the efficiency and scalability of the KNN algorithm are crucial, especially when dealing with large datasets. Different implementations of KNN are tailored to optimize these aspects without compromising the accuracy of the results.

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
DEFINE INDEX mt_pts ON pts FIELDS point HNSW DIMENSION 4 DIST EUCLIDEAN EFC 150 M 12;
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

  
  

## Using the `ANY`/`ALL` operators for string indexes

*Since v2.4.0*

An index defined on a string value can be used via the operators `CONTAINSANY`, `ALLINSIDE`, or `ANYINSIDE`. The operator `CONTAINS`, however, will not use a defined index as `CONTAINS` is used for substring matches between strings themselves as opposed to an index lookup.

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

-- Both return the user Billy McConnell
SELECT * FROM account WHERE name CONTAINS "Billy McConnell";
SELECT * FROM account WHERE name CONTAINSANY ["Billy McConnell"];

-- However, CONTAINS does not use the index
SELECT * FROM account WHERE name CONTAINS "Billy McConnell" EXPLAIN FULL;
-- CONTAINSANY + putting the value inside an array will use the index
SELECT * FROM account WHERE name CONTAINSANY ["Billy McConnell"] EXPLAIN FULL;
```

## Types of operators, order of operations and binding power

To determine which operator is executed first, a concept called "binding power" is used. Operators with greater binding power will operate directly on their neighbours before those with lower binding power. The following is a list of all operator types from greatest to lowest binding power.

<table>
	<thead>
		<tr>
			<th scope="col" class="w-40">Operator name</th>
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
