---
position: 5
title: CustomDuration
description: The CustomDuration type wraps time.Duration with SurrealDB-compatible CBOR encoding and human-readable formatting.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/api/values/duration.mdx"
---

# `CustomDuration` {#customduration}

The `CustomDuration` struct wraps Go's `time.Duration` and handles CBOR encoding with tag 14 as specified by SurrealDB. It stores durations as a `[seconds, nanoseconds]` pair and formats them using SurrealDB's human-readable syntax (e.g., `1d2h30m`).

**Package:** `github.com/surrealdb/surrealdb.go/pkg/models`

**Source:** [pkg/models/duration.go](https://github.com/surrealdb/surrealdb.go/blob/main/pkg/models/duration.go)

---

## Definition

```go
type CustomDuration struct {
    time.Duration
}
```

`CustomDuration` embeds `time.Duration`, so all standard `time.Duration` methods are available directly.

---

## Methods

### `.String()` {#string}

Returns the duration formatted in SurrealDB syntax (e.g., `2h30m`, `1d12h`, `500ms`).

```go title="Syntax"
s := dur.String()
```

**Returns:** `string`

### `.ToCustomDurationString()` {#tocustomdurationstring}

Converts to a `CustomDurationString` value.

```go title="Syntax"
ds := dur.ToCustomDurationString()
```

**Returns:** `CustomDurationString`

---

## Related types

### `CustomDurationString` {#customdurationstring}

A string type for durations in SurrealDB format (e.g., `"1d2h30m"`). Encoded with CBOR tag 13.

```go
type CustomDurationString string
```

#### Methods

- `.String()` — returns the string value
- `.ToDuration()` — parses into `time.Duration`
- `.ToCustomDuration()` — converts to `CustomDuration`

---

## Helper functions

### `FormatDuration` {#formatduration}

Formats nanoseconds into SurrealDB duration syntax.

```go title="Syntax"
s := models.FormatDuration(ns)
```

**Returns:** `string`

### `ParseDuration` {#parseduration}

Parses a SurrealDB duration string into nanoseconds.

```go title="Syntax"
ns, err := models.ParseDuration("1d2h30m")
```

**Returns:** `(int64, error)`

Supported units: `y`, `w`, `d`, `h`, `m`, `s`, `ms`, `us`/`µs`, `ns`.

---

## Usage

```go

dur := models.CustomDuration{Duration: 2*time.Hour + 30*time.Minute}
fmt.Println(dur.String()) // "2h30m"

type Session struct {
    ID      *models.RecordID      `json:"id,omitempty"`
    Timeout models.CustomDuration  `json:"timeout"`
}
```

---

## See also

- [RecordID](record-id.md) for the record identifier type
- [CustomDateTime](datetime.md) for the datetime type
- [Value types](../../concepts/value-types.md) for the full type mapping
- [Data manipulation](../../concepts/data-manipulation.md) for using duration values in CRUD operations
- [SurrealQL duration type](../../../../reference/query-language/language-primitives/data-types/durations.md) for the underlying data model
