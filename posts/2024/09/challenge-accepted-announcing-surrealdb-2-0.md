---
title: "Challenge accepted: announcing SurrealDB 2.0"
slug: "challenge-accepted-announcing-surrealdb-2-0"
date: "2024-09-17T00:00:00.000Z"
categories:
  - "releases"
  - "featured"
  - "company"
read_time: "7 min read"
summary: "With the massive community adoption that followed came massive expectations and challenges to live up to these expectations."
source: "https://surrealdb.com/blog/challenge-accepted-announcing-surrealdb-2-0"
cover: "../../assets/f3f8209b3e5b2ee8.jpg"
---

# Challenge accepted: announcing SurrealDB 2.0

![Challenge accepted: announcing SurrealDB 2.0](../../assets/f3f8209b3e5b2ee8.jpg)

When we [announced our 1.0 release](/blog/announcing-surrealdb-1-0), we planted our flag in the database world as a new and upcoming database with the potential of being [the future of database technology](/blog/why-surrealdb-is-the-future-of-database-technology-an-in-depth-look).

With the massive community adoption that followed came massive expectations and challenges to live up to these expectations.

However, the people of SurrealDB - employees and community champions, stepped up with a challenge accepted attitude and solved these challenges with our 2.0 release!

We've made major improvements in:

- [Stability and performance](#stability-and-performance)
- [Querying](#querying)
- [Security](#security)
- [SDKs](#sdks)
- [SurrealML](#surrealml)
- [SurrealKV](#surrealkv)

## Stability and Performance

### New SurrealQL parser

We've rebuilt the SurrealQL parser from the ground up to be faster and more resilient.

It addresses many of the shortcomings of the previous version, offering better error messages and overcoming the limitations of system stack constraints, ensuring that performance remains consistent even as query complexity increases.

Unlike the previous parser, which was based on the [`nom`](https://github.com/rust-bakery/nom) parser-combinator library, the new parser is an optimised recursive descent parser with a separate lexing step. This change allows for more efficient parsing by separating the tokenisation of the input from the parsing logic itself, streamlining the parsing process.

Additionally, the new parser includes new memory management techniques to ensure optimal resource usage, minimising memory overhead during parsing operations.

### Improved caching and transaction layer

The new caching mechanisms introduced in 2.0 significantly improve the performance of SurrealDB by reducing the need to refetch data from the underlying storage engine. The caching layer stores the results of frequently executed requests, allowing subsequent processes to be served from the caching layer. This improvement in the core engine will help to speed up queries which select from and modify the database.

In addition to the revamped transaction layer now providing better consistency and lower latency in distributed environments, which ensures your applications can seamlessly manage high-throughput workloads.

We can see this in practice with our graph queries, where before each field needed to fetched individually and now we fetch them all at once. We have also added a nicer syntax for that.

```surrealql
-- Before we used to fetch each field individually
SELECT
    ->product.category,
    ->product.sub_category,
    ->product.details
FROM order:01G07Z3RJ098G8GK8MCRZCPNF9;

-- Now we fetch them all at once and have a nicer syntax as well
SELECT ->product.{category, sub_category, details}
FROM order:01G07Z3RJ098G8GK8MCRZCPNF9;

```

### Optimised index performance

2.0 introduces several enhancements to indexing. These include improvements to hashing mechanisms, the addition of the [HNSW algorithm](/docs/surrealql/statements/define/indexes#hnsw-hierarchical-navigable-small-world) for AI-driven searches, and the option for [asynchronous indexing](/docs/surrealql/statements/define/indexes#using-concurrently-clause) and [rebuilding indexes](/docs/surrealql/statements/define/indexes#rebuilding-indexes). These updates ensure that your queries are executed quickly, even as your data grows in complexity and volume.

```surrealql
-- Build the HNSW index without blocking operations
DEFINE INDEX mt_pts ON pts FIELDS point
HNSW DIMENSION 4 DIST EUCLIDEAN EFC 150 M 12
CONCURRENTLY;

-- Rebuild the index
REBUILD INDEX mt_pts ON pts;
```

With all these advancements in stability and performance, SurrealDB 2.0 is more than just an upgrade to your database architecture - it's a platform built to handle the complex, high-performance needs of modern enterprises.

## Querying

### SurrealQL enhancements

In SurrealDB 2.0, we've made several improvements to our schema definitions such as the introduction of [literal types](/docs/surrealql/statements/define/field#defining-a-literal-on-a-field) to simplify the definition of complex types

```surrealql
-- Before: define the object then define its contents one by one
DEFINE FIELD addresses
    ON TABLE person
    TYPE object;
DEFINE FIELD addresses.address_line_1
    ON TABLE person
    TYPE string;
DEFINE FIELD addresses.city
    ON TABLE person
    TYPE string;
DEFINE FIELD addresses.country
    ON TABLE person
    TYPE string;
DEFINE FIELD addresses.post_code
    ON TABLE person
    TYPE string;

-- After: define a literal type of an object and its contents
DEFINE FIELD address ON TABLE person TYPE {
  address_line_1: string,
  city: string,
  country: string,
  post_code: string
};
```

We have also changed our default `DEFINE` statement behaviour to only run once, with a new [`OVERWRITE` clause](/docs/surrealql/statements/define/table#using-overwrite-clause) and [`ALTER` statement](/docs/surrealql/statements/alter) for updating the schema.

```surrealql
-- Define a table or overite the definition if it exists
DEFINE TABLE OVERWRITE product TYPE NORMAL SCHEMALESS;

-- Make a specific change to a table definition
ALTER TABLE product SCHEMAFULL;
```

Speaking of updating, we’ve also changed the default behaviour of the [`UPDATE` statement](/docs/surrealql/statements/update) to update only and added a new [`UPSERT` statement](/docs/surrealql/statements/upsert) for the previous create or update behaviour.

```surrealql
-- Will fail if the record doesn't exist
UPDATE product:01GRTTE7DG94R864R67MGDT0QM
SET name = "Surreal T-shirt";

-- Will create the record if it doesn't exist
UPSERT product:01GRTTE7DG94R864R67MGDT0QM
SET name = "Surreal T-shirt";
```

### GraphQL support

SurrealDB 2.0 now has experimental support for [GraphQL](https://graphql.org/), which together with [Surrealist](/docs/surrealdb/querying/graphql/surrealist) makes querying with GraphQL not just possible but a delight.

```surrealql

-- SurrealQL
SELECT name, price FROM product

-- GraphQL
{
    product {
        name
        price
    }
}
```

We’ve added automatic schema generation to enhance your experience. As you define your data models in GraphQL, Surrealist can automatically generate schemas for SurrealDB, saving you time and ensuring your database structure is always in sync with your application’s needs.

```surrealql
DEFINE CONFIG GRAPHQL AUTO;
DEFINE CONFIG GRAPHQL TABLES AUTO FUNCTIONS [fn::foo];
DEFINE CONFIG GRAPHQL TABLES {product: [name, price]};
```

Whether using SurrealQL or GraphQL, 2.0 offers powerful, flexible tools that make data management intuitive and efficient for your applications.

## Security

### Overhauled security framework

Security has been a major focus in 2.0, with significant enhancements aimed at providing robust protection and secure access to your data. Much of this is thanks to your input!

The introduction of the [`DEFINE ACCESS`](/docs/surrealql/statements/define/access) statement, which replaces [`DEFINE SCOPE`](/docs/surrealql/statements/define/scope) and [`DEFINE TOKEN`](/docs/surrealql/statements/define/token), offers greater control over user authentication, session management, and using 3rd-party authentication providers. These changes ensure that your databases are secure by default, with options for fine-tuning security settings to meet your specific needs.

```surrealql
DEFINE ACCESS token ON DATABASE TYPE RECORD WITH JWT
ALGORITHM RS256 KEY
"-----BEGIN PUBLIC KEY-----
MUO52Me9HEB4ZyU+7xmDpnixzA/CUE7kyUuE0b7t38oCh+sQouREqIjLwgHhFdhh3cQAwr6GH07D….";
```

### Enhanced security features

From JWT and token-based authentication to new sanitation functions, 2.0 is designed with enterprise-grade security in mind. These features help safeguard your data against common vulnerabilities while offering the flexibility to integrate with third-party authentication providers, enabling a more interconnected infrastructure.

With SurrealDB 2.0 you now have a security framework that is both comprehensive and adaptable, ensuring that your data is protected in all scenarios.

## SDKs

### Native types

Across our JavaScript, C and Python SDKs, we've implemented powerful new handling for `strings`, `numbers`, `floats`, and `booleans`.

JavaScript, .Net and PHP now leverage our brand-new CBOR protocol, while C and Python are now built on top of the Rust SDK, for even more efficient and accurate data processing. With custom datatypes like `Uuid`, `RecordId`, and `Geometry` now supported, you can expect more versatile and efficient data handling, no matter which language you're working with.

### Type Safety

We’re also committed to making our JavaScript SDK as type-safe and secure as possible. That’s why we’ve ensured out-of-the-box support for TypeScript! You can now enjoy seamless integrations with your favourite frameworks like React, SolidJS, and Vue, making your development process smoother and more efficient. PHP developers will be pleased to know that the same enhanced data handling is now at your fingertips, ensuring that your web applications benefit from the same cutting-edge technology.

## SurrealML

With SurrealML, you can now seamlessly integrate machine learning into your workflows without changing your existing tech stack, enabling you to store, load, and execute models right next to your data, streamlining your processes and saving you valuable time.

You can perform complex queries that compute columns based on calculations from the ML model, and then use these values to filter, group, or order your data.

```surrealql
SELECT * FROM (
  SELECT *,
  ml::house_price_prediction<0.0.1>({
    squarefoot: squarefoot_col,
    num_floors: num_floors_col
  }) AS price_prediction
  FROM house_listing
)
WHERE price_prediction > 177206.21875;
```

You also have the ability to summarise statistics on these results with a single SQL query, keeping your insights up-to-date.

```surrealql
SELECT
    math::min(price_prediction) AS min,
    math::max(price_prediction) AS max,
    math::median(price_prediction) AS median,
    math::mean(price_prediction) AS mean,
    math::stddev(price_prediction) AS stddev,
    math::variance(price_prediction) AS variance,
    math::interquartile(price_prediction) AS interquartile
FROM (
  SELECT *,
  ml::house_price_prediction<0.0.1>({
    squarefoot: squarefoot_col,
    num_floors: num_floors_col
  }) AS price_prediction
  FROM house_listing
)
GROUP BY squarefoot_col
```

SurrealML specialises in seamlessly running your pre-trained models directly within your database, ensuring accurate and efficient data processing right where your data is stored. This allows data scientists and engineers to focus on driving smarter decisions and insights more easily and accurately.

## SurrealKV

We are excited to announce that in SurrealDB `2.0`, we are now debuting our own native key value storage engine - SurrealKV. Built entirely in Rust - like the rest of SurrealDB - SurrealKV is an embedded ACID-compliant key-value storage engine with built-in versioning, that allows for historical or temporal querying.

### Versioned querying

SurrealKV enables immutable data querying, data change auditing, historic aggregate query analysis, and versioned queries across the graph.

Currently, versioning is only possible when running on SurrealKV and you can access this using the `VERSION` keyword and a `datetime`. Here's an example to demonstrate how simple it is to view a snapshot of a table's records at any point in time.

First, let's create the initial version of a record:

```surrealql
CREATE user:john SET name = 'John v1'
```

Let's say that the current time is `2024-08-12 T11:30:00Z` Now update the record:

```surrealql
UPDATE user:john SET name = 'John v2'
```

As expected, normal SELECT without a version returns the latest update

```surrealql
SELECT * FROM user
[[{ id: user:john, name: 'John v2' }]]
```

To get the initial record, use the VERSION clause with the timestamp

```surrealql

SELECT * FROM user VERSION d'2024-08-12T11:03:00Z'
[[{ id: user:john, name: 'John v1' }]]
```

This ground-breaking query functionality, when combined with the advanced multi-model capabilities in SurrealDB, allows you to query data with an additional dimension, without sacrificing on performance, or forcing you to change your query in any other way. By enabling this functionality across records, record links, and graph edges, now you have the ability to time-travel across highly-connected graph data.

Now that SurrealKV is a built-in option to SurrealDB, you can try it out too. To start a database instance with SurrealKV in SurrealDB 2.0, just add the surrealkv prefix and a file name to the [`surreal start`](/docs/surrealdb/cli/start#surrealkv-beta) command.

```cli
surreal start surrealkv://my_database
```

## What’s next?

Building a database is never finished, when you think you’ve reached the summit, you instead see another summit to climb.

The next summit we’re climbing leads into the [Surreal Cloud](/cloud), which our cloud team has been moving heaven and earth to make happen, as you’ll see soon.

Until then, we want to thank you for being on this journey with us!
