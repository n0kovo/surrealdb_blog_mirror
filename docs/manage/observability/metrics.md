---
position: 5
title: Metrics reference
description: Access paths, label catalogue and the complete metric reference for SurrealDB Community and Enterprise, with a migration table from 3.0.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/observability/metrics.mdx"
---

# Metrics reference

This page is the canonical reference for every metric emitted by SurrealDB. It covers how operators access them, the labels and naming rules that govern the surface, the full catalogue grouped by signal family, the public allowlist for anonymous scrapers, and the migration table from 3.0 names.

*Since v3.1.0*

The instruments listed below were introduced as part of the 3.1 observability overhaul. The [Migration from 3.0](#migration-from-30) section at the bottom maps every legacy Prometheus name to its current replacement.

## Access paths

Metrics can be exposed in two complementary ways. Both pipelines can run simultaneously.

### Prometheus pull

| Property | Value |
| --- | --- |
| Trigger | `SURREAL_METRICS_ENABLED=true` (default) |
| Transport | `GET /metrics` on the main HTTP port, content-type `text/plain; version=0.0.4` |
| Authentication | Root credentials gate the full surface. Anonymous scrapers receive the [`PUBLIC_METRICS`](#public-metrics-allowlist) allowlist only. |
| Surface | Every instrument the running build registers. |

Disable the endpoint by setting `SURREAL_METRICS_ENABLED=false` — the route then returns `404`.

### OTLP push

| Property | Value |
| --- | --- |
| Trigger | `SURREAL_TELEMETRY_PROVIDER=otlp` |
| Transport | gRPC, default endpoint `http://localhost:4317`, push cadence from `OTEL_METRIC_EXPORT_INTERVAL` (milliseconds; default `60000`), cumulative temporality |
| Authentication | The collector's responsibility. The exporter speaks gRPC and native-TLS but does not enforce client authentication. |
| Surface | The same instruments as `/metrics`, plus the OTel logs surface (audit and slow-query records, when their OTel export is enabled) and `tracing` spans. |

Selectively disable parts of the OTLP pipeline:

- `SURREAL_TELEMETRY_DISABLE_METRICS=true` — suppress the OTLP metrics reader, leaving logs and traces unaffected.
- `SURREAL_TELEMETRY_DISABLE_TRACING=true` — suppress the OTLP trace exporter, leaving metrics and logs unaffected.

For the full environment variable reference, see [Configuration](configuration.md#core-knobs).

## Render rules

OpenTelemetry instrument names use a dotted form (`surrealdb.statement.duration`). The Prometheus text exporter converts each instrument deterministically:

- Counters get a `_total` suffix.
- Histograms and counters with unit `s` get a `_seconds` suffix.
- Histograms and counters with unit `By` get a `_bytes` suffix.
- Up-down counters render as plain gauges with no suffix.
- Attribute keys containing dots (`http.request.method`, `http.route`, `rpc.method`) are sanitised to underscore form at render time.

A few worked examples:

<table>
    <thead>
        <tr>
            <th scope="col">OpenTelemetry name</th>
            <th scope="col">Unit</th>
            <th scope="col">Prometheus name</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="OTel">`surrealdb.statement.duration`</td>
            <td scope="row" data-label="Unit">`s`</td>
            <td scope="row" data-label="Prometheus">`surrealdb_statement_duration_seconds`</td>
        </tr>
        <tr>
            <td scope="row" data-label="OTel">`surrealdb.statement` (counter)</td>
            <td scope="row" data-label="Unit">—</td>
            <td scope="row" data-label="Prometheus">`surrealdb_statement_total`</td>
        </tr>
        <tr>
            <td scope="row" data-label="OTel">`surrealdb.http.request.size`</td>
            <td scope="row" data-label="Unit">`By`</td>
            <td scope="row" data-label="Prometheus">`surrealdb_http_request_size_bytes_total`</td>
        </tr>
        <tr>
            <td scope="row" data-label="OTel">`surrealdb.process.memory`</td>
            <td scope="row" data-label="Unit">`By`</td>
            <td scope="row" data-label="Prometheus">`surrealdb_process_memory_bytes`</td>
        </tr>
        <tr>
            <td scope="row" data-label="OTel">`surrealdb.http.active_requests` (up-down counter)</td>
            <td scope="row" data-label="Unit">—</td>
            <td scope="row" data-label="Prometheus">`surrealdb_http_active_requests`</td>
        </tr>
    </tbody>
</table>

## Common labels

Every labelled family carries `outcome` plus the resolved tenant context (`namespace`, `database`, `user`) where applicable. Unresolved values render as the `"-"` sentinel; record-access principals render as the fixed `<record>` sentinel.

<table>
    <thead>
        <tr>
            <th scope="col">Key</th>
            <th scope="col">Bounded values</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Key">`outcome`</td>
            <td scope="row" data-label="Values">`success`, `error`, `cancelled`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`statement_type`</td>
            <td scope="row" data-label="Values">`select`, `update`, `create`, … (closed AST set)</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`namespace` / `database` / `user`</td>
            <td scope="row" data-label="Values">Free-form strings up to a user-configured length. `"-"` when unresolved; `&lt;record&gt;` for record-access principals.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`protocol`</td>
            <td scope="row" data-label="Values">`websocket`, `http`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`auth_action`</td>
            <td scope="row" data-label="Values">`signin`, `signup`, `authenticate`, …</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`auth_scope`</td>
            <td scope="row" data-label="Values">`root`, `namespace`, `database`, `record`, `none`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`http_request_method`</td>
            <td scope="row" data-label="Values">`get`, `post`, `put`, `delete`, `patch`, `head`, `options`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`http_route`</td>
            <td scope="row" data-label="Values">Matched router pattern, bounded by the router definitions. `"-"` for unmatched.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`http_response_status_code`</td>
            <td scope="row" data-label="Values">Stringified status (`200`, `400`, …)</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`rpc_method`</td>
            <td scope="row" data-label="Values">Bounded by the RPC dispatch table.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Key">`error_class`</td>
            <td scope="row" data-label="Values">Bounded; populated only when `outcome != success`.</td>
        </tr>
    </tbody>
</table>

The SurrealDS cluster family adds a small set of additional labels (`peer`, `kind`, `message_type`, `path`, `phase`, `role`, `result`, `source`, `reason`). See [SurrealDS labels](#surrealds-labels) further down.

## Metric catalogue

The catalogue is grouped by signal family. Each subsection lists the Prometheus name (the form an operator scrapes), the instrument type, the edition that exposes it, the labels it carries, and any notes.

### Process — `surrealdb.process`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
            <th scope="col">Notes</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_build_info`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">`build_version`</td>
            <td scope="row" data-label="Notes">Always `1`. The value carries no signal; the label is the static compile-time version.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_process_uptime_seconds`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">—</td>
            <td scope="row" data-label="Notes">Seconds since process start.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_process_memory_bytes`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">—</td>
            <td scope="row" data-label="Notes">Resident set size of the process.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_process_cpu_percent`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">—</td>
            <td scope="row" data-label="Notes">Aggregate process CPU %. May exceed `100` on multi-core hosts.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`target_info`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">resource attributes</td>
            <td scope="row" data-label="Notes">Emitted by the OTel SDK from the process `Resource`. Carries `service_edition`.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`otel_scope_info`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">scope attributes</td>
            <td scope="row" data-label="Notes">Emitted by the OTel SDK per instrumentation scope.</td>
        </tr>
    </tbody>
</table>

The cadence of the process snapshot can be tuned with `SURREAL_PROCESS_METRICS_REFRESH_INTERVAL` (seconds; default `5`, floored at 1).

### Statement — `surrealdb.statement`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_statement_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`statement_type, outcome, error_class, namespace, database, user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_statement_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_statement_rows_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">same as above. Recorded only when `result_rows &gt; 0`.</td>
        </tr>
    </tbody>
</table>

### Query — `surrealdb.query`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_query_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`outcome, error_class, namespace, database, user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_query_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
    </tbody>
</table>

### Transaction — `surrealdb.transaction`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`write, outcome, error_class, namespace, database, user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_kv_ops_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`op` (`get` / `scan` / `set` / `del` / …)</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_keys_read_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`outcome`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_keys_written_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`outcome`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_key_bytes_read_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`outcome`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_value_bytes_read_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`outcome`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_key_bytes_written_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`outcome`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_value_bytes_written_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`outcome`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_transaction_conflicts_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`namespace, database, user` only. Doubles as the retry-pressure signal — alert on `rate(...[5m])`.</td>
        </tr>
    </tbody>
</table>

### RPC — `surrealdb.rpc`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_rpc_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`rpc_method, outcome, error_class, namespace, database, user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_rpc_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
    </tbody>
</table>

### Auth — `surrealdb.auth`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_auth_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`auth_action, auth_scope, outcome, error_class, namespace, database, user`</td>
        </tr>
    </tbody>
</table>

### Session — `surrealdb.session`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_session_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`session_action` (`connect` / `disconnect`), `protocol`, `service`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_session_active`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">`protocol, service`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_session_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">`protocol, service`</td>
        </tr>
    </tbody>
</table>

### Network — `surrealdb.network`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_network_received_bytes_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`protocol, namespace, database, user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_network_sent_bytes_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
    </tbody>
</table>

### HTTP — `surrealdb.http`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_http_request_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`http_request_method, http_route, http_response_status_code, outcome, error_class, namespace, database, user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_http_request_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_http_request_size_bytes_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_http_response_size_bytes_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_http_active_requests`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">`http_request_method, http_route` (attribute-stripped to keep the gauge balanced)</td>
        </tr>
    </tbody>
</table>

### Live query — `surrealdb.live_query`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_live_query_active`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">—</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_live_query_notifications_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">—</td>
        </tr>
    </tbody>
</table>

### Slow-query counter — `surrealdb.slow_query`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_slow_query_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">Same labels as `surrealdb_statement_total`. Increments when statement duration ≥ `SURREAL_SLOW_QUERY_METRIC_THRESHOLD_MS` (default 1000 ms; `0` disables the counter).</td>
        </tr>
    </tbody>
</table>

The slow-query counter is a Community-edition signal — it bumps for every statement that crosses the threshold. The [Enterprise slow-query log pipeline](slow-query-logging.md) produces full records on top of this counter.

### GraphQL — `surrealdb.graphql`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_graphql_operation_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`operation_type` (`query` / `mutation` / `subscription`), `outcome`, `error_class`, `namespace`, `database`, `user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_graphql_operation_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
    </tbody>
</table>

### MCP — `surrealdb.mcp`

<Edition value="community" />

<table>
    <thead>
        <tr>
            <th scope="col">Name</th>
            <th scope="col">Type</th>
            <th scope="col">Labels</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_mcp_tool_invocation_total`</td>
            <td scope="row" data-label="Type">counter</td>
            <td scope="row" data-label="Labels">`tool, transport, outcome, error_class, namespace, database, user`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_mcp_tool_duration_seconds`</td>
            <td scope="row" data-label="Type">histogram</td>
            <td scope="row" data-label="Labels">same as above</td>
        </tr>
        <tr>
            <td scope="row" data-label="Name">`surrealdb_mcp_session_active`</td>
            <td scope="row" data-label="Type">gauge</td>
            <td scope="row" data-label="Labels">`transport`</td>
        </tr>
    </tbody>
</table>

### Storage backend — `surrealdb.storage.<backend>`

<Edition value="community" />

Each enabled backend publishes a manifest of `u64` values through the transaction layer. The server bridge registers each entry as an observable gauge under `surrealdb.storage.<backend>.<metric>`; Prometheus renders them as `surrealdb_storage_<backend>_<metric>`. The set is backend-specific (RocksDB, in-memory, SurrealKV) and may change between releases — the canonical list at runtime is whatever the running build exposes at `/metrics`.

Treat these metrics as operator-only — they leak backend-specific implementation detail (compaction stats, block cache hits, etc.) that is rarely meaningful outside the operator persona.

### SurrealDS cluster — `surrealdb.ds`

<Edition value="enterprise" /> *Since v3.1.0*

> [!NOTE]
> **SurrealDS** is SurrealDB's distributed storage engine, available on [SurrealDB Cloud Scale](https://surrealdb.com/pricing/scale) and in self-hosted Enterprise deployments. These instruments apply when an Enterprise build runs the DS runtime with at least one metrics reader configured.

The SurrealDS cluster family is registered by the Enterprise composer when the runtime has at least one metrics reader configured. Every instrument is operator-only — the [`PUBLIC_METRICS`](#public-metrics-allowlist) allowlist excludes the family in its entirety.

#### Network and transport

| Name | Type | Labels |
| --- | --- | --- |
| `surrealdb_ds_network_bytes_sent_bytes_total` | counter (`By`) | `peer` |
| `surrealdb_ds_network_bytes_received_bytes_total` | counter (`By`) | `peer` (omitted on reply-only variants) |
| `surrealdb_ds_network_packets_sent_total` | counter | `peer` |
| `surrealdb_ds_network_packets_received_total` | counter | `peer` (omitted on reply-only variants) |
| `surrealdb_ds_network_send_errors_total` | counter | `peer, kind` |
| `surrealdb_ds_messages_sent_total` | counter | `message_type, peer` |
| `surrealdb_ds_messages_received_total` | counter | `message_type, peer` (omitted on reply-only variants) |
| `surrealdb_ds_udp_reresolves_total` | counter | `reason` |

#### Transactions and consensus

| Name | Type | Labels |
| --- | --- | --- |
| `surrealdb_ds_transactions_committed_total` | counter | — |
| `surrealdb_ds_transactions_aborted_total` | counter | `reason` |
| `surrealdb_ds_occ_conflicts_total` | counter | — |
| `surrealdb_ds_consensus_path_total` | counter | `path` |
| `surrealdb_ds_consensus_fast_quorum_timeouts_total` | counter | — |
| `surrealdb_ds_consensus_stale_view_aborts_total` | counter | — |
| `surrealdb_ds_finalize_prepare_retries_total` | counter | — |
| `surrealdb_ds_operation_timeouts_total` | counter | `phase` |
| `surrealdb_ds_prepare_results_total` | counter | `role, result` |
| `surrealdb_ds_begin_replies_total` | counter | `role, result` (currently coordinator-side only) |
| `surrealdb_ds_reads_served_total` | counter | `source` |
| `surrealdb_ds_reads_begin_backoffs_total` | counter | — |

#### View management and recovery

| Name | Type | Labels |
| --- | --- | --- |
| `surrealdb_ds_view_changes_total` | counter | `outcome` |
| `surrealdb_ds_recovery_started_total` | counter | — |
| `surrealdb_ds_recovery_completed_total` | counter | `outcome` |
| `surrealdb_ds_recovery_transactions_applied_total` | counter | — |
| `surrealdb_ds_prepare_probes_total` | counter | `outcome` |

#### Garbage collection

| Name | Type | Labels |
| --- | --- | --- |
| `surrealdb_ds_gc_supervisor_ticks_total` | counter | — |
| `surrealdb_ds_gc_runs_total` | counter | `kind, outcome` |
| `surrealdb_ds_gc_records_collected_total` | counter | `kind` |
| `surrealdb_ds_gc_duration_seconds` | histogram | `kind, outcome` |

#### Live state (observable gauges)

Populated only after the replica is wired in via the enterprise observer install hook.

| Name | Type | Notes |
| --- | --- | --- |
| `surrealdb_ds_replica_state` | gauge | Encoded `Normal=0`, `ViewChange=1`, `Recovering=2`, `RecoveringCompleted=3`. |
| `surrealdb_ds_active_view_number` | gauge | Current TAPIR view number. |
| `surrealdb_ds_prepared_list_len` | gauge | Length of the prepared list. |
| `surrealdb_ds_records_len` | gauge | Length of the records list. |
| `surrealdb_ds_pending_finalises_len` | gauge | Number of pending finalises. |
| `surrealdb_ds_cluster_peers_unresolved` | gauge | Number of cluster peers currently unresolved. |

#### SurrealDS labels

| Key | Used on | Bounded values |
| --- | --- | --- |
| `peer` | `network_*`, `messages_*` | Stringified `NodeId` (interned). Cardinality bounded by cluster size. |
| `kind` | `network_send_errors`, `gc_runs`, `gc_records_collected`, `gc_duration_seconds` | `send_failed`, `serialisation`, `channel_closed`, `unresolved`, `no_endpoint`, `write_failed`, `other` (send errors); `upgrade_tentative`, `gc_records`, `repair_tentative_consensus`, `gc_pending_finalises`, `gc_unlogged_inflight`, `gc_finalize_prepare_decisions`, `backup_recovery` (GC). |
| `message_type` | `messages_sent`, `messages_received` | TAPIR message variants (closed set). |
| `path` | `consensus_path` | `fast`, `slow` |
| `phase` | `operation_timeouts` | `propose`, `finalize`, `broadcast`, `unlogged`, `recovery`, `inconsistent` |
| `role` | `prepare_results`, `begin_replies` | `replica`, `coordinator` |
| `result` | `prepare_results` | `ok`, `abort`, `abstain`, `retry` |
| `result` | `begin_replies` | `eligible`, `anterior_prepared`, `higher_committed` |
| `outcome` | `view_changes`, `recovery_completed`, `prepare_probes` | `triggered`, `completed`, `applied`, `retried`, `rebuild_failed` (view changes); `success`, `failure` (recovery); `committed`, `aborted`, `insufficient` (probes). |
| `source` | `reads_served` | `local`, `remote_eligible`, `remote_higher_committed` |
| `reason` | `transactions_aborted`, `udp_reresolves` | `conflict`, `abstain`, `other` (aborts); `unresolved`, `send_failure`, `recovery_view_change` (re-resolves). |

### Audit log pipeline self-metrics

<Edition value="enterprise" /> *Since v3.1.0*

Observable gauges registered when the [audit log pipeline](audit-logging.md) is enabled. The values are pulled at scrape time from atomic counters on the pipeline, so the cost is zero when nothing consumes the metric.

| Name | Type | Notes |
| --- | --- | --- |
| `surrealdb_audit_records` | gauge | Cumulative count of records successfully enqueued (observer → queue). |
| `surrealdb_audit_dropped` | gauge | Cumulative count of records dropped (overflow or queue closed). **Alert on any non-zero rate** — every drop is a lost record. |
| `surrealdb_audit_queue_depth` | gauge | Records currently buffered between observer and worker. Sustained depth above ~50% of `SURREAL_AUDIT_QUEUE_CAPACITY` indicates a slow sink. |
| `surrealdb_audit_appended` | gauge | Cumulative records the worker wrote to the sink. The gap to `surrealdb_audit_records` is queue depth plus append errors. |
| `surrealdb_audit_append_errors` | gauge | Cumulative sink-write failures. **Alert on any non-zero rate**. |

> These are exposed as gauges, not counters — the values are pulled live from atomic counters on the pipeline. The Prometheus name therefore has no `_total` suffix even though the underlying values are monotonic.

### Slow-query log pipeline self-metrics

<Edition value="enterprise" /> *Since v3.1.0*

The slow-query pipeline exposes the same shape as the audit pipeline under the `surrealdb.slow_query` scope:

| Name | Type | Notes |
| --- | --- | --- |
| `surrealdb_slow_query_records` | gauge | Cumulative records enqueued. |
| `surrealdb_slow_query_dropped` | gauge | Cumulative records dropped. **Alert on any non-zero rate**. |
| `surrealdb_slow_query_queue_depth` | gauge | Current queue depth. |
| `surrealdb_slow_query_appended` | gauge | Cumulative records written to the sink. |
| `surrealdb_slow_query_append_errors` | gauge | Cumulative sink-write failures. **Alert on any non-zero rate**. |

### Per-tenant rollups — `surrealdb.tenant`

<Edition value="enterprise" />

The `surrealdb.tenant` meter scope is **reserved** for low-cardinality per-tenant rollups keyed on `(namespace, database)` only. No instruments are currently registered under it. Until rollups land, customer-tenant filtering must be done at a proxy by filtering the higher-cardinality labelled families on `namespace` / `database`.

## Public metrics allowlist

Anonymous scrapers on `/metrics` see only the metrics on the public allowlist. Adding a metric to this list requires a security review. The six allowlisted metrics are:

- `surrealdb_build_info`
- `surrealdb_process_uptime_seconds`
- `surrealdb_process_memory_bytes`
- `surrealdb_process_cpu_percent`
- `target_info`
- `otel_scope_info`

Root credentials unlock the full surface for an authenticated scrape.

### Recommended cloud whitelist

For cloud and multi-tenant deployments the recommendation is a three-tier whitelist:

- **Tier 1 — Always public.** The allowlisted six above.
- **Tier 2 — Customer-visible (per-tenant, via proxy filter).** A subset of labelled families exposed to customers showing their own usage. Every metric in this tier carries `namespace` and `database` labels and the cloud proxy MUST filter on those before responding to a customer request — there is no server-side mechanism today that restricts a labelled family to a single tenant. Strip the `user` label before exposing. Suggested subset: `surrealdb_statement_*`, `surrealdb_transaction_total`, `surrealdb_transaction_duration_seconds`, `surrealdb_transaction_conflicts_total`, `surrealdb_query_*`, `surrealdb_http_request_total`, `surrealdb_network_received_bytes_total`, `surrealdb_network_sent_bytes_total`, `surrealdb_live_query_active`, `surrealdb_slow_query_total`.
- **Tier 3 — Operator-only.** Everything else: all `surrealdb_ds_*`, all pipeline self-metrics, `surrealdb_rpc_*` (full method dimension), `surrealdb_auth_*` (failure rates can be probed by an attacker), `surrealdb_graphql_*`, `surrealdb_mcp_*`, `surrealdb_storage_*`, `surrealdb_http_active_requests` (real-time concurrency snapshot), and the KV-layer `surrealdb_transaction_*` counters. Reach these over an internal sidecar or private network with root credentials.

## Cardinality and sensitivity

| Flag | Where it applies | Mitigation |
| --- | --- | --- |
| **Tenant-identifying** | `namespace`, `database`, `user` on every labelled family | Strip or filter at the proxy before exposing to a customer. Anonymous scrapers cannot see any family carrying these labels because the families are absent from the public allowlist. |
| **High-cardinality** | `peer` (DS, bounded by cluster size), `http_route`, `rpc_method` | Fine internally. External exposure should be conditional on the route or method set already being public. |
| **Workload inference** | All process gauges (uptime, memory, CPU) | Already on the allowlist, but in a single-tenant-per-pod deployment they correlate with tenant workload. Acceptable trade-off in most architectures. |
| **PII risk** | Audit and slow-query *records* carry SQL when `*_INCLUDE_SQL=true`. The pipeline self-metrics are safe; the records themselves go to the file sink and (opt-in) OTLP logs, not to `/metrics`. | Run the [three-pass redactor](audit-logging.md#redaction); alert on `*_append_errors`. |
| **Default-deny** | Multi-tenant deployments | Set `SURREAL_METRICS_ENABLED=false` on customer-facing pods; serve scrapes from an internal sidecar bound to a non-tenant-visible interface. |

## Alert hints

A starter set for production:

- `rate(surrealdb_statement_total{outcome="error"}[5m])` rising sharply against a baseline — application or operator error spike.
- `rate(surrealdb_transaction_conflicts_total[5m])` rising — OCC pressure or retry storms.
- `rate(surrealdb_ds_consensus_fast_quorum_timeouts_total[5m]) > 0` — consensus is falling through to the slow path.
- `surrealdb_ds_replica_state != 0` for more than a few seconds — a replica is in view-change or recovery.
- `surrealdb_ds_cluster_peers_unresolved > 0` for more than a startup window — DNS or connectivity gap.
- `rate(surrealdb_audit_dropped[5m]) > 0` or `rate(surrealdb_audit_append_errors[5m]) > 0` — audit records being lost.
- `surrealdb_audit_queue_depth` sustained above ~50% of `SURREAL_AUDIT_QUEUE_CAPACITY` — sink is falling behind.

## Migration from 3.0

The 3.1 release renamed the metric surface to a consistent `surrealdb.*` namespace. Legacy Prometheus names that operators may still see in old dashboards, and their current replacements:

<table>
    <thead>
        <tr>
            <th scope="col">3.0 name</th>
            <th scope="col">3.1 replacement</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_statements_completed_total`</td>
            <td scope="row" data-label="New">`surrealdb_statement_total{outcome="success"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_statement_errors_total`</td>
            <td scope="row" data-label="New">`surrealdb_statement_total{outcome="error"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_queries_completed_total`</td>
            <td scope="row" data-label="New">`surrealdb_query_total{outcome="success"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_query_errors_total`</td>
            <td scope="row" data-label="New">`surrealdb_query_total{outcome="error"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_query_dim_duration_seconds`</td>
            <td scope="row" data-label="New">`surrealdb_query_duration_seconds`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_transactions_completed_total`</td>
            <td scope="row" data-label="New">`surrealdb_transaction_total{outcome="success"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_transaction_writes_total`</td>
            <td scope="row" data-label="New">`surrealdb_transaction_total{write="true",outcome="success"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_transaction_errors_total`</td>
            <td scope="row" data-label="New">`surrealdb_transaction_total{outcome="error"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_rpcs_completed_total`</td>
            <td scope="row" data-label="New">`surrealdb_rpc_total{outcome="success"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_rpc_errors_total`</td>
            <td scope="row" data-label="New">`surrealdb_rpc_total{outcome="error"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_auth_attempts_total`</td>
            <td scope="row" data-label="New">`surrealdb_auth_total`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_auth_failures_total`</td>
            <td scope="row" data-label="New">`surrealdb_auth_total{outcome!="success"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_http_requests_completed_total`</td>
            <td scope="row" data-label="New">`surrealdb_http_request_total{outcome="success"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_http_request_errors_total`</td>
            <td scope="row" data-label="New">`surrealdb_http_request_total{outcome="error"}`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_http_dim_active_requests`</td>
            <td scope="row" data-label="New">`surrealdb_http_active_requests`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_network_dim_received_bytes_total`</td>
            <td scope="row" data-label="New">`surrealdb_network_received_bytes_total`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`surrealdb_network_dim_sent_bytes_total`</td>
            <td scope="row" data-label="New">`surrealdb_network_sent_bytes_total`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`http_server_request_duration_milliseconds`</td>
            <td scope="row" data-label="New">`surrealdb_http_request_duration_seconds`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`http_server_request_count_total`</td>
            <td scope="row" data-label="New">`surrealdb_http_request_total`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`http_server_active_requests`</td>
            <td scope="row" data-label="New">`surrealdb_http_active_requests`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`rpc_server_request_duration_milliseconds`</td>
            <td scope="row" data-label="New">`surrealdb_rpc_duration_seconds`</td>
        </tr>
        <tr>
            <td scope="row" data-label="Old">`rpc_server_active_connections`</td>
            <td scope="row" data-label="New">`surrealdb_session_active{protocol="websocket"}`</td>
        </tr>
    </tbody>
</table>

The `otel_scope_name` label also changes shape in 3.1: scopes are now signal-domain (`surrealdb.statement`, `surrealdb.query`, …) rather than edition-tier (`surrealdb.community`, `surrealdb.enterprise`). Dashboards that filtered by scope should switch to the metric name (which now carries the same information, since scopes mirror the family prefix) or to the `service.edition` resource attribute, which is the authoritative edition signal.
