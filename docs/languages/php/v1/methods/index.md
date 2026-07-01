---
position: 1
title: SDK methods
description: List of methods available in the SurrealDB SDK for PHP. Learn how to connect to a database, query data, and manage authentication.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v1/methods/index.mdx"
---

# SDK methods

The SurrealDB SDK for PHP has a single SurrealDB class that provides methods for querying a remote SurrealDB database.
The class is designed to be simple to use and easy to understand for developers who are new to PHP or SurrealDB.
This page lists out the methods that are available in the SurrealDB class.

## Initialization methods

<table>
	<thead>
		<tr>
			<th scope="col">Function</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/connect"> ` $db->connect($url, $options) `</a></td>
			<td scope="row" data-label="Description">Connects to a local or remote database endpoint</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/close"> ` $db->close() `</a></td>
			<td scope="row" data-label="Description">Closes the persistent connection to the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/use"> ` $db->use($options)`</a></td>
			<td scope="row" data-label="Description">Switch to a specific namespace and database</td>
		</tr>
		<tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/let"> `$db->let($key,$val)`</a></td>
            <td scope="row" data-label="Description">Assigns a value as a parameter for this connection</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/unset"> `$db->unset($key)`</a></td>
            <td scope="row" data-label="Description">Removes a parameter for this connection</td>
        </tr>
	</tbody>
</table>

## Query methods

<table>
    <thead>
        <tr>
            <th scope="col">Function</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/query"> `$db->query($sql,$vars)`</a></td>
            <td scope="row" data-label="Description">Runs a set of [SurrealQL statements](../../../../reference/query-language/index.md) against the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/select"> `$db->select($thing)`</a></td>
            <td scope="row" data-label="Description">Selects all records in a table, or a specific record</td>
        </tr>
    </tbody>
</table>

## Mutation methods

<table>
    <thead>
        <tr>
            <th scope="col">Function</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/create"> `$db->create($thing,$data)`</a></td>
            <td scope="row" data-label="Description">Creates a record in the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/insert"> `$db->insert($thing,$data)`</a></td>
            <td scope="row" data-label="Description">Inserts one or multiple records in the database</td>
        </tr>
		<tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/insert-relation"> `$db->insertRelation($thing,$data)`</a></td>
            <td scope="row" data-label="Description">Inserts one or multiple records in the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/update"> `$db->update($thing,$data)`</a></td>
            <td scope="row" data-label="Description">Updates all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/merge"> `$db->merge($thing,$data)`</a></td>
            <td scope="row" data-label="Description">Modifies all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/patch"> `$db->patch($thing,$data)`</a></td>
            <td scope="row" data-label="Description">Applies JSON Patch changes to all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/delete"> `$db->delete($thing,$data)`</a></td>
            <td scope="row" data-label="Description">Deletes all records, or a specific record</td>
        </tr>
    </tbody>
</table>

## Authentication methods

<table>
    <thead>
        <tr>
            <th scope="col">Function</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/signup"> `$db->signup($vars)`</a></td>
            <td scope="row" data-label="Description">Signs this connection up to a specific authentication scope</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/signin"> `$db->signin($vars)`</a></td>
            <td scope="row" data-label="Description">Signs this connection in to a specific authentication scope</td>
        </tr>
		<tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/invalidate"> `$db->invalidate()`</a></td>
            <td scope="row" data-label="Description">Invalidates the authentication for the current connection</td>
        </tr>
        <tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/authenticate"> `$db->authenticate(token)`</a></td>
            <td scope="row" data-label="Description">Authenticates the current connection with a JWT token</td>
        </tr>
		<tr>
            <td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/info"> `$db->info()`</a></td>
            <td scope="row" data-label="Description">Returns the record of an authenticated scope user</td>
        </tr>
    </tbody>
</table>

## Utility methods

<table>
	<thead>
		<tr>
			<th scope="col">Function</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/import"> `$db->import($content, $username, $password)`</a></td>
			<td scope="row" data-label="Description">Imports data into the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/export"> `$db->export($username, $password)`</a></td>
			<td scope="row" data-label="Description">Exports data from the database</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/health"> `$db->health()`</a></td>
			<td scope="row" data-label="Description">Checks wether the database is running and the storage engine is healthy</td>
		</tr>
		<tr>
			<td scope="row" data-label="Function"><a href="/docs/languages/php/v1/methods/status"> `$db->status()`</a></td>
			<td scope="row" data-label="Description">Wether the database is running or is reachable</td>
		</tr>
	</tbody>
</table>
