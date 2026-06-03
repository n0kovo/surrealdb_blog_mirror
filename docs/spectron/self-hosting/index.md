---
position: 0
title: Overview
description: Deploy and operate Spectron on your own infrastructure.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/self-hosting/index.mdx"
---

# Self-hosting

Spectron can be deployed on your own infrastructure so memory and knowledge stay under your control. The self-hosted distribution is a single Rust binary – **`spectrond`** – that connects to a SurrealDB instance and an object store. The binary holds no durable state itself (everything important lives in SurrealDB and object storage), so you can scale **api** and **worker** replicas horizontally.

## When to self-host

Self-hosting is appropriate when:

- Your data must not leave your infrastructure for compliance or privacy reasons.
- You need to customise extraction models, use self-hosted LLMs, or configure the pipeline in ways not supported by the hosted offering.
- You are building on top of an existing SurrealDB deployment and want tight integration.
- You require air-gapped or private-cloud operation.

The hosted offering at [cloud.surrealdb.com](https://cloud.surrealdb.com) handles infrastructure, upgrades, and scaling automatically. Self-hosting is an operational commitment – you are responsible for availability, backups, and upgrades.

## Deployment options

| Option | Best for |
|---|---|
| [Docker Compose](deployment/docker.md) | Local development, small teams, low-traffic deployments |
| [Kubernetes](deployment/kubernetes.md) | Production workloads, high availability, autoscaling |
| [Bare metal (systemd)](deployment/bare-metal.md) | Single-server deployments, edge, or constrained environments |

All three options use the same binary and configuration model. You can start with Docker Compose locally and deploy to Kubernetes in production without any changes to Spectron's configuration – only the infrastructure wrapper changes.

## What you need

Every Spectron deployment requires:

- **SurrealDB** – `ws://` or `wss://` endpoint. Spectron uses SurrealDB for all durable state: sessions, turns, extracted entities, knowledge nodes, API keys, and decision traces.
- **Object store** – an S3-compatible bucket, Google Cloud Storage bucket, Azure Blob container, or local filesystem path. Spectron stores the raw bytes of uploaded documents here.
- **LLM provider keys** – at least one of `OPENAI_API_KEY` or `ANTHROPIC_API_KEY`, depending on which models you configure. The extraction, reflection, and response model stages each call an LLM.

See [Architecture overview](deployment/architecture-overview.md) for how these components fit together.

## Sections in this guide

| Section | Contents |
|---|---|
| [Deployment](deployment/architecture-overview.md) | Architecture, Docker, Kubernetes, bare metal, storage |
| [Security](security/authentication.md) | Authentication, principals, scope, multi-tenancy |
| [Observability](observability/tracing.md) | Tracing, audit trails, cost tracking, live queries |
| [Operations](operations/contexts.md) | Context management, migrations, upgrades |
