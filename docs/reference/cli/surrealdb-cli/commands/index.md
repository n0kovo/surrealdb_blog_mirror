---
position: 1
title: Overview
description: How the SurrealDB CLI is organised into subcommands, with links to each command’s flags and examples.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/surrealdb-cli/commands/index.mdx"
---

The `surreal` executable exposes a single entry point with **subcommands** for running the server, executing SurrealQL, importing and exporting data, and maintenance tasks. Each page documents that subcommand’s arguments, related environment variables, and typical usage.

<Synopsis>
surreal [OPTIONS] <COMMAND>
</Synopsis>

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

**Sidebar order:** [`start`](start.md) and [`sql`](sql.md) first, then remaining subcommands alphabetically.

## Shared options

Every subcommand accepts `-h` / `--help`, which prints its arguments and options and exits, and the logging option group (`-l` / `--log`, `--log-format`, `--log-file-*`, and the socket and OpenTelemetry overrides). Each page lists `--log` alongside the command's own flags and shows the full group in its command help output.

Most flags have an equivalent environment variable, listed in the tables on each page and in full on the [environment variables](../environment-variables.md#command-environment-variables) page.

## What is not here

These subcommands act on a database that already exists or that you start yourself. Provisioning, pausing, scaling, and deleting SurrealDB Cloud instances is the control plane, handled by [`surrealctl instance`](../../surrealctl/overview.md) instead. `surrealctl` calls out to `surreal` for SQL, imports, and exports, so the pages here still describe what happens once a Cloud instance has been resolved.

For installation and a minimal end-to-end example, see the [SurrealDB CLI overview](../overview.md).
