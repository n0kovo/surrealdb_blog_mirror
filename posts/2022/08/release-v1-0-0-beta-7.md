---
title: "Release v1.0.0-beta.7"
slug: "release-v1-0-0-beta-7"
date: "2022-08-29T00:00:00.000Z"
categories:
  - "releases"
read_time: "1 min read"
summary: "Add support for Objects and Arrays as Record IDs, add support for querying records using Record ID ranges, add SQL <code>session<\\/code> functions for retrieving session variables, make <code>--ns<\\/code> and <code>--db<\\/code> arguments optional in command-line REPL, and much more."
source: "https://surrealdb.com/blog/release-v1-0-0-beta-7"
cover: "../../assets/3a47c28caf2a55ab.jpg"
---

# Release v1.0.0-beta.7

![Release v1.0.0-beta.7](../../assets/3a47c28caf2a55ab.jpg)

- Add support for Objects and Arrays as Record IDs
- Add support for querying records using Record ID ranges
- Add SQL session functions for retrieving session variables
- Make --ns and --db arguments optional in command-line REPL
- Return an error when the specified datastore is not able to be initiated
- Enable root authentication for client libraries using WebSocket protocol
- Ensure math::sum() returns a number instead of a NONE value, when called on a non-array value
- Add ACID compliant, persistant, on-disk storage implementation, with multiple concurrent writers using RocksDB

## Complex Record IDs

SurrealDB now supports the ability to define record IDs using arrays. These values sort correctly, and can be used to store values or recordings in a timeseries context.

```surrealql
// Create a record with a complex ID using an array
CREATE temperature:['London', '2022-08-29T08:03:39'] SET
    location = 'London',
    date = '2022-08-29T08:03:39',
    temperature = 23.7
;

// Select a specific record using a complex ID
SELECT * FROM temperature:['London', '2022-08-29T08:03:39'];
```

## Record ID ranges

SurrealDB now supports the ability to query a range of records, using the record ID. The record ID ranges, retrieve records using the natural sorting order of the record IDs. With the addition of complex record IDs above, this can be used to query a range of records in a timeseries context.

```surrealql
// Select all person records with IDs between the given range
SELECT * FROM person:1..1000;
// Select all temperature records with IDs between the given range
SELECT * FROM temperature:['London', '2022-08-29T08:03:39']..['London', '2022-08-29T08:09:31'];
```

/releases
