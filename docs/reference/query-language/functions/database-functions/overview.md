---
position: 0
title: Overview
description: Built-in SurrealQL database functions and constants, along with JavaScript and SurrealML functions.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/functions/database-functions/overview.mdx"
---

# Database functions overview

Database functions are SurrealQL’s built-in, namespaced helpers (`string::split()`, `math::mean()`, `time::now()`, and so on). They run inside the database engine, are documented module-by-module in this section, and are the usual choice for everyday querying and data shaping.

SurrealQL also supports other kinds of callable logic:

- [JavaScript functions](../../scripting/overview.md) — embedded scripts when the JavaScript runtime is enabled; see the scripting docs for definitions, context, and limits.
- [SurrealML functions](../../../../explore/ml-models/index.md) — helpers used with SurrealML.

For the full module list, short examples per module, and calling conventions (classic `::` paths, method chaining, and v3 underscore paths), open the [database functions catalogue](index.md).

## Constants

Several modules expose constants: fixed values referenced like `math::pi` or `time::minimum` (without parentheses) alongside callable functions on the same pages:

- [Math constants](math.md#math-constants) — numeric values such as `math::e`, `math::pi`, τ, infinities, and common fractions.
- [Time constants](time.md#time-constants) — `time::epoch`, `time::minimum`, and `time::maximum`.
- [Duration constants](duration.md#duration-constants) — `duration::max` as the greatest representable duration.

## Extensions

You can also write your own functions in Rust that can be compiled to WASM modules, linked to and called from the database. For more on how extensions are built and run, see [this page](../../../../learn/extensions/index.md).
