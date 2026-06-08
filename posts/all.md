# All Posts

_229 posts_  
[← Index](../README.md)

- **2026-06-05** · [Context layers, semantic layers, and knowledge graphs: the modern data architecture for AI](2026/06/context-layers-semantic-layers-and-knowledge-graphs-the-modern-data-architecture-for-ai.md)  
  `company` — Three concepts AI teams constantly confuse: a context layer assembles the right data into an LLM prompt at query time, a semantic layer maps raw data to business meaning, and a knowledge graph stores entities and their relationships. Most teams build all three by stitching together separate graph, vector, and relational systems - creating sync problems, higher latency, and rising costs. SurrealDB's multi-model architecture handles all three natively, letting a single SurrealQL query run vector search, graph traversal, and document retrieval in one round trip
- **2026-05-29** · [SurrealDB 3.x by the numbers](2026/05/surrealdb-3-x-by-the-numbers.md)  
  `engineering` `company` `featured` — Fresh SurrealDB 3.x benchmarks: 141k ops\/s CRUD, scans 164× faster than 2.x, and head-to-head numbers vs. Postgres, Mongo, Neo4j, and Redis.
- **2026-05-27** · [SurrealDB 3.1: stability, DiskANN, and a new release process](2026/05/surrealdb-3-1-stability-diskann-and-a-new-release-process.md)  
  `releases` `featured` — SurrealDB 3.1 is here. The first minor release in the 3.x series brings DiskANN, a comprehensive stability and security pass, and a refreshed release process.
- **2026-05-22** · [Using SurrealDB to understand how Buffalo buffalo buffalo Buffalo buffalo](2026/05/using-surrealdb-to-understand-how-buffalo-buffalo-buffalo-buffalo-buffalo.md)  
  `tutorials` — Using SurrealDB and Surrealist's graph visualisation to not just understand but also see how Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo works.
- **2026-05-19** · [Agentic retrieval for structured data with text-to-surql](2026/05/agentic-retrieval-for-structured-data-with-text-to-surql.md)  
  `ai` `tutorials` — RAG pipelines usually focus on unstructured content (chunks + vectors\/BM25), but structured data introduces a different retrieval problem: you need to pull exact rows and aggregates from tables, not just “similar passages.” This article explains an agentic pattern for structured retrieval using text-to-SurrealQL: give an LLM agent a single database-aware tool that converts natural-language questions into valid SurrealQL, executes the query in SurrealDB, and returns deterministic, auditable results.
- **2026-05-12** · [What chunking strategies exist and how to choose one?](2026/05/what-chunk-strategies-exist-and-how-to-choose-one.md)  
  `ai` — If you've decided to chunk your documents for a RAG pipeline or semantic search system, the next question hits almost immediately: which chunking strategy should I use?
- **2026-05-08** · [What is the recommended chunk size?](2026/05/what-is-the-recommended-chunk-size.md)  
  `ai` — If you're building a RAG (Retrieval-Augmented Generation) pipeline, a semantic search system, or any AI application that reads from a vector store, one question comes up almost immediately: what chunk size should I use?
- **2026-05-07** · [Schema migrations in SurrealDB: A local dev workflow](2026/05/schema-migrations-in-surrealdb-a-local-dev-workflow.md)  
  `tutorials` `featured` `releases` — Managing schema changes in SurrealDB shouldn't slow down your local development. This post walks through a practical migration workflow that keeps your database in sync as your project evolves.
- **2026-04-30** · [Kreuzberg & SurrealDB: from unstructured documents to hybrid retrieval](2026/04/kreuzberg-surrealdb-from-unstructured-documents-to-hybrid-retrieval.md)  
  `releases` — SurrealDB now integrates with Kreuzberg to ingest, chunk, and search unstructured documents across 88+ formats - with built-in keyword, semantic, and hybrid search with reranking.
- **2026-04-30** · [Hybrid search inside SurrealDB](2026/04/hybrid-search-inside-surrealdb.md)  
  `ai` — How I fused vector and keyword retrieval in a single query
- **2026-04-27** · [Building compounding memory with knowledge graphs and agentic RAG](2026/04/building-compounding-memory-with-knowledge-graphs-and-agentic-rag.md)  
  `community` `ai` — Synapse, a memory-first reflection agent, helps users track therapy journal patterns. It structures insights into a knowledge graph, revealing patterns and answering questions based on context.
- **2026-04-22** · [New SurrealDB docs search using hybrid search and HNSW\/BM25 reranking](2026/04/a-real-world-example-of-hybrid-fusion-search-using-the-surrealdb-docs-search.md)  
  `engineering` `tutorials` — How SurrealDB has implemented documentation search using hybrid search (full-text and vector hybrid search and reranking with HNSW and BM25 indexes), plus a simplified example to show the same pattern in just a few queries.
- **2026-04-21** · [What's new in Surrealist 3.8](2026/04/whats-new-in-surrealist-3-8.md)  
  `featured` `releases` — Surrealist 3.8 introduces a fully redesigned organisation view, improved query formatting, and loads of other enhancements.
- **2026-04-17** · [Graph RAG does not need a graph database. It needs a database that does everything.](2026/04/graph-rag-does-not-need-a-graph-database-it-needs-a-database-that-does-everything.md)  
  `featured` `ai` — Graph RAG is the right idea. Using relationships between entities to scope and improve retrieval produces better results than vector similarity alone. What matters in production is whether graph traversal, vector search, full-text search, and structured filters compose in a single atomic statement.
- **2026-03-28** · [How to get near-perfect, deterministic accuracy from your AI agents](2026/03/how-to-get-near-perfect-deterministic-accuracy-from-your-ai-agents.md)  
  `featured` `ai` — Agent accuracy problems are almost always retrieval problems, not model problems. Scope-first retrieval and reasoning and retrieval graph feedback loops close the gap to 99%+.
- **2026-03-25** · [SurrealMX: In-memory storage with time travel and persistent storage](2026/03/surrealmx-in-memory-storage-with-time-travel-and-persistent-storage.md)  
  `featured` `tutorials` — SurrealMX lets you use in-memory storage along with optional time travel versioned queries and two types of persistent storage with a large number of configurations to balance performance with durability.
- **2026-03-19** · [Exponential cost traps in database architectures: how SurrealDB breaks the cycle](2026/03/exponential-cost-traps-in-database-architectures-how-surrealdb-breaks-the-cycle.md)  
  `featured` `engineering` — SurrealDB offers a consolidated solution to store data once and querying it across models to reduce overall costs, particularly in storage-heavy environments where cloud block storage is in use.
- **2026-03-12** · [Where SurrealDB fits in your stack](2026/03/where-surrealdb-fits-in-your-stack.md)  
  `featured` — By consolidating databases into one platform, SurrealDB enables applications with multi-model capabilities, blending relational queries, graph traversals, vector search, time-series and geospatial analysis without the overhead of disparate tools.
- **2026-03-11** · [SurrealDB is now available on AWS Marketplace](2026/03/surrealdb-is-now-available-on-aws-marketplace.md)  
  `featured` `company` — You can now deploy SurrealDB directly into your AWS environment with streamlined procurement, simplified billing, and faster time to production - all through your existing AWS environment.
- **2026-03-04** · [OpenAI’s Postgres Architecture: A Brilliant Fix for a Billion-Dollar Mistake](2026/03/openais-postgres-architecture-a-brilliant-fix-for-a-billion-dollar-mistake.md)  
  `featured` `engineering` — OpenAI engineered an impressive PostgreSQL scaling strategy, but this article argues it is a cautionary tale and explains why distributed-first architectures can avoid many of the same pitfalls.
- **2026-03-02** · [How to use Surrealism to build your own custom SurrealDB extensions](2026/03/how-to-use-surrealism-to-build-your-own-custom-surrealdb-extensions.md)  
  `featured` `tutorials` — Surrealism lets you build your own custom plugins, WASM functions that you can build and compile to their own binaries that can be called directly from the database
- **2026-02-25** · [File support in SurrealDB 3.0](2026/02/file-support-in-surrealdb-3-0.md)  
  `featured` `engineering` `tutorials` — SurrealDB 3.0 includes experimental file support that allows you to create, update, and delete files regardless of whether the database itself saves its data persistently or not.
- **2026-02-25** · [Introducing JavaScript SDK 2.0](2026/02/introducing-javascript-sdk-2-0.md)  
  `engineering` `releases` — The most significant update to the JavaScript SDK to date: SurrealDB 3.0 support, multi-session support, automatic token refreshing, a redesigned live query API, and a new query builder pattern.
- **2026-02-18** · [Custom API Endpoints: streamlining your architecture](2026/02/custom-api-endpoints-streamlining-your-architecture.md)  
  `featured` `engineering` `tutorials` — Custom API endpoints allow developers to define database behaviours, set up middleware, and create custom API endpoints directly within the familiar SurrealQL query language.
- **2026-02-18** · [SurrealDB Raises $23M Series A extension to power the AI-native database era](2026/02/surrealdb-raises-23m-series-a-extension-to-power-the-ai-native-database-era.md)  
  `featured` `company` — SurrealDB Raises $23M Series A extension to power the AI-native database era
- **2026-02-17** · [Introducing SurrealDB 3.0 - the future of AI agent memory](2026/02/introducing-surrealdb-3-0--the-future-of-ai-agent-memory.md)  
  `featured` — Introducing SurrealDB 3.0 - the future of AI agent memory
- **2026-02-17** · [SurrealDB 3.0 benchmarks: a new foundation for performance](2026/02/surrealdb-3-0-benchmarks-a-new-foundation-for-performance.md)  
  `featured` `engineering` — SurrealDB 3.0 introduces a new benchmarking foundation that showcases its improved, production-ready performance and the architectural advancements driving it.
- **2026-02-17** · [Introducing Surrealism](2026/02/introducing-surrealism.md)  
  `featured` — Introducing Surrealism
- **2026-02-16** · [SurrealDB vs. Neo4j](2026/02/surrealdb-vs-neo4j.md)  
  `featured` — SurrealDB is built for live, large-scale application data. Neo4j is built for traversal-heavy graph workloads at modest scale.
- **2026-02-16** · [SurrealDB vs. Postgres](2026/02/surrealdb-vs-postgres.md)  
  `featured` — SurrealDB natively unifies relational, graph, vector, document, and temporal data in a single engine, no extensions or workarounds.
- **2026-02-16** · [SurrealDB vs. MongoDB](2026/02/surrealdb-vs-mongodb.md)  
  `featured` — SurrealDB is a unified, transactional, multi-model database. MongoDB is a document-oriented database with multiple specialised subsystems.
- **2026-02-05** · [How to build a knowledge graph for AI](2026/02/how-to-build-a-knowledge-graph-for-ai.md)  
  `featured` `tutorials` `ai` — What is a knowledge graph and how can it be used to enhance AI agents?
- **2026-01-29** · [Knowledge Graph RAG: two query patterns for smarter AI agents](2026/01/knowledge-graph-rag-two-query-patterns-for-smarter-ai-agents.md)  
  `featured` `tutorials` `ai` — A post that walks through two powerful SurrealQL query patterns that demonstrate how to retrieve context from a knowledge graph to feed AI agents.
- **2026-01-27** · [A look at SurrealQL and how it differs from PostgreSQL](2026/01/a-look-at-surrealql-and-how-it-differs-from-postgresql.md)  
  `featured` `tutorials` — In this article, we will explore the similarities and differences between PostgreSQL and SurrealQL. We will also see how SurrealQL can overcome some of the limitations that relational databases have.
- **2025-12-18** · [Learning through building: SurrealDB University's newest tutorial](2025/12/learning-through-building-surrealdb-universitys-newest-tutorial.md)  
  `featured` `tutorials` — Now you can learn SurrealDB by building your own database that takes advantage of its multi-model capabilities to store and query over 100 of the world's most popular movies.
- **2025-12-17** · [Agents with memory: how Agno and SurrealDB enable reliable AI systems](2025/12/agents-with-memory-how-agno-and-surrealdb-enable-reliable-ai-systems.md)  
  `featured` `ai` — Highlights from our Agno x SurrealDB livestream on building reliable, context-rich agents with a strong memory layer.
- **2025-12-17** · [PolyAI on building context-aware voice agents: latency, knowledge bases, and what actually ships](2025/12/polyai-on-building-context-aware-voice-agents-latency-knowledge-bases-and-what-actually-ships.md)  
  `featured` `ai` `events` — Key takeaways from SurrealDB Stream #34 with PolyAI CTO & co-founder Shawn Wen on the hard parts of shipping context-aware voice agents: latency budgets, knowledge governance, and operational trust.
- **2025-12-11** · [SurrealDB joins the NVIDIA Inception Program](2025/12/surrealdb-joins-the-nvidia-inception-program.md)  
  `featured` `company` — SurrealDB joins the NVIDIA Inception Program, gaining access to GPU acceleration, CUDA integrations, and advanced vector search capabilities for AI-driven applications.
- **2025-11-26** · [Why companies are adopting SurrealDB](2025/11/why-companies-are-adopting-surrealdb.md)  
  `featured` `company` — SurrealDB unifies documents, graphs, vectors, and real-time logic in one engine, cutting infrastructure complexity and empowering faster, more flexible development for modern AI-driven applications.
- **2025-10-29** · [Exploring the new SurrealDB integration with Agno](2025/10/exploring-the-new-surrealdb-integration-with-agno.md)  
  `featured` `tutorials` `ai` — SurrealDB's built-in capabilities comprising graph queries, geolocational data and recursive queries make it the perfect fit to identify malevolent entities involved in organised influence campaigns.
- **2025-10-10** · [Using SurrealDB to Expose Organised Influence Campaigns](2025/10/using-surrealdb-to-expose-organised-influence-campaigns.md)  
  `featured` `tutorials` — SurrealDB's built-in capabilities comprising graph queries, geolocational data and recursive queries make it the perfect fit to identify malevolent entities involved in organised influence campaigns.
- **2025-10-09** · [Bring your own knowledge base: Agent Studio meets SurrealDB](2025/10/bring-your-own-knowledge-base-agent-studio-meets-surrealdb.md)  
  `featured` `ai` `community` — How Agent Studio from PolyAI integrates with SurrealDB
- **2025-09-30** · [From Knowledge Graph Generation to RAG for Stablecoin Regulatory Intelligence](2025/09/from-knowledge-graph-generation-to-rag-for-stablecoin-regulatory-intelligence.md)  
  `featured` `ai` `community` — We’re excited to share this community-written deep dive by Sugi Venugeethan into Stablebridge, a project tackling the complex world of stablecoin regulation. This article explores how knowledge graphs, RAG systems, and SurrealDB can be combined to connect it all together. It’s a practical look into knowledge graph generation to advanced retrieval methodologies - showcasing both challenges and breakthroughs along the way.
- **2025-09-17** · [Research paper - Bridging Analytics and Semantics with SurrealDB](2025/09/research-paper--bridging-analytics-and-semantics-with-surrealdb.md)  
  `featured` `community` — We’re excited to highlight new research from two members of the SurrealDB community: “Bridging Analytics and Semantics: A Hybrid Database Approach to Retrieval-Augmented Generation”, now published on Zenodo.
- **2025-09-11** · [Using historical books to create structured knowledge graphs in SurrealDB](2025/09/using-historical-books-to-create-structured-knowledge-graphs-in-surrealdb.md)  
  `featured` `tutorials` — PDF scans of old historical books can be brought to life with LLM models and then stored and queried in a structured form using SurrealQL.
- **2025-09-03** · [Power up your AI workflows: the official SurrealDB x n8n node is here](2025/09/power-up-your-ai-workflows-the-official-surrealdb-x-n8n-node-is-here.md)  
  `featured` `tutorials` `engineering` `ai` — We've shipped the official SurrealDB node for n8n. It's a first-party, production-ready integration that lets you query, create, update, upsert, and delete data in SurrealDB from any n8n workflow - and it also runs as an AI tool inside n8n's Agent nodes.
- **2025-09-03** · [How defence is changing and why databases are critical to the shift into AI](2025/09/how-defence-is-changing-and-why-databases-are-critical-to-the-shift-into-ai.md)  
  `featured` `company` — SurrealDB has launched SurrealMCP, giving AI agents secure, real-time, permission-aware memory powered by its multi-model database.
- **2025-08-29** · [SurrealDB Cloud successfully completes SOC 2 Type 2 Audit](2025/08/surrealdb-cloud-successfully-completes-soc-2-type-2-audit.md)  
  `featured` `company` — SurrealDB Cloud has successfully has successfully completed its SOC 2 Type 2 Audit
- **2025-08-27** · [Multi-tool agent with SurrealMCP and Agno](2025/08/multi-tool-agent-with-surrealmcp-and-agno.md)  
  `featured` `tutorials` `ai` — Using SurrealMCP and Agno, this is how you can build a “researcher” agent that finds information on the web, structures the data, and stores it in SurrealDB.
- **2025-08-23** · [Introducing SurrealMCP](2025/08/introducing-surrealmcp.md)  
  `featured` `releases` `ai` — SurrealDB has launched SurrealMCP, giving AI agents secure, real-time, permission-aware memory powered by its multi-model database.
- **2025-08-22** · [Using unstructured data to create knowledge graphs in SurrealDB](2025/08/using-unstructured-data-to-create-knowledge-graphs-in-surrealdb.md)  
  `featured` `tutorials` `ai` — There are many ways to give structure to unstructured data so that it can be used systematically in a database.
- **2025-08-21** · [From legacy to leverage - unlocking financial data with SurrealDB](2025/08/from-legacy-to-leverage--unlocking-financial-data-with-surrealdb.md)  
  `featured` `tutorials` — SurrealDB helps financial institutions unlock the value of legacy transactional data by transforming it into connected, intelligent, and monetisable insights that power compliance, customer personalisation, and entirely new revenue streams.
- **2025-08-20** · [Enforcing XOR (Either\/Or) Fields in SurrealDB](2025/08/enforcing-xor-eitheror-fields-in-surrealdb.md)  
  `featured` `tutorials` `community` — What to do in your schema when a record should contain one of two possible fields, but not both or neither?
- **2025-08-19** · [SurrealDB achieves Cyber Essentials Plus certification](2025/08/surrealdb-achieves-cyber-essentials-plus-certification.md)  
  `featured` `company` — SurrealDB has successfully achieved CyberEssentials Plus certification
- **2025-08-18** · [Ten tips and tricks for your SurrealDB queries](2025/08/ten-tips-and-tricks-for-your-surrealdb-queries.md)  
  `featured` `tutorials` — SurrealQL queries are expressive and powerful, and the more you know the more you can make your queries work for you.
- **2025-08-11** · [Multi-model RAG with LangChain](2025/08/multi-model-rag-with-langchain.md)  
  `featured` `tutorials` `ai` — A practical walkthrough of building a multi-model RAG pipeline with LangChain and SurrealDB, combining vector search with lightweight graph retrieval over chat conversations.
- **2025-08-07** · [Hybrid vector + text Search in the terminal with SurrealDB and Ratatui](2025/08/hybrid-vector-text-search-in-the-terminal-with-surrealdb-and-ratatui.md)  
  `featured` `tutorials` `ai` — Building an AI-native UI for the terminal that demonstrates newly added hybrid search that combines vector with full-text queries into a single result.
- **2025-08-06** · [Migrate your data directly to SurrealDB using Surreal Sync](2025/08/migrate-your-data-directly-to-surrealdb-using-surreal-sync.md)  
  `featured` `company` `tutorials` — The Surreal Sync command-line tool lets you migrate your data from three sources into SurrealDB with a single terminal command.
- **2025-07-31** · [Does the edge need a new database?](2025/07/does-the-edge-need-a-new-database.md)  
  `featured` `company` — As AI shifts from the cloud to the edge, it’s becoming clear that yesterday’s embedded databases weren’t built for today’s on-device intelligence.
- **2025-07-30** · [Beyond basic RAG: Building a multi-cycle reasoning engine on SurrealDB](2025/07/beyond-basic-rag-building-a-multi-cycle-reasoning-engine-on-surrealdb.md)  
  `tutorials` `featured` `ai` — Standard RAG models operate on single shot principle. The Reflexion RAG Engine overcomes this through a multi-cycle, self-correcting architecture powered by SurrealDB.
- **2025-07-29** · [Building an AI-native multi-model UI with SurrealDB](2025/07/building-an-ai-native-multi-model-ui-with-surrealdb.md)  
  `featured` `tutorials` `ai` — Schema definition in SurrealDB is a powerful thing, and the more you know the more you can make your schema work for you.
- **2025-07-24** · [What's new in Surrealist 3.5](2025/07/whats-new-in-surrealist-3-5.md)  
  `releases` `featured` — Surrealist 3.5 introduces a fully redesigned Sidekick experience, a new Parameters view, a revamped functions view, and loads of other enhancements
- **2025-07-22** · [Two new ways to keep an eye on your SurrealDB database](2025/07/two-new-ways-to-keep-an-eye-on-your-surrealdb-database.md)  
  `featured` `tutorials` — Logging output to file and seeing the current tasks on a console are two new ways to gain greater insight into what your database is doing.
- **2025-07-18** · [The new era of data lakes: knowledge lakes](2025/07/the-new-era-of-data-lakes-knowledge-lakes.md)  
  `featured` `company` — Data lakes are the new era of data storage, but they are not the only way to store data. Knowledge lakes are a new way to store data that is more flexible and scalable.
- **2025-07-15** · [Ten more tips and tricks for your database schema](2025/07/ten-more-tips-and-tricks-for-your-database-schema.md)  
  `featured` `tutorials` — Schema definition in SurrealDB is a powerful thing, and the more you know the more you can make your schema work for you.
- **2025-07-09** · [Make a medical chatbot using GraphRAG with SurrealDB + LangChain](2025/07/make-a-medical-chatbot-using-graphrag-with-surrealdb-langchain.md)  
  `featured` `engineering` `ai` — Build a medical chatbot with GraphRAG, SurrealDB, and LangChain using Rust.
- **2025-07-08** · [The power of SurrealDB embedded](2025/07/the-power-of-surrealdb-embedded.md)  
  `featured` `company` — SurrealDB embedded is a lightweight, secure, and AI-native database engine built in Rust, designed for intelligent, offline-first applications at the edge, supporting rich data models, schema flexibility, built-in ML inference, and fast performance.
- **2025-07-07** · [Semantic search in Rust with SurrealDB and Mistral AI](2025/07/semantic-search-in-rust-with-surrealdb-and-mistral-ai.md)  
  `featured` `engineering` `ai` — SurrealDB's built-in vector search capabilities make it a perfect match for semantic search using Mistral AI
- **2025-07-04** · [Minimal LangChain chatbot example with vector and graph](2025/07/minimal-langchain-chatbot-example-with-vector-and-graph.md)  
  `featured` `tutorials` `ai` — Want to build a chatbot that understands context? This blog post breaks it down with a minimal LangChain example. Learn how to use vector stores and graphs to generate intelligent, natural language answers.
- **2025-07-01** · [Announcing our official LangChain integration](2025/07/announcing-our-official-langchain-integration.md)  
  `engineering` `featured` `ai` — We’re thrilled to announce that SurrealDB now has an official integration with LangChain, one of the most popular frameworks for building powerful LLM-driven applications.
- **2025-06-30** · [Make a GenAI chatbot using GraphRAG with SurrealDB + LangChain](2025/06/make-a-genai-chatbot-using-graphrag-with-surrealdb-langchain.md)  
  `featured` `tutorials` `ai` — Build a GenAI chatbot with GraphRAG, SurrealDB, and LangChain for accurate, graph-enhanced LLM responses; code examples provided.
- **2025-06-27** · [The state of Agentic AI and the need for Agentic Memory](2025/06/the-state-of-agentic-ai-and-the-need-for-agentic-memory.md)  
  `company` `featured` `ai` — Rethinking your data for agents
- **2025-06-26** · [Semantic search with SurrealDB and OpenAI](2025/06/semantic-search-with-surrealdb-and-openai.md)  
  `featured` `engineering` `ai` — SurrealDB's built-in vector search capabilities make it a perfect match for semantic search using OpenAI
- **2025-06-25** · [SurrealDB Cloud Enterprise](2025/06/surreal-cloud-enterprise.md)  
  `company` `featured` — Power your mission-critical applications with SurrealDB Cloud Enterprise
- **2025-06-25** · [Introducing network capabilities in Surreal Cloud](2025/06/introducing-network-capabilities-in-surreal-cloud.md)  
  `releases` `featured` — Surreal Cloud’s latest release introduces network capabilities. Fine grained controls that determine exactly which network targets your database can reach. In this blog we will walk through network capabilities, explore the motivation behind it, and explain how it improves security for everyone running SurrealDB in the cloud.
- **2025-06-24** · [Building real-time AI pipelines in SurrealDB](2025/06/building-real-time-ai-pipelines-in-surrealdb.md)  
  `tutorials` `featured` `ai` — Say goodbye to complex ETL pipelines with SurrealDB's multi-model approach.
- **2025-06-23** · [Seamless data ingestion with the Airbyte connector](2025/06/seamless-data-ingestion-with-the-airbyte-connector.md)  
  `engineering` `featured` — Today, we’re excited to announce official support for Airbyte, the leading open-source data integration platform.
- **2025-06-20** · [What are knowledge graphs and why is everyone talking about them?](2025/06/what-are-knowledge-graphs-and-why-is-everyone-talking-about-them.md)  
  `tutorials` `featured` `ai` — Knowledge graphs provide the structured memory AI agents need for grounded, context-aware reasoning. Learn how this decades-old concept became essential infrastructure for modern AI systems.
- **2025-06-20** · [What's new in Surrealist 3.4](2025/06/whats-new-in-surrealist-3-4.md)  
  `releases` `featured` — Surrealist 3.4 introduces multi-window support, improved computed table views, redesigned Cloud deployment workflow, and multi-record selection capabilities
- **2025-06-19** · [Databases Are the Next AI Frontier](2025/06/databases-are-the-next-ai-frontier.md)  
  `featured` `company` — AI’s bottleneck is no longer compute, it’s about databases: data, storage, and memory.
- **2025-06-17** · [How to simplify a Graph RAG architecture using Amazon Bedrock and SurrealDB](2025/06/how-to-simplify-a-graph-rag-architecture-using-amazon-bedrock-and-surrealdb.md)  
  `featured` `tutorials` `ai` — A typical RAG pipeline forces developers to juggle a vector store, a document store, a graph store (for relationships), plus an LLM endpoint, and to keep them all consistent. SurrealDB and Amazon Bedrock put an end to that sprawl.
- **2025-06-17** · [Ten tips and tricks for your database schema](2025/06/ten-tips-and-tricks-for-your-database-schema.md)  
  `featured` `tutorials` — Schema definition in SurrealDB is a powerful thing.
- **2025-06-17** · [RAG can be Rigged](2025/06/rag-can-be-rigged.md)  
  `featured` `engineering` `ai` — Building a smart knowledge agent with SurrealDB and Rig.rs
- **2025-06-13** · [Fraud detection with SurrealDB](2025/06/fraud-detection-with-surrealdb.md)  
  `featured` — Fraud is fundamentally a graph problem: fraudsters rarely act alone; they connect through shared emails, reused devices, forwarding addresses, or round‑robin money flows.
- **2025-06-11** · [Seamless data ingestion with the Fivetran connector](2025/06/seamless-data-ingestion-with-the-fivetran-connector.md)  
  `featured` `engineering` — Today, we’re excited to announce official support for Fivetran, the industry leader in automated, fully-managed data pipelines.
- **2025-06-09** · [How Aspire Comps replaced 5 backend tools with SurrealDB and scaled to 700,000 users](2025/06/how-aspire-comps-replaced-5-backend-tools-with-surrealdb-and-scaled-to-700000-users.md)  
  `featured` `company` — Aspire Comps moved from Firebase to SurrealDB, eliminated backend bloat, and now powers a high-scale platform with one unified database engine.
- **2025-06-03** · [Enhance your musical skills with Surrealist's Graph View](2025/06/enhance-your-musical-skills-with-surrealists-graph-view.md)  
  `tutorials` `featured` — Did you know that Surrealist's Graph Visualisation tool can even make you into a better musician? Let's find out how.
- **2025-06-02** · [Three ways to model data relationships in SurrealDB](2025/06/three-ways-to-model-data-relationships-in-surrealdb.md)  
  `featured` `engineering` — In a recent SurrealDB Stream, we cracked open a foundational part of SurrealDB’s power: relationship modelling. From traditional record-to-record links to bidirectional references and Graph Edge metadata, we explored the many ways you can model connected data - clearly, scalably, and with performance in mind.
- **2025-05-23** · [Surreal Cloud successfully completes SOC2 Type 1 Audit](2025/05/surreal-cloud-successfully-completes-soc2-type-1-audit.md)  
  `company` — SurrealDB's Surreal Cloud has successfully completed its SOC2 Type 1 Audit
- **2025-04-15** · [Introducing Teams and Organisations in SurrealDB Cloud](2025/04/introducing-teams-and-organisations-in-surreal-cloud.md)  
  `featured` `releases` — Whether you're a startup of two or an enterprise of thousands, SurrealDB Cloud now scales with your team.
- **2025-04-10** · [What's a database anyway?? A blog post for kids](2025/04/whats-a-database-anyway-a-blog-post-for-kids.md)  
  `tutorials` `featured` — An easy explanation for children of what a database is.
- **2025-04-02** · [Cooking up faster RAG using in-database embeddings in SurrealDB](2025/04/cooking-up-faster-rag-using-in-database-embeddings-in-surrealdb.md)  
  `engineering` `ai` — Speed up RAG pipelines by running embedding models directly inside SurrealDB. Eliminate external API latency with in-database vector embeddings for faster retrieval-augmented generation.
- **2025-03-26** · [What's new in Surrealist 3.3](2025/03/whats-new-in-surrealist-3-3.md)  
  `releases` `featured` — Explore the key features of the Surrealist 3.3 release
- **2025-03-26** · [Beyond black boxes - building customisable and secure RAG systems for financial services](2025/03/beyond-black-boxes--building-customisable-and-secure-rag-systems-for-financial-services.md)  
  `engineering` `ai` — This isn’t just another RAG blog post - it tackles the specific challenges financial services data teams face when building systems in regulated, data-sensitive environments.
- **2025-03-25** · [Tips and tricks on using the Rust SDK](2025/03/tips-and-tricks-on-using-the-rust-sdk.md)  
  `tutorials` `featured` — In this article we are going to explore some tips and tricks for using the Rust SDK.
- **2025-03-25** · [Revolutionising decentralised discovery with SurrealDB and confidential computing](2025/03/revolutionising-decentralised-discovery-with-surrealdb-and-confidential-computing.md)  
  `engineering` `featured` — ndex Network enables secure, decentralised discovery by unifying public and private data using SurrealDB and TEEs.
- **2025-03-24** · [Data analysis using graph traversal, recursion, and shortest path](2025/03/data-analysis-using-graph-traversal-recursion-and-shortest-path.md)  
  `tutorials` `featured` — Whether you're building intelligent applications, modelling complex relationships, or looking to optimise performance, SurrealDB's graph capabilities open up exciting new possibilities.
- **2025-03-21** · [Our support for FaunaDB users](2025/03/our-support-for-faunadb-users.md)  
  `company` `featured` — We wanted to take a moment to acknowledge the difficult news about FaunaDB winding down operations.
- **2025-03-13** · [Visualising your data with Surrealist's Graph view](2025/03/visualising-your-data-with-surrealists-graph-view.md)  
  `tutorials` `featured` — We as humans love visual data, and the new graph view for Surrealist provides exactly this.
- **2025-03-06** · [Building smarter product recommendations with SurrealDB](2025/03/building-smarter-product-recommendations-with-surrealdb.md)  
  `tutorials` `featured` — Blog post inspired by your reading history
- **2025-02-27** · [Find your celebrity soulmate with the magic of vector search](2025/02/find-your-celebrity-soulmate-with-the-magic-of-vector-search.md)  
  `tutorials` `featured` — Have you ever wondered how to find someone or something that’s most like you, whether it’s a roommate, someone who shares your Christmas traditions, or even a celebrity? Vector search is the answer. It’s a modern way to find matches based on multiple preferences at once, and tools like SurrealDB make it incredibly easy to use. Let’s explore what vector search is and how it works, step by step.
- **2025-02-21** · [Automating knowledge graphs with SurrealDB and Gemini](2025/02/automating-knowledge-graphs-with-surrealdb-and-gemini.md)  
  `engineering` `ai` — This is the release you've been waiting for
- **2025-02-11** · [Beginning our benchmarking journey](2025/02/beginning-our-benchmarking-journey.md)  
  `company` `featured` — From humble beginnings come great things.
- **2025-02-11** · [SurrealDB 2.2: Benchmarking, graph path algorithms and foreign key constraints](2025/02/surrealdb-2-2-benchmarking-graph-path-algorithms-and-foreign-key-constraints.md)  
  `releases` `company` `featured` — This is the release you've been waiting for
- **2025-02-05** · [How we improved the Python SDK for our 1.0 stable version](2025/02/how-we-improved-the-python-sdk-for-our-1-0-stable-version.md)  
  `engineering` — We've released our 1.0 stable version of our Python SDK
- **2025-02-04** · [Powering Drug Trial Innovation with SurrealDB](2025/02/powering-drug-trial-innovation-with-surrealdb.md)  
  `community` `featured` — By leveraging SurrealDB, we built a system that simplifies the drug trial search process
- **2025-01-31** · [Enhancing retrieval-augmented generation with SurrealDB](2025/01/enhancing-retrieval-augmented-generation-with-surrealdb.md)  
  `tutorials` `featured` `ai` — GraphRAG: Enhancing Retrieval-Augmented Generation with SurrealDB, Gemini and DeepSeek
- **2025-01-31** · [Improving the documentation user experience](2025/01/improving-the-documentation-user-experience.md)  
  `community` `featured` — We have made some improvements to the documentation user experience learn more
- **2025-01-30** · [What's new in Surrealist 3.2](2025/01/whats-new-in-surrealist-3-2.md)  
  `releases` `featured` — Explore the key features of the Surrealist 3.2 release
- **2025-01-24** · [Making your own PR to the SurrealDB source code](2025/01/making-your-own-pr-to-the-surrealdb-source-code.md)  
  `community` — Making a small PR to the SurrealDB source code is easier than you think, even if you come from another programming language.
- **2024-12-13** · [Your personal Surreal Sidekick](2024/12/your-personal-surreal-sidekick.md)  
  `releases` `featured` `company` — With the recent release of SurrealDB Cloud (beta) and the introduction of the SurrealDB Cloud panel in Surrealist, we introduced a brand new tool to help you increase your SurrealDB productivity.
- **2024-11-27** · [What's new in Surrealist 3.1](2024/11/whats-new-in-surrealist-3-1.md)  
  `releases` `featured` — Explore the key features of the Surrealist 3.1 release
- **2024-11-21** · [SurrealDB 2.1.0 is live!](2024/11/surrealdb-2-1-0-is-live.md)  
  `releases` — We are excited to announce the release of SurrealDB 2.1.0, our latest version of our scalable cloud graph database.
- **2024-10-21** · [Aeon's Surreal Renaissance: Learn SurrealDB through a story](2024/10/aeons-surreal-renaissance-learn-surrealdb-through-a-story.md)  
  `releases` `featured` — An immersive and interactive story that makes learning about SurrealDB as exciting as reading your favourite book.
- **2024-10-15** · [SurrealDB Empowers Developers to Build Applications with the Launch of SurrealDB University](2024/10/surrealdb-empowers-developers-to-build-applications-with-the-launch-of-surrealdb-university.md)  
  `releases` `featured` `company` — Access to this comprehensive course provides any developer with the education and documentation needed to quickly and successfully build applications on SurrealDB in as little as three hours
- **2024-09-17** · [SurrealDB delivers future-ready database technology for developers and enterprises with release of SurrealDB 2.0 ](2024/09/surrealdb-delivers-future-ready-database-technology-for-developers-and-enterprises-with-release-of-surrealdb-2-0.md)  
  `releases` `featured` `company` — Powerful new features introduce advanced stability, performance, security and data management capabilities to build enterprise-ready applications
- **2024-09-17** · [Surrealist 3.0 is now available!](2024/09/surrealist-3-0-is-now-available.md)  
  `releases` `featured` — We are excited to announce the latest major iteration of Surrealist
- **2024-09-17** · [Challenge accepted: announcing SurrealDB 2.0](2024/09/challenge-accepted-announcing-surrealdb-2-0.md)  
  `releases` `featured` `company` — With the massive community adoption that followed came massive expectations and challenges to live up to these expectations.
- **2024-09-02** · [Surrealist 3.0 beta](2024/09/surrealist-3-0-beta.md)  
  `releases` — We are thrilled to announce that the first beta release for Surrealist 3.0 is now available.
- **2024-08-28** · [Building a retrieval-augmented generation (RAG) app with OpenAI and SurrealDB](2024/08/building-a-retrieval-augmented-generation-app-with-openai-and-surrealdb.md)  
  `engineering` `tutorials` — We'll build an assistant that can answer questions based on Wikipedia information, using the GPT Turbo model from OpenAI
- **2024-08-20** · [It’s about time: time series in SurrealDB](2024/08/its-about-time-time-series-in-surrealdb.md)  
  `engineering` `tutorials` — What is time anyway
- **2024-07-25** · [Moving from full-text search to vector search in SurrealDB](2024/07/moving-from-full-text-search-to-vector-search-in-surrealdb.md)  
  `engineering` — If you know exactly what you’re searching for Full-Text Search would be the way to go but when you want your search to understand you, Vector Search might be right for you.
- **2024-07-16** · [Real-time data science: Orchestrating insights with the right ensemble](2024/07/real-time-data-science-orchestrating-insights-with-the-right-ensemble.md)  
  `engineering` `tutorials` — Building real-time analytics leveraging OLAP, multi-model databases and workload isolation.
- **2024-06-24** · [Celebrating milestones and looking forward](2024/06/celebrating-milestones-and-looking-forward.md)  
  `company` `featured` — Last week was awesome for our team at SurrealDB! It feels like the perfect time to pause and reflect on the whirlwind of achievements, all of which signal exciting times ahead for our company. We are incredibly proud to share some major milestones we've hit, and we want to extend our deepest gratitude to everyone who has been part of this journey to date.
- **2024-06-17** · [SurrealDB Raises $20M to Disrupt Database Tech; Introduces New Cloud Beta Access](2024/06/surrealdb-raises-20m-to-disrupt-database-tech-introduces-new-cloud-beta-access.md)  
  `company` `featured` — London, United Kingdom June 18, 2024, SurrealDB, the ultimate multi-model database, today announced a $20 million investment round led by FirstMark and Georgian with participation from Crew Capital and Alumni Ventures. This latest round of funding brings SurrealDB’s total to $26 million.
- **2024-06-14** · [Surrealist just got better - Update now!](2024/06/surrealist-just-got-better--update-now.md)  
  `releases` — This article dives into the Surrealist 2.1.2 release, highlights some technical changes, and explains why you will have to download this release manually
- **2024-06-13** · [Our new demo dataset has a lot in store for you!](2024/06/our-new-demo-dataset-has-a-lot-in-store-for-you.md)  
  `releases` `tutorials` — But Wait, There's More!
- **2024-06-04** · [What's new in Surrealist 2.1](2024/06/whats-new-in-surrealist-2-1.md)  
  `releases` — Explore the key features of the Surrealist 2.1 release
- **2024-05-17** · [Introducing Surreal<Any>: Dynamic Support for any Engine in Rust](2024/05/introducing-surrealany-dynamic-support-for-any-engine-in-rust.md)  
  `engineering` `tutorials` — Understand what is a `Surreal<Any>` engine and how you can use it in your Rust code.
- **2024-05-14** · [v1.5.0 is live!🎉](2024/05/v1-5-0-is-live.md)  
  `releases` — This new release comes with performance updates and new additions to Vector Search
- **2024-05-09** · [Why SurrealDB is the Future of Database Technology - An In-Depth Look](2024/05/why-surrealdb-is-the-future-of-database-technology--an-in-depth-look.md)  
  `community` `tutorials` — The people who are crazy enough to think that they can change the world, are the ones who do
- **2024-05-01** · [Surrealist 2.0](2024/05/surrealist-2-0.md)  
  `releases` `featured` — An important part of each database is the ability to easily and effortlessly control each aspect of the database. While this may appear trivial at first, it actually encompasses a wide set of different tasks. For this reason Surrealist has officially joined SurrealDB as the official management interface.
- **2024-04-23** · [The Surrealist journey](2024/04/the-surrealist-journey.md)  
  `company` — Interacting with a database is not an easy job. You’ll often find yourself needing to query patterns in your data, testing whether your queries have the intended outcome, or carefully designing a schema to suit your application. This was a natural hurdle I ran into when first adopting SurrealDB into my workflow, and is exactly why I built Surrealist.
- **2024-04-22** · [Introducing Surrealist](2024/04/introducing-surrealist.md)  
  `releases` — Dive into why this mobile software development company chose to migrate to our multi-model database.
- **2024-04-15** · [ELI5 - Why SurrealDB, explained through building with LEGO](2024/04/eli5--why-surrealdb-explained-through-building-with-lego.md)  
  `community` `tutorials` — Can databases inspire a sense of child-like play?
- **2024-04-09** · [v1.4.0 is live! 🎉](2024/04/v1-4-0-is-live.md)  
  `releases` — This new release comes with bug fixes, performance improvements, and feature updates to -insert thing-
- **2024-03-26** · [Exploring the AI revolution](2024/03/exploring-the-ai-revolution.md)  
  `tutorials` — Looking to keep up-to-date with what's next in Generative AI and LLMs? We've got you covered.
- **2024-03-25** · [Document-Style Relationships in SurrealDB](2024/03/document-style-relationships-in-surrealdb.md)  
  `tutorials` — Your feedback matters! We’re introducing short-form video tutorials.
- **2024-03-17** · [How to simplify your tech stack](2024/03/how-to-simplify-your-tech-stack.md)  
  `tutorials` — Oscar Merry talks about powering a social podcasting app, Fountain, using SurrealDB.
- **2024-03-15** · [Understanding CBOR](2024/03/understanding-cbor.md)  
  `engineering` `tutorials` — JSON is the popular kid in school, but CBOR is the new kid who's smaller, faster, and has more tricks up its sleeve!
- **2024-03-13** · [Why we are betting on Rust](2024/03/why-we-are-betting-on-rust.md)  
  `engineering` `company` — The best way to predict the future is to create it.
- **2024-03-12** · [v1.3.0 is live! 🎉](2024/03/v1-3-0-is-live.md)  
  `releases` — This new release comes with bug fixes, performance improvements, and feature updates to our define & remove statements and KNN syntax.
- **2024-03-09** · [Introducing SurrealDB's custom emoji pack](2024/03/introducing-surrealdbs-custom-emoji-pack.md)  
  `community` — If the Internet has enabled us to communicate beyond boundaries in real-time, emojis helped it by making them the universal language of expression.
- **2024-03-08** · [From medical doctor to rust developer - interview with our new Senior Clinical Research Fellow](2024/03/from-medical-doctor-to-rust-developer--interview-with-our-new-senior-clinical-research-fellow.md)  
  `community` — Read about her journey and why she is using SurrealDB for her current research.
- **2024-02-21** · [Thinking Inside The Box: Relational Style Joins in SurrealDB](2024/02/thinking-inside-the-box-relational-style-joins-in-surrealdb.md)  
  `tutorials` — SurrealDB's relational style joins exist in a superposition. The only way to know for sure is by looking at this blog post.
- **2024-02-06** · [v1.2.0-beta.1 is live! 🎉](2024/02/v1-2-0-beta-1-is-live.md)  
  `releases` — This new release comes with bug fixes, performance improvements, and feature updates to string methods, support for READONLY fields and type support for subfields.
- **2024-02-01** · [We're hiring](2024/02/were-hiring.md)  
  `company` — We're hiring! Join SurrealDB as we continue to shape the future of database technology! We're on the lookout for exceptional individuals - those who are passionate about their craft and equally passionate about the team they work with to develop and promote groundbreaking technology.
- **2024-01-29** · [Beyond SQL joins: Exploring SurrealDB's multi-model relationships](2024/01/beyond-sql-joins-exploring-surrealdbs-multi-model-relationships.md)  
  `tutorials` — Can't join? No worries, we can relate.
- **2024-01-23** · [VART: A persistent data structure for snapshot isolation](2024/01/vart-a-persistent-data-structure-for-snapshot-isolation.md)  
  `engineering` — The blog introduces VART, an Immutable Versioned Adaptive Radix Trie, designed for snapshot isolation in databases (surrealKV), exploring isolation levels, concurrency control.
- **2024-01-14** · [Integrate Auth0 as an Authentication provider](2024/01/integrate-auth0-as-an-authentication-provider.md)  
  `tutorials` — This guide will cover using Auth0 as the authentication provider for single-page web applications using SurrealDB as the only backend.
- **2024-01-12** · [Introducing our new monthly release schedule](2024/01/introducing-our-new-monthly-release-schedule.md)  
  `releases` `company` — We are excited to announce a change in our product release schedule, with a regular monthly release cycle, allowing developers and organisations to build on top of SurrealDB, with predictable timelines for software improvements and fixes.
- **2024-01-10** · [Live queries in Rust](2024/01/live-queries-in-rust.md)  
  `tutorials` `engineering` — SurrealDB comes with a LIVE SELECT statement that allows you to listen for creations, updates and deletions to specific records you are interested in or entire tables.
- **2024-01-09** · [Release v1.1.0](2024/01/release-v1-1-0.md)  
  `releases` — We're excited to announce SurrealDB v1.1.0, with many performance improvements, bug fixes, and new features, and native machine learning computation, right within the database.
- **2024-01-09** · [Introducing Nightly and Beta Rust Crates](2024/01/introducing-nightly-and-beta-rust-crates.md)  
  `releases` `engineering` `company` — We are pleased to announce two additional Rust crates, surrealdb-nightly and surrealdb-beta. These crates are designed to complement the surrealdb crate.
- **2023-12-18** · [Crafting our full-text search in SurrealDB: A journey beyond Lucene and Tantivy](2023/12/crafting-our-full-text-search-in-surrealdb-a-journey-beyond-lucene-and-tantivy.md)  
  `engineering` — How SurrealDB built its own ACID-compliant full-text search engine instead of integrating Lucene or Tantivy, delivering a unified query experience without external dependencies.
- **2023-12-12** · [What is SurrealML: A getting started guide](2023/12/what-is-surrealml-a-getting-started-guide.md)  
  `tutorials` `engineering` — The developer community has made great strides in building open-source machine-learning packages that save machine-learning models. However, there are still areas of this pipeline that are not fully complete.
- **2023-12-05** · [Introducing the New SurrealDB Documentation on Docusaurus!](2023/12/introducing-the-new-surrealdb-documentation-on-docusaurus.md)  
  `company` — We are excited to announce the new SurrealDB documentation. At SurrealDB, we are constantly looking for ways to improve the experience of developers on our platform which has brought us to rethinking our documentation platform.
- **2023-11-30** · [How I built a SaaS powered by SurrealDB (recorded live at SurrealDB Social)](2023/11/how-i-built-a-saas-powered-by-surrealdb-recorded-live-at-surrealdb-social.md)  
  `tutorials` — Join Software Engineer Micha de Vries as he explores his journey as a developer and dives into a practical application of SurrealDB, showcasing his SaaS product PlayrBase, built almost entirely with SurrealDB.
- **2023-11-30** · [Deploy SurrealDB to Kubernetes with GitOps - Ryota Sawada (recorded live at SurrealDB Social)](2023/11/deploy-surrealdb-to-kubernetes-with-gitops--ryota-sawada-recorded-live-at-surrealdb-social.md)  
  `tutorials` — Community Spotlight talk by Ryota Sawada. When trying out SurrealDB on your local machine for the first time, it is extremely simple to get started with its excellent CLI.
- **2023-11-20** · [Unlocking Streaming Data Magic with SurrealDB: Live Queries and Change Feeds](2023/11/unlocking-streaming-data-magic-with-surrealdb-live-queries-and-change-feeds.md)  
  `tutorials` — In this article, you will learn what streaming means with SurrealDB. We will also cover some patterns addressing how users can use streaming in practice.
- **2023-11-14** · [How Rust gave SurrealDB an edge in the database world](2023/11/how-rust-gave-surrealdb-an-edge-in-the-database-world.md)  
  `tutorials` `community` — Join Senior Software Engineer, Maxwell Flitton, as he shines a light on how Rust and Async Rust gave SurrealDB an edge in the database world.
- **2023-11-13** · [Create a search engine with SurrealDB full-text search](2023/11/create-a-search-engine-with-surrealdb-full-text-search.md)  
  `tutorials` — When it comes to managing and retrieving vast amounts of textual data, the ability to perform efficient and accurate searches is paramount.
- **2023-11-02** · [How to handle big data properly with SurrealDB](2023/11/how-to-handle-big-data-properly-with-surrealdb.md)  
  `tutorials` — Join SurrealDB's co-founder and CEO, Tobie Morgan Hitchcock, and Software Engineer Micha de Vries as we dive into how to handle big data properly with SurrealDB. Ask questions, leave comments, and get involved.
- **2023-10-13** · [Surreal Stickies 2.0: Adding Graph Relations, Live Queries, and Authentication](2023/10/surreal-stickies-2-0-adding-graph-relations-live-queries-and-authentication.md)  
  `tutorials` — Welcome back to the second instalment of our tutorial series on building a notes app with Next.js, Tailwind, and SurrealDB.
- **2023-10-02** · [SurrealDB World 2023 - A Recap](2023/10/surrealdb-world-2023--a-recap.md)  
  `events` `company` — Two weeks ago at SurrealDB World 2023, our first-ever user conference, we launched SurrealDB 1.0! We were thrilled to see an amazing response to the event, with over 300 people attending in person and more than 2,000 online.
- **2023-09-14** · [Announcing SurrealDB 1.0](2023/09/announcing-surrealdb-1-0.md)  
  `releases` `company` — At SurrealDB World, we’re excited to launch SurrealDB 1.0, a revolution in the database technology landscape. With this stable release, we're not just introducing a database; we're redefining the essence of how databases function and integrate with your projects.
- **2023-09-04** · [What's new for developers in SurrealDB Beta 10](2023/09/whats-new-for-developers-in-surrealdb-beta-10.md)  
  `releases` — Hello Developers! After months of hard work, we're excited to roll out v1.0.0-beta.10. Here's what's new!
- **2023-08-29** · [Data Modelling and Performance](2023/08/data-modelling-and-performance.md)  
  `tutorials` — As SurrealDB is a multi-model database, you have a lot of options for how to model your data. In this stream, we'll take a practical look into different approaches to data modelling and discuss use cases, pros, cons and performance implications.
- **2023-08-15** · [Questions from the Community](2023/08/questions-from-the-community.md)  
  `tutorials` — For this stream we’ll cover a variety of topics raised by our community including data modelling in SurrealDB, performance, transactions and more. It’s also your opportunity to ask questions live during the stream.
- **2023-08-01** · [Record IDs, Expressions and Graphs](2023/08/record-ids-expressions-and-graphs.md)  
  `tutorials` — Join us for our 10th live stream as we talk practically about how record IDs help us with connecting data through record links and graph relations and how it can be used to simplify your CRUD operations through simple and advanced expressions.
- **2023-07-24** · [What are multi-model databases?](2023/07/what-are-multi-model-databases.md)  
  `engineering` `tutorials` — In today's digital age, staying connected is easier than ever. Social media platforms allow us to remain connected with loved ones, meet new people, and stay updated on world news...
- **2023-07-18** · [All About Python](2023/07/all-about-python.md)  
  `tutorials` — This stream is all about Python, where we'll cover the why and the how of using it with SurrealDB. You'll learn all about the design decisions for the Rust rewrite and see demos of how to get up and running as well as deploying a Flask app in Docker.
- **2023-07-04** · [Full-Text Search Indexing](2023/07/full-text-search-indexing.md)  
  `tutorials` — Join Senior Software Engineer, Emmanuel Keller and co-founder and CEO Tobie Morgan Hitchcock as we dive into the innovative roadmap of SurrealDB.
- **2023-06-27** · [Tutorial: Build a Notes App with Next.js, Tailwind and SurrealDB](2023/06/tutorial-build-a-notes-app-with-next-js-tailwind-and-surrealdb.md)  
  `tutorials` — In this guide, you'll learn how to implement a simple full-stack note-taking application called Surreal Stickies.
- **2023-06-26** · [We're now on Instagram!](2023/06/were-now-on-instagram.md)  
  `community` — It’s been a crazy 9 months, and we have lots of awesome photos to share with you from our journey so far!
- **2023-06-20** · [JavaScript Library with Micha & Tobie](2023/06/javascript-library-with-micha-tobie.md)  
  `tutorials` `engineering` — This week we're focusing on SurrealDB's JavaScript Library. Join Micha and Tobie as they chat about recent updates and highlights, and showcase how to use live queries and the WASM library.
- **2023-06-19** · [WebSocket Protocol Guide](2023/06/websocket-protocol-guide.md)  
  `tutorials` — We've published a WebSocket Protocol Guide! This allows for easy bi-directional communication with SurrealDB. If you're excited about Live Queries, check this out!
- **2023-06-16** · [Installing SurrealDB](2023/06/installing-surrealdb.md)  
  `tutorials` — Installed SurrealDB yet? Here's a guide to get started.
- **2023-06-15** · [Deploy to Kubernetes](2023/06/deploy-to-kubernetes.md)  
  `tutorials` — Our guide for deploying to Kubernetes is live! Learn more here...
- **2023-06-08** · [Announcing Developer Office Hours](2023/06/announcing-developer-office-hours.md)  
  `community` — We're kicking off Developer Office Hours! 🎉 Starting June 9th, we'll be hosting this on Discord every Friday.
- **2023-06-02** · [Announcing SurrealDB World](2023/06/announcing-surrealdb-world.md)  
  `events` — Over the past six months, we have been forging ahead with SurrealDB, and now we are delighted to announce SurrealDB World conference, which will take place on September 13 2023 in London, UK.
- **2023-05-31** · [Thank you GitHub for the feature!](2023/05/thank-you-github-for-the-feature.md)  
  `community` `company` — Thank you GitHub for the feature on the Maintainer Month Library! 🎉 As part of our efforts to celebrate #MaintainerMonth 2023, we had a chat with one of our maintainers here at SurrealDB, Rushmore Mushambi.
- **2023-05-29** · [Maintainer Month 2023: Behind the scenes with Yusuke Kuoka](2023/05/maintainer-month-2023-behind-the-scenes-with-yusuke-kuoka.md)  
  `community` — Hi! I’m Yusuke, and I’m a Senior Software Engineer at SurrealDB. It’s #MaintainerMonth, so I’d like to explain why I became a ‘maintainer’, tell you about my journey so far, and then give you a glimpse of my life as a maintainer.
- **2023-05-26** · [Rounding up May with SurrealDB Social](2023/05/rounding-up-may-with-surrealdb-social.md)  
  `events` — Whether you've just discovered SurrealDB or are an early adopter, you're invited to our monthly tech meetup SurrealDB Social at Huckletree, Oxford Circus. This month’s focus is on Live Queries, with talks from Hugh Kaznowski and CEO Tobie Morgan Hitchcock.
- **2023-05-25** · [Maintainer Month 2023: Behind the scenes with Rushmore Mushambi](2023/05/maintainer-month-2023-behind-the-scenes-with-rushmore-mushambi.md)  
  `community` — Hi everyone. My name is Feranmi Okafor. I'm a Social Media Manager at SurrealDB. As part of our efforts to celebrate #MaintainerMonth 2023, we had a quick chat with one of our maintainers here at SurrealDB.
- **2023-05-16** · [Live Queries with Tobie & Hugh](2023/05/live-queries-with-tobie-hugh.md)  
  `tutorials` — This week we're focusing on live queries, with co-founder Tobie Morgan Hitchcock and Senior Software Engineer Hugh Kaznowski.
- **2023-05-11** · [The life-changing magic of SurrealDB record IDs](2023/05/the-life-changing-magic-of-surrealdb-record-ids.md)  
  `engineering` `tutorials` — At SurrealDB, we are all about doing things that spark joy for developers. One of those things that constantly surprises and delights is the humble record ID, which we discussed in our live stream.
- **2023-05-06** · [SurrealDB Giveaway](2023/05/surrealdb-giveaway.md)  
  `community` — We are utterly blown away! Thank you so, so much to the SurrealDB and dev communities for your amazing support since our launch in August.
- **2023-05-05** · [Getting started with the SurrealDB Go Driver](2023/05/getting-started-with-the-surrealdb-go-driver.md)  
  `tutorials` — In our Beta 9 release, we updated our Go driver. In this tutorial, we will learn to build a simple SurrealDB URL shortener using the Go driver. A URL shortener is a very simple yet powerful tool that can help you be more productive.
- **2023-05-01** · [SurrealDB Scalability](2023/05/surrealdb-scalability.md)  
  `engineering` — SurrealDB is a multi-paradigm database that allows you to perform document, graph, temporal, spatial, and text operations within an ACID environment. The SurrealDB service is a compute layer that processes queries and operates on a storage layer. As of writing, our storage layer is predominantly RocksDB.
- **2023-04-25** · [All About SurrealQL](2023/04/all-about-surrealql.md)  
  `tutorials` — This week's SurrealDB Stream focused on SurrealQL with co-founder Tobie Morgan Hitchcock, Data Evangelist Alexander Fridriksson and Software Engineer Micha de Vries: Why is SurrealQL a SQL-like language vs a custom language like MongoQL or Cypher?
- **2023-04-25** · [Clustered SurrealDB for 1.0.0-beta9](2023/04/clustered-surrealdb-for-1-0-0-beta9.md)  
  `tutorials` — In this post, I will show you how to set up a distributed SurrealDB cluster that shares a distributed TiKV cluster. This architecture allows you to scale your operations to improve writes and reads and seamlessly continue operations during failures.
- **2023-04-21** · [The ultimate beginners guide to databases](2023/04/the-ultimate-beginners-guide-to-databases.md)  
  `tutorials` — It is our belief that developers should be able to build secure, modern, collaborative applications without needing to build complicated backend APIs and database layers, and without being forced into using a single data model or cloud platform.
- **2023-04-12** · [Behind the scenes of the exciting beta 9 release](2023/04/behind-the-scenes-of-the-exciting-beta-9-release.md)  
  `tutorials` — Our team has been working very hard on the new release, which introduces a ton of new features, bug fixes and performance improvements you can see here...
- **2023-03-30** · [Understanding SurrealQL and how it is different from PostgreSQL](2023/03/understanding-surrealql-and-how-it-is-different-from-postgresql.md)  
  `tutorials` — In this article, we will explore the similarities and differences between PostgreSQL and SurrealQL. We will also see how SurrealQL can overcome some of the limitations that relational databases have.
- **2023-02-08** · [An introduction to SurrealDB](2023/02/an-introduction-to-surrealdb.md)  
  `tutorials` — If you are reading this, you may be wondering how to get started with this fantastic product you just discovered, SurrealDB. It's a database that does many routine things, so you can focus on what matters to you - processing your data.
- **2023-02-06** · [SurrealDB Social X Swingers](2023/02/surrealdb-social-x-swingers.md)  
  `events` — The room was buzzing at our first SurrealDB Social held at Swingers Crazy Golf in central London, as we had the opportunity to connect with members of our SurrealDB community face-to-face! We had Surrealers travel in from around the UK, as well as Europe and even the US.
- **2023-02-06** · [First New York SurrealDB Social](2023/02/first-new-york-surrealdb-social.md)  
  `events` — We’re throwing our first New York SurrealDB Social on Tuesday 14 March, 6-10PM EST, at Swingers (35 W 29th St, New York, NY 10001)!
- **2023-02-05** · [New 'Awesome SurrealDB' repo!](2023/02/new-awesome-surrealdb-repo.md)  
  `community` — We have created an 'Awesome SurrealDB' repo. Please suggest any libraries, tools, tutorials or videos there by submitting a pull request!
- **2023-01-11** · [First London SurrealDB Social](2023/01/first-london-surrealdb-social.md)  
  `events` — We're throwing our first SurrealDB Social in London on Wednesday 25 January, 6-9PM GMT, at Swingers West End!
- **2023-01-04** · [We are thrilled to announce our $6M Seed round led by FirstMark Capital and Matt Turck!](2023/01/we-are-thrilled-to-announce-our-6m-seed-round-led-by-firstmark-capital-and-matt-turck.md)  
  `company` — Matt and FirstMark deeply share our vision, and we are truly humbled to have them with us on this journey.
- **2022-12-13** · [Get your hands on our first ever SurrealDB stickers!](2022/12/get-your-hands-on-our-first-ever-surrealdb-stickers.md)  
  `community` — Want to get your hands on our first ever limited-edition SurrealDB stickers 🌈❄️👀 We would love to learn how you are using SurrealDB!
- **2022-11-25** · [We are hiring!](2022/11/we-are-hiring.md)  
  `company` — We are a startup with an ambitious mission to build the ultimate multi-model database for tomorrow’s applications. We are seeking to hire the best - people who care deeply about the work they do, and care about the people with whom they create and promote the product.
- **2022-10-01** · [Release v1.0.0-beta.8](2022/10/release-v1-0-0-beta-8.md)  
  `releases` — We know you've been waiting for it! And SurrealDB's beta 8 is finally here!
- **2022-09-17** · [Beyond Surreal? A closer look at NewSQL Relational Data.](2022/09/beyond-surreal-a-closer-look-at-newsql-relational-data.md)  
  `community` — Thank you very much Fireship once again for another brilliant video on SurrealDB! We really, really appreciate it!
- **2022-09-17** · [#2 on Hacker News](2022/09/2-on-hacker-news.md)  
  `community` — #2 on Hacker News... There won't be much sleep once again for Jaime and Tobie this weekend! Thank you once again for all the support over the past 3 weeks!
- **2022-09-17** · [10,000 thank yous!](2022/09/10000-thank-yous.md)  
  `community` — ⭐ 10,000 GitHub stars in 4 weeks! We are utterly blown away! Thank you so, so much to the SurrealDB and dev communities for your amazing support! This is only the start of the SurrealDB journey! We have so much more to come! ⭐
- **2022-09-16** · [Thank you Fireship!](2022/09/thank-you-fireship.md)  
  `community` — Thank you very much Fireship for the 📹 video on SurrealDB! We really appreciate it!
- **2022-09-16** · [We think we have broken GitHub...](2022/09/we-think-we-have-broken-github.md)  
  `community` — Thank you once again for all the love and support over the last 24 hours! SurrealDB is currently the No. 1 📈 AND No. 2 📈 trending public repository on GitHub worldwide! We think we have broken GitHub 😵!
- **2022-09-12** · [5000 thank yous](2022/09/5000-thank-yous.md)  
  `community` — ⭐ 5000 GitHub stars in 3 weeks! Wow! We are blown away! Thank you, thank you, thank you to the SurrealDB and dev communities for your amazing support! ⭐
- **2022-09-10** · [Rust Powered Database SurrealDB (It's Pretty Ambitious)](2022/09/rust-powered-database-surrealdb-its-pretty-ambitious.md)  
  `community` — Thank you very much to Code to the Moon for the YouTube video tour of the query language and capabilities of SurrealDB!
- **2022-09-06** · [Getting started with SurrealDB](2022/09/getting-started-with-surrealdb.md)  
  `community` — Thank you very much to Chris Hay, CTO at IBM iX for his excellent, thorough video on SurrealDB. We are looking forward to the sequel!
- **2022-09-02** · [Just released SurrealDB for Windows!](2022/09/just-released-surrealdb-for-windows.md)  
  `releases` — The easiest and preferred way to get going with SurrealDB on Windows is to install and use the SurrealDB command-line tool. Run the following command in your terminal and follow the on-screen instructions...
- **2022-08-29** · [Release v1.0.0-beta.7](2022/08/release-v1-0-0-beta-7.md)  
  `releases` — Add support for Objects and Arrays as Record IDs, add support for querying records using Record ID ranges, add SQL <code>session<\/code> functions for retrieving session variables, make <code>--ns<\/code> and <code>--db<\/code> arguments optional in command-line REPL, and much more.
- **2022-08-24** · [No. 1 GitHub trending repository!](2022/08/no-1-github-trending-repository.md)  
  `community` — Absolutely shocked and honoured to reach the No. 1 trending public repository on GitHub worldwide. Thank you to everyone who has shown interest in SurrealDB and helped us reach 2500 GitHub stars!
- **2022-08-22** · [No. 1 on Reddit's Programming subreddit 🔥 'Hot' list](2022/08/no-1-on-reddits-programming-subreddit--hot-list.md)  
  `community` — Thank you for all the comments, feedback and support on the SurrealDB post on Reddit's 4.5 million member-strong Programming subreddit. We are honoured to have made No. 1 on the 🔥 'Hot' list.
- **2022-08-22** · [Honoured to be #4 on the front page of Hacker News](2022/08/honoured-to-be-4-on-the-front-page-of-hacker-news.md)  
  `community` — Wow!!! We really can't believe this!!! We are absolutely buzzing to make it onto the front page of Hacker News, and to get to number 4, no less! 😍
- **2022-08-20** · [SurrealDB on Reddit Rust](2022/08/surrealdb-on-reddit-rust.md)  
  `community` — Thank you for all the comments, feedback and support on the SurrealDB post on Reddit's Rust subreddit. We are honoured to have made the 🔥 'Hot' list.
- **2022-08-13** · [Release v1.0.0-beta.6](2022/08/release-v1-0-0-beta-6.md)  
  `releases` — Add command-line SurrealQL REPL for quick querying of a database, log username at server startup when root authentication is enabled, enable SurrealDB server to be configured using environment variables, implement config definition key and value caching within a transaction, and much more.
- **2022-08-05** · [Thank you!](2022/08/thank-you.md)  
  `community` — Thank you to our SurrealDB stargazers for helping us pass 100 GitHub stars! It’s early days, but we greatly appreciate it!
- **2022-08-04** · [Indie Hackers launch](2022/08/indie-hackers-launch.md)  
  `company` — Thank you for all the comments, feedback and support on our SurrealDB 'launch' post on IndieHackers.com. We are honoured to have made the 'Popular' list!
- **2022-08-04** · [Client libraries live!](2022/08/client-libraries-live.md)  
  `engineering` — We’re happy to announce that initial server side documentation for Node.js, Golang and Deno, along with client side documentation for JavaScript is LIVE!
- **2022-08-03** · [Why use SurrealDB?](2022/08/why-use-surrealdb.md)  
  `tutorials` — SurrealDB is an innovative NewSQL cloud database, suitable for serverless applications, jamstack applications, single-page applications, and traditional applications. It is unmatched in its versatility and financial value, with the ability for deployment on cloud, on-premise, embedded, and edge computing environments.
- **2022-08-01** · [Release v1.0.0-beta.5](2022/08/release-v1-0-0-beta-5.md)  
  `releases` — Temporarily disable HTTP response compression, improve <code>surreal import<\/code> and <code>surreal export<\/code> cli commands, and more...
- **2022-07-28** · [Release v1.0.0-beta.4](2022/07/release-v1-0-0-beta-4.md)  
  `releases` — Add new strict mode to SurrealDB server, ensure default table permissions are set to <code>NONE<\/code> not <code>FULL<\/code>, and more...
- **2022-07-24** · [Release v1.0.0-beta.3](2022/07/release-v1-0-0-beta-3.md)  
  `releases` — Log root authentication configuration status on server startup, ensure CORS headers are set on all HTTP responses even when request fails with an error, and more...
- **2022-07-21** · [Documentation is live](2022/07/documentation-is-live.md)  
  `company` `releases` — We’re happy to announce that our SurrealDB Documentation is LIVE! Installation, setup, datatypes, querying, connectivity, advanced functionality. It's all here.
- **2022-07-20** · [Dreaming of something better](2022/07/dreaming-of-something-better.md)  
  `company` `featured` — WE ARE LIVE!!! After 7 years of conceptualising, planning, designing and developing, our #opensource scalable cloud graph database SurrealDB is now in open beta to the world!
- **2022-07-20** · [Release v1.0.0-beta.2](2022/07/release-v1-0-0-beta-2.md)  
  `releases` — Improve command-line logging output, enable new <code>--log<\/code> argument for specifying server log level, hide default randomly-generated server password, and more...
