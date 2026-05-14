---
title: "Crafting Our Full-Text Search in SurrealDB: A Journey Beyond Lucene and Tantivy"
slug: "crafting-our-full-text-search-in-surrealdb-a-journey-beyond-lucene-and-tantivy"
date: "2023-12-18T00:00:00.000Z"
categories:
  - "engineering"
read_time: "3 min read"
summary: "How SurrealDB built its own ACID-compliant full-text search engine instead of integrating Lucene or Tantivy, delivering a unified query experience without external dependencies."
source: "https://surrealdb.com/blog/crafting-our-full-text-search-in-surrealdb-a-journey-beyond-lucene-and-tantivy"
cover: "../../assets/50e561926e603a6a.jpg"
---

# Crafting Our Full-Text Search in SurrealDB: A Journey Beyond Lucene and Tantivy

![Crafting Our Full-Text Search in SurrealDB: A Journey Beyond Lucene and Tantivy](../../assets/50e561926e603a6a.jpg)

## Embracing Complexity for Simplified User Experience

To achieve an efficient and comprehensive search experience, it is pivotal to have a deep understanding of both the technology and user needs. At SurrealDB, we embarked on this journey with a clear goal: to create a solution that upholds the integrity and simplicity of our ACID SQL database while delivering unparalleled user experience.

![Emmanuel Keller](../../assets/ba87fa3f136cdcf1.jpg)

## The Crossroads: Lucene-Based Solutions and Rust Alternatives

Our efforts initially revolved around Lucene-based solutions like Solr, ElasticSearch, and the Java library. These established technologies offer robustness and efficiency, but integrating them would have necessitated an additional Java runtime, similar to MongoDB's approach with Atlas. Alternatively, the Rust-based solution, Tantivy, offered a modern and performance-oriented choice.

## The Dual Dilemmas: Language Disparity and Structural Challenges

Two primary concerns guided our decision-making process:

1. **Language Inconsistency**: Utilising Tantivy or Lucene would mean introducing a separate query language for full-text search, complicating the user experience by requiring fluency in two different query languages.
1. **Index Management in Distributed Environments**: Employing external libraries would cede control over the full-text index structure, posing challenges in distributed environments, crucial for scalability.

## ACID Compliance and Our Resolution

Neither Tantivy nor Lucene are inherently ACID-compliant, posing a significant challenge.

At SurrealDB, we view ACID (Atomicity, Consistency, Isolation, Durability) compliance not just as a feature, but as a fundamental pillar for database integrity and reliability. This commitment to ACID principles played a pivotal role in our decision to develop our own full-text search capabilities.

- **Atomicity and Consistency**: These principles ensure that every transaction in our database, including those involving full-text searches, is treated as a single unit. This means either the entire transaction succeeds or fails, maintaining data consistency even in complex scenarios where full-text search queries are combined with standard SQL operations.
- **Isolation**: By adhering to isolation, SurrealDB guarantees that concurrent transactions do not interfere with each other. This is particularly important in full-text search where frequent updates and queries occur. Isolation ensures that search results remain consistent and unaffected by other simultaneous transactions.
- **Durability**: Durability assures that once a transaction impacting full-text search is committed, it remains so, even in the event of a system crash. This reliability is crucial for maintaining up-to-date and accurate search indexes, which are key to the performance and utility of the full-text search feature.

Integrating full-text search capabilities while preserving these ACID properties ensures that our users experience not only powerful and flexible search functionality but also the reliability and trustworthiness that is synonymous with SurrealDB. By upholding these standards, we deliver a robust and consistent user experience, vital for applications that depend on the accuracy and integrity of their data.

## Looking Ahead with SurrealDB: Vector Search and Beyond

The successful implementation of our full-text search is just the beginning. SurrealDB is now gearing up for exciting advancements, including the support of vector search. This new feature will optimise exact (KNN) and approximate (ANN) neighbourhood queries, further enhancing our database's capabilities. Our journey into vector search represents our continuous commitment to innovation, delivering sophisticated yet user-friendly solutions.

As we move forward, SurrealDB remains dedicated to pushing the boundaries of database technology, ensuring that our users have access to the most advanced and reliable tools in the industry.

Stay tuned as we continue to redefine what's possible in the world of databases.

To try out [Full-Text search](/docs/surrealdb/models/full-text-search) for yourself, install [SurrealDB](/install) and check out our [beginner blog](/blog/create-a-search-engine-with-surrealdb-full-text-search) to get started. Do share your experience with us on [Discord](https://discord.com/invite/surrealdb).
