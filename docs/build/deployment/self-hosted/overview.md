---
position: 1
title: Self-hosted deployment
description: Getting started with SurrealDB is quick and easy. Follow these tutorials for deploying SurrealDB in different environments.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/deployment/self-hosted/overview.mdx"
---

# Deployment

Deploying a self-hosted instance with SurrealDB is quick and easy. All of SurrealDB's functionality for starting a server, and importing and exporting data, is enabled through the [command-line tool](../../../reference/cli/surrealdb-cli/overview.md), packaged and distributed as a single executable file, which can be downloaded, installed, or run from within Docker.

Once a self-hosted instance is running, the [Observability](../../../manage/observability/index.md) section covers the built-in metrics, audit logs and slow-query logs you can scrape over Prometheus or push over OTLP for production monitoring.

## Guides

| Guide | Typical use |
| --- | --- |
| [Docker](docker.md) | Quickest path; RocksDB with a volume mount |
| [Kubernetes](kubernetes.md) | Single SurrealDB pod with RocksDB on a persistent volume |
| [Amazon EKS](amazon-eks.md) / [GKE](google-gke.md) / [AKS](azure-aks.md) | Highly available clusters on managed Kubernetes |
| [SurrealDB Cloud](../surrealdb-cloud/what-is-surrealdb-cloud.md) | Managed infrastructure without operating servers yourself |

Most self-hosted workloads use **RocksDB** on disk — one SurrealDB process per database file. See [Deployment models](../index.md) for how single-node and highly available topologies compare.
