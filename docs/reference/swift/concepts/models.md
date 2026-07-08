---
position: 1
title: Models
description: Define type-safe models for SurrealDB using the @SurrealModel macro or manual conformance in the Swift SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/swift/concepts/models.mdx"
---

# Models

Models describe the shape of your records and give the SDK the type information it needs for type-safe CRUD operations and [predicates](predicates.md).

## The `@SurrealModel` macro

The `@SurrealModel` macro is the recommended way to declare a model. It takes the table name and generates everything the SDK needs:

```swift

@SurrealModel("person")
struct Person: Codable, Sendable {
    let id: String?
    let name: String
    let age: Int
}
```

The macro generates:

- `static let surrealTable`, the table name passed to the macro.
- `SurrealModel` conformance, so the type can be used directly with [`select`](../methods/select.md), [`create`](../methods/create.md), [`update`](../methods/update.md), [`upsert`](../methods/upsert.md) and [`delete`](../methods/delete.md).
- A `Fields` namespace for building type-safe predicates such as `Person.Fields.age >= 18`.

## Manual conformance

If you prefer not to use the macro, you can conform to `SurrealModel` manually by declaring the `surrealTable` property:

```swift
struct Article: SurrealModel, Codable, Sendable {
    static let surrealTable = "article"
    let id: String?
    let title: String
}
```

Manual conformance does not generate a `Fields` namespace, so you will need to write [raw predicates](predicates.md#raw-predicates) for queries that filter on fields.
