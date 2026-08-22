---
position: 0
title: Overview
description: Connecting SurrealDB Agent Memory to your stack – SDKs, MCP server, AI SDKs, agent frameworks, voice tools, and automation.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/agent-memory/integrations/index.mdx"
---

# Integrations

SurrealDB Agent Memory connects to agents through HTTP, MCP, **official SDKs**, and harness adapters that mirror conversation turns into `POST /api/v1/{context_id}/facts/batch`, using the same provenance and trust model as the server.

The REST surface is described by an OpenAPI specification. The Python, TypeScript, Swift, and Kotlin clients track that spec so request and response shapes stay aligned with the server.

## MCP server (coding assistants)

Native MCP at `/mcp` on the api port, with the same **`Authorization: Bearer`** auth as REST. Prefer this when the client already speaks MCP. Point the client at your instance's `/mcp` endpoint, or install it with [`install-mcp`](https://github.com/supermemoryai/install-mcp):

```bash
npx install-mcp https://<your-context-host>/mcp \
  --client cursor \
  --header "Authorization: Bearer <your-api-key>" --oauth no
```

→ [MCP server install](mcp-server/install.md) · Per-client guides: [Claude](mcp-server/coding-assistants/claude-desktop-and-code.md) · [Cursor](mcp-server/coding-assistants/cursor.md) · [VS Code](mcp-server/coding-assistants/vscode.md) · [JetBrains](mcp-server/coding-assistants/jetbrains.md) · [Zed](mcp-server/coding-assistants/zed.md) · [Windsurf](mcp-server/coding-assistants/windsurf.md) · [Codex](mcp-server/coding-assistants/codex.md) · [Antigravity](mcp-server/coding-assistants/antigravity.md) · [OpenCode](mcp-server/coding-assistants/opencode.md)

## SDKs

Call SurrealDB Agent Memory directly from application code.

| Language | Package |
| --- | --- |
| Dart | `surrealdb` (import `spectron.dart`) |
| Elixir | `:surrealdb` (`SurrealDB.Spectron`) |
| Go | `spectron` package in `surrealdb.go` |
| Haskell | `surrealdb-spectron` |
| JavaScript / TypeScript | `@surrealdb/spectron` |
| Kotlin | bundled in `com.surrealdb:kotlin` |
| Python | `surrealdb` (SurrealDB Agent Memory ships inside it) |
| Swift | `Spectron` product in `surrealdb.swift` |

→ [Dart](sdks/dart.md) · [Elixir](sdks/elixir.md) · [Go](sdks/go.md) · [Haskell](sdks/haskell.md) · [JavaScript & TypeScript](sdks/javascript-and-typescript.md) · [Kotlin](sdks/kotlin.md) · [Python](sdks/python.md) · [Swift](sdks/swift.md)

## AI SDKs

Drop-in memory for the popular TypeScript AI SDKs, with recall and storage wrapped around your model calls.

- **Cloudflare Workers AI**: the client inside a Worker, alongside Workers AI models.
- **TanStack AI**: the `@surrealdb/spectron` client in TanStack Start server routes.
- **Vercel AI SDK**: `@surrealdb/spectron-vercel-ai`, via `wrapLanguageModel` middleware and a tool set.

→ [Cloudflare Workers AI](ai-sdks/cloudflare-workers-ai.md) · [TanStack AI](ai-sdks/tanstack-ai.md) · [Vercel AI SDK](ai-sdks/vercel-ai-sdk.md)

## Agent frameworks

Harness adapters expose SurrealDB Agent Memory as agent tools and add automatic per-turn memory, without changing your prompts.

| Framework | Package | Language |
| --- | --- | --- |
| CrewAI | `spectron-crew-ai` | Python |
| Eve | `@surrealdb/spectron-eve` | TypeScript |
| Google ADK | `spectron-google-adk` | Python |
| Hermes Agent | `spectron-hermes` | Python |
| LangChain / LangGraph | `@surrealdb/langchain`, `@surrealdb/langgraph` | TypeScript |
| Mastra | `@surrealdb/mastra-ai` | TypeScript |
| OpenAI Agents SDK | `spectron-openai-agents-sdk` | Python |
| OpenClaw | `@surrealdb/spectron-openclaw` | TypeScript |
| Pydantic AI | `spectron-pydantic-ai` | Python |
| Strands Agents | `spectron-strands-agents` | Python |

→ [CrewAI](frameworks/crewai.md) · [Eve](frameworks/eve.md) · [Google ADK](frameworks/google-adk.md) · [Hermes Agent](frameworks/hermes.md) · [LangChain](frameworks/langchain.md) · [Mastra](frameworks/mastra.md) · [OpenAI Agents SDK](frameworks/openai-agents.md) · [OpenClaw](frameworks/openclaw.md) · [Pydantic AI](frameworks/pydantic-ai.md) · [Strands Agents](frameworks/strands-agents.md)

Frameworks without a dedicated package integrate directly through the SDK: [Agno](frameworks/agno.md) · [AutoGen](frameworks/autogen.md) · [Camel AI](frameworks/camel-ai.md) · [LlamaIndex](frameworks/llamaindex.md)

## Voice & realtime

Give voice agents memory that persists across calls.

→ [ElevenLabs](voice/elevenlabs.md) · [LiveKit](voice/livekit.md)

## Automation

- **n8n**: the `@surrealdb/n8n-nodes-surrealdb` community node, plus SurrealDB Agent Memory over the REST API.
- **Zo Computer**: a Zo skill that calls the SurrealDB Agent Memory SDK for recall and storage.

→ [n8n](automation/n8n.md) · [Zo Computer](automation/zo-computer.md)

## Observability

Run SurrealDB Agent Memory for memory while an observability platform traces and evaluates the agent.

→ [AgentOps](observability/agentops.md) · [Respan](observability/respan.md)

## REST API

Direct HTTP from any language. End-user routes: `/api/v1/{context_id}/…`. Management: `/api/v1/contexts/…`.

→ [REST integration guide](surfaces/rest.md) · [Full reference](../reference/rest-api.md)

## Not shipped yet

- **Embedded in-process library**: use REST or an SDK against a deployed instance ([Embedded quickstart](https://surrealdb.com/docs/agent-memory/quickstarts/embedded)).
