---
position: 3
title: Installation
description: In this section, you will learn how to install the JavaScript SDK in your project.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/installation.mdx"
---

# Installation

In this section, you will learn how to install the JavaScript SDK in your project.

### Install the SDK

First, install the [SurrealDB SDK](https://npmjs.com/package/surrealdb) using your favorite package manager:

  
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

### Import the SDK into your project

After installing the SDK as a dependency, you can import the SDK into your project. Depending on your setup and environment, we supported multiple options.

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

After installing the SDK, check out the quick start guide to build your a simple application with the SDK. You can also learn more about carrying out common tasks with the SDK in the following sections:
- [Quickstart](start.md)
- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md)
- [Authentication](concepts/authentication.md)
