---
position: 3
title: Response
description: The Response class wraps the results of a SurrealQL query execution.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/java/api/core/response.mdx"
---

# `Response` {#response}

The `Response` class wraps the results returned by a SurrealQL query execution. A single query string can contain multiple statements, and the `Response` holds the result of each statement indexed by its zero-based position.

**Source:** [surrealdb.java](https://github.com/surrealdb/surrealdb.java)

---

## Methods

### `.take(index)` {#take}

Extracts the result of a specific statement from the response by its zero-based index. The untyped variant returns a raw `Value`, while the typed variant deserializes the result into the specified Java class.

```java title="Method Syntax"
Value take(int num)
<T> List<T> take(Class<T> type, int num)
```

<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`type` *[optional]*</td>
            <td>`Class&lt;T&gt;`</td>
            <td>The class to deserialize the result into. Omit for an untyped `Value` return.</td>
        </tr>
        <tr>
            <td>`num` *[required]*</td>
            <td>`int`</td>
            <td>The zero-based index of the statement result to extract.</td>
        </tr>
    </tbody>
</table>

**Returns:** `Value` (untyped) or `List<T>` (typed)

```java title="Example"
Response response = db.query("SELECT * FROM users; SELECT * FROM posts;");

Value users = response.take(0);
List<Post> posts = response.take(Post.class, 1);
```

### `.size()` {#size}

Returns the number of statement results contained in the response.

```java title="Method Syntax"
response.size()
```

**Returns:** `int`

```java title="Example"
Response response = db.query("SELECT * FROM users; SELECT * FROM posts;");
int count = response.size();
```

---

## Complete example

```java title="Working with multi-statement responses"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    Response response = db.query(
        "CREATE person SET name = 'Alice'; SELECT * FROM person;"
    );

    int statementCount = response.size();

    Value created = response.take(0);
    List<Person> people = response.take(Person.class, 1);
}
```

---

## See also

- [Surreal](surreal.md), Connection and method reference
- [Executing queries](../../concepts/executing-queries.md), Query concepts and patterns
- [Value types](../../concepts/value-types.md), Working with the Value class
- [SurrealQL](../../../query-language/index.md), Query language reference
