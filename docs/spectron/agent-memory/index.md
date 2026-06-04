---
position: 0
title: Overview
description: "Ingest, retrieve, reason, and tune agent memory on Spectron's unified SurrealDB substrate."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/agent-memory/index.mdx"
---

# Memory & knowledge

Spectron stores **authoritative** and **experiential** material in **one** SurrealDB graph — the **Authoritative** and **Experiential** pillars from [Eight pillars and six categories](https://surrealdb.com/docs/spectron/architecture/eight-pillars-and-categories). This section is organised by **what you do** (ingest, retrieve, reason, tune), not by two separate products.

- **Authoritative** — manuals, policies, product data, structured uploads (`source.kind = "document"`, higher default trust).
- **Experiential** — conversation, sessions, and derived facts (`source.kind = "turn"`, reflections, elaborations, consolidations).

Start with [Unified substrate and authority](https://surrealdb.com/docs/spectron/mental-model/two-layer-architecture) and [Memory categories](https://surrealdb.com/docs/spectron/mental-model/memory-categories) (the six experiential types, including chat-extracted **knowledge** — distinct from authoritative uploads).

## Ingest

**Authoritative**

- [Uploading documents](ingest/authoritative/uploading-documents.md), [Bulk import](ingest/authoritative/bulk-import.md)
- [Multi-modal content](ingest/authoritative/multimodal-content.md), [Knowledge nodes](ingest/authoritative/knowledge-nodes.md)

**Experiential**

- [Remember](ingest/experiential/remember.md) — `POST /facts` and `/facts/batch`
- [Sessions](sessions/chat-sessions.md) — containers for turns ([creating](sessions/creating-sessions.md), [adding turns](sessions/adding-turns.md))

## Retrieve

Unified read path over facts **and** document passages:

- [Recalling memories](retrieve/recall.md) — `/query`, `/context`, `/chat`
- [Hybrid search](retrieve/hybrid-search.md), [Keywords and BM25](retrieve/keywords-and-bm25.md), [Graph traversal](retrieve/graph-traversal.md)

HTTP tables: [REST API](../reference/rest-api.md) and [Surface, models, and security](https://surrealdb.com/docs/spectron/architecture/surface-security-and-models).

## Reasoning

How writes are extracted, reconciled, and time-stamped — for **both** documents and turns:

- [Extraction pipeline](reasoning/extraction-pipeline.md)
- [Reconciliation and supersession](reasoning/reconciliation-and-supersession.md)
- [Authority when pillars meet](reasoning/authority-hierarchy.md), [Cross-layer linking](reasoning/cross-layer-linking.md)
- [Temporal validity](reasoning/temporal-validity.md), [Instructions and uncertainties](reasoning/instructions-and-uncertainties.md)

## Operations & tuning

- [Reflect](operations/reflect.md), [Forget](operations/forget.md), [Profiles](operations/profiles.md)
- [Models per stage](tuning/models-per-stage.md), [Caching and invalidation](tuning/caching-and-invalidation.md), [Ontology grounding](tuning/ontology-grounding.md)
