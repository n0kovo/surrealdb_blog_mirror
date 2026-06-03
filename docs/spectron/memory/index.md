---
position: 1
title: Overview
description: Sessions, episodic memory, operations, and tuning – experiential memory on the unified Spectron substrate.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/memory/index.mdx"
---

# Memory

**Memory** workflows cover the **experiential** side of Spectron: sessions, turns, `remember` / `recall` / `reflect` / `forget`, profiles, and tuning. Extracted records still live in the **same** SurrealDB graph as document knowledge – distinguished by provenance and **trust** (`source.kind = "turn"`, reflections, elaborations, consolidations, …) rather than by a separate database.

The experiential side is where “I have a cat”, “I saw a cat last night”, and “I used to have a cat” land as **different kinds** of belief – not one undated note. Start with the six **experiential categories** (including **episodic** raw turns) in [Memory categories](https://surrealdb.com/docs/spectron/mental-model/memory-categories), then read [Traces and memory evolution](https://surrealdb.com/docs/spectron/architecture/traces-and-evolution) to see how `response_trace` and `retrieval_trace` close the loop on ranking and reuse.

## What this section contains

- **[Sessions](sessions/chat-sessions.md)** – containers for turns; the episodic substrate every extraction cites ([creating sessions](sessions/creating-sessions.md), [adding turns](sessions/adding-turns.md))
- **Operations** – [Remember](operations/remember.md), [Recall](operations/recall.md), [Reflect](operations/reflect.md), [Forget](operations/forget.md), [Profiles](operations/profiles.md)
- **Reasoning model** – extraction, reconciliation, authority, temporality ([extraction pipeline](reasoning-model/extraction-pipeline.md))
- **[Tuning](tuning/models-per-stage.md)** – models per stage, caching, ontology

HTTP verbs (`/facts`, `/facts/batch`, `/query`, `/chat`, `/reflect`, traces) are documented under [Surface, models, and security](https://surrealdb.com/docs/spectron/architecture/surface-security-and-models) and the [REST API](../reference/rest-api.md).

Authoritative ingest is covered in [Knowledge](../knowledge/index.md).
