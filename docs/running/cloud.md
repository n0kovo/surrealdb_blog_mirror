---
position: 3
title: SurrealDB Cloud
description: Get a free managed SurrealDB instance with an email sign-in. Persistent data without installing the server yourself.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/running/cloud.mdx"
---

# SurrealDB Cloud

[SurrealDB Cloud](../manage/instances/index.md) is a managed service: SurrealDB runs in our environment, and you connect from SurrealDB Studio, the SDKs, or the HTTP and WebSocket APIs. Compared to the [SurrealDB Studio Sandbox](sandbox.md), you sign in (typically with an email) and your **data persists** in a proper cloud instance.

![Diagram of a SurrealDB Cloud instance: requests to [instance-id].surreal.cloud reach a compute node backed by storage on Amazon S3.](../assets/img/image/cloud/light/cloud-architecture-light.png)

In SurrealDB Studio you can go from the Sandbox to Cloud with **Deploy to Cloud**, create an instance, and then point your connection at the new instance instead of Sandbox.

For day-to-day management, see [Instances](../manage/instances/index.md) and [Organisations](../manage/organisations/index.md) in the *Manage* section.
