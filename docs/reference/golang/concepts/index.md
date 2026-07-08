---
title: Concepts
generated: stub
---

# Concepts

_Auto-generated index — 11 pages._

## Pages

- [Authentication](authentication.md)
  The Go SDK provides methods for signing in, signing up, and managing authentication at root, namespace, database, and record levels.
- [Connecting to SurrealDB](connecting-to-surrealdb.md)
  The Go SDK supports connecting to SurrealDB over WebSocket or HTTP using a URL-based connection factory.
- [Data manipulation](data-manipulation.md)
  The Go SDK provides generic functions for selecting, creating, updating, and deleting records in SurrealDB.
- [Error handling](error-handling.md)
  The Go SDK provides structured error types for distinguishing between server errors, query errors, and transport failures.
- [Executing queries](executing-queries.md)
  The Go SDK provides generic functions for executing SurrealQL queries with typed results and parameterised variables.
- [Live queries](live-queries.md)
  The Go SDK supports real-time live queries that stream change notifications from the database through Go channels.
- [Multiple sessions](multiple-sessions.md)
  The Go SDK supports creating multiple isolated sessions on a single WebSocket connection, each with its own authentication and namespace.
- [Query builder](query-builder.md)
  The Go SDK provides a contrib package for building type-safe SurrealQL queries programmatically with automatic parameter binding.
- [Reliable connections](reliable-connections.md)
  The Go SDK provides a contrib package for auto-reconnecting WebSocket connections with session restoration and live query persistence.
- [Transactions](transactions.md)
  The Go SDK supports interactive transactions that let you execute statements one at a time and conditionally commit or cancel.
- [Value types](value-types.md)
  The Go SDK uses typed wrappers for SurrealDB values like RecordID, UUID, DateTime, and Duration, encoded over CBOR.
