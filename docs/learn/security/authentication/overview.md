---
position: 1
title: Introduction
description: An overview of how authentication works in SurrealDB, covering system users, record users, sessions, and third-party token integration.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/security/authentication/overview.mdx"
---

# Authentication

SurrealDB supports multiple authentication methods designed for different use cases, from server administration to end-user access in client-side applications.

- [System users](authentication.md#system-users) — administrator-managed accounts with role-based access control at the root, namespace, or database level.
- [Record users](authentication.md#record-users) — application users that sign up and sign in through custom logic, restricted by table and field permissions.
- [Sessions](authentication.md#sessions) — persistent connections that carry authentication state, with configurable token and session expiration.
- [JSON Web Tokens](summary.md#json-web-tokens) — internal token management and third-party provider integration via JWKS.

For a condensed reference of all authentication-related features and links, see the [Summary](summary.md) page.
