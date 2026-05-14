---
title: "The Surrealist Journey"
slug: "the-surrealist-journey"
date: "2024-04-23T00:00:00.000Z"
categories:
  - "company"
read_time: "7 min read"
summary: "Interacting with a database is not an easy job. You’ll often find yourself needing to query patterns in your data, testing whether your queries have the intended outcome, or carefully designing a schema to suit your application. This was a natural hurdle I ran into when first adopting SurrealDB into my workflow, and is exactly why I built Surrealist."
source: "https://surrealdb.com/blog/the-surrealist-journey"
cover: "../../assets/3835f44a7b547c10.jpg"
---

# The Surrealist Journey

![The Surrealist Journey](../../assets/3835f44a7b547c10.jpg)

Interacting with a database is not an easy job. You’ll often find yourself needing to query patterns in your data, testing whether your queries have the intended outcome, or carefully designing a schema to suit your application. This was a natural hurdle I ran into when first adopting SurrealDB into my workflow, and is exactly why I built Surrealist.

## Introduction

Hello everyone, I’m Julian (also known as Jools). Some of you might know me as the developer behind [Surrealist](https://app.surrealdb.com), an open-source graphical application for interacting with SurrealDB. I’ve spent the past 16 months building and growing Surrealist into a multi-purpose management application allowing individuals and teams to take full advantage of the fantastic features offered by this database. Today, I'm pleased to announce that I have officially joined SurrealDB, and that Surrealist is now SurrealDB's official graphical UI to provide first-class support for interacting with your database. In this blog post I would love to share my journey and future plans for Surrealist.

## Humble beginnings

Everyone has to start somewhere. For me this was finding an old weathered HTML 2.0 book in the attic. Only 15 years old at the time, I was sparked with interest by the mysterious-sounding subject of publishing on the world wide web. As I started reading the book and experimenting with building web pages on my computer, it introduced the world of software development to me. This book ultimately led to me perusing a career in web and software development.

![The book that sparked my software career](../../assets/1450e6bc247b791a.jpg)

## Discovering SurrealDB

We now fast forward seven years to September 2022, when I am struggling to find a solution to a set of difficulties I’m facing while migrating my backend application from Firebase to Postgres at work. My application had the unusual requirement of being highly flexible, previously made possible due to Firebase. However, because of growing customer demands and limitations of Firebase, I had to incorporate a more efficient and powerful database into my setup. This ultimately ended up being Postgres. While at first everything seemed fine, Postgres quickly became increasingly unwieldy to use, with enormous JOIN chains littering my codebase, and a lack of features I was used to - such as live queries. Additionally, the mandatory schema contradicted the flexibility required by my application, which benefitted from a rigid schema in places but still required the freedom to do away with it when necessary.

One day, as I was visiting YouTube, I came across [a fantastic video](https://www.youtube.com/watch?v=C7WFwgDRStM) posted by Fireship. This video resonated with me and quickly made me realise this was the database I had been searching for all this time. Without hesitation, I started experimenting with SurrealDB in my off time and explored the capabilities it could offer. To my honest surprise, it really did work as well as expected, and I quickly fell in love with the approach SurrealDB takes on common database challenges.

## Dawn of Surrealist

A few months later, in December of 2022, I once again ran into a major struggle with Postgres at work. I decided enough is enough and made the decision to start building a SurrealDB-powered version of the backend. Before I could start however, I needed an efficient way to write and test my queries. This is when I made the very first version of Surrealist, which at the time was nothing more than a graphical way to execute queries and view their responses.

![The very first public version of Surrealist which offered only query capabilities](../../assets/596a0ab3f00e8a08.jpg)

Although the first version of Surrealist was bare bones, it did its job well and allowed me to start developing against SurrealDB without resorting to the CLI. I proceeded to post this first release in the SurrealDB Discord hoping it could help others in the same way it helped me. Over time I received feature requests and suggestions from community members which fell in line with my vision for Surrealist.

The first few months following the initial release of Surrealist were turbulent as I was working on new functionality nearly daily. Some of the earliest features that were added include query saving, the query history, and table name autocompletion. Soon after that came the first feature that didn’t revolve specifically around sending queries, which was the explorer view. Switching to the explorer view allowed users to present records in an easy-to-navigate data table, and effortlessly update records by clicking on them. This ultimately paved the way forward for Surrealist to introduce additional views focusing on the different aspects of interacting with a SurrealDB database.

![The first version of the Surrealist explorer view, intended for browsing your records without the need of writing manual queries.](../../assets/a9f06328a2675f20.jpg)

## The official unofficial interface

In the months that followed, Surrealist evolved into a whole project on its own. By this time many users in the community were using Surrealist to interact with their database. At the same time I was also using it at work to manage 30+ different SurrealDB databases. This first-hand experience working with SurrealDB gave me insight into how to design Surrealist so it could most effectively help its users.

Over time I expanded Surrealist with additional views such as the Designer view, and Authentication view. The former allows users to build and manage database schemas without having to write any queries manually, while the latter can be used to manage user logins and scope access. As Surrealist became increasingly valuable to more and more users, it was even included in the official ‘getting started’ guide within the docs. At the same time I was also invited to attend the SurrealDB World conference as a guest speaker to talk about Surrealist.

![Micha and Julian at SurrealDB World](../../assets/a99dd9078bdd2d1d.jpg)

At this point in time Surrealist had already grown beyond my expectations. What started as a simple tool I built for myself to test queries slowly evolved into the most-used management interface for SurrealDB. This brings us to today, when Surrealist is taking the next step forward to become the official interface used to interact with SurrealDB.

## Surrealist 2.0

As announced above, I have officially joined SurrealDB together with Surrealist. While that is exciting on its own, I have many plans for the future in order to make even more SurrealDB functionality accessible to a wider audience. This latest step forward is the release of Surrealist 2.0, a near complete redesign and rework of Surrealist. Alongside it, we have updated the Surrealist brand and design to align with SurrealDB and offer a visually pleasing experience.

![Surrealist 2.0](../../assets/b612aee8e0e9e539.jpg)

As for Surrealist itself, many features have been reworked and revised. This was finally the right time to clean up a lot of legacy that was left around since the early days. Some changes include simplifying connection management, merging live query support into the Query View, and updating the underlying SurrealQL editor. I have also taken the time to introduce many new features, such as an easy-to-navigate command palette, an API docs view for browsing personalised documentation, and much more.

We now have a [brand new documentation section](/docs/surrealist) devoted just to Surrealist, which I invite everyone to visit to see all new features introduced in Surrealist 2.0. Additionally, we now provide guides on how to use all available views, including those introduced in this latest update.

I'm incredibly happy to be at SurrealDB in a position where I can dedicate my time to Surrealist and break through new frontiers in order to make Surrealist the ultimate dashboard for the ultimate database. All I can say to end this post is thank you for using Surrealist, and I hope I can positively contribute to your database experience.
