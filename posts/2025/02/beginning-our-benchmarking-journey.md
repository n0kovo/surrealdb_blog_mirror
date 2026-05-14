---
title: "Beginning our benchmarking journey"
slug: "beginning-our-benchmarking-journey"
date: "2025-02-11T00:00:00.000Z"
categories:
  - "company"
  - "featured"
read_time: "12 min read"
summary: "From humble beginnings come great things."
source: "https://surrealdb.com/blog/beginning-our-benchmarking-journey"
cover: "../../assets/5d62da251236f798.jpg"
---

# Beginning our benchmarking journey

![Beginning our benchmarking journey](../../assets/5d62da251236f798.jpg)

> [!WARNING: These benchmarks are outdated] These benchmarks reflect an old version of SurrealDB. For the latest benchmarks, visit the up-to-date [benchmarks page](/benchmarks).

What is SurrealDB?

That might be a strange question to start off a blog post about benchmarking, but it’s a very important one.

Why is it important?

Because that, to a large extent, determines what kind of benchmarks make sense to run against SurrealDB.

Let's therefore address that question first: What exactly is SurrealDB?

## The challenge of multi-model benchmarking

SurrealDB is a multi-model database that natively handles all types of data: relational, document, graph, time-series, key-value, vector and full-text search and more, all in one place.

SurrealDB also handles all types of deployment environments, from embedded devices to distributed clusters. This is made possible by one of the fundamental architecture designs of SurrealDB, separating the storage layer from the computation layer.

SurrealDB also has a built-in security layer, along with API layers for REST, RPC, and GraphQL. This blurs the lines between a traditional database and a backend as a service (BaaS).

Users like you giving SurrealDB a try for the first time come from all kinds of previous databases:

- SQL and NoSQL
- Embedded and distributed
- Traditional database and backend as a service

Naturally, you want to know how it compares to your previous database. Possibly even multiple previous databases if you’re replacing multiple databases with SurrealDB.

This is also something we are very interested in. But considering the versatility of SurrealDB, it can get complicated very fast.

For example, how immediately and reliably data is flushed to disk is not the same across databases. There are many configuration options which can result in dramatically different performance metrics. In-memory databases, as the name suggests, don't even write to disk.

It's important to keep this in mind, as we're comparing SurrealDB with various configurations against various kinds of databases. We've done our best to configure each database in the most fair way possible and added code comments, [such as in the code for MongoDB](https://github.com/surrealdb/crud-bench/blob/main/src/mongodb.rs#L65), to help explain some of our reasoning. If you think any of our configurations can be improved, we'd love to hear about it, as we want to be as fair as possible.

## The need for robust internal tooling

Over this last year, we have been looking into all the various benchmarking possibilities out there and have run various tools and tests to help us improve our performance and make sure there are no performance regressions between versions.

We have a vision for what SurrealDB is and can be, but as a young project, we are also heavily influenced by what you want SurrealDB to be and, therefore, the contributions you make really matter. That is why we are now opening up all our benchmarking tooling and asking for your feedback in helping us test and optimise for the things that matter to you!

## Our internal benchmarking tool

What we have found the most useful and therefore put the most effort into is developing our own benchmarking tool that is built in Rust and can be easily extended to cover everything that SurrealDB does and compare against any database or platform you use.

[The crud-bench benchmarking tool](https://github.com/surrealdb/crud-bench?tab=readme-ov-file) is an open-source benchmarking tool for testing and comparing the performance of a number of different workloads on embedded, networked, and remote databases. It can be used to compare both SQL and NoSQL platforms, including key-value and embedded databases. Importantly, crud-bench focuses on testing additional features which are not present in other benchmarking tools, but which are available in SurrealDB.

The primary purpose of crud-bench is to continually test and monitor the performance of features and functionality built into SurrealDB, enabling developers working on features in SurrealDB to assess the impact of their changes on database queries and performance.

[The crud-bench benchmarking tool](https://github.com/surrealdb/crud-bench?tab=readme-ov-file) is being actively developed with new features and functionality being added regularly. If you have ideas for how to improve our code or want to add a new database to compare against, we’re more than happy for your feedback and contributions!

### How does it work?

When running simple, automated tests, the crud-bench benchmarking tool will automatically start a Docker container for the datastore or database which is being benchmarked (when the datastore or database is networked). This configuration can be modified so that an optimised, remote environment can be connected to, instead of running a Docker container locally. This allows for running crud-bench against remote datastores, and distributed datastores on a local network or remotely in the cloud.

In one table, the benchmark will operate 5 main tasks:

- **Create:** inserting N unique records, with the specified concurrency.
- **Read:** read N unique records, with the specified concurrency.
- **Update:** update N unique records, with the specified concurrency.
- **Scans:** perform a number of range and table scans, with the specified concurrency.
- **Delete:** delete N unique records, with the specified concurrency.

With crud-bench almost all aspects of the benchmark engine are configurable:

- The number of rows or records (samples).
- The number of concurrent clients or connections.
- The number of concurrent threads (concurrent messages per client).
- Whether rows or records are modified sequentially or randomly.
- The primary id or key type for the records.
- Total control on the record structure: Columnar, object (JSON-like).
- Fine grained control over record types: string, booleans, numbers, array.
- The scan specifications for range or table queries.

### Which workloads can it run?

As crud-bench is in active development, some benchmarking workloads are already implemented, while others will be implemented in future releases. The list below details which benchmarks are implemented for the supporting datastores and lists those which are planned in the future.

**CRUD**

- [x] Creating single records in individual transactions
- [x] Reading single records in individual transactions
- [x] Updating single records in individual transactions
- [x] Deleting single records in individual transactions
- [ ] Batch creating multiple records in a transaction
- [ ] Batch reading multiple records in a transactions
- [ ] Batch updating multiple records in a transactions
- [ ] Batch deleting multiple records in a transactions

**Scans**

- [x] Full table scans, projecting all fields
- [x] Full table scans, projecting id field
- [x] Full table count queries
- [x] Scans with a limit, projecting all fields
- [x] Scans with a limit, projecting id field
- [x] Scans with a limit, counting results
- [x] Scans with a limit and offset, projecting all fields
- [x] Scans with a limit and offset, projecting id field
- [x] Scans with a limit and offset, counting results

One thing to note about the scans with a limit and offset, `[S]can::limit_start_all (100)`, is that our implementation is not fully optimised yet and will therefore not be as fast as other databases.

**Filters**

- [ ] Full table query, using filter condition, projecting all fields
- [ ] Full table query, using filter condition, projecting id field
- [ ] Full table query, using filter condition, counting rows

**Indexes**

- [ ] Indexed table query, using filter condition, projecting all fields
- [ ] Indexed table query, using filter condition, projecting id field
- [ ] Indexed table query, using filter condition, counting rows

**Relationships**

- [ ] Fetching or traversing 1-level, one-to-one relationships or joins
- [ ] Fetching or traversing 1-level, one-to-many relationships or joins
- [ ] Fetching or traversing 1-level, many-to-many relationships or joins
- [ ] Fetching or traversing n-level, one-to-one relationships or joins
- [ ] Fetching or traversing n-level, one-to-many relationships or joins
- [ ] Fetching or traversing n-level, many-to-many relationships or joins

**Workloads**

- [ ] Workload support for creating, updating, and reading records concurrently

As you can see from the above list, there is still a lot to do and we are committed to provide a very comprehensive benchmarking environment. If you think there is something we are missing or something we can improve, let us know!

Crud-bench is open for contributions such that you can [raise issues](https://github.com/surrealdb/crud-bench/issues) and [submit PRs](https://github.com/surrealdb/crud-bench/pulls) for things that matter most to you.

### Details of this benchmarking run

Crud-bench is running with the following hardware specifications:

- **Environment:** [single node Hetzner instance](https://www.hetzner.com/cloud)
- **Instance size:** CCX63
- **Dedicated vCPU:** 48
- **Memory (GiB):** 192
- **Instance storage:** 960 GB NVMe SSD

Crud-bench is running with the following configurations:

- **Number of records:** 5 000 000
- **Number of clients:** 128
- **Number of threads:** 64
- **Primary key type:** string26
- **Cooldown between runs**: 15 min (cooldown prevents CPU throttling)
- **Record contents sample:**

```json
{
    "integer": -649603394,
    "nested": {
      "array": [
        "oICD6WTWrrPgHxDsSPSBoOSDF5fOw63orRmaieWlC59Mnbtx9S",
        "3679FpWwclzTXEICDe8Qyqxf7XWwiDNhP9SFIDNszaLsQxg316",
        "UrZt46kMNd60oCftGYtd0ZcEAMAReuBiwCdlcvIDqZgEkww9bg",
        "CbwLLVw8OX0ymvgcBJ8AldhXMAlk3DmvIJvFQzAZLSOsubfhL4",
        "pTiBvzTomwOyCkY3xv9CAfRU7klrmDAvbfQcASe66UNEGf89Wz"
      ],
      "text": "cFw L3div76qg OIP3I mKMU3l vX395uDd 16jMHx 7zPM39 yG Cj L7Y8C8D nZZzc pUE8 qMz4 VPmkUH N7Yh2Xwg S00I 2hJLQC F5S2o IDadxYiaU wJ6s0I Dq KkOjxDC2 Zuj NZx28LU EG WJXG9v hKBWyX7 GiKpIL HtSwDANp3 y16Thb 08kYxhPWB u7bU TWaFZ t7nfoe4CU wKrq6HhB nFmR WIR9H Sb3BpPk rO Zk bWWLNHa IALWXX ajOCI NwO zl cN vMYZZ 4hkiWn Lh6A XR1 UkHZyiuw tiF o3JF1TNi v4f ICWpD 8JCWJ LP0h ywfLy do NPNt3q x6sfOn b9DDWfR Y4WqYJE S0T TC Iy uyr9W8i muj1 1N50bSQyL fnU 5QJaNSNOD 7Biav64 ez U5Wid1vk KsN CAyqJwG It as RJP KO 6q gJnE 6aljDtes DurAHei qIOFjC DS AbXvrmUX1 qz4 8Dq14i MqxAnt CHo u6kSff53t ng fSLgs PG 8UHhQA0A ei aX1ou 0V17xl 8Yc0T eUURFG0 oydm JYI VcJdFAd dI fm w7o mhDYTaY4A Y0xmtucTZ 7ZnM1M Z8h06h AGx6aI4 3Xi aFrb g65D0 ixSYe ZHA0 Ag KwTasnW C7A1pSzvg G3Hn3Gtw eGvxZfzQQ 4RMXFJgWM Ozj7oF llFwyn9R lvrYOJfv Y8 FrhfWUMIL pU5KdGZd taueohT LxFaieQ 4Bpebv J0t5bHtsz l3VVN aPH5 EGZ CsDT8 5J SKF 9k7FMR7X JzNtI qfF2vu T2MZx iLtv llmEl CxKnhhF6 N6bULGU fQxIOo5n M6Umh rjK 0y KIWLf 9CVj 9G36Vwji 7vSMt7GmH 1uk b23htGq stB CvWNZuFxG"
    },
    "text": "04Pn 8jBDDE ATemPG79l jkh1 u8zHq KP E6tZytaI dOT4 NDNT"
}
```

Below you'll find summary tables of the crud-bench results, grouped into the different data models.

For more detailed results, you can check out the [crud-bench GitHub repository](https://github.com/surrealdb/crud-bench?tab=readme-ov-file)

[We run all the various benchmarks daily on GitHub actions](https://github.com/surrealdb/crud-bench/actions/workflows/benchmark.yml), so you can also keep track of our performance journey there.

> [!WARNING: These benchmarks are outdated] These benchmarks reflect an old version of SurrealDB. For the latest benchmarks, visit the up-to-date [benchmarks page](/benchmarks).

## Relational (SQL) database comparison

While SurrealDB is a multi-model database, at its core, SurrealDB stores data in documents on transactional key-value stores. SurrealDB also uses record links and graph connections to establish relationships instead of joins.

This means that the most established relational benchmarks, such as TPC-C for transactional databases, cannot currently be run without modifications that the TPC-C benchmark would explicitly prohibit. This also applies to TPC-DS for analytical databases. Therefore, while we’ve looked into this quite a bit to determine the feasibility, we’ve decided not to implement these benchmarks yet. If you are interested in seeing this benchmark for SurrealDB, let us know. We would also be happy for contributions if you are familiar with implementing this benchmark.

For now, you can see the below crud-bench summary results comparing SurrealDB with the RocksDB and SurrealKV configurations vs PostgreSQL and MySQL.

### Total time

Wall time - Lower is better - Time from start to finish as measured by a clock

| Benchmark | SurrealDB (RocksDB) | PostgreSQL | MySQL | SurrealDB (SurrealKV) |
|---|---|---|---|---|
| [C]reate | 32s 237ms | 24s 399ms | 1m 57s | 4m 8s |
| [R]ead | 9s 827ms | 17s 624ms | 20s 821ms | 1m 10s |
| [U]pdate | 34s 181ms | 30s 458ms | 2m 28s | 4m 37s |
| [S]can::count_all (100) | 4s 19ms | 6s 236ms | 4s 268ms | 6s 985ms |
| [S]can::limit_id (100) | 81ms 632µs | 39ms 770µs | 29ms 81µs | 58ms 287µs |
| [S]can::limit_all (100) | 64ms 714µs | 32ms 778µs | 20ms 586µs | 67ms 195µs |
| [S]can::limit_count (100) | 63ms 966µs | 32ms 240µs | 21ms 360µs | 62ms 69µs |
| [S]can::limit_start_id (100) | 804ms 91µs | 42ms 602µs | 53ms 621µs | 929ms 129µs |
| [S]can::limit_start_all (100) | 779ms 538µs | 25ms 749µs | 103ms 82µs | 738ms 549µs |
| [S]can::limit_start_count (100) | 701ms 106µs | 28ms 848µs | 56ms 275µs | 700ms 844µs |
| [D]elete | 57s 793ms | 25s 158ms | 2m 15s | 4m 30s |

### Throughput

Operations per second (OPS) - Higher is better

| Benchmark | SurrealDB (RocksDB) | PostgreSQL | MySQL | SurrealDB (SurrealKV) |
|---|---|---|---|---|
| [C]reate | 155,096.92 | 204,923.10 | 42,409.99 | 20,123.13 |
| [R]ead | 508,757.45 | 283,699.12 | 240,133.35 | 71,195.44 |
| [U]pdate | 146,277.98 | 164,156.17 | 33,688.41 | 18,043.96 |
| [S]can::count_all (100) | 24.88 | 16.03 | 23.43 | 14.32 |
| [S]can::limit_id (100) | 1,225.00 | 2,514.40 | 3,438.61 | 1,715.65 |
| [S]can::limit_all (100) | 1,545.25 | 3,050.82 | 4,857.47 | 1,488.18 |
| [S]can::limit_count (100) | 1,563.31 | 3,101.73 | 4,681.62 | 1,611.11 |
| [S]can::limit_start_id (100) | 124.36 | 2,347.28 | 1,864.92 | 107.63 |
| [S]can::limit_start_all (100) | 128.28 | 3,883.56 | 970.09 | 135.40 |
| [S]can::limit_start_count (100) | 142.63 | 3,466.34 | 1,776.97 | 142.68 |
| [D]elete | 86,514.94 | 198,739.46 | 36,780.72 | 18,478.25 |

### Latency

99th percentile - Lower is better - Top 1% slowest operations, 99% of operations are faster than this

| Benchmark | SurrealDB (RocksDB) | PostgreSQL | MySQL | SurrealDB (SurrealKV) |
|---|---|---|---|---|
| [C]reate | 79.04 ms | 57.57 ms | 484.61 ms | 360.19 ms |
| [R]ead | 15.36 ms | 130.94 ms | 31.10 ms | 129.53 ms |
| [U]pdate | 82.30 ms | 62.59 ms | 598.01 ms | 388.61 ms |
| [S]can::count_all (100) | 4009.98 ms | 6221.82 ms | 4169.73 ms | 6975.49 ms |
| [S]can::limit_id (100) | 76.29 ms | 5.03 ms | 19.12 ms | 53.79 ms |
| [S]can::limit_all (100) | 60.67 ms | 7.92 ms | 16.80 ms | 62.72 ms |
| [S]can::limit_count (100) | 61.38 ms | 7.44 ms | 13.91 ms | 58.27 ms |
| [S]can::limit_start_id (100) | 799.23 ms | 39.74 ms | 50.17 ms | 926.21 ms |
| [S]can::limit_start_all (100) | 774.65 ms | 22.93 ms | 98.11 ms | 733.18 ms |
| [S]can::limit_start_count (100) | 696.32 ms | 25.66 ms | 51.87 ms | 695.81 ms |
| [D]elete | 226.43 ms | 47.62 ms | 552.45 ms | 376.83 ms |

[Click here to see the full results](https://github.com/surrealdb/crud-bench/actions/runs/13263890764)

______________________________________________________________________

## Relational embedded database comparison

See the below crud-bench summary results comparing SurrealDB with the RocksDB, SurrealKV and in-memory configurations vs SQLite.

### Total time

Wall time - Lower is better - Time from start to finish as measured by a clock

| Benchmark | SurrealDB embedded (RocksDB) | SurrealDB embedded (SurrealKV) | SurrealDB embedded (in-memory) | SQLite |
|---|---|---|---|---|
| [C]reate | 19s 753ms | 1m 57s | 2m 29s | 1m 23s |
| [R]ead | 9s 985ms | 1m 5s | 9s 381ms | 38s 300ms |
| [U]pdate | 27s 938ms | 2m 11s | 2m 51s | 44s 964ms |
| [S]can::count_all (100) | 5s 385ms | 7s 72ms | 11s 744ms | 6s 9ms |
| [S]can::limit_id (100) | 34ms 537µs | 72ms 30µs | 47ms 990µs | 42ms 374µs |
| [S]can::limit_all (100) | 21ms 992µs | 22ms 617µs | 35ms 50µs | 29ms 69µs |
| [S]can::limit_count (100) | 21ms 767µs | 22ms 921µs | 27ms 384µs | 24ms 718µs |
| [S]can::limit_start_id (100) | 774ms 886µs | 787ms 202µs | 788ms 488µs | 23ms 416µs |
| [S]can::limit_start_all (100) | 610ms 580µs | 618ms 336µs | 610ms 489µs | 27ms 203µs |
| [S]can::limit_start_count (100) | 253ms 788µs | 258ms 285µs | 263ms 95µs | 23ms 758µs |
| [D]elete | 1m 8s | 2m 24s | 2m 27s | 1m 9s |

### Throughput

Operations per second (OPS) - Higher is better

| Benchmark | SurrealDB embedded (RocksDB) | SurrealDB embedded (SurrealKV) | SurrealDB embedded (in-memory) | SQLite |
|---|---|---|---|---|
| [C]reate | 253,119.34 | 42,471.82 | 33,503.79 | 59,666.43 |
| [R]ead | 500,710.20 | 76,006.62 | 532,942.01 | 130,545.35 |
| [U]pdate | 178,967.41 | 37,946.57 | 29,140.42 | 111,198.12 |
| [S]can::count_all (100) | 18.57 | 14.14 | 8.51 | 16.64 |
| [S]can::limit_id (100) | 2,895.43 | 1,388.30 | 2,083.73 | 2,359.92 |
| [S]can::limit_all (100) | 4,547.03 | 4,421.45 | 2,853.02 | 3,440.05 |
| [S]can::limit_count (100) | 4,593.97 | 4,362.64 | 3,651.72 | 4,045.58 |
| [S]can::limit_start_id (100) | 129.05 | 127.03 | 126.82 | 4,270.52 |
| [S]can::limit_start_all (100) | 163.78 | 161.72 | 163.80 | 3,676.01 |
| [S]can::limit_start_count (100) | 394.03 | 387.17 | 380.09 | 4,208.96 |
| [D]elete | 73,129.86 | 34,535.40 | 33,998.67 | 72,338.41 |

### Latency

99th percentile - Lower is better - Top 1% slowest operations, 99% of operations are faster than this

| Benchmark | SurrealDB embedded (RocksDB) | SurrealDB embedded (SurrealKV) | SurrealDB embedded (in-memory) | SQLite |
|---|---|---|---|---|
| [C]reate | 50.69 ms | 185.98 ms | 252.54 ms | 111.87 ms |
| [R]ead | 22.72 ms | 262.91 ms | 22.94 ms | 49.63 ms |
| [U]pdate | 77.50 ms | 204.80 ms | 271.62 ms | 57.31 ms |
| [S]can::count_all (100) | 5357.57 ms | 6975.49 ms | 8384.51 ms | 5947.39 ms |
| [S]can::limit_id (100) | 28.99 ms | 62.81 ms | 44.67 ms | 11.65 ms |
| [S]can::limit_all (100) | 19.87 ms | 15.03 ms | 20.35 ms | 14.84 ms |
| [S]can::limit_count (100) | 19.41 ms | 19.04 ms | 20.45 ms | 1.30 ms |
| [S]can::limit_start_id (100) | 770.05 ms | 783.36 ms | 784.89 ms | 18.56 ms |
| [S]can::limit_start_all (100) | 605.70 ms | 611.33 ms | 603.65 ms | 24.89 ms |
| [S]can::limit_start_count (100) | 249.22 ms | 250.50 ms | 257.41 ms | 11.50 ms |
| [D]elete | 183.17 ms | 237.95 ms | 233.22 ms | 91.14 ms |

[Click here to see the full results](https://github.com/surrealdb/crud-bench/actions/runs/13263890764)

______________________________________________________________________

## Document database comparison

The closest thing the NoSQL community has to a standard benchmark is the [Yahoo! Cloud Serving Benchmark (YCSB)](https://github.com/surrealdb/benchmarking?tab=readme-ov-file#go-ycsb), which has 6 workloads simulating various database use cases.

In our benchmarking repository, you’ll find an implementation of this benchmark in the Go programming language. This implementation was ported to Go from Java by PingCAP.

You’ll also find a fork of [NoSQLBench](https://github.com/surrealdb/benchmarking?tab=readme-ov-file#nosqlbench) which is developed by DataStax. The SurrealDB changes to this benchmarking tool have not yet been released, but its something we are actively looking into.

We are working on running the YCSB benchmark in a multi-node configuration, which will come after this single node crud-bench benchmark.

For now, you can see the below crud-bench summary results comparing SurrealDB with the RocksDB and SurrealKV configurations vs MongoDB and ArangoDB.

### Total time

Wall time - Lower is better - Time from start to finish as measured by a clock

| Benchmark | SurrealDB (RocksDB) | MongoDB | ArangoDB | SurrealDB (SurrealKV) |
|---|---|---|---|---|
| [C]reate | 32s 237ms | 54s 211ms | 3m 2s | 4m 8s |
| [R]ead | 9s 827ms | 55s 0ms | 27s 615ms | 1m 10s |
| [U]pdate | 34s 181ms | 57s 53ms | 3m 18s | 4m 37s |
| [S]can::count_all (100) | 4s 19ms | 8s 285ms | 22s 85ms | 6s 985ms |
| [S]can::limit_id (100) | 81ms 632µs | 43ms 280µs | 57ms 753µs | 58ms 287µs |
| [S]can::limit_all (100) | 64ms 714µs | 31ms 805µs | 10s 167ms | 67ms 195µs |
| [S]can::limit_count (100) | 63ms 966µs | 29ms 773µs | 43ms 949µs | 62ms 69µs |
| [S]can::limit_start_id (100) | 804ms 91µs | 29ms 73µs | 86ms 470µs | 929ms 129µs |
| [S]can::limit_start_all (100) | 779ms 538µs | 23ms 178µs | 10s 311ms | 738ms 549µs |
| [S]can::limit_start_count (100) | 701ms 106µs | 28ms 340µs | 65ms 24µs | 700ms 844µs |
| [D]elete | 57s 793ms | 53s 553ms | 3m 5s | 4m 30s |

### Throughput

Operations per second (OPS) - Higher is better

| Benchmark | SurrealDB (RocksDB) | MongoDB | ArangoDB | SurrealDB (SurrealKV) |
|---|---|---|---|---|
| [C]reate | 155,096.92 | 92,230.93 | 27,395.80 | 20,123.13 |
| [R]ead | 508,757.45 | 90,907.45 | 181,056.51 | 71,195.44 |
| [U]pdate | 146,277.98 | 87,636.30 | 25,171.61 | 18,043.96 |
| [S]can::count_all (100) | 24.88 | 12.07 | 4.53 | 14.32 |
| [S]can::limit_id (100) | 1,225.00 | 2,310.52 | 1,731.51 | 1,715.65 |
| [S]can::limit_all (100) | 1,545.25 | 3,144.14 | 9.84 | 1,488.18 |
| [S]can::limit_count (100) | 1,563.31 | 3,358.69 | 2,275.33 | 1,611.11 |
| [S]can::limit_start_id (100) | 124.36 | 3,439.61 | 1,156.46 | 107.63 |
| [S]can::limit_start_all (100) | 128.28 | 4,314.37 | 9.70 | 135.40 |
| [S]can::limit_start_count (100) | 142.63 | 3,528.48 | 1,537.88 | 142.68 |
| [D]elete | 86,514.94 | 93,365.28 | 26,939.30 | 18,478.25 |

### Latency

99th percentile - Lower is better - Top 1% slowest operations, 99% of operations are faster than this

| Benchmark | SurrealDB (RocksDB) | MongoDB | ArangoDB | SurrealDB (SurrealKV) |
|---|---|---|---|---|
| [C]reate | 79.04 ms | 105.22 ms | 285.18 ms | 360.19 ms |
| [R]ead | 15.36 ms | 70.78 ms | 38.75 ms | 129.53 ms |
| [U]pdate | 82.30 ms | 88.64 ms | 323.58 ms | 388.61 ms |
| [S]can::count_all (100) | 4009.98 ms | 8232.96 ms | 21708.80 ms | 6975.49 ms |
| [S]can::limit_id (100) | 76.29 ms | 14.74 ms | 53.53 ms | 53.79 ms |
| [S]can::limit_all (100) | 60.67 ms | 7.00 ms | 9953.28 ms | 62.72 ms |
| [S]can::limit_count (100) | 61.38 ms | 3.67 ms | 30.27 ms | 58.27 ms |
| [S]can::limit_start_id (100) | 799.23 ms | 17.57 ms | 82.11 ms | 926.21 ms |
| [S]can::limit_start_all (100) | 774.65 ms | 16.89 ms | 10100.74 ms | 733.18 ms |
| [S]can::limit_start_count (100) | 696.32 ms | 12.67 ms | 60.80 ms | 695.81 ms |
| [D]elete | 226.43 ms | 68.67 ms | 284.16 ms | 376.83 ms |

[Click here to see the full results](https://github.com/surrealdb/crud-bench/actions/runs/13263890764)

______________________________________________________________________

## Graph database comparison

As we continue to make improvements to our graph features, we are looking into implementing the benchmarks from the [Linked Data Benchmark Council (LDBC)](https://ldbcouncil.org/benchmarks/overview/). If this is something you are interested in, please reach out to us!

For now, you can see the below crud-bench summary results comparing SurrealDB with the RocksDB and SurrealKV configurations vs Neo4j.

One thing to note is that this is not comparing graph relationships, only crud operations, as we have not yet implemented relationships in crud-bench.

### Total time

Wall time - Lower is better - Time from start to finish as measured by a clock

| Benchmark | SurrealDB (RocksDB) | Neo4j | SurrealDB (SurrealKV) |
|---|---|---|---|
| [C]reate | 32s 237ms | 6m 36s | 4m 8s |
| [R]ead | 9s 827ms | 1m 3s | 1m 10s |
| [U]pdate | 34s 181ms | 8m 37s | 4m 37s |
| [S]can::count_all (100) | 4s 19ms | 20s 226ms | 6s 985ms |
| [S]can::limit_id (100) | 81ms 632µs | 237ms 2µs | 58ms 287µs |
| [S]can::limit_all (100) | 64ms 714µs | 42ms 530µs | 67ms 195µs |
| [S]can::limit_count (100) | 63ms 966µs | 43ms 153µs | 62ms 69µs |
| [S]can::limit_start_id (100) | 804ms 91µs | 84ms 143µs | 929ms 129µs |
| [S]can::limit_start_all (100) | 779ms 538µs | 30ms 818µs | 738ms 549µs |
| [S]can::limit_start_count (100) | 701ms 106µs | 44ms 6µs | 700ms 844µs |
| [D]elete | 57s 793ms | 2m 20s | 4m 30s |

### Throughput

Operations per second (OPS) - Higher is better

| Benchmark | SurrealDB (RocksDB) | Neo4j | SurrealDB (SurrealKV) |
|---|---|---|---|
| [C]reate | 155,096.92 | 12,614.50 | 20,123.13 |
| [R]ead | 508,757.45 | 78,444.68 | 71,195.44 |
| [U]pdate | 146,277.98 | 9,657.01 | 18,043.96 |
| [S]can::count_all (100) | 24.88 | 4.94 | 14.32 |
| [S]can::limit_id (100) | 1,225.00 | 421.94 | 1,715.65 |
| [S]can::limit_all (100) | 1,545.25 | 2,351.27 | 1,488.18 |
| [S]can::limit_count (100) | 1,563.31 | 2,317.29 | 1,611.11 |
| [S]can::limit_start_id (100) | 124.36 | 1,188.44 | 107.63 |
| [S]can::limit_start_all (100) | 128.28 | 3,244.85 | 135.40 |
| [S]can::limit_start_count (100) | 142.63 | 2,272.42 | 142.68 |
| [D]elete | 86,514.94 | 35,556.12 | 18,478.25 |

### Latency

99th percentile - Lower is better - Top 1% slowest operations, 99% of operations are faster than this

| Benchmark | SurrealDB (RocksDB) | Neo4j | SurrealDB (SurrealKV) |
|---|---|---|---|
| [C]reate | 79.04 ms | 774.65 ms | 360.19 ms |
| [R]ead | 15.36 ms | 98.75 ms | 129.53 ms |
| [U]pdate | 82.30 ms | 694.27 ms | 388.61 ms |
| [S]can::count_all (100) | 4009.98 ms | 20201.47 ms | 6975.49 ms |
| [S]can::limit_id (100) | 76.29 ms | 234.50 ms | 53.79 ms |
| [S]can::limit_all (100) | 60.67 ms | 40.38 ms | 62.72 ms |
| [S]can::limit_count (100) | 61.38 ms | 28.77 ms | 58.27 ms |
| [S]can::limit_start_id (100) | 799.23 ms | 81.73 ms | 926.21 ms |
| [S]can::limit_start_all (100) | 774.65 ms | 21.45 ms | 733.18 ms |
| [S]can::limit_start_count (100) | 696.32 ms | 19.21 ms | 695.81 ms |
| [D]elete | 226.43 ms | 473.34 ms | 376.83 ms |

[Click here to see the full results](https://github.com/surrealdb/crud-bench/actions/runs/13263890764)

______________________________________________________________________

## In-memory database comparison

See the below crud-bench summary results comparing SurrealDB with the in-memory configuration vs Redis, Dragonfly and KeyDB.

If you would like to see more comparisons or have ideas of how we can improve these benchmarks, let us know.

### Total time

Wall time - Lower is better - Time from start to finish as measured by a clock

| Benchmark | SurrealDB in-memory | Redis | Dragonfly | KeyDB |
|---|---|---|---|---|
| [C]reate | 4m 36s | 57s 502ms | 14s 734ms | 54s 278ms |
| [R]ead | 8s 689ms | 54s 481ms | 14s 171ms | 52s 8ms |
| [U]pdate | 5m 2s | 53s 799ms | 14s 682ms | 52s 607ms |
| [S]can::count_all (100) | 1m 29s | 4m 39s | 26m 11s | 4m 58s |
| [S]can::limit_id (100) | 97ms 340µs | 139ms 608µs | 1s 295ms | 171ms 813µs |
| [S]can::limit_all (100) | 101ms 131µs | 599ms 524µs | 1s 975ms | 679ms 912µs |
| [S]can::limit_count (100) | 58ms 410µs | 145ms 503µs | 1s 387ms | 167ms 701µs |
| [S]can::limit_start_id (100) | 944ms 173µs | 284ms 803µs | 2s 583ms | 351ms 872µs |
| [S]can::limit_start_all (100) | 898ms 607µs | 918ms 956µs | 3s 302ms | 927ms 417µs |
| [S]can::limit_start_count (100) | 818ms 139µs | 314ms 147µs | 3s 48ms | 340ms 127µs |
| [D]elete | 4m 32s | 54s 114ms | 14s 171ms | 51s 101ms |

### Throughput

Operations per second (OPS) - Higher is better

| Benchmark | SurrealDB in-memory | Redis | Dragonfly | KeyDB |
|---|---|---|---|---|
| [C]reate | 18,092.85 | 86,952.42 | 339,345.39 | 92,117.50 |
| [R]ead | 575,416.45 | 91,774.61 | 352,816.53 | 96,137.26 |
| [U]pdate | 16,510.91 | 92,937.11 | 340,535.51 | 95,042.82 |
| [S]can::count_all (100) | 1.11 | 0.36 | 0.06 | 0.33 |
| [S]can::limit_id (100) | 1,027.32 | 716.29 | 77.20 | 582.03 |
| [S]can::limit_all (100) | 988.81 | 166.80 | 50.63 | 147.08 |
| [S]can::limit_count (100) | 1,712.01 | 687.27 | 72.06 | 596.30 |
| [S]can::limit_start_id (100) | 105.91 | 351.12 | 38.71 | 284.19 |
| [S]can::limit_start_all (100) | 111.28 | 108.82 | 30.28 | 107.83 |
| [S]can::limit_start_count (100) | 122.23 | 318.32 | 32.80 | 294.01 |
| [D]elete | 18,325.80 | 92,397.10 | 352,832.63 | 97,844.68 |

### Latency

99th percentile - Lower is better - Top 1% slowest operations, 99% of operations are faster than this

| Benchmark | SurrealDB in-memory | Redis | Dragonfly | KeyDB |
|---|---|---|---|---|
| [C]reate | 403.71 ms | 83.20 ms | 24.67 ms | 95.94 ms |
| [R]ead | 13.65 ms | 75.33 ms | 23.09 ms | 92.67 ms |
| [U]pdate | 431.10 ms | 73.73 ms | 24.50 ms | 92.67 ms |
| [S]can::count_all (100) | 89915.39 ms | 274726.91 ms | 1535115.26 ms | 293339.14 ms |
| [S]can::limit_id (100) | 93.50 ms | 134.66 ms | 1258.49 ms | 164.09 ms |
| [S]can::limit_all (100) | 97.66 ms | 587.77 ms | 1953.79 ms | 659.46 ms |
| [S]can::limit_count (100) | 54.78 ms | 137.73 ms | 1355.78 ms | 161.79 ms |
| [S]can::limit_start_id (100) | 939.01 ms | 280.57 ms | 2512.89 ms | 340.48 ms |
| [S]can::limit_start_all (100) | 893.44 ms | 891.39 ms | 3219.45 ms | 906.75 ms |
| [S]can::limit_start_count (100) | 812.54 ms | 304.13 ms | 3012.61 ms | 330.50 ms |
| [D]elete | 391.94 ms | 74.30 ms | 23.12 ms | 90.81 ms |

[Click here to see the full results](https://github.com/surrealdb/crud-bench/actions/runs/13263890764)

______________________________________________________________________

## Key-Value store comparison

See the below crud-bench summary results comparing SurrealKV key-value storage engine vs RocksDB, LMDB and Fjall.

A few things to note regarding SurrealKV:

- It's still in beta and under active development.
- It's primary purpose is not to replace RocksDB, but to enable new use cases such as versioning/versioned queries.
- RocksDB is still our primary key-value storage engine

If you would like to see more comparisons or have ideas of how we can improve these benchmarks, let us know.

### Total time

Wall time - Lower is better - Time from start to finish as measured by a clock

| Benchmark | RocksDB | SurrealKV | LMDB | Fjall |
|---|---|---|---|---|
| [C]reate | 49s 354ms | 1m 27s | 2m 21s | 1m 38s |
| [R]ead | 8s 458ms | 35s 749ms | 4s 170ms | 5s 106ms |
| [U]pdate | 48s 842ms | 1m 20s | 2m 14s | 1m 41s |
| [S]can::count_all (100) | 11s 571ms | 9s 739ms | 868ms 104µs | 14s 423ms |
| [S]can::limit_id (100) | 36ms 686µs | 29ms 516µs | 22ms 885µs | 83ms 776µs |
| [S]can::limit_all (100) | 30ms 455µs | 22ms 489µs | 22ms 309µs | 33ms 984µs |
| [S]can::limit_count (100) | 24ms 901µs | 23ms 685µs | 21ms 121µs | 18ms 819µs |
| [S]can::limit_start_id (100) | 21ms 526µs | 16ms 100µs | 22ms 362µs | 21ms 706µs |
| [S]can::limit_start_all (100) | 17ms 847µs | 75ms 414µs | 22ms 424µs | 20ms 943µs |
| [S]can::limit_start_count (100) | 24ms 22µs | 27ms 197µs | 24ms 15µs | 15ms 994µs |

### Throughput

Operations per second (OPS) - Higher is better

| Benchmark | RocksDB | SurrealKV | LMDB | Fjall |
|---|---|---|---|---|
| [C]reate | 101,307.73 | 56,953.28 | 35,284.94 | 50,890.18 |
| [R]ead | 591,113.32 | 139,862.88 | 1,198,773.26 | 979,056.07 |
| [U]pdate | 102,370.10 | 62,131.25 | 37,195.57 | 49,277.46 |
| [S]can::count_all (100) | 8.64 | 10.27 | 115.19 | 6.93 |
| [S]can::limit_id (100) | 2,725.80 | 3,387.93 | 4,369.66 | 1,193.65 |
| [S]can::limit_all (100) | 3,283.52 | 4,446.44 | 4,482.44 | 2,942.52 |
| [S]can::limit_count (100) | 4,015.79 | 4,221.92 | 4,734.49 | 5,313.53 |
| [S]can::limit_start_id (100) | 4,645.47 | 6,210.92 | 4,471.77 | 4,606.96 |
| [S]can::limit_start_all (100) | 5,602.94 | 1,326.01 | 4,459.32 | 4,774.72 |
| [S]can::limit_start_count (100) | 4,162.77 | 3,676.86 | 4,164.06 | 6,252.01 |
| [D]elete | 106,131.13 | 78,687.82 | 23,215.52 | 55,013.69 |

### Latency

99th percentile - Lower is better - Top 1% slowest operations, 99% of operations are faster than this

| Benchmark | RocksDB | SurrealKV | LMDB | Fjall |
|---|---|---|---|---|
| [C]reate | 0.75 ms | 138.24 ms | 32.58 ms | 11.08 ms |
| [R]ead | 0.79 ms | 2.14 ms | 0.39 ms | 0.29 ms |
| [U]pdate | 0.77 ms | 126.27 ms | 34.94 ms | 11.46 ms |
| [S]can::count_all (100) | 4476.93 ms | 3731.45 ms | 326.65 ms | 5844.99 ms |
| [S]can::limit_id (100) | 0.30 ms | 0.12 ms | 0.01 ms | 70.91 ms |
| [S]can::limit_all (100) | 0.35 ms | 0.70 ms | 0.01 ms | 0.27 ms |
| [S]can::limit_count (100) | 0.30 ms | 0.09 ms | 0.04 ms | 0.41 ms |
| [S]can::limit_start_id (100) | 6.41 ms | 10.22 ms | 0.55 ms | 10.11 ms |
| [S]can::limit_start_all (100) | 9.10 ms | 64.06 ms | 0.37 ms | 10.59 ms |
| [S]can::limit_start_count (100) | 7.96 ms | 3.58 ms | 0.43 ms | 8.08 ms |
| [D]elete | 0.69 ms | 107.14 ms | 50.59 ms | 10.90 ms |

[Click here to see the full results](https://github.com/surrealdb/crud-bench/actions/runs/13263890764)

## Vector search benchmarks

To help us improve our vector search performance, we started by forking the [ANN benchmarks](https://github.com/surrealdb/benchmarking?tab=readme-ov-file#ann-benchmarks) developed by Erik Bernhardsson, which are one of the most popular vector search benchmarks at the moment. We have since expanded on that with tests for all flavours of vector search (MTREE, Brute-Force, HNSW) in SurrealDB. There is still more work to be done, but feel free to look at what we have done so far.

## How you can use our benchmarking tooling

We have made our [benchmarking repository on GitHub](https://github.com/surrealdb/benchmarking) public and you can find all the code and detailed instructions on how to run and contribute to each benchmark there.

[https://github.com/surrealdb/benchmarking](https://github.com/surrealdb/benchmarking)

SurrealDB can do a lot and this is only the start of our performance optimisation journey!

There is still a lot to do and we are committed to provide a very comprehensive benchmarking environment, and as always, we really appreciate any feedback and contributions. SurrealDB wouldn’t be what it is today without you!

[You can reach out to us here](/contact)
