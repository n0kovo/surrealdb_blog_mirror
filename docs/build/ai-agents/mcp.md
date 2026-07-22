---
position: 2
title: Model Context Protocol (MCP)
description: Connect AI agents and IDEs to SurrealDB through the built-in MCP server over HTTP or stdio.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/ai-agents/mcp.mdx"
---

# Model Context Protocol (MCP)

*Since v3.1.0*

SurrealDB ships a built-in [Model Context Protocol](https://modelcontextprotocol.io) server so agents and editors can list schema, run SurrealQL, and manipulate records through a standard tool surface. The same access-control rules as [`/sql`](../../reference/rest-api/http-protocol.md#post-sql) and RPC apply: `DEFINE USER` permissions, table `PERMISSIONS`, and server capability flags all gate what tools can do.

Both entry points expose the **same MCP tools** — the difference is how your editor connects and who shares the database.

## When to use `surreal mcp` vs `surreal start`

| | **`surreal mcp`** (stdio) | **`surreal start`** + **`/mcp`** (HTTP) |
| --- | --- | --- |
| **How it works** | Your editor spawns SurrealDB as a child process; MCP runs over stdin/stdout | You run a server; the editor connects to `http://…/mcp` |
| **Database** | Embedded in the MCP process (default `memory`, or a local file path) | The same instance your app, CLI, or Surrealist uses |
| **Authentication** | Owner-level access for every tool call — no login step | Normal SurrealDB auth (Bearer JWT, HTTP Basic, …) |
| **Best for** | Learning MCP, solo local dev, quickest editor setup | Shared databases, teams, remote/Cloud instances, production patterns |
| **Editor config** | `command` + `args` in MCP settings | `url` + auth headers |

**Use `surreal mcp` when** you want the lowest-friction path on a machine you trust — paste a config, restart the editor, and experiment. Think of it as a self-contained database for your assistant.

**Use `surreal start` and `/mcp` when** the agent should work against a database that already exists or that other clients share. That is the right model for least-privilege users, TLS, audit logging, and anything beyond trusted solo local dev.

> [!TIP]
> New to MCP? Start with [`surreal mcp`](connect-mcp-to-your-editor.md) in your coding assistant, then move to HTTP once you want the agent on the same SurrealDB instance as your application.

## Transports

### HTTP (`/mcp`)

When you run `surreal start`, the server exposes **`POST /mcp`** (streamable HTTP) on the same bind address as the REST API. Authenticate with the same headers you use elsewhere, for example `Authorization: Bearer <jwt>` or HTTP Basic.

```bash
surreal start --user root --pass secret --bind 127.0.0.1:8000 memory
# MCP endpoint: http://127.0.0.1:8000/mcp
```

For a non-loopback hostname (a public FQDN, Kubernetes service name, or load-balancer host), the HTTP transport's DNS-rebinding guard rejects the request with `403 Forbidden: Host header is not allowed` unless you opt in. Set `SURREAL_MCP_ALLOWED_HOSTS` to your hostnames, or `SURREAL_MCP_ALLOW_ALL_HOSTS=true` behind a trusted proxy. See [Configuration](#configuration).

Run behind TLS in production. The `mcp-session-id` header acts like a bearer token for the lifetime of a session — anyone who holds it can replay tool calls as the bound subject until the session expires (idle timeout defaults to five minutes).

### Stdio (`surreal mcp`)

For local IDE integrations (Cursor, VS Code, Claude Desktop, and similar), use the dedicated subcommand. It runs the MCP server in-process with an embedded datastore:

```bash
surreal mcp --user root --pass secret --ns main --db main memory
```

Stdio uses `Session::owner()` for every tool call. **Do not expose this entry point to untrusted users** — there is no per-request credential re-binding on stdio because there is no network handshake to attach headers to.

See [`surreal mcp`](../../reference/cli/surrealdb-cli/commands/mcp.md) for flags and environment variables (`SURREAL_MCP_NS`, `SURREAL_MCP_DB`, and the shared `SURREAL_MCP_*` limits below).

## Published tools

`tools/list` exposes these tools (names are stable):

| Tool | Purpose |
| --- | --- |
| `query` | Run SurrealQL and return serialised results |
| `gql` | Run an [OpenGQL](../../learn/querying/gql/overview.md) query (requires the `opengql` experimental capability on the server) |
| `graphql` | Run a [GraphQL](../../learn/querying/graphql/overview.md) query against the configured schema |
| `select`, `create`, `insert`, `upsert`, `update`, `delete`, `relate` | Data manipulation helpers |
| `run` | Call a database function with typed arguments |
| `list` | List namespaces, databases, tables, indexes, users, … |
| `use` | Select namespace / database context |
| `info` | Schema or engine information for a scope |

Legacy names such as `list_tables`, `use_database`, or `version` are not published anymore — use `list` and `use` instead.

## Configuration

MCP-specific limits are read once from the environment (prefix `SURREAL_MCP_`). HTTP body size uses the server-wide cap.

| Variable | Default | Effect |
| --- | --- | --- |
| `SURREAL_MCP_QUERY_TIMEOUT_SECS` | 60 | Outer timeout on each tool execution (`0` disables) |
| `SURREAL_MCP_MAX_RESULT_BYTES` | 256 KiB | Cap on serialised tool output (`0` disables) |
| `SURREAL_MCP_RUN_MAX_ARGS` | 64 | Maximum arguments to `run` |
| `SURREAL_MCP_PARAMS_MAX_KEYS` | 256 | Maximum top-level keys in parameter objects |
| `SURREAL_MCP_PARAMS_MAX_QL_BYTES` | 4 KiB | Maximum byte length of a `$ql` string inside a `*_data` payload |
| `SURREAL_MCP_SCHEMA_RESOURCE_MAX_TABLES` | 200 | Cap on tables enriched in the database schema resource |
| `SURREAL_MCP_ALLOWED_HOSTS` *Since v3.2.1* | loopback only | Exact `Host` values accepted for HTTP `/mcp` (replaces the loopback default) |
| `SURREAL_MCP_ALLOW_ALL_HOSTS` *Since v3.2.1* | `false` | Accept any `Host` (trusted proxy escape hatch; overrides the allowlist) |
| `SURREAL_HTTP_MAX_MCP_BODY_SIZE` | 4 MiB | Maximum HTTP body size for `/mcp` |

Full tables live under [Environment variables](../../reference/cli/surrealdb-cli/environment-variables.md). [Observability metrics](../../manage/observability/metrics.md) include `surrealdb.mcp.*` counters and histograms from 3.1.0.

## Security checklist

- Prefer a least-privilege `DEFINE USER` (for example a custom role with table-level `PERMISSIONS`) instead of root credentials for agent clients.
- Lock down capabilities (`--deny-funcs`, `--allow-net`, …) so a hijacked session cannot reach `http::*` or other high-risk functions.
- Set `--allow-origin` explicitly for browser-based MCP clients; avoid `*` in production.
- For HTTP `/mcp` on a public hostname, set `SURREAL_MCP_ALLOWED_HOSTS` (or `SURREAL_MCP_ALLOW_ALL_HOSTS` only behind a trusted proxy). The default allowlist is loopback-only.
- Forward the `surrealdb::mcp::audit` tracing target to your SIEM — audit records include tool name, subject, namespace, database, and outcome, but never query text or row payloads.

## Next steps

- **[Connect MCP to your coding assistant](connect-mcp-to-your-editor.md)** — step-by-step Cursor, VS Code, and Claude Desktop setup
- [Why SurrealDB for AI agents](index.md) — memory, tools, and retrieval patterns
- [Agent Skills](agent-skills.md) — installable SurrealQL and SDK skills for coding agents
- [AI frameworks integrations](../integrations/ai-frameworks/overview.md)
