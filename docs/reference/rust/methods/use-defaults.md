---
position: 26
title: use_defaults
description: The .use_defaults() method for the SurrealDB Rust SDK selects the default namespace and database for this connection, if the server and client are configured to provide one.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/rust/methods/use-defaults.mdx"
---

# `use_defaults()`

Selects the namespace and database set by [`DEFINE CONFIG DEFAULT`](../../query-language/statements/define/config.md). If no default is configured, the session is left unchanged.

```rust title="Method Syntax"
db.use_defaults().await?
```

This complements [`use_ns()` and `use_db()`](use.md) when you want the configured default instead of a specific pair.

The defaults only fill in what is missing. A session that has already selected a namespace — from a token, for example — keeps that selection.

### See also

* [`.use_defaults()` on Docs.rs](https://docs.rs/surrealdb/latest/surrealdb/struct.Surreal.html#method.use_defaults)
