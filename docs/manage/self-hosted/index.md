---
position: 1
title: Self-hosted
description: SurrealDB deployment models on your own infrastructure. Containers, configuration, backups, monitoring, and upgrades.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/self-hosted/index.mdx"
---

# Self-hosted

Running SurrealDB yourself is quick to start and gives you full control over storage, configuration, and placement. Everything needed to start a server and to import and export data is in the [command-line tool](../../reference/cli/db/index.md), packaged and distributed as a single executable that can be downloaded, installed, or run from within Docker.

For initial installation, see the [installation guide](../../running/installation/index.md). If you would rather not operate the infrastructure, see [Instances](../instances/index.md) for the managed option.

## Deployment guides

| Guide | Typical use |
| --- | --- |
| [Deployment models](deployment-models.md) | Choosing between single-node, multi-node, embedded, and managed |
| [Docker](../../running/docker.md) | Quickest path; SurrealKV with a volume mount |
| [Kubernetes](kubernetes.md) | Single SurrealDB pod with SurrealKV on a persistent volume |
| [Managed Kubernetes](managed-kubernetes.md) | Paths on Amazon EKS, Google GKE, and Azure AKS |

Most self-hosted workloads store data on disk, with one SurrealDB process per database directory. From SurrealDB 4.0 the on-disk engine is **SurrealKV** (`surrealkv://`). RocksDB (`rocksdb://`) was removed in SurrealDB 4.0; see [Moving a RocksDB database to SurrealKV](deployment-models.md#moving-a-rocksdb-database-to-surrealkv).

## Operating a self-hosted instance

- [Configuration](configuration.md) - server startup options, environment variables, and storage engine selection.
- [Backups and recovery](backups-and-recovery.md) - export and import commands, backup strategies, and disaster recovery.
- [Monitoring and observability](monitoring-and-observability.md) - health endpoints, metrics, and tracing integration.
- [Upgrades and patching](upgrades-and-patching.md) - version upgrades, major-version data migration, and compatibility notes.

Once an instance is running, the [Observability](../observability/index.md) section covers the built-in metrics, audit logs and slow-query logs you can scrape over Prometheus or push over OTLP for production monitoring.

## Enterprise Edition

Self-hosted clusters can run [Enterprise Edition](../enterprise/product/database-enterprise.md), which adds distributed live queries, audit logging, FIPS-validated cryptography and support tiers on top of the same server.
