---
title: "v1.5.0 is live!🎉"
slug: "v1-5-0-is-live"
date: "2024-05-14T00:00:00.000Z"
categories:
  - "releases"
read_time: "4 min read"
summary: "This new release comes with performance updates and new additions to Vector Search"
source: "https://surrealdb.com/blog/v1-5-0-is-live"
cover: "../../assets/7aa0130658a9e011.jpg"
---

# v1.5.0 is live!🎉

![v1.5.0 is live!🎉](../../assets/7aa0130658a9e011.jpg)

We are thrilled to announce the release of SurrealDB 1.5.0! This update includes new features, including some notable ones, like the addition of the HNSW index and enhancements that improve the flexibility and performance of our database system. Grab some popcorn and take a look at some of the highlights of the 1.5 release!

Check out our [release page](/releases#v1-5-0) for the complete list of updates, improvements and bug fixes. If you haven't installed SurrealDB yet, you can install it [here](/docs/surrealdb/installation).

## Implementation of the HNSW index

SurrealDB 1.5.0 brings an exciting update to our indexing capabilities with the implementation of the HNSW algorithm. Known for its speed and efficiency in handling approximate nearest neighbour searches, [HNSW](/docs/surrealql/operators#hnsw-method-since-150) is now part of our in-memory operations.

Here’s how you can utilise this new feature: Add a few vector records to a table `pts`.

```surrealql
CREATE pts:1 SET point = [1,2,3,4];
CREATE pts:2 SET point = [4,5,6,7];
CREATE pts:3 SET point = [8,9,10,11];
```

Define an [HNSW index](/docs/surrealql/statements/define/indexes#hnsw-hierarchical-navigable-small-world-since-150) on the field `point`

```surrealql
DEFINE INDEX hnsw_pts ON pts FIELDS point HNSW DIMENSION 4 DIST EUCLIDEAN TYPE F32 EFC 500 M 12;
```

With the help of vector operations, you can find the approximate nearest neighbours to a given point from an existing dataset.

```surrealql
LET $pt = [2,3,4,5];
SELECT
  id,
  vector::distance::euclidean(point, $pt) AS dist
  FROM pts
  WHERE point <|2,100|> $pt;

SELECT
  id
  FROM pts
  WHERE point <|2,100|> $pt
  EXPLAIN;
```

Here `pts:1` and `pts:2` are nearest to the given point.

```surrealql
[[{ dist: 2f, id: pts:1 }, { dist: 4f, id: pts:2 }]]
[[{ detail: { plan: { index: 'hnsw_pts', operator: '<2,100>', value: [2, 3, 4, 5] }, table: 'pts' }, operation: 'Iterate Index' }, { detail: { type: 'Memory' }, operation: 'Collector' }]]
```

## Introducing the Rebuild command

In this release, we have introduced a powerful new command: [REBUILD](/docs/surrealql/statements/rebuild). This command is essential for maintaining the efficiency of your indexes, especially for M-TREE and HNSW indexes, which can degrade over time due to frequent updates. Rebuilding the index will ensure that it is fully optimised.

```surrealql
REBUILD INDEX hnsw_pts ON TABLE pts;
```

You can also use it along with an if exists clause

```surrealql
REBUILD INDEX IF EXISTS hnsw_pts ON TABLE pts;
```

## The parser will no longer overflow the stack

To prevent stack overflows in our recursive descent parser, we have integrated the reblessive library into the parser. Reblessive is a heap-allocated runtime for deeply recursive algorithms. The [reblessive library](https://github.com/DelSkayn/reblessive) moves state, which would normally be stored on the stack onto a fast heap structure, preventing any query, even very deeply nested ones, from overflowing the stack and causing a crash.

## Improvements to the Query Planner

The query planner has been upgraded to detect when a query specifically targets data in another table. As a result, the execution plan now incorporates an index-backed iterator strategy for navigating through record links. So, if you had indexes defined on the following tables

```surrealql
-- Define an index on the 'invoices' and 'transactions' table.
DEFINE INDEX idx_transaction_id ON TABLE invoices COLUMNS transaction;
DEFINE INDEX idx_transaction_name ON TABLE transactions COLUMNS transaction_name;
```

And one of the fields was a record link between the invoices and transactions.

```surrealql
DEFINE FIELD transaction_name ON TABLE transactions TYPE string;
DEFINE FIELD transaction ON TABLE invoices TYPE record<transactions>;
```

You can fetch all invoices linked to transactions named 'hardware purchase'.

```surrealql
-- Create two transactions with the same name.
CREATE transactions:1 SET transaction_name = 'hardware purchase';
CREATE transactions:2 SET transaction_name = 'hardware purchase';

-- Create two invoices referencing the transactions created above.
CREATE invoices:A SET transaction = transactions:1;
CREATE invoices:B SET transaction = transactions:2;

-- Explain the execution plan for a query that fetches all invoices linked to transactions named 'hardware purchase'.
SELECT * FROM invoices WHERE transaction.transaction_name = 'hardware purchase' EXPLAIN;

-- Execute the query to fetch all invoices linked to transactions named 'hardware purchase'.
SELECT * FROM invoices WHERE transaction.transaction_name = 'hardware purchase';
```

```surrealql
[
  [
    {
      detail: {
        plan: {
          index: 'idx_invoice_transaction',
          joins: [
            {
              index: 'idx_transaction_name',
              operator: '=',
              value: 'hardware purchase'
            }
          ],
          operator: 'join'
        },
        table: 'invoices'
      },
      operation: 'Iterate Index'
    },
    {
      detail: {
        type: 'Memory'
      },
      operation: 'Collector'
    }
  ],
  [
    {
      id: invoices:A,
      transaction: transactions:1
    },
    {
      id: invoices:B,
      transaction: transactions:2
    }
  ]
];
```

## On-disk temporary tables for large result sets

Our new FileCollector structure handles large result sets that do not fit into memory, generating an OOM (Out of Memory error). Using a temporary directory on disk for storage, the FileCollector ensures that sorting and processing large datasets do not lead to memory overflows. This new file collector is used when the datastore is file-based (SurrealKV, RocksDB, Speedb) or remote-based (Tikv, FDB). Here's how you can configure the temporary directory using the SurrealDB [start command](/docs/surrealdb/cli/start#command-help)

```cli
# Setting the directory for storing temporary database files
surreal start --temporary-directory /path/to/tempdir file:mydatabase.db
```

You can also set up the temporary directory via the environment variable.

```cli
export SURREAL_TEMPORARY_DIRECTORY=/path/to/tempdir
surreal start file:mydatabase.db
```

## sql2 and jwks stabilization

Previously, in order to use the `sql2` and `jwks` features, you had to `export RUSTFLAGS="--cfg surrealdb_unstable"` before building the Rust SDK. With the 1.5 release, the `sql2` and `jwks` features are no longer unstable and the command is not needed anymore.

## Improvements to the Tree cache for Mtree and Btree

It was observed that the Tree cache (cache for BTree and MTree-based indexes) was flushed with every new version of the index. This was affecting the performance as read counts increased. In 1.5, by replacing the previous BTreeMap with a HashMap and precomputing hashes for vectors, the index now benefits from faster lookup times. The update also introduces flexibility in setting MTree index parameters in any order and ensures proper handling of the vector type setting. Overall, this improvement is aimed at making the indexing experience better for everyone.

## Polling rate for change feeds and live queries changed back to 10s

The community reported a performance drop since increasing the polling rate for Live queries and Change Feeds to 1s. Hence, after carefully studying all the logs and instances, it has been changed back to 10s.

## Explore more and stay updated

Continuing our commitment towards better developer experience, we have more examples and reference guides coming up around SurrealDB and SurrealQL. We encourage you to explore these changes by checking out our detailed [release notes](/releases#v1-5-0) and updated [documentation](/docs/surrealdb).

Thank you for your continued support and enthusiasm for SurrealDB. We are excited to see how you integrate these new capabilities into your applications! [Try out](/install) the new release and let us know your feedback.
