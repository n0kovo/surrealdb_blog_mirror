---
title: "Introducing Nightly and Beta Rust Crates"
slug: "introducing-nightly-and-beta-rust-crates"
date: "2024-01-09T00:00:00.000Z"
categories:
  - "releases"
  - "engineering"
  - "company"
read_time: "2 min read"
summary: "We are pleased to announce two additional Rust crates, surrealdb-nightly and surrealdb-beta. These crates are designed to complement the surrealdb crate."
source: "https://surrealdb.com/blog/introducing-nightly-and-beta-rust-crates"
cover: "../../assets/8d65556c1dacb740.jpg"
---

# Introducing Nightly and Beta Rust Crates

![Introducing Nightly and Beta Rust Crates](../../assets/8d65556c1dacb740.jpg)

We are pleased to announce two additional Rust crates, `surrealdb-nightly` and `surrealdb-beta`. These crates are designed to complement the `surrealdb` crate. Starting with `v1.1.0` we plan to publish a stable release on the second Tuesday of every month. These stable releases are only published to the stable `surrealdb` crate. If you use SurrealDB in production, this is the ideal crate for you. You can add it to your project using `cargo add` or by simply adding a line like this one to your dependencies section:

```yaml
surrealdb = "1"
```

## Nightly Crate

If you prefer living on the bleeding edge, this crate is perfect for you. It follows our development branch very closely. It’s automatically published every night but only when there are new changes to the development branch. It makes it easy to test new features as an embedded library or as a client when running a nightly binary on the server.

When using nightly or beta crates, we recommend adding a line similar to this one to your dependencies section in Cargo.toml:

```yaml
surrealdb = { version = "1", package = "surrealdb-nightly" }
```

This makes it easy to switch between the three crates by simply changing the package name. You could start your development using `surrealdb-nightly` if the nightly version has a feature you want that hasn’t stabilised yet, later switch to `surrealdb-beta` once it reaches beta and finally switch to `surrealdb` once it’s stable. All this by simply changing the package name. This way you won’t have to update your feature flag names if you have features that activate SurrealDB features. For example `memory = ["surrealdb/kv-mem"]`.

## Beta Crate

Every month we will freeze features on the development branch by creating a new branch which will only receive bug fixes from that point onwards. This gives us a month to polish our releases before they hit the stable crate. Updates in that branch are pushed to the `surrealdb-beta` crate. New features in this crate are not guaranteed to reach the stable crate. Such features may be reverted to give them more time to develop if we think they are not ready to stabilise yet.

## Conclusion

The nightly and beta crates are great for testing new features and bug fixes. However, these are, by definition, pre-releases. Use them responsibly 😄.
