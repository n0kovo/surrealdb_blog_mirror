---
position: 2
title: Upgrades & patching
description: "Upgrade SurrealDB safely: binary replacement, surreal fix for major versions, migrations, and cluster rolling upgrades."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/self-hosted/upgrades-and-patching.mdx"
---

# Upgrades & patching

**Routine upgrades** typically follow: quiesce or drain clients if your SLA allows, **stop** the server gracefully, **replace** the `surreal` binary with the new release, then **start** with unchanged data paths and reviewed configuration.

Read the release notes for breaking changes, new defaults, or removed flags before you cut over. Re-run integration tests against the new version before promoting the change across your organisation.

Across **major versions**, on-disk formats may change. When documentation requires it, run [`surreal fix`](../../reference/cli/surrealdb-cli/commands/fix.md) to migrate data between layouts, and follow [Migrating from older SurrealDB versions](../../build/migrating/from-old-surrealdb-versions/overview.md) plus any linked guides (for example between specific major lines).

**Rolling upgrades** in **clustered** setups usually upgrade one node at a time: verify cluster health, upgrade a member, wait for replication or quorum to stabilise, then continue.

Never skip staging validation for production-like data volumes. If the cluster spans regions, plan maintenance windows that respect dependency order between tiers.

**Before any upgrade**, take a fresh backup—[`surreal export`](../../reference/cli/surrealdb-cli/commands/export.md) for a logical copy and/or a storage snapshot—so you can revert if migration or client incompatibility surfaces after deploy.

Patch **security** releases promptly: subscribe to SurrealDB advisories, test the patch build in staging, then roll out using the same stop–replace–start or rolling pattern your architecture supports. Document the upgraded version in your asset inventory for compliance reviews.
