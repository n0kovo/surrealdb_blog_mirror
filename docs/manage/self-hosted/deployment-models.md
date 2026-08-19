---
position: 2
title: Deployment models
description: Deployment models for SurrealDB — managed instances, single-node RocksDB, multi-node clusters, and embedded runtimes — and how to choose between them.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/self-hosted/deployment-models.mdx"
---

# Deployment models

SurrealDB separates the query engine (compute) from the underlying storage layer. The same SurrealQL, APIs, and client SDKs work across embedded devices, single-node servers, distributed clusters, and [managed instances](../instances/index.md) — so you can change how the database runs without rewriting application code.

This page explains the available deployment options, storage engines, and how to choose the right architecture for your workload. For how the compute and storage layers interact, see [Architecture](../../architecture.md).

## Deployment models summary

| Deployment model | Storage engine(s) | Scaling | High availability | Versioning (`VERSION`) | Best for | Managed option |
| --- | --- | --- | --- | --- | --- | --- |
| Managed | Start (single-node) to Scale (multi-node cluster) | Vertical and horizontal (by plan) | Fully managed HA on Scale | Where enabled | Production without operating infrastructure | Yes |
| Single node | RocksDB (recommended for server workloads); SurrealKV (beta) | Vertical | Filesystem backups | Where enabled (see engine docs) | Development and single-node production | Self-hosted (Community Edition) |
| Multi-node | Distributed transactional storage | Horizontal; distributed storage | High (replication and consensus) | Where enabled on the storage tier | Large-scale production workloads | [Scale](https://surrealdb.com/pricing/scale) plan; self-hosted Enterprise |
| Embedded | SurrealMX (memory), SurrealKV (beta), RocksDB, IndexedDB (browser) | Application-bound | Application-bound | Where enabled | Offline, edge, browser, and low-latency local apps | No |

## Architecture overview

SurrealDB consists of two major layers:

**Query layer**

- Parses and executes SurrealQL
- Authenticates connections and sessions
- Enforces table- and field-level permissions on reads and writes
- Plans index-backed queries, maintains index entries during writes, and coordinates transactions

**Storage layer**

- Handles persistence and durability
- Determines scalability, temporal versioning, replication, and fault tolerance

Because these layers are separated in the architecture, applications can move between deployment models without changing application code or queries. Embedded and browser deployments still use both layers, but they run in-process rather than as separate services.

## Managed instances

[Managed instances](../instances/index.md) provide a fully managed deployment platform built on scalable, fault-tolerant infrastructure. They remove the operational complexity of running clusters while providing production-ready deployments.

Plans range from **Start** (single-node, vertically scalable instances) to **Scale** (multi-node clusters on distributed storage, minimum three compute units). Start is enough for many workloads; Scale is aimed at business-critical production where a single-node outage would stop the application and where operating HA yourself (Kubernetes, replication, patching, and backups) would otherwise consume platform team time. See [Architecture](../instances/architecture.md) and [Pricing](https://surrealdb.com/pricing).

### Features

- Managed SurrealDB infrastructure
- Vertical and horizontal scaling without rebuilding the cluster
- High availability
- Managed backups
- Secure connectivity
- Multi-node distributed architecture on the Scale plan
- Production monitoring and operations

### Best for

- Managed infrastructure
- Rapid production deployment
- Scaling applications
- SaaS platforms
- Enterprise workloads

### Benefits compared to self-hosting

| Feature | Self-hosted | Managed |
| --- | --- | --- |
| Infrastructure management | Required | Managed |
| Backups | Manual | Managed |
| Scaling | Manual | Managed resize, no cluster rebuild |
| HA setup | Manual | Built-in |
| Upgrades | Manual | Managed |
| Cluster operations | Manual | Managed |

## Single-node (RocksDB)

Single-node deployments run SurrealDB as a standalone server process using [RocksDB](https://rocksdb.org/). This is the simplest and most widely used production architecture on disk. RocksDB is a high-performance LSM-tree key-value store optimised for high write throughput, SSD storage, and predictable persistence.

**Best for**

- Small to medium production workloads
- Internal tooling
- Development environments
- Applications without horizontal scaling or built-in cluster fault tolerance

### Limitations

- Vertical scaling only
- No built-in distributed fault tolerance

For setup examples, see [Run a single-node, on-disk server](../../running/file-backed.md).

### Common deployment methods

**CLI**

```bash
surreal start rocksdb://path/to/database
```

**Docker**

```bash
docker run --rm \
  -p 8000:8000 \
  surrealdb/surrealdb:latest \
  start --user root --pass secret rocksdb://data/database.db
```

See also [Self-hosted](index.md) for Docker, Kubernetes, and platform guides.

### SurrealKV (beta)

For single-node and embedded workloads, [SurrealKV](https://github.com/surrealdb/surrealkv) is SurrealDB’s own LSM-backed storage engine, developed in concert with the database rather than as a third-party dependency. That co-development shows up in day-to-day operation: SurrealKV exposes a comparatively small [configuration surface](../../reference/cli/surrealdb-cli/commands/start.md#supported-parameters-for-surrealkv) and [environment variable set](../../reference/cli/surrealdb-cli/environment-variables.md#surrealkv-environment-variables) next to RocksDB’s extensive tuning knobs, and is aimed at embedded and local-first scenarios.

SurrealKV remains **beta**. For conservative production on-disk server deployments today, **prefer RocksDB**. For embedded deployments where smaller resident memory and in-process behaviour are priorities, SurrealKV is the path to evaluate first. It is nonetheless a serious storage path inside the project: features such as temporal reads via the [`VERSION`](../../reference/query-language/statements/select.md#the-version-clause) clause were exercised on SurrealKV first and have since been extended to [SurrealMX](../../running/in-memory.md) and RocksDB where the engine supports them.

To try SurrealKV on a server, see the SurrealKV tab on [Run a single-node, on-disk server](../../running/file-backed.md) and the [`surreal start`](../../reference/cli/surrealdb-cli/commands/start.md) storage parameters.

## Multi-node clusters

For high availability and horizontal scalability, SurrealDB supports distributed deployments backed by a distributed transactional storage layer built for large-scale clusters.

### Architecture

In distributed deployments:

- Multiple query nodes scale horizontally against shared storage
- The storage layer manages replication, consensus, fault tolerance, and distributed transactions
- Object-storage backing (rolling out on Scale) places transactional data in commodity object storage while frequently accessed data stays on local disk

This architecture enables zero-downtime scaling, resilient clusters, high-throughput workloads, geographically distributed applications, and (as Scale features roll out) database branching, instant replication and recovery, and lower storage costs at scale.

For managed multi-node clusters, use the [Scale](https://surrealdb.com/pricing/scale) plan on a [managed instance](../instances/index.md). For self-hosted multi-node clusters on Kubernetes, use [SurrealDB Enterprise](https://surrealdb.com/enterprise); the [Managed Kubernetes](managed-kubernetes.md) page summarises options per cloud. For a local Community playground against open-source distributed storage (TiKV), see [Run a multi-node cluster](../../running/multi-node.md) — that path is not the storage engine behind Scale or Enterprise clusters.

### Features

**Horizontal scalability** — Scale query and storage nodes independently.

**Fault tolerance** — Replication and consensus allow clusters to tolerate node failures.

**Distributed ACID transactions** — Strong transactional guarantees across distributed infrastructure.

**Large-scale storage** — Designed for very large datasets and high-concurrency production workloads.

### Best for

- Enterprise deployments
- High-availability applications
- Multi-region systems
- Large graph workloads
- Real-time platforms
- AI-native distributed systems

### Operational considerations

Distributed deployments add cluster orchestration, node management, monitoring, and replication management. Teams that want distributed scalability without operating that stack should consider [managed instances](../instances/index.md).

## Embedded deployments

Embedded deployments run SurrealDB inside your application process without a separate database server. The query and storage layers share the process (and, in the browser, the same runtime), which removes network latency between your app and the database. This model suits edge computing, mobile and desktop software, offline-first apps, browser PWAs, and AI workflows that need minimal latency.

For language-specific setup, see [Embedding SurrealDB](../../build/embedding/index.md) and [Storage engines](../../build/embedding/storage-engines.md).

### Supported runtimes

SurrealDB supports embedded operation in Rust, Go, JavaScript / TypeScript, WebAssembly, Python, and .NET. Capabilities vary by SDK and storage backend — check the embedding guide for your language.

### Storage options

**In-memory (SurrealMX)** — Default in-memory backend since SurrealDB 3.0, with optional snapshots or append-only persistence and support for versioned queries. See [Run a single-node, in-memory server](../../running/in-memory.md).

**RocksDB** — Persistent on-disk storage with mature tuning for write-heavy, SSD-backed server workloads. See [File-backed storage](../../running/file-backed.md).

**SurrealKV** — Same beta engine as single-node server deployments; aimed at embedded and local-first in-process workloads where smaller resident memory and simple operational behaviour matter most.

**IndexedDB (browser)** — Browser-native persistence with binary serialisation for PWAs and local-first web apps. See [Embedding SurrealDB](../../build/embedding/index.md) and the [Wasm engine](../../reference/javascript/engines/wasm.md).

## Choosing the right deployment model

**Use a managed instance when**

- You want managed infrastructure instead of operating clusters yourself
- You need production-ready HA quickly — especially on the **Scale** plan for multi-node fault tolerance
- Your team prefers building applications over provisioning servers, Kubernetes, replication, and upgrade runbooks

**Use single-node deployments with RocksDB when**

- Simplicity matters most
- Scaling requirements are moderate
- You run small-to-medium production workloads without cluster-level fault tolerance

**Use multi-node deployments when**

- High availability is required
- Workloads need horizontal scaling
- Infrastructure spans multiple nodes or availability zones

For managed clusters, use the [Scale](https://surrealdb.com/pricing/scale) plan. For self-hosted clusters, see [SurrealDB Enterprise](https://surrealdb.com/enterprise) and [Managed Kubernetes](managed-kubernetes.md).

**Use embedded deployments when**

- You run on edge devices or in the browser
- Offline operation is required
- Minimising latency between app and database is critical

## Conclusion

SurrealDB’s architecture lets the same engine and query language run across embedded, single-node, distributed, and managed models. Whether you embed SurrealDB in a browser, run RocksDB on one server, scale horizontally across a multi-node cluster, or use a managed Start or Scale instance, you can match operational and scalability requirements without rewriting queries.

## Next steps

- **[Managed instances](../instances/index.md)** — Provision a managed SurrealDB instance with built-in monitoring, network access controls and operations tooling.
- **[Self-hosted](index.md)** — Run SurrealDB on Docker, Kubernetes (AKS, EKS, GKE) or as a standalone binary with full control over storage and configuration.
- **[Observability](../observability/index.md)** — Metrics, OTLP and Prometheus access, audit logs and slow-query logs for both Community and Enterprise editions.
