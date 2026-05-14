---
title: "Introducing our new monthly release schedule"
slug: "introducing-our-new-monthly-release-schedule"
date: "2024-01-12T00:00:00.000Z"
categories:
  - "releases"
  - "company"
read_time: "5 min read"
summary: "We are excited to announce a change in our product release schedule, with a regular monthly release cycle, allowing developers and organisations to build on top of SurrealDB, with predictable timelines for software improvements and fixes."
source: "https://surrealdb.com/blog/introducing-our-new-monthly-release-schedule"
cover: "../../assets/1ab7b4bb3fcaa5e8.jpg"
---

# Introducing our new monthly release schedule

![Introducing our new monthly release schedule](../../assets/1ab7b4bb3fcaa5e8.jpg)

## Introduction

Over the course of the last 18 months, SurrealDB product releases have been feature-driven, rolling out updates as and when they were ready. This approach, while flexible, often led to unpredictable release dates which could cause challenges for users of the database, and engineers who develop against our embedded Rust SDK.

In our pursuit of improvement and efficiency, we are excited to announce a significant shift in our product release schedule. Taking inspiration from the Rust programming language’s release train model, we are transitioning to a more structured, monthly release cycle. This process will ensure that we release often, with predictable updates and product patches, allowing developers and organisations to build on top of SurrealDB, with predictable timelines for software improvements and fixes.

With this new release cycle, on the second Tuesday of each month, a new beta version of SurrealDB will be released, allowing users to test and update their software locally and in continuous integration environments, before the stable release of that version. On the second Tuesday of the following month, the beta release will be promoted to a stable release version, at which time a new beta version will be released.

## Release channels

With this new approach to releases there are now three _release channels_ for the SurrealDB database server, and SurrealDB Rust client.

- Nightly (along with a [`surrealdb-nightly`](https://crates.io/crates/surrealdb-nightly) Rust crate)
- Beta (along with a [`surrealdb-beta`](https://crates.io/crates/surrealdb-beta) Rust crate)
- Stable (available with the [`surrealdb`](https://crates.io/crates/surrealdb) Rust crate)

Most developers and organisations will primarily use the stable release channel, but those who want to try out future or new experimental features may use the beta or nightly channels.

Every night a new nightly version of the crate, and of the database server are released, both as a downloadable binary, and as an embeddable library. On the second Tuesday of each month, a new beta release is made consisting of the new features and improvements available in the nightly releases. Over the course of the next month, a number of further beta releases will be made as features are stabilised. On the second Tuesday of the following month, the beta release becomes stable, ensuring users can upgrade to the latest stable version.

Here’s an example of how the development and release process works. Each night, a new nightly version of the SurrealDB server and library are produced. Every day is a release day, and these releases are created by our release infrastructure automatically. So as time passes, our releases look like this, once a night:

```syntax
nightly: * - - * - - *
```

On the second Tuesday of every month, we build and deploy a new release. The beta branch of the SurrealDB repository branches off from the main branch from which the nightly releases are made. Now, there are two releases:

```syntax
nightly: * - - * - - *
                     |
beta:                *
```

Some SurrealDB users will actively test against the beta release in continuous integration environments to help discover any possible regressions. In addition, the beta release can be used to develop applications locally, to ensure that future functionality can be used within projects. In the meantime, there’s still a nightly release every night:

```syntax
nightly: * - - * - - * - - * - - *
                     |
beta:                *
```

Let’s say a regression is found. Good thing we had some time to test the beta release before the regression snuck into a stable release! The fix is applied to the main branch, so that the nightly release is fixed, and then the fix is backported to the beta branch, and a new release of beta is produced:

```syntax
nightly: * - - * - - * - - * - - * - - *
                     |
beta:                * - - - - - - - - *
```

On the second Tuesday of the following month, after the beta was created, it’s time for a stable release. The stable branch is now produced from the beta branch:

```syntax
nightly: * - - * - - * - - * - - * - - * - * - *
                     |
beta:                * - - - - - - - - *
                                       |
stable:                                *
```

We now have a new stable release of SurrealDB! Which is great. In addition however, we also need a new beta of the next version of SurrealDB. So after stable branches off of beta, the next version of beta branches off of nightly again:

```syntax
nightly: * - - * - - * - - * - - * - - * - * - *
                     |                         |
beta:                * - - - - - - - - *       *
                                       |
stable:                                *
```

In a similar manner to Rust's release train model which occurs every 6 weeks, the SurrealDB release train will guarantee a timely and reliable release progression. This is called the 'train model' because every month, a new release 'leaves the station', but still has to take a journey through the beta channel before it arrives as a stable release.

## Why the Change?

The unpredictability of our current process sometimes led to prolonged periods without updates, followed by a flood of changes. This irregularity can be disorienting and inconvenient for developers and organisations building on top of SurrealDB. Monthly releases strike a balance between the rapid iteration of continuous delivery and the stability of longer release cycles. They allow us to incorporate user feedback more swiftly and maintain a consistent development pace. Regular releases will provide our users with a predictable schedule, allowing them to plan for and adapt to new changes more effectively. This model enables us to iterate quickly and incorporate user feedback into subsequent releases, significantly improving the overall quality of the SurrealDB platform.

## Summary

Our goal is to make our product more reliable and user-friendly. We expect this change to significantly enhance our ability to meet and exceed user expectations. We believe this new monthly release schedule will bring a new level of efficiency and predictability to our product development. We're excited about this change and confident it will bring about positive outcomes for both our team and our users.

We would love to hear your thoughts on this new approach. Please feel free to provide feedback, subscribe to our updates, or join our community forum to engage in further discussion.
