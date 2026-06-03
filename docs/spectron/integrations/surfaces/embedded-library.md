---
position: 2
title: Embedded library
description: In-process integration surfaces.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/integrations/surfaces/embedded-library.mdx"
---

# Embedded library

Spectron runs as a **horizontally scalable HTTP service** in front of SurrealDB. Application code integrates through:

| Surface | Description |
| --- | --- |
| **REST** | `/api/v1/{context_id}/...` |
| **MCP** | `/mcp` on the same port |
| **SDKs** | `surrealdb-spectron`, `@surrealdb/spectron` |
| **Harness adapters** | LangChain, Vercel AI SDK, OpenAI Agents, n8n, Claude Code hook |

There is no supported in-process library that runs extraction and recall inside your binary without the Spectron server.

## Rust agents

Deploy **`spectrond`** with [Docker](../../self-hosting/deployment/docker.md) and call the HTTP API or generated client.

## Related

- [Embedded quickstart](https://surrealdb.com/docs/spectron/quickstarts/embedded)
- [Self-hosted quickstart](https://surrealdb.com/docs/spectron/quickstarts/self-hosted)
