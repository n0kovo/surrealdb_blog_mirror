---
position: 0
title: Overview
description: Principles, architecture, quickstarts, and mental model for SurrealDB Agent Memory – memory and knowledge for AI agents on SurrealDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/agent-memory/index/index.mdx"
---

# SurrealDB Agent Memory documentation

SurrealDB Agent Memory is a **memory and knowledge layer for AI agents** – a **horizontally scalable application tier** in front of **SurrealDB**, which holds every durable record (graph, vector, document, relational, geospatial) with **ACID writes**, **first-class provenance and trust**, **graph-resident traces**, and **tri-temporal** belief history. It aims for memory that **associates** related ideas and keeps straight **what was said, what is true now, and what used to be true** – much like people do, but queryable and auditable in software.

Use this hub to go from principles to running code, then dive into the product sections (memory & knowledge, integrations, cookbooks, reference).

> [!NOTE]
> SurrealDB Agent Memory was developed under the project name **Spectron**, and that name is retained throughout the shipped interface: the `spectron` and `spectrond` binaries, the `SPECTRON_*` environment variables, the `spectron_*` MCP tool names, and SDK packages such as `@surrealdb/spectron`. The rule of thumb is that prose uses the product name and anything you type or configure uses `spectron`. These names will be renamed in a future release.

## Architecture

What SurrealDB Agent Memory is built to do, what it is not, and how retrieval, traces, and time work:

- [Principles and goals](https://surrealdb.com/docs/agent-memory/architecture/principles-and-goals)
- [Eight pillars and six categories](https://surrealdb.com/docs/agent-memory/architecture/eight-pillars-and-categories)
- [Coherence, retrieval, and cost tiers](https://surrealdb.com/docs/agent-memory/architecture/coherence-retrieval-and-tiers)
- [Traces and memory evolution](https://surrealdb.com/docs/agent-memory/architecture/traces-and-evolution)
- [Tri-temporal model](https://surrealdb.com/docs/agent-memory/architecture/tri-temporal-model)
- [Surface, models, and security](https://surrealdb.com/docs/agent-memory/architecture/surface-security-and-models)
- [Glossary](https://surrealdb.com/docs/agent-memory/architecture/glossary)

## Welcome and quickstarts

- **[What is SurrealDB Agent Memory?](https://surrealdb.com/docs/agent-memory/welcome/what-is-surrealdb-agent-memory)** – product positioning in one pass.
- **[Why agentic memory?](https://surrealdb.com/docs/agent-memory/welcome/why-agentic-memory)** – where naive context and pure-vector shortcuts fail.
- **[The accuracy promise](https://surrealdb.com/docs/agent-memory/welcome/accuracy-promise)** – provenance, reconciliation, and auditability.
- **[How it works](https://surrealdb.com/docs/agent-memory/welcome/how-it-works)** – end-to-end path from a turn to stored, retrievable state.

**Quickstarts**

- **[Agent Memory on SurrealDB Cloud](https://surrealdb.com/docs/agent-memory/quickstarts/surrealdb-cloud)** – Cloud API vs data plane, organisation roles, and your first context in SurrealDB Studio.
- **[Hosted quickstart](https://surrealdb.com/docs/agent-memory/quickstarts/hosted)** – SurrealDB Agent Memory Cloud, API key, first remember and recall.
- **[Embedded library](https://surrealdb.com/docs/agent-memory/quickstarts/embedded)** – HTTP, MCP, and SDK integration surfaces.

**Building with AI coding tools?** Start with **[Agent guide (AGENTS.md)](../reference/agents.md)** — copy it into Cursor rules or a project skill so your agent can learn SurrealDB Agent Memory without reading the full docs.

## Mental model

How isolation, sessions, categories, and provenance fit together:

- [Unified substrate and authority](https://surrealdb.com/docs/agent-memory/mental-model/two-layer-architecture) – authoritative versus experiential **streams** in **one** graph.
- [Contexts and scope](https://surrealdb.com/docs/agent-memory/mental-model/contexts-and-scope)
- [Sessions and turns](https://surrealdb.com/docs/agent-memory/mental-model/sessions-and-turns)
- [Memory categories](https://surrealdb.com/docs/agent-memory/mental-model/memory-categories)
- [Provenance and traceability](https://surrealdb.com/docs/agent-memory/mental-model/provenance-and-traceability)
- [Supersession, decay, and forget](https://surrealdb.com/docs/agent-memory/mental-model/memory-lifecycle) – how beliefs change, fade, and are removed

## Product sections

- **[Memory & knowledge](https://surrealdb.com/docs/agent-memory/memory-and-knowledge)** – authoritative and experiential ingest, unified retrieval, reasoning, operations, tuning.
- **[Integrations](../integrations/index.md)** – SDKs, MCP, framework adapters.
- **[Cookbooks](../cookbooks/index.md)** – end-to-end patterns.
- **[Reference](../reference/index.md)** – REST, management API, CLI, configuration, errors.
