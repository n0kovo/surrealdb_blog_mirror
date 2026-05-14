---
title: "What's new for developers in SurrealDB Beta 10"
slug: "whats-new-for-developers-in-surrealdb-beta-10"
date: "2023-09-04T00:00:00.000Z"
categories:
  - "releases"
read_time: "5 min read"
summary: "Hello Developers! After months of hard work, we're excited to roll out v1.0.0-beta.10. Here's what's new!"
source: "https://surrealdb.com/blog/whats-new-for-developers-in-surrealdb-beta-10"
cover: "../../assets/92184fccc73ffda4.jpg"
---

# What's new for developers in SurrealDB Beta 10

![What's new for developers in SurrealDB Beta 10](../../assets/92184fccc73ffda4.jpg)

Hello Developers!

After months of hard work, we're excited to roll out v1.0.0-beta.10.

This [release](/releases) is packed with features and improvements that we believe will make your development experience smoother and more efficient. From cleaner syntax for default clauses and robust typing options to powerful new capabilities like full-text search and real-time live queries, there's a lot to explore. We've also enhanced our authentication mechanisms and introduced vector functions for advanced data manipulation.

This release includes a lot of contributions and feature suggestions from the community.

Let's dive right into it and see what's new:

### Default Clauses: Cleaner and More Intuitive

Remember the old way of setting default values?

```surrealql
DEFINE FIELD published ON article
    TYPE boolean
    VALUE $value ?? $before ?? true
;
```

Well, we've streamlined it:

```surrealql
DEFINE FIELD published ON article TYPE boolean DEFAULT true;
```

This not only simplifies the syntax but also ensures the type is the one defined by the user for the `$value` variable.

### Typing: More Robust and Flexible

We've made some significant tweaks to the typing system:

- Strict typing right out of the box.

No more:

```surrealql
DEFINE FIELD age ON person TYPE number ASSERT $value != NONE && $value != NULL;
```

Just use:

```surrealql
DEFINE FIELD age ON person TYPE number;
```

- Optional types, multi-type fields, and advanced array types, including fixed-length arrays.

```surrealql
-- The type is optional, meaning it can be a number or NULL.
DEFINE FIELD age ON person TYPE option<number>;

-- an array of strings with a fixed length of 5.
DEFINE FIELD age ON person TYPE array<string, 5>;

-- Nested array elements still need to be defined however!
DEFINE FIELD age.* ON person TYPE string;
```

- And yes, we've transitioned to arrow brackets for consistency:

```surrealql
DEFINE FIELD author ON article TYPE record<person>
```

You can read more about it on the [`DEFINE FIELD` statement](/docs/surrealql/statements/define/field) docs

### Full-Text Search: More Power to Your Queries

We've introduced a full-text search capability. Here's a taste:

```surrealql
SELECT search::score(1) AS score,
search::highlight('<b>', '</b>', 1)
AS title FROM book
WHERE title @1@ 'rust web'
ORDER BY score DESC;
```

It even accounts for multi-lingual semantic nuances. And while we're still working on phrase and regex/wildcard queries, we believe this is a solid start.

You can also check out a non-production [web indexer](https://github.com/surrealdb/web-indexer) we built to understand how full-text search works.

### Secondary Indexing: Speed and Integrity

Secondary indexing is here, and with it, a query planner. Here's how you can use it:

##### Unique Index:

Prevent creating or updating a record with a value that already exists in another record.

```surrealql
DEFINE INDEX email ON TABLE user COLUMNS email UNIQUE;
```

##### Non-unique index:

Unlike unique indexes, which enforce data integrity by preventing duplicate entries, non-unique indexes focus solely on speeding up data retrieval.

When you execute a query with a `WHERE` clause that filters based on an indexed field, the query planner kicks in. Instead of scanning the entire table, it only traverses the records returned by the index, making your queries faster and more efficient.

```surrealql
-- Optimise queries looking for users of a given age
DEFINE INDEX userAgeIndex ON TABLE user COLUMNS age;
```

Now, when you run a query like `SELECT * FROM user WHERE age = 30;`, the query planner will use the `userAgeIndex` to quickly locate all users who are 30 years old, skipping the need for a full table scan.

##### Limitations:

Currently, the query planner only supports the `=` operator for non-unique indexes. This means range queries won't benefit from the index just yet. Also, non-unique indexes are not used for sorting operations.

We're actively working on expanding the capabilities of this feature, so keep an eye out for updates in future releases.

### Live Queries: Real-Time Events, Simplified

Get real-time events from transactions with [Live Queries](/docs/surrealql/statements/live). It's designed for real-time updates that don't require strict consistency.

When you execute a `LIVE SELECT` query, it triggers an ongoing session that captures any subsequent changes to the data in real-time and SurrealDB will push the entire record over the WebSocket when created or updated, and just the record's ID when deleted.

```surrealql
LIVE SELECT * FROM person;
```

You can also get [JSON patches](https://jsonpatch.com) and filter the live queries.

```surrealql
LIVE SELECT DIFF FROM person;
```

```surrealql
LIVE SELECT * FROM person WHERE age > 18;
```

You can also use the `KILL` [statement](/docs/surrealql/statements/kill) to terminate a running live query.

```surrealql
KILL '0189d6e3-8eac-703a-9a48-d9faa78b44b9';
```

### Authentication

We've beefed up our [authentication mechanisms](/docs/surrealdb/security/authentication) in SurrealDB, and here's a quick rundown:

### System Users

Users defined at various levels (root, namespace, or database) with roles like `OWNER`, `EDITOR`, and `VIEWER`.

It is now possible to define multiple root users in SurrealDB.

Quick Examples:

- Root-level user:

```surrealql
DEFINE USER john ON ROOT PASSWORD 'VerySecurePassword!' ROLES OWNER;
```

- Database-level user:

```surrealql
DEFINE USER mary ON DATABASE PASSWORD 'VerySecurePassword!' ROLES EDITOR;
```

### Scope Users

You can now customise your sign-in and sign-up logic, turning SurrealDB into a potential all-in-one BaaS.

Key Points:

- Define your own SIGNUP and SIGNIN logic.
- Set session durations with SESSION.

```surrealql
DEFINE SCOPE user SESSION 1d
    SIGNIN (
        SELECT * FROM user
            WHERE email = $email
            AND crypto::argon2::compare(password, $password)
    )
    SIGNUP (
        CREATE user CONTENT {
            name: $name,
            email: $email,
            password: crypto::argon2::generate($password)
        }
    )
;
```

SurrealDB uses a [crypto function](/docs/surrealql/functions/database/crypto) to hash the password.

### Vector Functions

Here's a quick rundown of the [vector functions](/docs/surrealql/functions/database/vector) now at your fingertips in SurrealQL:

Elementary Operations: Add, subtract, multiply, or divide elements in your vectors with `vector::add()`, `vector::subtract()`, `vector::multiply()`, and `vector::divide()`.

```surrealql
RETURN vector::add([1, 2, 3], [1, 2, 3]);
-- Output: [2, 4, 6]
```

Advanced Calculations: Calculate dot products with `vector::dot()`, find the angle between vectors using `vector::angle()`, or get the cross product with `vector::cross()`.

```surrealql
RETURN vector::dot([1, 2, 3], [1, 2, 3]);
-- Output: 14
```

Distance and Similarity Metrics: Compute various distance metrics like Euclidean (`vector::distance::euclidean()`) or Manhattan (`vector::distance::manhattan()`) distances, and similarity coefficients such as Cosine similarity (`vector::similarity::cosine()`).

```surrealql
RETURN vector::distance::euclidean([10, 50, 200], [400, 100, 20]);
-- Output: 432.43
```

Why should you care?

These functions open up a world of possibilities for advanced data manipulation right within your database queries. No need to export your data to specialised software for these computations - you can now do it all in SurrealDB!

So, whether you're calculating the trajectory for a SpaceX launch or just trying to find the cosine similarity between user preferences, Vector Functions have got you covered.

### Looking Ahead

We've taken you through a whirlwind tour of some features of SurrealDB Beta 10, highlighting the leaps we've made since Beta 9.

Our commitment is to provide you with a database experience that's not just fast but also intuitive. And while Beta 10 offers a glimpse into our vision, the production-ready version set to be unveiled at SurrealDB World promises even more.

And for those eager to see what's next, mark your calendars for [SurrealDB World](https://surrealdb.world). It's not just a product launch; it's where we celebrate our shared journey and look forward to the road ahead.

[Register for SurrealDB World Here](https://surrealdb.world)!

Together, let's redefine database innovation. See you at SurrealDB World!
