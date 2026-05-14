---
title: "Thinking Inside The Box: Relational Style Joins in SurrealDB"
slug: "thinking-inside-the-box-relational-style-joins-in-surrealdb"
date: "2024-02-21T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "7 min read"
summary: "SurrealDB's relational style joins exist in a superposition. The only way to know for sure is by looking at this blog post."
source: "https://surrealdb.com/blog/thinking-inside-the-box-relational-style-joins-in-surrealdb"
cover: "../../assets/d6b5dd5a18eb742f.jpg"
---

# Thinking Inside The Box: Relational Style Joins in SurrealDB

![Thinking Inside The Box: Relational Style Joins in SurrealDB](../../assets/d6b5dd5a18eb742f.jpg)

SurrealDB doesn't do traditional SQL joins. What we have instead done is think from first principles what developers need from database relationships to be able to develop easier and scale quicker.

This led us to our primary ways of creating relationships at write time to simplify scaling and improve developer experience at query time. To dig more into that, see our previous [Beyond SQL Joins](/blog/beyond-sql-joins-exploring-surrealdbs-multi-model-relationships) blog post.

That blog post ended with the question:

> However, what if we want to make arbitrary relationships on the fly similar to relational style joins?

Let's now explore the answer to that question where, spoiler alert, we will learn about semi-joins, anti-joins, and correlated subqueries. Those are fancy terms, but don't worry, it's all going to make sense soon enough 😉

Starting with:

## It's me, subquery, I'm the problem, It's me

![wait, its all subqueries, always has been](../../assets/d21f7008d17eef9d.jpg)

Now that the secret is out of the bag, let's dive into the code to show how it works in practice.

Our data and examples for today will be based on the [w3schools SQL tutorial](https://www.w3schools.com/sql)(great resource btw) where we will compare the SQL approach shown there with SurrealQL.

This is the very simple schema that we will be using, consisting of a product table and a supplier table.

| ProductID | ProductName | SupplierID | Price |
|---|---|---|---|
| 1 | Chais | 1 | 18 |
| 2 | Chang | 1 | 19 |
| 3 | Aniseed Syrup | 1 | 10 |
| 4 | Chef Anton's Cajun Seasoning | 2 | 22 |
| 5 | Chef Anton's Gumbo Mix | 2 | 21.35 |

| SupplierID | SupplierName |
|---|---|
| 1 | Exotic Liquid |
| 2 | New Orleans Cajun Delights |
| 3 | Grandma Kelly's Homestead |
| 4 | Tokyo Traders |

If you want to follow along, you can go to [https://app.surrealdb.com/](https://app.surrealdb.com/) → Create session → Click on sandbox → Type any name for namespace and database → Copy and paste the two queries below, which work both for SurrealDB and most relational DBs

Products table:

```surrealql
INSERT INTO Products (ProductID, ProductName, SupplierID, Price)
VALUES (1, "Chais", 1, 18), (2, "Chang", 1, 19), (3, "Aniseed Syrup", 1, 10), (4, "Chef Anton's Cajun Seasoning", 2, 22), (5, "Chef Anton's Gumbo Mix", 2, 21.35);
```

Supplier table:

```surrealql
INSERT INTO Suppliers (SupplierID, SupplierName)
VALUES (1, "Exotic Liquid"), (2, "New Orleans Cajun Delights"), (3, "Grandma Kelly's Homestead"), (4, "Tokyo Traders");
```

## Semi-Joins

It's a subquery that filters the outer query with the results of the inner query.

Now that we've got the dictionary definition out of the way, let's get to the exciting stuff, where we'll explore the same query written in 3 different ways in both SQL and SurrealQL.

This will really help you see the difference between a semi-join, correlated subquery and a traditional SQL join.

### `IN` example

As SurrealQL is a SQL-like language, you’ll notice that the examples will look very similar, such as just a single word difference like in the below example, see if you can spot it.

#### SQL Example

```surrealql
-- Outer query
SELECT SupplierName
FROM Suppliers
WHERE SupplierID IN (
  -- Inner query
    SELECT SupplierID
    FROM Products
    WHERE Price < 20
    );
```

#### SurrealQL Example

```surrealql
-- Outer query
SELECT SupplierName
FROM Suppliers
WHERE SupplierID IN (
  -- Inner query
    SELECT VALUE SupplierID
    FROM Products
    WHERE Price < 20
    );
```

Since inner queries run before outer queries, it's often good to read subqueries from the inside out.

Starting with us filtering for products in the `Products` table that have a price less than 20, then "joining" the `Products` table to the `Suppliers` table using the `SupplierID`.

This then allows us to see the names of the suppliers which have products where the price is less than 20.

The reason why you see the word `VALUE` added to the `SELECT` in SurreaQL is because by default SurrealDB returns objects. Since we want to check if an ID is in an array of IDs, [`SELECT VALUE`](/docs/surrealql/statements/select#basic-usage) allows you to return an array of values instead.

A key thing to notice here is that the entirety of the inner query is run before the outer query, which would make it an uncorrelated subquery. This does have some pros and cons, as we'll explore in our next example.

### Correlated subquery example

It's still a subquery that filters the outer query with the results of the inner query and is a type of semi-join.

#### SQL example

```surrealql
SELECT SupplierName
FROM Suppliers
WHERE EXISTS (
    SELECT SupplierID FROM Products
    WHERE Products.SupplierID = Suppliers.supplierID
    AND Price < 20
    LIMIT 1);
```

### SurrealQL example

```surrealql
SELECT SupplierName
FROM Suppliers
WHERE (
    SELECT SupplierID FROM Products
    WHERE SupplierID = $parent.SupplierID AND Price < 20
    LIMIT 1
);
```

The key difference here is that the inner query can't run without the outer query, as you can see in the `WHERE` statement. Where the defining characteristic of correlated subqueries is that it references a column in the outer query and executes the subquery once for each row in the outer query.

Now you might be wondering, why would we do that?

![Why cat](../../assets/3f79d60f909e43fd.jpg)

There is a straightforward answer to that: it might be more performant, but as always, it depends™

One of the things it depends on is how your query optimiser treats it, but it also depends on how large the table of the inner query is and how complicated the logic is.

In our example, the product table is small and only filters on price, so it's not a big deal to scan the whole table. The reason why `WHERE SupplierID = $parent.SupplierID` can be more performant is because we are limiting the range of possible records/rows to scan to only those relevant to the outer query. In addition we are also adding `LIMIT 1` to the inner query since we are executing the subquery once for each row in the outer query, therefore we can further reduce the rows returned by the inner query.

There are also reasons to do it that are not directly related to performance, such as you could literally run out of memory if the product table were large enough... which we won't cover here so that you won't run out of memory for this blog post 😉

The key thing to remember is that you cannot assume one way is always better as it depends on the above factors and more. Therefore its worth testing both if you need the best performance as the results might surprise you.

## Anti-Joins

You're in for a surprise here... nah, just kidding, It's still a subquery that filters the outer query with the results of the inner query.

The only difference is that it's the opposite of the queries above. Instead of `IN`, it is `NOT IN`, and instead of `EXISTS`, it's `NOT EXISTS`. However since SurrealDB doesn’t use `EXIST` you instead put `!` in front of the subquery, to indicate `NOT EXISTS` like in this SurrealQL example.

```surrealql
SELECT SupplierName
FROM Suppliers
WHERE !(
    SELECT SupplierID FROM Products
    WHERE SupplierID = $parent.SupplierID AND Price < 20
    LIMIT 1
);
```

### SQL join example

Ok ok, enough with the subqueries, let's look at how this compares to a normal SQL join.

#### `LEFT JOIN` example

```surrealql
SELECT DISTINCT Suppliers.SupplierName
FROM Suppliers
LEFT JOIN Products ON Products.SupplierID = Suppliers.supplierID
WHERE Products.price < 20
```

Just to reiterate, the `IN`, `EXIST`, and this `LEFT JOIN` examples all give the same results, they just have a different way of getting there.

This `LEFT JOIN` approach would probably be most people's initial approach, but can you spot why it might be better to use the subquery approach as seen above?

It's because with the `LEFT JOIN` we get duplicate results that we then need to de-duplicate. This might be less performant than the subqueries, but again, it depends™

SurrealDB does not do these typical joins and one of the reasons is this unnecessary computation of getting more data than you need and then spending even more computing resources on de-duplicating/filtering the data back down to what you actually need.

But that leaves the question, how would you do it instead in SurrealDB?

One possibility is using record links:

### SurrealQL record links example

```surrealql
SELECT Suppliers.SupplierName
FROM Products
WHERE price < 20
```

As you can see in this example, things don't need to be complicated.

This example will produce the same result as the semi-joins and the left join, but without any table scan at all due to [how our record IDs work.](/blog/the-life-changing-magic-of-surrealdb-record-ids)(if you're following along, this query will not work with the imported dataset, because that is using SQL numeric IDs instead of SurrealDB record IDs).

If you can make relationships at write time, you can have peace of mind at query time that you're not going to get duplicate data that you then need to remember to de-duplicate. That is even if everyone who has access to this can remember to use the right join conditions to begin with 😅

I hope this clears some of the fears of missing out (FOMO) that you might have about SurrealDB not having traditional SQL joins. You can still do the things you need to do such as with the subqueries. When it comes to the traditional joins though, we think about it more in terms of the joy of missing out (JOMO) because the best way to reduce errors in your code is by [writing less code](https://github.com/kelseyhightower/nocode), as seen in our record links example.

If this has piqued your interest, why not check out our previous [Beyond SQL Joins](/blog/beyond-sql-joins-exploring-surrealdbs-multi-model-relationships) blog post or just [get started with SurrealDB](/docs/surrealdb/installation).
