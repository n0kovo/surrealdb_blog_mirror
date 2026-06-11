---
position: 2
title: connect
description: The connect() method for the SurrealDB Swift SDK connects the client to the configured endpoint.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/swift/methods/connect.mdx"
---

# `connect()` {#connect}

Connects the client to the endpoint it was configured with.

```swift title="Method Syntax"
try await client.connect()
```

### Example usage

```swift
let client = try SurrealHTTPClient(endpoint: "http://localhost:8000")
try await client.connect()
defer { Task { await client.close() } }
```

See [Connecting to SurrealDB](../concepts/connecting.md) for the available client types and configuration options.
