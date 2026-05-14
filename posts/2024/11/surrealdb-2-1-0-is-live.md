---
title: "SurrealDB 2.1.0 is live!"
slug: "surrealdb-2-1-0-is-live"
date: "2024-11-21T00:00:00.000Z"
categories:
  - "releases"
read_time: "6 min read"
summary: "We are excited to announce the release of SurrealDB 2.1.0, our latest version of our scalable cloud graph database."
source: "https://surrealdb.com/blog/surrealdb-2-1-0-is-live"
cover: "../../assets/054f88e57bd96a85.jpg"
---

# SurrealDB 2.1.0 is live!

![SurrealDB 2.1.0 is live!](../../assets/054f88e57bd96a85.jpg)

We are thrilled to announce the release of SurrealDB 2.1.0! This update includes major enhancements to graph querying and a prominent new role for our custom-built storage backend SurrealKV. Explore our [release page](/releases#v2-1-0) for a detailed overview of all the updates, including enhancements in security, performance and stability, as well as a comprehensive list of bug fixes.

## Recursive graph traversal

SurrealDB 2.1.0 marks an important release, expanding our suite of graph querying capabilities, now introducing the ability to recursively walk graph relations or record links with an easy to use syntax. With the ability to retrieve a flat result or tree-like data structures, allowing you to collect details at each level of depth, this feature unlocks numerous new use-cases previously not possible.

```surrealql
-- Select all people who connect to a person, 3 levels deep
SELECT *, @{3}->knows->person AS connections_3rds FROM person;

-- Select page:main with its id, name and nested pages, at least 3 and at most 5 pages deep
-- Here, the recursive pattern will repeat at the `@` symbol, creating an arbitrary depth tree-like data structure
page:main.{3..5}.{ id, name, contains: <-contained_in<-page.@ };
-- Recursive idioms work with any idiom parts, not limited to graphs
-- Here, we recursively fetch friends and then collect their names
person:tobie.{1..5}(.friend).name
```

## Cross-transaction caching

In `2.1.0` we have added a cross-transaction caching layer to the document processing layer, ensuring that all `DEFINE FIELD`, `DEFINE INDEX`, `DEFINE EVENT`, `DEFINE TABLE ... AS`, and `LIVE SELECT` statement definitions are loaded initially, and then cached. Subsequent requests or transactions can then use the cached statement definitions, removing the need to perform 5 additional range scans.

The caching works by specifying a cache version (an uuid value) for each definition type on the `DEFINE TABLE` statement definition. As this table definition is always fetched for each table (for which a document is being processed) within each transaction, we can always detect when the cached statement definitions are in need of being refreshed. When we detect an invalid cache entry, we refetch the relevant definitions from the storage engine. Importantly, each statement definition type (fields, events, indexes, foreign tables, live queries) are cached separately, so modifying any one of those statement types will not invalidate the other types. This change greatly reduces the number of requests on the key-value store, and allows for cross-transaction caching in embedded, single-node, and distributed environments.

The only downside to this addition is that any concurrent additions or modifications of fields, events, indexes, foreign tables, or live queries, will now need to update the table definition, leading to potential concurrent editing conflicts if executed at exactly the same time. This is probably not an issue for `DEFINE` statements, but might be more visible when there are many concurrent `LIVE SELECT` or `KILL` statements on a table.

The cache is bounded, only storing 1000 entries (although this is configurable with the `SURREAL_DATASTORE_CACHE_SIZE` environment variable). Least recently used cache entries will be replaced with more recent entries.

So for instance if you run the following query, we will use 5 cache entries (1 for the fields, 1 for the indexes, 1 for the events, 1 for the foreign tables, and 1 for the live queries):

```surrealql
SELECT * FROM person:tobie;
```

If you then run a different query, then we will use an additional 5 cache entries (1 for the fields, 1 for the indexes, 1 for the events, 1 for the foreign tables, and 1 for the live queries):

```surrealql
SELECT * FROM product:tshirt;
```

So effectively using the default caching parameter, we can cache the definitions for 200 tables. This is for a single SurrealDB node, and the items which are cached could be different on another SurrealDB node in a cluster, depending on the queries which are executed against each node.

## Streaming imports

With the new release, imports are now streamed. Previously, when running an import, the entire import had to be parsed before it could be run. This introduced limitations on the size of imports as they had to fit within the available system memory. With the introduction of streaming imports, the import query is now parsed and run statement by statement. This makes it possible to import datasets without issue, even if they exceed a computer's available memory

## SurrealKV enhancements

SurrealKV is now used for our in-memory instances. Our previous storage solution did not allow concurrent transactions. SurrealKV allows concurrent transactions and is therefore significantly faster. Additionally, we have optimised for the database load times when restarting surrealkv, further improving efficiency.

## Improved UPSERT statement behaviour

In `2.1` the behaviour of the `UPSERT` statement from versions `2.0.0` -> `2.0.4` has also been improved to correctly handle existing index entries, `WHERE` conditions, and when generating new records without specifically setting the RecordID. Let’s take a look at some examples of the improvements.

When using a `UNIQUE` index combined with the `UPSERT` statement, SurrealDB will now fetch the record from the index if it already exists. If a specific RecordID has been specified for the statement, then an error will be returned in the event that the index is already populated with a matching unique value for a different record.

```surrealql
-- This will define a unique index on the table
DEFINE INDEX OVERWRITE testing ON person FIELDS one, two, three UNIQUE;
-- This will create a record, and populate the unique index with this record id
UPSERT person SET one = "something", two = "something", three = "something";
-- This will update the record, returning the same record id created in the statement above
UPSERT person SET one = "something", two = "something", three = "something";
-- This will throw an error, because the unique index already has a record with a different record id
UPSERT person:test SET one = "something", two = "something", three = "something";

```

Another example regarding the `WHERE` clause is that in `2.1` when no RecordID has been specifically set, the iterator will first fetch records from storage. If records already exist which match the `WHERE` clause, then these records will be updated. Otherwise, a new record will be created if no records are found.

```surrealql
-- This will return the created record as no matching records exist
UPSERT person SET name = 'Jaime' WHERE name = 'Jaime';
-- This will return the updated record, because a matching record exists, and the WHERE clause matches
UPSERT person SET name = 'Tobie' WHERE name = 'Jaime';
-- This will return a newly created record, because the WHERE clause does not match
UPSERT person SET name = 'Tobie' WHERE name = 'Jaime';

```

For more information on the `UPSERT` statement works with records, please refer to the [`UPSERT` documentation](/docs/surrealql/statements/upsert)

## Improve functions

This release also introduces some new functions, and improvements to existing ones.

The `type::field()` and `type::fields()` functions can now be used in more projections, like `WHERE` clauses in `SELECT` statements.

```surrealql
LET $field = "foo";  
SELECT type::field($field) FROM person WHERE type::field($field) == "bar";  
```

We introduced two new array methods too: `array::fold()` and `array::reduce()`. These methods allow you to walk over array values and collect them into something else, like an object, string or number as an example.

```surrealql
"I am a forwards string"  
  .split('')  
  .fold("", |$one, $two| $two + $one);  
```

Lastly, we introduced new string distance and similarity functions, allowing you to find distance and similarity between two strings.

```surrealql
// No distance (0)
RETURN string::distance::hamming("", "");
RETURN string::distance::hamming("hamming", "hamming");
// Distance of 3
RETURN string::distance::hamming("hamming", "hammers");
// Distance of 2
RETURN string::distance::hamming("hamming", "h香mmüng");;
// Distance of 14
RETURN string::distance::hamming("Friedrich Nietzs", "Jean-Paul Sartre");
```

## Additional changes

Some additional note-worthy changes include:

- Allow configuration over what to export. This functionality will soon be implemented into Surrealist, our graphical user interface for SurrealDB, allowing for easy customised exports of your databases.
- Improvements to experimental bearer access type
- Improved error logging and handling in authentication
- Introduce ability to run database initialisation query
- Expand static value list for `DEFAULT` clause

## Explore more and stay updated

To see the full list of enhancement please [check out our release notes](/releases), and [documentation](/docs/surrealdb). Thank you for your continued support and enthusiasm for SurrealDB. We are excited to see how you integrate these new capabilities into your applications! [Install](/install) the new release and let us know your feedback.
