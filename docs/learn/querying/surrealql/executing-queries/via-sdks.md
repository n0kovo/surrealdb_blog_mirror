---
position: 3
title: Via SDKs
description: Query SurrealDB programmatically using one of the official SDKs available for Rust, JavaScript, Python, Go, Java, .NET, and PHP.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/querying/surrealql/executing-queries/via-sdks.mdx"
---

# Querying via SDKs

SurrealDB supports a number of methods for connecting to the database and performing data queries. Each SDK has its own set of methods for connecting to the database and performing data queries.

In each SDK, you can connect to the database using a local or remote connection. Once you are connected, you can start performing data queries. Here is a list of all the Supported SDKs:

- **[Rust](../../../../languages/rust/overview.md)**
- **[JavaScript](../../../../languages/javascript/concepts/connecting-to-surrealdb.md)**
- **[TypeScript](../../../../languages/javascript/concepts/connecting-to-surrealdb.md)**
- **[Python](../../../../languages/python/index.md)**
- **[Node.js](../../../../languages/javascript/engines/node.md)**
- **[.NET](../../../../languages/dotnet/index.md)**
- **[Golang](../../../../languages/golang/index.md)**
- **[Java](../../../../languages/java/index.md)**
- **[PHP](../../../../languages/php/index.md)**

## Writing SurrealQL queries in SDKs

In addition to the variety of methods provided by the SDKs to perform data queries, the `query` method works as a catch-all way to run [SurrealQL statements](../../../../reference/query-language/index.md) against the database.

  
**Javascript**

```ts title="Method Syntax"
async db.query<T>(query, vars)
```

#### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `query`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `vars`
               <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Assigns variables which can be used in the query.
            </td>
        </tr>
    </tbody>
</table>

#### Example usage
```ts
type Person = {
	id: string;
	name: string;
};

// Assign the variable on the connection
const result = await db.query<[Person[], Person[]]>(
	'CREATE person SET name = "John"; SELECT * FROM type::table($tb);',
	{ tb: 'person' }
);

// Get the first result from the first query
const created = result[0].result[0];

// Get all of the results from the second query
const people = result[1].result;
```

`.query_raw()`

With `.query_raw()`, you will get back the raw RPC response. In contrast to the `.query()` method, this will not throw errors that occur in individual queries, but will rather give those back as a string, and this will include the time it took to execute the individual queries.

**PHP**

```php title="Method Syntax"
$db->query($query, $vars)
```

#### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `$query`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `$vars`
               <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Assigns variables which can be used in the query.
            </td>
        </tr>
    </tbody>
</table>

#### Example usage
```php
// Assign the variable on the connection
$result = db->query(
	'CREATE person SET name = "John"; SELECT * FROM type::table($tb);',
	[ "tb" => "person" ]
);

// Get the first result from the first query
$created = $result[0]->result[0];

// Get all of the results from the second query
$people = $result[1]->result;
```

**Python**

```python title="Method Syntax"
db.query(sql, vars)
```

#### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `sql`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `vars`
               <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Assigns variables which can be used in the query.
            </td>
        </tr>
    </tbody>
</table>

#### Example usage
```python
# Assign the variable on the connection
result = await db.query('CREATE person; SELECT * FROM type::table($tb)', {
	'tb': 'person',
})
# Get the first result from the first query
result[0]['result'][0]
# Get all of the results from the second query
result[1]['result']
```

**.NET**

```csharp title="Method Syntax"
await db.Query(sql)
```

#### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="col" data-label="Arguments">
                `sql`
                <label label="required" />
            </td>
            <td colspan="2" scope="col" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" data-label="Arguments">
                `cancellationToken`
               <label label="optional" />
            </td>
            <td colspan="2" scope="col" data-label="Description">
                The cancellationToken enables graceful cancellation of asynchronous operations.
            </td>
        </tr>
    </tbody>
</table>
  

#### Example usage

```csharp
// Execute query with params
const string table = "person";
var result = await db.Query($"CREATE person; SELECT * FROM type::table({table});");

// Get the first result from the first query
var created = result.GetValue<Person>(0);

// Get all of the results from the second query
var people = result.GetValue<List<Person>>(1);
```

  

`.RawQuery()` : Runs a set of SurrealQL statements against the database, based on a raw SurrealQL query.

```csharp title="Method Syntax"
await db.RawQuery(sql, params)
```

#### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="col" data-label="Arguments">
                `sql`
                <label label="required" />
            </td>
            <td colspan="2" scope="col" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" data-label="Arguments">
                `params`
               <label label="optional" />
            </td>
            <td colspan="2" scope="col" data-label="Description">
                Assigns variables which can be used in the query.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="col" data-label="Arguments">
                `cancellationToken`
               <label label="optional" />
            </td>
            <td colspan="2" scope="col" data-label="Description">
                The cancellationToken enables graceful cancellation of asynchronous operations.
            </td>
        </tr>
    </tbody>
</table>

#### Example usage
```csharp
// Assign the variable on the connection
var @params = new Dictionary<string, object> { { "table", "person" } };
var result = await db.RawQuery("CREATE person; SELECT * FROM type::table($table);", @params);

// Get the first result from the first query
var created = result.GetValue<Person>(0);

// Get all of the results from the second query
var people = result.GetValue<List<Person>>(1);
```

**Golang**

```go title="Method Syntax"
db.Query(sql, vars)
```

#### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `sql`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `vars`
               <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Assigns variables which can be used in the query.
            </td>
        </tr>
    </tbody>
</table>

#### Example usage
```go
// Assign the variable on the connection
result, err := db.Query("CREATE person; SELECT * FROM type::table($tb);", map[string]string{
	"tb": "person"
});
```

**Rust**

```rust title="Method Syntax"
db.query(sql).bind(vars)
```

#### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Arguments</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `sql`
                <label label="required" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Specifies the SurrealQL statements.
            </td>
        </tr>
        <tr>
            <td colspan="2" scope="row" data-label="Arguments">
                `vars`
               <label label="optional" />
            </td>
            <td colspan="2" scope="row" data-label="Description">
                Assigns variables which can be used in the query.
            </td>
        </tr>
    </tbody>
</table>

#### Example usage
```rust
// Run some queries
let sql = "
    CREATE person;
    SELECT * FROM type::table($table);
";
let mut result = db
    .query(sql)
    .bind(("table", "person"))
    .await?;
// Get the first result from the first query
let created: Option<Person> = result.take(0)?;
// Get all of the results from the second query
let people: Vec<Person> = result.take(1)?;
```

## Learn more

Learn more about the [SurrealQL query language](../../../../reference/query-language/index.md).
