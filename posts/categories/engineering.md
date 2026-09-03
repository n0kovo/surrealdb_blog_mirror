# Category: engineering

_46 posts_  
[← Index](../../README.md)

- **2026-08-13** · [Graph engineering is missing a graph](../2026/08/graph-engineering-is-missing-a-graph.md)  
  `featured` `engineering` `ai` — Graph engineering stops at the diagram. The harder half is the context graph underneath: whether relations, vectors and memory share one consistency boundary.
- **2026-08-11** · [Testing known time in Spectron on a 2,200-year corpus](../2026/08/hi.md)  
  `engineering` — How to use asOf in Spectron to allow gating of spoilers to ensure that spoiler-filled memory, even if already ingested, does not show up if it should not.
- **2026-08-06** · [Integrating Ultima VII with Spectron, part II: the testing](../2026/08/integrating-ultima-vii-with-spectron-part-ii-the-testing.md)  
  `engineering` — How Ultima VII was integrated with Spectron via changes to the Exult code to emit certain events and a Rust app using egui between the game and Spectron.
- **2026-08-04** · [Agent memory needs three clocks: tri-temporal belief history](../2026/08/spectron-insights-how-tri-temporal-belief-history-works.md)  
  `engineering` — Why tri-temporal belief history is needed for agent memory to properly simulate human memory and how to work with Spectron to best use it.
- **2026-07-30** · [Integrating Ultima VII with Spectron, part I: the game](../2026/07/using-ultima-vii-to-test-spectron-part-i-the-game.md)  
  `engineering` — Why Ultima VII through the Exult open-source game engine ended up being the perfect testing platform for SurrealDB's memory layer Spectron.
- **2026-06-19** · [Deterministic simulation testing and its use at SurrealDB](../2026/06/deterministic-simulation-testing-and-its-use-at-surrealdb.md)  
  `engineering` — How deterministic simulation works from easy to complex scenarios, and its ussage at SurrealDB's transactional key-value store and embedded key-value engine.
- **2026-06-11** · [Fuzz testing for SurrealDB: finding bugs before users do](../2026/06/fuzz-testing-for-surrealdb-using-randomised-input-to-find-bugs-before-users-do.md)  
  `engineering` — A good choice to complement unit and integration tests, fuzz testing lets you use semi-random data to discover obscure bugs before users do.
- **2026-05-29** · [SurrealDB 3.x by the numbers: benchmarks and comparisons](../2026/05/surrealdb-3-x-by-the-numbers.md)  
  `engineering` `company` `featured` — Fresh SurrealDB 3.x benchmarks: 141k ops\/s CRUD, scans 164× faster than 2.x, and head-to-head numbers vs. Postgres, Mongo, Neo4j, and Redis.
- **2026-04-22** · [New SurrealDB docs search with hybrid search and reranking](../2026/04/a-real-world-example-of-hybrid-fusion-search-using-the-surrealdb-docs-search.md)  
  `engineering` `tutorials` — How SurrealDB implemented documentation search using hybrid search: full-text and vector hybrid search and reranking with HNSW and BM25 indexes.
- **2026-03-19** · [Exponential cost traps in database architectures](../2026/03/exponential-cost-traps-in-database-architectures-how-surrealdb-breaks-the-cycle.md)  
  `featured` `engineering` — Polyglot database sprawl grows costs faster than traffic. Storing data once in SurrealDB cuts block-storage spend by roughly two thirds.
- **2026-03-04** · [OpenAI’s brilliant fix for a billion-dollar Postgres mistake](../2026/03/openais-postgres-architecture-a-brilliant-fix-for-a-billion-dollar-mistake.md)  
  `featured` `engineering` — OpenAI engineered an impressive PostgreSQL scaling strategy that ended up as a cautionary tale. How distributed-first architectures can avoid the same pitfalls.
- **2026-02-25** · [File support in SurrealDB 3.0: buckets and file pointers](../2026/02/file-support-in-surrealdb-3-0.md)  
  `featured` `engineering` `tutorials` — Define a bucket, then create, read, rename and delete files through SurrealQL file pointers - held in memory or on disk, alongside your records.
- **2026-02-25** · [Introducing JavaScript SDK 2.0](../2026/02/introducing-javascript-sdk-2-0.md)  
  `engineering` `releases` — A large update to the SurrealDB JavaScript SDK: 3.0 and multi-session support, automatic token refreshing, new live query API, and a new query builder pattern.
- **2026-02-18** · [Custom API Endpoints: streamlining your architecture](../2026/02/custom-api-endpoints-streamlining-your-architecture.md)  
  `featured` `engineering` `tutorials` — Declare HTTP endpoints, middleware and response bodies in SurrealQL with DEFINE API, and let clients call the database without a middleware tier.
- **2026-02-17** · [SurrealDB 3.0 benchmarks: a new foundation for performance](../2026/02/surrealdb-3-0-benchmarks-a-new-foundation-for-performance.md)  
  `featured` `engineering` — SurrealDB 3.0 introduces a new benchmarking foundation that showcases its improved, production-ready performance and the architectural advancements driving it.
- **2025-09-03** · [Power your AI workflows with the official SurrealDB x n8n node](../2025/09/power-up-your-ai-workflows-the-official-surrealdb-x-n8n-node-is-here.md)  
  `featured` `tutorials` `engineering` `ai` — The SurrealDB node for n8n is a 1st-party, production-ready integration that lets you query, create, update,, and delete SurrealDB data from any n8n workflow
- **2025-07-09** · [Make a medical chatbot using GraphRAG with SurrealDB + LangChain](../2025/07/make-a-medical-chatbot-using-graphrag-with-surrealdb-langchain.md)  
  `featured` `engineering` `ai` — Build a medical chatbot with GraphRAG, SurrealDB, and LangChain using Rust.
- **2025-07-07** · [Semantic search in Rust with SurrealDB and Mistral AI](../2025/07/semantic-search-in-rust-with-surrealdb-and-mistral-ai.md)  
  `featured` `engineering` `ai` — SurrealDB's built-in vector search capabilities make it a perfect match for semantic search using Mistral AI
- **2025-07-01** · [Announcing our official LangChain integration](../2025/07/announcing-our-official-langchain-integration.md)  
  `engineering` `featured` `ai` — We’re thrilled to announce SurrealDB's official integration with LangChain, one of the most popular frameworks for building powerful LLM-driven applications.
- **2025-06-26** · [Semantic search with SurrealDB and OpenAI](../2025/06/semantic-search-with-surrealdb-and-openai.md)  
  `featured` `engineering` `ai` — SurrealDB's built-in vector search capabilities make it a perfect match for semantic search using OpenAI
- **2025-06-23** · [Seamless data ingestion with the Airbyte connector](../2025/06/seamless-data-ingestion-with-the-airbyte-connector.md)  
  `engineering` `featured` — Today, we’re excited to announce official support for Airbyte, the leading open-source data integration platform.
- **2025-06-17** · [RAG can be Rigged: building a context-aware agent that just works](../2025/06/rag-can-be-rigged.md)  
  `featured` `engineering` `ai` — Building a smart knowledge agent with SurrealDB and Rig.rs: a context-aware support agent that just works.
- **2025-06-11** · [Seamless data ingestion with the Fivetran connector](../2025/06/seamless-data-ingestion-with-the-fivetran-connector.md)  
  `featured` `engineering` — Today, we’re excited to announce official support for Fivetran, the industry leader in automated, fully-managed data pipelines.
- **2025-06-02** · [Three ways to model data relationships in SurrealDB](../2025/06/three-ways-to-model-data-relationships-in-surrealdb.md)  
  `featured` `engineering` — A SurrealDB Stream focused on relationship modelling, from traditional record-to-record links to bidirectional references and Graph Edge metadata.
- **2025-04-02** · [Cooking up faster RAG using in-database embeddings in SurrealDB](../2025/04/cooking-up-faster-rag-using-in-database-embeddings-in-surrealdb.md)  
  `engineering` `ai` — Speed up RAG pipelines by running embedding models inside SurrealDB.Eliminate API latency with in-database vector embeddings for retrieval-augmented generation.
- **2025-03-26** · [Beyond black boxes: customisable and secure financial RAG systems](../2025/03/beyond-black-boxes--building-customisable-and-secure-rag-systems-for-financial-services.md)  
  `engineering` `ai` — A blog post that tackles the specific challenges financial services data teams face when building systems in regulated, data-sensitive environments.
- **2025-03-25** · [Revolutionising decentralised discovery with SurrealDB](../2025/03/revolutionising-decentralised-discovery-with-surrealdb-and-confidential-computing.md)  
  `engineering` `featured` — Index Network enables secure, decentralised discovery by unifying public and private data using SurrealDB and TEEs.
- **2025-02-21** · [Automating knowledge graphs with SurrealDB and Gemini](../2025/02/automating-knowledge-graphs-with-surrealdb-and-gemini.md)  
  `engineering` `ai` — How to use SurrealDB with Gemini to automate knowledge graphs to move beyond simple storage and retrieval.
- **2025-02-05** · [How we improved the Python SDK for our 1.0 stable version](../2025/02/how-we-improved-the-python-sdk-for-our-1-0-stable-version.md)  
  `engineering` — We've released our 1.0 stable version of our Python SDK including a consistent interface for WebSockets and HTTP requests.
- **2024-08-28** · [Building a RAG app with OpenAI and SurrealDB](../2024/08/building-a-retrieval-augmented-generation-app-with-openai-and-surrealdb.md)  
  `engineering` `tutorials` — We'll build an assistant that can answer questions based on Wikipedia information, using the GPT Turbo model from OpenAI
- **2024-08-20** · [It’s about time: time series in SurrealDB](../2024/08/its-about-time-time-series-in-surrealdb.md)  
  `engineering` `tutorials` — The types of time series data in SurrealDB and how to efficiently structure and query this data using SurrealQL.
- **2024-07-25** · [Moving from full-text search to vector search in SurrealDB](../2024/07/moving-from-full-text-search-to-vector-search-in-surrealdb.md)  
  `engineering` — If you know exactly what you’re searching for Full-Text Search would be the way to go but when you want your search to understand you, Vector Search might be right for you.
- **2024-07-16** · [Orchestrating real-time data insights with the right ensemble](../2024/07/real-time-data-science-orchestrating-insights-with-the-right-ensemble.md)  
  `engineering` `tutorials` — Building real-time analytics leveraging OLAP, multi-model databases and workload isolation.
- **2024-05-17** · [Introducing Surreal<Any>: Dynamic Support for any Engine in Rust](../2024/05/introducing-surrealany-dynamic-support-for-any-engine-in-rust.md)  
  `engineering` `tutorials` — Understand what is a `Surreal<Any>` engine and how you can use it in your Rust code.
- **2024-03-15** · [Understanding the CBOR data serialisation format](../2024/03/understanding-cbor.md)  
  `engineering` `tutorials` — JSON is the popular kid in school, but CBOR is the new kid who's smaller, faster, and has more tricks up its sleeve!
- **2024-03-13** · [Why SurrealDB is betting on Rust](../2024/03/why-we-are-betting-on-rust.md)  
  `engineering` `company` — The best way to predict the future is to create it. For a database company, this means choosing Rust and all the benefits it provides.
- **2024-01-23** · [VART: A persistent data structure for snapshot isolation](../2024/01/vart-a-persistent-data-structure-for-snapshot-isolation.md)  
  `engineering` — An introduction to VART (Immutable Versioned Adaptive Radix Trie), made for snapshot isolation in databases (SurrealKV).
- **2024-01-10** · [SurrealDB live queries in Rust](../2024/01/live-queries-in-rust.md)  
  `tutorials` `engineering` — Use SurrealDB's LIVE SELECT statement that allows you to listen for creations, updates and deletions to specific records you are interested in or entire tables.
- **2024-01-09** · [Introducing Nightly and Beta Rust Crates](../2024/01/introducing-nightly-and-beta-rust-crates.md)  
  `releases` `engineering` `company` — We are pleased to announce two additional Rust crates, surrealdb-nightly and surrealdb-beta. These crates are designed to complement the surrealdb crate.
- **2023-12-18** · [Full-text search in SurrealDB: Going beyond Lucene and Tantivy](../2023/12/crafting-our-full-text-search-in-surrealdb-a-journey-beyond-lucene-and-tantivy.md)  
  `engineering` — SurrealDB's own ACID-compliant full-text search engine is a unified query experience without external dependencies instead of integrating Lucene or Tantivy.
- **2023-12-12** · [What is SurrealML: A getting started guide](../2023/12/what-is-surrealml-a-getting-started-guide.md)  
  `tutorials` `engineering` — The developer community has made great strides in open-source machine-learning packages. However, there are still areas that are not fully complete.
- **2023-07-24** · [What are multi-model databases?](../2023/07/what-are-multi-model-databases.md)  
  `engineering` `tutorials` — A talk about the intriguing world of databases and where different data models co-exist, much like trains within a bustling metro station.
- **2023-06-20** · [JavaScript Library with Micha & Tobie](../2023/06/javascript-library-with-micha-tobie.md)  
  `tutorials` `engineering` — This week focuses on SurrealDB's JavaScript Library. Join Micha and Tobie for a chat on recent updates and how to use live queries and the WASM library.
- **2023-05-11** · [The life-changing magic of SurrealDB record IDs](../2023/05/the-life-changing-magic-of-surrealdb-record-ids.md)  
  `engineering` `tutorials` — At SurrealDB, we are all about doing things that spark joy for developers. One of those things that constantly surprises and delights is the humble record ID.
- **2023-05-01** · [SurrealDB Scalability: the details](../2023/05/surrealdb-scalability.md)  
  `engineering` — SurrealDB scales with separate compute and storage layers, a cost-based query planner, and distributed deployments on SurrealDB Cloud Scale and Enterprise.
- **2022-08-04** · [SurrealDB client libraries are now live!](../2022/08/client-libraries-live.md)  
  `engineering` — We’re happy to announce that initial server side documentation for Node.js, Golang and Deno, along with client side documentation for JavaScript is LIVE!
