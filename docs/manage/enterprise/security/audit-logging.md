---
position: 1
title: Audit logging
description: "Enterprise Edition audit logging: captured events, log formats, storage, and SIEM integration."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/manage/enterprise/security/audit-logging.mdx"
---

# Audit logging <Edition value="enterprise" />

The audit log pipeline in SurrealDB Enterprise emits an authoritative, identity-bound record for every authenticated action — statements, queries, transactions, RPC calls, sign-in attempts, sessions and HTTP requests. Records flow to a durable NDJSON file sink with optional tamper-evident SHA-256 hash chaining and a three-pass redactor for embedded PII.

The full pipeline reference — events captured, record shape, rotation and durability, hash chaining, redaction, overflow semantics, and pipeline self-metrics — lives under the Observability section:

- **[Audit logging reference](../../observability/audit-logging.md)** — the canonical reference for the pipeline.
- **[Configuration → Audit log knobs](../../observability/configuration.md#audit-log-knobs)** — every audit-log environment variable, including the [Compliance checklist](../../observability/configuration.md#compliance-checklist) for tamper-evident deployments.
- **[Slow-query logging](../../observability/slow-query-logging.md)** — the sister pipeline that captures the long tail of slow queries for triage.
