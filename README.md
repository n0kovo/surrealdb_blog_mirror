# SurrealDB Blog Mirror

_Last updated: 2026-06-17 07:53 UTC_

## Stats

- **Total posts:** 233
- **First post:** 2022-07-20
- **Latest post:** 2026-06-16
- **Years covered:** 5
- **Categories:** 8

## Browse

- [All posts (chronological)](posts/all.md)
- [Manifest (`posts.json`)](posts/posts.json)
- [Atom feed (`atom.xml`)](posts/atom.xml)
- [SurrealDB Documentation (Markdown mirror)](docs/README.md)

### By year

- [2026](posts/years/2026.md) — 38 posts
- [2025](posts/years/2025.md) — 76 posts
- [2024](posts/years/2024.md) — 44 posts
- [2023](posts/years/2023.md) — 47 posts
- [2022](posts/years/2022.md) — 28 posts

### By category

- [ai](posts/categories/ai.md) — 37 posts
- [community](posts/categories/community.md) — 34 posts
- [company](posts/categories/company.md) — 41 posts
- [engineering](posts/categories/engineering.md) — 40 posts
- [events](posts/categories/events.md) — 7 posts
- [featured](posts/categories/featured.md) — 106 posts
- [releases](posts/categories/releases.md) — 47 posts
- [tutorials](posts/categories/tutorials.md) — 87 posts

## Latest posts

- **2026-06-16** · [What's new in Surrealist 3.9](posts/2026/06/whats-new-in-surrealist-3-9.md)  
  `featured` `releases` — Surrealist 3.9 introduces a complete design overhaul, a new datasets browser and data manager, and loads of other enhancements.
- **2026-06-12** · [Organizations and Teams for your SurrealDB App](posts/2026/06/organizations-and-teams-for-your-surrealdb-app.md)  
  `tutorials` — Bootstrapping multi-tenant orgs, roles, permissions, and the functions that enforce them - straight from SurrealKit templates.
- **2026-06-11** · [Fuzz testing for SurrealDB: using randomised input to find bugs before users do](posts/2026/06/fuzz-testing-for-surrealdb-using-randomised-input-to-find-bugs-before-users-do.md)  
  `engineering` — A good choice to complement unit and integration tests, fuzz testing lets you use semi-random data to discover obscure bugs before users do.
- **2026-06-09** · [SurrealDB is now available on the Nebius AI Cloud Marketplace](posts/2026/06/surrealdb-is-now-available-on-nebius-ai-cloud-marketplace.md)  
  `releases` — SurrealDB is now available on the Nebius AI Cloud Marketplace.
- **2026-06-05** · [Context layers, semantic layers, and knowledge graphs: the modern data architecture for AI](posts/2026/06/context-layers-semantic-layers-and-knowledge-graphs-the-modern-data-architecture-for-ai.md)  
  `company` — Three concepts AI teams constantly confuse: a context layer assembles the right data into an LLM prompt at query time, a semantic layer maps raw data to business meaning, and a knowledge graph stores entities and their relationships. Most teams build all three by stitching together separate graph, vector, and relational systems - creating sync problems, higher latency, and rising costs. SurrealDB's multi-model architecture handles all three natively, letting a single SurrealQL query run vector search, graph traversal, and document retrieval in one round trip
- **2026-05-29** · [SurrealDB 3.x by the numbers](posts/2026/05/surrealdb-3-x-by-the-numbers.md)  
  `engineering` `company` `featured` — Fresh SurrealDB 3.x benchmarks: 141k ops\/s CRUD, scans 164× faster than 2.x, and head-to-head numbers vs. Postgres, Mongo, Neo4j, and Redis.
- **2026-05-27** · [SurrealDB 3.1: stability, DiskANN, and a new release process](posts/2026/05/surrealdb-3-1-stability-diskann-and-a-new-release-process.md)  
  `releases` `featured` — SurrealDB 3.1 is here. The first minor release in the 3.x series brings DiskANN, a comprehensive stability and security pass, and a refreshed release process.
- **2026-05-22** · [Using SurrealDB to understand how Buffalo buffalo buffalo Buffalo buffalo](posts/2026/05/using-surrealdb-to-understand-how-buffalo-buffalo-buffalo-buffalo-buffalo.md)  
  `tutorials` — Using SurrealDB and Surrealist's graph visualisation to not just understand but also see how Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo works.
- **2026-05-19** · [Agentic retrieval for structured data with text-to-surql](posts/2026/05/agentic-retrieval-for-structured-data-with-text-to-surql.md)  
  `ai` `tutorials` — RAG pipelines usually focus on unstructured content (chunks + vectors\/BM25), but structured data introduces a different retrieval problem: you need to pull exact rows and aggregates from tables, not just “similar passages.” This article explains an agentic pattern for structured retrieval using text-to-SurrealQL: give an LLM agent a single database-aware tool that converts natural-language questions into valid SurrealQL, executes the query in SurrealDB, and returns deterministic, auditable results.
- **2026-05-12** · [What chunking strategies exist and how to choose one?](posts/2026/05/what-chunk-strategies-exist-and-how-to-choose-one.md)  
  `ai` — If you've decided to chunk your documents for a RAG pipeline or semantic search system, the next question hits almost immediately: which chunking strategy should I use?
