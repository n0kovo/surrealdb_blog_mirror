---
position: 1
title: Running SurrealDB
description: Ways to run SurrealDB, from a browser sandbox to managed cloud. Or install it on your own hardware.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/running/overview.mdx"
---

# Running SurrealDB

You can start with SurrealDB in more than one way. This section orders them from **the least to the most** involved, so you can pick how much you want to set up.

## Try it without installing

1. **[SurrealDB Studio Sandbox](sandbox.md)** (under a minute) - Open SurrealDB Studio in the browser and use the built-in Sandbox. There is nothing to install. Data is not persistent, which suits quick experiments and learning SurrealQL.

2. **[SurrealDB Cloud](cloud.md)** (about 5 minutes) - Create a free [SurrealDB Cloud](../manage/instances/index.md) instance (you will need an email to sign in). You keep persistence and a managed database without running a server on your own machine.

3. **[Installation](installation/index.md)** (about 10 minutes) - Install the `surreal` binary and run SurrealDB locally or on your own infrastructure. This is the path when you want full control, offline work, or production self-hosting.

## How you run the database on your own infrastructure

After you are running SurrealDB (locally or on servers you manage), you can choose storage and topology:

- [Run a single-node, in-memory server](in-memory.md) with optional persistence and versioning (SurrealMX)
- [Run a single-node, on-disk server](file-backed.md) (RocksDB or SurrealKV)
- [Run a multi-node cluster](multi-node.md)
- [Run with Docker](docker.md)
