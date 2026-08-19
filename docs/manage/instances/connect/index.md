---
position: 1
title: Connect to an instance
description: "The four routes to an instance: SurrealDB Studio, the CLI, a client SDK, and the HTTP API. Includes where to find the connection details."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/instances/connect/index.mdx"
---

# Connect to an instance

An instance exposes one endpoint, and every client reaches it the same way.

What differs is the tool you use and how you authenticate.

| Route | Use it for |
| --- | --- |
| [SurrealDB Studio](via-studio.md) | Running queries and browsing data in a graphical interface. |
| [CLI](via-cli.md) | An interactive SurrealQL shell, and one-off queries from a terminal or a script. |
| [SDK](via-sdk.md) | Application code in Rust, JavaScript, Python, .NET, PHP, and the other supported languages. |
| [HTTP](via-http.md) | cURL, Postman, and any HTTP client, including bulk import. |

## Before you begin

You need:

- An account. See [Accounts and sign-in](../../organisations/sign-in.md).
- A running instance. See [Create an instance](../create.md).
- A **namespace** and a **database** to work in. SurrealDB needs both to know where a query runs. See [system structure](../../../concepts.md#system-structure).
- Credentials, unless you connect from SurrealDB Studio, which authenticates with your own session.

## Finding the connection details

The **Connect** menu of the instance in [SurrealDB Studio](https://app.surrealdb.com) holds the endpoint. It also produces a ready-made command or snippet for each route, with the details of your instance already filled in. Copying from there avoids transcription mistakes in the hostname.

`surrealctl instance endpoint` prints the same endpoint, and `surrealctl instance token` issues a token for it. Both are useful in scripts and in CI, where opening a browser is not an option. See [surrealctl instances](../../surrealctl/instances.md).
