---
position: 2
title: WebAssembly
description: The SurrealDB SDK for JavaScript using the WebAssembly engine.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/engines/wasm.mdx"
---

# WebAssembly engine

The `@surrealdb/wasm` package is a plugin for the [JavaScript SDK](../installation.md) that runs SurrealDB as an embedded database within a browser environment. It supports in-memory databases and persistent storage via IndexedDB, and can optionally run inside a Web Worker.

> [!IMPORTANT]
> This package works with ES modules (`import`), not CommonJS (`require`).

## Installation

First, [install the JavaScript SDK](../installation.md) if you haven't already. Then add the WASM engine:

**npm**

```bash
npm install --save @surrealdb/wasm
```

**yarn**

```bash
yarn add @surrealdb/wasm
```

**pnpm**

```bash
pnpm install @surrealdb/wasm
```

## Quick start

```ts

const db = new Surreal({
    engines: {
        ...createRemoteEngines(),
        ...createWasmEngines(),
    },
});

await db.connect('mem://');
```

## Learn more

- [Connecting to SurrealDB](../concepts/connecting-to-surrealdb.md) for engine registration, embedded protocols, and connection options
- [`@surrealdb/wasm` on npm](https://npmjs.com/package/@surrealdb/wasm)
