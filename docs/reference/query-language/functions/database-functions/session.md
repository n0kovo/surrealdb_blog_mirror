---
position: 22
title: Session
description: These functions return information about the current SurrealDB session.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/functions/database-functions/session.mdx"
---

# Session functions

These functions return information about the current SurrealDB session.

<table>
  <thead>
    <tr>
      <th scope="col">Function</th>
      <th scope="col">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessionac">`session::ac()`</a></td>
      <td scope="row" data-label="Description">Returns the current user's access method</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessiondb">`session::db()`</a></td>
      <td scope="row" data-label="Description">Returns the currently selected database</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessionid">`session::id()`</a></td>
      <td scope="row" data-label="Description">Returns the current user's session ID</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessionip">`session::ip()`</a></td>
      <td scope="row" data-label="Description">Returns the current user's session IP address</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessionns">`session::ns()`</a></td>
      <td scope="row" data-label="Description">Returns the currently selected namespace</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessionorigin">`session::origin()`</a></td>
      <td scope="row" data-label="Description">Returns the current user's HTTP origin</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessionrd">`session::rd()`</a></td>
      <td scope="row" data-label="Description">Returns the current user's record authentication data</td>
    </tr>
    <tr>
      <td scope="row" data-label="Function"><a href="#sessiontoken">`session::token()`</a></td>
      <td scope="row" data-label="Description">Returns the current user's authentication token</td>
    </tr>
  </tbody>
</table>

## `session::ac`

*Since v2.0.0*

> [!NOTE]
> This function was known as `session::sc` in versions of SurrealDB before 2.0. The behaviour has not changed.

The `session::ac` function returns the current user's access method.

```surql title="API DEFINITION"
session::ac() -> string
```

The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN session::ac();

"user"
```

  
  

## `session::db`

The `session::db` function returns the currently selected database.

```surql title="API DEFINITION"
session::db() -> string
```
The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN session::db();

"my_db"
```

  

## `session::id`

The `session::id` function returns the current user's session ID.

```surql title="API DEFINITION"
session::id() -> string
```
The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN session::id();

"I895rKuixHwCNIduyBIYH2M0Pga7oUmWnng5exEE4a7EB942GVElGrnRhE5scF5d"
```

  

## `session::ip`

The `session::ip` function returns the current user's session IP address.

```surql title="API DEFINITION"
session::ip() -> string
```
The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN session::ip();

"2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF"
```

  

## `session::ns`

The `session::ns` function returns the currently selected namespace.

```surql title="API DEFINITION"
session::ns() -> string
```
The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN session::ns();

"my_ns"
```

  

## `session::origin`

The `session::origin` function returns the current user's HTTP origin.

```surql title="API DEFINITION"
session::origin() -> string
```
The following example shows this function, and its output, when used in a [`RETURN`](../../statements/return.md) statement:

```surql
RETURN session::origin();

"http://localhost:3000"
```

  

## `session::rd`

*Since v2.0.0*

The `session::rd` function returns the current user's record authentication.

```surql title="API DEFINITION"
session::rd() -> string
```

## `session::token`

The `session::token` function returns the current authentication token.

```surql title="API DEFINITION"
session::token() -> string
```
