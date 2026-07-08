---
position: 1
title: JavaScript
description: Embedding SurrealDB in JavaScript
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/embedding/by-language/javascript.mdx"
---

# Embedding in JavaScript

SurrealDB is designed to be run in many different ways and in many environments. Due to the [separation of the storage and compute](../../../architecture.md) layers, SurrealDB can be run in embedded mode, from within your JavaScript environments. 

You can embed SurrealDB in both browser and server environments. In browser environments using the [Wasm engine](../../../reference/javascript/engines/wasm.md), SurrealDB can be run as an in-memory database, or it can persist data using IndexedDB. In server environments using the [Node.js engine](../../../reference/javascript/engines/node.md), SurrealDB can be run as an embedded database, backed by either an in-memory engine or [SurrealKV](../../../running/file-backed.md).

In this document, we will cover how to embed SurrealDB in both browser and server environments.

## Browser
In browser environments, using the [Wasm engine](../../../reference/javascript/engines/wasm.md), you can run SurrealDB in-memory or with IndexedDB persistence.

For more information on how to embed SurrealDB in browser environments, please see the [Wasm engine](../../../reference/javascript/engines/wasm.md) documentation.

## Server

In server environments, you can use the [Node.js engine](../../../reference/javascript/engines/node.md) to run SurrealDB as an embedded database. 

For more information on how to embed SurrealDB in server environments, please see the [Node.js engine](../../../reference/javascript/engines/node.md) documentation.
