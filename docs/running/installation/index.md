---
position: 1
title: Installation
description: "Install the surreal command-line tool and the SurrealDB database on macOS, Windows and Linux. Nightly builds and the install script's options are covered too."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/running/installation/index.mdx"
---

# Installation

If you are not ready to install anything yet, start with the [SurrealDB Studio Sandbox](../sandbox.md) or [SurrealDB Cloud](../cloud.md) as described in the [Running overview](../overview.md).

One of the most popular ways to get started with SurrealDB is to install and run it as a standalone database service, allowing any number of clients to connect to it and interact with the data.

You install one command, `surreal`. It installs the database as a component, keeps it current, and runs it with `surreal db <command>`. The same command installs and runs the other [components](../../explore/cli/components.md), such as `cloud` for SurrealDB Cloud. This section covers installing it on your local machine for development or as a production database.

The current stable version of SurrealDB is <a href='/releases'> *(latest)*</a>.

## Installation steps

The install script is the same on every platform: it installs `surreal` and, by default, the database. The pages below give the steps for each operating system, including the package managers that install the database on its own. [Install the SurrealDB CLI](../../explore/cli/install.md) lists every option of the install script.

You can install SurrealDB on the following operating systems:

- **[macOS](macos.md)**
- **[Windows](windows.md)**
- **[Linux](linux.md)**

## SurrealDB Cloud

Running and maintaining your own database can be a time consuming task. That's why we offer [SurrealDB Cloud](../../manage/instances/index.md), a fully managed database service that allows you to focus on building your applications without worrying about the underlying infrastructure.

## Nightly builds

- [Nightly](nightly.md) - install an unreleased build to try changes early
