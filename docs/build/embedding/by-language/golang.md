---
position: 1
title: Golang
description: The documentation for embedding SurrealDB within Go can be found in the Go SDK and surrealdb.c.go documentation.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/embedding/by-language/golang.mdx"
---

# Embedding in Go

SurrealDB can be run [as an embedded database](../../../reference/golang/embedding.md) within your Go application, allowing you to use SurrealDB without running a separate server process. This is ideal for desktop applications, testing, local development, and edge computing scenarios.

## Embedded database options

SurrealDB supports multiple types of embedded storage in Go:

- **In-memory database** (`mem://`) - Fastest performance with data stored in RAM. Perfect for testing, caching, or temporary data. Data is lost when the connection closes.

- **File-based database** (`surrealkv://` or `rocksdb://`) - Persistent storage on disk using the SurrealKV storage engine. Data persists across connections and application restarts. The RocksDB backend requires a separate manual build detailed [here](https://github.com/surrealdb/surrealdb.c.go/blob/main/docs/rocksdb.md)

## Quick example

```csharp
package main

    "context"
    "fmt"
    "log"

    surrealdb "github.com/surrealdb/surrealdb.c.go"
)

type Person struct {
    ID   surrealdb.RecordID[string] `cbor:"id,omitempty"`
    Name string                     `cbor:"name"`
    Age  int64                      `cbor:"age"`
}

func main() {
    ctx := context.Background()

    db, err := surrealdb.Open(ctx, "mem://")
    if err != nil {
        log.Fatal(err)
    }
    defer db.Close()

    db.Use(ctx, "main", "main")
    db.Query(ctx, "CREATE $rid CONTENT $content", map[string]any{
        "rid":     surrealdb.NewRecordID("person", "alice"),
        "content": Person{Name: "Alice", Age: 30},
    })

    results, _ := surrealdb.Query[Person](ctx, db, "SELECT * FROM person", nil)
    for _, p := range results[0].Values() {
        fmt.Printf("%s: %s (age %d)\n", p.ID, p.Name, p.Age)
    }
}
```

For complete documentation, installation instructions, examples, best practices, and troubleshooting, see the [Go SDK embedding guide](../../../reference/golang/embedding.md).
