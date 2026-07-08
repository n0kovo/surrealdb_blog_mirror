---
position: 10
title: Swift
description: Connect to SurrealDB and run your first queries with the Swift SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/swift.mdx"
---

# Getting started

The Swift SDK for SurrealDB lets you connect to a database and query it from your application. This guide covers connecting, authenticating, and running your first queries.

## 1. Install the SDK

Follow the [installation guide](../reference/swift/installation.md) to add the SDK to your project. Once installed, import the SDK.

```swift
```

## 2. Connect to SurrealDB

Create a client for your endpoint and connect. The `SurrealHTTPClient` is the simplest starting point for most applications.

Supported connection protocols include:
- **HTTP** (`http://`, `https://`) using [`SurrealHTTPClient`](../reference/swift/concepts/connecting.md) for short-lived stateless connections, the simplest way to get started
- **WebSocket** (`ws://`, `wss://`) using the WebSocket client for long-lived stateful connections, required for [live queries](../reference/swift/concepts/live-queries.md)

```swift
let client = try SurrealHTTPClient(endpoint: "http://localhost:8000")
try await client.connect()
defer { Task { await client.close() } }
```

After connecting, use [`signin`](../reference/swift/concepts/authentication.md) to authenticate and [`use`](../reference/swift/concepts/connecting.md) to select the namespace and database you want to work with. Most operations require both.

```swift
let tokens = try await client.signin(.root(username: "root", password: "root"))
try await client.use(namespace: "myapp", database: "mydb")
```

## 3. Inserting data into SurrealDB

The Swift SDK is model-first. The `@SurrealModel` macro generates `SurrealModel` conformance, the `surrealTable` name, and a type-safe `Fields` namespace used to build [predicates](../reference/swift/concepts/predicates.md).

```swift
@SurrealModel("person")
struct Person: Codable, Sendable {
    let id: String?
    let name: String
    let age: Int
}
```

Once you have a model, use [`create`](../reference/swift/methods/create.md) to insert a record.

```swift
let created: [Person] = try await client.create(
    Person(id: nil, name: "Ada", age: 30)
)
```

## 4. Retrieving data from SurrealDB

### Selecting records

Use [`select`](../reference/swift/methods/select.md) to retrieve all records of a table, or narrow the results with a type-safe predicate built from the model's `Fields` namespace.

```swift
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

### Running SurrealQL queries

For more advanced use cases, use [`queryRaw`](../reference/swift/methods/query-raw.md) to run [SurrealQL](../reference/query-language/index.md) statements directly. Use bound parameters to safely pass dynamic values.

```swift
let results: [RPCQueryResult] = try await client.queryRaw(
    "SELECT * FROM person WHERE age > $minAge LIMIT $limit;",
    bindings: [
        "minAge": .int(18),
        "limit": .int(50)
    ]
)

for row in results {
    if row.status == .ok {
        print(row.result)
    }
}
```

## 5. Closing the connection

Always close the connection when you are done to release resources. The idiomatic Swift pattern is to `defer` the close immediately after connecting, as shown in step 2.

```swift
await client.close()
```

## Next steps

You have learned how to install the SDK, connect to SurrealDB, create records, and retrieve data. There is a lot more you can do with the SDK, including updating and deleting records, authentication, live queries, and transactions.

- **[Connecting to SurrealDB](../reference/swift/concepts/connecting.md)** — Learn how to manage your database connections, including protocols and configuration.
- **[Authentication](../reference/swift/concepts/authentication.md)** — Read more about authentication levels and how to integrate them into your application.
- **[Models](../reference/swift/concepts/models.md)** — Learn how to define models with the @SurrealModel macro and build type-safe queries.
- **[API Reference](../reference/swift/methods/index.md)** — Complete reference for all methods, types, and errors.

> [!NOTE]
> This getting-started guide covers the essentials. For the complete methods, API, and concept reference, see the [Swift SDK reference](../reference/swift/index.md).
