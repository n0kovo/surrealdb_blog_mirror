---
position: 1
title: Migrating from other databases
description: Map data and concepts from other databases to SurrealDB using Surreal Sync, the CLI import or SDKs.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/migrating/from-other-databases/overview.mdx"
---

# Migrating from other databases to SurrealDB

This section details how to map data, queries and concepts you may know from other databases and datatypes into SurrealDB.

All of the sources in this section of the documentation can be automatically imported to SurrealDB using the [Surreal Sync](https://github.com/surrealdb/surreal-sync/) tool.

To migrate from other databases not yet supported, consider beginning by exporting the database as JSON which can be [imported on the command line](../../../reference/cli/surrealdb-cli/commands/import.md). Alternatively, you can use [one of the many available SDKs](https://surrealdb.com/docs/start) to access your existing database and transfer its content directly to a SurrealDB instance.

* [MongoDB](https://surrealdb.com/docs/build/migrating/mongodb)
* [Neo4j](https://surrealdb.com/docs/build/migrating/neo4j)
* [PostgreSQL](https://surrealdb.com/docs/build/migrating/postgresql)
