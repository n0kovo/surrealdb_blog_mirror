---
position: 1
title: Overview
description: What surrealctl is, where the control plane ends and the SurrealDB CLI begins, the command grammar, and how this reference is organised.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/surrealctl/overview.mdx"
---

# surrealctl

`surrealctl` manages SurrealDB Cloud from the command line. It creates and scales instances, reads logs and metrics, manages organisation members and invitations, mints credentials, and drives SurrealDB Agent Memory contexts — all through the SurrealDB API at `https://api.surrealdb.com`.

This reference is for operators, CI pipelines and agents. Every command emits machine-readable JSON on request, keeps its data payload on stdout, and returns an exit code precise enough to branch on.

## The control plane and the data plane

`surrealctl` owns the **control plane**: the resources around a database — instances, organisations, members, tokens, capabilities, backups. The [`surreal` CLI](../surrealdb-cli/overview.md) owns the **data plane**: queries, imports, exports, and running a server. The two are siblings, and `surrealctl` follows the same conventions so you can move between them without relearning anything.

| Task | Tool |
| --- | --- |
| Create, scale, pause or delete a Cloud instance | `surrealctl instance` |
| Read an instance's logs, metrics or usage | `surrealctl instance` |
| Invite a colleague, change their role | `surrealctl team`, `surrealctl invite` |
| Mint a database token or fetch a key set | `surrealctl instance token`, `surrealctl instance jwks` |
| Run a SurrealQL query | [`surreal sql`](../surrealdb-cli/commands/sql.md) |
| Run a local server | [`surreal start`](../surrealdb-cli/commands/start.md) |

Three commands cross the boundary. [`instance sql`](commands/instance.md#instance-sql), [`instance import`](commands/instance.md#instance-import) and [`instance export`](commands/instance.md#instance-export) resolve the instance, mint a database token, and hand off to the `surreal` binary rather than reimplementing SurrealQL. Everything after a `--` separator is forwarded to `surreal` verbatim. See [the `surreal` handoff](../../../manage/surrealctl/install.md#the-surreal-handoff) for how the binary is located.

## Before you start

This reference documents commands and flags. For installing `surrealctl`, signing in, and a first walkthrough, see the [surrealctl guide](../../../manage/surrealctl/index.md).

| Task | Page |
| --- | --- |
| Install the binary and sign in | [Install](../../../manage/surrealctl/install.md) |
| Choose between a login session and a token | [Authentication](../../../manage/surrealctl/authentication.md) |
| Work through a first instance | [Instances](../../../manage/surrealctl/instances.md) |

## Command grammar

The grammar is regular, and worth learning once:

- **Groups are singular nouns.** `instance`, not `instances` — the plural is a visible alias.
- **Verbs are `list`, `get`, `create`, `update`, `delete`.** The only aliases are `ls` for `list` and `rm` for `delete`.
- **Destructive commands take `--force`**, never `--skip-confirmations`. The global `--yes` pre-answers every confirmation in one invocation.
- **`--json` is the only encoding switch.** There is no `--format`.
- **Two deliberate exceptions**, both in `team`: `team remove` ends a membership rather than deleting a person, and `team invite` sends an invitation, which no house verb covers.

Any noun group invoked on its own prints its own help, and `help` works at every level:

```bash
surrealctl instance
surrealctl help instance create
```

## How this reference is organised

The cross-cutting pages describe behaviour shared by every command. Read them once.

| Page | Covers |
| --- | --- |
| [Authentication](authentication.md) | Login sessions, personal access tokens, and where credentials are stored |
| [Global flags](global-flags.md) | The 16 flags every command accepts, their environment variables, and the precedence chain |
| [Output and exit codes](output-and-exit-codes.md) | The `--json` contract, the stream split, list presentation flags, and every exit code |
| [Long-running operations](long-running-operations.md) | `--wait`, `--no-wait`, polling behaviour, and exit code `10` |

The command pages document every flag, argument and refusal, one page per group:

| Group | Purpose |
| --- | --- |
| [`auth`](commands/auth.md) | Sign in, sign out, and inspect credentials |
| [`org`](commands/org.md) | Manage organisations, roles, usage and spend |
| [`instance`](commands/instance.md) | Manage instances, capabilities and backups |
| [`team`](commands/team.md) | Manage organisation members |
| [`invite`](commands/invite.md) | Manage organisation invitations |
| [`token`](commands/token.md) | Manage personal access tokens |
| [`catalog`](commands/catalog.md) | Browse the platform catalogues |
| [`spectron`](commands/spectron.md) | Manage SurrealDB Agent Memory contexts, keys and principals |
| [`config`](commands/config.md) | Read and write configuration |
| [`context`](commands/context.md) | Inspect and switch profiles |
| [`whoami`, `api`, `open`, `status`, `version`, `completion`](commands/misc.md) | Identity, the raw API escape hatch, and diagnostics |

## Reference syntax

Usage blocks in this reference use one notation throughout:

| Notation | Meaning |
| --- | --- |
| `<NAME>` | A required value you supply |
| `[NAME]` | An optional value you supply |
| `[OPTIONS]` | Zero or more flags |
| `...` | The preceding item may be repeated |
| `--` | Everything after this separator is passed to another program |

Usage blocks are notation, not commands — they carry brackets a shell will not accept. Copy from the examples instead.

## Resource references

Most commands accept a resource by more than one spelling. An organisation is named by id or name. An instance is named by id, slug, name, or `org/name`. A bare id is used without a lookup; anything else is resolved against the organisation in force, and an unrecognised name is answered with a did-you-mean list.

Omit the reference entirely and, on a terminal, the command offers an interactive picker. In a non-interactive session it exits `2` and lists what was available, so a CI failure names the fix.

```bash
surrealctl instance get production
surrealctl instance get acme/production
surrealctl instance get 67upif0m8sh1cn1p2c8t
```
