---
position: 1
title: SurrealKit schema migration
description: SurrealKit is the official schema management and migration CLI for SurrealDB. Define your schema in .surql files and keep databases in sync across every environment.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/schema-migration/index.mdx"
---

# SurrealKit

> [!NOTE]
> All of the example commands in this tutorial assume a database running at `http://localhost:8000`, a root user named `root` with the password `secret`, a namespace `main` and a database `main`.
> As host `http://localhost:8000`, namespace `main` and database `main` are default values, only the necessary `--user root` and `--pass secret` will be shown alongside each command.
> To test these commands without `--user root` and `--pass secret`, authentication can be disabled by passing in the `--unauthenticated` flag when [starting the SurrealDB server](../../reference/cli/surrealdb-cli/commands/start.md).

SurrealKit is the official schema management and migration CLI for SurrealDB. You define your database schema as plain `.surql` files, commit them alongside your application code, and SurrealKit keeps every environment in sync with those definitions.

It has two modes for getting schema into a database:

- **Sync:** immediately pushes your schema files to the connected database. Best for local development and ephemeral environments where fast iteration matters and losing data is acceptable.
- **Rollouts:** generates a reviewed, phased migration manifest and applies changes in non-destructive then destructive passes, with rollback support. Best for shared, staging, and production databases.

Most teams use Sync day-to-day and switch to Rollouts when promoting changes to shared environments.

SurrealKit also provides:

- **Templates:** scaffold a new project from a template with selectable features (`surrealkit init`).
- **Seeding:** apply `.surql` seed data on demand.
- **Type generation:** introspect a database to emit JSON and TypeScript types for your application.
- **Testing:** a declarative framework for validating schema, permissions, and API endpoints.

## Installation

**cargo binstall** (recommended, no compilation required once [cargo binstall is installed](https://github.com/cargo-bins/cargo-binstall#installation)):

```bash
cargo binstall surrealkit
```

**Cargo from source:**

```bash
cargo install surrealkit
```

**Docker:**

```bash
docker pull ghcr.io/surrealdb/surrealkit:latest
```

Prebuilt binaries for Linux (x86_64 / aarch64), macOS (x86_64 / aarch64), and Windows (x86_64) are available on the [GitHub releases page](https://github.com/surrealdb/surrealkit/releases).

## Initialise a project

```bash
surrealkit init
```

This scaffolds a project from a template, letting you pick which optional features to include. It always writes the base layout:

```
database/
├── schema/        # .surql schema definition files
├── rollouts/      # rollout manifests (generated)
├── snapshots/     # schema and catalog snapshots
├── seed/          # optional seed data
├── tests/         # test suites and config
└── setup.surql    # runs before sync
surrealkit.toml    # project configuration
```

See [Project templates](templates.md) for the feature checklist, non-interactive flags, and custom templates.

## Connection configuration

SurrealKit resolves connection details in the following order (first match wins):

1. CLI arguments (`--host`, `--ns`, `--db`, `--user`, `--pass`, `--auth-level`)
2. `SURREALDB_*` environment variables
3. `.env` file in the working directory
4. Fallback `DATABASE_*` environment variables

| Environment variable | CLI equivalent | Purpose |
|---|---|---|
| `SURREALDB_HOST` | `--host` | Database endpoint URL |
| `SURREALDB_NAMESPACE` | `--ns` | Namespace |
| `SURREALDB_NAME` | `--db` | Database name |
| `SURREALDB_USER` | `--user` | Username |
| `SURREALDB_PASSWORD` | `--pass` | Password |
| `SURREALDB_AUTH_LEVEL` | `--auth-level` | `root`, `namespace`/`ns`, or `database`/`db` |

The project root (containing `schema/`, `rollouts/`, `snapshots/`, `seed/`, and `tests/`) defaults to `./database`. Override it with the global `--folder` flag or the `SURREALDB_FOLDER` environment variable.

Example connecting via CLI flags:

```bash
surrealkit --user root --pass secret sync
```

## Next steps

- [New databases](getting-started/new-databases.md): start a fresh project with SurrealKit from the beginning
- [Existing databases](getting-started/existing-databases.md): adopt SurrealKit in a project that already has a database
- [Sync vs Rollouts](getting-started/sync-vs-rollouts.md): choose the right mode for each environment
- [Project templates](templates.md): scaffold a project with selectable features
- [Type generation](typegen.md): generate JSON and TypeScript types from your schema
