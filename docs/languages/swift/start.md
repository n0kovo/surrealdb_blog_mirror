---
position: 3
title: Getting started
description: In this section, you will learn how to connect to SurrealDB and run your first query using the Swift SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/swift/start.mdx"
---

# Getting started

This guide covers defining a model, connecting to SurrealDB, authenticating, and running your first queries with the Swift SDK. Make sure you have [installed the SDK](installation.md) first.

## Define a model

The `@SurrealModel` macro generates `SurrealModel` conformance, the `surrealTable` name, and a type-safe `Fields` namespace used to build [predicates](concepts/predicates.md).

```swift

@SurrealModel("person")
struct Person: Codable, Sendable {
    let id: String?
    let name: String
    let age: Int
}
```

## Connect to the database

Create a client for your endpoint and connect. The HTTP client is the simplest starting point; for [live queries](concepts/live-queries.md) you will need the WebSocket client instead.

```swift
let client = try SurrealHTTPClient(endpoint: "http://localhost:8000")
try await client.connect()
defer { Task { await client.close() } }
```

## Authenticate and select a namespace

```swift
let tokens = try await client.signin(.root(username: "root", password: "root"))
try await client.use(namespace: "myapp", database: "mydb")
```

## Create and select records

```swift
// Create a record
let created: [Person] = try await client.create(
    Person(id: nil, name: "Ada", age: 30)
)

// Select all records of a table
let people = try await client.select(Person.self)

// Select with a type-safe predicate
let adults = try await client.select(
    Person.self,
    where: Person.Fields.age >= 18,
    limit: 20,
    start: 0
)
```

## Next steps

Continue with the rest of the documentation:

- [Models and the `@SurrealModel` macro](concepts/models.md)
- [Connecting to SurrealDB](concepts/connecting.md)
- [Authentication](concepts/authentication.md)
- [The full list of SDK methods](methods/index.md)
