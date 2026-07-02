---
position: 14
title: Representations and codecs
description: Choose the right built-in when moving data between strings, bytes, tokens, patches, and executable query text.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/concepts-and-guides/representations-and-codecs.mdx"
---

# Representations and codecs

*Since v3.2.0*

Many SurrealDB built-ins do the same broad job: take a value in **representation A** and produce a value in **representation B**. As these tend to be found over various parts of the documentation, this page is a map to introduce them in a single location and help you pick the right one.

## Quick overview

| I want to… | Use | Reference |
| --- | --- | --- |
| Serialise a value to JSON or CBOR (or Base64 bytes) | `encoding::json::*`, `encoding::cbor::*`, `encoding::base64::*` | [Encoding functions](../../../reference/query-language/functions/database-functions/encoding.md) |
| Parse JSON/CBOR bytes back into SurrealQL values | `encoding::json::decode`, `encoding::cbor::decode` | [Encoding functions](../../../reference/query-language/functions/database-functions/encoding.md) |
| Preview how an analyzer tokenizes text | `search::analyze` | [Search functions](../../../reference/query-language/functions/database-functions/search.md#searchanalyze) |
| Extract part of an email or URL string | `parse::email::*`, `parse::url::*` | [Parse functions](../../../reference/query-language/functions/database-functions/parse.md) |
| Diff or patch a value with JSON Patch | `value::diff`, `value::patch` | [Value functions](../../../reference/query-language/functions/database-functions/value.md) |
| Coerce or inspect types | `type::*`, casts (`<datetime>`, `<bytes>`, …) | [Type functions](../../../reference/query-language/functions/database-functions/type.md) |
| **Run a query string at runtime** | `eval::surql`, `eval::gql` | [Eval functions](../../../reference/query-language/functions/database-functions/eval.md) |

## Serialisation (`encoding::*`)

**Reversible codecs** for wire formats and storage:

- [`encoding::json::encode`](../../../reference/query-language/functions/database-functions/encoding.md#encodingjsonencode) / [`decode`](../../../reference/query-language/functions/database-functions/encoding.md#encodingjsondecode) — JSON text
- [`encoding::cbor::encode`](../../../reference/query-language/functions/database-functions/encoding.md#encodingcborencode) / [`decode`](../../../reference/query-language/functions/database-functions/encoding.md#encodingcbordecode) — [CBOR](../../../reference/rest-api/cbor-protocol.md) bytes
- [`encoding::base64::encode`](../../../reference/query-language/functions/database-functions/encoding.md#encodingbase64encode) / [`decode`](../../../reference/query-language/functions/database-functions/encoding.md#encodingbase64decode) — Base64 text for binary payloads

Typical uses: [`DEFINE API`](../../../reference/query-language/statements/define/api.md) request bodies, file bucket payloads, and SDK interchange. Round-trip is the mental model.

```surql
LET $payload = { event: 'signup', user: 'tobie' };

-- Value → JSON text → value again
encoding::json::decode(encoding::json::encode($payload));
-- { event: 'signup', user: 'tobie' }
```

Related one-way or format-specific helpers elsewhere include `string::html::encode`, `geo::hash::encode`, and [`crypto::*`](../../../reference/query-language/functions/database-functions/crypto.md) hashes.

## Text analysis (`search::analyze`)

[`search::analyze`](../../../reference/query-language/functions/database-functions/search.md#searchanalyze) runs a named [`DEFINE ANALYZER`](../../../reference/query-language/statements/define/analyzer.md) pipeline on a string and returns an array of tokens. It is **lossy** (stemming, filtering) and mirrors what full-text indexing does — useful for debugging analyzers before you index.

The "format" here is not JSON or CBOR; it is whatever pipeline you defined on the analyzer.

```surql
DEFINE ANALYZER demo_blank TOKENIZERS blank;

search::analyze("demo_blank", "SurrealDB graph queries");
-- ['SurrealDB', 'graph', 'queries']
```

Compare the tokens above with what you get after adding `FILTERS lowercase, snowball(english)` — the same input string produces a different token list, which is why `search::analyze` is handy when tuning an analyzer before you create a [`FULLTEXT`](../../../reference/query-language/statements/define/indexes.md) index.

## Structured parsing (`parse::*`)

[`parse::url::*`](../../../reference/query-language/functions/database-functions/parse.md) and [`parse::email::*`](../../../reference/query-language/functions/database-functions/parse.md) extract one component from a structured string. There is no round-trip — you get a field value, not a reassembled URL.

```surql
{
	domain: parse::url::domain("https://surrealdb.com/docs"),
	user: parse::email::user("tobie@surrealdb.com"),
};
-- { domain: 'surrealdb.com', user: 'tobie' }
```

## In-value transforms (`value::*`)

[`value::diff`](../../../reference/query-language/functions/database-functions/value.md#valuediff) and [`value::patch`](../../../reference/query-language/functions/database-functions/value.md#valuepatch) move between a SurrealQL value and JSON Patch operations. They pair naturally with [changefeeds](../real-time/changefeeds.md) and [`LIVE SELECT DIFF`](../real-time/live-queries.md).

```surql
LET $before = { title: 'Weekly update', status: 'draft' };
LET $after = { title: 'Weekly update', status: 'published' };
LET $patch = value::diff($before, $after);

value::patch($before, $patch);
-- { title: 'Weekly update', status: 'published' }
```

`value::diff` produced the patch; `value::patch` applied it. The same pair works when you receive patch operations from a client or a live diff stream.

## Dynamic evaluation (`eval::*`)

*Since v3.2.0*

[`eval::surql`](../../../reference/query-language/functions/database-functions/eval.md#evalsurql) and [`eval::gql`](../../../reference/query-language/functions/database-functions/eval.md#evalgql) parse and **execute** query text in the caller's transaction. That is fundamentally different from encoding:

- Input is **executable** SurrealQL or [ISO GQL](../gql/overview.md), not a static wire format.
- **Denied by default** — requires [`allow-eval-query`](../../security/authorization/capabilities.md#eval-queries) and the [arbitrary-query](../../security/authorization/capabilities.md#arbitrary-queries) gate.
- Nested writes affect the caller's transaction; transaction-control statements are rejected.

Use `eval::*` when the query string is only known at runtime. Prefer [`DEFINE FUNCTION`](../../../reference/query-language/statements/define/function.md), [`DEFINE API`](../../../reference/query-language/statements/define/api.md), or normal client queries when the shape of the work is fixed at deploy time.

```surql
-- Query text from a table, config row, or user input (requires allow-eval-query)
LET $template = "$greeting + ', ' + $name";
eval::surql($template, { greeting: 'Hello', name: 'world' });
-- 'Hello, world'
```

For [ISO GQL](../gql/overview.md) strings, use `eval::gql` instead — same bindings object, plus the `gql` experimental capability. See [Eval functions](../../../reference/query-language/functions/database-functions/eval.md) for setup and examples.

## See also

- [Database functions catalogue](../../../reference/query-language/functions/database-functions/index.md)
- [Parameterised queries](parameterised-queries.md) — `$parameters` at the SurrealQL layer (contrast with `eval` bindings)
- [Capabilities](../../security/authorization/capabilities.md)
