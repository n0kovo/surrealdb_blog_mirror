---
position: 1
title: CLI Tools
description: "Reference for the three SurrealDB command-line tools: surrealctl for the control plane, surreal for the data plane, and surqlfmt for formatting SurrealQL."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/index.mdx"
---

SurrealDB ships three command-line tools. They are installed separately and cover different jobs, so most workflows use more than one of them.

| Tool | Covers | Reference |
| --- | --- | --- |
| `surrealctl` | The control plane: organisations, instances, members, tokens, and billing. | [surrealctl](surrealctl/overview.md) |
| `surreal` | The data plane: run a server, query it, and move data in and out. | [SurrealDB CLI](surrealdb-cli/overview.md) |
| `surqlfmt` | Formatting `.surql` files to a consistent style. | [SurrealQL formatter](formatter/overview.md) |

## surrealctl

`surrealctl` manages SurrealDB Cloud from the command line: it signs you in, selects an organisation, and creates, scales, pauses, and deletes instances. Every command can emit JSON, so it is the scriptable path for CI pipelines and provisioning scripts.

```bash
surrealctl auth login
surrealctl instance create api --type shared-1 --region aws-euw1
```

`surrealctl` never replaces `surreal`. For SurrealQL work against a Cloud instance it resolves the endpoint and credentials, then hands off to the `surreal` binary.

See the [surrealctl reference](surrealctl/overview.md) for installation, authentication, global flags, and every command.

## SurrealDB CLI

The `surreal` binary is the data-plane tool. It starts a server, opens an interactive SurrealQL shell, imports and exports data, validates query files, and reports the version in use.

```bash
surreal start --user root --pass secret
surreal sql --username root --password secret --pretty
```

See the [SurrealDB CLI reference](surrealdb-cli/overview.md) for a walkthrough, the [command list](surrealdb-cli/commands/index.md) for each subcommand, and [environment variables](surrealdb-cli/environment-variables.md) for the `SURREAL_*` variables that mirror its flags.

## SurrealQL formatter

`surqlfmt` reformats `.surql` files to a consistent style. It is distributed as an npm package rather than as part of the `surreal` binary, which makes it easy to pin in a project and run in CI.

```bash
npm install -g @surrealdb/surql-fmt
surqlfmt --check ./src/**/*.surql
```

See the [SurrealQL formatter reference](formatter/overview.md) for its options and usage patterns.
