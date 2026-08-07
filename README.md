# SurrealDB Blog Mirror

_Last updated: 2026-08-07 07:08 UTC_

## Stats

- **Total posts:** 254
- **First post:** 2022-07-20
- **Latest post:** 2026-08-06
- **Years covered:** 5
- **Categories:** 8

## Browse

- [All posts (chronological)](posts/all.md)
- [Manifest (`posts.json`)](posts/posts.json)
- [Atom feed (`atom.xml`)](posts/atom.xml)
- [SurrealDB Documentation (Markdown mirror)](docs/README.md)

### By year

- [2026](posts/years/2026.md) — 59 posts
- [2025](posts/years/2025.md) — 76 posts
- [2024](posts/years/2024.md) — 44 posts
- [2023](posts/years/2023.md) — 47 posts
- [2022](posts/years/2022.md) — 28 posts

### By category

- [ai](posts/categories/ai.md) — 47 posts
- [community](posts/categories/community.md) — 35 posts
- [company](posts/categories/company.md) — 41 posts
- [engineering](posts/categories/engineering.md) — 44 posts
- [events](posts/categories/events.md) — 7 posts
- [featured](posts/categories/featured.md) — 110 posts
- [releases](posts/categories/releases.md) — 51 posts
- [tutorials](posts/categories/tutorials.md) — 99 posts

## Latest posts

- **2026-08-06** · [Integrating Ultima VII with Spectron, part II: the testing](posts/2026/08/integrating-ultima-vii-with-spectron-part-ii-the-testing.md)  
  `engineering` — How Ultima VII through Exult was integrated with Spectron via some changes to the Exult code to emit events in a certain way and a Rust app built using egui to stand in between the game and Spectron.
- **2026-08-05** · [Chat with your meeting notes: a CocoIndex knowledge graph and a text-to-SurrealQL agent](posts/2026/08/chat-with-your-meeting-notes-a-cocoindex-knowledge-graph-and-a-text-to-surrealql-agent.md)  
  `tutorials` `ai` — A folder of Markdown meeting notes becomes a self-maintaining knowledge graph in SurrealDB — and the text-to-SurrealQL prompt is not a string in the repo, it is a function call against the live database. Built with CocoIndex and Pydantic AI, fenced in by a database role rather than a regex.
- **2026-08-05** · [Announcing the Snowflake integration for SurrealDB: from data warehouse to context layer](posts/2026/08/announcing-snowflake-integration-for-surrealdb-from-data-warehouse-to-context-layer.md)  
  `releases` — SurrealDB now imports Snowflake tables directly. Move warehouse data into a context layer where facts, relationships, vectors and agent memory live in one engine.
- **2026-08-05** · [Empower your agents with the new SurrealDB MCP](posts/2026/08/surrealmcp-a-managed-mcp-server-for-ai-agents.md)  
  `featured` `releases` `tutorials` `ai` — The SurrealMCP server is now fully managed. Add one URL to Claude, Cursor, or any other AI tool, sign in with your Surreal ID, and your assistant can deploy, query, and look after your SurrealDB Cloud account alongside you.
- **2026-08-04** · [Agent memory needs three clocks: tri-temporal belief history in Spectron](posts/2026/08/spectron-insights-how-tri-temporal-belief-history-works.md)  
  `engineering` — Why tri-temporal belief history is needed for agent memory to properly simulate human memory and how to work with Spectron to best use it.
- **2026-07-30** · [Embedding models comparison: OpenAI, Google, Qwen, Nomic, Jina, BAAI](posts/2026/07/embedding-models-comparison.md)  
  `ai` — A practical guide to eight embedding models — text-embedding-3-small\/large, gemini-embedding-001, embeddinggemma-300m, qwen3-embedding, nomic-embed-text-v2-moe, jina-embeddings-v5-text-small, and BGE-M3.
- **2026-07-30** · [Integrating Ultima VII with Spectron, part I: the game](posts/2026/07/using-ultima-vii-to-test-spectron-part-i-the-game.md)  
  `engineering` — Why Ultima VII through the Exult open-source game engine ended up being the perfect testing platform for SurrealDB's memory layer Spectron.
- **2026-07-29** · [One database for the whole claim: agentic claims triage on SurrealDB](posts/2026/07/one-database-for-the-whole-claim-agentic-claims-triage-on-surrealdb.md)  
  `ai` `tutorials` — An AI agent triaging an insurance claim needs semantic, graph, and document data at once. Do it in one SurrealDB database — vector recall of similar past claims plus graph fraud-ring detection, fused in a single function. Schema, seed data, and queries included.
- **2026-07-27** · [Even a jailbroken LLM can't exceed its database permissions — here's how](posts/2026/07/even-a-jailbroken-llm-cant-exceed-its-database-permissions-heres-how.md)  
  `ai` `tutorials` — AI agents that write their own database queries can be talked into rewriting, deleting, or leaking your data with a single polite request, with no jailbreak required. No system-prompt rule can reliably stop that. SurrealDB's role-based access control can, because it lives in the data layer the LLM can't reach.
- **2026-07-23** · [One graph for the whole maison: modelling luxury retail on SurrealDB](posts/2026/07/one-graph-for-the-whole-maison-modeling-luxury-retail-on-surrealdb.md)  
  `tutorials` — How a high-end fashion house can model clients, artisans, products, and waitlists as one graph — with vector recommendations and full-text search built in.
