---
title: "Why we are betting on Rust"
slug: "why-we-are-betting-on-rust"
date: "2024-03-13T00:00:00.000Z"
categories:
  - "engineering"
  - "company"
read_time: "5 min read"
summary: "The best way to predict the future is to create it."
source: "https://surrealdb.com/blog/why-we-are-betting-on-rust"
cover: "../../assets/b7657667e95c2f78.jpg"
---

# Why we are betting on Rust

![Why we are betting on Rust](../../assets/b7657667e95c2f78.jpg)

SurrealDB has been built from the ground up to be the ultimate database for developers who want to build tomorrow's applications.

In order to build the future of databases that can support the future of applications, we needed the future of low-level programming languages. We believe this language is Rust, which quite literally has allowed us to bring the [`future`](/docs/surrealql/datamodel/futures) to our SQL-like query language SurrealQL, inspired by the [Rust future.](https://doc.rust-lang.org/std/future/trait.Future.html)

## Go slow to go fast

Front and centre on our home page, you'll see [these three sentences](/):

- Develop easier.
- Build faster.
- Scale quicker.

This is not only what SurrealDB can do for your application, but what Rust does for SurrealDB. Due to Rust's notoriously steep learning curve, develop easier and build faster might not be the first thing that comes to mind when you think of using Rust.

However, the ways Rust supports you to think differently, through using the borrow checker, lifetimes and more, pays compounding interest as your application starts achieving a phenomenal balance of safety and performance.

Yes, you may not be as fast going from 0 to 1 in Rust as in some other languages, but [it's easier than you think.](https://opensource.googleblog.com/2023/06/rust-fact-vs-fiction-5-insights-from-googles-rust-journey-2022.html) This might however mean prototyping in a different language and then re-writing it in Rust once you see a long-term potential for the project. [SurrealDB itself was first prototyped in Go and then entirely re-written in Rust.](https://www.youtube.com/watch?v=Chl8IdMxr4Y)

The key point here is that once you pay the upfront cost of learning Rust, you can go further faster, or as is often said: go slow to go fast.

Now, before we go any further, we need to address the question I'm sure many of you will have: why not Zig or other newer languages?

While it's true that you can build a database with Zig or other newer languages, they don't have the features of Rust when it comes to memory safety by default while not having a garbage collector for the highest performance. However, there is one thing that stands out more than any feature difference.

## Critical adoption

There is no denying that Rust has captured the hearts and minds of the developer community, having topped the chart as [“the most admired programming language”](https://survey.stackoverflow.co/2023/#section-admired-and-desired-programming-scripting-and-markup-languages) in Stack Overflow’s annual developer survey for 8 years in a row. Far from being just admired, it's also one of the [fastest-growing languages on GitHub](https://octoverse.github.com/2022/top-programming-languages).

Rust has even achieved adoption where no other language aside from C has been, not even C++, namely the [Linux kernel](https://www.phoronix.com/news/Linux-6.6-Rust-Changes).

This begs the question, why?

As [Software Engineer Wedson Almeida Filho said](https://security.googleblog.com/2021/04/rust-in-linux-kernel.html)

> We feel that Rust is now ready to join C as a practical language for implementing the kernel. It can help us reduce the number of potential bugs and security vulnerabilities in privileged code while playing nicely with the core kernel and preserving its performance characteristics.

To put this into perspective, a talk at the [2019 Linux Security Summit](https://static.sched.com/hosted_files/lssna19/d6/kernel-modules-in-rust-lssna2019.pdf) showed that memory safety issues are estimated to account for 65-88% of security vulnerabilities in major systems, including Android and Ubuntu.

This also aligns with [Microsoft's experience](https://msrc.microsoft.com/blog/2019/07/we-need-a-safer-systems-programming-language)

> ~70% of the vulnerabilities Microsoft assigns a CVE each year continue to be memory safety issues

This goes to show how even after decades of development from some of the best engineers using C and C++ best practices, issues such as accessing memory that has already been freed, data races, and other problems still persist. Therefore it's hard to claim it's just skill issues, but rather more likely fundamental issues with the languages being used.

With this context in mind, you can see why [Microsoft Azure CTO Mark Russinovich said](https://www.theregister.com/2022/09/20/rust_microsoft_c)

> Speaking of languages, it's time to halt starting any new projects in C/C++ and use Rust for those scenarios where a non-GC language is required. For the sake of security and reliability. the industry should declare those languages as deprecated.

This trust in Rust does not come from nowhere, there has been a tremendous amount of work put into making Rust fully usable in safety-critical environments. This can be seen in Rust's recent qualification under the ISO 26262 and IEC 61508 standards through the [Ferrocene toolchain](https://ferrous-systems.com/blog/officially-qualified-ferrocene) developed by Ferrous Systems.

You might have also heard that governments are taking notice of these developments, such as the [US White House Office of the National Cyber Director (ONCD).](https://www.whitehouse.gov/wp-content/uploads/2024/02/Final-ONCD-Technical-Report.pdf) This office issued a report last month (February 2024) recommending a move to memory-safe programming languages and pointing to Rust as an example of a potential replacement for C and C++ in safety-critical space systems.

## It's not rocket science

While databases are not life-critical space systems, they often play a life-critical role in organisations. You want to keep your data safe and secure because if you lose your data, you can lose your business.

Therefore if between 65-88% of security vulnerabilities in major systems can be caused by memory issues, it's not rocket science to understand why we are betting on Rust to keep your data as safe as possible.

At SurrealDB we are passionate about building the future we want to see in the world.

If you want to be a part of building this future, you can [join our exceptional community](https://discord.gg/surrealdb) and contribute to shaping the future of Rust and SurrealDB.

If you want to be a part of experiencing this future, [get started with SurrealDB](/docs/surrealdb/introduction/start).

Part of the change we want to see in the world is making Rust more accessible, which is why we started the [Women in Rust meet-up](https://www.meetup.com/women-in-rust), where women can come together to learn and build skills in Rust!
