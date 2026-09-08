---
position: 1
title: SDK methods
description: The .NET SDK for SurrealDB has a single SurrealDB class that provides methods for querying a remote SurrealDB database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/dotnet/methods/index.mdx"
---

# SDK methods

The .NET SDK for SurrealDB has a single SurrealDB class that provides methods for querying a remote SurrealDB database.
The class is designed to be simple to use and easy to understand for developers who are new to .NET or SurrealDB.
This page lists out the methods that are available in the SurrealDB class.

## Initialisation methods

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/connect"> ` db.Connect() `</a></td>
			<td scope="row" data-label="Description">Connects the client to the underlying endpoint, also improving performance to avoid cold starts</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/use"> ` db.Use(namespace, database)`</a></td>
			<td scope="row" data-label="Description">Switch to a specific namespace and database</td>
		</tr>
		<tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/set"> `db.Set(key, value)`</a></td>
            <td scope="row" data-label="Description">Assigns a value as a parameter for this connection</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/unset"> `db.Unset(key)`</a></td>
            <td scope="row" data-label="Description">Removes a parameter for this connection</td>
        </tr>
			<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/health"> ` db.Health() `</a></td>
			<td scope="row" data-label="Description">Checks the status of the database server and storage engine</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/version"> ` db.Version() `</a></td>
			<td scope="row" data-label="Description">Retrieves the version of the SurrealDB instance</td>
		</tr>
</tbody>
</table>

## Query methods

<table>
    <thead>
        <tr>
            <th scope="col">Method</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/query"> `db.Query&lt;T&gt;(sql)`</a></td>
            <td scope="row" data-label="Description">Runs a set of [SurrealQL statements](../../query-language/index.md) against the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/raw-query"> `db.RawQuery&lt;T&gt;(sql, vars)`</a></td>
            <td scope="row" data-label="Description">Runs a set of [SurrealQL statements](../../query-language/index.md) against the database, based on a raw SurrealQL query</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/select"> `db.Select&lt;T&gt;(thing)`</a></td>
            <td scope="row" data-label="Description">Selects all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/core/streaming#live-query"> `db.LiveQuery&lt;T&gt;(sql)`</a></td>
            <td scope="row" data-label="Description">Initiate a live query from a [SurrealQL statement](../../query-language/index.md)</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/core/streaming#live-raw-query"> `db.LiveRawQuery&lt;T&gt;(sql)`</a></td>
            <td scope="row" data-label="Description">Initiate a live query from a [SurrealQL statement](../../query-language/index.md), based on a raw SurrealQL query</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/core/streaming#live-table"> `db.LiveTable&lt;T&gt;(table, diff)`</a></td>
            <td scope="row" data-label="Description">Initiate a live query from a table</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/core/streaming#listen-live"> `db.ListenLive&lt;T&gt;(queryUuid)`</a></td>
            <td scope="row" data-label="Description">Listen responses from an existing live query</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/core/streaming#kill"> `db.Kill(queryUuid)`</a></td>
            <td scope="row" data-label="Description">Kill a running live query</td>
        </tr>
    		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/run"> ` db.Run(name, version, args) `</a></td>
			<td scope="row" data-label="Description">Runs a SurrealQL function</td>
		</tr>
</tbody>
</table>

## Mutation methods

<table>
    <thead>
        <tr>
            <th scope="col">Method</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/create"> `db.Create&lt;T&gt;(thing, data)`</a></td>
            <td scope="row" data-label="Description">Creates a record in the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/insert"> `db.Insert&lt;T&gt;(thing, data)`</a></td>
            <td scope="row" data-label="Description">Inserts one or multiple records in the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/update"> `db.Update&lt;T&gt;(thing, data)`</a></td>
            <td scope="row" data-label="Description">Updates all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/upsert"> `db.Upsert&lt;T&gt;(thing, data)`</a></td>
            <td scope="row" data-label="Description">Creates or updates a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/merge"> `db.Merge&lt;T&gt;(thing, data)`</a></td>
            <td scope="row" data-label="Description">Modifies all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/patch"> `db.Patch&lt;T&gt;(thing, data)`</a></td>
            <td scope="row" data-label="Description">Applies JSON Patch changes to all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/delete"> `db.Delete(thing)`</a></td>
            <td scope="row" data-label="Description">Deletes all records, or a specific record</td>
        </tr>
    		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/relate"> ` db.Relate(table, @in, @out, data) `</a></td>
			<td scope="row" data-label="Description">Creates a graph relation between two records</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/insert-relation"> ` db.InsertRelation&lt;T&gt;(table, data) `</a></td>
			<td scope="row" data-label="Description">Inserts one or more graph relations into a table</td>
		</tr>
</tbody>
</table>

## Live query methods

A live query streams changes as they happen. Start one from a statement or a table, listen to the stream it returns, then stop it with the query's id.

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/live-query"> ` db.LiveQuery&lt;T&gt;(sql) `</a></td>
			<td scope="row" data-label="Description">Initiates a live query from a SurrealQL statement</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/live-raw-query"> ` db.LiveRawQuery&lt;T&gt;(sql, params) `</a></td>
			<td scope="row" data-label="Description">Initiates a live query from a raw SurrealQL statement with parameters</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/live-table"> ` db.LiveTable&lt;T&gt;(table, diff) `</a></td>
			<td scope="row" data-label="Description">Initiates a live query on a whole table</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/listen_live"> ` db.ListenLive&lt;T&gt;(queryUuid) `</a></td>
			<td scope="row" data-label="Description">Listens for changes on a live query that is already running</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/kill"> ` db.Kill(queryUuid) `</a></td>
			<td scope="row" data-label="Description">Stops a running live query</td>
		</tr>
	</tbody>
</table>

## Data management methods

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/export"> ` db.Export(options) `</a></td>
			<td scope="row" data-label="Description">Exports the database as a SurrealQL script</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/import"> ` db.Import(string) `</a></td>
			<td scope="row" data-label="Description">Imports a SurrealQL script into the database</td>
		</tr>
	</tbody>
</table>

## Authentication methods

<table>
    <thead>
        <tr>
            <th scope="col">Method</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/signup"> `db.SignUp(credentials)`</a></td>
            <td scope="row" data-label="Description">Signs this connection up to a specific authentication scope</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/signin"> `db.SignIn(credentials)`</a></td>
            <td scope="row" data-label="Description">Signs this connection in to a specific authentication scope</td>
        </tr>
		<tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/invalidate"> `db.Invalidate()`</a></td>
            <td scope="row" data-label="Description">Invalidates the authentication for the current connection</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/authenticate"> `db.Authenticate(token)`</a></td>
            <td scope="row" data-label="Description">Authenticates the current connection with a JWT token</td>
        </tr>
		<tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/dotnet/methods/info"> `db.Info&lt;T&gt;()`</a></td>
            <td scope="row" data-label="Description">Returns the record of an authenticated scope user</td>
        </tr>
    </tbody>
</table>
