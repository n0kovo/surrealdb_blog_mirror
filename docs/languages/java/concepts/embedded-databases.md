---
position: 10
title: Embedded databases
description: The Java SDK can run SurrealDB as an embedded in-process database for testing and standalone applications.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/concepts/embedded-databases.mdx"
---

# Embedded databases

The Java SDK can run SurrealDB as an embedded in-process database, eliminating the need for a separate server. Embedded databases use JNI to run the SurrealDB engine directly within your application, which removes network overhead and simplifies deployment for testing, prototyping, and standalone applications.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#connect">`db.connect(url)`</a></td>
			<td scope="row" data-label="Description">Connects using an embedded protocol</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#export-sql">`db.exportSql(path)`</a></td>
			<td scope="row" data-label="Description">Exports the database to a file</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/java/api/core/surreal#import-sql">`db.importSql(path)`</a></td>
			<td scope="row" data-label="Description">Imports data from a file</td>
		</tr>
	</tbody>
</table>

## Running an in-memory database

Use the `memory://` scheme to start an in-memory embedded database. All data is stored in memory and is lost when the connection closes. This is ideal for unit tests and rapid prototyping where persistence is not required.

```java
try (Surreal db = new Surreal()) {
    db.connect("memory://");
    db.useNs("main").useDb("main");
}
```

## Running a disk-based database

Use the `surrealkv://` scheme with a file path to start a disk-based embedded database. Data is persisted to the specified directory and survives application restarts.

```java
try (Surreal db = new Surreal()) {
    db.connect("surrealkv://path/to/database");
    db.useNs("app").useDb("main");
}
```

## Exporting and importing data

The [`.exportSql()`](../api/core/surreal.md#export-sql) method writes the current database contents to a SurrealQL file. The [`.importSql()`](../api/core/surreal.md#import-sql) method reads a SurrealQL file and applies it to the database.

```java
try (Surreal db = new Surreal()) {
    db.connect("surrealkv://path/to/database");
    db.useNs("app").useDb("main");

    db.exportSql("backup.surql");
    db.importSql("backup.surql");
}
```

## When to use embedded databases

Embedded databases are well suited for scenarios where running a separate SurrealDB server is unnecessary or impractical:

- **Testing** — use `memory://` for fast, isolated tests that start with a clean database on every run.
- **Desktop and mobile applications** — use `surrealkv://` to bundle a persistent database directly within the application.
- **CLI tools** — embed a database to store local state or configuration without requiring users to install SurrealDB.
- **Prototyping** — iterate quickly without managing a server process.

## Learn more

- [Surreal API reference](../api/core/surreal.md) for complete method signatures
- [Connecting to SurrealDB](connecting-to-surrealdb.md) for all connection protocols
- [SurrealDB deployment](../../../build/deployment/index.md) for production server deployment
- [SurrealDB CLI start](../../../reference/cli/surrealdb-cli/commands/start.md) for server configuration and storage backends
- [SurrealDB CLI import](../../../reference/cli/surrealdb-cli/commands/import.md) and [export](../../../reference/cli/surrealdb-cli/commands/export.md) for command-line data management
