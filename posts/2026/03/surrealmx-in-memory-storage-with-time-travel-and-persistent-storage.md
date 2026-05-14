---
title: "SurrealMX: In-memory storage with time travel and persistent storage"
slug: "surrealmx-in-memory-storage-with-time-travel-and-persistent-storage"
date: "2026-03-25T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "6 min read"
summary: "SurrealMX lets you use in-memory storage along with optional time travel versioned queries and two types of persistent storage with a large number of configurations to balance performance with durability."
source: "https://surrealdb.com/blog/surrealmx-in-memory-storage-with-time-travel-and-persistent-storage"
cover: "../../assets/e0920a4978c72390.jpg"
---

![SurrealMX: In-memory storage with time travel and persistent storage](../../assets/e0920a4978c72390.jpg)

# SurrealMX: SurrealDB's new in-memory storage backend

There have been quite a few blog posts since the release of SurrealDB 3.0 to introduce each of the new features we have to show. Today's post is about one called SurrealMX that you likely have yet to hear about - but use every day.

That's because the way you use it is...by typing `surreal start`. That's it!

That's because SurrealMX is in fact the name of SurrealDB's new in-memory datastore. And since SurrealDB stores data in memory by default, 100% of SurrealDB's users have already given it a try.

## What is SurrealMX?

SurrealMX is SurrealDB's in-memory storage engine that was built from the ground up a bit over a year ago. It was merged into the core database [during the 3.0 alpha period last November](https://github.com/surrealdb/surrealdb/pull/6581) with no fanfare at all in order to try it out for the first time as SurrealDB's in-memory storage engine. Since SurrealDB uses in-memory storage by default, that means that SurrealMX has been every 3.x user's default storage option since then.

But SurrealMX isn't just a more performant way to store data in memory, it comes with new optional functionality too.

If you pay close attention to the SurrealDB source code you might have noticed a PR merged [three weeks ago](https://github.com/surrealdb/surrealdb/pull/6882) in the runup to 3.0 general availability that included a new way to pass in configuration parameters when starting a database.

If you go to [this part of the documentation](/docs/surrealdb/cli/start#datastore-configuration) for the `surreal start` command, you can see a comparison of how this worked in 2.x versions compared to 3.0.

In 2.x versions, specifying whether SurrealKV is versioned or not was done before the path to the database which led to either writing `surrealkv` or `surrealkv+versioned`. Other backends didn't have similar configurations.

```syntax
surrealkv://my_db
rocksdb://my_db
surrealkv://mydb
surrealkv+versioned://mydb
memory
```

In 3.0, this has now been changed to pass as many configurations as needed *after* the path to the database, in the same way that you do the same with a URL. Here are two examples from the documentation showing how this is done.

```syntax
"surrealkv://path/to/db?versioned=true&sync=every&retention=30d"
"mem://tmp/data?versioned=true&aol=sync&snapshot=60s&sync=5s"
"mem://?versioned=true"
```

Did you notice that `versioned=true` is found not just in the `surrealkv` but also the `mem` backend? That's because SurrealMX includes versioned queries in the same way that SurrealKV does.

Let's take a closer look!

## Time travel using the VERSION clause

With the addition of SurrealMX, SurrealDB now has two storage backgrounds that have versioning: SurrealKV and memory. Versioning is the capability to not just query a table as it stands now, but as it stood before. This feature is exceptionally important in areas like legal compliance in which a database needs to keep past information intact even if it has been overwritten later on.

In SurrealDB, time travel queries are done using the [`VERSION`](/docs/surrealql/statements/select#the-version-clause) keyword. Let's give this a quick try with the in-memory backend. First we will start a server with `?versioned=true` added:

```syntax
surreal start --user root --pass secret "mem://?versioned=true"
```

And then connect via [Surrealist](/docs/surrealist) or this command in the CLI.

```syntax
surreal sql --user root --pass secret
```

Once that is done, we can create a `person` record or two and make some queries using `VERSION` followed by `time::now()` minus how ever long ago we would like to query.

```surrealql
CREATE person;
[{ id: person:g4z4v7yoju9pe21jck6v }]

SELECT * FROM person;
[{ id: person:g4z4v7yoju9pe21jck6v }]

// No 'person' records existed yesterday
SELECT * FROM person VERSION time::now() - 1d
[]

// Add a second record
CREATE person;
[[{ id: person:aczudhy0mvef5bxurcry }]]

// 'person' has two records, but about ten seconds ago
// it had just one
SELECT * FROM person VERSION time::now() - 10s
[{ id: person:g4z4v7yoju9pe21jck6v }]
```

Since the `VERSION` keyword has been available via SurrealKV since SurrealDB 2.0, it's very likely that you are already quite familiar with it. Let's now move on to in-memory persistent storage options which were entirely unavailable before SurrealDB 3.0.

## In-memory with optional persistent storage and versioning

In-memory storage with optional persistent storage is one of the features of Redis that has made it so popular. SurrealMX offers this as well, via a somewhat more composable model.

Persistence for the memory backend is used for the following:

- Append-Only Log (AOL) - Synchronous/asynchronous modes for durability
- Snapshots - Periodic full database state capture
- Data Recovery - Automatic recovery from snapshots + AOL on startup
- AOL Truncation - Automatic cleanup after snapshots

You may be curious at this point how this differs from using SurrealKV (or RocksDB) to store your data. The difference is that SurrealMX persistent storage does not compress the data. It is an append-only-log of database writes, never compacted, until a snapshot occurs. It is in effect an entire database export. You can think of it as a convenience on top of in-memory speed while SurrealKV is used for traditional durable storage for datasets of any size.

## Trying it out

Let's grab part of the documentation to see how it works. These are the available parameters to use when starting a database with in-memory storage.

- `retention` (a duration string, e.g. 30d, 24h, 30m)
- `aol` (never, sync, or async), for writing changes to an append-only log file
- `snapshot` (a duration string, e.g. 60s), for periodically writing a snapshot of the database to the file system
- `sync` (never, every, or a duration string like 5s), for specifying when to flush the append-only log file to the file system
- `never` - (default) leave flushing to the OS (least durable)
- `every` - sync on every commit (most durable)
- `interval` - periodic background flushing at the given interval

We can match this up against the example above which shows that `aol` is set to `sync`, `snapshot` is set to `60s`, and `sync` is set to `5s`.

```syntax
"mem://tmp/data?versioned=true&aol=sync&snapshot=60s&sync=5s"
```

That's quite a bit to think about, but fortunately the SurrealMX repo has a table that lays out exactly when you would want to use one configuration over another. Each of these is balanced against the performance hit, ranging from no persistence at all (the fastest) to Sync AOL + Every fsync which survives both process and system crash at the greatest cost to performance.

To make a choice, just ask yourself the following as you move down the chart: what do you want to happen to your data if the process or system crashes? Then choose the most performant option that offers you the guarantees you need.

| Configuration | Survives Process Crash | Survives System Crash | Performance |
|---|---|---|---|
| No persistence | ❌ | ❌ | Fastest |
| Snapshot-only | ⚠️ (last snapshot) | ⚠️ (last snapshot) | Fastest |
| Async AOL + No fsync | ⚠️ (mostly) | ⚠️ (mostly + OS buffers) | Very fast |
| Async AOL + Interval fsync | ⚠️ (mostly) | ⚠️ (mostly + since last fsync) | Very fast |
| Async AOL + Every fsync | ⚠️ (mostly) | ⚠️ (mostly) | Very fast |
| Sync AOL + No fsync | ✅ | ⚠️ (OS buffers) | Fast |
| Sync AOL + Interval fsync | ✅ | ⚠️ (since last fsync) | Fast |
| Sync AOL + Every fsync | ✅ | ✅ | Slow |

Looks like the quickest and easiest way to use persistent storage is through periodic snapshots. Since these must be set to a number at least greater than 30 seconds, we'll give it a try with 31.

```syntax
surreal start --user root --pass secret "mem://tmp/data?snapshot=31s"
```

We can then connect with Surrealist or the `surreal sql --user root --pass secret` command and do a `CREATE person` or two.

After that, use `cd tmp/data` to go into the folder and wait for the file to show up. After 30 seconds you should see a file called `snapshot.bin`. That's the snapshot!

```syntax
!v�4��y��
         /!cgdefault�?H/�y��mainmain/!ndI��� H�
��t����4P���I��� H�
��t��@~����D�&���I��� H�
...snip
*/***person*rh6xmo5z8cqffvp4hbf6��BQ7
                                     ��
/***user*john��T|��
nameJohn%
```

Once that file is present, you can stop and restart the database, use `SELECT * FROM person` and see that the `person` records are still there. Not bad at all!

We suspect that the most popular options will be the following four:

- Snapshot only: the fastest option
- Async AOL + no fsync: the fastest option that tracks every change the moment one happens
- Sync AOL + no fsync: the fastest option if you think you might have a process crash
- Sync AOL + every fsync: the most durable option, survives both process and systems crashes

But that remains to be seen.

If you've given persistent in-memory storage a try already or have used it since the publication of this blog post, please get in touch and let us know!
