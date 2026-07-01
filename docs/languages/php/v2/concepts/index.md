---
title: Concepts
generated: stub
---

# Concepts

_Auto-generated index — 12 pages._

## Pages

- [Authentication](authentication.md)
  Sign in and sign up with typed credentials in version 2 of the PHP SDK, then manage tokens and authentication state.
- [Connecting to SurrealDB](connecting-to-surrealdb.md)
  Open a connection to a SurrealDB instance with version 2 of the PHP SDK, select a namespace and database, and configure reconnection.
- [Data types](data-types.md)
  How version 2 of the PHP SDK maps SurrealQL data types to native PHP types and custom value classes.
- [Error handling](error-handling.md)
  Handle failures in version 2 of the PHP SDK with the typed exception hierarchy rooted at SurrealException.
- [Events](events.md)
  Observe connection lifecycle and RPC traffic in version 2 of the PHP SDK with the high-level subscribe() API and the lower-level PSR-14 event dispatcher.
- [Executing queries](executing-queries.md)
  Run raw SurrealQL or use the fluent query builders for select, create, update, and delete in version 2 of the PHP SDK.
- [Live queries](live-queries.md)
  Subscribe to real-time changes from SurrealDB over a WebSocket connection with version 2 of the PHP SDK.
- [Middleware](middleware.md)
  Intercept every RPC in version 2 of the PHP SDK with middleware, including the built-in logging, telemetry, retry, and authentication steps.
- [Observability](observability.md)
  Emit OpenTelemetry traces and metrics from version 2 of the PHP SDK, with runtime-aware presets, a configurable provider factory, and vendor-neutral tracing and metrics seams.
- [Runtimes and workers](runtimes.md)
  Configure your PHP environment (PHP-FPM, OpenSwoole, or FrankenPHP) so live queries and other long-lived connections run without blocking your application.
- [Sessions](sessions.md)
  Run multiple independent sessions over a single WebSocket connection with version 2 of the PHP SDK, each with its own namespace, variables, and authentication.
- [Transactions](transactions.md)
  Run multiple statements atomically with version 2 of the PHP SDK, using a SurrealQL transaction block or explicit transaction handles.
