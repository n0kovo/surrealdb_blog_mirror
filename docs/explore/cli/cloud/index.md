---
position: 0
title: Managing SurrealDB Cloud
description: "Manage SurrealDB Cloud from the command line with surreal cloud: sign in, create and scale instances, pause and resume them, read logs and metrics, manage members, and script it in CI. Includes the move from surrealctl."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/explore/cli/cloud/index.mdx"
---

# Managing SurrealDB Cloud

`surreal cloud` is the component of the [`surreal` command](../index.md) for the SurrealDB Cloud control plane. Use it to sign in, create and list instances, scale them, pause and resume them, take backups, read logs and metrics, manage organisation members, and mint tokens, from a terminal, a shell script or a CI job.

This page covers what the component is for and gets you through a first session. It is written for operators and developers who already have a SurrealDB Cloud account. For exhaustive flag detail, see the [`surreal cloud` reference](../../../reference/cli/cloud/index.md).

## When to use which tool

- **[SurrealDB Studio](https://studio.surrealdb.com)** is the place for sign-up, browsing data, billing pages and anything you do once. The browser is the fastest route for one-off work.
- **`surreal cloud`** is for anything you want to repeat, script, schedule or review in a pull request: provisioning, scaling, pausing an environment overnight, pulling logs into a report, granting a colleague a role.
- **[`surreal db`](../database.md)** is for schema, queries and data, and for a local server during development.

`surreal cloud` and Studio use the same API, so a change made in one shows up in the other.

## Install

Install the component with the launcher. If you do not have `surreal` yet, the [install script](../install.md) installs it, and `--with cloud` adds this component in the same step.

```bash
surreal install cloud
```

Instance commands that open a shell or move data, `instance sql`, `instance import` and `instance export`, run the database through the launcher as `surreal db`, which offers to install it if it is missing. Nothing else in `surreal cloud` needs the database. To upgrade the component, run `surreal upgrade cloud`; see [Managing components](../components.md).

## Sixty-second quickstart

```bash title="First session"
surreal cloud auth login
surreal cloud whoami
surreal cloud org list
surreal cloud org use acme

surreal cloud instance create api --type shared-1 --region aws-euw1
surreal cloud instance sql api -- --ns app --db main
surreal cloud instance pause api
surreal cloud instance delete api --force
```

`auth login` opens a browser and stores the session for later commands. `org use` remembers an organisation so you do not have to name it every time. `instance create` waits until the instance is ready before it returns, so the `sql` command on the next line connects to a running database.

## Output that scripts can read

Every command takes `--json`. Every command sends its data to stdout and everything else, including progress, prompts, warnings and errors, to stderr, so a pipe always receives data and nothing else, and a failed command leaves stdout empty.

```bash title="Machine-readable output"
surreal cloud instance list --json | jq -r '.[] | select(.state == "ready") | .name'
```

## Guides

- **[Authenticating surreal cloud](authentication.md)** — Login sessions, personal access tokens, scopes and CI credentials.
- **[Organisations with surreal cloud](organisations.md)** — Choose an organisation, manage members and invitations, and read usage.
- **[Instances with surreal cloud](instances.md)** — Create, scale, pause, back up, connect to and delete instances.
- **[Scripting surreal cloud](scripting.md)** — Exit codes, waiting, non-interactive credentials and CI recipes.

## Coming from surrealctl

`surrealctl` is now `surreal cloud`, with the same commands and flags. On its first run, `surreal cloud` copies your configuration and stored login from `~/.config/surrealctl` (`%APPDATA%\surrealctl` on Windows) to `~/.surrealdb/cloud`, and says so once. The original stays in place, so an installed `surrealctl` keeps working beside it.

The `SURREALCTL_*` environment variables still work as aliases of `SURREAL_CLOUD_*`, and a run that uses any of them prints one warning naming each replacement. Update scripts to `surreal cloud` and the `SURREAL_CLOUD_` prefix.
