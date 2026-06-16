---
position: 3
title: Environment variables
description: A list of the available environment variables used when running SurrealDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/cli/surrealdb-cli/environment-variables.mdx"
---

# Environment variables

Environment variables can be used to tailor the behaviour of a running SurrealDB instance.

Environment variables are divided into four types: 

* **SurrealDB environment variables**: environment variables that pertain to the overall running of a SurrealDB server. Example: `SURREAL_DEFAULT_DATABASE`.
* **Command environment variables**: environment variables that can be used in lieu of a command flag. Example: `SURREAL_CAPS_ALLOW_ALL=true surreal start`, equivalent to `surreal start --allow-all`.
* **Storage backend environment variables**: environment variables that pertain to a certain storage backend. Example: `SURREAL_SURREALKV_MAX_SEGMENT_SIZE`.
* **SurrealDB Cloud environment variables**: environment variables that are set via the [Configure instance](../../../build/deployment/surrealdb-cloud/getting-started/create-an-instance.md#configure-an-instance) sidebar for a SurrealDB Cloud instance.

Many environment variables have a maximum value equivalent to the greatest possible `usize`, which is an unsigned integer with a number of bytes depending on the target that the database runs on. For most systems this will be 64 bits, leading to a maximum size of 18_446_744_073_709_551_615 (2<sup>64</sup>), while for 32 bits the maximum will be 4_294_967_296 (2<sup>32</sup>).

## SurrealDB environment variables

These environment variables can be used to configure a SurrealDB server to configure areas such as the HTTP server and client, limits, telemetry, and so on.

### Batch config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_NORMAL_FETCH_SIZE`</td>
      <td scope="row" data-label="Default">500</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of keys that should be scanned at once in general queries.</td>
    </tr>
        <tr>
      <td scope="row" data-label="Env var">`SURREAL_EXPORT_BATCH_SIZE`</td>
      <td scope="row" data-label="Default">1000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of keys that should be scanned at once for export queries.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_COUNT_BATCH_SIZE`*Since v2.2.0*</td>
      <td scope="row" data-label="Default">10,000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of keys that should be scanned at once for count queries.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_INDEXING_BATCH_SIZE`</td>
      <td scope="row" data-label="Default">250</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of keys to scan at once per concurrent indexing batch.</td>
    </tr>
  </tbody>
</table>

### Cache config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_TRANSACTION_CACHE_SIZE`</td>
      <td scope="row" data-label="Default">10,000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Specifies the number of items which can be cached within a single transaction.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_DATASTORE_CACHE_SIZE`*Since v2.1.0*</td>
      <td scope="row" data-label="Default">1,000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of definitions which can be cached across transactions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HNSW_CACHE_SIZE`</td>
      <td scope="row" data-label="Default">268,435,456 (256 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum size of the HNSW vector cache.</td>
    </tr>
  </tbody>
</table>

### File config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td scope="row" data-label="Env var">`SURREAL_BUCKET_FOLDER_ALLOWLIST`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">Comma-separated paths</td>
      <td scope="row" data-label="Notes">Specifies a list of paths in which files can be accessed.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_GLOBAL_BUCKET`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">Specifies the name of a global bucket for file data.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_GLOBAL_BUCKET_ENFORCED`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to enforce a global bucket for file data.</td>
    </tr>
  </tbody>
</table>

### HTTP client config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>

  <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_HTTP_REDIRECTS`*Since v2.0.5*</td>
      <td scope="row" data-label="Default">10</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of HTTP redirects allowed within http functions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_HTTP_IDLE_CONNECTIONS_PER_HOST`</td>
      <td scope="row" data-label="Default">128</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of idle HTTP connections to maintain per host.</td>
    </tr>
        <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_HTTP_IDLE_CONNECTIONS`</td>
      <td scope="row" data-label="Default">1000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of idle HTTP connections to maintain.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_IDLE_TIMEOUT_SECS`</td>
      <td scope="row" data-label="Default">90</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The timeout for idle HTTP connections before closing.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_CONNECT_TIMEOUT_SECS`</td>
      <td scope="row" data-label="Default">30</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The timeout for connecting to HTTP endpoints.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_USER_AGENT`</td>
      <td scope="row" data-label="Default">SurrealDB</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The USER-AGENT string used by HTTP requests.</td>
    </tr>
  </tbody>
</table>

### HTTP server config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>

<tr>
      <td scope="row" data-label="Env var">`SURREAL_NET_MAX_CONCURRENT_REQUESTS`</td>
      <td scope="row" data-label="Default">1,048,576</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">How many concurrent network requests can be handled at once</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_ML_BODY_SIZE`</td>
      <td scope="row" data-label="Default">4,398,046,511,104 (4 GiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum HTTP body size of the HTTP /ml endpoints</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_MCP_BODY_SIZE`*Since v3.1.0*</td>
      <td scope="row" data-label="Default">4,194,304 (4 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum HTTP body size of the HTTP `/mcp` endpoint. See [MCP](../../../build/ai-agents/mcp.md).</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_SQL_BODY_SIZE`</td>
      <td scope="row" data-label="Default">1,048,576 (1 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum HTTP body size of the HTTP /sql endpoint</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_API_BODY_SIZE`</td>
      <td scope="row" data-label="Default">4,194,304 (4 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum HTTP body size of the HTTP /api endpoint.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_RPC_BODY_SIZE`</td>
      <td scope="row" data-label="Default">4,194,304 (4 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum HTTP body size of the HTTP /rpc endpoint.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_KEY_BODY_SIZE`</td>
      <td scope="row" data-label="Default">16,384 (16 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum HTTP body size of the HTTP /key endpoints</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_SIGNUP_BODY_SIZE`</td>
      <td scope="row" data-label="Default">1024 (1 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum HTTP body size of the HTTP /signup endpoint.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_IMPORT_BODY_SIZE`</td>
      <td scope="row" data-label="Default">4,398,046,511,104 (4 GiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum HTTP body size of the HTTP /import endpoints</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HTTP_MAX_SIGNIN_BODY_SIZE`</td>
      <td scope="row" data-label="Default">1024 (1 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum HTTP body size of the HTTP /signin endpoints</td>
    </tr>
  </tbody>
</table>

### MCP config *Since v3.1.0*

Used by the built-in [Model Context Protocol](../../../build/ai-agents/mcp.md) server (`/mcp` on `surreal start`, `surreal mcp` on stdio). Stdio namespace/database selection uses `SURREAL_MCP_NS` and `SURREAL_MCP_DB` on the [`mcp`](commands/mcp.md) subcommand.

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MCP_QUERY_TIMEOUT_SECS`</td>
      <td scope="row" data-label="Default">60</td>
      <td scope="row" data-label="Allowed values">Seconds (integer); `0` disables</td>
      <td scope="row" data-label="Notes">Outer timeout on each MCP tool execution.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MCP_MAX_RESULT_BYTES`</td>
      <td scope="row" data-label="Default">262,144 (256 KiB)</td>
      <td scope="row" data-label="Allowed values">Bytes (integer); `0` disables</td>
      <td scope="row" data-label="Notes">Maximum serialised tool / resource response size; larger results are truncated with a marker.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MCP_RUN_MAX_ARGS`</td>
      <td scope="row" data-label="Default">64</td>
      <td scope="row" data-label="Allowed values">A positive integer</td>
      <td scope="row" data-label="Notes">Maximum arguments for a single `run` tool call.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MCP_PARAMS_MAX_KEYS`</td>
      <td scope="row" data-label="Default">256</td>
      <td scope="row" data-label="Allowed values">A positive integer</td>
      <td scope="row" data-label="Notes">Maximum top-level keys in MCP parameter / data objects.</td>
    </tr>
  </tbody>
</table>

### Limits config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>

    <tr>
      <td scope="row" data-label="Env var">`SURREAL_EXTERNAL_SORTING_BUFFER_LIMIT`</td>
      <td scope="row" data-label="Default">50000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of result records which will trigger on-disk sorting.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_STRING_SIMILARITY_LIMIT`</td>
      <td scope="row" data-label="Default">16384</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum input string length for similarity/distance functions</td>
    </tr>
     <tr>
      <td scope="row" data-label="Env var">`SURREAL_GENERATION_ALLOCATION_LIMIT`</td>
      <td scope="row" data-label="Default">1,048,576</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Limits memory allocation for certain built-in functions (e.g., string::replace) to avoid uncontrolled memory usage. Default is 1,048,576 bytes (computed as 2<sup>20</sup>).</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_IDIOM_RECURSION_LIMIT`</td>
      <td scope="row" data-label="Default">256</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum recursive idiom path depth allowed.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_COMPUTATION_DEPTH`</td>
      <td scope="row" data-label="Default">120</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Specifies how deep recursive computation will go before erroring.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_CONCURRENT_TASKS`</td>
      <td scope="row" data-label="Default">64</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Specifies how many concurrent jobs can be buffered in the worker channel.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_OBJECT_PARSING_DEPTH`</td>
      <td scope="row" data-label="Default">100</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Specifies how deep the parser will parse nested objects and arrays in a query.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_ORDER_LIMIT_PRIORITY_QUEUE_SIZE`*Since v2.2.0*</td>
      <td scope="row" data-label="Default">1000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum size of the priority queue triggering usage of the priority queue for the result collector.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MAX_QUERY_PARSING_DEPTH`</td>
      <td scope="row" data-label="Default">20</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Specifies how deep the parser will parse recursive queries (queries within queries).</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_OPERATOR_BUFFER_SIZE`*Since v2.1.5*</td>
      <td scope="row" data-label="Default">2</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of batches each operator buffers ahead of downstream demand. Set to 0 to disable operator-level pipeline buffering.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_REGEX_SIZE_LIMIT`*Since v2.1.5*</td>
      <td scope="row" data-label="Default">10,485,760 (10 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Limits the maximum allowed size (in bytes) for regular expressions. This prevents excessive memory consumption when building complex or very large regex patterns.</td>
    </tr>
  </tbody>
</table>

### Runtime config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_RUNTIME_MAX_BLOCKING_THREADS`</td>
      <td scope="row" data-label="Default">512</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Number of threads which can be started for blocking operations.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_RUNTIME_STACK_SIZE`</td>
      <td scope="row" data-label="Default">10,485,760 (10 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Runtime thread memory stack size. Default stack size is doubled if compiled from source in Debug mode.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_RUNTIME_WORKER_THREADS`</td>
      <td scope="row" data-label="Default">Number of CPU cores (minimum 4)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Number of runtime worker threads used to start.</td>
    </tr>
  </tbody>
</table>

### Scripting config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SCRIPTING_MAX_STACK_SIZE`</td>
      <td scope="row" data-label="Default">262_144 (256 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum stack size of the JavaScript function runtime.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SCRIPTING_MAX_MEMORY_LIMIT`</td>
      <td scope="row" data-label="Default">2,097,152 (2 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum memory limit of the JavaScript function runtime.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SCRIPTING_MAX_TIME_LIMIT`*Since v2.0.5*</td>
      <td scope="row" data-label="Default">5000 (5000 milliseconds or 5 seconds)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Maximum allowed time in milliseconds that a JavaScript function is allowed to run for.</td>
    </tr>
  </tbody>
</table>

### Security config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_INSECURE_FORWARD_ACCESS_ERRORS`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Forward all signup/signin/authenticate query errors to a client performing authentication. Do not use in production.</td>
    </tr>
  </tbody>
</table>

### Surrealism config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LAZY_SURREALISM`*Since v3.1.0*</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to lazy-load Surrealism modules instead of eagerly compiling them at server startup.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALISM_CACHE_SIZE`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">100</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of surrealism modules which can be cached across transactions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALISM_MAX_POOL_SIZE`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">8</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Per-module controller pool size ceiling for Surrealism WASM modules.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALISM_MAX_MEMORY`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">None (unlimited)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Per-module WASM linear memory ceiling in bytes.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALISM_MAX_EXECUTION_TIME`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">None (unlimited)</td>
      <td scope="row" data-label="Allowed values">A u64 (milliseconds)</td>
      <td scope="row" data-label="Notes">Per-invocation execution time ceiling for Surrealism WASM modules.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALISM_MAX_KV_ENTRIES`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">None (unlimited)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Per-module KV store entry count ceiling.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALISM_MAX_KV_VALUE_BYTES`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">None (unlimited)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Per-module KV store maximum value size in bytes.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALISM_LOG_LEVEL`*Since v3.1.0*</td>
      <td scope="row" data-label="Default">debug</td>
      <td scope="row" data-label="Allowed values">none, full, error, warn, info, debug, trace</td>
      <td scope="row" data-label="Notes">Controls the tracing level at which Surrealism module stdout is emitted.</td>
    </tr>
  </tbody>
</table>

### Telemetry config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TELEMETRY_DISABLE_METRICS`*Since v2.1.3*</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to disable sending metrics to the GRPC OTEL collector.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TELEMETRY_DISABLE_TRACING`*Since v2.1.3*</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to disable sending traces to the GRPC OTEL collector.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TELEMETRY_NAMESPACE`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">If set then use this as value for the namespace label when sending telemetry</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TELEMETRY_PROVIDER`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">otlp</td>
      <td scope="row" data-label="Notes">If set to "otlp" then telemetry is sent to the GRPC OTEL collector.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TOKIO_CONSOLE_ENABLED`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to enable [tokio console](https://github.com/tokio-rs/console).</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TOKIO_CONSOLE_RETENTION`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">60</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">How long, in seconds, to retain data for completed events.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TOKIO_CONSOLE_SOCKET_ADDR`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a socket address</td>
      <td scope="row" data-label="Notes">The socket address that Tokio Console will bind to.</td>
    </tr>
  </tbody>
</table>

### WebSocket config

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEBSOCKET_MAX_MESSAGE_SIZE`</td>
      <td scope="row" data-label="Default">134,217,728 (128 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum WebSocket message size.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEBSOCKET_MAX_WRITE_BUFFER_SIZE`</td>
      <td scope="row" data-label="Default">Greatest possible usize value</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum write buffer size before backpressure is applied.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEBSOCKET_READ_BUFFER_SIZE`</td>
      <td scope="row" data-label="Default">131,072 (128 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The size of the read buffer for WebSocket connections. This controls how much data can be buffered when reading from WebSocket connections. Larger values can improve performance for high-throughput connections but consume more memory per connection.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEBSOCKET_WRITE_BUFFER_SIZE`</td>
      <td scope="row" data-label="Default">131,072 (128 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The size of the write buffer for WebSocket connections. This controls how much data can be buffered when writing to WebSocket connections. Larger values can improve performance for high-throughput connections but consume more memory per connection.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEBSOCKET_RESPONSE_BUFFER_SIZE`</td>
      <td scope="row" data-label="Default">0</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">How many responses can be buffered when delivering to the client.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEBSOCKET_RESPONSE_CHANNEL_SIZE`</td>
      <td scope="row" data-label="Default">100</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Number of messages that can be queued for sending via WebSocket.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEBSOCKET_RESPONSE_FLUSH_PERIOD`</td>
      <td scope="row" data-label="Default">3</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">How often (in milliseconds) any buffered responses are flushed to the WebSocket client.</td>
    </tr>
  </tbody>
</table>

### Other environment variables

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '40%'}}>Environment variable</th>
      <th scope="col" style={{width: '20%'}}>Default</th>
      <th scope="col" style={{width: '20%'}}>Allowed values</th>
      <th scope="col" style={{width: '20%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_BUILD_METADATA`</td>
      <td scope="row" data-label="Default">Automatically populated</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The version identifier of this build. Defaults to the CARGO_PKG_VERSION environment variable if not specified.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DATASTORE_AOL`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">never</td>
      <td scope="row" data-label="Allowed values">never|sync|async</td>
      <td scope="row" data-label="Notes">Append-only log mode. Only used by the memory engine.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DATASTORE_PERSIST`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a file path</td>
      <td scope="row" data-label="Notes">Filesystem path for persistence. Only used by the memory engine.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DATASTORE_RETENTION`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">0 (unlimited)</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">Version retention period as a duration string. Used by memory and surrealkv engines.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DATASTORE_SNAPSHOT`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">never</td>
      <td scope="row" data-label="Allowed values">never|duration</td>
      <td scope="row" data-label="Notes">Snapshot interval. Only used by the memory engine.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DATASTORE_SYNC_DATA`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">every</td>
      <td scope="row" data-label="Allowed values">never|every|duration</td>
      <td scope="row" data-label="Notes">The sync mode for the database. Used by memory, rocksdb, and surrealkv engines.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DATASTORE_VERSIONED`*Since v3.0.0*</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true|false|0|1</td>
      <td scope="row" data-label="Notes">Whether MVCC versioning is enabled. Used by memory and surrealkv engines.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_MEMORY_THRESHOLD`*Since v2.1.5*</td>
      <td scope="row" data-label="Default">0</td>
      <td scope="row" data-label="Allowed values">A usize or suffixed integer</td>
      <td scope="row" data-label="Notes">Configuring the memory threshold which can be used across the programme to check if the amount of memory available to the programme is lower than required. The value can be specified as bytes (b, or without any suffix), kibibytes (k, kb, or kib), mebibytes (m, mb, or mib), or gibibytes (g, gb, or gib). If the environment variable is not specified, then the threshold is not used, and no memory limit is enabled.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_REGEX_CACHE_SIZE`</td>
      <td scope="row" data-label="Default">1000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of computed regexes which can be cached in the engine.</td>
    </tr>
  </tbody>
</table>

## Command environment variables

Many of the arguments passed into [the CLI](commands/start.md) can be set using the above environment variables instead.

As each of these environment variables correspond to a flag or a required argument passed into a command, it is good practice to put together a command that matches the environment variables you wish to set. Once the database server conforms to your expected behaviour, you can then pull out the values passed into each flag for your environment variables.

For example, take the following command to start the database.

```bash
surreal start --user root --pass secret --allow-net --deny-funcs "crypto::md5, http::post, http::delete"
```

If we now wanted to use environment variables instead of the `--allow-net` and `--deny-funcs` flags, we would use the `SURREAL_CAPS_ALLOW_NET` and `SURREAL_CAPS_DENY_FUNC` environment variables.

As the `--allow-net` flag was passed in without a following value, the same will be the case with the `SURREAL_CAPS_ALLOW_NET` environment variable, becoming `SURREAL_CAPS_ALLOW_NET=`. The `--deny-funcs` flag can also be used on its own to deny execution of all functions, but in this case is followed by a string to indicate which exact functions are not allowed to be executed. As such, the `SURREAL_CAPS_DENY_FUNC` environment variable must also be followed by a string, becoming `SURREAL_CAPS_DENY_FUNC="crypto::md5, http::post, http::delete"`.

The command would then look like the following:

**Bash**

```bash
SURREAL_CAPS_ALLOW_NET
SURREAL_CAPS_DENY_FUNC="crypto::md5, http::post, http::delete"
surreal start --user root --pass secret
```

**PowerShell**

```powershell
$env:SURREAL_CAPS_ALLOW_NET
$env:SURREAL_CAPS_DENY_FUNC="crypto::md5, http::post, http::delete"
surreal start --user root --pass secret
```

A command environment variable that takes a boolean will be set to true if the flag is present, and following it with `true` will cause an error.

For example, the `SURREAL_CAPS_ALLOW_ALL` environment variable is used to set whether to allow all capabilities such as scripting and allowing network access. The flag `--allow-all` is all that is needed to set to `true`. But as an environment variable, the value `true` must be included to override its default `false` value.

```bash title="SURREAL_CAPS_ALLOW_ALL example"
# set to default false
surreal start

# Same, but implicitly shown
SURREAL_CAPS_ALLOW_ALL=false surreal start

# Set to true
SURREAL_CAPS_ALLOW_ALL=true surreal start

# Set to true
surreal start --allow-all

# Error: only --allow-all needed to set to true
surreal start --allow-all true
```

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '25%'}}>Environment variable</th>
      <th scope="col" style={{width: '15%'}}>Command arg</th>
      <th scope="col" style={{width: '12%'}}>For command(s)</th>
      <th scope="col" style={{width: '12%'}}>Default</th>
      <th scope="col" style={{width: '18%'}}>Allowed values</th>
      <th scope="col" style={{width: '18%'}}>Details</th>
    </tr>
  </thead>
  <tbody>
  <tr>
      <td scope="row" data-label="Env var">`SURREAL_ASYNC_EVENT_PROCESSING_INTERVAL`*Since v3.0.0* </td>
      <td scope="row" data-label="Command arg">`async-event-processing-interval`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">5s</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The interval at which to process async events.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_AUTH_LEVEL`</td>
      <td scope="row" data-label="Command arg">`auth-level`</td>
      <td scope="row" data-label="Command">`export`, `import`, `sql`</td>
      <td scope="row" data-label="Default">root</td>
      <td scope="row" data-label="Allowed values">root, namespace, ns, database, db</td>
      <td scope="row" data-label="Notes">Authentication level to use when connecting.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_BIND`</td>
      <td scope="row" data-label="Command arg">`bind`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">127.0.0.1:8000</td>
      <td scope="row" data-label="Allowed values">String to an address</td>
      <td scope="row" data-label="Notes">The hostname or IP address(es) to listen for connections on.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_ALL`</td>
      <td scope="row" data-label="Command arg">`allow-all`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Allow all capabilities.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_ARBITRARY_QUERY`</td>
      <td scope="row" data-label="Command arg">`allow-arbitrary-query`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">guest, record, system (comma-separated)</td>
      <td scope="row" data-label="Notes">Allows arbitrary queries to be used by user groups except when specifically denied. Alternatively, you can provide a comma-separated list of user groups to allow specifically denied user groups to prevail over any other allowed user group.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_EXPERIMENTAL`</td>
      <td scope="row" data-label="Command arg">`allow-experimental`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">files, surrealism (comma-separated)</td>
      <td scope="row" data-label="Notes">Allow execution of experimental features.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_FUNC`</td>
      <td scope="row" data-label="Command arg">`allow-funcs`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">all functions allowed</td>
      <td scope="row" data-label="Allowed values">Empty, `*`, or comma-separated function paths</td>
      <td scope="row" data-label="Notes">Allow execution of all functions except for functions that are specifically denied. Set to an empty value or `*` to allow all functions. Use a comma-separated list (for example, `array,string::len,http::get`) to allow specific function families or names. Values such as `true` are not valid. The environment variable name is singular (`FUNC`), matching the `--allow-funcs` flag.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_GUESTS`</td>
      <td scope="row" data-label="Command arg">`allow-guests`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Allow guest users to execute queries.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_NET`</td>
      <td scope="row" data-label="Command arg">`allow-net`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">Comma-separated list of paths</td>
      <td scope="row" data-label="Notes">Allow all or certain outbound network access.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_SCRIPT`</td>
      <td scope="row" data-label="Command arg">`allow-scripting`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Allow execution of embedded scripting functions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_ALLOW_INSECURE_STORABLE_CLOSURES`*Since v2.5.0*</td>
      <td scope="row" data-label="Command arg">`allow-insecure-storable-closures`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Takes a boolean. Prevents closures from being stored, which eliminates a potential attack surface. For version 2.5.0, this can still be allowed by using this capability.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_DENY_ALL`</td>
      <td scope="row" data-label="Command arg">`deny-all`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Deny all capabilities.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_DENY_FUNC`</td>
      <td scope="row" data-label="Command arg">`deny-funcs`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false, comma-separated list</td>
      <td scope="row" data-label="Notes">Deny execution of all or certain functions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_DENY_GUESTS`</td>
      <td scope="row" data-label="Command arg">`deny-guests`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Deny guest users from executing queries.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_DENY_NET`</td>
      <td scope="row" data-label="Command arg">`deny-net`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false, comma-separated list</td>
      <td scope="row" data-label="Notes">Deny all or certain outbound access paths.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CAPS_DENY_SCRIPT`</td>
      <td scope="row" data-label="Command arg">`deny-scripting`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Deny execution of embedded scripting functions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CHANGEFEED_GC_INTERVAL`</td>
      <td scope="row" data-label="Command arg">`changefeed-gc-interval`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">30s</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The interval at which to perform changefeed garbage collection.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_CLIENT_IP`</td>
      <td scope="row" data-label="Command arg">`client-ip`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">none, socket, CF-Connecting-IP, Fly-Client-IP, True-Client-IP, X-Real-IP, X-Forwarded-For, Forwarded</td>
      <td scope="row" data-label="Notes">The method of detecting the client's IP address. *Since v3.1.0* `Forwarded` parses the RFC 7239 `Forwarded` header (`for=` parameter).</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DATABASE`</td>
      <td scope="row" data-label="Command arg">`database`</td>
      <td scope="row" data-label="Command">`sql`</td>
      <td scope="row" data-label="Default">main</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The database selected when starting the REPL.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_DATABASE`</td>
      <td scope="row" data-label="Command arg">`database`</td>
      <td scope="row" data-label="Command">`export`, `import`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The database selected for the import or export.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DEFAULT_DATABASE`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`default-database`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">main</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The default database to use when starting a SurrealDB instance.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_DEFAULT_NAMESPACE`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`default-namespace`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">main</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The default namespace to use when starting a SurrealDB instance.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_HIDE_WELCOME`</td>
      <td scope="row" data-label="Command arg">`hide-welcome`</td>
      <td scope="row" data-label="Command">`sql`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to show the welcome message when starting the REPL.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_IMPORT_FILE`</td>
      <td scope="row" data-label="Command arg">`import-file`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A file path</td>
      <td scope="row" data-label="Notes">Path to a SurrealQL file that will be imported when starting the server.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_INDEX_COMPACTION_INTERVAL`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`index-compaction-interval`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">5s</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The interval at which to perform changefeed garbage collection.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_KEY`</td>
      <td scope="row" data-label="Command arg">`key`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string 16, 24, or 32 bytes long</td>
      <td scope="row" data-label="Notes">Encryption key to use for on-disk encryption. Not currently in use.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_KVS_CA`</td>
      <td scope="row" data-label="Command arg">`kvs-ca`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a path</td>
      <td scope="row" data-label="Notes">Path to the CA file used when connecting to the remote KV store.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_KVS_CRT`</td>
      <td scope="row" data-label="Command arg">`kvs-crt`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a path</td>
      <td scope="row" data-label="Notes">Path to the certificate file used when connecting to the remote KV store.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_KVS_KEY`</td>
      <td scope="row" data-label="Command arg">`kvs-key`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a path</td>
      <td scope="row" data-label="Notes">Path to the private key file used when connecting to the remote KV store.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LAZY_SURREALISM`*Since v3.1.0*</td>
      <td scope="row" data-label="Command arg">`lazy-surrealism`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to lazy-load Surrealism modules instead of eagerly compiling them at server startup.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG`</td>
      <td scope="row" data-label="Command arg">`log`</td>
      <td scope="row" data-label="Command">`start`, `fix`</td>
      <td scope="row" data-label="Default">info</td>
      <td scope="row" data-label="Allowed values">none, full, error, warn, info, debug, trace</td>
      <td scope="row" data-label="Notes">The logging level for the database server.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_FILE_ENABLED`*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-file-enabled`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Toggles file output.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_FILE_FORMAT`*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-file-format`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">text, json</td>
      <td scope="row" data-label="Notes">The format for log file output.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_FILE_LEVEL`*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-file-level`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">none, full, error, warn, info, debug, trace</td>
      <td scope="row" data-label="Notes">Override the logging level for file output</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_FILE_NAME`*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-file-name`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">surrealdb.log</td>
      <td scope="row" data-label="Allowed values">String to a file</td>
      <td scope="row" data-label="Notes">Filename for logs (default: `surrealdb.log`)</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_FILE_PATH`*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-file-path`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">logs</td>
      <td scope="row" data-label="Allowed values">String to a path</td>
      <td scope="row" data-label="Notes">Sets the directory for logs</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_FILE_ROTATION`*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-file-rotation`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">daily</td>
      <td scope="row" data-label="Allowed values">daily, hourly, never</td>
      <td scope="row" data-label="Notes">Sets the rotation duration for logs.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_FORMAT`*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-format`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">text</td>
      <td scope="row" data-label="Allowed values">text, json</td>
      <td scope="row" data-label="Notes">Sets the format for logs.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_OTEL_LEVEL`  
*Since v2.4.0*</td>
      <td scope="row" data-label="Command arg">`log-otel-level`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">SURREAL_LOG logging level</td>
      <td scope="row" data-label="Allowed values">none, full, error, warn, info, debug, trace</td>
      <td scope="row" data-label="Notes">Override the logging level for OpenTelemetry</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_SOCKET`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`log-socket`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a host:port</td>
      <td scope="row" data-label="Notes">Send logs to the specified host:port</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_SOCKET_FORMAT`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`log-socket-format`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">text</td>
      <td scope="row" data-label="Allowed values">text, json</td>
      <td scope="row" data-label="Notes">  Set the format of the logs to the socket.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_LOG_SOCKET_LEVEL`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`log-socket-level`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">SURREAL_LOG logging level</td>
      <td scope="row" data-label="Allowed values">none, full, error, warn, info, debug, trace</td>
      <td scope="row" data-label="Notes">  Override the logging level for socket logs. Possible values: none, full, error, warn, info, debug, trace</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_NAME`</td>
      <td scope="row" data-label="Command arg">`name`</td>
      <td scope="row" data-label="Command">`ml export`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The name of the model.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_NAMESPACE`</td>
      <td scope="row" data-label="Command arg">`namespace`</td>
      <td scope="row" data-label="Command">`sql`</td>
      <td scope="row" data-label="Default">main</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The namespace to connect to via the REPL.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_NAMESPACE`</td>
      <td scope="row" data-label="Command arg">`namespace`</td>
      <td scope="row" data-label="Command">`export`, `import`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The namespace selected for the import/export operation.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_NO_BANNER`</td>
      <td scope="row" data-label="Command arg">`no-banner`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to hide the startup banner.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_NO_DEFAULTS`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`no-defaults`</td>
      <td scope="row" data-label="Command">``start``</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to disable default namespace and database creation. Conflicts with SURREAL_DEFAULT_DATABASE and SURREAL_DEFAULT_NAMESPACE, which set a default value for namespace and database for a new instance.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_NO_IDENTIFICATION_HEADERS`</td>
      <td scope="row" data-label="Command arg">`no-identification-headers`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to suppress the server name and version headers.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_NODE_MEMBERSHIP_CHECK_INTERVAL`</td>
      <td scope="row" data-label="Command arg">`node-membership-check-interval`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">15s</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The interval at which to process and archive inactive nodes.</td>
    </tr>
  <tr>
      <td scope="row" data-label="Env var">`SURREAL_NODE_MEMBERSHIP_CLEANUP_INTERVAL`</td>
      <td scope="row" data-label="Command arg">`node-membership-cleanup-interval`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">300s</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The interval at which to process and cleanup archived nodes.</td>
    </tr>
  <tr>
      <td scope="row" data-label="Env var">`SURREAL_NODE_MEMBERSHIP_REFRESH_INTERVAL`</td>
      <td scope="row" data-label="Command arg">`node-membership-refresh-interval`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">3s</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The interval at which to refresh node registration information.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_PASS`</td>
      <td scope="row" data-label="Command arg">`pass`</td>
      <td scope="row" data-label="Command">`export`, `import`, `sql`, `start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">Database authentication password to use when connecting.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">SURREAL_PATH</td>
      <td scope="row" data-label="Command arg">`path`</td>
      <td scope="row" data-label="Command">`fix`, `start`</td>
      <td scope="row" data-label="Default">memory</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">Database path used for storing data. As a required argument (albeit with a default), it is not passed in via `--path`.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_PLANNER_STRATEGY`*Since v3.0.0*</td>
      <td scope="row" data-label="Command arg">`planner-strategy`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">best-effort</td>
      <td scope="row" data-label="Allowed values">best-effort|compute-only|all-read-only</td>
      <td scope="row" data-label="Notes">Which strategy to use with the new query planner introduced in SurrealDB 3.0. The default setting uses the new planner for read-only statements, falling back to the previous compute planner on unimplemented paths. The new planner can be skipped entirely by using compute-only.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_QUERY_TIMEOUT`</td>
      <td scope="row" data-label="Command arg">`query-timeout`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The maximum duration that a set of statements can run for.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SLOW_QUERY_LOG_THRESHOLD`  
*Since v2.3.8*</td>
      <td scope="row" data-label="Command arg">`slow-log-threshold`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">A duration specifying the minimum execution time after which a log is made to indicate a slow query</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SLOW_QUERY_LOG_PARAM_ALLOW`  
`slow-log-param-allow` *Since v2.3.9*</td>
      <td scope="row" data-label="Command arg">`slow-log-param-allow`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">Comma-separated strings</td>
      <td scope="row" data-label="Notes">A comma-separated list of parameter names to include in slow query logs.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SLOW_QUERY_LOG_PARAM_DENY`*Since v2.3.9*</td>
      <td scope="row" data-label="Command arg">`slow-log-param-deny`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">Comma-separated strings</td>
      <td scope="row" data-label="Notes">A comma-separated list of parameter names to omit from slow query logs.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_STRICT`</td>
      <td scope="row" data-label="Command arg">`strict`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether strict mode is enabled on this database instance. Ignored since SurrealDB 3.0 after which strictness is defined [per database](../../query-language/statements/define/database.md#defining-a-strict-database) instead of instance.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TEMPORARY_DIRECTORY`</td>
      <td scope="row" data-label="Command arg">`temporary-directory`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a directory</td>
      <td scope="row" data-label="Notes">Sets the directory for storing temporary database files</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TOKEN`</td>
      <td scope="row" data-label="Command arg">`token`</td>
      <td scope="row" data-label="Command">`export`, `import`, `sql`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">Authentication token in JWT format to use when connecting.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TRANSACTION_TIMEOUT`</td>
      <td scope="row" data-label="Command arg">`transaction-timeout`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The maximum duration that any single transaction can run for.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_UNAUTHENTICATED`</td>
      <td scope="row" data-label="Command arg">`unauthenticated`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to allow unauthenticated access.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_USER`</td>
      <td scope="row" data-label="Command arg">`user`</td>
      <td scope="row" data-label="Command">`export`, `import`, `sql`, start</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">Database authentication username to use when connecting.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_VERSION`</td>
      <td scope="row" data-label="Command arg">`version`</td>
      <td scope="row" data-label="Command">`ml export`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">The version of the ML model.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEB_CRT`</td>
      <td scope="row" data-label="Command arg">`web-crt`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a path</td>
      <td scope="row" data-label="Notes">Path to the certificate file for encrypted client connections.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_WEB_KEY`</td>
      <td scope="row" data-label="Command arg">`web-key`</td>
      <td scope="row" data-label="Command">`start`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">String to a path</td>
      <td scope="row" data-label="Notes">Path to the private key file for encrypted client connections.</td>
    </tr>
  </tbody>
</table>

## Storage backend environment variables

These environment variables are used to configure the storage backend for SurrealDB.

### RocksDB environment variables

Many RocksDB environment variables pertain to memory use. The default configuration results in the following rough estimates of RocksDB memory use on different instances:

| Instance memory size  | Estimate
| ------------- |:-------------:|
| 512 MiB | ~ 80MiB |
| 1 GiB | ~ 80MiB
| 2 GiB | ~ 640MiB
| 4 GiB | ~ 1.25GiB
| 8 GiB | ~ 3.25GiB
| 24 GiB | ~ 12GiB
| 128 GiB | ~ 67GiB

The available environment variables for configuring a RocksDB instance are:

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '50%'}}>Environment variable</th>
      <th scope="col" style={{width: '15%'}}>Default</th>
      <th scope="col" style={{width: '15%'}}>Allowed values</th>
      <th scope="col" style={{width: '30%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BACKGROUND_FLUSH`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">false, true</td>
      <td scope="row" data-label="Notes">Whether to enable background WAL file flushing.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BACKGROUND_FLUSH_INTERVAL`</td>
      <td scope="row" data-label="Default">200 (milliseconds)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The interval in milliseconds between background flushes.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BLOB_COMPRESSION_TYPE`</td>
      <td scope="row" data-label="Default">snappy</td>
      <td scope="row" data-label="Allowed values">none, snappy, lz4, zstd</td>
      <td scope="row" data-label="Notes">Compression type used for blob files.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BLOB_FILE_SIZE`</td>
      <td scope="row" data-label="Default">268,435,456 (256 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The target blob file size for RocksDB.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_ENABLE_BLOB_GC`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to enable blob garbage collection for RocksDB.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BLOB_GC_AGE_CUTOFF`</td>
      <td scope="row" data-label="Default">0.5</td>
      <td scope="row" data-label="Allowed values">Float between 0 and 1</td>
      <td scope="row" data-label="Notes">Fractional age cutoff for blob GC.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BLOB_GC_FORCE_THRESHOLD`</td>
      <td scope="row" data-label="Default">0.5</td>
      <td scope="row" data-label="Allowed values">Float between 0 and 1</td>
      <td scope="row" data-label="Notes">Discardable ratio threshold to force GC.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BLOB_COMPACTION_READAHEAD_SIZE`</td>
      <td scope="row" data-label="Default">0</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Readahead size for blob compaction/GC.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BLOCK_CACHE_SIZE`</td>
      <td scope="row" data-label="Default">Dynamically calculated via greater of ((system memory / 2) - 1 GiB) and 16MiB</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">RocksDB <a href="https://github.com/facebook/rocksdb/wiki/memory-usage-in-rocksdb">block cache size</a> in bytes</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_BLOCK_SIZE`</td>
      <td scope="row" data-label="Default">65,536 (64 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The size of each uncompressed data block in bytes.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_COMPACTION_READAHEAD_SIZE`</td>
      <td scope="row" data-label="Default">4 MiB (systems under 4 GiB), 8 MiB (up to 16 GiB), 16 MiB (others)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The readahead buffer size used during compaction.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_COMPACTION_STYLE` *Since v2.0.3*</td>
      <td scope="row" data-label="Default">level</td>
      <td scope="row" data-label="Allowed values">level, universal</td>
      <td scope="row" data-label="Notes">Use to specify the database compaction style.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_DELETION_FACTORY_DELETE_COUNT`*Since v2.0.3*</td>
      <td scope="row" data-label="Default">50</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of deletions to track in the window.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_DELETION_FACTORY_RATIO`*Since v2.0.3*</td>
      <td scope="row" data-label="Default">0.5</td>
      <td scope="row" data-label="Allowed values">A float</td>
      <td scope="row" data-label="Notes">The ratio of deletions to track in the window.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_DELETION_FACTORY_WINDOW_SIZE`*Since v2.0.3*</td>
      <td scope="row" data-label="Default">1000</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The size of the window used to track deletions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_ENABLE_BLOB_FILES`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to enable separate key and value file storage.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_ENABLE_PIPELINED_WRITES`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to use separate queues for WAL writes and memtable writes.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_GROUPED_COMMIT`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to enable grouped commit when sync is enabled. When enabled, multiple transaction commits are batched together and flushed to disk with a single fsync operation, improving throughput. When disabled, each transaction is committed and synced individually, which may provide lower latency for single transactions at the cost of reduced throughput under high load. Only used when SURREAL_SYNC_DATA is enabled and SURREAL_ROCKSDB_BACKGROUND_FLUSH is disabled.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_GROUPED_COMMIT_MAX_BATCH_SIZE`</td>
      <td scope="row" data-label="Default">4096</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of transactions in a single grouped commit batch. Used to prevent unbounded memory growth while still allowing large batches for efficiency. Larger batches improve throughput but increase memory usage and commit latency.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_GROUPED_COMMIT_TIMEOUT`</td>
      <td scope="row" data-label="Default">5ms</td>
      <td scope="row" data-label="Allowed values">A duration</td>
      <td scope="row" data-label="Notes">The maximum wait time in nanosecond before forcing a grouped commit. Used to ensure that transactions do not wait indefinitely when concurrency is low, and to balance between transaction latency and write throughput.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_GROUPED_COMMIT_WAIT_THRESHOLD`</td>
      <td scope="row" data-label="Default">12</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Threshold for deciding whether to wait for more transactions. If the current batch size is greater or equal to this threshold (and below ROCKSDB_GROUPED_COMMIT_MAX_BATCH_SIZE), then the coordinator will wait up to ROCKSDB_GROUPED_COMMIT_TIMEOUT to collect more transactions. Smaller batches are flushed immediately to preserve low latency.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_FILE_COMPACTION_TRIGGER`</td>
      <td scope="row" data-label="Default">4</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of files needed to trigger level 0 compaction.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_JOBS_COUNT` *Since v2.0.3*</td>
      <td scope="row" data-label="Default">Number of CPUs * 2</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of threads to use for flushing and compaction.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_KEEP_LOG_FILE_NUM`</td>
      <td scope="row" data-label="Default">10</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of information log files to keep.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_MAX_CONCURRENT_SUBCOMPACTIONS`</td>
      <td scope="row" data-label="Default">4</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number threads which will perform compactions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_MAX_OPEN_FILES`</td>
      <td scope="row" data-label="Default">1024</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of open files which can be opened by RocksDB.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_MAX_WRITE_BUFFER_NUMBER`</td>
      <td scope="row" data-label="Default">2 (systems under 4 GiB), 4 (up to 16 GiB), 8 (up to 64 GiB), 32 (others)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of write buffers which can be used.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_MIN_BLOB_SIZE`</td>
      <td scope="row" data-label="Default">4096</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The minimum size in bytes of a value for it to be stored in blob files.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_MIN_WRITE_BUFFER_NUMBER_TO_MERGE`</td>
      <td scope="row" data-label="Default">2</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The minimum number of write buffers to merge before writing to disk.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_SST_MAX_ALLOWED_SPACE_USAGE`</td>
      <td scope="row" data-label="Default">0</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum allowed space usage for SST files in bytes. The default of 0 means unlimited and disables space monitoring. When this limit is reached, the datastore enters read-and-deletion-only mode, where only read and delete operations are allowed. This allows gradual space recovery through data deletion.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_STORAGE_LOG_LEVEL`</td>
      <td scope="row" data-label="Default">warn</td>
      <td scope="row" data-label="Allowed values">none, full, error, warn, info, debug, trace</td>
      <td scope="row" data-label="Notes">The information log level of the RocksDB library.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_TARGET_FILE_SIZE_BASE`</td>
      <td scope="row" data-label="Default">67,108,864 (64 MiB)</td>
      <td scope="row" data-label="Allowed values">—</td>
      <td scope="row" data-label="Notes">The target file size for compaction in bytes.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_TARGET_FILE_SIZE_MULTIPLIER`</td>
      <td scope="row" data-label="Default">2</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The target file size multiplier for each compaction level.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_THREAD_COUNT`</td>
      <td scope="row" data-label="Default">Number of CPUs on machine</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The number of threads to start for flushing and compaction.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_WAL_SIZE_LIMIT`</td>
      <td scope="row" data-label="Default">0</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The write-ahead-log size limit in MiB.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_ROCKSDB_WRITE_BUFFER_SIZE`</td>
      <td scope="row" data-label="Default">32 MiB (systems under 1 GiB), 64 MiB (up to 16 GiB), 128 MiB (others)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The amount of data each write buffer can build up in memory.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SYNC_DATA`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to sync writes to disk before acknowledgement.</td>
    </tr>
  </tbody>
</table>

### SurrealKV environment variables

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '50%'}}>Environment variable</th>
      <th scope="col" style={{width: '15%'}}>Default</th>
      <th scope="col" style={{width: '15%'}}>Allowed values</th>
      <th scope="col" style={{width: '30%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_ENABLE_VLOG`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to enable value log separation.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_VERSIONED_INDEX`</td>
      <td scope="row" data-label="Default">false</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to enable versioned index. Only applies when versioning is enabled.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_BLOCK_SIZE`</td>
      <td scope="row" data-label="Default">65_536 (64 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The block size in bytes.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_VLOG_MAX_FILE_SIZE`</td>
      <td scope="row" data-label="Default">64 MiB (systems under 4 GiB), 128 MiB (up to 16 GiB), 256 MiB (up to 64 GiB), 512 MiB (others)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The readahead buffer size used during compaction.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_VLOG_THRESHOLD`</td>
      <td scope="row" data-label="Default">4096 (4 KiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The value log threshold in bytes. Values larger than this are stored in the value log.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_BLOCK_CACHE_CAPACITY`</td>
      <td scope="row" data-label="Default">Dynamically calculated via greater of ((system memory / 2) - 1 GiB) and 16MiB</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum log file size in bytes.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_GROUPED_COMMIT_TIMEOUT`</td>
      <td scope="row" data-label="Default">5ms</td>
      <td scope="row" data-label="Allowed values">A duration in nanoseconds</td>
      <td scope="row" data-label="Notes">The maximum wait time in nanoseconds before forcing a grouped commit. Ensures that transactions do not wait indefinitely under low concurrency and balances commit latency against write throughput.</td>
    </tr>
<tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_GROUPED_COMMIT_WAIT_THRESHOLD`</td>
      <td scope="row" data-label="Default">12</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Threshold for deciding whether to wait for more transactions. If the current batch size is greater or equal to this threshold (and below SURREAL_SURREALKV_GROUPED_COMMIT_MAX_BATCH_SIZE), then the coordinator will wait up to SURREAL_SURREALKV_GROUPED_COMMIT_TIMEOUT to collect more transactions. Smaller batches are flushed immediately to preserve low latency.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_SURREALKV_GROUPED_COMMIT_MAX_BATCH_SIZE`</td>
      <td scope="row" data-label="Default">4096</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The maximum number of transactions in a single grouped commit batch. This prevents unbounded memory growth while still allowing large batches for efficiency. Larger batches improve throughput but increase memory usage and commit latency.</td>
    </tr>
  </tbody>
</table>

### TiKV environment variables

<table>
  <thead>
    <tr>
      <th scope="col" style={{width: '50%'}}>Environment variable</th>
      <th scope="col" style={{width: '15%'}}>Default</th>
      <th scope="col" style={{width: '15%'}}>Allowed values</th>
      <th scope="col" style={{width: '30%'}}>Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TIKV_API_VERSION`</td>
      <td scope="row" data-label="Default">1</td>
      <td scope="row" data-label="Allowed values">A u8</td>
      <td scope="row" data-label="Notes">Which TiKV cluster API version to use.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TIKV_ASYNC_COMMIT`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to use asynchronous transactions.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TIKV_KEYSPACE`</td>
      <td scope="row" data-label="Default">none</td>
      <td scope="row" data-label="Allowed values">A string</td>
      <td scope="row" data-label="Notes">A string specifying the keyspace identifier for data isolation.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TIKV_GRPC_MAX_DECODING_MESSAGE_SIZE`*Since v2.1.8*</td>
      <td scope="row" data-label="Default">4,194,304 (4 MiB)</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">Sets the maximum decoding size of a gRPC message.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TIKV_ONE_PHASE_COMMIT`</td>
      <td scope="row" data-label="Default">true</td>
      <td scope="row" data-label="Allowed values">true, false</td>
      <td scope="row" data-label="Notes">Whether to use one-phase transaction commit.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_TIKV_REQUEST_TIMEOUT`</td>
      <td scope="row" data-label="Default">10</td>
      <td scope="row" data-label="Allowed values">A usize</td>
      <td scope="row" data-label="Notes">The duration in seconds for requests before they time out.</td>
    </tr>
  </tbody>
</table>

### FoundationDB environment variables

> [!WARNING]
> FoundationDB support is deprecated in SurrealDB `3.0`. Please plan to migrate to a supported storage backend.

<table>
  <thead>
    <tr>
      <th scope="col">Environment variable</th>
      <th scope="col">Default value</th>
      <th scope="col">Notes</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_FOUNDATIONDB_TRANSACTION_MAX_RETRY_DELAY`</td>
      <td scope="row" data-label="Default">500</td>
      <td scope="row" data-label="Notes">The maximum delay between transaction retries in milliseconds.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_FOUNDATIONDB_TRANSACTION_RETRY_LIMIT`</td>
      <td scope="row" data-label="Default">5</td>
      <td scope="row" data-label="Notes">The maximum number of times a transaction can be retried.</td>
    </tr>
    <tr>
      <td scope="row" data-label="Env var">`SURREAL_FOUNDATIONDB_TRANSACTION_TIMEOUT`</td>
      <td scope="row" data-label="Default">5000</td>
      <td scope="row" data-label="Notes">The maximum transaction timeout in milliseconds.</td>
    </tr>
  </tbody>
</table>

## SurrealDB Cloud environment variables

Instances on SurrealDB Cloud are not started with a CLI command or environment variables. Instead, they can be set on the [Configure Instance](../../../build/deployment/surrealdb-cloud/getting-started/create-an-instance.md#configure-an-instance) panel.
