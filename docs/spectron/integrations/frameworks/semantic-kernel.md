---
position: 2
title: Semantic Kernel
description: Semantic Kernel integration status.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/integrations/frameworks/semantic-kernel.mdx"
---

# Semantic Kernel

> **Status:** No Semantic Kernel adapter is available yet. This page is a placeholder.

## Recommended approach today

1. Call **`POST /api/v1/{context_id}/facts/batch`** after each SK chat turn (custom plugin or middleware).
2. Call **`POST /api/v1/{context_id}/query`** or **`/context`** before invoking the kernel planner.
3. Or expose Spectron via **MCP** if your host supports it.

See [REST API](../../reference/rest-api.md) and [Integrations overview](../index.md).

When an official `spectron-semantic-kernel` package is added under `clients/`, this page will document install lines and hook points.
