---
title: "The power of SurrealDB embedded"
slug: "the-power-of-surrealdb-embedded"
date: "2025-07-08T00:00:00.000Z"
categories:
  - "featured"
  - "company"
read_time: "8 min read"
summary: "SurrealDB embedded is a lightweight, secure, and AI-native database engine built in Rust, designed for intelligent, offline-first applications at the edge, supporting rich data models, schema flexibility, built-in ML inference, and fast performance."
source: "https://surrealdb.com/blog/the-power-of-surrealdb-embedded"
cover: "../../assets/494c1a0f797d3d1e.jpg"
---

# The power of SurrealDB embedded

![The power of SurrealDB embedded](../../assets/494c1a0f797d3d1e.jpg)

Embedded systems are rapidly evolving to power intelligent, offline-first applications at the edge, demanding more than traditional storage solutions. With the rise of on-device LLMs, dynamic data models, and real-time decision-making, a new kind of embedded database is needed. In this blog, we describe the power of SurrealDB embedded: a lightweight, secure, and AI-native engine built in Rust, designed to run anywhere - from browsers to IoT devices - while supporting rich data models, schema flexibility, built-in ML inference, and blazing-fast performance.

### A brief history of embedded devices

Since the early 2000s, with the emergence of cloud and mobile devices and connectivity, embedded systems have experienced a drastic change. These are specialised computing systems that are typically resource-constrained, tightly integrated with hardware, and optimised for reliability, efficiency, and real-time performance. Examples include microcontrollers in appliances, control units in cars, mobile devices, and chips in medical devices. They often run lightweight operating systems or bare-metal code and are commonly paired with embedded databases to manage local data without relying on external servers.

The technology evolution spanned from hardware platforms (microcontrollers, microprocessors, system-on-chip) to operating systems (RTOS, embedded Linux, bare-metal programming), programming languages (C and C++), and embedded databases. The latter have undergone a major transformation, led first and foremost by the rise of SQLite, and followed by a wave of innovation in local-first and analytics-driven systems.

SQLite, introduced in 2000 by D. Richard Hipp, marked a turning point. Unlike traditional relational databases, it required no server, no configuration, and was lightweight enough to run in mobile apps, browsers, and embedded devices. Thanks to its simplicity, reliability, and public domain licensing, it became the standard for local storage, used in nearly every smartphone, browser, and OS by the late 2000s.

As applications demanded more performance, scalability, and offline functionality through the 2010s, new embedded databases emerged. LevelDB and later \*\*\*\*RocksDB brought fast, low-level key-value storage optimised for write-heavy operations.

In the 2020s, embedded databases began serving not just transactional needs but also analytical ones. DuckDB, for example, allows developers to run complex analytical SQL queries entirely on-device, making it ideal for edge computing and interactive data science. Meanwhile, projects like Replicache and ElectricSQL are extending SQLite’s reach with live sync, peer-to-peer collaboration, and distributed edge storage.

Overall, the past 25 years have seen embedded databases evolve from lightweight data stores into essential infrastructure for modern apps, offering developers power, flexibility, and control closer to the user than ever before.

### Enter Rust 🦀

Over the past decade, Rust has surged to the forefront of systems programming, transforming how developers approach performance-critical software across domains, from operating systems and blockchain clients to game engines and cloud infrastructure. Praised for its unparalleled combination of safety, speed, and expressiveness, Rust has become one of the fastest-growing programming languages on GitHub for several years running. This reflects a groundswell of global developer adoption and ecosystem maturity (see [Why Rust is the most admired language among developers](https://github.blog/developer-skills/programming-languages-and-frameworks/why-rust-is-the-most-admired-language-among-developers/)). It has earned the trust of engineers building everything from web browsers (Mozilla Firefox) to cloud runtimes (AWS Firecracker, Microsoft Azure), cryptographic libraries and, no surprise, databases. SurrealDB was rebuilt from Go to Rust precisely for these reasons (see [Why we are betting on Rust](/blog/why-we-are-betting-on-rust) to learn more).

A significant percentage of cybersecurity vulnerabilities (typically estimated between 60% and 70%) are related to memory safety issues, such as buffer overflows, use-after-free, and null pointer dereferencing. These vulnerabilities are particularly common in software written in memory-unsafe languages like C and C++, which allow direct manipulation of memory without built-in safeguards. [[1]](https://msrc.microsoft.com/blog/2019/07/we-need-a-safer-systems-programming-language/) [[2]](https://www.chromium.org/Home/chromium-security/memory-safety/)

But perhaps its most profound impact is now unfolding in the embedded systems world, where Rust is rewriting the rules of what’s possible. Traditionally dominated by C and C++, embedded development has long required developers to navigate dangerous terrain riddled with memory corruption bugs, race conditions, and manual resource management. Rust’s fearless concurrency, zero-cost abstractions, and compile-time guarantees of memory safety are proving transformational.

Adoption is accelerating across automotive, aerospace, industrial control, and IoT, with industry leaders like Bosch, Toyota, Google, Microsoft, and Amazon integrating Rust into their embedded stacks. Community-driven frameworks such as RTIC, Embassy and Ferrocene, along with the support of the Embedded Rust Working Group, have further cemented Rust’s viability for real-time, resource-constrained environments.

The language’s strategic importance was underscored by the [White House’s National Cybersecurity Strategy](https://bidenwhitehouse.archives.gov/oncd/briefing-room/2024/02/26/press-release-technical-report/), which explicitly called for a shift toward memory-safe programming languages like Rust to reduce systemic vulnerabilities in critical software infrastructure. In safety- and security-critical domains, this shift is not just prudent, it’s essential. As embedded systems continue to spread into vehicles, medical devices, homes, and factories, Rust stands as a bold and battle-tested foundation for building the next generation of resilient, high-performance, and future-proof software at the edge.

### The rise of embedded LLMs

We got this far without mentioning AI (pat on the back!), but now is the time. Embedded LLMs have also rapidly evolved from cloud-dependent systems to models capable of running directly on local devices. This transformation, starting around 2023, was driven by advances in quantisation, model optimisation, and powerful runtimes like llama.cpp, GGML, and MLC LLM. Models such as LLaMA, Mistral, Phi-3, and DeepSeek were optimised to run with limited memory and compute, making them viable on consumer laptops, smartphones, and even Raspberry Pi-class devices.

Simultaneously, hardware improvements, including high-efficiency NPUs in mobile chips (Apple, Qualcomm) and increasingly capable GPUs from NVIDIA, made local inference faster and more accessible. Today, embedded LLMs like Gemini Nano and DeepSeek-MoE power assistants, copilots, and intelligent UIs with low latency and full offline capability, marking a decisive shift toward private, local-first AI at the edge.

### Why the edge needs a new database

As LLMs and intelligent applications move to the edge, traditional embedded databases fall short. These new workloads demand more than just lightweight storage - they require dynamic, contextual, and low-latency data systems that can keep up with real-time AI inference, evolving schemas, and autonomous decision-making. A new class of embedded database is needed, one designed for modern intelligence at the edge.

Key requirements include:

- **Low-latency querying:** embedded systems must respond in real time, often within milliseconds. Any delay in reading or updating data directly impacts perceived intelligence and responsiveness.
- **Rich, flexible data types and models:** support for documents, relationships, and nested structures is essential for representing the real-world context LLMs need to reason over.
- **Flexible schema evolution:** AI-driven systems learn and adapt; the database must support fluid, evolving data without manual schema changes or downtime.
- **Embedded and offline by default:** cloud round-trips are often infeasible in edge environments. The database must operate fully offline, while enabling optional sync when available.
- **Secure multi-user access:** applications and agents may run on shared devices or multi-tenant contexts. Fine-grained access control is necessary, even in local deployments.
- **Queryable context for LLMs:** embedded LLMs need fast, structured access to memory, knowledge, and interaction history. The database must serve as a real-time context layer.
- **Lightweight and portable:** designed to run efficiently on constrained hardware - laptops, smartphones, edge devices - without heavyweight dependencies.

As intelligent systems continue to decentralise, the edge needs databases that can act as real-time memory, knowledge base, and decision hub, not just storage.

### **Meet SurrealDB embedded**

SurrealDB is a full-featured, AI-native database engine built in Rust which is a perfect fit for the edge. With a minimal footprint and powerful capabilities, it enables developers to deploy rich, LLM-integrated systems on laptops, browsers, IoT devices, or air-gapped environments, without compromising on functionality.

Some of it’s core features are:

- **Rust-built and memory safe:** no dependencies, cross-compiles to ARM, RISC-V, x86, and WebAssembly.
- **Lightweight:** single binary including database engine with multi-model support, vector index, access control, and sync protocol.
- **Universal deployments:** the same database can run embedded, in single node or in a highly scalable deployment in the cloud. Read more about [Surreal\<Any>](/blog/introducing-surrealany-dynamic-support-for-any-engine-in-rust).
- **Multi-model support:** SurrealDB supports relational, document, time-series and graph data with full-text and vector search support, geospatial capabilities, embedded functions, and more in a single natively integrated query language.
- **Built-in ML inference:** load ONNX, run transformer blocks locally, and call them from with [SurrealML](https://github.com/surrealdb/surrealml) (it uses the same key value store and the ONNX runtime is embedded into the Rust binary).
- **Blazing fast performance:** not only because using one database is faster than stitching together multiple systems, but also because [how SurrealDB stores records enables](/blog/the-life-changing-magic-of-surrealdb-record-ids) real-time performance.

SurrealDB embedded powers on-device applications across a range of industries such as automotive (Volvo), retail (Walmart), and others such as manufacturing and government.

Its multi-model capabilities allow you to mix relational and document data models with file support into knowledge graphs and use vector search to power embedded LLMs. You can take advantage of SurrealDB’s robust security for edge deployments, such as row-level access controls and end user authentication.

Embedded systems now need more than just storage, they need a flexible, AI-ready data layer. SurrealDB embedded brings that capability to the edge today.

### Ready to build? Get started with SurrealDB Embedded

See our [Embedding SurrealDB Docs](/docs/surrealdb/embedding). SurrealDB can be [embedded in Rust](/docs/surrealdb/embedding/rust), [in JavaScript](/docs/surrealdb/embedding/javascript), and others.

[[1] We need a safer systems programming language](<%5Bhttps://msrc.microsoft.com/blog/2019/07/we-need-a-safer-systems-programming-language/%5D(https://msrc.microsoft.com/blog/2019/07/we-need-a-safer-systems-programming-language/)>) (Microsoft, 2019)

[[2] Chromium Security Memory Safety](<%5Bhttps://www.chromium.org/Home/chromium-security/memory-safety/%5D(https://www.chromium.org/Home/chromium-security/memory-safety/)>) (Google, 2020)
