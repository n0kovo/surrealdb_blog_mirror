---
position: 1
title: Agent setup
description: Connect your agents to SurrealDB with Agent Skills and MCP.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/agents/index.mdx"
---

# Agent setup

SurrealDB publishes Agent Skills and MCP servers, so the agent you already code with can write correct SurrealQL, run it against your databases, and manage the instances they live on.

Copy the setup prompt and paste it into your agent, or pick your agent below and follow the steps by hand. For a deeper reference on every way SurrealDB fits into AI tooling, see [AI agents](../build/ai-agents/index.md).

<AgentPrompt />

## Pick your agent

Select an agent for its setup steps. Every agent listed supports both Skills and MCP.

<AgentPicker />

Using something else? Any MCP client can reach the hosted server. Add `https://mcp.surrealdb.com` as a remote server in whatever form the client accepts, then install the skills with `npx skills add surrealdb/agent-skills`.

## What your agent gets

Setup connects two things: packaged knowledge of how SurrealDB behaves, and tools your agent can call against your databases. 

- **[Agent Skills](../build/ai-agents/agent-skills.md)** — Three official skills covering SurrealQL, vector search, and the Python SDK, so generated queries match how SurrealDB actually behaves.
- **[SurrealDB MCP Server](../build/ai-agents/mcp/index.md)** — One hosted URL connects your agent to SurrealDB Cloud: deploy and resize instances, query them, read metrics and logs, and check what it all costs.

## Next steps

- [SurrealDB MCP Server](../build/ai-agents/mcp/index.md) — the hosted server in full, including every tool it publishes
- [Embedded MCP](../build/ai-agents/mcp/embedded.md) — the MCP server inside SurrealDB, for databases you run yourself
- [Agent Skills](../build/ai-agents/agent-skills.md) — what each skill covers, and how to find community skills
- [Example usages](../build/ai-agents/mcp/examples.md) — prompts that show what an assistant can do once it is set up
