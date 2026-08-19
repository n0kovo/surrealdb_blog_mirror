---
position: 5
title: Managed Kubernetes
description: Options for running SurrealDB on Amazon EKS, Google GKE, and Azure AKS — managed Scale, self-hosted Enterprise clusters, or single-node RocksDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/self-hosted/managed-kubernetes.mdx"
---

# Managed Kubernetes

> [!IMPORTANT]
> Production **multi-node** SurrealDB uses shared distributed storage with replication and consensus — not TiKV. For managed HA, use the [Scale plan](https://surrealdb.com/pricing/scale). Self-hosted multi-node clusters on Kubernetes are available with [SurrealDB Enterprise](https://surrealdb.com/enterprise).

> [!NOTE]
> For a **single-node RocksDB** deployment on Kubernetes — including a cluster you create with EKS, GKE, or AKS — start with [Deploy on Kubernetes](kubernetes.md). For a local open-source distributed-storage playground only, see [Run a multi-node cluster](../../running/multi-node.md).

## The managed control planes

Each of the three major clouds offers a managed Kubernetes control plane. The control plane is the only part they manage for you; how SurrealDB storage is provided is still your choice — single-node RocksDB on a persistent volume, or a multi-node cluster on distributed storage (Scale or Enterprise).

| Provider | Service |
| --- | --- |
| AWS | [Amazon Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/) |
| Google Cloud | [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine), including Autopilot |
| Microsoft Azure | [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/products/kubernetes-service) |

## Choose a path

| Goal | Path |
| --- | --- |
| Managed multi-node HA (recommended for most teams) | A managed [Scale](../instances/index.md) cluster — no TiKV or TiDB operator to run |
| Self-hosted multi-node HA on EKS, GKE, or AKS | [SurrealDB Enterprise](https://surrealdb.com/enterprise) with distributed storage (operator and runbooks shipped with Enterprise) |
| Single SurrealDB pod, RocksDB on a volume | [Deploy on Kubernetes](kubernetes.md) on a cluster you manage |
| Local experiment with Community `tikv://` | [Run a multi-node cluster](../../running/multi-node.md) (not Scale or Enterprise storage) |

## Why not TiKV for production HA

Older guides walked through the [TiDB operator](https://github.com/pingcap/tidb-operator) and a TiKV cluster as the shared store behind SurrealDB on managed Kubernetes. That path is **not** the storage engine behind Scale or Enterprise deployments. Prefer a Scale or Enterprise cluster for production HA; keep TiKV for local Community experimentation only.

## Next steps

- [Deployment models](deployment-models.md) — single-node vs multi-node vs managed
- [Instances](../instances/index.md) — the managed option
- [Scale](https://surrealdb.com/pricing/scale) — pricing for managed multi-node clusters
- [Observability](../observability/index.md) once an instance is running
