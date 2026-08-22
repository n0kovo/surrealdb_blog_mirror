---
position: 1
title: Memory & knowledge
description: "Ingest, retrieve, reason, and tune agent memory on SurrealDB Agent Memory's unified substrate."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/agent-memory/index/memory-and-knowledge.mdx"
---

# Memory & knowledge

SurrealDB Agent Memory stores **authoritative** and **experiential** material in **one** SurrealDB graph — the **Authoritative** and **Experiential** pillars from [Eight pillars and six categories](https://surrealdb.com/docs/agent-memory/architecture/eight-pillars-and-categories). This section is organised by **what you do** (ingest, retrieve, reason, tune), not by two separate products.

- **Authoritative** — manuals, policies, product data, structured uploads (`source.kind = "document"`, higher default trust).
- **Experiential** — conversation, sessions, and derived facts (`source.kind = "turn"`, reflections, elaborations, consolidations).

Start with [Unified substrate and authority](https://surrealdb.com/docs/agent-memory/mental-model/two-layer-architecture) and [Memory categories](https://surrealdb.com/docs/agent-memory/mental-model/memory-categories) (the six experiential types, including chat-extracted **knowledge** — distinct from authoritative uploads).

## Ingest

**Authoritative**

- [Uploading documents](https://surrealdb.com/docs/agent-memory/ingest/authoritative/uploading-documents), [Bulk import](https://surrealdb.com/docs/agent-memory/ingest/authoritative/bulk-import)
- [Multi-modal content](https://surrealdb.com/docs/agent-memory/ingest/authoritative/multimodal-content), [Knowledge nodes](https://surrealdb.com/docs/agent-memory/ingest/authoritative/knowledge-nodes)

**Experiential**

- [Remember](https://surrealdb.com/docs/agent-memory/ingest/experiential/remember) — `POST /facts` and `/facts/batch`
- [Sessions](https://surrealdb.com/docs/agent-memory/sessions/chat-sessions) — containers for turns ([creating](https://surrealdb.com/docs/agent-memory/sessions/creating-sessions), [adding turns](https://surrealdb.com/docs/agent-memory/sessions/adding-turns))

## Retrieve

Unified read path over facts **and** document passages:

- [Recalling memories](https://surrealdb.com/docs/agent-memory/retrieve/recall) — `/query`, `/context`, `/chat`
- [Hybrid search](https://surrealdb.com/docs/agent-memory/retrieve/hybrid-search), [Keywords and BM25](https://surrealdb.com/docs/agent-memory/retrieve/keywords-and-bm25), [Graph traversal](https://surrealdb.com/docs/agent-memory/retrieve/graph-traversal)

HTTP tables: [REST API](../reference/rest-api.md) and [Surface, models, and security](https://surrealdb.com/docs/agent-memory/architecture/surface-security-and-models).

## Reasoning

How writes are extracted, reconciled, and time-stamped — for **both** documents and turns:

- [Extraction pipeline](https://surrealdb.com/docs/agent-memory/reasoning/extraction-pipeline)
- [Reconciliation and supersession](https://surrealdb.com/docs/agent-memory/reasoning/reconciliation-and-supersession)
- [Authority when pillars meet](https://surrealdb.com/docs/agent-memory/reasoning/authority-hierarchy), [Cross-layer linking](https://surrealdb.com/docs/agent-memory/reasoning/cross-layer-linking)
- [Temporal validity](https://surrealdb.com/docs/agent-memory/reasoning/temporal-validity), [Instructions and uncertainties](https://surrealdb.com/docs/agent-memory/reasoning/instructions-and-uncertainties)

## Operations & tuning

- [Reflect](https://surrealdb.com/docs/agent-memory/operations/reflect), [Forget](https://surrealdb.com/docs/agent-memory/operations/forget), [Profiles](https://surrealdb.com/docs/agent-memory/operations/profiles)
- [Models per stage](https://surrealdb.com/docs/agent-memory/tuning/models-per-stage), [Caching and invalidation](https://surrealdb.com/docs/agent-memory/tuning/caching-and-invalidation), [Extraction vocabulary](https://surrealdb.com/docs/agent-memory/tuning/ontology-grounding)
