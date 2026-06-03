---
position: 14
title: mcp
description: "Start SurrealDB's Model Context Protocol server over stdio for local IDE and agent integrations."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/surrealdb-cli/commands/mcp.mdx"
---

# MCP command

*Since v3.1.0*

The `surreal mcp` subcommand starts the built-in [Model Context Protocol](https://modelcontextprotocol.io) server on **stdio**, suitable for Cursor, VS Code, Claude Desktop, and other MCP clients. It opens an embedded datastore at the path you pass (default `memory`) and runs every tool call under `Session::owner()`.

For HTTP-based clients against a running server, use [`surreal start`](start.md) and connect to **`/mcp`** instead. See [Model Context Protocol (MCP)](../../../../build/ai-agents/mcp.md) for transports, tools, and security guidance.

> [!WARNING]
> Stdio MCP is intended for a trusted operator on the same machine. Do not expose this process to untrusted users — there is no per-call HTTP authentication surface to re-bind credentials.

## Usage

```bash
surreal mcp --ns main --db main memory
```

Optional root credentials apply only when no root user exists yet (same semantics as `surreal start`):

```bash
surreal mcp -u root -p secret --ns main --db main memory
```

## Options

| Argument / flag | Environment | Description |
| --- | --- | --- |
| `path` (positional) | `SURREAL_PATH` | Database path (`memory` by default) |
| `--ns` | `SURREAL_MCP_NS` | Initial namespace |
| `--db` | `SURREAL_MCP_DB` | Initial database |
| `-u` / `--username` | `SURREAL_USER` | Root username (requires `--password`; only if no root exists) |
| `-p` / `--password` | `SURREAL_PASS` | Root password |

Database tuning flags from `surreal start` are also available via the shared `dbs` option group (see `surreal mcp --help`).

## Limits

Process-wide MCP limits use the `SURREAL_MCP_*` variables documented in [Environment variables](../environment-variables.md) and on [MCP for AI agents](../../../../build/ai-agents/mcp.md#configuration).
