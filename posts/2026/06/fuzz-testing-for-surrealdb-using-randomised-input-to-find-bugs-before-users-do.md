---
title: "Fuzz testing for SurrealDB: using randomised input to find bugs before users do"
slug: "fuzz-testing-for-surrealdb-using-randomised-input-to-find-bugs-before-users-do"
date: "2026-06-11T07:26:28.000Z"
categories:
  - "engineering"
read_time: "8 min read"
summary: "A good choice to complement unit and integration tests, fuzz testing lets you use semi-random data to discover obscure bugs before users do."
source: "https://surrealdb.com/blog/fuzz-testing-for-surrealdb-using-randomised-input-to-find-bugs-before-users-do"
cover: "../../assets/41bec25f73069b33.jpg"
---

# Fuzz testing for SurrealDB: using randomised input to find bugs before users do

![Fuzz testing for SurrealDB: using randomised input to find bugs before users do](../../assets/41bec25f73069b33.jpg)

In this post we will take a quick look at one of the methods we began using in the run-up to SurrealDB 3.0 to prioritise stability and performance: fuzz testing.

Fuzz testing is a good choice for projects to use to complement unit and integration tests. Instead of asserting behaviour on a fixed set of inputs, a fuzz harness feeds semi-random data into your code and watches for crashes, panics, timeouts, and other failure modes. This makes it easier to stumble upon edge cases you might not have considered before a user hits them in production.

Fuzz testing itself is not brand new, but it became much more practical at scale after Google launched [OSS-Fuzz](https://google.github.io/oss-fuzz/) in 2016, partly in response to the Heartbleed vulnerability in OpenSSL:

> OSS-Fuzz was launched in 2016 in response to the Heartbleed vulnerability, discovered in OpenSSL, one of the most popular open source projects for encrypting web traffic. The vulnerability had the potential to affect almost every internet user, yet was caused by a relatively simple memory buffer overflow bug that could have been detected by fuzzing—that is, by running the code on randomized inputs to intentionally cause unexpected behaviors or crashes. At the time, though, fuzzing was not widely used and was cumbersome for developers, requiring extensive manual effort.

Fuzz testing tools were added to Rust as it began to grow as a language in the late 2010s and early 2020s. As [this video](https://www.youtube.com/watch?v=qUu1vJNg8yo) from RustConf 2021 puts it:

> Sometimes you can come up with an easy method to verify correctness, but you struggle with finding actual examples for the unit tests. You know that "For all x it holds that …", but you can't come up with good possibilities for x. This is where relying on fuzzing can quickly drive forward development through providing you with some real examples of what your code doesn't yet cover, allowing you to quickly cover a lot of ground.

Fuzz testing is a good fit for projects that reach a certain level of complexity or are reimplementing a lot of functionality, and that was the case for us. We added fuzz testing in the run-up to SurrealDB 3.0 because of the large number of structural changes to the database itself. Those changes are best covered in a later post, but if you are curious you can start with [this PR](https://github.com/surrealdb/surrealdb/pull/5977) from last May, which kicked off the process with a split of SurrealDB's AST and logical plan.

## Fuzz testing setup

The main way to run fuzz tests in Rust is through the [cargo-fuzz](https://github.com/rust-fuzz/cargo-fuzz) crate.

To build and run fuzz tests locally you need the nightly compiler, cargo-fuzz itself, and a build of surrealdb-core with the `arbitrary` feature enabled. The [fuzz/README.md](https://github.com/surrealdb/surrealdb/blob/main/fuzz/README.md)) page in that directory has more information on installation and some typical commands such as:

```surrealql
cargo +nightly install cargo-fuzz
cargo +nightly fuzz build --fuzz-dir ./fuzz fuzz_executor
cargo +nightly fuzz run --fuzz-dir ./fuzz fuzz_executor
```

There is also a [cargo-fuzz tutorial](https://rust-fuzz.github.io/book/cargo-fuzz/tutorial.html) which shows how to feed raw bytes into a target, starting with very simple examples:

```rust
#![no_main]

use libfuzzer_sys::fuzz_target;

fuzz_target!(|data: &[u8]| {
    if let Ok(s) = std::str::from_utf8(data) {
        let _ = url::Url::parse(s);
    }
});
```

Running that for long enough would eventually lead to output that resulted in [this bug](https://github.com/servo/rust-url/pull/108) a long time ago and has since been fixed.

The `arbitrary` crate mentioned above has a [derive macro](https://docs.rs/arbitrary/latest/arbitrary/trait.Arbitrary.html#deriving-arbitrary) that allows your own types to implement a trait called `Arbitrary` so that it can be used in fuzz testing. This trait can be implemented manually if you prefer.

## A simple example

Let's put a quick example of our own together to get an idea of how it works with something (a little) more complex than just some bytes. The code below shows one struct that holds two enums that represents something a little bit similar to a query language. We'll say that you can `Define` or `Remove`, and a query can be done on a `Table` or a `Record`.

We'll insert a bug in which you should not be able to remove a record or a table (because you delete them, not remove them), but the code doesn't account for that and assumes that this is an unreachable pattern. Obviously the code below is so simple that anyone can eyeball it to see where the problem is, but in a real repo with oodles and oodles of code a function like `fn compute() `below would be buried under so much other logic that a bug could easily slip through.

```rust
#![no_main]

use arbitrary::Arbitrary;
use libfuzzer_sys::fuzz_target;

#[derive(Arbitrary, Debug)]
struct Statement {
    clause1: Clause1,
    clause2: Clause2,
}

#[derive(Arbitrary, Debug)]
enum Clause1 {
    Define,
    Remove,
}

#[derive(Arbitrary, Debug)]
enum Clause2 {
    Table,
    Record,
}

impl Statement {
    fn compute(&self) -> String {
        match (&self.clause1, &self.clause2) {
            (Clause1::Define, Clause2::Table) => format!("{:?} {:?}", self.clause1, self.clause2),
            (Clause1::Remove, Clause2::Table) => format!("{:?} {:?}", self.clause1, self.clause2),
            _ => unreachable!("Something went wrong with input {:?}", &self),
        }
    }
}

fuzz_target!(|value: Statement| {
    let _ = value.compute();
});
```

Because the invalid `Remove` + `Record` combination is easy for the fuzzer to reach, `cargo +nightly fuzz run` typically finds it almost immediately:

> thread '<unnamed>' (1305219) panicked at src/main.rs:29:18:internal error: entered unreachable code: Something went wrong with input Statement { clause1: Remove, clause2: Record }

## Actual examples

With the basics out of the way, let's look at some real examples from the SurrealDB crate. Many of the structs and enums in it are quite simple and just derive the `Arbitrary` trait using an attribute.

```rust
#[cfg_attr(feature = "arbitrary", derive(arbitrary::Arbitrary))]
pub struct DatabaseId(pub u32);

#[cfg_attr(feature = "arbitrary", derive(arbitrary::Arbitrary))]
pub enum ApiMethod {
    Delete,
    #[default]
    Get,
    Patch,
    Post,
    Put,
    Trace,
}

#[cfg_attr(feature = "arbitrary", derive(arbitrary::Arbitrary))]
pub enum EventKind {
    Sync,
    Async {
        retry: u16,
        max_depth: u16,
    },
}
```

The `Arbitrary` trait is manually implemented in a number of places as well. We can see why this is useful if we take a look at the [trait signature](https://docs.rs/arbitrary/latest/arbitrary/trait.Arbitrary.html) for the `Arbitrary` trait. It unsurprisingly contains a few methods, of which `.arbitrary()` is the main one.

```rust
pub trait Arbitrary<'a>: Sized {
    fn arbitrary(u: &mut Unstructured<'a>) -> Result<Self>;

    fn arbitrary_take_rest(u: Unstructured<'a>) -> Result<Self> { ... }
    fn size_hint(depth: usize) -> (usize, Option<usize>) { ... }
    fn try_size_hint(
        depth: usize,
    ) -> Result<(usize, Option<usize>), MaxRecursionReached> { ... }
}
```

[Unstructured](https://docs.rs/arbitrary/latest/arbitrary/struct.Unstructured.html) includes helpers such as [arbitrary_len()](https://docs.rs/arbitrary/latest/arbitrary/struct.Unstructured.html#method.arbitrary_len), [int_in_range()](https://docs.rs/arbitrary/latest/arbitrary/struct.Unstructured.html#method.int_in_range), and [choose()](https://docs.rs/arbitrary/latest/arbitrary/struct.Unstructured.html#method.choose)). The SurrealDB codebase uses all three of these: `int_in_range` to pick enum variants, `arbitrary_len` to size vectors, and `choose` when selecting from a collection of already-built values (for example, field selectors in a `SELECT` list).

Inside the SurrealDB codebase is a function called `plain_idiom()`, which builds idioms whose first segment is either a field name or a graph lookup. That helper is reused anywhere the grammar expects a plain idiom (e.g. `UNSET` targets, assignment places, and similar positions), not the full range of `Part` variants.

```rust
impl<'a> Arbitrary<'a> for Data {
    fn arbitrary(u: &mut arbitrary::Unstructured<'a>) -> arbitrary::Result<Self> {
        let r = match u.int_in_range(0u8..=5)? {
            0 => Data::SetExpression(atleast_one(u)?),
            1 => Data::UnsetExpression(arb_vec1(u, |u| plain_idiom(u))?),
            2 => Data::PatchExpression(u.arbitrary()?),
            3 => Data::MergeExpression(u.arbitrary()?),
            4 => Data::ReplaceExpression(u.arbitrary()?),
            5 => Data::ContentExpression(u.arbitrary()?),
            _ => unreachable!(),
        };
        Ok(r)
    }
}

pub fn plain_idiom<'a>(u: &mut arbitrary::Unstructured<'a>) -> arbitrary::Result<Idiom> {
    let res = match u.int_in_range(0..=1)? {
        0 => Part::Field(u.arbitrary()?),
        1 => Part::Graph(u.arbitrary()?),
        _ => unreachable!(),
    };
    let mut res = vec![res];
    let len = u.arbitrary_len::<Part>()?;
    res.reserve(len);
    for _ in 0..len {
        res.push(u.arbitrary()?);
    }
    Ok(Idiom(res))
}
```

## SurrealDB fuzz harnesses

The [fuzz/](https://github.com/surrealdb/surrealdb/tree/main/fuzz) crate in the SurrealDB repo defines four libFuzzer targets:

1. `fuzz_sql_parser`: takes a raw `&str` as input, parses legacy syn::parse and must not crash on arbitrary text.
1. `fuzz_executor`: takes semicolon-separated SurrealQL as input, executes an in-memory datastore capped at 500 statements with a 5-second per command timeout.
1. `fuzz_structured_executor`: takes `Ast` via `Arbitrary` as input, runs Datastore::process on generated ASTs
1. `fuzz_format`: takes `Ast` via `Arbitrary` as input, runs a round troup from `Ast` to `to_sql()` and reparses, panicking if formatted SurrealQL no longer parses.

Dictionary files like fuzz_executor.dict and fuzz_sql_parser.dict\` seed the fuzzer with SurrealQL keywords to reach interesting parser and executor paths faster.

There is a separate harness for the newer parser crate (more on that in an upcoming blog post!!) at [surrealdb/parser/fuzz/](https://github.com/surrealdb/surrealdb/tree/main/surrealdb/parser/fuzz), which parses arbitrary strings through `surrealdb_parser::Parser` and exercises error rendering.

## When fuzz testing is used at SurrealDB

Together, the string-based and AST-based targets cover both "random bytes that might look like SQL" and "structured queries that are already syntactically plausible", which catches different failure classes.

Since one fuzz test is never guaranteed to return the same result as another, we do not run open-ended fuzz campaigns on every pull request. Running fuzz testing on each PR is never recommended, because:

- A long fuzz run might find a new crash one day that did not appear on another, which would block unrelated merges.
- Some findings might involve a security vulnerability that should not be made public until a fix has been added.

What we do run instead in CI is a lighter check: a [fuzzing workflow](https://github.com/surrealdb/surrealdb/blob/main/.github/workflows/fuzzing.yml) builds all harnesses on a daily schedule (and on demand), and verifies that our [OSS-Fuzz](https://google.github.io/oss-fuzz) project still compiles. OSS-Fuzz then runs continuous fuzzing against the parser and executor upstream. You can see [SECURITY.md](https://github.com/surrealdb/surrealdb/blob/main/SECURITY.md) for more details on how we handle security-relevant findings and disclosure deadlines.

Locally, engineers run `cargo +nightly fuzz run` when developing or reducing a crash to a minimal reproducer. Findings from those runs have fed into substantial fix PRs such as [PR #6595](https://github.com/surrealdb/surrealdb/pull/6595), which introduced `Arbitrary` implementations so the formatter could be fuzzed for parse-round-trip bugs, and [PR #6626](https://github.com/surrealdb/surrealdb/pull/6626), which addressed a batch of parser, formatting, and parameterisation issues surfaced by that work.

## Results

Fuzz testing has not replaced our language tests or integration suite, but it has been a productive suite that has pointed out defects in SurrealQL formatting, parser edge cases, and executor panics on malformed or unusual ASTs.

The `fuzz_format` target in particular encodes an invariant we care about: anything the engine accepts as an AST should survive a format-and-reparse cycle. Breakages there often indicate ambiguous syntax, incorrect `ToSql` output, or parser regressions that unit tests with hand-written queries did not cover.

Quantifying an exact bug count is difficult because fixes land across many PRs and some crashes share a root cause, but the two PRs above alone bundled dozens of related parser and formatting corrections discovered through structured AST fuzzing. That is exactly the outcome we wanted from investing in harnesses before the 3.0 release: surfacing sharp edges internally, with OSS-Fuzz providing continuous coverage after merge.

## Get in touch

Questions or comments about how we use fuzz testing or SurrealDB in general? Feel free to drop by our [Discord community](https://discord.com/invite/surrealdb) or [main repo](https://github.com/surrealdb/surrealdb).

If you'd like to give SurrealDB a spin, you can do so now at [app.surrealdb.com](https://app.surrealdb.com/) to begin queries in your browser, no installation required. If you'd like to save that data without needing to install, just click on Sign in on the top right to save it to a free [SurrealDB Cloud](https://surrealdb.com/cloud) instance of your own - all it requires is an email address.
