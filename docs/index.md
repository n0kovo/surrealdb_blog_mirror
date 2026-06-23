---
position: 0
title: Getting started
description: The official documentation for SurrealDB, a multi-model database for modern applications.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/index.mdx"
---

SurrealDB is a multi-model database designed to simplify building modern applications. It combines the capabilities of traditional relational databases, document stores, graph databases, and more into a single, unified platform. Whether you are building real-time applications, working with complex data relationships, or deploying AI-powered workflows, SurrealDB provides the tools you need without requiring multiple database systems.

## Learn

The SurrealDB documentation contains a large number of guides, each designed to address different aspects of database management and application development.

- **[Querying](learn/querying/index.md)** — Learn to query your data with SurrealQL, SDKs or GraphQL.
- **[Schema management](learn/schema-management/index.md)** — Learn how to shape data in SurrealDB using tables, fields, indexes, events, functions, and more.
- **[Data models](learn/data-models/index.md)** — Store and query document, graph, vector, time-series, and geospatial data with SurrealDB.
- **[Security](learn/security/index.md)** — Learn how to strengthen your SurrealDB deployment with best security practices.
- **[Spectron](https://surrealdb.com/docs/spectron)** — Learn how to use Spectron, the memory context for AI agents.
- **[Extensions](learn/extensions/index.md)** — Learn how to extend SurrealDB with custom modules and WASM plugins.

## Features

SurrealDB is built around a rich feature set that supports a wide variety of application requirements. Rather than requiring you to stitch together separate systems for different data models or capabilities, SurrealDB provides them all within a single engine.

- **[Real-time queries](learn/querying/real-time/live-queries.md)** — Subscribe to live queries and changefeeds for real-time data updates.
- **[Authentication](learn/security/authentication/overview.md)** — Built-in authentication and access control with scoped permissions.
- **[Graph relationships](learn/data-models/graph/overview.md)** — Model and traverse complex relationships using native graph edges.
- **[Vector search](learn/data-models/vector-search/overview.md)** — Store embeddings and perform similarity searches for AI and RAG workflows.
- **[Data migrations](explore/surrealist/index.md)** — Evolve your database schema over time with SurrealKit.
- **[Surrealist UI](explore/surrealist/index.md)** — A native UI to visually explore and manage your SurrealDB data.

## SDKs

SurrealDB offers official SDKs for popular languages, supporting queries, authentication, real-time updates, and in some cases, embedded use. See your chosen language’s docs for setup and examples.

- **[Go](languages/golang/index.md)**
- **[Java](languages/java/index.md)**
- **[JavaScript](languages/javascript/overview.md)**
- **[Kotlin](languages/kotlin/index.md)**
- **[Mojo](languages/mojo/index.md)**
- **[.NET](languages/dotnet/index.md)**
- **[PHP](languages/php/index.md)**
- **[Python](languages/python/index.md)**
- **[Rust](languages/rust/overview.md)**
- **[Swift](languages/swift/index.md)**

## Deployment

SurrealDB offers flexible deployment options to suit your infrastructure requirements. You can run the database as a fully managed cloud service, self-host it on your own servers, deploy it within containers, or embed it directly into your application.

- **[SurrealDB Cloud](manage/cloud/index.md)** — Provision and manage cloud-hosted SurrealDB instances with automatic scaling and backups.
- **[Self-hosted](manage/self-hosted/index.md)** — Install and run SurrealDB on your own infrastructure with full control over configuration.
- **[Embedding](build/embedding/index.md)** — Embed SurrealDB directly into your application as an in-process database engine.
- **[Docker](running/docker.md)** — Run SurrealDB in a Docker container for rapid setup and consistent environments.

## Integrations

SurrealDB connects with third-party tools, data management platforms, AI frameworks, and embeddings providers. It also supports AI agent workflows, with guides for connecting agents to the database.

- **[Integrations](build/integrations/index.md)** — Connect SurrealDB to third-party tools, AI frameworks, embeddings providers, and data management platforms.
- **[AI agents](build/ai-agents/index.md)** — Build AI agent workflows that use SurrealDB for knowledge storage, retrieval, and state management.

## Developer reference

The reference documentation provides comprehensive, detailed specifications for all SurrealDB interfaces. This includes the full SurrealQL query language with syntax definitions, as well as the command-line interface for managing SurrealDB instances and the HTTP-based REST API for programmatic access.

- **[SurrealQL](reference/query-language/index.md)** — Complete query language reference covering statements, functions, data types, and operators.
- **[CLI tools](reference/cli/index.md)** — Command-line interface reference for starting, managing, and interacting with SurrealDB.
- **[REST API](reference/rest-api/index.md)** — HTTP API reference for querying and managing SurrealDB over REST endpoints.

## Tutorials and resources

If you prefer learning through practical examples, the tutorials and demos section provides hands-on guides that walk you through common use cases and application patterns. The labs section offers experimental projects and community-contributed content for exploring SurrealDB in different contexts.

- **[Tutorials and demos](explore/tutorials/index.md)** — Step-by-step guides and example projects covering common SurrealDB use cases.
- **[Labs](labs/index.md)** — Experimental projects and community content for exploring SurrealDB capabilities.
