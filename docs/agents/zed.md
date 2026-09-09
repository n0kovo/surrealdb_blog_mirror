---
position: 8
title: Zed
description: Hosted MCP server and Agent Skills setup for Zed. Covers the context_servers entry in the Zed settings file.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/agents/zed.mdx"
---

# Zed

[Zed](https://zed.dev) calls MCP servers **context servers**. Adding SurrealDB gives Zed's assistant your Cloud instances and the data inside them.

## Add the MCP server

Open settings with `cmd`/`ctrl` `,`, which edits `~/.config/zed/settings.json`, and add SurrealDB under `context_servers`:

```json
{
  "context_servers": {
    "surrealdb": {
      "url": "https://mcp.surrealdb.com"
    }
  }
}
```

> [!NOTE]
> Zed runs stdio context servers as child processes. If your version does not yet accept a remote `url`, bridge the endpoint through `mcp-remote` instead, using a `command` with `"path": "npx"` and the arguments `["-y", "mcp-remote", "https://mcp.surrealdb.com"]`.

## Sign in

Restart Zed and approve the connection in the browser window it opens.

## Install the Agent Skills

```bash
npx skills add surrealdb/agent-skills
```

## Check it worked

Ask the assistant panel which SurrealDB tools it can call.

## Next steps

- [SurrealDB MCP Server](../build/ai-agents/mcp/index.md) - every tool the server publishes
- [Agent Skills](../build/ai-agents/agent-skills.md) - what each skill covers
