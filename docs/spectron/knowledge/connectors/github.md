---
position: 5
title: GitHub connector
description: Planned sync from GitHub repositories into Spectron documents.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/knowledge/connectors/github.mdx"
---

# GitHub connector

> **Not implemented.** Spectron does not ship a GitHub connector or `/connectors` API in the current release.

**Workaround:** export or clone repository files and ingest with:

```bash
spectron documents upload ./README.md
spectron documents ingest ./docs/
```

See [Connectors overview](overview.md).
