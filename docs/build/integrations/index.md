---
position: 1
title: Integrations
description: Integrations that connect SurrealDB to AI frameworks, embeddings providers, agents, and data tools.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/integrations/index.mdx"
---

# Integrations

This section collects guides for wiring SurrealDB into the rest of your stack: AI and agent frameworks, embeddings and model providers, data movement (ELT, automation, and similar), and related topics. Each page focuses on a specific tool or pattern so you can find a starting point quickly.

This section assumes a certain level of familiarity with SurrealDB itself. If more general orientation and tutorials are needed first, be sure to start with [What is SurrealDB?](../../what-is-surrealdb.md) and the [Querying](../../learn/querying/index.md) section of the docs.

## Agent rules

- [Agent rules](agent-rules/agent-rules.md) - rule files that teach an assistant your project's conventions

## Authentication

- [Better Auth](authentication/better-auth/overview.md) - use SurrealDB as the database behind Better Auth
- [Getting started](authentication/better-auth/getting-started.md) - wire the adapter up and run your first sign-in
- [Plugins](authentication/better-auth/plugins.md) - which Better Auth plugins the adapter supports
- [Transactions & limitations](authentication/better-auth/transactions-and-limitations.md) - what the adapter cannot do yet, and why

## Data management

- [Data management integrations](data-management/overview.md) - the pipeline and testing tools that connect to SurrealDB
- [Airbyte](data-management/airbyte.md) - move data in and out with an Airbyte connector
- [Fivetran](data-management/fivetran.md) - managed pipelines into SurrealDB
- [n8n](data-management/n8n.md) - automate workflows against a database
- [Qyrus](data-management/qyrus.md) - test-data generation

## Embeddings providers

- [Embeddings provider integrations](embeddings-providers/overview.md) - which providers are covered, and what each needs
- [OpenAI](embeddings-providers/openai.md) - embed with OpenAI models
- [Mistral](embeddings-providers/mistral.md) - embed with Mistral models
- [Fastembed](embeddings-providers/fastembed.md) - embed locally, without an API call
- [Python quickstart](embeddings-providers/python-quickstart.md) - end to end from Python
- [Rust quickstart](embeddings-providers/rust-quickstart.md) - end to end from Rust
