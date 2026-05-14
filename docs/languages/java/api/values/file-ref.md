---
position: 9
title: FileRef
description: The FileRef class represents a reference to a file stored in SurrealDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/api/values/file-ref.mdx"
---

# `FileRef` {#file-ref}

The `FileRef` class represents a reference to a [file stored in SurrealDB](../../../../reference/query-language/language-primitives/data-types/files.md). A file reference consists of a storage bucket name and a unique file key within that bucket.

**Source:** [surrealdb.java](https://github.com/surrealdb/surrealdb.java)

---

## Methods

### `.getBucket()` {#get-bucket}

Returns the name of the storage bucket containing the file.

```java title="Method Syntax"
fileRef.getBucket()
```

**Returns:** `String`

### `.getKey()` {#get-key}

Returns the unique key identifying the file within its bucket.

```java title="Method Syntax"
fileRef.getKey()
```

**Returns:** `String`

---

## Example

```java title="Working with file references"

try (Surreal db = new Surreal()) {
    db.connect("ws://localhost:8000");
    db.useNs("surrealdb").useDb("docs");
    db.signin(new RootCredential("root", "root"));

    Response response = db.query("SELECT avatar FROM user:tobie");
    Value result = response.take(0);

    if (result.isFile()) {
        FileRef file = result.getFile();
        String bucket = file.getBucket();
        String key = file.getKey();
    }
}
```

---

## See also

- [Value types](../../concepts/value-types.md) — Type mapping overview
- [Value](value.md) — The Value class reference
- [SurrealQL files](../../../../reference/query-language/language-primitives/data-types/files.md) — File storage in SurrealDB
