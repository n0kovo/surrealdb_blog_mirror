---
position: 1
title: Cloud management
description: "Manage your SurrealDB Cloud deployment: instances, networking, backups, billing, and team access."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/cloud/index.mdx"
---

# Cloud management

This section covers the day-to-day management of a SurrealDB Cloud deployment. If you are setting up Cloud for the first time, start with the [getting started guide](../../build/deployment/surrealdb-cloud/getting-started/index.md) and [connecting](../../build/deployment/surrealdb-cloud/connecting/index.md) pages instead.

## Cloud plans

SurrealDB Cloud offers managed deployments from development through production-scale clusters:

| Plan | Topology | Storage | Best for |
| --- | --- | --- | --- |
| **Start** (incl. free tier) | Single-node | Dedicated storage per instance | Development, staging, and workloads that scale vertically |
| **Scale** | Multi-node cluster (min. three compute units) | [SurrealDS](https://surrealdb.com/platform/surrealds) distributed storage | Business-critical production that must survive node failure |

**Start** is straightforward to operate: one server to resize, back up, and connect to. That is enough for many applications, including paid production workloads that tolerate brief downtime or can recover from snapshots.

**Scale** is where a managed service delivers the most value for **business-critical** databases. On a single node, a disk fault, host failure, or infrastructure issue in the region can take the whole application offline until recovery finishes — and the database is usually the component you least want down. Scale runs a **multi-node cluster** on SurrealDS so query traffic continues when one node is unavailable, and you can add compute units as load grows. SurrealDB Cloud handles cluster operations — provisioning, patching, backups, networking, and rolling upgrades — so your team does not need to build and run that platform itself.

Scale costs more than Start because it runs multiple nodes, but is likely to cost less than staffing and operating an equivalent self-hosted cluster on Kubernetes. See [High availability](high-availability.md), [Scaling](scaling.md), and [Cloud architecture](../../build/deployment/surrealdb-cloud/architecture.md). For pricing, see [surrealdb.com/pricing](https://surrealdb.com/pricing).

## Management topics

Topics covered here include:

- [Instance management](instance-management.md) — creating, pausing, resuming, and deleting instances.
- [Scaling](scaling.md) — adjusting compute and storage to match your workload.
- [High availability](high-availability.md) — fault tolerance on Start vs Scale plans.
- [Network access](network-access.md) — IP allowlisting, VPC peering, and PrivateLink configuration.
- [Backups & recovery](backups-and-recovery.md) — automated snapshots, retention policy, and in-platform restore.
- [Monitoring & logs](monitoring-and-logs.md) — dashboards, metrics, and log access.
- [Patches & upgrades](patches-and-upgrades.md) — changing the SurrealDB version on Cloud instances.
- [Organisations & users](organisations-and-users.md) — team management, roles, and invitations.
- [Billing & support](billing-and-support.md) — plans, invoices, and support channels.
- [AWS Marketplace](aws-marketplace.md) — subscribing to SurrealDB Cloud through AWS Marketplace.
