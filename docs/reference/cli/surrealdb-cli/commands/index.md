---
position: 1
title: Overview
description: How the SurrealDB CLI is organised into subcommands, with links to each command’s flags and examples.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/surrealdb-cli/commands/index.mdx"
---

# CLI commands

The `surreal` executable exposes a single entry point with **subcommands** for running the server, executing SurrealQL, importing and exporting data, and maintenance tasks. Each page documents that subcommand’s arguments, related environment variables, and typical usage.

**Sidebar order:** [`start`](start.md) and [`sql`](sql.md) first, then remaining subcommands alphabetically.

| Subcommand | Purpose |
| --- | --- |
| [`start`](start.md) | Run a SurrealDB server (in memory, on disk, or clustered). |
| [`sql`](sql.md) | Open an interactive SurrealQL shell or run queries from scripts. |
| [`export`](export.md) | Dump a database to SurrealQL. |
| [`fix`](fix.md) | Apply data or schema fixes offline. |
| [`help`](help.md) | Show help for the CLI or a subcommand. |
| [`import`](import.md) | Load SurrealQL from a file into a database. |
| [`isready`](isready.md) | Health check for readiness probes. |
| [`mcp`](mcp.md) *Since v3.1.0* | Start the Model Context Protocol server on stdio for IDE integrations. |
| [`ml`](ml.md) | Work with machine-learning features from the CLI. |
| [`module`](module.md) | Build and manage WASM modules (including Surrealism). |
| [`upgrade`](upgrade.md) | Upgrade between SurrealDB versions. |
| [`validate`](validate.md) | Validate SurrealQL or configuration. |
| [`version`](version.md) | Print CLI and server version information. |

For installation and a minimal end-to-end example, see the [SurrealDB CLI overview](../overview.md). For environment variables that mirror CLI flags, see [Environment variables](../environment-variables.md).
