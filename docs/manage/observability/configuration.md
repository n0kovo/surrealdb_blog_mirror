---
position: 6
title: Configuration reference
description: Every observability, audit log and slow-query log environment variable, plus recommended configurations for local, production and multi-tenant deployments.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/observability/configuration.mdx"
---

# Configuration reference

Every environment variable that controls the observability surface. Variables marked <Edition value="enterprise" /> exist only when the Enterprise binary is running; everything else is available in all editions.

*Since v3.1.0*

The audit log, slow-query log and SurrealDS configuration surfaces are new in SurrealDB 3.1.

## How to read this page

- **Default** is the value used when the variable is unset. Cells marked `—` are required when the surrounding feature is enabled.
- **Edition** identifies which builds register the variable. Variables marked <Edition value="enterprise" /> are no-ops on a Community binary.
- All variables can be set via environment, a `.env` file loaded by the deployment, or the orchestrator's secret store.

## Core knobs

These knobs control the two access paths (Prometheus pull and OTLP push) and the global telemetry switches. They are available in every edition.

<table>
    <thead>
        <tr>
            <th scope="col">Variable</th>
            <th scope="col">Default</th>
            <th scope="col">Edition</th>
            <th scope="col">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_METRICS_ENABLED`</td>
            <td scope="row" data-label="Default">`true`</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">Mount the `/metrics` endpoint. When `false` the route returns `404`.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_TELEMETRY_PROVIDER`</td>
            <td scope="row" data-label="Default">unset</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">Set to `otlp` to enable the OTLP push pipeline (metrics, logs and traces). Any other value leaves OTLP off.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_TELEMETRY_DISABLE_METRICS`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">Skip the OTLP metrics reader specifically, leaving logs and traces unaffected.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_TELEMETRY_DISABLE_TRACING`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">Skip the OTLP trace exporter specifically, leaving metrics and logs unaffected.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_METRIC_THRESHOLD_MS`</td>
            <td scope="row" data-label="Default">`1000`</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">Threshold above which a completed statement is counted on `surrealdb_slow_query_total`. Set to `0` to disable the counter.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_PROCESS_METRICS_REFRESH_INTERVAL`</td>
            <td scope="row" data-label="Default">`5`</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">Cadence in seconds for refreshing the cached process snapshot that backs `surrealdb_process_memory_bytes` and `surrealdb_process_cpu_percent`. Floored at 1.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`OTEL_EXPORTER_OTLP_ENDPOINT`</td>
            <td scope="row" data-label="Default">`http://localhost:4317`</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">OTLP gRPC endpoint. Standard OpenTelemetry variable.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`OTEL_METRIC_EXPORT_INTERVAL`</td>
            <td scope="row" data-label="Default">`60000` (ms)</td>
            <td scope="row" data-label="Edition"><Edition value="community" /></td>
            <td scope="row" data-label="Purpose">OTLP push cadence. Standard OpenTelemetry variable.</td>
        </tr>
    </tbody>
</table>

## Audit log knobs

<Edition value="enterprise" />

Controls the [Enterprise audit log pipeline](audit-logging.md). Setting `SURREAL_AUDIT_SINK=none` (the default) leaves the pipeline disabled entirely; no observer is registered and the cost is zero.

<table>
    <thead>
        <tr>
            <th scope="col">Variable</th>
            <th scope="col">Default</th>
            <th scope="col">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_SINK`</td>
            <td scope="row" data-label="Default">`none`</td>
            <td scope="row" data-label="Purpose">One of `none`, `file`. `syslog` and `table` are reserved but rejected at startup.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_FILE_PATH`</td>
            <td scope="row" data-label="Default">—</td>
            <td scope="row" data-label="Purpose">Required when `SURREAL_AUDIT_SINK=file`. Parent directory must exist; startup fails loudly if it doesn't. File is opened with mode `0600` on Unix.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_FILE_ROTATE_BYTES`</td>
            <td scope="row" data-label="Default">`268435456` (256 MiB)</td>
            <td scope="row" data-label="Purpose">Size threshold that triggers rotation.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_FILE_ROTATE_KEEP`</td>
            <td scope="row" data-label="Default">`8`</td>
            <td scope="row" data-label="Purpose">Number of rotated files to retain.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_FSYNC_EVERY`</td>
            <td scope="row" data-label="Default">`0`</td>
            <td scope="row" data-label="Purpose">Mid-stream fsync cadence. `0` never fsyncs mid-stream; `1` fsyncs every record; `N&gt;1` fsyncs every Nth record. Rotation and graceful shutdown always fsync regardless.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_HASH_CHAIN`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Purpose">Adds `prev_hash` / `hash` SHA-256 fields to every record for tamper-evidence. <strong>Requires `SURREAL_AUDIT_FSYNC_EVERY=1`</strong> — startup fails otherwise.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_INCLUDE_SQL`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Purpose">Include the full SQL text on `statement` records. Off by default; the identity and action context is still emitted.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_QUEUE_CAPACITY`</td>
            <td scope="row" data-label="Default">`4096`</td>
            <td scope="row" data-label="Purpose">Records the bounded observer-to-worker queue can hold.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_OVERFLOW`</td>
            <td scope="row" data-label="Default">`block`</td>
            <td scope="row" data-label="Purpose">`drop` (single non-blocking `try_send`) or `block` (bounded busy-yield retry). See <a href="/docs/manage/observability/audit-logging#overflow-semantics">overflow semantics</a>. Neither offers a lossless guarantee.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_REDACT_TABLES`</td>
            <td scope="row" data-label="Default">—</td>
            <td scope="row" data-label="Purpose">Comma-separated identifier tokens replaced with `***` in captured SQL.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_REDACT_REGEX`</td>
            <td scope="row" data-label="Default">—</td>
            <td scope="row" data-label="Purpose"><strong>Semicolon-separated</strong> regex patterns applied to captured SQL. Each pattern is compiled at startup; an invalid pattern fails startup.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_REDACT_LITERALS`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Purpose">Replace every quoted literal with `***`. Off by default.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_AUDIT_OTEL_EXPORT`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Purpose">Also emit each audit record as an OTel `LogRecord`. Off by default so compliance-sensitive records stay on the local file sink.</td>
        </tr>
    </tbody>
</table>

## Slow-query log knobs

<Edition value="enterprise" />

Controls the [Enterprise slow-query log pipeline](slow-query-logging.md). Setting `SURREAL_SLOW_QUERY_SINK=none` (the default) leaves the pipeline disabled entirely.

<table>
    <thead>
        <tr>
            <th scope="col">Variable</th>
            <th scope="col">Default</th>
            <th scope="col">Purpose</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_SINK`</td>
            <td scope="row" data-label="Default">`none`</td>
            <td scope="row" data-label="Purpose">Same selector set as `SURREAL_AUDIT_SINK`.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_FILE_PATH`</td>
            <td scope="row" data-label="Default">—</td>
            <td scope="row" data-label="Purpose">Required when the sink is `file`.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_FILE_ROTATE_BYTES`</td>
            <td scope="row" data-label="Default">`268435456` (256 MiB)</td>
            <td scope="row" data-label="Purpose">Rotation threshold.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_FILE_ROTATE_KEEP`</td>
            <td scope="row" data-label="Default">`8`</td>
            <td scope="row" data-label="Purpose">Retained rotation generations.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_FSYNC_EVERY`</td>
            <td scope="row" data-label="Default">`0`</td>
            <td scope="row" data-label="Purpose">Same semantics as the audit equivalent.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_HASH_CHAIN`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Purpose">Tamper-evident chain. Requires `SURREAL_SLOW_QUERY_FSYNC_EVERY=1`.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_THRESHOLD_MS`</td>
            <td scope="row" data-label="Default">—</td>
            <td scope="row" data-label="Purpose">Duration threshold above which a statement is captured. Required when the sink is enabled.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_INCLUDE_SQL`</td>
            <td scope="row" data-label="Default">`true`</td>
            <td scope="row" data-label="Purpose">Capture SQL text in slow-query records. Setting to `false` lets throughput-sensitive deployments skip per-statement `to_sql()` rendering at the cost of losing SQL context on captures.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_QUEUE_CAPACITY`</td>
            <td scope="row" data-label="Default">`4096`</td>
            <td scope="row" data-label="Purpose">Records the queue can hold.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_OVERFLOW`</td>
            <td scope="row" data-label="Default">`drop`</td>
            <td scope="row" data-label="Purpose"><strong>Default differs from audit</strong> — slow-query records are triage data, so dropping is preferred over busy-yielding the executor.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_REDACT_TABLES`</td>
            <td scope="row" data-label="Default">—</td>
            <td scope="row" data-label="Purpose">Same syntax as the audit equivalent.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_REDACT_REGEX`</td>
            <td scope="row" data-label="Default">—</td>
            <td scope="row" data-label="Purpose">Same syntax as the audit equivalent.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_REDACT_LITERALS`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Purpose">Same semantics as the audit equivalent.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_SLOW_QUERY_OTEL_EXPORT`</td>
            <td scope="row" data-label="Default">`false`</td>
            <td scope="row" data-label="Purpose">Emit each slow-query record as an OTel `LogRecord` at `WARN` severity.</td>
        </tr>
    </tbody>
</table>

## SurrealDS networking

<Edition value="enterprise" />

> [!NOTE]
> **SurrealDS** is SurrealDB's distributed storage engine for highly available, horizontally scalable clusters. The `SURREAL_DS_*` variables below apply when that runtime is deployed — on [SurrealDB Cloud Scale](https://surrealdb.com/pricing/scale) or in self-hosted Enterprise installations.

A short list of the SurrealDS networking and consensus knobs that operators routinely tune in response to a metric signal. For a product overview, see [SurrealDS](https://surrealdb.com/platform/surrealds). The complete `SURREAL_DS_*` reference is part of the Enterprise Kubernetes deployment guide.

<table>
    <thead>
        <tr>
            <th scope="col">Variable</th>
            <th scope="col">Default</th>
            <th scope="col">Tune in response to</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_DS_NTW_INBOUND_BYTES`</td>
            <td scope="row" data-label="Default">`3 * MAX_MSG_BYTES` (768 MiB) per `MessageClass`</td>
            <td scope="row" data-label="Trigger">`QUIC inbound bytes ... saturation warning` log.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_DS_NTW_INFLIGHT_PROCESSING_CAP`</td>
            <td scope="row" data-label="Default">`max(384, num_cpus*32)`</td>
            <td scope="row" data-label="Trigger">`QUIC inbound handlers ... saturation warning` log.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_DS_MAX_READ_OPERATIONS`</td>
            <td scope="row" data-label="Default">`192`</td>
            <td scope="row" data-label="Trigger">Steady-state RSS pressure or scan-heavy workloads.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_DS_MAX_WRITE_OPERATIONS`</td>
            <td scope="row" data-label="Default">`96`</td>
            <td scope="row" data-label="Trigger">`Write operations limit saturation warning` log.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_DS_CONSENSUS_FAST_QUORUM_TIMEOUT_MS`</td>
            <td scope="row" data-label="Default">implementation default</td>
            <td scope="row" data-label="Trigger">Rising `surrealdb_ds_consensus_fast_quorum_timeouts_total`.</td>
        </tr>
        <tr>
            <td scope="row" data-label="Variable">`SURREAL_DS_RETRY_BASE_MS` / `SURREAL_DS_RETRY_MAX_MS`</td>
            <td scope="row" data-label="Default">`500` / `5000`</td>
            <td scope="row" data-label="Trigger">Rising `surrealdb_ds_finalize_prepare_retries_total`.</td>
        </tr>
    </tbody>
</table>

## Recommended configurations

**Local development**

The minimum needed to scrape metrics from a local server during development:

```bash
surreal start --user root --pass root memory
# Anonymous: only the public allowlist
curl http://127.0.0.1:8000/metrics
# Authenticated: the full surface
curl -u root:root http://127.0.0.1:8000/metrics
```

To push to a local OpenTelemetry collector (for example a Grafana / Tempo / Loki / Prometheus docker-compose stack):

```bash
SURREAL_TELEMETRY_PROVIDER=otlp \
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317 \
surreal start --user root --pass root memory
```

To disable the endpoint entirely (useful when running with a third-party agent that scrapes via OTLP only):

```bash
SURREAL_METRICS_ENABLED=false surreal start ...
# /metrics → 404
```

**Self-hosted production**

For a self-hosted production deployment that ships metrics over OTLP and writes audit and slow-query records to a local sink for SIEM ingestion:

```bash
# Telemetry
SURREAL_METRICS_ENABLED=true
SURREAL_TELEMETRY_PROVIDER=otlp
OTEL_EXPORTER_OTLP_ENDPOINT=https://collector.internal:4317
OTEL_METRIC_EXPORT_INTERVAL=30000

# Audit log (Enterprise) — durable, hash-chained
SURREAL_AUDIT_SINK=file
SURREAL_AUDIT_FILE_PATH=/var/log/surrealdb/audit.log
SURREAL_AUDIT_FSYNC_EVERY=1
SURREAL_AUDIT_HASH_CHAIN=true
SURREAL_AUDIT_INCLUDE_SQL=true
SURREAL_AUDIT_REDACT_LITERALS=true
SURREAL_AUDIT_OVERFLOW=block

# Slow-query log (Enterprise) — best-effort triage data
SURREAL_SLOW_QUERY_SINK=file
SURREAL_SLOW_QUERY_FILE_PATH=/var/log/surrealdb/slow-query.log
SURREAL_SLOW_QUERY_THRESHOLD_MS=250
```

Pair this with the alert hints in the [metrics reference](metrics.md#alert-hints) and the alerting rules on `surrealdb_audit_dropped`, `surrealdb_audit_append_errors` and `surrealdb_audit_queue_depth` listed in the [Compliance checklist](#compliance-checklist) below.

**Multi-tenant / cloud-facing**

For pods that serve customer traffic directly, the default posture is **deny scraping at the pod boundary** and serve metrics from an internal sidecar instead. Customer-visible metrics should be filtered at a proxy.

```bash
# Customer-facing pod
SURREAL_METRICS_ENABLED=false

# Internal sidecar pod (same workload, internal-only interface)
SURREAL_METRICS_ENABLED=true
SURREAL_TELEMETRY_PROVIDER=otlp
OTEL_EXPORTER_OTLP_ENDPOINT=https://collector.internal:4317
```

Filter on `namespace` and `database` at the proxy and strip the `user` label before exposing to a customer. See the [Recommended cloud whitelist](metrics.md#recommended-cloud-whitelist) for the suggested customer-visible subset.

## Compliance checklist

<Edition value="enterprise" />

For deployments that require tamper-evident, durable audit trails the recommended configuration is:

```bash
SURREAL_AUDIT_SINK=file
SURREAL_AUDIT_FILE_PATH=/var/log/surrealdb/audit.log
SURREAL_AUDIT_FSYNC_EVERY=1            # required for hash chain
SURREAL_AUDIT_HASH_CHAIN=true
SURREAL_AUDIT_INCLUDE_SQL=true         # if a regulator requires statement text
SURREAL_AUDIT_REDACT_LITERALS=true     # scrub embedded PII from quoted values
SURREAL_AUDIT_OVERFLOW=block           # already the default; explicit for clarity
```

Plus alerts on:

- `surrealdb_audit_dropped` — any non-zero rate is a lost record.
- `surrealdb_audit_append_errors` — any non-zero rate is a lost record.
- `surrealdb_audit_queue_depth` sustained above ~50% of `SURREAL_AUDIT_QUEUE_CAPACITY` — the sink is falling behind.

For the full pipeline details (record shape, rotation, hash chain, redaction) see the [Audit logging](audit-logging.md) reference.

## Troubleshooting

| Symptom | Likely cause | Investigation |
| --- | --- | --- |
| `/metrics` returns `404` | `SURREAL_METRICS_ENABLED=false` | Re-enable, or scrape over OTLP instead. |
| `/metrics` returns only six metrics | Anonymous scrape against the public allowlist | Configure basic-auth with root credentials. |
| No `surrealdb_ds_*` metrics on a single-node setup | Enterprise composer did not start a metrics reader | Confirm the Enterprise binary is running and at least one of `SURREAL_METRICS_ENABLED=true` / `SURREAL_TELEMETRY_PROVIDER=otlp` is set. |
| `surrealdb_audit_records` missing entirely | Audit sink set to `none` (the default) | Set `SURREAL_AUDIT_SINK=file` and `SURREAL_AUDIT_FILE_PATH`. |
| Sustained `surrealdb_audit_dropped` rate | Worker can't keep up | Raise `SURREAL_AUDIT_QUEUE_CAPACITY`; check sink disk I/O; consider switching from `block` to `drop` if drops are acceptable. |
| `QUIC inbound bytes ... saturation warning` log | Per-class inbound budget saturated | Raise `SURREAL_DS_NTW_INBOUND_BYTES`. |
| OTLP collector not receiving metrics | `SURREAL_TELEMETRY_PROVIDER` unset, or `SURREAL_TELEMETRY_DISABLE_METRICS=true` | Confirm both, plus that `OTEL_EXPORTER_OTLP_ENDPOINT` is reachable. |
| Hash chain rejected at startup | `SURREAL_AUDIT_HASH_CHAIN=true` without `SURREAL_AUDIT_FSYNC_EVERY=1` | Set both, or disable hash chaining. |
