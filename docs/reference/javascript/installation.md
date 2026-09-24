---
position: 3
title: Installation
description: In this section, you will learn how to install the JavaScript SDK in your project.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/installation.mdx"
---

# Installation

This page shows how to install the JavaScript SDK and import it into your project.

## Install the SDK

First, install the [SurrealDB SDK](https://npmjs.com/package/surrealdb) using your preferred package manager:

**bun**

```bash
bun install surrealdb
```

**npm**

```bash
npm install --save surrealdb
```

**yarn**

```bash
yarn add surrealdb
```

**pnpm**

```bash
pnpm install surrealdb
```

> [!NOTE]
> The SurrealDB SDK for JavaScript is also available in the JSR registry as [`@surrealdb/surrealdb`](https://jsr.io/@surrealdb/surrealdb).

## Import the SDK into your project

After installing the SDK as a dependency, you can import the SDK into your project. The SDK supports several import options, depending on your setup and environment.

**ESM**

```ts
```

**CommonJS**

```ts
const { Surreal } = require('surrealdb');
```

**Deno**

```ts
//Importing from Deno

// Import with version 
```

  
**CDN**

```ts
// or
```

## Next steps

After installing the SDK, see the quick start guide to build a simple application with the SDK. You can also learn more about carrying out common tasks with the SDK in the following sections:
- [Getting started](../../languages/javascript.md)
- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md)
- [Authentication](concepts/authentication.md)
