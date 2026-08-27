---
position: 5
title: Managed Kubernetes
description: Options for running SurrealDB on Amazon EKS, Google GKE, and Azure AKS - managed Scale, self-hosted Enterprise clusters, or single-node RocksDB.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/self-hosted/managed-kubernetes.mdx"
---

# Managed Kubernetes

> [!IMPORTANT]
> Production **multi-node** SurrealDB uses shared distributed storage with replication and consensus. For managed HA, use the [Scale plan](https://surrealdb.com/pricing/scale). Self-hosted multi-node clusters on Kubernetes are available with [SurrealDB Enterprise](https://surrealdb.com/enterprise).

> [!NOTE]
> For a **single-node RocksDB** deployment on Kubernetes - including a cluster you create with EKS, GKE, or AKS - start with [Deploy on Kubernetes](kubernetes.md). For how the multi-node model works in general, see [Run a multi-node cluster](../../running/multi-node.md).

## The managed control planes

Each of the three major clouds offers a managed Kubernetes control plane. The control plane is the only part they manage for you; how SurrealDB storage is provided is still your choice - single-node RocksDB on a persistent volume, or a multi-node cluster on distributed storage (Scale or Enterprise).

| Provider | Service |
| --- | --- |
| AWS | [Amazon Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/) |
| Google Cloud | [Google Kubernetes Engine (GKE)](https://cloud.google.com/kubernetes-engine), including Autopilot |
| Microsoft Azure | [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/products/kubernetes-service) |

## Choose a path

| Goal | Path |
| --- | --- |
| Managed multi-node HA (recommended for most teams) | A managed [Scale](../instances/index.md) cluster, with the storage layer operated for you |
| Self-hosted multi-node HA on EKS, GKE, or AKS | [SurrealDB Enterprise](https://surrealdb.com/enterprise) with distributed storage (operator and runbooks shipped with Enterprise) |
| Single SurrealDB pod, RocksDB on a volume | [Deploy on Kubernetes](kubernetes.md) on a cluster you manage |

## Next steps

- [Deployment models](deployment-models.md) - single-node vs multi-node vs managed
- [Instances](../instances/index.md) - the managed option
- [Scale](https://surrealdb.com/pricing/scale) - pricing for managed multi-node clusters
- [Observability](../observability/index.md) once an instance is running
