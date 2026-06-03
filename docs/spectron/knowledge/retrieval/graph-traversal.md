---
position: 2
title: Graph traversal
description: Structural edges in the knowledge layer and how retrieval uses them.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/knowledge/retrieval/graph-traversal.mdx"
---

# Graph traversal

Spectron builds a **structural graph** during document ingest and fact extraction: documents, chunks, keywords, and entities linked by typed edges. You do not need a separate graph database – these edges live in SurrealDB alongside vectors and text.

Most retrieval uses this graph **implicitly** through **`hybrid_graph`** mode on **`POST /api/v1/{context_id}/documents/query`**, which reranks vector/BM25 hits using graph-density signals. You can also inspect or query edges directly with SurrealQL on self-hosted deployments.

> Dedicated **`/knowledge/traverse`** REST endpoints are **not shipped yet**. This page documents the **edge types that exist today** and how retrieval consumes them.

## Document-layer edges (ingest pipeline)

These relations are created automatically when documents are processed:

| Edge | From | To | Role |
| --- | --- | --- | --- |
| `knowledge_has_keyword` | Document | Keyword | Links content to RAKE keyphrases |
| `keyword_cooccurs_with` | Keyword | Keyword | PMI-weighted co-occurrence within the corpus |
| `knowledge_links_to` | Document | Document | Outbound hyperlinks or citations between files |

Optional **`graph_edges`** on **`/documents/query`** select which of these signals contribute during **`hybrid_graph`** reranking (`knowledge_has_keyword`, `section_match`, `document_link`, `document_summary`, `keyword_cooccurrence`). See [Hybrid search](hybrid-search.md).

## Entity graph (memory + extraction)

Conversational and document extraction both write **`entity`**, **`attribute`**, and **`relates_to`** records in the unified graph. Add or update relations explicitly with **`POST /api/v1/{context_id}/facts`** and `infer: "triples"` when you already know the structure.

Unified recall via **`POST /api/v1/{context_id}/query`** can traverse one- or two-hop entity relationships as part of tier-3 hybrid retrieval – you do not call a separate traverse API.

## Example: hybrid graph query

```http
POST /api/v1/{context_id}/documents/query
Content-Type: application/json

{
  "query": "return policy restocking fee",
  "mode": "hybrid_graph",
  "limit": 10,
  "graph_edges": ["knowledge_has_keyword", "document_link"]
}
```

## Example: SurrealQL inspection (self-hosted)

```surql
-- Keywords attached to a document
SELECT ->knowledge_has_keyword->keyword AS keywords
FROM document:01hx9…;

-- Documents linked from a handbook
SELECT ->knowledge_links_to->document AS related
FROM document:01hx9…;
```

## Related reading

- [Hybrid search](hybrid-search.md)
- [Keywords and BM25](keywords-and-bm25.md)
- [Cross-layer linking](cross-layer-linking.md)
- [Data model and schema](../../reference/data-model-and-schema.md)
