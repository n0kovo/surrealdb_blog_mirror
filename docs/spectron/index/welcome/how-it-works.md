---
position: 4
title: How it works in five minutes
description: From a message to structured substrate state – extraction, reconciliation, traces, and tiered reads.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/index/welcome/how-it-works.mdx"
---

# How it works in five minutes

This page sketches the lifecycle from a user message to **durable, queryable** state in SurrealDB, and how a later question is answered **cheaply first**, with expensive paths only when needed.

Think of it as teaching an agent to remember the way people do: capture what was said (**episodic**), pull out who someone is and what they know (**identity** and **knowledge**), note what matters right now (**context**), link “cat” to manuals and prior turns (**association** in one graph), and when someone says “I *used to* have a cat”, **close** the old fact instead of pretending both versions are current.

For pillars, categories, hybrid retrieval, trace feedback, and tri-temporal semantics, see the [overview hub](https://surrealdb.com/docs/spectron) and [Principles and goals](https://surrealdb.com/docs/spectron/architecture/principles-and-goals).

## End-to-end write path

```
User message (or uploaded file)
        │
        ▼
   Session / ingest
   (turn record or async document job)
        │
        ▼
┌───────────────────────────────┐
│  Extraction (pattern + LLM)   │  Typed entities, attributes, relations
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│  Reconciliation (one function)│  Dedup, scope, supersession, uncertainty
└───────────────┬───────────────┘
                ▼
┌───────────────────────────────┐
│  SurrealDB substrate          │  Graph + vectors + docs + geometry
│  + decision_trace nodes       │  Linked to considered / created records
└───────────────────────────────┘
```

[Sessions and turns](https://surrealdb.com/docs/spectron/mental-model/sessions-and-turns) remain the conversational unit of work. **Documents** enter the multi-modal [Knowledge](../../agent-memory/index.md) ingest pipeline instead of the turn path; extracted facts reconcile through the same pipeline.

## Reconciliation in one sentence

New extractions never “win” by accident: they are merged, superseded, or rejected into **`uncertainty`** using the **same** rules whether the source was a **turn** or a **document** (`source.kind` and **trust** tell the story).

## Read path: tiered resolution

Reads climb a **four-tier ladder** after a small query-understanding step. Spectron **always tries the cheapest tier first** (fewest tokens, lowest latency) and **only escalates** when the current tier cannot answer confidently:

1. **Structured lookup** when the question maps to a key in the graph.
2. **Semantic response reuse** when a prior `response_trace` still cites **current** facts (`reused_from` links the new trace).
3. **Hybrid retrieval + synthesis** – BM25, vectors, graph hops, keyword bridges, trace-derived features fused into one ranking, then LLM synthesis.
4. **Broader sweep** only when tier 3 is thin or low-confidence.

Each tier emits **`retrieval_trace`** metadata so you can see **which tier answered** and why. Full detail: [Coherence, retrieval, and cost tiers](https://surrealdb.com/docs/spectron/architecture/coherence-retrieval-and-tiers).

## What is stored on each fact

Beyond value and scope, expect **`source.*`**, **`valid_from` / `valid_until`**, **`confidence`**, and edges into **`decision_trace`** records. The **invariants** are: provenance is mandatory, supersession is non-destructive, and uncertainty is representable.

## Integration shapes

You can let Spectron drive `/chat`, or you can own the loop and call ingest + `/query` yourself via the [REST API](../../reference/rest-api.md) and [Integrations](../../integrations/index.md).

## Next steps

- [Unified substrate and authority](https://surrealdb.com/docs/spectron/mental-model/two-layer-architecture)
- [Extraction pipeline](../../agent-memory/reasoning/extraction-pipeline.md)
- [Tri-temporal model](https://surrealdb.com/docs/spectron/architecture/tri-temporal-model)
- [Traces and memory evolution](https://surrealdb.com/docs/spectron/architecture/traces-and-evolution)
