---
position: 6
title: Surface, models, and security
description: HTTP ingest and read verbs, integrations, model hooks, and security properties.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/index/architecture/surface-security-and-models.mdx"
---

# Surface, models, and security

How to call Spectron, how models plug in, and how security properties attach to stored state.

## Ingest and read (HTTP)

Two ingest families and one read family over a **unified** graph (same reconciler, same retrieval stack):

| Verb | Purpose |
| --- | --- |
| `POST /api/v1/{ctx}/facts` | Text or triples, with `infer: "full" \| "triples" \| "preview" \| "none"`. |
| `POST /api/v1/{ctx}/facts/batch` | Bulk conversation ingest (`messages: [{ role, content, ts }, …]`). Optional **`extract`**: `whole_conversation` (default) or `per_message`. Idempotent with `Idempotency-Key`. |
| `POST /api/v1/{ctx}/documents` | Byte ingest into the multi-modal pipeline (async). |
| `POST /api/v1/{ctx}/query` | Unified read over facts and passages. Accepts optional **`labels`**, **`lens`** (filters by scope-path **involvement** within the grant — does not shrink access to exact clause matches), and **`scope_view`** (`strict`, `merged`, or `crossTeam`) to control how broadly results are folded within what the caller is already allowed to see. |
| `POST /api/v1/{ctx}/chat` | Recall + LLM synthesis; SSE when streaming. |

`POST /api/v1/{ctx}/context` and the MCP **`recall`** / **`context`** tools accept the same read parameters as `/query`.

Trace listing: `GET /api/v1/{ctx}/traces`, `GET /api/v1/{ctx}/traces/stats` (supports **`windowHours`** for rolling operational aggregates), and `GET /api/v1/{ctx}/traces/{id}`. See [Traces and memory evolution](https://surrealdb.com/docs/spectron/architecture/traces-and-evolution) and [REST API](../../reference/rest-api.md).

## Integrations

- **Generated SDKs** – Python (`surrealdb-spectron`) and TypeScript (`@surrealdb/spectron`), both produced from Spectron’s OpenAPI specification so types track the server surface.
- **MCP over HTTP** – tools wrapping the same handlers; shared Bearer auth. See [MCP server](../../integrations/mcp-server/install.md).
- **Harness adapters** – LangChain, Claude Code hook, OpenAI Agents, Vercel AI SDK, n8n – flush conversations into `/facts/batch`.

## Model configuration (five hooks)

LLMs and embedders appear in five pipeline roles – each configurable **per Context** and **per call**, with model and cost recorded on traces:

1. **Extraction** – turns and chunks → entities, attributes, relations.
2. **Embedding** – vectors for entities, attributes, chunks.
3. **Reconciliation** – optional disambiguation when signals conflict.
4. **Synthesis** – `/chat` and `/reflect` generation.
5. **Elaboration / consolidation** – background passes.

Spectron supports **OpenAI-compatible endpoints** plus **first-class Anthropic and Google clients**. **The embedding model at write time must match read time** within a Context (or schedule re-embed).

## Security and privacy

- **Encryption** – **In transit:** terminate TLS at your reverse proxy or load balancer (typical deployments run Spectron on HTTP behind the proxy). **At rest:** configure encryption on your SurrealDB storage backend and object-store bucket (for example KMS on S3 or GCS); Spectron inherits whatever those backends provide.
- **Graph-resident audit** – writes emit `decision_trace`; reads emit `retrieval_trace`; `/chat` and `/reflect` emit `response_trace`. Together these record which caller asked what, against which scope, with which key, and which records were considered or returned.
- **Operational audit events** – alongside the trace graph, Spectron emits structured audit events for reads, destructive operations (`forget`), scope changes, background jobs, and **denied** authorisation attempts so refused access is on the record even when no trace record is written.
- **Prompt-injection handling** – ingest-time scanning on uploads and batched turns; `spectron fsck --check injection` for sweeps.
- **Right to be forgotten** – `forget` soft-deletes or purges per policy; supersession history optional for audit.

## Inspectability and operational signals

Operators can derive:

- **Cost** – tokens, model, latency from `response_trace`.
- **Cache hit rate** – responses with `reused_from` set (tier 2 — fewer tokens spent).
- **Contradiction rate** – `uncertainty` records per volume of writes, by source kind.
- **Source distribution** – attributes by `source.kind` over time.
- **Supersession churn** – `decision_trace.superseded` per entity.
- **Retrieval quality** – candidate sizes and per-signal agreement from `retrieval_trace`.

See [Self-hosting observability](../../self-hosting/observability/tracing.md) for more details.
