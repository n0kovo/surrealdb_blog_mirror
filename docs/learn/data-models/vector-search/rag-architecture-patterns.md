---
position: 5
title: RAG architecture patterns
description: Map retrieval-augmented generation to SurrealDB using chunk storage, embeddings, hybrid search, filters, and operational concerns for RAG.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/data-models/vector-search/rag-architecture-patterns.mdx"
---

# RAG architecture patterns

Retrieval-augmented generation (RAG) combines retrieval from your own data with generation from a language model. Instead of relying only on the model’s training data, you ground answers in chunks of text (and sometimes structured facts) that you control. SurrealDB is then used for storage and retrieval, allowing you to keep chunk text, metadata, access rules, and vector embeddings in one database and query them with SurrealQL.

## What RAG changes

A plain LLM call answers from parametric memory only. RAG adds a knowledge plane to this, in which documents are split into chunks, each chunk gets an embedding from a model you choose, and at query time you retrieve the most relevant chunks before (or while) the LLM writes an answer.

## Typical pipeline stages

1. Ingest: Load sources (files, web pages, tickets, database exports).
2. Chunk: Split text into segments with stable boundaries (headings, paragraphs, token limits) and optional overlap so ideas are not split awkwardly.
3. Embed: Call an embedding API or local model; store the resulting vector with each chunk. See [Embedding pipelines](embedding-pipelines.md) and the [embeddings integrations](../../../build/integrations/embeddings-providers/fastembed.md) for options outside the database.
4. Index: Define [vector indexes](vector-indexes.md) (for example HNSW) on embedding fields, and optionally [full-text indexes](../full-text-search/overview.md) on chunk text for lexical search.
5. Retrieve: For a user question, embed the query (or use the same model family as the corpus), run similarity search, optionally fuse with keyword results (see [Hybrid search](hybrid-search.md)).
6. Generate: Pass the top chunks as context to the LLM, with instructions to cite or stay within that context.

## Retrieval patterns

- Dense retrieval: KNN over embeddings with [`vector::distance::knn()`](../../../reference/query-language/functions/database-functions/vector.md#vectordistanceknn) and the patterns in [Similarity search](similarity-search.md). Good for paraphrases and conceptual match.
- Hybrid retrieval: Combine dense scores with [full-text search](../full-text-search/overview.md) when exact product names, error codes, or legislation matter; use [`search::rrf()`](hybrid-search.md) or related helpers as described under [Hybrid search](hybrid-search.md).

Re-ranking (a second model that scores the top *k* candidates) is often implemented in the application layer; SurrealDB supplies the candidate set efficiently.

## Chunking, metadata, and citations

There is no single best chunk size: smaller chunks improve precision but lose surrounding context; larger chunks add context but dilute embeddings. Many teams store title, heading path, or summary fields to improve retrieval without inflating the embedded body.

For citations, persist enough metadata to map a chunk back to a human-readable source (page, anchor, ticket id). The LLM should only “see” what you retrieved; clear provenance reduces hallucinated references.

## Operations and quality

- Embedding model changes usually require re-embedding the corpus or maintaining a version dimension; plan migrations before switching dimensions or distance metrics.
- Staleness: when sources update, replace or invalidate affected chunks so answers do not quote obsolete text.
- Evaluation: track retrieval hit rate, user thumbs-up/down, or offline benchmarks on labelled questions.

## Resources

- [Vector search cheat sheet](vector-indexes.md#vector-search-cheat-sheet)
- [Vector search overview](overview.md)
- [Hybrid search](hybrid-search.md)
- [Full-text search overview](../full-text-search/overview.md)
- [Embedding pipelines](embedding-pipelines.md)
- [Vector functions](../../../reference/query-language/functions/database-functions/vector.md#vector-functions)
- [Vector search indexes](../../../reference/query-language/statements/define/indexes.md#vector-search-indexes)
- [FastEmbed and embeddings integrations](../../../build/integrations/embeddings-providers/fastembed.md)
- [YouTube: Vector search intro](https://www.youtube.com/watch?v=MqddPmgKSCs)
