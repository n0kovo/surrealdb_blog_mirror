---
position: 5
title: Azure AKS
description: Options for running SurrealDB on Azure Kubernetes Service — managed Scale, Enterprise SurrealDS, or single-node RocksDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/deployment/self-hosted/azure-aks.mdx"
---

# Deploy on Azure Kubernetes Service (AKS)

> [!IMPORTANT]
> Production **multi-node** SurrealDB uses **[SurrealDS](https://surrealdb.com/platform/surrealds)** for shared distributed storage — not TiKV. For managed HA on SurrealDS, use [SurrealDB Cloud Scale](https://surrealdb.com/pricing/scale). Self-hosted SurrealDS on Kubernetes is available with [SurrealDB Enterprise](https://surrealdb.com/enterprise).

> [!NOTE]
> For a **single-node RocksDB** deployment on Kubernetes (including a cluster you create with AKS), start with [Deploy on Kubernetes](kubernetes.md). For a local open-source distributed-storage playground only, see [Run a multi-node cluster](../../../running/multi-node.md).

## What is AKS?

[Azure Kubernetes Service](https://azure.microsoft.com/products/kubernetes-service) is Microsoft Azure’s managed Kubernetes offering. Storage for SurrealDB is still your choice: single-node RocksDB on a persistent volume, or multi-node SurrealDS (Cloud Scale or Enterprise).

## Choose a path

| Goal | Path |
| --- | --- |
| Managed multi-node HA (recommended for most teams) | [SurrealDB Cloud Scale](../surrealdb-cloud/what-is-surrealdb-cloud.md) on SurrealDS — no TiKV or TiDB operator to run |
| Self-hosted multi-node HA on AKS | [SurrealDB Enterprise](https://surrealdb.com/enterprise) with SurrealDS (operator and runbooks shipped with Enterprise) |
| Single SurrealDB pod, RocksDB on a volume | [Deploy on Kubernetes](kubernetes.md) on an AKS cluster you manage |
| Local experiment with Community `tikv://` | [Run a multi-node cluster](../../../running/multi-node.md) (not Cloud Scale / Enterprise storage) |

## Why not TiKV for production HA

Older guides walked through the TiDB operator and a TiKV cluster as the shared store behind SurrealDB on AKS. That path is **not** the storage engine behind Cloud Scale or Enterprise SurrealDS deployments. Prefer SurrealDS for production HA; keep TiKV for local Community experimentation only.

## Next steps

- [Deployment models](../index.md) — single-node vs multi-node vs Cloud
- [What is SurrealDB Cloud?](../surrealdb-cloud/what-is-surrealdb-cloud.md)
- [SurrealDS](https://surrealdb.com/platform/surrealds)
- [Observability](../../../manage/observability/index.md) once an instance is running
