---
position: 2
title: Architecture
description: In this section, we will explore the SurrealDB Cloud architecture and how it is designed to provide a scalable, high-performance, and secure database solution.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/deployment/surrealdb-cloud/architecture.mdx"
---

# Cloud architecture

SurrealDB Cloud benefits from [SurrealDB’s layered architecture](../../../architecture.md), which separates storage from compute, enabling improved scalability, durability and availability without the need to operate, manage, scale or shard your database.

## Start
For development, and staging applications with vertically-scalable requirements. SurrealDB Cloud Start provides users with dedicated storage and a single-node for compute which can scale vertically.

![SurrealDB Cloud architecture](../../../assets/img/image/cloud/light/start-single-node-light.png)

## Scale

For large-scale, mission-critical applications that need fault tolerance and horizontal scalability. Scale clusters run on [SurrealDS](https://surrealdb.com/platform/surrealds), SurrealDB's distributed storage engine — quorum consensus, compute–storage separation, and object-storage-backed durability — so query nodes stay comparatively stateless while the storage tier handles replication and distributed transactions.

![SurrealDB Cloud Scale architecture](../../../assets/img/image/cloud/light/enterprise-multi-node-light.png)

To learn more about the plans, refer to the [Pricing](https://surrealdb.com/pricing) page.
