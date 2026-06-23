---
position: 4
title: Query builders
description: Build SurrealQL statements fluently with the Mojo SDK query builders.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/mojo/concepts/query-builders.mdx"
---

# Query builders

The Mojo SDK ships a set of fluent builders that construct SurrealQL statements for you. Each builder is `Copyable` and `Movable`, so you can chain calls or pass it around, and each has a `build()` method that returns the statement as a string.

```python
var qb = client.select_builder("person")
    .fields("id, name, age")
    .where_clause("age >= 18")
    .order_by("age DESC")
    .limit(20)

var resp = client.query_select(qb)
```

`query_select()` runs a `SelectBuilder`. The generic `query_builder()` runs any builder via its `build()` output.

## Available builders

The client exposes a factory method for each builder.

<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Builder</th>
            <th colspan="2" scope="col">Factory</th>
            <th colspan="2" scope="col">Methods</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Builder">`SelectBuilder`</td>
            <td colspan="2" scope="row" data-label="Factory">`select_builder(target)`</td>
            <td colspan="2" scope="row" data-label="Methods">`fields`, `where_clause`, `order_by`, `limit`, `start`, `fetch`</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Builder">`CreateBuilder`</td>
            <td colspan="2" scope="row" data-label="Factory">`create_builder(target)`</td>
            <td colspan="2" scope="row" data-label="Methods">`content`, `set_field`</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Builder">`UpdateBuilder`</td>
            <td colspan="2" scope="row" data-label="Factory">`update_builder(target)`</td>
            <td colspan="2" scope="row" data-label="Methods">`content`, `merge`, `patch`, `replace`, `where_clause`</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Builder">`UpsertBuilder`</td>
            <td colspan="2" scope="row" data-label="Factory">`upsert_builder(target)`</td>
            <td colspan="2" scope="row" data-label="Methods">`content`, `merge`</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Builder">`DeleteBuilder`</td>
            <td colspan="2" scope="row" data-label="Factory">`delete_builder(target)`</td>
            <td colspan="2" scope="row" data-label="Methods">`where_clause`</td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Builder">`InsertBuilder`</td>
            <td colspan="2" scope="row" data-label="Factory">`insert_builder(table)`</td>
            <td colspan="2" scope="row" data-label="Methods">`values`, `relation`</td>
        </tr>
    </tbody>
</table>

## Examples

Build and inspect a statement without running it:

```python
var qb = client.select_builder("person")
    .fields("name, age")
    .where_clause("age >= 18")
    .limit(10)

print(qb.build())  # SELECT name, age FROM person WHERE age >= 18 LIMIT 10;
```

Create a record:

```python
var cb = client.create_builder("person").content('{ "name": "Chiru" }')
var resp = client.query(cb.build())
```

> [!NOTE]
> The older `QueryBuilder` is kept for backwards compatibility. New code should use the builders above.
