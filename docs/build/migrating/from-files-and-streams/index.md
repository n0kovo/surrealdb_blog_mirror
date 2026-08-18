---
position: 1
title: Migrating
description: Migrating
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/migrating/from-files-and-streams/index.mdx"
---

# Migrating from files and streams to SurrealDB

This section details how to map data, queries and concepts you may know from other databases and datatypes into SurrealDB.

The sources in this section of the documentation can be automatically imported to SurrealDB using the [Surreal Sync](https://github.com/surrealdb/surreal-sync/) tool. In addition, [CSV data](csv.md) can be automatically imported into SurrealDB Studio using its own [built-in functionality](../../../explore/studio/index.md).

For other sources not yet supported, consider beginning by exporting the database as JSON which can be [imported on the command line](../../../reference/cli/surrealdb-cli/commands/import.md). Alternatively, you can use [one of the many available SDKs](/docs#sdks) to access your existing database and transfer its content directly to a SurrealDB instance.

* [CSV data](csv.md)
* [JSON lines](json-lines.md)
* [Kafka](kafka.md)
