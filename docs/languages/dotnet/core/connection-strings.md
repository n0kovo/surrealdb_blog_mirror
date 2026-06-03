---
position: 9
title: Connection strings
description: The .NET SDK for SurrealDB supports the familiar concept of ConnectionString.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/core/connection-strings.mdx"
---

# Connection strings

Connection Strings are an easy way to configure your application to connect to a SurrealDB instance.
They are stored in the `appsettings.json` file and can be used to configure the `SurrealDbClient`.

In general, it is known as a best practice to:

- set a development Connection String in `appsettings.Development.json`,
- store your production Connection String in a Secret environment variable, or even better in a Vault.

<table>
  <thead>
    <tr>
      <th scope="col">Keys</th>
      <th colspan="2" scope="col">
        Description
      </th>
      <th scope="col">Aliases</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Keys">
        `Endpoint`
        <label label="required" />
      </td>
      <td colspan="2" scope="row" data-label="Description">
        The database endpoint to connect to.   

        The disctinction between `Server` and `Client` can
        help you ensure you only call a distant database (server mode) or a
        local database (client mode).
      </td>
      <td scope="row" data-label="Aliases">
        `Server`
        `Client`
      </td>
    </tr>
    <tr>
      <td scope="row" data-label="Keys">
        `Namespace`
        <label label="optional" />
      </td>
      <td colspan="2" scope="row" data-label="Description">
        Switches to a specific namespace.
      </td>
      <td scope="row" data-label="Aliases">
        `NS`
      </td>
    </tr>
    <tr>
      <td scope="row" data-label="Keys">
        `Database`
        <label label="optional" />
      </td>
      <td colspan="2" scope="row" data-label="Description">
        Switches to a specific database.
      </td>
      <td scope="row" data-label="Aliases">
        `DB`
      </td>
    </tr>
    <tr>
      <td scope="row" data-label="Keys">
        `Username`
        <label label="optional" />
      </td>
      <td colspan="2" scope="row" data-label="Description">
        Username used to have root access.
      </td>
      <td scope="row" data-label="Aliases">
        `User`
      </td>
    </tr>
    <tr>
      <td scope="row" data-label="Keys">
        `Password`
        <label label="optional" />
      </td>
      <td colspan="2" scope="row" data-label="Description">
        Password used to have root access.
      </td>
      <td scope="row" data-label="Aliases">
        `Pass`
      </td>
    </tr>
    <tr>
      <td scope="row" data-label="Keys">
        `Token`
        <label label="optional" />
      </td>
      <td colspan="2" scope="row" data-label="Description">
        Token (JWT) used to have user access.
      </td>
      <td scope="row" data-label="Aliases"></td>
    </tr>
    <tr>
      <td scope="row" data-label="Keys">
        `AuthLevel`
        <label label="optional" />
      </td>
      <td colspan="2" scope="row" data-label="Description">
        Auth level when connecting to the SurrealDB instance.   

        Valid options are `Root`, `Namespace` or{" "}
        `Database`.   

        Defaults to `Root`.
      </td>
      <td scope="row" data-label="Aliases"></td>
    </tr>
  </tbody>
</table>

## Examples

Here is a couple of examples of Connection Strings:

```sh
Server=http://127.0.0.1:8000;Namespace=test;Database=test;Username=root;Password=root
```

```sh
Endpoint=http://127.0.0.1:8000;NS=test;DB=test;User=root;Pass=root
```

```sh
Server=ws://127.0.0.1:8000;AuthLevel=Namespace;NS=test;DB=test;User=root;Pass=root
```

```sh
Client=mem://;Namespace=test;Database=test
```
