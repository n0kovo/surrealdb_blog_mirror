---
position: 0
title: Tutorials
description: "Step-by-step tutorials and walkthroughs for specific tasks with SurrealDB: integrations, real-time apps, AI patterns, and more."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/explore/tutorials/tutorials/overview.mdx"
---

# Tutorials

This section holds **tutorials**: practical **walkthroughs** that take you through a task or feature in order, with commands, configuration, and code you can follow along with. They are aimed at learning and production-style setup rather than only skimming a finished app.

If you prefer a **ready-made project** you can clone and run with minimal narrative, see the [demos](../demos/overview.md) section instead.

If you are new to SurrealDB, you may also want [Getting started](/docs) and the [SurrealQL](../../../reference/query-language/index.md) reference.

## Getting started

- [Define a schema in SurrealDB](define-a-schema.md) - build up a schemafull table with fields, assertions and indexes
- [Query SurrealDB from Postman](http-via-postman.md) - drive the HTTP endpoints from a REST client
- [Connect to SurrealDB via ngrok](connect-via-ngrok.md) - expose a local instance to a remote client
- [Use SurrealDB in GitHub Actions](github-actions.md) - run a database alongside your CI jobs

## Authentication

- [Integrate Auth0 with SurrealDB](auth0-integration.md) - verify Auth0 tokens with a record access method
- [Integrate AWS Cognito with SurrealDB](aws-cognito-integration.md) - the same pattern with a Cognito user pool

## AI and search

- [Build an AI agent with Python](build-an-ai-agent.md) - an agent that queries the database as a tool
- [Build a GenAI chatbot with Graph RAG](gen-ai-chatbot.md) - retrieval over a graph rather than a flat vector store
- [Build a knowledge graph for AI](how-to-build-a-knowledge-graph-for-ai.md) - model entities and relations for retrieval
- [Build a minimal LangChain chatbot](minimal-langchain.md) - the smallest working LangChain setup
- [Implement semantic search in Rust](semantic-search-in-rust.md) - embeddings, a vector index, and search from the Rust SDK

## Real-time

- [Build a real-time presence app](build-a-real-time-presence-app.md) - live queries driving who is online
