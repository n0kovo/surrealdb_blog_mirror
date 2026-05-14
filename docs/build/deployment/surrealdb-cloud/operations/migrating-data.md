---
position: 4
title: Migrating data
description: SurrealDB Cloud is a hosted version of SurrealDB, providing a fully managed, scalable, and secure database solution. This guide will help you migrate your existing SurrealDB instance to SurrealDB Cloud.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/deployment/surrealdb-cloud/operations/migrating-data.mdx"
---

# Migrating data from SurrealDB to SurrealDB Cloud

## Exporting and importing data

1. Export your current data as a `.surql` (SurrealQL) file. You can do this using the [`surreal export`](../../../../reference/cli/surrealdb-cli/commands/export.md) command in the terminal:

```bash
# Example export command to export data to a file called `export.surql` in the downloads directory.
surreal export --conn <connection-url> --user root --pass secret --ns main --db main downloads/export.surql
``` 

2. This will create a file called `export.surql` in the current directory.

3. You can now import this file into your SurrealDB Cloud Instance.

```bash
surreal import --conn <connection-url> --user root --pass secret --ns main --db main downloads/export.surql
```
