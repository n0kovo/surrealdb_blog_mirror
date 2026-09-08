---
position: 1
title: JavaScript SDK
description: The SurrealDB SDK for JavaScript enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/index.mdx"
---

# JavaScript SDK

The SurrealDB SDK for JavaScript and TypeScript lets you easily connect to SurrealDB from any environment: frontend, backend, serverless, mobile, or embedded within your app. It supports connecting to remote or embedded databases, running queries, managing data and authentication, and subscribing to real-time updates with live queries.

> [!NOTE]
> The latest version of the SDK is *(latest)*.
> The SDK works with SurrealDB versions `v2.0.0` and later, including the current release, *(latest)*.

## Getting started

- **[Installation](installation.md)** — Install the SDK and add it to your project.
- **[Getting started guide](../../languages/javascript.md)** — Connect to SurrealDB and run your first queries.

## Learn

- **[Concepts](concepts/connecting-to-surrealdb.md)** — Guides for connecting, authenticating, querying, and working with data.
- **[API Reference](api/core/surreal.md)** — Complete reference for the SDK's methods, types, and errors.

## Concepts

- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md) - open a connection over HTTP or WebSocket
- [Authentication](concepts/authentication.md) - sign up, sign in, and authenticate with a token
- [Multiple sessions](concepts/multiple-sessions.md) - run isolated sessions over a single connection
- [Executing queries](concepts/executing-queries.md) - send SurrealQL and read the results back
- [Bound queries](concepts/bound-queries.md) - interpolate values into a query safely
- [Value types](concepts/value-types.md) - how SurrealDB's types map onto native ones
- [Codecs](concepts/codecs.md) - serialise and deserialise SurrealDB values
- [Transactions](concepts/transactions.md) - group statements so they succeed or fail together
- [Live queries](concepts/live-queries.md) - stream changes as they happen
- [Invoking APIs](concepts/invoking-apis.md) - call API endpoints defined in the database
- [Utilities](concepts/utilities.md) - compare, convert and escape values
- [Error handling](concepts/error-handling.md) - what a failure looks like, and how to catch it
- [Diagnostics](concepts/diagnostics.md) - inspect protocol-level traffic
- [Embedded engines](concepts/embedded-engines.md) - run the database in the browser or on the server through WebAssembly

## Language and engines

- **[JavaScript](installation.md)**
- **[Node.js](engines/node.md)**
- **[WebAssembly](engines/wasm.md)**

## Frameworks

- **[React](frameworks/react.md)**
- **[Solid.js](frameworks/solidjs.md)**
- **[Vue.js](frameworks/vuejs.md)**
- **[Expo](frameworks/expo.md)**
- **[React Native](frameworks/react-native.md)**
- **Next.js**
- **Angular**
- **Svelte**

## Example projects

You can find example repositories that demonstrate how to integrate SurrealDB in a number of different environments:

- **[Surreal Stickies (React)](https://github.com/surrealdb/examples/tree/main/notes-v2)** — A simple note-taking application built with SurrealDB, React, and Vite.

- **[Surreal Stickies (SvelteKit)](https://github.com/surrealdb/examples/tree/main/notes-kit)** — A simple note-taking application built with SurrealDB, SvelteKit, and Vite.

- **[Surreal Presence (React)](https://github.com/Odonno/surrealdb-presence-demo)** — A demo project on how to create a realtime presence web application using SurrealDB Live Queries.

- **[TypeScript Starter](https://github.com/surrealdb/examples/tree/main/ts-bun-starter)** — A simple TypeScript starter project using Bun.

## Contributing

To contribute to the SDK code, submit an Issue or Pull Request in the [surrealdb.js](https://github.com/surrealdb/surrealdb.js) repository. To contribute to this documentation, submit an Issue or Pull Request in the [docs.surrealdb.com](https://github.com/surrealdb/docs.surrealdb.com) repository.

## Sources

- [GitHub repository](https://github.com/surrealdb/surrealdb.js)
- [NPM package](https://npmjs.com/package/surrealdb)
- [JSR package](https://jsr.io/@surrealdb/surrealdb)
