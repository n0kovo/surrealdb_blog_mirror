---
title: "Unlocking Streaming Data Magic with SurrealDB: Live Queries and Change Feeds"
slug: "unlocking-streaming-data-magic-with-surrealdb-live-queries-and-change-feeds"
date: "2023-11-20T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "7 min read"
summary: "In this article, you will learn what streaming means with SurrealDB. We will also cover some patterns addressing how users can use streaming in practice."
source: "https://surrealdb.com/blog/unlocking-streaming-data-magic-with-surrealdb-live-queries-and-change-feeds"
cover: "../../assets/999b208377848fd0.jpg"
---

# Unlocking Streaming Data Magic with SurrealDB: Live Queries and Change Feeds

![Unlocking Streaming Data Magic with SurrealDB: Live Queries and Change Feeds](../../assets/999b208377848fd0.jpg)

Streaming transactional data is a difficult problem to solve, with concerns about speed, data accuracy, and duplication, [among others.](https://www.oreilly.com/library/view/streaming-systems/9781491983867) SurrealDB stands out from other databases because it has built-in streaming capabilities, which many others do not have.

In this article, you will learn what streaming means with SurrealDB. We will also cover some patterns addressing how users can use streaming in practice.

## SurrealDB streaming in action: Live Queries and Change Feeds

SurrealDB 1.0 offers two new streaming features: [Change Feeds](/features) and [Live Queries](/features). In this section, we will discuss these features in depth.

## Change Feeds: Historic View Over Time

[Change Feeds](/features) are our take on the [Change Data Capture pattern](https://en.wikipedia.org/wiki/Change_data_capture) you might be familiar with from software design patterns. Changes in the database, such as creating, updating, or deleting, are recorded and played back in another channel. This channel functions as a stream of messages.

Change Feeds are great for ensuring accurate order and consistent replication of tables or databases. They also provide immediate updates on any changes made.

You can transfer data from SurrealDB to a different database. This database is specifically designed for certain queries. You can also send data to a system for auditing. Additionally, you can use it for monitoring trigger conditions or replaying events for disaster recovery. Change Feeds ensure you capture these changes accurately and consistently.

We first [`DEFINE`](/docs/surrealql/statements/define/table#example-usage) the Change Feed:

```surrealql
DEFINE TABLE reading CHANGEFEED 1d;
```

To be able to see the changes we need to [`CREATE`](/docs/surrealql/statements/create) some records:

```surrealql
CREATE reading set story = "Once upon a time";
CREATE reading set story = "there was a database";
```

Then we can consume the Change Feeds by using a [`SHOW`](/docs/surrealql/statements/show) query:

```surrealql
-- Replay changes to the reading table
SHOW CHANGES FOR TABLE reading SINCE "2023-09-07T01:23:52Z" LIMIT 10;
```

An important thing to keep in mind here is that the `SINCE <time>` needs to be after the time the `CHANGEFEED` was defined.

Another thing to note is that defining a `CHANGEFEED` on a table implicitly defines a `CHANGEFEED` on the database as well.

## Live Queries: Real-Time Change Notifications

[Live Queries](/features) are another way to receive a stream of changes. However, Live Queries can only perform on tables, unlike Change Feeds. Live Queries replace the polling pattern that so many applications are accustomed to.

When you want to have a real-time reflection of data, as you would in a dashboard or form with multiple editors, then your standard way of solving that would be to poll the database for changes that you haven’t seen yet.

This is tricky to implement in practice, for instance, how often do you poll the database so that you don’t put unnecessary strain but also get a real-time experience? How many retries do you add to the code, and which errors do you handle instead of bubbling up to the user or logs?

At SurrealDB, we believe real-time is a common feature that people need from databases, and people shouldn’t be forced to have to reimplement this themselves constantly.

Consider a scenario where you want to subscribe to messages in a chat room:

```surrealql
LIVE SELECT author, message, timestamp, reactions FROM chat_table WHERE room="general"
```

One remarkable aspect of this query is that it adheres to [our row-based authorisation](/docs/surrealql/statements/define/field). This ensures that when the query is valid, all users can execute it and will receive only the data relevant to them. Furthermore, this authorisation check is enforced in real time for every message. That means you can revoke permissions or add permissions, and users do not need to re-initialise their queries.

## Diff, Patch, Match: Making Sense of Data Updates

When you are retrieving a stream of updates, you are likely to be correlating the changes against data you already have. We offer a modifier for the query so users can choose the changes they want to see. The selection method is called [Diff-Patch-Match](https://github.com/google/diff-match-patch). It is similar to the changes you would see in your version control software. However, instead of handling lines, it handles objects.

Like the [`UPDATE`](/docs/surrealql/statements/update) statement, live queries only need to include the `DIFF` keyword.

```surrealql
LIVE SELECT DIFF FROM table
```

This will return a Live Query ID as a UUID type, which can be used to manage the live query.

The stream you would receive after that includes the differences that can be applied to the objects you should already have from a previous `SELECT` query.

Here is an example subscription:

```surrealql
LIVE SELECT DIFF FROM test;
```

Now let’s create some data in the database using the CLI

```surrealql
test/test> CREATE test:hugh CONTENT {'name':'hugh'};
-- Query 1
[
        {
                id: test:hugh,
                name: 'hugh'
        }
]

test/test> UPDATE test:hugh SET language="golang";
-- Query 1
[
        {
                id: test:hugh,
                language: 'golang',
                name: 'hugh'
        }
]

test/test> UPDATE test:hugh SET language="rust";
-- Query 1
[
        {
                id: test:hugh,
                language: 'rust',
                name: 'hugh'
        }
]

test/test> UPDATE test:hugh SET language=NONE;
-- Query 1
[
        {
                id: test:hugh,
                name: 'hugh'
        }
]

test/test> DELETE test:hugh;
-- Query 1
[]
```

Now, let's look at what the live query results look like from an application using the [JavaScript SDK](/docs/sdk/javascript):

```javascript
[
    {
        action: 'CREATE',
        result: [
            {
                op: 'replace',
                path: '/',
                value: { id: 'test:hugh', name: 'hugh' },
            },
        ],
    },
    {
        action: 'UPDATE',
        result: [{ op: 'add', path: '/language', value: 'golang' }],
    },
    {
        action: 'UPDATE',
        result: [
            {
                op: 'change',
                path: '/language',
                value: `@@ -1,6 +1,4 @@
-golang
+rust
`,
            },
        ],
    },
    { action: 'UPDATE', result: [{ op: 'remove', path: '/language' }] },
    { action: 'DELETE', result: 'test:hugh' },
];
```

We can see the create event, 3 update events, and delete events all being reflected in the order they occurred in the CLI operation we made. We can also see that the result is an array of changes, with the path and type of change being indicated along with the value.

## Practical Live Query Patterns

Now that we’ve covered the basics of Change Feeds and Live Queries, let’s explore some interesting practical patterns to use them:

### 1. Get and Subscribe

As described earlier, the general pattern people will want to use will be to get a “snapshot” of the data and apply updates to it.

You can do that with the following queries

```surrealql
# Initiate the live query, so that we do not miss any updates
LIVE SELECT * FROM my_table;
# Select the snapshot of the data
SELECT * FROM my_table
```

Now, when you consume from the Live Query, you will have captured all the events that occurred from the start of the snapshot. You should be able to replay the events from the live query notifications on top of the snapshot and arrive at the same state - this works for `CREATE`/`UPDATE`/`DELETE` types.

For the `DIFF` type of events, you may get some incorrect entries because diffs are always relative. You will need to be careful of these at the start of your consumption. Or you start with a non-diff live query and swap it for a diff stream, as shown in a later pattern 4 where queries are swapped without losing events.

### 2. Filtering

Another often-asked question is how filtering works: how can you get the “top 10” results of something? If this were a polling system, you would do a `SELECT` query that matches the criteria. However, [in streaming, query execution behaves slightly differently](https://www.oreilly.com/library/view/streaming-systems/9781491983867). So we can’t easily filter without processing the entire dataset.

You could create a materialised view of the table and then perform a live query from it.

```surrealql
//only need this
DEFINE TABLE my_filtered_table AS
  SELECT id, name, points
  FROM primary_table
  WHERE points in math::top((SELECT VALUE points FROM primary_table), 10)
```

Then we can perform a live query on the materialised view we just created:

```surrealql
LIVE SELECT * FROM my_filtered_table
```

### 3. Artificial Sharding

Sharding which is the process of storing a large database across multiple machines is naturally supported within SurrealDB, but even with sharding, you will want to consider how you arrange your data.

Like the previous example, you can divide data artificially to decrease the number of Live Queries affected by updates.

Assume you have a huge table, and you expect to have a huge number of Live Queries. You can mitigate this strain by having Live Queries only subscribe to subsets of a table.

```surrealql
# Based on location
DEFINE TABLE my_uk_shard AS
  SELECT * FROM my_large_table
  WHERE country = "UK";

DEFINE TABLE my_us_shard AS
  SELECT * FROM my_large_table
  WHERE country = "US";

# Based on id range
DEFINE TABLE my_shard_one AS
  SELECT * FROM my_large_table
  WHERE meta::id(id) <= 1000;

DEFINE TABLE my_shard_two AS
  SELECT * FROM my_large_table
  WHERE meta::id(id) > 1000
  AND meta::id(id) < 2000;
```

Then, when Live Queries are triggered, a smaller number is checked and processed - reducing the duration of the transaction.

This kind of sharding won’t work for [complex records](/docs/surrealql/datamodel/ids) (`LIVE SELECT * FROM my_large_table[2, ..]`). That is because the live query subscription would be executed against the full table instead of a subset. So, to derive a subset, you need a separate table.

### 4. Replacing a live query without losing events

As a final pattern, we will talk about replacing the type of live query. Think of this as updating the live query.

Imagine that we have done a live query with some predicates or conditions:

```surrealql
LIVE SELECT * FROM my_table WHERE something > 50
```

Now, imagine that the conditions change. We need to remain subscribed to the events, but we are only interested in the new conditions.

We can start a second query while still keeping the previous query running:

```surrealql
LIVE SELECT * FROM my_table WHERE something < 50 AND maybe_something = true
```

And then you can kill the original as we no longer need the old results

```surrealql
KILL "previous-live-query-id"
```

## Conclusion

In this blog, we have looked at SurrealDB's new streaming features, [Live Queries](/features) and [Change Feeds](/features). Their versatility allows you to handle a variety of scenarios, from tracking changes in your data to dynamic aggregations to managing pagination, with ease. To learn more about using these features, check out our [documentation](/docs/surrealql/statements/live), our [live stream](https://www.youtube.com/watch?v=zEaQBiNbkoU&pp=ygUMbGl2ZSBxdWVyaWVz), and join our [community on Discord](https://discord.gg/surrealdb) to share your experience!
