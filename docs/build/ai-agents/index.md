---
position: 1
title: AI agents
description: The ways SurrealDB fits into AI tooling — MCP servers, Agent Skills, and framework integrations — and what the database gives an agent.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/ai-agents/index.mdx"
---

# AI agents

SurrealDB connects to AI tooling in three places: the assistant you write code with, the framework your application is built on, and the database your agent stores its knowledge in. This page covers each one and where to go next.

## Ways to integrate

**[MCP](mcp/index.md)** — Give an AI tool a set of tools to call. The hosted [SurrealDB MCP Server](mcp/index.md) connects Claude, Cursor, and other clients to your SurrealDB Cloud account with one URL, so an assistant can deploy instances, query their data, and read logs while you work. A database you run yourself publishes the same data tools through [Embedded MCP](mcp/embedded.md). *Since v3.1.0*

**[Agent Skills](agent-skills.md)** — Install packaged knowledge into a coding agent. The official skills cover SurrealQL, vector search, and the Python SDK, so generated queries match how SurrealDB actually behaves instead of guessing at an API.

**[AI frameworks](ai-frameworks.md)** — Use SurrealDB from the agent library you already have. LangChain, LlamaIndex, CrewAI, PydanticAI, Agno, and others connect through maintained integrations for vector stores, memory, and retrieval.

**[Spectron](https://surrealdb.com/docs/spectron)** — A memory and knowledge layer for agents, running in front of SurrealDB. Use it when an agent needs to remember across sessions, and to keep straight what was said, what is true now, and what used to be true, without designing that model yourself.

## What the database gives an agent

An agent needs somewhere to keep state, a way to query it that fits the question being asked, and retrieval fast enough to answer in the loop. SurrealDB does all three in one engine, so you are not keeping a document store, a graph database, and a vector index in sync.

**Memory** — Store conversation context, artefacts, and entity records as documents, and model the relationships between users, tasks, tools, and outcomes as a graph. Agents can then traverse those connections rather than re-reading everything. Partition memory per tenant or per session while keeping one query model.

**Retrieval** — Combine structured filters with [vector indexes and similarity search](../../learn/data-models/vector-search/vector-indexes.md) so a lookup can be semantic, exact, or both. That covers RAG and hybrid retrieval without a second system.

**Knowledge graphs** — Follow links between concepts, permissions, and resources inside the database, so a question can reach supporting facts in a few hops instead of several round-trips through application code.

**Tools the agent can call** — Express logic in SurrealQL, including [database functions](../../reference/query-language/functions/database-functions/index.md) for reusable server-side behaviour and [HTTP functions](../../reference/query-language/functions/database-functions/http.md) for reaching external APIs from the query layer.

Because schemas and indexes can change as your workflows change, the same deployment serves low-latency reads for live agents and batch jobs for backfills or evaluation.

## Next steps

- [SurrealDB MCP Server](mcp/index.md) — connect your AI tool to SurrealDB Cloud
- [Agent Skills](agent-skills.md) — install SurrealQL and SDK knowledge into a coding agent
- [AI frameworks overview](../integrations/ai-frameworks/overview.md) — compare the framework integrations
- [Build an AI agent](../../explore/tutorials/tutorials/build-an-ai-agent.md) — a worked example, end to end
