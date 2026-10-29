---
position: 0
title: CLI tools
description: Overview of every command in the surreal launcher, surreal db, surreal cloud and surreal ext, with links to each reference page, plus the separate surqlfmt formatter.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/index.mdx"
---

SurrealDB has one command line, `surreal`. The `surreal` launcher installs once, then installs, versions and runs **components**, each with its own commands: the database (`surreal db`), SurrealDB Cloud (`surreal cloud`) and Surrealism extensions (`surreal ext`). This section is the reference for all of them. For how they fit together, start with the [SurrealDB CLI guide](../../explore/cli/index.md).

```bash
surreal install cloud
surreal db start --user root --pass secret
surreal cloud instance list
```

| Reference | Covers |
| --- | --- |
| [Launcher commands](launcher.md) | Installing, upgrading, pinning and removing components, version names, `+VERSION`, and the launcher's environment variables |
| [`surreal db`](db/index.md) | The database: run a server, query it, and move data in and out |
| [`surreal cloud`](cloud/index.md) | SurrealDB Cloud: organisations, instances, backups, members and tokens |
| [`surreal ext`](ext.md) | Surrealism extensions |
| [`surqlfmt`](formatter/overview.md) | Formatting `.surql` files, distributed separately as an npm package |

## Launcher commands

These commands belong to the launcher, and nothing else installs or changes component versions. See [Launcher commands](launcher.md) for options and examples.

| Command | Purpose |
| --- | --- |
| `surreal install <COMPONENT[@VERSION]>...` | Install components, or another version of one beside those installed |
| `surreal upgrade [<COMPONENT[@VERSION]> \| cli]...` | Upgrade the launcher and every installed component, or those named |
| `surreal use <COMPONENT@VERSION>` | Make an installed version the default |
| `surreal uninstall <COMPONENT[@VERSION]>...` | Remove a version, or a component entirely |
| `surreal list` | Show each component, the version that runs, and where it runs from |
| `surreal --version` | Print the launcher's own version |
| `surreal +VERSION <COMPONENT> ...` | Run another version for one command |
| `surreal help` | Print the launcher's help |

## surreal db

The database component. Everything after `db` goes to the database, so the same flags and `SURREAL_*` variables apply. Each command has its own page under [database commands](db/commands/index.md).

| Command | Purpose |
| --- | --- |
| [`surreal db start`](db/commands/start.md) | Run a SurrealDB server |
| [`surreal db sql`](db/commands/sql.md) | Open an interactive SurrealQL shell |
| [`surreal db import`](db/commands/import.md) | Load a SurrealQL file into a database |
| [`surreal db export`](db/commands/export.md) | Dump a database to SurrealQL |
| [`surreal db is-ready`](db/commands/isready.md) | Check that a server accepts connections |
| [`surreal db validate`](db/commands/validate.md) | Validate SurrealQL files |
| [`surreal db fix`](db/commands/fix.md) | Repair storage issues |
| [`surreal db ml`](db/commands/ml.md) | Import and export machine-learning models |
| [`surreal db mcp`](db/commands/mcp.md) | Run the Model Context Protocol server over stdio |
| [`surreal ext`](ext.md) | Build, sign, install and run Surrealism extensions |
| [`surreal db version`](db/commands/version.md) | Print the database or server version |

The old top-level forms, such as `surreal start`, still run and print a deprecation warning. Upgrading the database is `surreal upgrade db`, a launcher command.

## surreal cloud

The SurrealDB Cloud component. Every command takes `--json`, and sends its data to stdout and everything else to stderr. See [global flags](cloud/global-flags.md) and [output and exit codes](cloud/output-and-exit-codes.md).

| Command | Purpose |
| --- | --- |
| [`surreal cloud auth`](cloud/commands/auth.md) | Sign in, sign out, and inspect credentials |
| [`surreal cloud org`](cloud/commands/org.md) | Manage organisations, usage, spend and plans |
| [`surreal cloud instance`](cloud/commands/instance.md) | Create, scale, pause, back up, connect to and delete instances |
| [`surreal cloud team`](cloud/commands/team.md) | Manage organisation members |
| [`surreal cloud invite`](cloud/commands/invite.md) | Manage organisation invitations |
| [`surreal cloud token`](cloud/commands/token.md) | Manage personal access tokens |
| [`surreal cloud catalog`](cloud/commands/catalog.md) | Browse regions, instance types and versions |
| [`surreal cloud config`](cloud/commands/config.md) | Read and write configuration |
| [`surreal cloud context`](cloud/commands/context.md) | Inspect and switch profiles |
| [`surreal cloud whoami`, `api`, `open`, `status`, `version`, `completion`](cloud/commands/misc.md) | Identity, raw API calls, dashboard links, diagnostics and shell completions |

## surreal ext

The Surrealism extension component, which builds, signs and installs extensions. Its first release is not published yet. Before SurrealDB 4.0, the same commands were `surreal db module`. See [`surreal ext`](ext.md).

## SurrealQL formatter

`surqlfmt` reformats `.surql` files to a consistent style. It is distributed as an npm package rather than as a component of `surreal`, which makes it easy to pin in a project and run in CI.

```bash
npm install -g @surrealdb/surql-fmt
surqlfmt --check ./src/**/*.surql
```

See the [SurrealQL formatter reference](formatter/overview.md) for its options and usage patterns.
