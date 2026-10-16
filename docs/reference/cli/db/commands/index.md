---
position: 1
title: surreal db commands
description: Every surreal db subcommand with its purpose, and how each relates to the launcher commands, with links to each command’s flags and examples.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/db/commands/index.mdx"
---

`surreal db` has **subcommands** for running the server, executing SurrealQL, importing and exporting data, and maintenance tasks. Each page documents that subcommand’s arguments, related environment variables, and typical usage.

<Synopsis>
surreal db [OPTIONS] <COMMAND>
</Synopsis>

| Subcommand | Purpose |
| --- | --- |
| [`surreal db start`](start.md) | Run a SurrealDB server (in memory, on disk, or clustered). |
| [`surreal db sql`](sql.md) | Open an interactive SurrealQL shell or run queries from scripts. |
| [`surreal db export`](export.md) | Dump a database to SurrealQL. |
| [`surreal db fix`](fix.md) | Apply data or schema fixes offline. |
| [`surreal db help`](help.md) | Show help for `surreal db` or a subcommand. |
| [`surreal db import`](import.md) | Load SurrealQL from a file into a database. |
| [`surreal db is-ready`](isready.md) | Health check for readiness probes. |
| [`surreal db mcp`](mcp.md) *Since v3.1.0* | Start the Model Context Protocol server on stdio for IDE integrations. |
| [`surreal db ml`](ml.md) | Work with machine-learning features from the CLI. |
| [`surreal db module`](module.md) | Build and manage WASM modules (including Surrealism). |
| [`surreal upgrade db`](upgrade.md) | Upgrade the database component. Run by the launcher, not by `surreal db`. |
| [`surreal db validate`](validate.md) | Validate SurrealQL or configuration. |
| [`surreal db version`](version.md) | Print the database client version, or the version of a server. |

**Sidebar order:** [`start`](start.md) and [`sql`](sql.md) first, then remaining subcommands alphabetically.

## Shared options

Every `surreal db` subcommand accepts `-h` / `--help`, which prints its arguments and options and exits, and the logging option group (`-l` / `--log`, `--log-format`, `--log-file-*`, and the socket and OpenTelemetry overrides). Each page lists `--log` alongside the command's own flags and shows the full group in its command help output.

Most flags have an equivalent environment variable, listed in the tables on each page and in full on the [environment variables](../environment-variables.md#command-environment-variables) page.

## What is not here

These subcommands act on a database that already exists or that you start yourself. Provisioning, pausing, scaling, and deleting SurrealDB Cloud instances is handled by [`surreal cloud instance`](../../cloud/index.md), which calls out to `surreal db` for SQL, imports, and exports, so the pages here still describe what happens once a Cloud instance has been resolved.

Installing, upgrading and selecting versions of the database is done by the launcher, with `surreal install db`, `surreal upgrade db`, `surreal use db@<VERSION>` and `surreal version`, described in the [launcher reference](../../launcher.md). The `surreal db upgrade` form is refused, with a message that names `surreal upgrade db`.

For installation and a minimal end-to-end example, see the [surreal db overview](../index.md).
