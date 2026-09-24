---
position: 12
title: Manage
description: "Running SurrealDB in production: managed instances and organisations. Billing, the surrealctl CLI, observability, schema migration and self-hosting."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/manage.mdx"
---

# Manage

This section contains operational documentation for both SurrealDB Cloud and self-hosted deployments. These pages assume a database that already exists and concentrate on keeping it running, observable and up to date.

- **[Instances](manage/instances/index.md)** — Create, connect to, scale, back up and monitor managed instances.
- **[Organisations](manage/organisations/index.md)** — Members, roles, invitations and billing for a team.
- **[surrealctl](manage/surrealctl/index.md)** — Manage instances and organisations from the command line.
- **[Observability](manage/observability/index.md)** — Metrics, logs, traces and slow-query analysis.
- **[Schema migration](manage/schema-migration/index.md)** — Promote schema changes safely with SurrealKit.
- **[Self-hosted](manage/self-hosted/index.md)** — Run and operate SurrealDB on your own infrastructure.

## Enterprise

[SurrealDB Enterprise](manage/enterprise/index.md) adds the controls a regulated deployment needs, including FIPS-validated cryptography and single sign-on.

## Related sections

The full command surface for `surrealctl`, `surreal` and `surqlfmt` is in the [CLI reference](reference/cli/index.md). The pages here cover what to run and when; the reference covers every flag.
