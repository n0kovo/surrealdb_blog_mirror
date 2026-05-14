---
title: "Two new ways to keep an eye on your SurrealDB database"
slug: "two-new-ways-to-keep-an-eye-on-your-surrealdb-database"
date: "2025-07-22T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "3 min read"
summary: "Logging output to file and seeing the current tasks on a console are two new ways to gain greater insight into what your database is doing."
source: "https://surrealdb.com/blog/two-new-ways-to-keep-an-eye-on-your-surrealdb-database"
cover: "../../assets/fe90ca2801019b8c.jpg"
---

# Two new ways to keep an eye on your SurrealDB database

![Two new ways to keep an eye on your SurrealDB database](../../assets/fe90ca2801019b8c.jpg)

Two PRs were merged into SurrealDB last month with very little fanfare that vastly improve on the observability of your SurrealDB instance. This post is a short and sweet one that gives them some well-deserved fanfare by seeing what they are all about!

The first new feature is one that lets you save your logging output in a place and format of your choosing.

## Saving logging output as a file

[This PR](https://github.com/surrealdb/surrealdb/pull/6048) merged last month is available as of version 3.0.0-alpha.7 and all newer 2.x versions. It adds a few environment variables that allow you to choose to save logging output to a file as opposed to just the terminal. It comes with quite a few environment variables that allow customisation.

Two to get started with are `SURREAL_LOG_FILE_ENABLED` to enable logging to file in the first place, and `SURREAL_LOG_FILE_FORMAT` if you want to save the files as JSON. There is also a `SURREAL_LOG_FORMAT` for the same if you want to see JSON in the terminal output.

The following command will start the database with logging sent to a file in JSON format:

```syntax
SURREAL_LOG_FILE_ENABLED=true SURREAL_LOG_FILE_FORMAT=json surreal start --unauthenticated --log debug
```

As soon as the database is started you will see a file show up with a format that will match today's date, such as `surrealdb.log.2025-07-22`. This can be customised with environment variables too: `SURREAL_LOG_FILE_ROTATION` which lets you change the default `daily` rotation to `hourly` or `never` or `SURREAL_LOG_FILE_NAME` to choose a name that differs from the default `surrealdb.log`.

The file will look something like this for a database that is started and quickly shut down.

```syntax
{"timestamp":"2025-07-22T03:18:59.349350Z","level":"INFO","fields":{"message":"Running 3.0.0+20250721.eaff383ce for macos on aarch64"},"target":"surreal::env"}
{"timestamp":"2025-07-22T03:18:59.349604Z","level":"DEBUG","fields":{"message":"Database strict mode is false"},"target":"surreal::dbs"}
{"timestamp":"2025-07-22T03:18:59.349647Z","level":"WARN","fields":{"message":"❌🔒 IMPORTANT: Authentication is disabled. This is not recommended for production use. 🔒❌"},"target":"surreal::dbs"}
{"timestamp":"2025-07-22T03:18:59.349787Z","level":"DEBUG","fields":{"message":"Server capabilities: scripting=false, guest_access=false, live_query_notifications=true, allow_funcs=all, deny_funcs=none, allow_net=none, deny_net=none, allow_rpc=all, deny_rpc=none, allow_http=all, deny_http=none, allow_experimental=none, deny_experimental=none, allow_arbitrary_query=all, deny_arbitrary_query=none"},"target":"surreal::dbs"}
{"timestamp":"2025-07-22T03:18:59.349946Z","level":"INFO","fields":{"message":"Starting kvs store in memory"},"target":"surrealdb::core::kvs::ds"}
{"timestamp":"2025-07-22T03:18:59.350261Z","level":"INFO","fields":{"message":"Started kvs store in memory"},"target":"surrealdb::core::kvs::ds"}
{"timestamp":"2025-07-22T03:18:59.366682Z","level":"INFO","fields":{"message":"Listening for a system shutdown signal."},"target":"surrealdb::net"}
{"timestamp":"2025-07-22T03:18:59.367084Z","level":"INFO","fields":{"message":"Started web server on 127.0.0.1:8000"},"target":"surrealdb::net"}
{"timestamp":"2025-07-22T03:18:59.416461Z","level":"DEBUG","fields":{"message":"Started processing request"},"target":"surreal::net::tracer","span":{"client.address":"127.0.0.1","http.request.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","http.request.method":"GET","http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","name":"request"},"spans":[{"client.address":"127.0.0.1","http.request.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","http.request.method":"GET","http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","name":"request"}]}
{"timestamp":"2025-07-22T03:18:59.417239Z","level":"DEBUG","fields":{"message":"Finished processing request"},"target":"surreal::net::tracer","span":{"client.address":"127.0.0.1","http.latency.ms":"0","http.request.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","http.request.method":"GET","http.response.status_code":101,"http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","name":"request"},"spans":[{"client.address":"127.0.0.1","http.latency.ms":"0","http.request.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","http.request.method":"GET","http.response.status_code":101,"http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","name":"request"}]}
{"timestamp":"2025-07-22T03:18:59.418561Z","level":"DEBUG","fields":{"message":"Process RPC request"},"target":"surreal::rpc::websocket","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/use","rpc.method":"use","rpc.request_id":"","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/use","rpc.method":"use","rpc.request_id":"","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:18:59.418823Z","level":"DEBUG","fields":{"message":"Process RPC response"},"target":"surreal::rpc::response","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/use","rpc.method":"use","rpc.request_id":"","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/use","rpc.method":"use","rpc.request_id":"","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:18:59.419157Z","level":"DEBUG","fields":{"message":"Process RPC request"},"target":"surreal::rpc::websocket","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/kill","rpc.method":"kill","rpc.request_id":"17","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/kill","rpc.method":"kill","rpc.request_id":"17","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:18:59.420673Z","level":"DEBUG","fields":{"message":"Process RPC response"},"target":"surreal::rpc::response","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/kill","rpc.method":"kill","rpc.request_id":"17","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/kill","rpc.method":"kill","rpc.request_id":"17","rpc.service":"surrealdb","ws.id":"a07b1568-b675-4a2a-8a96-67f19f849a16","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.500111Z","level":"DEBUG","fields":{"message":"Started processing request"},"target":"surreal::net::tracer","span":{"client.address":"127.0.0.1","http.request.id":"12856969-0db2-4d13-afb5-424e50a76f99","http.request.method":"GET","http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","user_agent.original":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)","name":"request"},"spans":[{"client.address":"127.0.0.1","http.request.id":"12856969-0db2-4d13-afb5-424e50a76f99","http.request.method":"GET","http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","user_agent.original":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)","name":"request"}]}
{"timestamp":"2025-07-22T03:19:00.501949Z","level":"DEBUG","fields":{"message":"Finished processing request"},"target":"surreal::net::tracer","span":{"client.address":"127.0.0.1","http.latency.ms":"1","http.request.id":"12856969-0db2-4d13-afb5-424e50a76f99","http.request.method":"GET","http.response.status_code":101,"http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","user_agent.original":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)","name":"request"},"spans":[{"client.address":"127.0.0.1","http.latency.ms":"1","http.request.id":"12856969-0db2-4d13-afb5-424e50a76f99","http.request.method":"GET","http.response.status_code":101,"http.route":"/rpc","network.protocol.name":"http","network.protocol.version":"1.1","otel.kind":"server","otel.name":"GET /rpc","url.path":"/rpc","user_agent.original":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)","name":"request"}]}
{"timestamp":"2025-07-22T03:19:00.505180Z","level":"DEBUG","fields":{"message":"Process RPC request"},"target":"surreal::rpc::websocket","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/invalidate","rpc.method":"invalidate","rpc.request_id":"12364","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/invalidate","rpc.method":"invalidate","rpc.request_id":"12364","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.505664Z","level":"DEBUG","fields":{"message":"Process RPC response"},"target":"surreal::rpc::response","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/invalidate","rpc.method":"invalidate","rpc.request_id":"12364","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/invalidate","rpc.method":"invalidate","rpc.request_id":"12364","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.540473Z","level":"DEBUG","fields":{"message":"Process RPC request"},"target":"surreal::rpc::websocket","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/version","rpc.method":"version","rpc.request_id":"12365","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/version","rpc.method":"version","rpc.request_id":"12365","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.540803Z","level":"DEBUG","fields":{"message":"Process RPC response"},"target":"surreal::rpc::response","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/version","rpc.method":"version","rpc.request_id":"12365","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/version","rpc.method":"version","rpc.request_id":"12365","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.543316Z","level":"DEBUG","fields":{"message":"Process RPC request"},"target":"surreal::rpc::websocket","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12366","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12366","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.547539Z","level":"DEBUG","fields":{"message":"Process RPC response"},"target":"surreal::rpc::response","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12366","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12366","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.548843Z","level":"DEBUG","fields":{"message":"Process RPC request"},"target":"surreal::rpc::websocket","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12367","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12367","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.549222Z","level":"DEBUG","fields":{"message":"Process RPC response"},"target":"surreal::rpc::response","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12367","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12367","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.549468Z","level":"DEBUG","fields":{"message":"Process RPC request"},"target":"surreal::rpc::websocket","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12368","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12368","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:00.549716Z","level":"DEBUG","fields":{"message":"Process RPC response"},"target":"surreal::rpc::response","span":{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12368","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"},"spans":[{"otel.kind":"server","otel.name":"surrealdb.rpc/query","rpc.method":"query","rpc.request_id":"12368","rpc.service":"surrealdb","ws.id":"12856969-0db2-4d13-afb5-424e50a76f99","name":"rpc/call"}]}
{"timestamp":"2025-07-22T03:19:01.346244Z","level":"WARN","fields":{"message":"SIGINT received. Waiting for a graceful shutdown. A second signal will force an immediate shutdown."},"target":"surrealdb::net"}
{"timestamp":"2025-07-22T03:19:01.346456Z","level":"INFO","fields":{"message":"Listening for a system shutdown signal."},"target":"surrealdb::net"}
{"timestamp":"2025-07-22T03:19:01.601797Z","level":"INFO","fields":{"message":"Web server stopped. Bye!"},"target":"surrealdb::net"}
```

</br>

## Tokio console

The next new observability feature is interoperability with a platform known as [`tokio console`](https://github.com/tokio-rs/console). The tokio project includes a console that allows you to visually follow which async tasks are currently running and where most of the work is happening. And since SurrealDB is an async database built with Rust on the tokio async runtime, adding interoperability with tokio console made good sense.

This feature is currently only available in nightly, but you will soon see it also show up in the next alpha version.

You need to have Rust installed to use the console, but you don't need to know Rust itself. The following two commands will install Rust and the `cargo` package manager using `curl`, and then use Cargo to install tokio console.

```cli
curl https://sh.rustup.rs -sSf | sh
cargo install --locked tokio-console
```

You can then test it out by typing `tokio-console`, which should show a completely blank screen because nothing is being sent to it yet.

Now use ctrl-C to leave the console, open up a new window and start SurrealDB with the console enabled via an environment variable called `SURREAL_TOKIO_CONSOLE_ENABLED`.

```cli
SURREAL_TOKIO_CONSOLE_ENABLED=true surreal start --unauthenticated
```

If you type `tokio-console` in the other window again, this time you should see a field that looks like this. The database is sitting idle, but has already sent some information to the console.

A busy database will look like this:

During or after which you can use the down arrows to move to a certain task and hit enter to see further details such as average elapsed time.

For more on the layout and the commands you can use via the `tokio-console` CLI, see [this page](https://github.com/tokio-rs/console/tree/main/tokio-console).
