---
position: 1
title: SDK methods
description: The full method reference for the SurrealDB Mojo SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/methods/index.mdx"
---

# SDK methods

Most methods in the SurrealDB Mojo SDK are called on an instance of `AsyncSurrealClient` or its blocking wrapper `SurrealClient`. Both expose the same surface.

The table below lists documented methods **in alphabetical order** (by page name).

## All methods

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/api">`client.api()`</a></td>
			<td scope="row" data-label="Description">Calls a custom API handler defined on the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/authenticate">`client.authenticate()`</a></td>
			<td scope="row" data-label="Description">Authenticates the current connection with a token</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/begin-transaction">`client.begin_transaction()`</a></td>
			<td scope="row" data-label="Description">Starts a session-scoped transaction, returning a handle</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/call">`client.call()`</a></td>
			<td scope="row" data-label="Description">Runs a SurrealQL function</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/close">`client.close()`</a></td>
			<td scope="row" data-label="Description">Closes the connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/connect">`client.connect()`</a></td>
			<td scope="row" data-label="Description">Connects to a database endpoint</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/create">`client.create()`</a></td>
			<td scope="row" data-label="Description">Creates a record in the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/delete">`client.delete()`</a></td>
			<td scope="row" data-label="Description">Deletes all records, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/health">`client.health()`</a></td>
			<td scope="row" data-label="Description">Runs a health check against the server</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/insert">`client.insert()`</a></td>
			<td scope="row" data-label="Description">Inserts one or more records into a table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/insert-relation">`client.insert_relation()`</a></td>
			<td scope="row" data-label="Description">Inserts one or more relations into a table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/invalidate">`client.invalidate()`</a></td>
			<td scope="row" data-label="Description">Invalidates the authentication for the current connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/kill">`client.kill()`</a></td>
			<td scope="row" data-label="Description">Stops a running live query</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/live">`client.live_query()`</a></td>
			<td scope="row" data-label="Description">Starts a live query on a table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/merge">`client.merge()`</a></td>
			<td scope="row" data-label="Description">Merges data into a record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/patch">`client.patch()`</a></td>
			<td scope="row" data-label="Description">Applies a JSON Patch to a record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/query">`client.query()`</a></td>
			<td scope="row" data-label="Description">Runs a set of SurrealQL statements against the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/select">`client.select()`</a></td>
			<td scope="row" data-label="Description">Selects all records in a table, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/set">`client.set()`</a></td>
			<td scope="row" data-label="Description">Assigns a value as a parameter for this connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/signin">`client.signin()`</a></td>
			<td scope="row" data-label="Description">Signs in to the database with credentials</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/signup">`client.signup()`</a></td>
			<td scope="row" data-label="Description">Signs up to a record-access method</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/transaction-multi">`client.transaction_multi()`</a></td>
			<td scope="row" data-label="Description">Runs a list of statements as one atomic transaction</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/unset">`client.unset()`</a></td>
			<td scope="row" data-label="Description">Removes a parameter for this connection</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/update">`client.update()`</a></td>
			<td scope="row" data-label="Description">Updates all records in a table, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/upsert">`client.upsert()`</a></td>
			<td scope="row" data-label="Description">Upserts all records in a table, or a specific record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/use">`client.use()`</a></td>
			<td scope="row" data-label="Description">Switches to a specific namespace and database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/mojo/methods/version">`client.version()`</a></td>
			<td scope="row" data-label="Description">Returns the database version</td>
		</tr>
	</tbody>
</table>
