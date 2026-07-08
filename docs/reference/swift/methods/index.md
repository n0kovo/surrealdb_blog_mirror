---
position: 1
title: SDK methods
description: The Swift SDK for SurrealDB enables simple and advanced querying of a remote database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/swift/methods/index.mdx"
---

# SDK methods

The Swift SDK exposes its functionality through the `SurrealHTTPClient` and `SurrealWebSocketClient` types, which share the same API. This page lists the methods available on a connected client.

## Initialization methods

<table>
    <thead>
        <tr>
            <th scope="col">Method</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/connect"> `client.connect()`</a></td>
            <td scope="row" data-label="Description">Connects the client to the underlying endpoint</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/use"> `client.use(namespace, database)`</a></td>
            <td scope="row" data-label="Description">Switch to a specific namespace and database</td>
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
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/signup"> `client.signup(credentials)`</a></td>
            <td scope="row" data-label="Description">Signs this connection up to a specific authentication access</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/signin"> `client.signin(credentials)`</a></td>
            <td scope="row" data-label="Description">Signs this connection in to a specific authentication level</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/authenticate"> `client.authenticate(token)`</a></td>
            <td scope="row" data-label="Description">Authenticates the current connection with a JWT token</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/invalidate"> `client.invalidate()`</a></td>
            <td scope="row" data-label="Description">Invalidates the authentication for the current connection</td>
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
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/select"> `client.select(model)`</a></td>
            <td scope="row" data-label="Description">Selects all records in a table, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/query"> `client.query(query)`</a></td>
            <td scope="row" data-label="Description">Runs a query built with the query DSL or macros</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/query-raw"> `client.queryRaw(sql, bindings)`</a></td>
            <td scope="row" data-label="Description">Runs a raw SurrealQL query with bound parameters</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/live"> `client.live(query)`</a></td>
            <td scope="row" data-label="Description">Subscribes to changes via a live query (WebSocket only)</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/kill"> `client.kill(liveQueryID)`</a></td>
            <td scope="row" data-label="Description">Kills a running live query</td>
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
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/create"> `client.create(model)`</a></td>
            <td scope="row" data-label="Description">Creates a record in the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/update"> `client.update(model)`</a></td>
            <td scope="row" data-label="Description">Updates matching records, or a specific record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/upsert"> `client.upsert(model)`</a></td>
            <td scope="row" data-label="Description">Creates or updates matching records</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/reference/swift/methods/delete"> `client.delete(model)`</a></td>
            <td scope="row" data-label="Description">Deletes matching records, or a specific record</td>
        </tr>
    </tbody>
</table>
