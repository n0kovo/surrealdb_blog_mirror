---
position: 0
title: Observability
description: Logging, Prometheus pull, OTLP push, Enterprise pipelines, metric catalogues, and Tokio console — production visibility for SurrealDB Community and Enterprise.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/observability/index.mdx"
---

# Observability

SurrealDB exposes **logging**, **metrics**, **traces**, and (with **SurrealDB Enterprise**) durable **audit** and **slow-query** record pipelines through one OpenTelemetry-oriented surface. Signals can leave the process in two complementary ways:

- **Pull** — scrapers call `GET /metrics` (Prometheus text exposition).
- **Push** — the server exports metrics, logs, and traces over **OTLP** to a collector when `SURREAL_TELEMETRY_PROVIDER=otlp`.

Both paths can run together or independently; each is controlled with environment variables documented on the [configuration reference](configuration.md).

**Suggested reading order**

1. [Logging](logging.md) — stderr, JSON, files, sockets, and line-based slow-query logging (no metrics stack required).
2. [Observability (metrics and Prometheus)](observability.md) — `GET /metrics`, naming, migration from pre-3.1 series, the public allowlist, and behaviour common to **Community and Enterprise**.
3. [Telemetry (OTLP)](telemetry.md) — push export, intervals, and backward-compatible instruments on the wire.
4. [Enterprise observability](enterprise-observability.md) — SurrealDS cluster metrics, audit and slow-query file pipelines, pipeline self-metrics, and OTLP log export opt-ins.
5. [Metrics reference](metrics.md) — full catalogue, labels, alert hints, and the 3.0 → 3.1 migration table.
6. [Configuration](configuration.md) — every telemetry, audit, and slow-query environment variable.
7. [Audit logging](audit-logging.md) and [Slow-query logging](slow-query-logging.md) — Enterprise pipeline references.
8. [Tokio console](tokio-console.md) — optional async-runtime debugging alongside metrics and traces.

**Pull** means scrapers call your server. **Push** means the server opens an export connection to a collector. From SurrealDB 3.1 onward, both paths share the same instruments. Canonical prose also ships in-tree: [`doc/OBSERVABILITY.md`](https://github.com/surrealdb/surrealdb/blob/main/doc/OBSERVABILITY.md) and [`doc/TELEMETRY.md`](https://github.com/surrealdb/surrealdb/blob/main/doc/TELEMETRY.md); the Enterprise distribution extends `doc/OBSERVABILITY.md` with **[C]** / **[E]** catalogue markers.

*Since v3.1.0*

The `surrealdb.*` metric namespace, the `PUBLIC_METRICS` allowlist, the audit-log pipeline, and the slow-query log pipeline are new in SurrealDB 3.1. Operators upgrading from 3.0 should read the [Migration from 3.0](metrics.md#migration-from-30) section in the metrics reference.

## Editions at a glance

The Community server publishes the full set of primary signal families. The Enterprise composer adds the SurrealDS cluster metrics, the audit and slow-query log pipelines (with their own self-metrics), and the reserved per-tenant rollup scope.

<table>
    <thead>
        <tr>
            <th scope="col">Capability</th>
            <th scope="col">Community</th>
            <th scope="col">Enterprise</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td scope="row" data-label="Capability">Prometheus `/metrics` endpoint</td>
            <td scope="row" data-label="Community"><Edition value="community" /></td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">OTLP push (metrics, logs, traces)</td>
            <td scope="row" data-label="Community"><Edition value="community" /></td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">Primary signal families (statement, query, transaction, RPC, auth, session, network, HTTP, live query, slow-query counter, GraphQL, MCP, storage)</td>
            <td scope="row" data-label="Community"><Edition value="community" /></td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">Public metrics allowlist for anonymous scrapers</td>
            <td scope="row" data-label="Community"><Edition value="community" /></td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">SurrealDS cluster metrics (`surrealdb.ds.*`)</td>
            <td scope="row" data-label="Community">—</td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /> (when DS runtime is deployed)</td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">Audit log records (file sink + optional OTel logs)</td>
            <td scope="row" data-label="Community">—</td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">Slow-query log records (file sink + optional OTel logs)</td>
            <td scope="row" data-label="Community">—</td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">Hash-chained, tamper-evident records</td>
            <td scope="row" data-label="Community">—</td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">Three-pass redaction (literal, identifier, regex)</td>
            <td scope="row" data-label="Community">—</td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
        <tr>
            <td scope="row" data-label="Capability">Per-tenant rollup scope (`surrealdb.tenant`) <em>(reserved)</em></td>
            <td scope="row" data-label="Community">—</td>
            <td scope="row" data-label="Enterprise"><Edition value="enterprise" /></td>
        </tr>
    </tbody>
</table>

Edition is also carried on the OTel `Resource` via the `service.edition` attribute (`community` or `enterprise`), so dashboards can group or filter on it without hard-coding metric scopes.

## Quickstart

**Prometheus pull**

The `/metrics` endpoint is mounted by default. Anonymous scrapers receive only the six metrics on the [public allowlist](metrics.md#public-metrics-allowlist); root credentials unlock the full surface.

```bash
# Start the server (Community example)
surreal start --user root --pass root memory

# Anonymous scrape — public allowlist only
curl http://127.0.0.1:8000/metrics

# Operator scrape — full surface, including labelled families
curl -u root:root http://127.0.0.1:8000/metrics
```

To turn the endpoint off entirely:

```bash
SURREAL_METRICS_ENABLED=false surreal start ...
# /metrics now returns 404
```

**OTLP push**

OTLP push targets any OpenTelemetry collector. SurrealDB exports metrics, logs (including audit and slow-query records when opted in) and traces over gRPC, using native-TLS roots when the endpoint is HTTPS.

```bash
SURREAL_TELEMETRY_PROVIDER=otlp \
OTEL_EXPORTER_OTLP_ENDPOINT="http://my-collector.monitoring.svc.cluster.local:4317" \
surreal start ...
```

To selectively disable parts of the OTLP pipeline:

```bash
SURREAL_TELEMETRY_DISABLE_METRICS=true   # OTLP metrics off; logs + traces still push
SURREAL_TELEMETRY_DISABLE_TRACING=true   # OTLP traces off; metrics + logs still push
```

Audit and slow-query records flow over OTLP **only when explicitly opted in** per pipeline via `SURREAL_AUDIT_OTEL_EXPORT=true` / `SURREAL_SLOW_QUERY_OTEL_EXPORT=true`. The local file sink remains the primary path for compliance ingestion.

## What is new in 3.1

*Since v3.1.0*

- A reworked metric namespace — every instrument is now `surrealdb.*`, grouped by signal family (statement, query, transaction, RPC, …). Names from 3.0 are mapped in the [migration table](metrics.md#migration-from-30).
- **Dual access paths.** Prometheus pull on `/metrics` and OTLP push run side-by-side. Both pipelines can be toggled independently.
- **Public metrics allowlist (`PUBLIC_METRICS`).** Six low-sensitivity gauges are safe to expose anonymously; the rest require root credentials.
- **Audit log pipeline.** <Edition value="enterprise" /> Durable NDJSON file sink with size-based rotation, tunable fsync cadence, optional hash chaining for tamper-evidence, and three-pass redaction.
- **Slow-query log pipeline.** <Edition value="enterprise" /> Mirrors the audit pipeline, with a configurable duration threshold and the slow-query counter metric.
- **SurrealDS cluster metrics.** <Edition value="enterprise" /> Around thirty instruments covering network, consensus, view changes, recovery and garbage collection when SurrealDS is deployed (SurrealDB Cloud Scale or self-hosted Enterprise).
- **OpenTelemetry alignment.** Standard semantic-convention attribute keys (`http.request.method`, `http.route`, `http.response.status_code`, `db.namespace`, `db.user`) replace ad-hoc keys.

## Where to go next

- **[Logging](logging.md)** — Log level, text or JSON format, files, sockets, and line-based slow-query logging.
- **[Metrics and Prometheus](observability.md)** — Pull scraping, naming, multi-tenant guidance, and version-specific tabs before and after 3.1.
- **[Telemetry (OTLP)](telemetry.md)** — Push export, intervals, process gauges, and legacy instruments on the wire.
- **[Enterprise observability](enterprise-observability.md)** — SurrealDS metrics, audit and slow-query pipelines, and OTLP log export opt-ins.
- **[Metrics reference](metrics.md)** — Access paths, label catalogue, every metric grouped by signal family, and the 3.0 → 3.1 migration table.
- **[Configuration reference](configuration.md)** — All telemetry, audit log and slow-query log environment variables, plus recommended configurations for local, production and multi-tenant deployments.
- **[Audit logging](audit-logging.md)** — Enterprise audit log pipeline: events captured, record shape, rotation, hash chaining and redaction.
- **[Slow-query logging](slow-query-logging.md)** — Enterprise slow-query log pipeline: how a query qualifies, record shape and pipeline self-metrics.
- **[Tokio console](tokio-console.md)** — Optional Tokio runtime debugging — tasks, poll times, and scheduling alongside metrics and traces.
- **[Cloud monitoring](../../build/deployment/surrealdb-cloud/operations/monitoring-overview.md)** — The built-in monitoring dashboard, log retention and metrics views for SurrealDB Cloud instances.
- **[Self-hosted monitoring](../self-hosted/monitoring-and-observability.md)** — Pairing the `/health` endpoint, Prometheus and Grafana with the observability surface for a self-hosted deployment.

## Structured logs versus audit and slow-query records

Server **structured logs** (levels, format, files, sockets, and the `--slow-log-*` line-based slow-query helpers) are configured on [`surreal start`](../../reference/cli/surrealdb-cli/commands/start.md) and in the [environment variables](../../reference/cli/surrealdb-cli/environment-variables.md) catalogue — see [Logging](logging.md). That stream is separate from the **Enterprise audit** and **slow-query** NDJSON pipelines, which have their own sinks and optional OTel log export — see [Audit logging](audit-logging.md) and [Slow-query logging](slow-query-logging.md).

For async runtime introspection (tasks, poll histograms), use the [Tokio console](tokio-console.md) on trusted hosts only; it complements OTLP and `/metrics`, it does not replace them.
