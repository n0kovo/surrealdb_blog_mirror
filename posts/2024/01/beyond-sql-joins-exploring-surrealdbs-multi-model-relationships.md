---
title: "Beyond SQL Joins: Exploring SurrealDB's Multi-Model Relationships"
slug: "beyond-sql-joins-exploring-surrealdbs-multi-model-relationships"
date: "2024-01-29T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "6 min read"
summary: "Can't join? No worries, we can relate."
source: "https://surrealdb.com/blog/beyond-sql-joins-exploring-surrealdbs-multi-model-relationships"
cover: "../../assets/43c023ac551261d0.jpg"
---

# Beyond SQL Joins: Exploring SurrealDB's Multi-Model Relationships

![Beyond SQL Joins: Exploring SurrealDB's Multi-Model Relationships](../../assets/43c023ac551261d0.jpg)

How many ways can you join your data without using traditional SQL joins? As SurrealDB is a multi-model database, it has different ways "joining" data together.

In this blog post, we'll cover the three primary ways of creating relationships inspired by document and graph data models.

We’ll start off with embedded records, which are a key component of document-style databases.

When we

```surrealql
SELECT * FROM person
```

We can see the whole person record.

```json
[
    {
        "address": {
            "address_line_1": "767 Culkeeran",
            "address_line_2": null,
            "city": "Matlock",
            "coordinates": [-51.195338, 114.885025],
            "country": "England",
            "post_code": "MU1P 0XX"
        },
        "company_name": null,
        "email": "said1813@example.com",
        "first_name": "Caprice",
        "id": "person:00e1nc508h9f7v63x72o",
        "last_name": "Huber",
        "name": "Caprice Huber",
        "phone": "0115 262 2984"
    }
]
```

The key thing to notice here is that the address field is an embedded record.

That means that instead of the address field containing the primary key to an address table, like in relational databases, we can de-normalise the data so that we can skip making joins entirely when we want the full information for the person record.

The tradeoff we are making here is wanting faster queries by using more storage space.

## Embedded records

Working with embedded records is simple. We can select just the address field to get the address record or in other words the address object.

```surrealql
SELECT
  address
FROM person
```

```json
[
    {
        "address": {
            "address_line_1": "767 Culkeeran",
            "address_line_2": null,
            "city": "Matlock",
            "coordinates": [-51.195338, 114.885025],
            "country": "England",
            "post_code": "MU1P 0XX"
        }
    }
]
```

We use the dot notation to select a field inside the object, for example, selecting the coordinates field.

```surrealql
SELECT
  address.coordinates
FROM person
```

```json
[
    {
        "address": {
            "coordinates": [-51.195338, 114.885025]
        }
    }
]
```

We use the bracket notation to select just the first item in the coordinates array.

```surrealql
SELECT
  address.coordinates[0]
FROM person
```

```json
[
    {
        "address": {
            "coordinates": -51.195338
        }
    }
]
```

There is no limit to the depth of objects and arrays you can embed inside a record, allowing you to model complex data scenarios and navigate them simply with a combination of dot and bracket notation.

## Record links

This brings us to record links, which enable you to create normalised data models by linking records together.

When we

```surrealql
SELECT * FROM review
```

We can see that this table is primarily made up of record IDs pointing to other records.

```json
[
    {
        "artist": "artist:73z6oc419v1c5v34j20x",
        "id": "review:00a0ic854u4j7z02s00v",
        "person": "person:67s8cp304i4p6p83q02d",
        "product": "product:41v2qv923h3o7s55e96l",
        "rating": 3,
        "review_text": "repeat languages.."
    }
]
```

In SurrealDB we don’t use the primary & foreign key pairs. Instead we use record IDs, which are like primary keys that we just directly embedded in places where a foreign key would otherwise be.

This allows us to traverse from record-to-record without needing to run a table scan query, because the query planner knows exactly what table and record the id belongs to. Therefore, it just directly fetches the record instead of searching for a needle in a haystack.

Working with record links is as simple as working with embedded objects. You simply use the dot and bracket notations as if the data was all embedded in one record.

```surrealql
SELECT
  rating,
  product.name
FROM review
```

```json
[
    {
        "product": {
            "name": "ago classifieds"
        },
        "rating": 3
    }
]
```

You can also select multiple fields and have them grouped together under the product object.

```surrealql
SELECT
  rating,
  product.name,
  product.category
FROM review
```

```json
[
    {
        "product": {
            "category": "digital art",
            "name": "ago classifieds"
        },
        "rating": 3
    }
]
```

Or you can alias them and have them show up as individual fields, there is a lot of flexibility here.

```surrealql
SELECT
  rating,
  product.name as product_name,
  product.category as product_cat
FROM review

```

```json
[
    {
        "product_cat": "digital art",
        "product_name": "ago classifieds",
        "rating": 3
    }
]
```

Notice also that this completely eliminates the typical complexity and errors people make with joins. Such as not knowing the grain of the data and whether you need a left, right, inner, outer, lateral, or cross join.

Making the wrong choice can lead to a lot of headaches and perhaps some angry database administrators.

Now you might be wondering, what is the tradeoff behind the magic of record links?

The key tradeoff is referential integrity, which, while important, is not always needed.

But when it's needed, we have a way to preserve referential integrity using graph traversal, which we will cover next.

## Graph relations

SurrealDB introduces a `relate` statement to SQL for making graph relationships.

A short introduction to working with graph data is that you have nodes connected by edges.

![Relate statement - node edge node](../../assets/aa9b581e6c2a9660.jpg)

Here, we can see that the person is a node, the order is an edge, and the product is also a node.

Another way to think about it is in terms of nouns connected by verbs, such that it forms a sentence.

![Relate statement - node edge node](../../assets/b8a9ab7b8e834719.jpg)

In our example, person order product.

Most graph databases work with these [semantic triples](https://en.wikipedia.org/wiki/Semantic_triple).

### SurrealDB vs graph-only databases

However, what sets SurrealDB apart from graph-only databases is that our edges are also real tables, enabling you to store information in them and allowing for even more flexible data models.

```surrealql
RELATE person:00e1nc508h9f7v63x72o -> order -> product:09r8bs593p1b3d41v83d
CONTENT {
       "currency": "£",
       "discount": ->product.discount,
       "order_date": time::now(),
       "order_status": "pending",
       "payment_method": "PayPal",
       "price": ->product.price,
       "product_name": ->product.name,
       "quantity": 1,
       "shipping_address": <-person.address
   };

```

In this instance order is actually an order items table, which has its own information along with information joined from the person and product tables.

Because we have specified the relationship in the `relate` statement, it becomes easy and efficient to fetch the required fields from the joined tables.

As you can see when we start getting the fields from the product table, the arrow syntax differentiates this from the record links we saw in the earlier example.

Aside from starting with the arrow syntax, you would use the dot and bracket syntax in exactly the same way as record links or embedded objects.

Notice also that the direction of the arrow changes whether we are fetching from the product or person table.

Looking at the `relate` statement again, we can see that we only specified one direction, going from person to order to product.

```surrealql
RELATE person:00e1nc508h9f7v63x72o -> order -> product:09r8bs593p1b3d41v83d
```

SurrealDB however, has bi-directional querying by default that therefore enables us to specify it once but use it in both directions.

### The two ways of traversing the graph

When we now

```surrealql
SELECT * FROM order
```

we can see the record we created in the order edge table.

```json
[
  {
      "currency": "£",
      "discount": null,
      "id": "order:['England', '2023-02-21T21:16:06.236861']",
      "in": "person:00e1nc508h9f7v63x72o",
      "order_date": "2023-02-21T21:16:06.236861",
      "order_status": "processing",
      "out": "product:09r8bs593p1b3d41v83d",
      "payment_method": "credit card",
      "price": 24954.01,
      "product_name": "management console",
      "quantity": 1,
      "shipping_address": {...}
  }
]
```

I want to bring your attention to 3 specific fields, those are in, id and out.

```surrealql
SELECT
  in,
  id,
  out
FROM order
```

```json
[
    {
        "id": "order:['England', '2023-02-21T21:16:06.236861']",
        "in": "person:00e1nc508h9f7v63x72o",
        "out": "product:09r8bs593p1b3d41v83d"
    }
]
```

Now you might be wondering, when were these created since it didn’t seem like we specified them before.

We did specify the in and out field with the `relate` statement and because we didn’t specify the order ID, it was generated for us.

![Relate statement - in id out](../../assets/a377ce6ff22c5506.jpg)

Another way of looking at the `relate` statement is that the first node is called `in`, the edge is the `id`, and the second node is the `out`.

Now I want to bring your attention to the following select statement, which shows how you can select the same fields using the arrow syntax.

```surrealql
SELECT
  <-person,
  id,
  ->product
FROM order
```

Both of these approaches are valid ways of querying the data.

### Complex queries made simple

Graph relations can be both super powerful and elegant once you get more comfortable using them.

In the following example, we create a simple recommendation system in one query.

```surrealql
SELECT
  ->order->product<-order<-person->order->product
FROM person:00e1nc508h9f7v63x72o
```

```syntax
[
   {
       "->order": {
           "->product": {
               "<-order": {
                   "<-person": {
                       "->order": {
                           "->product": [
                           "product:09r8bs593p1b3d41v83d",
                            "product:53c8dz218n0u1k22a70y",
        …
```

What this is saying is, based on all the products this person ordered, which persons also ordered those products and what did they order?

Breaking it down:

```surrealql
-- Focusing on the person
person:00e1nc508h9f7v63x72o

-- Which products did they order?
->order->product

-- Which persons also ordered those products?
<-order<-person

-- And what did they order?
->order->product
```

If we were to express this logic using SQL joins we would need up to 6 of them, as we are joining 3 tables at different levels of granularity, and then a where clause to filter on the specific person.

When doing multiple joins like this, you really start to see the advantages of the graph model.

There are always tradeoffs to each approach, and the tradeoff we are making here is establishing the relationships at write time to make it simpler and easier for everyone at query time.

You can see more discussions around graph relations in our [SurrealDB Stream #17: How To Improve Your (Database) Relationships](https://www.youtube.com/watch?v=ffzxt0iToWs)

## More to come

However, what if we want to make arbitrary relationships on the fly similar to relational style joins?

We have ways of doing that, but that is a topic for [another blog post](/blog/thinking-inside-the-box-relational-style-joins-in-surrealdb), so make sure you subscribe to get notified when that comes out.

Also you can run the above queries and more using our [demo data, which you can find in our docs.](/docs/surrealql/demo)
