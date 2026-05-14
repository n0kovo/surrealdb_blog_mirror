---
position: 2
title: Writing SurrealQL
description: Ways of executing SurrealQL queries such as Surrealist, CLI, HTTP, SDKs, and GraphQL.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/surrealql/writing-surrealql.mdx"
---

# Writing SurrealQL

[SurrealQL](../../../reference/query-language/index.md) is the query language for SurrealDB. How they reach the database depends on your tool or integration. The sections below describe each path in more detail.

## SurrealQL execution paths

The following four approaches are the most commonly used ways to execute SurrealQL queries directly or indirectly via SDKs in one of many programming languages.

| Approach | Typical use |
| -------- | ----------- |
| [Surrealist](executing-queries/via-surrealist.md) | Interactive editing, Sandbox, and visual results in the browser. |
| [CLI](executing-queries/via-cli.md) | Local development, scripts, and [`surreal sql`](../../../reference/cli/surrealdb-cli/commands/sql.md) against a running server. |
| [HTTP](executing-queries/via-http.md) | Services and integrations that call the [`/sql`](../../../reference/rest-api/http-protocol.md#sql) endpoint. |
| [SDKs](executing-queries/via-sdks.md) | Application code using the official clients (WebSocket or HTTP under the hood, depending on SDK and configuration). |

In Surrealist, the built-in Sandbox does not persist data. To keep experimental work, use **Deploy to Cloud** in the app to create a free SurrealDB Cloud instance.

For a single entry point into these guides, see **[Executing queries](executing-queries/index.md)**.

Interactive clients (including the SDKs) usually speak to the database over **WebSocket** or **HTTP**. The [RPC protocol](../../../reference/rest-api/rpc-protocol.md) describes how queries and responses are framed on the wire.

Language syntax, statements, and functions are documented in the **[SurrealQL reference](../../../reference/query-language/index.md)**.

## GraphQL

[GraphQL](../graphql/overview.md) is a separate query interface on top of SurrealDB: you describe fields and shapes in GraphQL, not in SurrealQL. You can use it from [Surrealist](../graphql/via-surrealist.md), over [HTTP](../graphql/via-http.md), or from tools such as Postman or Bruno.
