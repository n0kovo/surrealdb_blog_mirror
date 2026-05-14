---
position: 2
title: Installation
description: The SurrealDB Go SDK can be installed with a single go get command.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/golang/installation.mdx"
---

# Installation

Install the SDK from [pkg.go.dev](https://pkg.go.dev/github.com/surrealdb/surrealdb.go) using `go get`:

```bash
go get github.com/surrealdb/surrealdb.go
```

Then import the SDK and its models package in your Go files:

```go
	surrealdb "github.com/surrealdb/surrealdb.go"
	"github.com/surrealdb/surrealdb.go/pkg/models"
)
```

The `surrealdb` package contains the client, query functions, and authentication methods. The `models` package contains value types such as [`RecordID`](api/values/record-id.md), [`Table`](api/values/table.md), and [`UUID`](api/values/uuid.md).

## Requirements

- Go `1.23` or later
- SurrealDB `v2.x` or `v3.x`

## Next steps

- [Quick start](start.md) to build your first application
- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md) for connection protocols and configuration
