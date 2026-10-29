---
position: 1
title: Node.js
description: The SurrealDB SDK for JavaScript using the Node.js engine.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/engines/node.mdx"
---

# Node.js engine

The `@surrealdb/node` package is a plugin for the [JavaScript SDK](../installation.md) that runs SurrealDB as an embedded database within Node.js, Bun, or Deno.

**SurrealDB 4.0 and later**

The engine supports in-memory databases (`mem://`) and persistent storage via [SurrealKV](../../../running/file-backed.md) (`surrealkv://`).

RocksDB was removed in SurrealDB 4.0. With `@surrealdb/node-native` 4.0 or later, `rocksdb://` is a deprecated spelling of `surrealkv://`: the engine opens the path with SurrealKV and logs a warning that says to use `surrealkv://` instead. SurrealKV converts a RocksDB data directory written by SurrealDB the first time it opens it, and keeps the original files in a `_rocksdb_backup/` folder inside the directory. Take a copy of the directory before the first connection, and change the endpoint to `surrealkv://` with the same path. [Moving a RocksDB database to SurrealKV](../../../manage/self-hosted/deployment-models.md#moving-a-rocksdb-database-to-surrealkv) describes the conversion.

**Before SurrealDB 4.0**

The engine supports in-memory databases (`mem://`) and persistent storage via RocksDB (`rocksdb://`) and [SurrealKV](../../../running/file-backed.md) (`surrealkv://`).

> [!IMPORTANT]
> This package works with ES modules (`import`), not CommonJS (`require`).

## Installation

First, [install the JavaScript SDK](../installation.md) if you haven't already. Then add the Node.js engine plugin and the SurrealDB engine it runs:

**npm**

```bash
npm install --save @surrealdb/node @surrealdb/node-native
```

**yarn**

```bash
yarn add @surrealdb/node @surrealdb/node-native
```

**pnpm**

```bash
pnpm install @surrealdb/node @surrealdb/node-native
```

### Choosing the engine version

From `@surrealdb/node` 3.0.4, the SurrealDB engine is a separate package, `@surrealdb/node-native`, which the plugin declares as a peer dependency. The engine version is independent of the plugin version, so you choose which SurrealDB release runs in your process.

To run a specific release, install it by version:

```bash
npm install --save @surrealdb/node @surrealdb/node-native@3.3.2
```

The result in `package.json` looks like this:

```json title="package.json"
{
    "dependencies": {
        "surrealdb": "^2.0.1",
        "@surrealdb/node": "^3.0.4",
        "@surrealdb/node-native": "3.3.2"
    }
}
```

An exact version gives the same engine on every install. A range such as `^3.3.2` follows new engine releases when you update your dependencies.

If you do not install the engine yourself, npm 7 or later, pnpm and Bun add the newest release that satisfies the peer range. Two installs of the same `@surrealdb/node` version can then run different engines. To make every install match, pin the engine version or commit your lockfile. Yarn does not install peer dependencies, so add `@surrealdb/node-native` explicitly.

Only engine versions inside the peer range of `@surrealdb/node` are supported. A version outside the range causes a peer dependency conflict in your package manager.

To confirm which engine is loaded, for example when you report a bug, call `engineVersion()`:

```ts

console.log(engineVersion());
```

```text title="Sample output"
3.3.2
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
