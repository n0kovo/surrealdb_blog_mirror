---
position: 1
title: Node.js
description: The SurrealDB SDK for JavaScript using the Node.js engine.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/engines/node.mdx"
---

# Node.js engine

The `@surrealdb/node` package is a plugin for the [JavaScript SDK](../installation.md) that runs SurrealDB as an embedded database within Node.js, Bun, or Deno. It supports in-memory databases and persistent storage via RocksDB and SurrealKV.

> [!IMPORTANT]
> This package works with ES modules (`import`), not CommonJS (`require`).

## Installation

First, [install the JavaScript SDK](../installation.md) if you haven't already. Then add the Node.js engine:

**npm**

```bash
npm install --save @surrealdb/node
```

**yarn**

```bash
yarn add @surrealdb/node
```

**pnpm**

```bash
pnpm install @surrealdb/node
```

## Quick start

```ts

const db = new Surreal({
    engines: {
        ...createRemoteEngines(),
        ...createNodeEngines(),
    },
});

await db.connect('mem://');

// Always close the connection when done
await db.close();
```

## Learn more

- [Connecting to SurrealDB](../concepts/connecting-to-surrealdb.md) for engine registration, embedded protocols, and connection options
- [`@surrealdb/node` on npm](https://npmjs.com/package/@surrealdb/node)
