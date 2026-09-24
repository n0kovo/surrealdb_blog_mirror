---
position: 4
title: GROUP
description: The `GROUP` clause is used to group records by one or more fields.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/clauses/group.mdx"
---

# `GROUP` clause

The `GROUP` clause is used to aggregate data based on one or more fields. It is particularly useful when you want to perform calculations on groups of data, such as counting the number of records, calculating averages, or finding sums for each group. 

This is often used in reporting and data analysis to summarize data in a meaningful way. More specifically, it is used to:

- Aggregating data: When you need to calculate aggregate values like SUM, COUNT, AVG, MIN, or MAX for each group of data.
- Data summarisation: When you want to summarise data into categories or groups.
- Reporting: When generating reports that require grouped data, such as sales reports by region or department.

This clause is followed with either:

* `BY` to specify certain fields to group by, or
* `ALL` to group every selected record into a single aggregate.

*Since v3.2.5*

A projection made entirely of bare zero-argument [`count()`](../functions/database-functions/count.md) implies `GROUP ALL`, so `SELECT count() FROM person` and `SELECT count() FROM person GROUP ALL` are equivalent. See [Bare `count()` implies `GROUP ALL`](../statements/select.md#bare-count-implies-group-all) for the cases that stay per-row (`count(field)`, `*`, `SELECT VALUE`, `SPLIT`, and so on).

## Syntax

```syntax title="Clause Syntax"
GROUP [ BY @fields | ALL ]
```

## What a projection returns

After `GROUP`, each result stands for many records rather than one. A projection therefore has a single value to return only when that value is the same for every record in the group. Where it differs from record to record, SurrealDB returns all of them in an array instead of picking one.

Three rules decide which happens:

1. A **group key** is one value, because grouping is what made every record in the group share it.
2. An **aggregate name** always aggregates, including over a constant.
3. **Everything else** depends on whether the expression reads the record. An expression that does not is evaluated once and gives one value; an expression that does gives an array holding one element per record.

The group key is the field named in `GROUP BY`. A record id is not a group key, so projecting `id` collects it like any other expression that reads the record:

```surql
CREATE person:alice SET age = 30, name = 'Alice';
CREATE person:bob SET age = 30, name = 'Bob';

SELECT
    -- Rule 1, a group key: one value, shared by every record in the group
    age,
    -- Rule 2, an aggregate name: aggregates even over a constant, so this counts the records
    math::sum(1) AS total,
    -- Rule 3, does not read the record: evaluated once
    4 + 3 AS constant,
    -- Rule 3, reads the record: one element per record
    name,
    -- Rule 3, and the reason a record id is not a group key
    id
FROM person GROUP BY age;
```

```surql title="Output"
[
	{
		age: 30,
		constant: 7,
		id: [
			person:alice,
			person:bob
		],
		name: [
			'Alice',
			'Bob'
		],
		total: 2
	}
]
```

A collected value is an array, not a [set](../language-primitives/data-types/sets.md): it keeps duplicates, so two records named `'Alice'` in one group give `['Alice', 'Alice']`. Its order follows the record ids, which is why the example above gives its own ids rather than letting SurrealDB generate them. Use [`array::group()`](../functions/database-functions/array.md#arraygroup) where the unique values are what you want.

Some expressions count as reading the record because the engine cannot see through them: a call to a user-defined function, whose body may reach the record through `$parent`; `type::field()` and the index functions behind `@@` and `<|...|>`, which are bound to the record; and any function that writes, whose number of effects depends on how often it runs.

> [!NOTE]
> Standard SQL raises an error for the record-reading branch of rule 3, on the grounds that a projection would otherwise have more than one value to return. SurrealDB collects the values into an array instead, which keeps every value and stays deterministic.

## Aggregate functions

A [number of functions](../functions/database-functions/index.md#aggregate-functions) can be used inside a `GROUP BY` query to perform an operation on the data as a whole as opposed to per record.

For example, the [`math::sum()`](../functions/database-functions/math.md#mathsum) function can be used on an array of numbers to calculate their final sum.

```surql
math::sum([
    {
        name: "Billy",
        money: 10
    },
    { 
        name: "Tommy",
        money: 20
    }
].money);
//- 30
```

Attempting to use the same function inside a `SELECT` query will not work as `math::sum()` expects an array of numbers but only receives a single integer each time it is called.

```surql
SELECT 
    name AS names, 
    math::sum(money) AS money 
FROM [
    {
        name: "Billy",
        money: 10
    },
    { 
        name: "Tommy",
        money: 20
    }
];
```

If the data is aggregated with a `GROUP` clause, the query will no longer fail.

```surql
SELECT 
    name AS names,
    math::sum(money) AS money
FROM [
    {
        name: "Billy",
        money: 10
    },
    { 
        name: "Tommy",
        money: 20
    }
] GROUP ALL;
```

```surql title="Output"
[
	{
		money: 30,
		names: [
			'Billy',
			'Tommy'
		]
	}
]
```

## Longer example

```surql
SELECT
    product_id,
    region,
    math::sum(amount) AS total_sales
FROM
    sales
GROUP BY
    product_id, region;
```

Explanation:
- `SELECT product_id, region, math::sum(amount) AS total_sales`: This selects the `product_id` and `region` fields and calculates the total sales amount for each group. The `AS` clause is used to rename the calculated field to `total_sales`.

- `FROM sales`: This specifies the table from which to retrieve the data. Using the `FROM` clause, we specify the table `sales` to retrieve the data from.

- `GROUP BY product_id, region`: This groups the results by product_id and region, so the `math::sum()` function calculates the total sales for each unique combination of product_id and region.

This query will return a result where each record represents a unique combination of `product_id` and `region`, along with the total sales amount for that combination. This is useful for understanding how different products are performing in different regions.

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%0A%09%09SELECT%0A%09count%28%29%20AS%20total%2C%0A%09math%3A%3Amean%28age%29%20AS%20average_age%2C%0A%09gender%2C%0A%09country%0AFROM%20rams%0AGROUP%20BY%20gender%2C%20country%3B%0A%09)

## Latest record per group

When you need the most recently modified record for each value of a field, group by that field and use [`.map()`](../functions/database-functions/array.md#arraymap) to run a nested `SELECT` per group:

```surql
(SELECT id, role FROM person GROUP BY role).map(|$o| {
    SELECT * FROM ONLY $o.id ORDER BY modified_at DESC LIMIT 1
});
```

`GROUP BY` collects record ids into an array, after which the inner query orders those records and returns the latest. For a worked example with sample data, see [Latest record per group](../../../learn/querying/concepts-and-guides/subqueries-and-advanced-patterns.md#latest-record-per-group).
