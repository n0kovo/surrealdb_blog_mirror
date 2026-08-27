---
position: 6
title: Visual Studio Code
description: Set up Visual Studio Code for SurrealDB with the hosted MCP server and the official Agent Skills.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/agents/vscode.mdx"
---

# Visual Studio Code

[Visual Studio Code](https://code.visualstudio.com) has a native MCP client, so any chat extension that uses it can reach your SurrealDB Cloud account.

## Add the MCP server

VS Code uses a `servers` object with an explicit transport type. Put it in `.vscode/mcp.json` for the workspace, or in the user-level `mcp.json` to have it everywhere.

```json
{
  "servers": {
    "surrealdb": {
      "type": "http",
      "url": "https://mcp.surrealdb.com"
    }
  }
}
```

| Scope | Path |
| --- | --- |
| Workspace | `.vscode/mcp.json` |
| Global (macOS) | `~/Library/Application Support/Code/User/mcp.json` |
| Global (Windows) | `%APPDATA%\Code\User\mcp.json` |
| Global (Linux) | `~/.config/Code/User/mcp.json` |

## Sign in

Reload the window, start the server from the MCP view, and approve the connection in the browser window that opens.

## Install the Agent Skills

```bash
npx skills add surrealdb/agent-skills
```

## Check it worked

Ask chat which SurrealDB tools it has available. If nothing appears, reload the window — VS Code reads `mcp.json` at startup.

## Next steps

- [GitHub Copilot](github-copilot.md) — the same file, with Copilot agent mode
- [SurrealDB MCP Server](../build/ai-agents/mcp/index.md) — every tool the server publishes
