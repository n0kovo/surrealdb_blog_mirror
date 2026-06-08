---
position: 0
title: Overview
description: Principles, architecture, quickstarts, and mental model for Spectron – memory and knowledge for AI agents on SurrealDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/index/index.mdx"
---

# Spectron documentation

Spectron is a **memory and knowledge layer for AI agents** – a **horizontally scalable application tier** in front of **SurrealDB**, which holds every durable record (graph, vector, document, relational, geospatial) with **ACID writes**, **first-class provenance and trust**, **graph-resident traces**, and **tri-temporal** belief history. Spectron aims for memory that **associates** related ideas and keeps straight **what was said, what is true now, and what used to be true** – much like people do, but queryable and auditable in software.

Use this hub to go from principles to running code, then dive into operational sections (memory & knowledge, self-hosting, integrations, reference).

## Architecture

What Spectron is built to do, what it is not, and how retrieval, traces, and time work:

- [Principles and goals](https://surrealdb.com/docs/spectron/architecture/principles-and-goals)
- [Eight pillars and six categories](https://surrealdb.com/docs/spectron/architecture/eight-pillars-and-categories)
- [Coherence, retrieval, and cost tiers](https://surrealdb.com/docs/spectron/architecture/coherence-retrieval-and-tiers)
- [Traces and memory evolution](https://surrealdb.com/docs/spectron/architecture/traces-and-evolution)
- [Tri-temporal model](https://surrealdb.com/docs/spectron/architecture/tri-temporal-model)
- [Surface, models, and security](https://surrealdb.com/docs/spectron/architecture/surface-security-and-models)
- [Glossary](https://surrealdb.com/docs/spectron/architecture/glossary)

## Welcome and quickstarts

- **[What is Spectron?](https://surrealdb.com/docs/spectron/welcome/what-is-spectron)** – product positioning in one pass.
- **[Why agentic memory?](https://surrealdb.com/docs/spectron/welcome/why-agentic-memory)** – where naive context and pure-vector shortcuts fail.
- **[The accuracy promise](https://surrealdb.com/docs/spectron/accuracy-promise)** – provenance, reconciliation, and auditability.
- **[How it works](https://surrealdb.com/docs/spectron/welcome/how-it-works)** – end-to-end path from a turn to stored, retrievable state.

**Quickstarts**

- **[Surrealist dashboard quickstart](https://surrealdb.com/docs/spectron/quickstarts/surrealist-dashboard)** – create a Context in Surrealist, Playground, Memories, Knowledge, API keys.
- **[Hosted quickstart](https://surrealdb.com/docs/spectron/quickstarts/hosted)** – Spectron Cloud, API key, first remember and recall.
- **[Self-hosted quickstart](https://surrealdb.com/docs/spectron/quickstarts/self-hosted)** – Docker Compose and your first remember/recall calls.
- **[Embedded library](https://surrealdb.com/docs/spectron/quickstarts/embedded)** – HTTP, MCP, and SDK integration surfaces.

**Building with AI coding tools?** Start with **[Agent guide (AGENTS.md)](../reference/agents.md)** — copy it into Cursor rules or a project skill so your agent can learn Spectron without reading the full docs.

## Mental model

How isolation, sessions, categories, and provenance fit together:

- [Unified substrate and authority](https://surrealdb.com/docs/spectron/mental-model/two-layer-architecture) – authoritative versus experiential **streams** in **one** graph.
- [Contexts and scope](https://surrealdb.com/docs/spectron/mental-model/contexts-and-scope)
- [Sessions and turns](https://surrealdb.com/docs/spectron/mental-model/sessions-and-turns)
- [Memory categories](https://surrealdb.com/docs/spectron/mental-model/memory-categories)
- [Provenance and traceability](https://surrealdb.com/docs/spectron/mental-model/provenance-and-traceability)
- [Supersession, decay, and forget](https://surrealdb.com/docs/spectron/mental-model/memory-lifecycle) – how beliefs change, fade, and are removed

## Product sections

- **[Memory & knowledge](../agent-memory/index.md)** – authoritative and experiential ingest, unified retrieval, reasoning, operations, tuning.
- **[Integrations](../integrations/index.md)** – SDKs, MCP, framework adapters.
- **[Self-hosting](../self-hosting/index.md)** – deployment, security, operations, observability.
- **[Cookbooks](../cookbooks/index.md)** – end-to-end patterns.
- **[Reference](../reference/index.md)** – REST, management API, CLI, configuration, errors.
