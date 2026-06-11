---
position: 3
title: Kubernetes
description: Deploy SurrealDB to Kubernetes with RocksDB on a persistent volume.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/deployment/self-hosted/kubernetes.mdx"
---

# Deploy on Kubernetes

This guide deploys SurrealDB to a local [KIND](https://kind.sigs.k8s.io/) cluster (Kubernetes in Docker) with **RocksDB** on a persistent volume. That is a **single-node** topology: one SurrealDB pod owns the database file. See [Deployment models](../index.md#single-node-rocksdb).

For highly available clusters on managed Kubernetes, see [Amazon EKS](amazon-eks.md), [Google GKE](google-gke.md), and [Azure AKS](azure-aks.md). For a managed service, see [SurrealDB Cloud](../surrealdb-cloud/what-is-surrealdb-cloud.md).

## Requirements

- [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- [`helm`](https://helm.sh/docs/intro/install/)
- [KIND](https://kind.sigs.k8s.io/) and [Docker](https://www.docker.com/)
- [Surreal CLI](../../../reference/cli/surrealdb-cli/overview.md)

## Create a KIND cluster

```bash
kind create cluster -n surreal-demo
kubectl config current-context   # kind-surreal-demo
kubectl get ns
```

## Deploy SurrealDB

Use the [SurrealDB Helm chart](https://github.com/surrealdb/helm-charts) with a **ReadWriteOnce** persistent volume. Keep **`replicaCount: 1`** — multiple pods must not share one RocksDB file.

### 1. Add the Helm repository

```bash
helm repo add surrealdb https://helm.surrealdb.com
helm repo update
```

### 2. Install with persistence

The chart mounts storage at `/home/nonroot` so the non-root container user can write to the volume:

```bash
cat <<'EOF' | helm install surrealdb-rocksdb surrealdb/surrealdb -f -
strategy:
  type: Recreate
replicaCount: 1
persistence:
  enabled: true
  mountPath: /home/nonroot
  size: 10Gi
surrealdb:
  path: rocksdb:///home/nonroot/data.db
  unauthenticated: true
EOF
```

### 3. Create initial credentials

Port-forward the service, define a root user, then re-enable authentication:

```bash
kubectl port-forward svc/surrealdb-rocksdb 8000:8000
```

In another shell:

```bash
surreal sql -e http://localhost:8000
> DEFINE USER root ON ROOT PASSWORD 'StrongSecretPassword!' ROLES OWNER;
```

Upgrade the release without `unauthenticated`:

```bash
helm upgrade surrealdb-rocksdb surrealdb/surrealdb -f - <<'EOF'
strategy:
  type: Recreate
replicaCount: 1
persistence:
  enabled: true
  mountPath: /home/nonroot
  size: 10Gi
surrealdb:
  path: rocksdb:///home/nonroot/data.db
EOF
```

### 4. Verify persistence

```bash
surreal sql -u root -p 'StrongSecretPassword!' -e http://localhost:8000
> USE NS ns DB db;
ns/db> CREATE record SET id = record:one;
ns/db> SELECT * FROM record;
```

Delete the SurrealDB pod and confirm data survives on the PVC:

```bash
kubectl get pod
kubectl delete pod <surrealdb-rocksdb-pod-name>
kubectl port-forward svc/surrealdb-rocksdb 8000:8000
surreal sql -u root -p 'StrongSecretPassword!' -e http://localhost:8000
> USE NS ns DB db;
ns/db> SELECT * FROM record;
```

> [!NOTE]
> On a full Kubernetes cluster, set `ingress.enabled=true` when installing the chart to expose SurrealDB through a load balancer instead of port-forwarding.

## Next steps

- [Docker](docker.md) — single-node RocksDB without Kubernetes
- [Run a single-node, on-disk server](../../../running/file-backed.md) — CLI startup options for RocksDB and SurrealKV
- [Deployment models](../index.md) — Cloud, single-node, and highly available options
