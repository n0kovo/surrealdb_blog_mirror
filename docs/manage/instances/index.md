---
position: 1
title: Instances
description: What an instance is, how the Start and Scale plans differ, and where each operational task is documented.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/instances/index.mdx"
---

# Instances

An instance is a SurrealDB deployment that SurrealDB runs for you.

That covers provisioning, high availability, patching, backups, and version upgrades. You choose a plan, a size, and a region, then connect your application.

Every instance belongs to an [organisation](../organisations/index.md), which also holds members, usage, and billing. You operate instances from [SurrealDB Studio](https://app.surrealdb.com), or from a terminal with [`surrealctl`](../surrealctl/instances.md). To run and operate the server yourself, see [Self-hosted](../self-hosted/index.md).

<Button label="Open SurrealDB Studio" href="https://app.surrealdb.com" variant="surreal" />

<YouTube code="S04qOKkVcmE?si=6tOcQyeXPTzcR8JS" />

## Plans

Two plans are available. The plan you choose at deploy time fixes the topology of the instance.

| Plan | Topology | How it grows | Storage | Suited to |
| --- | --- | --- | --- | --- |
| **Start** | A single node | Vertically, by moving to a larger instance type | A dedicated disk per instance | Development, staging, and workloads that fit on one node |
| **Scale** | A cluster of three nodes or more | Vertically and horizontally, by using larger nodes or more nodes | Distributed storage shared across the cluster | Production that must survive the loss of a node |

Start offers three families of instance type. **Free** is for trying SurrealDB out, **Burstable** is for low-traffic and intermittent workloads, and **General purpose** is for steady production traffic. Scale uses General purpose nodes.

The plan also gates some options. Configurable [backup frequency](backups.md) is available on Scale instances only.

Current capacity ceilings and prices are on the [pricing page](https://surrealdb.com/pricing). The plan cards in the deploy flow show what applies to your organisation. For the topology behind each plan, see [Architecture](architecture.md).

## Where instances live

The **Instances** section of SurrealDB Studio lists every instance in the organisation you are viewing. Each card shows the SurrealDB version and the region. Use the search box and the **Version** and **Type** filters to narrow a long list.

![The Instances page of SurrealDB Studio for the Acme Corp organisation, listing three instance cards: api-production on SurrealDB 3.2.4, and api-staging and analytics-eu on SurrealDB 3.2.1. All three are in AWS Europe (Ireland). The page also has a search box, Version and Type filters, and a Deploy new instance button.](../../assets/img/surrealdb/manage/instances-list.webp)

Selecting an instance opens its own workspace. That workspace holds a [dashboard](monitoring.md) of resource use, the schema and query views, and **Settings**. Settings is where [configuration](configure.md), [capabilities](configure.md#capabilities), [versions](versions-and-upgrades.md), compute, and [backups](backups.md) live.

`surrealctl instance list` prints the same list in a terminal, and `--json` makes it scriptable. See [surrealctl instances](../surrealctl/instances.md).

## Lifecycle

You control the lifecycle of an instance with four actions.

| Action | Effect | Where |
| --- | --- | --- |
| **Deploy** | Provisions the instance on the chosen plan, type, and region | [Create an instance](create.md) |
| **Resize** | Changes the instance type or the storage capacity in place | [Scaling](scaling.md) |
| **Pause** | Stops compute and usage billing. Data and configuration are kept, and the instance is unreachable until you resume it | [Configure an instance](configure.md#pause-an-instance) |
| **Delete** | Destroys the instance and everything stored in it, with no way to recover it | [Configure an instance](configure.md#delete-an-instance) |

You cannot change an instance name after deployment. Pick a name a colleague will still recognise in six months, such as `api-production` rather than `db1`.

## Topics

- **[Create an instance](create.md):** plan, instance type, region, version, name, and starting data.
- **[Configure an instance](configure.md):** capabilities, compute, storage, pausing, and deletion.
- **[Connect to an instance](connect/index.md):** SurrealDB Studio, the CLI, SDKs, and HTTP.
- **[Architecture](architecture.md):** single-node and multi-node topologies.
- **[Scaling](scaling.md):** matching compute and storage to the workload.
- **[High availability](high-availability.md):** what survives a node failure on each plan.
- **[Backups and recovery](backups.md):** automated snapshots, retention, and restore.
- **[Import and export](import-and-export.md):** moving data with `surreal export` and `surreal import`.
- **[Versions and upgrades](versions-and-upgrades.md):** changing the SurrealDB version.
- **[Monitoring](monitoring.md):** the instance dashboard, metrics, and logs.
- **[Network access](network-access.md):** which outbound destinations queries may reach.
- **[Private connectivity](private-connectivity.md):** AWS PrivateLink and instance access modes.

## Related sections

- **[Organisations](../organisations/index.md):** accounts, members, roles, usage, billing, and support.
- **[surrealctl](../surrealctl/index.md):** the management-plane command-line tool.
- **[Observability](../observability/index.md):** the full metric, audit-log, and slow-query reference.
- **[Self-hosted](../self-hosted/index.md):** running SurrealDB on your own infrastructure instead.
