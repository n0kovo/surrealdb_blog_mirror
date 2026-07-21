---
position: 4
title: Embedded library quickstart
description: Integration surfaces for Spectron.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/index/quickstarts/embedded.mdx"
---

# Embedded library quickstart

Spectron runs as a **horizontally scalable service** in front of SurrealDB. Integrate through:

- **HTTP** — `/api/v1/{context_id}/...` ([REST API](../../integrations/surfaces/rest.md))
- **MCP** — `/mcp` on the same port
- **Generated SDKs** — Python (`surrealdb`) and TypeScript (`@surrealdb/spectron`)
- **Harness adapters** — LangChain, Vercel AI SDK, OpenAI Agents, n8n, Claude Code hook ([Integrations](../../integrations/index.md))

## In-process library

There is **no** supported in-process API that runs extraction and recall inside your application binary without the Spectron server. Rust, Python, and TypeScript agents call the HTTP API or SDK against a deployed Spectron instance.

## What to use

| Goal | Use |
| --- | --- |
| Python / TypeScript agent | [Python](../../integrations/sdks/python.md) or [JavaScript SDK](../../integrations/sdks/javascript-and-typescript.md) |
| Coding assistant | [MCP install](../../integrations/mcp-server/install.md) |
| LangChain / Vercel AI / OpenAI Agents | [Framework adapters](../../integrations/frameworks/langchain.md) |
| Hosted Spectron | [Hosted quickstart](https://surrealdb.com/docs/spectron/quickstarts/hosted) |

See also [Embedded library](../../integrations/surfaces/embedded-library.md) for Rust-specific notes.
