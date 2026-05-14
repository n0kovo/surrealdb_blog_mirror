---
title: "Maintainer Month 2023: Behind the scenes with Rushmore Mushambi"
slug: "maintainer-month-2023-behind-the-scenes-with-rushmore-mushambi"
date: "2023-05-25T00:00:00.000Z"
categories:
  - "community"
read_time: "6 min read"
summary: "Hi everyone. My name is Feranmi Okafor. I'm a Social Media Manager at SurrealDB. As part of our efforts to celebrate #MaintainerMonth 2023, we had a quick chat with one of our maintainers here at SurrealDB."
source: "https://surrealdb.com/blog/maintainer-month-2023-behind-the-scenes-with-rushmore-mushambi"
cover: "../../assets/f40da83f8f9b1456.jpg"
---

# Maintainer Month 2023: Behind the scenes with Rushmore Mushambi

![Maintainer Month 2023: Behind the scenes with Rushmore Mushambi](../../assets/f40da83f8f9b1456.jpg)

Hi everyone. My name is Feranmi Okafor. I'm a Social Media Manager at SurrealDB. As part of our efforts to celebrate [#MaintainerMonth 2023](https://maintainermonth.github.com), we had a quick chat with one of our maintainers here at SurrealDB.

Rushmore Mushambi is one of our senior software engineers. He maintains our Rust API layer and WebAssembly library. He is also our first engineering hire, joining SurrealDB in January.

**Feranmi:** Rushmore, can you tell us a little bit about yourself?

**Rushmore:** Thanks, Feranmi. I'm an accountant by training, but I have a huge passion for software engineering, which is what got me here. I grew up in a rural area in Zimbabwe. I moved to Bulawayo, Zimbabwe's second-largest city, in 1998 to start to form one. In 2002 I moved to Harare, Zimbabwe's capital city, for the lower six. This is interesting to me because this was when the famous dot-com bubble happened. I was oblivious to this at the time, though. I had no access to computers, let alone the Internet.

**Feranmi:** Right! So how did you get into software engineering?

**Rushmore:** During lower six, some of my new friends at school would visit Internet Cafes to check their emails. I accompanied them one day, and that's how I got introduced to the world of computers and got exposed to the Internet for the first time. I was fascinated! From then on, I would go with them every time they visited Internet Cafes. Before long, I was sneaking out to play on my own. I didn't want to embarrass myself in front of my friends! I wanted to know how everything worked. How one could send a message halfway around the world, and it arrived almost instantly. How were those messages got displayed on the computer screen? By the time I finished upper six, I had built my own website and was well on my way to becoming a software engineer.

**Feranmi:** Nice!

**Rushmore:** From there, I went to university to study for an accounting degree. By this time, I had already developed a passion for software engineering, but my background was in commercial subjects. I excelled at Math, and Accounting was one of my favourite subjects. I like to think that I left university with two degrees because while there, I read many software engineering and database design books. I also watched plenty of videos and studied several programming languages. I was also interested in marketing in general and Internet marketing in particular. During my university years, I developed and maintained a free online keyword research tool called Keyword Enchanter. It wasn't open source. This was a pre-GitHub era. Back then, maintaining open-source code was less convenient than it is now.

**Feranmi:** OK. I take it you now maintain some open-source projects?

**Rushmore:** Yes, I do! Almost all of my open-source projects are in Rust. Since picking Rust up in 2015, I have published several Rust libraries to [crates.io](http://crates.io). As of today, they have a combined total download count of 15 million. Last I heard, one of the crates, publicsuffix, was said to be used at 1Password. Something I'm very proud of!

**Feranmi:** Amazing! What made you choose Rust?

**Rushmore:** When I started, I was using PHP. As I learnt more languages, however, type safety and being able to catch a lot of errors during development was very appealing to me. I also loved the improved runtime efficiency that typically comes with languages compiled ahead of time. As such, I had always been drawn to C, but its lack of memory safety scared me. So for a while, I played around with [Phalcon](https://phalcon.io/en-us), a PHP framework that compiles down to a C extension. Back then, [Zephir](https://zephir-lang.com/en), their language for writing PHP extensions, was still very young and needed more features. When I discovered Go, I decided to move to it because it was a statically typed, compiled and memory-safe language. Once Rust released v1.0 switching to it was a no-brainer for me. At a glance, it was very similar to Go, but it also had a nice package manager, something Go lacked at the time. In my opinion, it also had nicer error handling and support for generics. I fell in love with it right away.

**Feranmi:** How did you end up at SurrealDB?

**Rushmore:** I love databases. As part of my accounting degree, I took an introductory course to computer science, CS 101. Our first assignment for that course was on Structured Query Language (SQL). It was the most beautiful thing I had ever seen! I have been hooked ever since. Being an early adopter of both Go and Rust and TitanDB and RethinkDB, I was forced to write database drivers for both languages. I wrote a driver for TitanDB in Go and later re-wrote it in Rust once I switched. I also wrote a driver for RethinkDB in Rust that I have maintained since 2015. I have always had a keen interest in embed-able databases. Last year when I read about SurrealDB, an ACID-compliant database written in Rust you could embed in your app or access remotely with a SQL-like query language with support for live queries and graph querying capabilities, I knew right away I wanted to do whatever I could to help it succeed. Fortunately, I got the opportunity to join their team, something I'm very grateful for.

**Feranmi:** Cool! Can you explain a bit about what the Rust API layer is?

**Rushmore:** OK. SurrealDB is very modular in its architecture. At the very bottom are storage engines which handle the actual storage of data. SurrealDB supports a few of those. Above that is the query layer which adds all the functionality that SurrealDB comes with, making it pleasant to work with your data. On top of that layer is the API layer, which is what is accessible publicly. It makes it possible to interact with the query layer from Rust as an embedded database in your application or something you connect to remotely via a server.

**Feranmi:** That was very insightful. Thanks a lot for your time, Rushmore!

**Rushmore:** No problem, Feranmi! Thanks a lot for taking the time to talk to me.

Fascinated by what we're building? Visit our [GitHub](https://github.com/surrealdb) to learn more.
