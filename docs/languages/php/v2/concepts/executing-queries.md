---
position: 3
title: Executing queries
description: Run raw SurrealQL or use the fluent query builders for select, create, update, and delete in version 2 of the PHP SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v2/concepts/executing-queries.mdx"
---

# Executing queries

Version 2 of the PHP SDK gives you two ways to query SurrealDB: raw SurrealQL through `run()`, and fluent query builders such as `select()`, `create()`, `update()`, and `delete()`. The builders compile to the same parameter-bound queries you could write by hand, so you can mix the two freely.

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
            <td scope="row" data-label="Method"><a href="/docs/languages/php/v2/api/query-builders#run"> ` $db->run($surql, $bindings) `</a></td>
            <td scope="row" data-label="Description">Executes raw SurrealQL statements</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/php/v2/api/query-builders#select"> ` $db->select($target) `</a></td>
            <td scope="row" data-label="Description">Selects records from the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/php/v2/api/query-builders#create"> ` $db->create($target) `</a></td>
            <td scope="row" data-label="Description">Creates a new record</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/php/v2/api/query-builders#insert"> ` $db->insert($target, $data) `</a></td>
            <td scope="row" data-label="Description">Inserts one or many records</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/php/v2/api/query-builders#update"> ` $db->update($target) `</a></td>
            <td scope="row" data-label="Description">Updates existing records</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/php/v2/api/query-builders#delete"> ` $db->delete($target) `</a></td>
            <td scope="row" data-label="Description">Deletes records from the database</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method"><a href="/docs/languages/php/v2/api/query-builders#relate"> ` $db->relate($from, $edge, $to) `</a></td>
            <td scope="row" data-label="Description">Creates graph relationships between records</td>
        </tr>
    </tbody>
</table>

## Running raw SurrealQL

The `run()` method executes raw [SurrealQL statements](../../../../reference/query-language/statements/overview.md). Pass bindings as the second argument to inject values safely. It returns one result per statement.

```php
[$adults] = $db->run(
    'SELECT * FROM person WHERE age > $min_age',
    ['min_age' => 18],
);
```

For a multi-statement query, each result keeps its position in the returned list.

```php
[$people, $posts] = $db->run('
    SELECT * FROM person;
    SELECT * FROM post;
');
```

## Builders, execute, and compile

Every builder method returns a builder object. Call `execute()` to run it and get the result of the single statement, or `compile()` to get the [`BoundQuery`](../api/utilities.md#boundquery) without running it.

```php
$query = $db->select(new Table('person'))->where('age >= 18');

$result = $query->execute();   // runs the statement
$bound = $query->compile();    // BoundQuery: SurrealQL text + bindings
```

## Selecting records

The `select()` method reads records. Pass a [`Table`](../api/data-types.md#table) to read all records, or a [`RecordId`](../api/data-types.md#recordid) to read one. Chain `fields()`, `where()`, `start()`, `limit()`, and `fetch()` to refine the query.

```php
use SurrealDB\SDK\Types\Table;
use SurrealDB\SDK\Types\RecordId;

$everyone = $db->select(new Table('person'))->execute();

$tobie = $db->select(new RecordId('person', 'tobie'))->execute();

$page = $db->select(new Table('person'))
    ->fields('name', 'age')
    ->where('age >= 18')
    ->start(0)
    ->limit(10)
    ->fetch('posts')
    ->execute();
```

The `where()` method accepts a SurrealQL string for static conditions. For dynamic values, pass a `BoundQuery` so the values stay parameterised.

```php
use SurrealDB\SDK\Query\BoundQuery;

$db->select(new Table('person'))
    ->where(new BoundQuery('age >= $min', ['min' => 18]))
    ->execute();
```

## Creating records

The `create()` method starts a `CREATE`. Chain `content()` to set the record data. A `Table` generates a random ID; a `RecordId` creates the record with that ID.

```php
$db->create(new RecordId('person', 'tobie'))
    ->content(['name' => 'Tobie', 'age' => 32])
    ->execute();

$db->create(new Table('person'))
    ->content(['name' => 'Jaime'])
    ->execute();
```

## Inserting records

The `insert()` method inserts one or many records in a single statement. Pass a target table and the records, or pass the records alone when each contains its own ID.

```php
$db->insert(new Table('person'), [
    ['name' => 'Alice'],
    ['name' => 'Bob'],
])->execute();
```

Chain `relation()` to insert into a relation table (`INSERT RELATION`), or `ignore()` to skip records that already exist (`INSERT IGNORE`).

## Updating records

The `update()` and `upsert()` methods modify records. Choose a strategy by chaining `content()`, `merge()`, `replace()`, or `patch()`.

**Replace content**

Replace the record with new data. Fields not included are removed.

```php
$db->update(new RecordId('person', 'tobie'))
    ->content(['name' => 'Tobie', 'age' => 33])
    ->execute();
```

**Merge fields**

Merge new fields into the record. Existing fields stay unless overwritten.

```php
$db->update(new RecordId('person', 'tobie'))
    ->merge(['age' => 33])
    ->execute();
```

**JSON Patch**

Apply [JSON Patch](https://jsonpatch.com) operations for fine-grained edits.

```php
$db->update(new RecordId('person', 'tobie'))
    ->patch([
        ['op' => 'replace', 'path' => '/age', 'value' => 33],
        ['op' => 'add', 'path' => '/verified', 'value' => true],
    ])
    ->execute();
```

You can filter which records to update with `where()`.

```php
$db->update(new Table('person'))
    ->merge(['verified' => true])
    ->where('age >= 18')
    ->execute();
```

## Deleting records

The `delete()` method removes records. It defaults to `RETURN BEFORE`, so the deleted records are returned.

```php
$db->delete(new RecordId('person', 'tobie'))->execute();

$db->delete(new Table('person'))->execute();
```

## Creating graph relationships

The `relate()` method creates edges in SurrealDB's [graph model](../../../../reference/query-language/statements/relate.md). Pass the source, the edge table, and the target, with optional edge data.

```php
$db->relate(
    new RecordId('person', 'tobie'),
    new Table('likes'),
    new RecordId('post', 'surrealdb'),
    ['since' => 2024],
)->execute();
```

## Running functions

The `call()` method invokes a SurrealQL or SurrealML function by name. Pass an optional version and a list of arguments.

```php
$total = $db->call('fn::calculate_total', null, [100, 0.2])->execute();

$prediction = $db->call('ml::predict', '1.0.0', [$input])->execute();
```

## Setting session parameters

Use `let()` to define a parameter on the session and `unset()` to remove it. Session parameters are available in later queries as `$name`.

```php
$db->let('current_user', ['first' => 'Tobie']);

$db->run('CREATE post SET author = $current_user');

$db->unset('current_user');
```

## Learn more

- [Query Builders API reference](../api/query-builders.md) for every builder method
- [Live queries](live-queries.md) for real-time subscriptions
- [Transactions](transactions.md) for atomic multi-statement operations
- [SurrealQL statements](../../../../reference/query-language/statements/overview.md) for the query language reference
