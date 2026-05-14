---
position: 2
title: Via CLI
description: In this section, you will explore SurrealQL queries using the SurrealDB CLI. The SurrealDB CLI provides a powerful command-line interface for writing, executing, and visualising SurrealQL queries in real-time.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/surrealql/executing-queries/via-cli.mdx"
---

# SurrealQL via CLI

To get started, [install the SurrealDB CLI](../../../../reference/cli/surrealdb-cli/overview.md) on your local machine.

## Getting started

After installing the SurrealDB CLI, you can start writing SurrealQL queries by running the [`surreal start`](../../../../reference/cli/surrealdb-cli/commands/start.md) command in your terminal. You can also add the `--help` flag to view the available options and commands.

To start a SurrealDB server, run the surreal start command, using the options below. This example serves the database at the default location (http://localhost:8000), with a username and password.

```bash
surreal start --user root --pass secret
```

The server is actively running, and can be left alone until you want to stop hosting the SurrealDB server.

![Terminal start](../../../../assets/img/terminal-start.png)

## Running queries

To run a SurrealQL query, open up a new terminal window and run the [`surreal sql`](../../../../reference/cli/surrealdb-cli/commands/sql.md) command. You will now be connected to the server and able to follow up with a query. For example, to run a simple `SELECT` query, you can run the following command:

```bash title="Start a SurrealDB Shell with local endpoint"
surreal sql --endpoint http://localhost:8000 --ns main --db main
```

```bash title="Start a SurrealDB Shell with memory endpoint"
## Run query in memory
surreal sql --endpoint memory --ns main --db main
```
![Terminal SQL](../../../../assets/img/terminal-sql.png)

## Learn more

Learn more about the available commands and options in the [SurrealDB CLI documentation](../../../../reference/cli/surrealdb-cli/overview.md).
