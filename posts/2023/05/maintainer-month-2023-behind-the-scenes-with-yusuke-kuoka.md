---
title: "Maintainer Month 2023: Behind the scenes with Yusuke Kuoka"
slug: "maintainer-month-2023-behind-the-scenes-with-yusuke-kuoka"
date: "2023-05-29T00:00:00.000Z"
categories:
  - "community"
read_time: "5 min read"
summary: "Hi! I’m Yusuke, and I’m a Senior Software Engineer at SurrealDB. It’s #MaintainerMonth, so I’d like to explain why I became a ‘maintainer’, tell you about my journey so far, and then give you a glimpse of my life as a maintainer."
source: "https://surrealdb.com/blog/maintainer-month-2023-behind-the-scenes-with-yusuke-kuoka"
cover: "../../assets/f40da83f8f9b1456.jpg"
---

# Maintainer Month 2023: Behind the scenes with Yusuke Kuoka

![Maintainer Month 2023: Behind the scenes with Yusuke Kuoka](../../assets/f40da83f8f9b1456.jpg)

Hi! I’m Yusuke, and I’m a Senior Software Engineer at SurrealDB. It’s #MaintainerMonth, so I’d like to explain why I became a ‘maintainer’, tell you about my journey so far, and then give you a glimpse of my life as a maintainer.

I'm a former application developer who had some experience developing web, Android, and iOS apps. Recently I was an infrastructure engineer focusing on AWS and Kubernetes. This March, I joined SurrealDB, and since then I’ve been focusing on a new feature called ‘change feeds’.

![Yusuke Kuoka](../../assets/f7a5647d2dc58fa8.jpg)

## Open-source and me

Regardless of what I focus on at any time, I'm always interested in making things ‘nearly the best at that moment in time’. But sometimes the team you're working with is very small, and you have no one to ask to implement cutting-edge things for you. Doing it alone is rarely possible. Open-source to the rescue!

I tend to maintain or create projects from necessity. Back in the day, I started contributing to a project called ‘kube-aws’ to automate Kubernetes deployment onto AWS; later I became the primary maintainer of this, which enabled me to introduce Kubernetes to my company. I collaboratively built kube-aws with many contributors and maintainers from around the world. It did require me to pay forward. I had to fix bugs and add features that didn’t seem directly related to my company. Later on, though, it all paid off. I made Kubernetes into production, thanks to kube-aws being all set with both day-1 and day-2 operations, and thanks to the community! Without open-source, it wasn’t possible with a small team of one dedicated to the infrastructure and Kubernetes, and it was way before there was an AWS-managed service for Kubernetes (EKS). AWS gave me the title 'AWS Container Landing,' probably for advocating using Kubernetes with AWS in the early days.

At the same time, I did similar things for projects like `helmfile`, `helm-diff`, and `actions-runner-controller(ARC)`. All three solve diverging problems related to leveraging Kubernetes and are pretty popular today, gaining thousands of stars each. ARC is now part of GitHub, and I can benefit from GitHub-supported new ARC as a user - because my ex-colleague started the project, and the co-maintainer and I kept growing the project for three years. Again, open-source worked for me!

## Why I joined SurrealDB

Whenever I had to write an app, I had to choose a database that worked best for the use case, find a library and a framework to easily interact with it, and repeat this every time I wrote a new app! These days, of course, it's very common to have two or more databases for one app, due to each database doing a single thing very well.

When I first learned about SurrealDB last fall, it looked like an excellent open-source database that did many things in one database. I wanted it to be real! So I looked deeper. I realised that the only missing fundamental piece for my dream-use case of SurrealDB was the ability to deliver a correct and scalable change history of the database. Although there was a similar roadmap item (‘live queries and record changes’, which is suitable for building real-time apps), it wasn’t clear to me if the database author meant to give it bigger correctness and scalability stories - which might be too much for live queries, but necessary for doing things like CDC (Change-Data-Capture). That’s when I started wishing there was a ‘change feeds’ feature in SurrealDB.

If you are unfamiliar with the term, in SurrealDB, ‘change feeds’ gives you a history of all the changes made to the database. Although some databases include more features like not storing changes but also exporting changes to external databases, this ‘history of all the changes’ is what I wanted first in SurrealDB’s change feeds because it is the foundation for everything else!

I always wish for something like ‘change feeds’, ‘change history’, ‘changelog’, ‘commit history’, whatever you call it, to be:

- replayable (you can continue reading changes from where you previously stopped);
- consistently ordered (changes are streamed in the commit order);
- scalable, as much as possible.

So that it could be used for virtually any CDC-related tasks, I read SurrealDB implementation. It is envisioned to support both single-node and distributed cluster setups thanks to various open-source single-node and distributed KVS as backends. For the distributed setup, though, I thought I could build such change feeds more easily on top of FoundationDB, which was and still is my favourite distributed KVS. I sent a pull request to add support for it, followed by an unsolicited design proposal to implement a scalable ‘change feeds’ feature on top of it. A few months later, I became a full-time SurrealDB employee.

## My work now

Today, I still focus on ‘change feeds’ because it’s supposed to be the only reliable way to securely export data from SurrealDB to other SurrealDB or other projects. You can connect any purpose-built open-source database to SurrealDB, for example. And you might eventually be able to sync SurrealDB across native apps, edges, and clouds!

At SurrealDB, we encourage contributions back to the [SurrealDB](https://github.com/surrealdb) org on GitHub, whether it's the [main repo](https://github.com/surrealdb/surrealdb), [client & server libraries](https://github.com/surrealdb/surrealdb#getting-started) or my personal favourite [awesome-surreal](https://github.com/surrealdb/awesome-surreal).

I like that being a maintainer allows me to make significant changes that I wouldn’t be able to alone. Being a maintainer is what brought me here. Today, I’m one of the SurrealDB maintainers because I want to build a database of my dreams with you.
