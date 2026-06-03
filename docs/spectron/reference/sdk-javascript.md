---
position: 5
title: JavaScript SDK reference
description: Package layout and configuration for @surrealdb/spectron.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/reference/sdk-javascript.mdx"
---

# JavaScript SDK reference

| Item | Value |
| --- | --- |
| npm package | `@surrealdb/spectron` |
| Source | `spectron/clients/typescript/` |
| OpenAPI input | `doc/spec/*.swagger.json` |

## Install

```bash
npm install @surrealdb/spectron
```

## Configuration

```typescript

const client = createSpectronClient({
  baseUrl: process.env.SPECTRON_URL!,
  apiKey: process.env.SPECTRON_API_KEY!,
  contextId: process.env.SPECTRON_CONTEXT_ID!,
});
```

Uses **`API-KEY`** header authentication (not `Authorization: Bearer`).

## Core operations

Same REST mapping as Python; see the [REST API](rest-api.md).

## Harness adapter

```bash
npm install @surrealdb/spectron-vercel-ai
```

→ [Vercel AI SDK](../integrations/frameworks/vercel-ai-sdk.md)

## User guide

→ [JavaScript and TypeScript SDK](../integrations/sdks/javascript-and-typescript.md)
