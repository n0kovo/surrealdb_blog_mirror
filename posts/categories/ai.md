# Category: ai

_53 posts_  
[← Index](../../README.md)

- **2026-09-08** · [Multi-hop graph traversal inside SurrealDB](../2026/09/multi-hop-graph-traversal-inside-surrealdb.md)  
  `tutorials` `ai` — Move breadth-first search into SurrealDB: recursive traversal with a depth range, predicates pushed into every hop, and what EXPLAIN says about edge indexes.
- **2026-09-03** · [Why does my vector search return nothing when I add a filter?](../2026/09/why-does-my-vector-search-return-nothing-when-i-add-a-filter-2.md)  
  `ai` `tutorials` — A filter applied after an HNSW walk can only remove rows, so a selective one comes back empty. Three measured SurrealDB fixes, plus the schema that avoids them.
- **2026-09-03** · [Announcing the Mastra integration for SurrealDB and Agent Memory](../2026/09/announcing-the-mastra-integration-for-surrealdb-and-agent-memory.md)  
  `releases` `ai` — One package gives Mastra agents a single database for conversations, workflow state, observability and vectors, plus managed memory that extracts and semantically recalls facts.
- **2026-08-27** · [Building a filesystem-based agent memory on SurrealDB](../2026/08/agent-memory-is-a-filesystem-building-one-on-surrealdb.md)  
  `tutorials` `ai` — Give an AI agent persistent memory as a filesystem in SurrealDB: computed file paths, fused full-text and vector search, and RBAC in a single PERMISSIONS clause
- **2026-08-13** · [Graph engineering is missing a graph](../2026/08/graph-engineering-is-missing-a-graph.md)  
  `featured` `engineering` `ai` — Graph engineering stops at the diagram. The harder half is the context graph underneath: whether relations, vectors and memory share one consistency boundary.
- **2026-08-05** · [Chat with your meeting notes: CocoIndex graph with SurrealQL](../2026/08/chat-with-your-meeting-notes-a-cocoindex-knowledge-graph-and-a-text-to-surrealql-agent.md)  
  `tutorials` `ai` — A folder of Markdown meeting notes becomes a self-maintaining knowledge graph in SurrealDB with CocoIndex and Pydantic AI, fenced in by a database role.
- **2026-08-05** · [Empower your agents with the new SurrealDB MCP](../2026/08/surrealmcp-a-managed-mcp-server-for-ai-agents.md)  
  `featured` `releases` `tutorials` `ai` — The SurrealMCP server lets you add one URL to any AI tool, sign in with your Surreal ID, and deploy, query, and look after your SurrealDB Cloud account.
- **2026-07-30** · [Embedding models comparison: OpenAI, Google, Qwen, Nomic, more](../2026/07/embedding-models-comparison.md)  
  `ai` — A practical guide to eight embedding models — text-embedding-3-small\/large, gemini-embedding-001, embeddinggemma-300m, qwen3-embedding, and more.
- **2026-07-29** · [One database for the whole claim: agentic claims on SurrealDB](../2026/07/one-database-for-the-whole-claim-agentic-claims-triage-on-surrealdb.md)  
  `ai` `tutorials` — An AI agent triaging insurance claims needs semantic, graph, and document data. Do it in one SurrealDB database.
- **2026-07-27** · [Even a jailbroken LLM can't exceed its database permissions](../2026/07/even-a-jailbroken-llm-cant-exceed-its-database-permissions-heres-how.md)  
  `ai` `tutorials` — AI agents an be talked into modifying your data with a single polite request. SurrealDB's role-based access control lives in the data layer the LLM can't reach.
- **2026-07-21** · [Modelling a financial services enterprise ontology in SurrealDB](../2026/07/modelling-a-financial-services-enterprise-ontology-in-surrealdb.md)  
  `ai` `tutorials` — Model a financial services ontology in SurrealDB: map ownership, custody, and transactions as a graph and resolve beneficial-ownership chains in one query.
- **2026-07-15** · [Temporal graph traversal: incident response in one query language](../2026/07/your-asset-inventory-is-a-graph-query-it-like-one.md)  
  `tutorials` `ai` — Model your security assets as a graph in SurrealDB and use the VERSION clause to time-travel through incidents. Schemas, seed data, and queries included.
- **2026-07-14** · [One query, not two stores: how SurrealDB makes agents accurate](../2026/07/one-query-not-two-stores-how-vector-graph-in-surrealdb-makes-agents-more-accurate.md)  
  `ai` `tutorials` — Vector search and graph traversal in a single SurrealDB query. How single-engine hybrid retrieval makes RAG agents more accurate.
- **2026-07-09** · [Generating embeddings inside SurrealQL with a custom function](../2026/07/generating-embeddings-inside-surrealql-with-a-custom-function.md)  
  `ai` `tutorials` — Define a custom SurrealQL function to call any embedding API, then run semantic search, graph traversal and field shaping in one query
- **2026-07-01** · [Bring SurrealDB to your Replit Agent](../2026/07/bring-surrealdb-to-your-replit-agent.md)  
  `tutorials` `ai` `featured` — SurrealDB's MCP server lets Replit Agent build apps directly on a database you own, reading your schema and querying live data.
- **2026-06-22** · [Build apps on your data with SurrealDB and Lovable](../2026/06/build-apps-on-your-data-with-surrealdb-and-lovable.md)  
  `tutorials` `featured` `ai` — Connect SurrealDB to Lovable using the Model Context Protocol (MCP) to read your schema, query your live data, and build a working application on top of it.
- **2026-05-19** · [Agentic retrieval for structured data with text-to-surql](../2026/05/agentic-retrieval-for-structured-data-with-text-to-surql.md)  
  `ai` `tutorials` — An agentic pattern overview for structured retrieval that gives an LLM agent a database-aware tool that converts natural-language questions into valid SurrealQL
- **2026-05-12** · [What chunking strategies exist and how to choose one?](../2026/05/what-chunk-strategies-exist-and-how-to-choose-one.md)  
  `ai` — If you've decided to chunk documents for a RAG pipeline or semantic search system, the next question hits immediately: which chunking strategy should I use?
- **2026-05-08** · [What is the recommended chunk size?](../2026/05/what-is-the-recommended-chunk-size.md)  
  `ai` — What chunk size to one when building a RAG (Retrieval-Augmented Generation) pipeline, a semantic search system, or AI app that reads from a vector store?
- **2026-04-30** · [Hybrid search inside SurrealDB](../2026/04/hybrid-search-inside-surrealdb.md)  
  `ai` — How Júlia Sala-Bayo and Archie Marshall fused vector and keyword retrieval in a single query.
- **2026-04-27** · [Building compounding memory with knowledge graphs and agentic RAG](../2026/04/building-compounding-memory-with-knowledge-graphs-and-agentic-rag.md)  
  `community` `ai` — Synapse, a memory-first reflection agent, helps users track therapy journal patterns. It structures insights into a knowledge graph to revealing patterns.
- **2026-04-17** · [Graph RAG does not need a graph database](../2026/04/graph-rag-does-not-need-a-graph-database-it-needs-a-database-that-does-everything.md)  
  `featured` `ai` — Graph RAG is the right idea, but what matters is whether graph traversal, vector and full-text search, and filters compose in a single atomic statement.
- **2026-03-28** · [How to get near-perfect, deterministic accuracy from your agents](../2026/03/how-to-get-near-perfect-deterministic-accuracy-from-your-ai-agents.md)  
  `featured` `ai` — Agent accuracy problems are almost always retrieval, not model problems. Scope-first retrieval and reasoning and retrieval graph feedback loops close the gap.
- **2026-02-05** · [How to build a knowledge graph for AI](../2026/02/how-to-build-a-knowledge-graph-for-ai.md)  
  `featured` `tutorials` `ai` — What is a knowledge graph and how can it be used to enhance AI agents?
- **2026-01-29** · [Knowledge Graph RAG: two query patterns for smarter AI agents](../2026/01/knowledge-graph-rag-two-query-patterns-for-smarter-ai-agents.md)  
  `featured` `tutorials` `ai` — A post that walks through two powerful SurrealQL query patterns that demonstrate how to retrieve context from a knowledge graph to feed AI agents.
- **2025-12-17** · [Agents with memory: how Agno and SurrealDB enable reliable AI](../2025/12/agents-with-memory-how-agno-and-surrealdb-enable-reliable-ai-systems.md)  
  `featured` `ai` — Highlights from our Agno x SurrealDB livestream on building reliable, context-rich agents with a strong memory layer.
- **2025-12-17** · [PolyAI on building context-aware voice agents on SurrealDB Stream](../2025/12/polyai-on-building-context-aware-voice-agents-latency-knowledge-bases-and-what-actually-ships.md)  
  `featured` `ai` `events` — SurrealDB Stream with PolyAI CTO Shawn Wen on the hard parts of context-aware voice agents: latency budgets, knowledge governance, and operational trust.
- **2025-10-29** · [Exploring the new SurrealDB integration with Agno](../2025/10/exploring-the-new-surrealdb-integration-with-agno.md)  
  `featured` `tutorials` `ai` — Introducing the new SurrealDB integration with Agno along with examples from the Agno Cookbook.
- **2025-10-09** · [Bring your own knowledge base: Agent Studio meets SurrealDB](../2025/10/bring-your-own-knowledge-base-agent-studio-meets-surrealdb.md)  
  `featured` `ai` `community` — How the RAG provider Agent Studio from PolyAI integrates with SurrealDB.
- **2025-09-30** · [From Knowledge Graph to RAG for Stablecoin Regulatory Intel](../2025/09/from-knowledge-graph-generation-to-rag-for-stablecoin-regulatory-intelligence.md)  
  `featured` `ai` `community` — We’re excited to share this community-written deep dive by Sugi Venugeethan into Stablebridge, a project tackling the complex world of stablecoin regulation.
- **2025-09-03** · [Power your AI workflows with the official SurrealDB x n8n node](../2025/09/power-up-your-ai-workflows-the-official-surrealdb-x-n8n-node-is-here.md)  
  `featured` `tutorials` `engineering` `ai` — The SurrealDB node for n8n is a 1st-party, production-ready integration that lets you query, create, update,, and delete SurrealDB data from any n8n workflow
- **2025-08-27** · [Multi-tool agent with SurrealMCP and Agno](../2025/08/multi-tool-agent-with-surrealmcp-and-agno.md)  
  `featured` `tutorials` `ai` — Using SurrealMCP and Agno, this is how you can build a “researcher” agent that finds information on the web, structures the data, and stores it in SurrealDB.
- **2025-08-23** · [Introducing SurrealMCP for SurrealDB users](../2025/08/introducing-surrealmcp.md)  
  `featured` `releases` `ai` — SurrealDB has launched SurrealMCP, giving AI agents secure, real-time, permission-aware memory powered by its multi-model database.
- **2025-08-22** · [Using unstructured data to create knowledge graphs in SurrealDB](../2025/08/using-unstructured-data-to-create-knowledge-graphs-in-surrealdb.md)  
  `featured` `tutorials` `ai` — There are many ways to give structure to unstructured data so that it can be used systematically in a database.
- **2025-08-11** · [Multi-model RAG with LangChain](../2025/08/multi-model-rag-with-langchain.md)  
  `featured` `tutorials` `ai` — A walkthrough of a multi-model RAG pipeline with LangChain and SurrealDB, combining vector search with lightweight graph retrieval over chat conversations.
- **2025-08-07** · [Terminal hybrid vector + text search with SurrealDB and Ratatui](../2025/08/hybrid-vector-text-search-in-the-terminal-with-surrealdb-and-ratatui.md)  
  `featured` `tutorials` `ai` — Building an AI-native UI for the terminal that demonstrates newly added hybrid search that combines vector with full-text queries into a single result.
- **2025-07-30** · [Beyond basic RAG: a multi-cycle reasoning engine on SurrealDB](../2025/07/beyond-basic-rag-building-a-multi-cycle-reasoning-engine-on-surrealdb.md)  
  `tutorials` `featured` `ai` — Standard RAG models operate on single shots. The Reflexion RAG Engine overcomes this through a multi-cycle, self-correcting architecture powered by SurrealDB.
- **2025-07-29** · [Building an AI-native multi-model UI with SurrealDB](../2025/07/building-an-ai-native-multi-model-ui-with-surrealdb.md)  
  `featured` `tutorials` `ai` — Schema definition in SurrealDB is a powerful thing, and the more you know the more you can make your schema work for you.
- **2025-07-09** · [Make a medical chatbot using GraphRAG with SurrealDB + LangChain](../2025/07/make-a-medical-chatbot-using-graphrag-with-surrealdb-langchain.md)  
  `featured` `engineering` `ai` — Build a medical chatbot with GraphRAG, SurrealDB, and LangChain using Rust.
- **2025-07-07** · [Semantic search in Rust with SurrealDB and Mistral AI](../2025/07/semantic-search-in-rust-with-surrealdb-and-mistral-ai.md)  
  `featured` `engineering` `ai` — SurrealDB's built-in vector search capabilities make it a perfect match for semantic search using Mistral AI
- **2025-07-04** · [Minimal LangChain chatbot example with vector and graph](../2025/07/minimal-langchain-chatbot-example-with-vector-and-graph.md)  
  `featured` `tutorials` `ai` — Build a chatbot that understands context with a minimal LangChain example that uses vector stores and graphs to generate intelligent, natural language answers.
- **2025-07-01** · [Announcing our official LangChain integration](../2025/07/announcing-our-official-langchain-integration.md)  
  `engineering` `featured` `ai` — We’re thrilled to announce SurrealDB's official integration with LangChain, one of the most popular frameworks for building powerful LLM-driven applications.
- **2025-06-30** · [Make a GenAI chatbot using GraphRAG with SurrealDB + LangChain](../2025/06/make-a-genai-chatbot-using-graphrag-with-surrealdb-langchain.md)  
  `featured` `tutorials` `ai` — Build a GenAI chatbot with GraphRAG, SurrealDB, and LangChain for accurate, graph-enhanced LLM responses; code examples provided.
- **2025-06-27** · [The state of Agentic AI and the need for Agentic Memory](../2025/06/the-state-of-agentic-ai-and-the-need-for-agentic-memory.md)  
  `company` `featured` `ai` — The paradigm shift we are at with agentic AI and the role SurrealDB plays in empowering it.
- **2025-06-26** · [Semantic search with SurrealDB and OpenAI](../2025/06/semantic-search-with-surrealdb-and-openai.md)  
  `featured` `engineering` `ai` — SurrealDB's built-in vector search capabilities make it a perfect match for semantic search using OpenAI
- **2025-06-24** · [Building real-time AI pipelines in SurrealDB](../2025/06/building-real-time-ai-pipelines-in-surrealdb.md)  
  `tutorials` `featured` `ai` — Say goodbye to complex ETL pipelines with SurrealDB's multi-model approach.
- **2025-06-20** · [What are knowledge graphs and why is everyone talking about them?](../2025/06/what-are-knowledge-graphs-and-why-is-everyone-talking-about-them.md)  
  `tutorials` `featured` `ai` — Knowledge graphs provide the structured memory AI agents need for context-aware reasoning. Learn how this decades-old concept became essential infrastructure.
- **2025-06-17** · [How to simplify Graph RAG using Amazon Bedrock and SurrealDB](../2025/06/how-to-simplify-a-graph-rag-architecture-using-amazon-bedrock-and-surrealdb.md)  
  `featured` `tutorials` `ai` — A typical RAG pipeline forces you to juggle a vector store, a document store, a graph store, plus an LLM endpoint. SurrealDB and Amazon Bedrock end that sprawl.
- **2025-06-17** · [RAG can be Rigged: building a context-aware agent that just works](../2025/06/rag-can-be-rigged.md)  
  `featured` `engineering` `ai` — Building a smart knowledge agent with SurrealDB and Rig.rs: a context-aware support agent that just works.
- **2025-04-02** · [Cooking up faster RAG using in-database embeddings in SurrealDB](../2025/04/cooking-up-faster-rag-using-in-database-embeddings-in-surrealdb.md)  
  `engineering` `ai` — Speed up RAG pipelines by running embedding models inside SurrealDB.Eliminate API latency with in-database vector embeddings for retrieval-augmented generation.
- **2025-03-26** · [Beyond black boxes: customisable and secure financial RAG systems](../2025/03/beyond-black-boxes--building-customisable-and-secure-rag-systems-for-financial-services.md)  
  `engineering` `ai` — A blog post that tackles the specific challenges financial services data teams face when building systems in regulated, data-sensitive environments.
- **2025-02-21** · [Automating knowledge graphs with SurrealDB and Gemini](../2025/02/automating-knowledge-graphs-with-surrealdb-and-gemini.md)  
  `engineering` `ai` — How to use SurrealDB with Gemini to automate knowledge graphs to move beyond simple storage and retrieval.
- **2025-01-31** · [Enhancing retrieval-augmented generation with SurrealDB](../2025/01/enhancing-retrieval-augmented-generation-with-surrealdb.md)  
  `tutorials` `featured` `ai` — GraphRAG: Enhancing Retrieval-Augmented Generation with SurrealDB, Gemini and DeepSeek
