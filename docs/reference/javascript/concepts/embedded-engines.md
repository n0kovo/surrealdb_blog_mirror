---
position: 10
title: Embedded engines
description: Run SurrealDB as an embedded database in the browser or on the server using the WebAssembly and Node.js engine plugins.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/concepts/embedded-engines.mdx"
---

# Embedded engines

The JavaScript SDK supports running SurrealDB as an embedded database through two engine plugins. Choose the one that matches your environment:

| Engine | Package | Environment | Storage options |
|--------|---------|-------------|-----------------|
| WebAssembly | `@surrealdb/wasm` | Browsers | `mem://`, `indxdb://` |
| Node.js | `@surrealdb/node` | Node.js, Bun, Deno | `mem://`, `rocksdb://`, `surrealkv://` |

Both plugins work with ES modules (`import`), not CommonJS (`require`).

## WebAssembly engine (browser)

The `@surrealdb/wasm` package runs SurrealDB inside a browser environment. It supports in-memory databases and persistent storage via IndexedDB, and can optionally run inside a Web Worker to keep the main thread responsive.

### Installation

```bash
npm install --save @surrealdb/wasm
```

### Registering the engine

```ts

const db = new Surreal({
    engines: {
        ...createRemoteEngines(),
        ...createWasmEngines(),
    },
});

await db.connect('mem://');
// or persist with IndexedDB:
await db.connect('indxdb://myapp');
```

### Running in a web worker

Offload database operations from the main thread to keep your interface responsive:

```ts

const db = new Surreal({
    engines: {
        ...createRemoteEngines(),
        ...createWasmWorkerEngines({
            createWorker: () => new WorkerAgent(),
        }),
    },
});

await db.connect('mem://');
```

### Bundler configuration

If you are using a bundler like Vite, you may need to exclude the WASM package from dependency optimisation and enable top-level await:

```js title="vite.config.js"
export default {
    optimizeDeps: {
        exclude: ['@surrealdb/wasm'],
        esbuildOptions: {
            target: 'esnext',
        },
    },
    esbuild: {
        supported: {
            'top-level-await': true,
        },
    },
};
```

## Node.js engine (server)

The `@surrealdb/node` package runs SurrealDB within Node.js, Bun, or Deno. It supports in-memory databases and persistent storage via RocksDB and SurrealKV.

### Installation

```bash
npm install --save @surrealdb/node
```

### Registering the engine

```ts

const db = new Surreal({
    engines: {
        ...createRemoteEngines(),
        ...createNodeEngines(),
    },
});

await db.connect('mem://');
// or persist with SurrealKV:
await db.connect('surrealkv://./data');
```

To enable [versioned storage](../../query-language/statements/select.md#version) for temporal queries, append `?versioned=true` to the connection string:

```ts
await db.connect('surrealkv://./data?versioned=true');
```

### Closing the connection

When using the Node.js engine, you must close the connection with `.close()` when you are done to ensure the database is properly shut down:

```ts
await db.close();
```

## Learn more

- [WebAssembly engine reference](../engines/wasm.md)
- [Node.js engine reference](../engines/node.md)
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for connection options and reconnection behaviour
- [`@surrealdb/wasm` on npm](https://npmjs.com/package/@surrealdb/wasm)
- [`@surrealdb/node` on npm](https://npmjs.com/package/@surrealdb/node)
