---
position: 0
title: Getting started
description: The official documentation for SurrealDB, a multi-model database. Built for modern applications.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/index.mdx"
---

SurrealDB stores relational, document, graph, time-series, vector and full-text data in one engine, queried through SurrealQL and reachable from ten official SDKs. It runs embedded in your application, as a single node, or as a distributed cluster.

<AgentBanner />

## Where do you want to start?

- **[I am new here](running/overview.md)** — Install SurrealDB, run it locally or in the cloud, and write your first query.
- **[I want to build something](learn.md)** — Connect an SDK, model your data, secure it, and put it into production.
- **[I need the details](reference.md)** — Every SurrealQL statement, protocol message and SDK method.

## Your first query

SurrealQL is SQL-shaped, so most of it reads as you would expect. What it adds is the ability to relate records directly and traverse those relations in the same statement, without a join table or a second database. Edit and run this:

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=--%20Records%20are%20addressed%20by%20table%20and%20id%0ACREATE%20person%3Aalice%20SET%20name%20%3D%20%27Alice%27%3B%0ACREATE%20company%3Aacme%20SET%20name%20%3D%20%27Acme%27%3B%0A--%20RELATE%20creates%20a%20graph%20edge%2C%20which%20can%20carry%20its%20own%20fields%0ARELATE%20person%3Aalice-%3Eworks_at-%3Ecompany%3Aacme%20SET%20since%20%3D%20d%272024-01-15%27%3B%0A--%20Traverse%20the%20edge%20from%20the%20record%2C%20in%20the%20projection%0ASELECT%20name%2C%20-%3Eworks_at-%3Ecompany.name%20AS%20employers%20FROM%20person%3B%0A)

The [querying guide](learn/querying/index.md) covers the language properly, and [data models](learn/data-models/index.md) covers what else the engine stores.

## Connect from your language

Each SDK has a quickstart that gets you connected, and a reference covering every method.

- **[Rust](languages/rust.md)**
- **[JavaScript](languages/javascript.md)**
- **[Python](languages/python.md)**
- **[Go](languages/golang.md)**
- **[.NET](languages/dotnet.md)**
- **[Java](languages/java.md)**
- **[Kotlin](languages/kotlin.md)**
- **[PHP](languages/php.md)**
- **[Swift](languages/swift.md)**
- **[Mojo](languages/mojo.md)**

[Community SDKs](languages/community.md) cover further languages, and the [Expo](frameworks/expo.md) and [React Native](frameworks/react-native.md) guides cover mobile.

## Run it somewhere

- **[SurrealDB Cloud](manage/instances/index.md)** — A managed instance with scaling, backups and monitoring handled for you.
- **[Self-hosted](manage/self-hosted/index.md)** — Run and operate SurrealDB on your own infrastructure.
- **[Docker](running/docker.md)** — A container for local development and consistent environments.
- **[Embedded](build/embedding/index.md)** — The engine in-process, natively or through WebAssembly.

## The rest of the documentation

- **[Learn](learn.md)** — Querying, schema, data models and security.
- **[Build](build.md)** — Embedding, migrating, integrations and AI agents.
- **[Manage](manage.md)** — Instances, organisations, observability and self-hosting.
- **[Explore](explore.md)** — SurrealDB Studio, tutorials, demos and labs.
- **[Reference](reference.md)** — SurrealQL, protocols, CLI tools and SDK methods.
- **[Agent Memory](https://surrealdb.com/docs/agent-memory)** — The memory and knowledge layer for AI agents.
