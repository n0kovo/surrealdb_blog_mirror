---
position: 5
title: Embedding
description: The documentation for embedding SurrealDB within .NET.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/embedding.mdx"
---

# Embedding in .NET

SurrealDB is designed to be run in many different ways and in many environments.
Due to the [separation of the storage and compute](../../architecture.md) layers, SurrealDB can be run in embedded mode, from within a number of different language environments.
In .NET, SurrealDB can be run as an [in-memory database](#memory-provider), or it can persist data using a [file-based storage engine](#file-providers). 

## Memory provider

The memory provider is a simple in-memory database that is useful in some contexts.
It can be extremely useful for testing scenarios, or for small applications that do not require persistence.

```bash
dotnet add package SurrealDb.Embedded.InMemory
```

### Consume the provider as is

The simplest way to use an in-memory database instance of SurrealDB is to create an instance of the `SurrealDbMemoryClient` class.

```csharp
// highlight-next-line
using var db = new SurrealDbMemoryClient();

const string TABLE = "person";

var person = new Person
{
    Title = "Founder & CEO",
    Name = new() { FirstName = "Tobie", LastName = "Morgan Hitchcock" },
    Marketing = true
};
var created = await db.Create(TABLE, person);
Console.WriteLine(ToJsonString(created));
```

### Consume the provider via dependency injection

Following the .NET Dependency Injection pattern, you can register the in-memory provider using the `AddInMemoryProvider` extension method.
This will allow the `SurrealDbClient` to resolve the `mem://` endpoint.

```csharp
var builder = WebApplication.CreateBuilder(args);

var services = builder.Services;
var configuration = builder.Configuration;

// highlight-start
services
  .AddSurreal("Endpoint=mem://")
  .AddInMemoryProvider();
// highlight-end
```

Learn more about [Dependency Injection with SurrealDB in .NET](core/dependency-injection.md) in the SDK documentation.

Once the memory provider is configured, you can use the .NET SDK the same way you would with a remote database.
Please refer to the [.NET client SDK](index.md) documentation to get started with SurrealDB for .NET.

## File providers

The file provider is a more advanced storage engine that can be used to persist data to disk.

  
**RocksDB**

```bash
dotnet add package SurrealDb.Embedded.RocksDb
```

  
**SurrealKV**

```bash
dotnet add package SurrealDb.Embedded.SurrealKv
```

### Consume the provider as is

  
**RocksDB**

The simplest way to use a file-backed database instance of SurrealDB is to create an instance of the `SurrealDbRocksDbClient` class.
Note that the `path` to the storage is mandatory.

```csharp
// highlight-next-line
using var db = new SurrealDbRocksDbClient("data.db");

const string TABLE = "person";

var person = new Person
{
    Title = "Founder & CEO",
    Name = new() { FirstName = "Tobie", LastName = "Morgan Hitchcock" },
    Marketing = true
};
var created = await db.Create(TABLE, person);
Console.WriteLine(ToJsonString(created));
```

  
**SurrealKV**

The simplest way to use a file-backed database instance of SurrealDB is to create an instance of the `SurrealDbKvClient` class.
Note that the `path` to the storage is mandatory.

```csharp
// highlight-next-line
using var db = new SurrealDbKvClient("data.db");

const string TABLE = "person";

var person = new Person
{
    Title = "Founder & CEO",
    Name = new() { FirstName = "Tobie", LastName = "Morgan Hitchcock" },
    Marketing = true
};
var created = await db.Create(TABLE, person);
Console.WriteLine(ToJsonString(created));
```

### Consume the provider via dependency injection

  
**RocksDB**

Following the .NET Dependency Injection pattern, you can register the file provider using the `AddRocksDbProvider` extension method.
This will allow the `SurrealDbClient` to resolve the `rocksdb://` endpoint.

```csharp
var builder = WebApplication.CreateBuilder(args);

var services = builder.Services;
var configuration = builder.Configuration;

// highlight-start
services
  .AddSurreal("Endpoint=rocksdb://data.db")
  .AddRocksDbProvider();
// highlight-end
```

  
**SurrealKV**

Following the .NET Dependency Injection pattern, you can register the file provider using the `AddSurrealKvProvider` extension method.
This will allow the `SurrealDbClient` to resolve the `surrealkv://` endpoint.

```csharp
var builder = WebApplication.CreateBuilder(args);

var services = builder.Services;
var configuration = builder.Configuration;

// highlight-start
services
  .AddSurreal("Endpoint=surrealkv://data.db")
  .AddSurrealKvProvider();
// highlight-end
```

Learn more about [Dependency Injection with SurrealDB in .NET](core/dependency-injection.md) in the SDK documentation.

### Next step

Once the file provider is configured, you can use the .NET SDK the same way you would with a remote database.
Please refer to the [.NET client SDK](index.md) documentation to get started.
