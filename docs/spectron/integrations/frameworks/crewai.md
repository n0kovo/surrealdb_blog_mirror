---
position: 4
title: CrewAI
description: CrewAI integration status.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/integrations/frameworks/crewai.mdx"
---

# CrewAI

> **Status:** No CrewAI adapter is available yet. This page is a placeholder.

## Recommended approach today

- Use the **Python SDK** (`surrealdb-spectron`) or REST from crew tools / task callbacks to **`/facts/batch`** and **`/query`**.
- Scope each crew or user with path strings (`org=acme`, `agent=researcher`, …).

See [Storing memories](../../memory/operations/remember.md) and [Recalling memories](../../memory/operations/recall.md).

A future harness adapter would mirror crew message history into batch ingest with stable idempotency keys, similar to `spectron-langchain`.
