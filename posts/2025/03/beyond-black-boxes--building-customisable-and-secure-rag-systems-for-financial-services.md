---
title: "Beyond black boxes - building customisable and secure RAG systems for financial services"
slug: "beyond-black-boxes--building-customisable-and-secure-rag-systems-for-financial-services"
date: "2025-03-26T00:00:00.000Z"
categories:
  - "engineering"
  - "ai"
read_time: "13 min read"
summary: "This isn’t just another RAG blog post - it tackles the specific challenges financial services data teams face when building systems in regulated, data-sensitive environments."
source: "https://surrealdb.com/blog/beyond-black-boxes--building-customisable-and-secure-rag-systems-for-financial-services"
cover: "../../assets/37712b5ccdf5e9f7.jpg"
---

# Beyond black boxes - building customisable and secure RAG systems for financial services

![Beyond black boxes - building customisable and secure RAG systems for financial services](../../assets/37712b5ccdf5e9f7.jpg)

Imagine a financial analyst looking for stocks to trade, or investigating potential insider trading. They have mountains of data: SEC filings, news articles, internal communications, trading records. Traditional RAG systems are like that analyst, diligently analysing individual pieces of information, but often missing *crucial connections* that lie hidden *between* the data points - relationships that could reveal suspicious activity. Those missed connections could mean the difference between compliance and a costly regulatory violation, or between a profitable trade and a missed opportunity.

Now, imagine that same analyst with a powerful tool - a system that not only understands the *content* of each document, but also the *relationships* between companies, executives, transactions, and news events. Suddenly, the analyst can see the bigger picture, identify hidden patterns, uncover non-obvious correlations, and generate insights that would be impossible to find otherwise. This isn't just about faster search; it's about *deeper understanding*. This is the power of combining retrieval-augmented generation (RAG) with the relational capabilities of a graph database, all within a single, secure, and *controllable* platform: SurrealDB.

This isn't just another blog post about RAG. This is about addressing the *specific* challenges faced by financial services data scientists and technologists who are tasked with building and deploying these systems in a highly regulated, data-sensitive environment. If you're handling fragmented data architectures, security concerns, the limitations of "black box" AI, and the constant need to adapt to evolving regulations and business needs, then this is for you. We'll explore how SurrealDB empowers financial institutions to build RAG systems that go beyond the limitations of traditional approaches, giving you the tools to experiment, fine-tune, maintain full control over your data and your models, and ultimately, gain a competitive edge.

The project in this post focuses on the fundamentals of traditional RAG and prompt engineering from a financial point of view. The platform it’s built on naturally extends to more advanced techniques, like the GraphRAG approach detailed in our previous post: *enhancing retrieval-augmented generation with SurrealDB*.

## Why "black box" AI isn't enough for finserv - and the crippling pain of traditional RAG architectures

The promise of RAG is immense: to empower your team with AI-driven insights derived from your vast and complex data holdings. But the reality of implementing RAG in a financial institution is often far more challenging than the demos suggest. Many RAG solutions rely on large, pre-trained models hosted by third-party providers (like OpenAI, Google, or Meta). While convenient, these "black box" solutions raise serious, and often insurmountable, concerns for financial institutions:

- **Data security and privacy - paramount concerns.** Sending sensitive financial data - customer information, trading strategies, internal analyses - to external APIs creates *unacceptable* compliance and security risks. You lose direct control over where your data resides, how it's processed, and who has access to it. This is a non-starter for most financial institutions.
- **Lack of customisation - financial data is unique.** Pre-trained, general-purpose models are not optimised for the specific nuances of financial terminology, the intricate structures of regulatory filings (10-Ks, 10-Qs, prospectuses), or the specialised language used in internal documents and communications. Fine-tuning options are often limited, leaving you with a system that doesn't fully understand the *context* of your data.
- **Transparency and explainability - a regulatory imperative.** In the financial world, "because the AI said so" is not an acceptable answer. You need to understand *why* a RAG system produces a particular result. This is crucial for auditability, regulatory compliance (think model risk management), and building trust in the system. Opaque, "black box" models make this difficult, if not impossible, creating significant operational and legal risks.

![ChatGPT](../../assets/f26879007a78d5fa.jpg)

- **Vendor lock-in and lack of control.** Relying on a single, external provider creates dependencies and limits your flexibility. You're at the mercy of their pricing, their roadmap, and their security practices.

But let's say you decide to tackle the challenge of bringing the models in-house, to maintain control. Even then, traditional RAG architectures present a *daunting* set of technical hurdles:

- **Database fragmentation - a jigsaw puzzle of data.** You're forced to assemble a complex system from disparate parts. You need a vector database (like Pinecone, Weaviate, or Qdrant) to store and search the embeddings of your documents. You need a document store (perhaps MongoDB, a cloud storage service, or even a traditional relational database) to hold the actual text of your documents. And, if you want to leverage relationships between entities (companies, people, transactions), you likely need a *third* database, a graph database like Neo4j. This fragmentation creates a logistical and engineering nightmare.
- **API overload - a tangled web of connections.** Each of these databases requires its own API, its own set of connection strings, its own authentication and authorisation mechanisms. Managing this complexity is a significant burden, increasing the risk of errors, security vulnerabilities, and operational overhead. Just keeping track of all the credentials and ensuring consistent access control is a full-time job.
- **Data silos and latency - the enemy of real-time insights.** Moving data between these disparate systems introduces significant latency. You can't perform real-time analysis because you're constantly copying and synchronising data between databases. This creates opportunities for inconsistencies, stale data, and delays in getting insights to decision-makers. In the fast-paced world of finance, delays can be costly.
- **Complex orchestration - the hidden cost.** You need a separate orchestration layer - typically a complex set of Python scripts or a dedicated workflow engine - to manage the flow of data between these different components. This adds *another* layer of complexity, requiring specialised expertise to develop, maintain, and debug. This orchestration layer becomes a critical point of failure and a significant source of technical debt.

The result? A RAG system that is fragile, expensive to maintain, difficult to scale, and slow to adapt to changing business needs. You're spending more time wrestling with infrastructure than you are extracting value from your data.

## The SurrealDB advantage: RAG your way - unified, secure, customisable, and *fast*

SurrealDB offers a fundamentally different approach. It's not just *another* database; it's a *unified data platform* designed to eliminate the complexity and pain points of traditional RAG architectures. SurrealDB's unique architecture provides several key advantages for building RAG systems in the financial services sector:

- **Unified data platform - the power of one.** Unlike traditional setups, SurrealDB handles vectors, documents, and relationships, *and* structured data *within a single database*. This is the core differentiator. It eliminates the need for complex ETL processes, drastically reduces latency (because data doesn't have to travel between different systems), and simplifies your entire architecture. Imagine the simplicity of writing a *single* query to retrieve semantically similar documents, traverse relationships, *and* filter based on structured data - all without leaving the database.
- **Vector search + graph + documents + flexible relational data - all in one place.** SurrealDB combines the power of semantic similarity (vector search) with the contextual understanding of graph databases, the flexibility of document stores, *and* the power of traditional relational queries, all in one. You’ll see this in practice in the next section which contains an SEC Edgar filings example, in which we store structured JSON data in the `additional_data` field alongside the document text and embeddings. This allows you to perform queries that combine semantic search with precise filtering on structured fields, like company names, filing dates, auditor information, or specific financial metrics. You aren't limited to pre-defined relationships; you can query *any* structured data associated with your documents, giving you unprecedented flexibility and analytical power. And, as demonstrated in our previous blog post, this foundation readily extends to support *full GraphRAG* capabilities.
- **Full data control - your data, your rules.** You choose where to run SurrealDB: on-premises, in your private cloud, or even locally on a developer's machine. Your data *never* leaves your control unless *you* explicitly choose to integrate with an external API. This is absolutely crucial for meeting stringent data security and compliance requirements in the financial industry. You have complete control over your data residency, access controls, and audit trails.
- **Customisable embeddings and LLMs - no more black boxes.** You're not locked into a single embedding model or LLM. Experiment with OpenAI ([OpenAI embeddings documentation](https://platform.openai.com/docs/guides/embeddings)), GloVe ([GloVe project page](https://nlp.stanford.edu/projects/glove/)), or even train your *own* custom embeddings, fine-tuned on your internal financial data, to achieve superior accuracy and relevance. Integrate with locally hosted LLMs (via Ollama - [Ollama](https://ollama.ai/), [Ollama model library](https://ollama.ai/library)) for maximum control and privacy, eliminating the need to send *any* sensitive data to external providers. You have the freedom to choose the tools that best fit your needs and risk tolerance.
- **SurrealQL - power and flexibility and the language of data.** SurrealDB's query language, SurrealQL, is designed for the modern data landscape. It allows you to perform complex data retrieval, manipulation, and transformation *directly within the database*. You can even make HTTP requests to external LLM APIs (like Gemini ([Google AI studio](https://ai.google.dev/)) or OpenAI ([OpenAI developer quickstart](https://platform.openai.com/docs/quickstart))) from within SurrealQL, giving you the option to leverage cloud-based models when appropriate, while maintaining control over when and how your data leaves your environment.
- **Data layer computation - the future of RAG.** By running your embeddings *within* SurrealDB, you're not just simplifying your architecture; you're preparing for the future. This enables the possibility of running the LLM *itself* within the same data layer, eliminating the need to move data back and forth between the database and the application. This reduces latency to near-zero, opening up possibilities for real-time, interactive RAG applications that were previously unthinkable.

## Practical example: SEC filings and insider trading detection - unleashing the power of combined data

Let's see how this works in practice with a concrete example. The provided code includes examples for working with SEC Edgar filings (10-K, 10-Q, 8-K, etc.). You can:

1. **Download and process filings.** Use the `download_edgar` script, specifying form types, tickers, and date ranges. This script leverages the `edgartools` library ([https://github.com/dgunning/edgartools](https://github.com/dgunning/edgartools)) to efficiently retrieve data from the SEC EDGAR database.

1. **Generate embeddings.** Create vector embeddings of the text content using OpenAI's `text-embedding-ada-002` or GloVe. You have the flexibility to choose the model that best suits your needs, or even train your own.

1. **Store data in SurrealDB - the unified approach.** Load the filings, embeddings, *and* relationships into SurrealDB. Critically, alongside the document text and embeddings, we also store *structured* JSON data in the `additional_data` field. This field contains key metadata extracted from the filings, such as the company's CIK (central index key), the filing date, the fiscal year and period, the auditor, and more. This structured data is *just as accessible* as the text and embeddings, allowing for powerful combined queries.

1. **Build a RAG-powered application.** Use the included FastAPI application to ask sophisticated questions that leverage *all* aspects of the data:

- **Combining graph, semantic, and structured data.** "Show me all companies mentioned in recent 10-K filings that also have connections to [company x] in our internal relationship graph, *and* where the `additional_data.industry` field is 'pharmaceutical preparations'."
- **Semantic search with precise filtering.** "Summarise the risk factors related to [specific topic] across all 10-Q filings for [industry sector], \*filtering for filings where `additional_data.fiscal_year` is 2023 and `additional_data.fiscal_period` is 'Q3'."
- **Advanced pattern detection.** "Identify any unusual changes in executive compensation mentioned in recent filings, compared to historical data, *specifically looking at companies where `additional_data.cik` is in [list of CIKs] and where the sentiment analysis of the compensation discussion is negative*."

By combining vector search (for semantic similarity), graph relationships (for contextual understanding), and flexible relational queries on structured JSON data, you can uncover hidden connections, patterns, and anomalies that would be impossible to find with traditional, siloed approaches. This allows for far more precise, powerful, and insightful analysis, leading to better decision-making and reduced risk. And, because SurrealDB is designed for relationships, you can easily extend this example to incorporate *true* graph relationships (as described in the [enhancing retrieval-augmented generation with SurrealDB](/blog/enhancing-retrieval-augmented-generation-with-surrealdb) blog post) for even more powerful analysis.

## Experimentation and customisation: the key to effective RAG, *without* the re-embedding headaches

The provided code is designed to be a starting point for *rapid* experimentation and iterative development. You can easily:

- **Test different embedding models.** Compare the performance of OpenAI embeddings versus GloVe, or integrate your own custom-trained financial embedding model - *without having to re-embed your entire dataset every time you switch*. This is a *huge* time-saver and a major advantage of SurrealDB's unified architecture.
- **Integrate different LLMs.** Use API-hosted models like OpenAI's ChatGPT and Google's Gemini, or run local LLMs via Ollama for complete data privacy. Switch between them with a simple configuration change, allowing you to evaluate the trade-offs between performance, cost, and control.
- **Adjust RAG parameters.** Fine-tune the number of retrieved chunks, similarity thresholds, and chat history inclusion to optimise performance for your specific use cases and data characteristics. All these parameters are controlled directly within the SurrealQL code, allowing for dynamic adjustments *without* redeploying your application or modifying any external configuration files. The relevant files are within the `surrealdb_rag/db/queries/` directory (although, remember, the specific file structure might evolve).
- **Engineer your prompts.** Craft prompts that elicit the most accurate, relevant, and insightful responses from your chosen LLM. The prompts, and different pre-canned prompts, can be modified directly in the web UI, allowing for real-time experimentation and iteration. You can quickly test different phrasing, instructions, and contextual information to see how they affect the LLM's output. The logic for prompt handling is also within `surrealdb_rag/db/queries/`.

## Conclusion: taking control of your AI future - and simplifying your data stack

In the highly regulated and data-sensitive world of financial services, "black box" AI is simply not good enough, and traditional, fragmented RAG architectures are too complex, inefficient, and costly. SurrealDB provides a powerful, flexible, and *unified* platform for building RAG systems that meet the unique demands of the industry: security, customisation, transparency, control, *and* simplified operations.

By combining vector search, graph databases, document storage, *and* flexible relational queries in a single platform, SurrealDB empowers you to unlock the true potential of your data, build AI solutions that are tailored to your specific needs, drastically reduce the complexity of your data stack, and gain a significant competitive advantage.

This isn't just about building a better chatbot; it's about building a more intelligent, more responsive, and more trustworthy financial institution. It's about empowering your analysts, researchers, and compliance officers with the tools they need to make better decisions, faster. It's about taking control of your AI future. Start experimenting today and discover the power of RAG, *your* way.

**Next steps:**

- **Clone the repository:** `git clone https://github.com/surrealdb/examples`
- **Install [SurrealDB](/install)** or **sign up to our [Cloud](/cloud)**
- **Explore the code:** dive into the `surrealdb_rag` directory to understand the implementation. Experiment with the different scripts and parameters.
- **Shout-outs:** this project builds upon and extends the original work by [Ce11an](https://github.com/Ce11an)
