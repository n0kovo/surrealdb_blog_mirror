---
title: "Release v1.0.0-beta.6"
slug: "release-v1-0-0-beta-6"
date: "2022-08-13T00:00:00.000Z"
categories:
  - "releases"
read_time: "1 min read"
summary: "Add command-line SurrealQL REPL for quick querying of a database, log username at server startup when root authentication is enabled, enable SurrealDB server to be configured using environment variables, implement config definition key and value caching within a transaction, and much more."
source: "https://surrealdb.com/blog/release-v1-0-0-beta-6"
cover: "../../assets/070db1ddc2c955d9.jpg"
---

# Release v1.0.0-beta.6

![Release v1.0.0-beta.6](../../assets/070db1ddc2c955d9.jpg)

- Add command-line SurrealQL REPL for quick querying of a database
- Log username at server startup when root authentication is enabled
- Enable SurrealDB server to be configured using environment variables
- Implement config definition key and value caching within a transaction
- Add array::sort functions for sorting of arrays and array fields
- Ensure an error is returned when selecting from a non-existent table in strict mode
- Allow polymorphic remote record constraints in DEFINE FIELD statements
- Fix bug with SQL export, where DEFINE INDEX statements were not exported
- Fix bug where multi-yield path expressions with multiple alias outputs were returning nested arrays
- Fix bug where aliased field was not output when fetching a multi-yield expressions with a final alias yield

## SurrealDB REPL

SurrealDB now supports the ability to start a command-line REPL to query a local or remote database from the terminal.

```cli
user@localhost % surreal sql --conn http://localhost:8000 --user root --pass root --ns test --db test
```

/releases
