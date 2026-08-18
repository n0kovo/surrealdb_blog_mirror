---
position: 14
title: new
description: The .new() method for the SurrealDB Rust SDK connects to a local or remote database endpoint.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/rust/methods/new.mdx"
---

# `new()`

**3.x**

Connects to a local or remote database endpoint.

```rust title="Method Syntax"
Surreal::new::<T>(address)
```

### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Argument</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">
                `endpoint`
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The database endpoint to connect to.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

#### Basic example

```rust
use surrealdb::engine::remote::ws::Ws;
use surrealdb::Surreal;

#[tokio::main]
async fn main() -> surrealdb::Result<()> {
    let db = Surreal::new::<Ws>("127.0.0.1:8000").await?;
    Ok(())
}
```

#### Configuring the database

The `new()` function takes an argument of [`impl IntoEndpoint`](https://docs.rs/surrealdb/latest/surrealdb/opt/trait.IntoEndpoint.html#foreign-impls), which is implemented not only for strings and string-like structs like [`PathBuf`](https://doc.rust-lang.org/std/path/struct.PathBuf.html) and [`SocketAddr`](https://doc.rust-lang.org/std/net/enum.SocketAddr.html), but also a tuple of one of these types for the address along with a second [`Config`](https://docs.rs/surrealdb/latest/surrealdb/opt/struct.Config.html) struct for the configuration.

```rust title="Example with all capabilities enabled except one function"
use surrealdb::{Error, engine::any::connect, opt::{Config, capabilities::Capabilities}};

#[tokio::main]
async fn main() -> Result<(), Error> {
    let mut capabilities = Capabilities::all();
    capabilities.deny_function("math::abs").unwrap();
    let config = Config::default()
        .capabilities(capabilities);
    let db = connect(("mem://", config)).await?;

    db.use_ns("main").use_db("main").await?;

    // Result: "Function 'math::abs' is not allowed to be executed"
    println!("{:?}", db.query("math::abs(-10)").await?);

    Ok(())
}
```

##### Config options

`Config` is a builder with methods that can be chained. `Config::new()` and `Config::default()` are equivalent starting points.

<table>
    <thead>
        <tr>
            <th scope="col">Method</th>
            <th scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Method">`.user(root)`</td>
            <td scope="row" data-label="Description">Sets the root user the local engines start with. Takes an `opt::auth::Root`.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.capabilities(caps)`</td>
            <td scope="row" data-label="Description">Sets which functions, network targets, scripting and live queries are permitted. See <a href="/docs/learn/security/authorization/capabilities">Capabilities</a>.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.query_timeout(duration)`</td>
            <td scope="row" data-label="Description">Maximum time a single query may run for.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.transaction_timeout(duration)`</td>
            <td scope="row" data-label="Description">Maximum time a transaction may stay open for.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.ast_payload()`</td>
            <td scope="row" data-label="Description">Sends queries as a parsed AST rather than as text. `.set_ast_payload(bool)` sets the same option from a variable.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.websocket(config)`</td>
            <td scope="row" data-label="Description">Sets the WebSocket buffer sizes. Returns a `Result`, as the maximum write buffer must be larger than the write buffer.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.rustls(config)`, `.native_tls(config)`</td>
            <td scope="row" data-label="Description">Configures TLS. Each requires the matching feature flag. Neither is covered by the SDK's stability guarantee, as the underlying crate is not yet stable.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.temporary_directory(path)`</td>
            <td scope="row" data-label="Description">Where the local engines spill temporary data. Requires a storage backend feature flag.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.changefeed_gc_interval(duration)`</td>
            <td scope="row" data-label="Description">How often expired change feed entries are collected.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Method">`.node_membership_refresh_interval(duration)`, `.node_membership_check_interval(duration)`, `.node_membership_cleanup_interval(duration)`</td>
            <td scope="row" data-label="Description">Intervals for the node maintenance tasks the local engines run. A zero duration is treated as unset.</td>
        </tr>
    </tbody>
</table>

An example of the `Config` builder used to set a number of attributes in a single chain:

```rust
use std::time::Duration;

use surrealdb::engine::any::connect;
use surrealdb::opt::Config;
use surrealdb::opt::auth::Root;
use surrealdb::opt::capabilities::Capabilities;

#[tokio::main]
async fn main() -> surrealdb::Result<()> {
    let config = Config::new()
        .user(Root {
            username: "root".to_string(),
            password: "secret".to_string(),
        })
        .query_timeout(Duration::from_secs(5))
        .transaction_timeout(Duration::from_secs(10))
        .capabilities(
            Capabilities::all()
                .with_function_denied("http::*")
                .unwrap(),
        );

    let db = connect(("mem://", config)).await?;
    db.signin(Root {
        username: "root".to_string(),
        password: "secret".to_string(),
    })
    .await?;
    db.use_ns("main").use_db("main").await?;

    println!("{:?}", db.query("RETURN http::get('https://example.com')").await?);
    Ok(())
}
```

The denied function shows up as an error on the statement rather than on the call as a whole:

```
Err(Error { code: -32602, message: "Function 'http::get' is not allowed to be executed", details: NotAllowed(Some(Function { name: "http::get" })), cause: None })
```

Note that the `Capabilities` methods that take a function or network target parse their argument, so they return a `Result`. The pairs come in two shapes: `allow_function` / `deny_function` take `&mut self`, while `with_function_allowed` / `with_function_denied` consume and return the value, which is what makes them chainable.

#### Using a backend with versioning

To make a new connection that includes SurrealKV versioning, add the "kv-surrealkv" feature flag to the `surrealdb` dependency in `Cargo.toml`, add the path to the folder containing the database inside `new()`, and call the `.versioned()` method. Versioning is also available with the memory backend.

```rust
use surrealdb::{Surreal, engine::local::{Mem, SurrealKv}};

#[tokio::main]
async fn main() -> surrealdb::Result<()> {
    // SurrealKV with versioning
    let db = Surreal::new::<SurrealKv>("path/to/database-folder")
        .versioned()
        .await?;

    // In-memory DB with versioning
    let mem_db = Surreal::new::<Mem>(())
        .versioned()
        .await?;
    Ok(())
}
```

### See also

* [.new() method on Docs.rs](https://docs.rs/surrealdb/latest/surrealdb/struct.Surreal.html#method.new)

**2.x**

Connects to a local or remote database endpoint.

```rust title="Method Syntax"
Surreal::new::<T>(address)
```

### Arguments
<table>
    <thead>
        <tr>
            <th colspan="2" scope="col">Argument</th>
            <th colspan="2" scope="col">Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td colspan="2" scope="row" data-label="Argument">
                `endpoint`
            </td>
            <td colspan="2" scope="row" data-label="Description">
                The database endpoint to connect to.
            </td>
        </tr>
    </tbody>
</table>

### Example usage

#### Basic example

```rust
use surrealdb::engine::remote::ws::Ws;
use surrealdb::Surreal;

#[tokio::main]
async fn main() -> surrealdb::Result<()> {
    let db = Surreal::new::<Ws>("127.0.0.1:8000").await?;
    Ok(())
}
```

#### Configuring the database

The `new()` function takes an argument of [`impl IntoEndpoint`](https://docs.rs/surrealdb/latest/surrealdb/opt/trait.IntoEndpoint.html#foreign-impls), which is implemented not only for strings and string-like structs like [`PathBuf`](https://doc.rust-lang.org/std/path/struct.PathBuf.html) and [`SocketAddr`](https://doc.rust-lang.org/std/net/enum.SocketAddr.html), but also a tuple of one of these types for the address along with a second [`Config`](https://docs.rs/surrealdb/latest/surrealdb/opt/struct.Config.html) struct for the configuration.

```rust title="Example with all capabilities enabled except one function"
#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = Config::default()
        .capabilities(Capabilities::all().with_deny_function("math::abs")?);
    let db = connect(("mem://", config)).await?;

    db.use_ns("ns").use_db("db").await?;

    // Result: Err(Db(FunctionNotAllowed("math::abs")))
    println!("{:?}", db.query("math::abs(-10)").await?);
    println!("{:?}", db.run::<i32>("math::abs").args(-10).await);

    Ok(())
}
```

#### Using SurrealKV with versioning

To make a new connection that includes SurrealKV versioning, add the `kv-surrealkv` feature flag to the `surrealdb` dependency in `Cargo.toml`, add the path to the folder containing the database inside `new()`, and call the `.versioned()` method.

```rust
use surrealdb::engine::local::SurrealKv;
use surrealdb::Surreal;

#[tokio::main]
async fn main() -> surrealdb::Result<()> {
    let db = Surreal::new::<SurrealKv>("path/to/database-folder").versioned().await?;
    Ok(())
}
```

### See also

* [.new() method on Docs.rs](https://docs.rs/surrealdb/latest/surrealdb/struct.Surreal.html#method.new)
