---
position: 1
title: Security
description: Secure a SurrealDB deployment with authentication and authorisation. Plus security best practices.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/security/index.mdx"
---

# Security

SurrealDB provides a layered security model that covers how users and systems prove their identity, what they are allowed to do once authenticated, and the operational practices that keep a deployment safe.

This section is organised into three areas:

- [Authentication](authentication/overview.md) - signing in with credentials, record-based access, and third-party identity providers.
- [Authorization](authorization/permissions-and-row-level-security.md) - controlling access at the table, field, and row level with the `PERMISSIONS` clause and JWTs.
- [Best practices](best-practices/security-best-practices.md) - guidance on secure configuration, token handling, network exposure, and common pitfalls.

## Authorization

- [Tokens & JWTs](authorization/tokens-and-jwts.md) - how a token carries identity and what the database checks

- [Guest access](authorization/capabilities.md#guest-access) - letting clients that have not signed in read public tables or call public functions, turned on with `--allow-guests` and limited by each table's and function's `PERMISSIONS`

Logic that goes beyond reading and writing records, such as an order that has to update stock and create an invoice together, can live in the database as a [custom function](../querying/concepts-and-guides/custom-functions.md) or behind an HTTP endpoint defined with [`DEFINE API`](../../reference/query-language/statements/define/api.md). A function's `PERMISSIONS` clause decides who may call it, while its body runs with the caller's own table and field permissions - see [function permissions](../../reference/query-language/statements/define/function.md#permissions).

## Troubleshooting

- [Troubleshooting](best-practices/troubleshooting.md) - what a rejected token, an expired session or a denied permission looks like, and what to check
