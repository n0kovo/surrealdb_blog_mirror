---
position: 0
title: Overview
description: Multi-modal document ingest, object-store originals, hybrid retrieval, and authoritative knowledge on the unified Spectron substrate.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/knowledge/index.mdx"
---

# Knowledge

**Knowledge** workflows are how **authoritative** material enters Spectron: manuals, policies, product data, repositories, and warehouse exports. Bytes land in object storage where appropriate; **structured index state** (chunks, entities, embeddings, keyword graph, document links, traces) lives in SurrealDB under the same **ACID** write path as conversational memory.

This is the **same unified substrate** described in [Unified substrate and authority](https://surrealdb.com/docs/spectron/mental-model/two-layer-architecture): one graph and retrieval stack for documents and conversation, distinguished by **`source.kind = "document"`** (and operator `upsert`) plus higher default **`source.trust`**.

## Multi-modal pipeline (summary)

- **Ingest profiles** trade completeness for cost (`TextOnly` → `MultimodalFull`).
- **Content addressing** (for example Blake3 hashes) makes re-upload and rechunk idempotent.
- **Chunks** are first-class records with embeddings, spans into originals, and links to extracted entities.
- **Extraction** runs the **same reconciler** as conversational turns – document facts can contradict turn facts and surface **`uncertainty`** instead of silent merges.
- **Keyword graph** (RAKE + PMI edges) and **section embeddings / document links** precompute structure the [hybrid ranker](https://surrealdb.com/docs/spectron/architecture/coherence-retrieval-and-tiers) reads cheaply at query time.

See [Surface, models, and security](https://surrealdb.com/docs/spectron/architecture/surface-security-and-models) and the retrieval pages below.

## Capabilities in this section

- [Uploading documents](ingestion/uploading-documents.md) and [Bulk import](ingestion/bulk-import.md)
- [Multi-modal content](ingestion/multimodal-content.md)
- [Knowledge nodes](ingestion/knowledge-nodes.md) – structured fact ingest (see page for current API)
- [Hybrid search](retrieval/hybrid-search.md), [Keywords and BM25](retrieval/keywords-and-bm25.md), [Graph traversal](retrieval/graph-traversal.md), [Cross-layer linking](retrieval/cross-layer-linking.md)
- [Connectors](connectors/overview.md) for warehouses and collaboration tools

When you are ready to wire agents, continue to [Memory](../memory/index.md) for sessions and operations, or to [Principles and goals](https://surrealdb.com/docs/spectron/architecture/principles-and-goals) for the full conceptual spine.
