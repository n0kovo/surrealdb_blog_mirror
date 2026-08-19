---
position: 1
title: Overview
description: A map of every surrealctl command group and leaf command, with links to the page documenting each one.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/surrealctl/commands/index.mdx"
---

# Commands

`surrealctl` groups its commands by noun. A group on its own prints its own help; the leaf commands below do the work. Every command accepts the [global flags](../global-flags.md), and every command except [`token create`](token.md#token-create) accepts `--json`.

| Group | Leaf commands |
| --- | --- |
| [`auth`](auth.md) | `login`, `logout`, `status`, `refresh`, `scopes` |
| [`org`](org.md) | `list`, `get`, `create`, `update`, `archive`, `use`, `roles`, `permissions`, `usage`, `spend`, `plans` |
| [`instance`](instance.md) | `list`, `get`, `create`, `update`, `delete`, `pause`, `resume`, `watch`, `status`, `endpoint`, `token`, `jwks`, `sql`, `import`, `export`, `metrics`, `logs`, `usage`, `estimate`, `capabilities get`, `capabilities set`, `backup list`, `backup create`, `backup policy get`, `backup policy set` |
| [`team`](team.md) | `list`, `get`, `invite`, `update`, `remove` |
| [`invite`](invite.md) | `list`, `create`, `delete` |
| [`token`](token.md) | `list`, `create`, `delete`, `scopes` |
| [`catalog`](catalog.md) | `regions`, `instance-types`, `storage-types`, `instance-versions`, `billing-countries` |
| [`spectron`](spectron.md) | `context`, `key`, `scoped-key`, `access-token`, `principal`, `package`, `scopes`, `verbs`, `providers`, `usage`, `config` |
| [`config`](config.md) | `list`, `get`, `set`, `unset`, `path`, `edit` |
| [`context`](context.md) | `show`, `use`, `list` |
| [Other commands](misc.md) | `whoami`, `api`, `open`, `status`, `version`, `completion` |

## Aliases

Plural spellings of the group nouns work, and so do two verb aliases. Nothing else is aliased.

| Alias | Means |
| --- | --- |
| `orgs`, `instances`, `teams`, `invites`, `tokens`, `contexts` | The singular group |
| `ls` | `list` |
| `rm` | `delete` — and `team remove` |
| `doctor` | `status` |

## Reading these pages

Each leaf command gets a usage block, a table of its arguments, a table of its own options, at least one runnable example, and a note on how it refuses.

Usage blocks are notation, not commands: `<NAME>` is a value you must supply, `[NAME]` one you may, `[OPTIONS]` any number of flags, and `...` marks something repeatable. Copy from the examples instead.

Flags shared across many commands are documented once:

- The [global flags](../global-flags.md), accepted everywhere.
- The [list presentation flags](../output-and-exit-codes.md#list-presentation-flags) — `--columns`, `--wide`, `--no-header`, `--sort`, `--reverse` and `--limit` — carried by every list-shaped command.
- The [wait flags](../long-running-operations.md#the-wait-flags) — `--wait`, `--no-wait` and `--wait-timeout` — carried by five `instance` commands.

For queries, imports, exports and running a server, use the [`surreal` CLI](../../surrealdb-cli/overview.md) instead. See the [overview](../overview.md) for where that boundary sits.
