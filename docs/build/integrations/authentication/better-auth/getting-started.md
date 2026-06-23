---
position: 1
title: Getting started
description: Install the @surrealdb/better-auth adapter, connect to SurrealDB, configure the adapter, and generate your Better Auth schema.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/integrations/authentication/better-auth/getting-started.mdx"
---

# Getting started

This guide walks through installing the `@surrealdb/better-auth` adapter, connecting it to SurrealDB, and generating the schema Better Auth needs.

## Installation

Install the adapter alongside `better-auth` and the [SurrealDB JavaScript SDK](../../../../languages/javascript/index.md):

**Bun**

```bash
bun add @surrealdb/better-auth better-auth surrealdb
```

**npm**

```bash
npm install @surrealdb/better-auth better-auth surrealdb
```

**pnpm**

```bash
pnpm add @surrealdb/better-auth better-auth surrealdb
```

## Quick start

Connect a `Surreal` client, then pass it to `surrealAdapter` as the `database` option in your Better Auth configuration. Better Auth manages all table operations through the adapter.

```typescript

const db = new Surreal();
await db.connect('ws://localhost:8000/rpc');
await db.use({ namespace: 'namespace', database: 'database' });

export const auth = betterAuth({
    database: surrealAdapter({ db }),
    emailAndPassword: { enabled: true },
});
```

## Connecting to SurrealDB

The adapter accepts any connected `Surreal` instance. Connect it before passing it to `surrealAdapter`. Use WebSocket for long-running servers and HTTP for stateless environments such as serverless functions.

```typescript

const db = new Surreal();

// WebSocket (recommended for persistent servers)
await db.connect('ws://localhost:8000/rpc', {
    namespace: 'myapp',
    database: 'production',
    authentication: {
        username: 'root',
        password: 'root',
    },
});

// HTTP (for stateless environments)
await db.connect('http://localhost:8000', {
    namespace: 'myapp',
    database: 'production',
});
```

For a full reference of connection options, see [Connecting to SurrealDB](../../../../languages/javascript/concepts/connecting-to-surrealdb.md) in the JavaScript SDK documentation.

## Configuration options

`surrealAdapter` accepts the following options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `db` | `Surreal` | required | A connected SurrealDB client instance. |
| `usePlural` | `boolean` | `false` | Use plural table names (`users` instead of `user`). |
| `schemaMode` | `'schemafull' \| 'schemaless'` | `'schemafull'` | Table mode used by the generated schema. `schemaless` keeps known fields typed and indexed while still accepting writes to undeclared fields. |

```typescript
surrealAdapter({
    db,
    usePlural: true, // use plural table names
});
```

## Schema generation

The adapter includes a `createSchema` implementation that generates SurrealQL DDL statements for all Better Auth tables. Use the Better Auth CLI to produce a `schema.surql` file:

```bash
bunx @better-auth/cli generate --output schema.surql
```

Then apply it to your SurrealDB instance:

```bash
surreal import --conn http://localhost:8000 \
    --ns myapp --db production \
    --user root --pass root \
    schema.surql
```

The generated schema uses `SCHEMAFULL` tables by default. Each field is typed from the Better Auth schema:

- Required fields take a concrete type (`string`, `datetime`, `bool`, and so on).
- Optional fields use `option<T | null>`, so they accept a typed value, a stored `NULL`, or a missing value.
- Object fields are marked `FLEXIBLE` so they can hold arbitrary keys.
- `DEFINE INDEX` statements are emitted for unique fields and for fields Better Auth marks as indexed.

Every statement uses `IF NOT EXISTS`, so the file is safe to reapply.

> [!NOTE]
> If your app adds many dynamic plugin fields and you would rather not regenerate the schema each time, set `schemaMode: 'schemaless'`. Known fields stay typed and indexed, and writes to undeclared fields are accepted.

## Table names

By default the adapter uses singular table names: `user`, `session`, `verification`, and `account`. Set `usePlural: true` to use plural names instead.

Better Auth also lets you override model names per-table via the `modelName` option in your configuration, and the adapter respects those overrides automatically.

## Next steps

- [Overview](overview.md): adapter capabilities and prerequisites
- [Plugins](plugins.md): use any Better Auth plugin and the SurrealQL helper functions generated for the organisation plugin.
- [Transactions & limitations](transactions-and-limitations.md): how transactions behave and what to be aware of.
