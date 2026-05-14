---
title: "Announcing SurrealDB 1.0"
slug: "announcing-surrealdb-1-0"
date: "2023-09-14T00:00:00.000Z"
categories:
  - "releases"
  - "company"
read_time: "5 min read"
summary: "At SurrealDB World, we’re excited to launch SurrealDB 1.0, a revolution in the database technology landscape. With this stable release, we're not just introducing a database; we're redefining the essence of how databases function and integrate with your projects."
source: "https://surrealdb.com/blog/announcing-surrealdb-1-0"
cover: "../../assets/d5191161654e91d1.jpg"
---

# Announcing SurrealDB 1.0

![Announcing SurrealDB 1.0](../../assets/d5191161654e91d1.jpg)

At SurrealDB World, we’re excited to launch SurrealDB 1.0, a revolution in the database technology landscape. With this stable release, we're not just introducing a database; we're redefining the essence of how databases function and integrate with your projects.

Imagine a world where the majority of your backend logic is seamlessly embedded within the database itself. SurrealDB makes this vision a reality, minimising the need for extensive backend coding and eliminating the hassle of juggling multiple tools. This ensures that you can focus on what truly matters: building and scaling your next big product.

This post takes a look at what’s new, and what the 1.0 designation means for SurrealDB users.

## SurrealLQ: Live Queries

![SurrealLQ](../../assets/0fc4dcb60f40abe3.jpg)

SurrealDB 1.0 introduces Live Queries, which develops an efficient way to stay updated with real-time data changes. By leveraging this feature, any alterations in the data are immediately flagged and sent as notifications, eliminating the need to constantly poll or manually check for updates. This is further enhanced by SurrealDB's integrated permission system, ensuring that each notification is tailored according to the user's authentication, adding an extra layer of security and relevance. For instance, to receive updates on all changes in the 'person' table, one would use:

```surrealql
LIVE SELECT * FROM person;
```

To filter these live updates, say for persons aged over 18, the query would be:

```surrealql
LIVE SELECT * FROM person WHERE age > 18;
```

This capability simplifies the development process, especially for applications that rely on real-time data. Whether it's building dynamic user interfaces, monitoring tools, or applications that require immediate response to data shifts, Live Queries streamline the process, making real-time data management more accessible and efficient for developers.

## SurrealCF: Change Feeds

![SurrealCF Icon](../../assets/c3084e38d4bbf71c.jpg)

With SurrealDB 1.0, we are introducing [Change Feeds](/features). This fundamental feature provides change-data-capture functionality to SurrealDB, enabling users and developers to track and respond to changes as they occur within the database.

Whether exporting data in real-time into third-party systems, moving data to object storage for backup or analysis purposes, or even for real-time cross-cloud synchronisation with other platforms, Change Feeds enable greater interoperability with other technologies within larger enterprise systems.

The design of Change Feeds emphasises three key characteristics:

- Replayable: Allows users to continue from where they left off.
- Ordered: Changes are displayed in the sequence they were committed.
- Scalable: Adapts to different data sizes.

Accessible to any database user with the correct permissions level, our initial implementation of Change Feeds can be applied to individual tables separately, or all tables within a database as a whole. What this means to a developer is that applications can subscribe to the specific data that they need, without impacting the performance of the database system or cluster.

## SurrealIX: Indexing and Vector Functions

![SurrealIX](../../assets/e0fbbf44a6e42d4f.jpg)

[SurrealIX](/features) is SurrealDB's integrated indexing solution. Eschewing external libraries, SurrealDB has crafted its own indexing engine to ensure consistent query performance across all database configurations. This engine seamlessly integrates with the SurrealQL query language, simplifying the indexing process.

In SurrealDB 1.0, we've expanded our indexing capabilities to include traditional and [unique indexes](/docs/surrealql/statements/define/indexes), [full-text search](/docs/surrealql/functions/database/search), and a beta version of [v](/docs/surrealql/functions/database/vector)ector search. This vector search efficiently finds similar items in datasets by comparing their multi-dimensional representations, optimising the kNN operation.

Whether you're dealing with standard queries or diving into machine learning-generated datasets, SurrealIX is designed to speed up your queries!

## SurrealQL: Loop and Error statements

![SurrealQL](../../assets/d44a9fb1f98d4e2b.jpg)

We've introduced some powerful control flow statements in [SurrealQL](/docs/surrealql).

The **`FOR`** statement allows you to loop through arrays, enabling you to perform actions on each item.

#### Syntax:

```javascript
FOR @item IN @iteratable @block
```

Sometimes, you might want to skip certain iterations in a loop. The **`CONTINUE`** statement lets you do just that.

The `BREAK` statement can be used to break out of a loop, like the [FOR](/docs/surrealql/statements/for)-statement.

The `THROW` statement can be used to throw an error in a place where something unexpected is happening. Execution of the query will be aborted and the error will be returned to the client.

## SurrealML: Machine Learning

![SurrealML](../../assets/d4e8d9af29ba7837.jpg)

[SurrealML](/features) is all about enabling us to run machine learning models efficiently on our database, all without the user having to load and transfer a model over a network.

At its core, `.surml` is a meticulously crafted file format library, built in Rust with Python bindings, and designed to bridge the gap between model training and deployment.

Train your models in Python, save them in the **`.surml`** format, and enrich them with metadata like column names and normalisers. Once saved, these models are primed for execution, either in our Rust runtime or any Python environment with Pytorch installed.

SurrealML stands out because of how it uses metadata. This means users don't have to manually adjust data or decide how inputs are used. Just give it the data, and SurrealML takes care of the rest. It works well with decision trees from SkLearn and tensors in Pytorch.

SurrealML within SurrealDB 1.0 will be released in beta this month, so you can start working with machine learning models right within the database with ease.

## What’s Next?

As we unveil SurrealDB 1.0, we're filled with gratitude for the invaluable feedback and contributions from our community. This release marks a significant milestone in our journey, showcasing our dedication to stability and top-tier performance. While we're proud of the strides we've made with 1.0, we're not stopping here. We're diligently refining and enhancing SurrealDB, ensuring it meets the exacting standards required for production environments. Rest assured, our next major release is on the horizon, and it promises to be a game-changer.

Stay connected and be the first to know about our latest developments by following us on [GitHub](https://github.com/surrealdb/surrealdb), [Discord](https://discord.gg/surrealdb), [Twitter](https://twitter.com/SurrealDB) and [LinkedIn](https://www.linkedin.com/company/surrealdb). SurrealDB is poised to redefine the database landscape. Join us in shaping the future.
