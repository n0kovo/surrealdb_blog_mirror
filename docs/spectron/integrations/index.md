---
position: 0
title: Overview
description: Connecting Spectron to your stack – SDKs, MCP server, AI SDKs, agent frameworks, voice tools, and automation.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/integrations/index.mdx"
---

# Integrations

Spectron connects to agents through HTTP, MCP, **official SDKs**, and harness adapters that mirror conversation turns into `POST /api/v1/{context_id}/facts/batch`, using the same provenance and trust model as the server.

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

Call Spectron directly from application code.

| Language | Package |
| --- | --- |
| Python | `surrealdb` (Spectron ships inside it) |
| JavaScript / TypeScript | `@surrealdb/spectron` |
| Swift | `Spectron` product in `surrealdb.swift` |
| Kotlin | bundled in `com.surrealdb:kotlin` |
| Go | `spectron` package in `surrealdb.go` |
| Dart | `surrealdb` (import `spectron.dart`) |
| Elixir | `:surrealdb` (`SurrealDB.Spectron`) |
| Haskell | `surrealdb-spectron` |

→ [Python](sdks/python.md) · [JavaScript & TypeScript](sdks/javascript-and-typescript.md) · [Swift](sdks/swift.md) · [Kotlin](sdks/kotlin.md) · [Go](sdks/go.md) · [Dart](sdks/dart.md) · [Elixir](sdks/elixir.md) · [Haskell](sdks/haskell.md)

## AI SDKs

Drop-in memory for the popular TypeScript AI SDKs, with recall and storage wrapped around your model calls.

- **Vercel AI SDK**: `@surrealdb/spectron-vercel-ai`, via `wrapLanguageModel` middleware and a tool set.
- **TanStack AI**: the `@surrealdb/spectron` client in TanStack Start server routes.
- **Cloudflare Workers AI**: the client inside a Worker, alongside Workers AI models.

→ [Vercel AI SDK](ai-sdks/vercel-ai-sdk.md) · [TanStack AI](ai-sdks/tanstack-ai.md) · [Cloudflare Workers AI](ai-sdks/cloudflare-workers-ai.md)

## Agent frameworks

Harness adapters expose Spectron as agent tools and add automatic per-turn memory, without changing your prompts.

| Framework | Package | Language |
| --- | --- | --- |
| LangChain / LangGraph | `@surrealdb/langchain`, `@surrealdb/langgraph` | TypeScript |
| CrewAI | `spectron-crew-ai` | Python |
| OpenAI Agents SDK | `spectron-openai-agents-sdk` | Python |
| Pydantic AI | `spectron-pydantic-ai` | Python |
| Google ADK | `spectron-google-adk` | Python |
| Strands Agents | `spectron-strands-agents` | Python |
| Mastra | `@surrealdb/mastra-ai` | TypeScript |
| Hermes Agent | `spectron-hermes` | Python |
| OpenClaw | `@surrealdb/spectron-openclaw` | TypeScript |
| Eve | `@surrealdb/spectron-eve` | TypeScript |

→ [LangChain](frameworks/langchain.md) · [CrewAI](frameworks/crewai.md) · [OpenAI Agents SDK](frameworks/openai-agents.md) · [Pydantic AI](frameworks/pydantic-ai.md) · [Google ADK](frameworks/google-adk.md) · [Strands Agents](frameworks/strands-agents.md) · [Mastra](frameworks/mastra.md) · [Hermes Agent](frameworks/hermes.md) · [OpenClaw](frameworks/openclaw.md) · [Eve](frameworks/eve.md)

Frameworks without a dedicated package integrate directly through the SDK: [AutoGen](frameworks/autogen.md) · [Agno](frameworks/agno.md) · [Camel AI](frameworks/camel-ai.md) · [LlamaIndex](frameworks/llamaindex.md)

## Voice & realtime

Give voice agents memory that persists across calls.

→ [LiveKit](voice/livekit.md) · [ElevenLabs](voice/elevenlabs.md)

## Automation

- **n8n**: the `@surrealdb/n8n-nodes-surrealdb` community node, plus Spectron memory over the REST API.
- **Zo Computer**: a Zo skill that calls the Spectron SDK for recall and storage.

→ [n8n](automation/n8n.md) · [Zo Computer](automation/zo-computer.md)

## Observability

Run Spectron for memory while an observability platform traces and evaluates the agent.

→ [Respan](observability/respan.md) · [AgentOps](observability/agentops.md)

## REST API

Direct HTTP from any language. End-user routes: `/api/v1/{context_id}/…`. Management: `/api/v1/contexts/…`.

→ [REST integration guide](surfaces/rest.md) · [Full reference](../reference/rest-api.md)

## Not shipped yet

- **Embedded in-process library**: use REST or an SDK against a deployed instance ([Embedded quickstart](https://surrealdb.com/docs/spectron/quickstarts/embedded)).
