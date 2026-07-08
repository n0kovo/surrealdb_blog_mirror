---
position: 1
title: SDK methods
description: The SurrealDB SDK for Rust enables simple and advanced querying of a remote or embedded database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/rust/methods/index.mdx"
---

# SDK methods

Most methods in the SurrealDB SDK involve either working with or creating an instance of the [`Surreal`](https://docs.rs/surrealdb/latest/surrealdb/struct.Surreal.html) struct, which serves as the database client instance for embedded or remote databases.

The table below lists documented methods **in alphabetical order** (by page name).

## All methods

<table>
	<thead>
		<tr>
			<th scope="col">Function</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/authenticate"> `db.authenticate()`</a></td>
			<td scope="row" data-label="Description">Authenticates the current connection with a JWT token</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/begin"> `db.begin()`</a></td>
			<td scope="row" data-label="Description">Start a session-scoped multi-statement transaction, returning a `Transaction` handle (commit, cancel, query, and CRUD)</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/connect"> `db.connect()`</a></td>
			<td scope="row" data-label="Description">Connects to a local or remote database endpoint</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/create"> `db.create()`</a></td>
			<td scope="row" data-label="Description">Creates a record in the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/delete"> `db.delete()`</a></td>
			<td scope="row" data-label="Description">Deletes all records, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/export"> `db.export()`</a></td>
			<td scope="row" data-label="Description">Exports the database to a file or a live stream of bytes</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/get"> `value.get()`</a></td>
			<td scope="row" data-label="Description">On `Value` (and query results), reads a field on an object or an index in an array</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/health"> `db.health()`</a></td>
			<td scope="row" data-label="Description">Runs a health check to verify the server accepts commands</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/import"> `db.import()`</a></td>
			<td scope="row" data-label="Description">Imports the contents of another database from a file</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/init"> `Surreal::init()`</a></td>
			<td scope="row" data-label="Description">Initializes a non-connected instance of the database client</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/insert"> `db.insert()`</a></td>
			<td scope="row" data-label="Description">Inserts one or multiple records or relations in the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/invalidate"> `db.invalidate()`</a></td>
			<td scope="row" data-label="Description">Invalidates the authentication for the current connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/new"> `Surreal::new()`</a></td>
			<td scope="row" data-label="Description">Initializes a connected instance of the database client</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/query"> `db.query()`</a></td>
			<td scope="row" data-label="Description">Runs a set of [SurrealQL statements](../../query-language/index.md) against the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/run"> `db.run()`</a></td>
			<td scope="row" data-label="Description">Runs a SurrealQL function</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/select"> `db.select()`</a></td>
			<td scope="row" data-label="Description">Selects all records in a table, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/select-live"> `db.select().live()`</a></td>
			<td scope="row" data-label="Description">Performs a LIVE SELECT query on the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/set"> `db.set()`</a></td>
			<td scope="row" data-label="Description">Assigns a value as a parameter for this connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/signin"> `db.signin()`</a></td>
			<td scope="row" data-label="Description">Signs this connection in to a specific authentication scope</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/signup"> `db.signup()`</a></td>
			<td scope="row" data-label="Description">Signs this connection up to a specific authentication scope</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/unset"> `db.unset()`</a></td>
			<td scope="row" data-label="Description">Removes a parameter for this connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/update"> `db.update()`</a></td>
			<td scope="row" data-label="Description">Updates all records in a table, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/upsert"> `db.upsert()`</a></td>
			<td scope="row" data-label="Description">Upserts all records in a table, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/use"> `db.use_ns().use_db()`</a></td>
			<td scope="row" data-label="Description">Switch to a specific namespace and database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/use-defaults"> `db.use_defaults()`</a></td>
			<td scope="row" data-label="Description">Select the default namespace and database for this connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/version"> `db.version()`</a></td>
			<td scope="row" data-label="Description">Returns the current database version</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/reference/rust/methods/wait-for"> `db.wait_for()`</a></td>
			<td scope="row" data-label="Description">Blocks until a connection or database session event (such as `WaitFor::Connection`) is ready</td>
		</tr>
	</tbody>
</table>
