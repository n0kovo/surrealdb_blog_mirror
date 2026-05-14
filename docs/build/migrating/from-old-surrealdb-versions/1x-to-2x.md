---
position: 2
title: 1.x to 2.x
description: This guide will help you upgrade your current SurrealDB installation to the latest `2.x` release.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/build/migrating/from-old-surrealdb-versions/1x-to-2x.mdx"
---

# Upgrading from `1.x` to `2.x`

The `2.0.0` release of SurrealDB includes [many new features, improvements, and bug fixes](/releases#v2-0-0). However, due to this there are some breaking changes that you should be aware of when upgrading.

This guide will help you upgrade your current SurrealDB installation to the latest `2.x` release.

## Breaking changes

### Datastore
- The underlying approach for storing record IDs and ranges has changed
  - [Record IDs now support storing UUIDs instead of strings](https://github.com/surrealdb/surrealdb/pull/4491)
  - [Ranges are now their own value as suppose to being available as just record id ranges](https://github.com/surrealdb/surrealdb/pull/4506)

### SurrealQL
- The `UPDATE` statement no longer creates records if these are missing. Instead, use the new [UPSERT](../../../reference/query-language/statements/upsert.md) statement for this behaviour.
- The `file://` connection protocol has been deprecated in favour of the more explicit `rocksdb://` protocol.
- The `DEFINE SCOPE` statement has been dropped in favor for the new [`DEFINE ACCESS TYPE RECORD`](../../../reference/query-language/statements/define/access/record.md) statement
  - `DEFINE TOKEN` definitions defined under scopes are now integrated into `DEFINE ACCESS TYPE RECORD`.
- Some functions have been renamed for clarity
  - `meta::tb()` -> [`record::tb()`](../../../reference/query-language/functions/database-functions/record.md)
  - `meta::id()` -> [`record::id()`](../../../reference/query-language/functions/database-functions/record.md)
  - `string::endsWith()` -> [`string::ends_with()`](../../../reference/query-language/functions/database-functions/string.md)
  - `string::startsWith()` -> [`string::starts_with()`](../../../reference/query-language/functions/database-functions/string.md)

### Authentication and headers
- Authentication is now enabled by default as you previously would with `--auth`. The [`--unauthenticated`](../../../reference/cli/surrealdb-cli/commands/start.md#unauthenticated-mode) flag is now required in order to provide the previous default behavior.
- Specifying the level on which credentials will be authenticated is now required when connecting to SurrealDB. By default, this level will be root. This can be provided with the `--auth-level` flag in the CLI or the `surreal-auth-ns` and `surreal-auth-db` headers in the HTTP REST API.
- SurrealDB now listens only for connections from the local machine unless another interface (e.g. 0.0.0.0) is provided via the `--bind` command line argument.
- SurrealDB now does not print secrets in response to `INFO` statements. The values of the secrets will appear as `[REDACTED]` to prevent accidental leakage. The export functionality will still print the values of the secrets. An `UNREDACTED` clause will be added soon to provide the previous behavior.
- Headers used to communicated via HTTP with SurrealDB now require the `surreal-` prefix. For example, the legacy `ns` and `db` headers are now `surreal-ns` and `surreal-db`.

## Upgrading your data

A new [`surreal fix`](../../../reference/cli/surrealdb-cli/commands/fix.md) command has been implemented to automatically change the format of your stored data. The command is followed by a path to the data. For example:

```bash
# For SurrealKV
surreal fix surrealkv://mydata

# For RocksDB
surreal fix rocksdb:somedatabase
```

### Limitations of the surreal fix command

Although the `surreal fix` command is a quick way to migrate your data, it is not without its drawbacks:

-  If you have used the now deprecated [`DEFINE TOKEN`](../../../reference/query-language/statements/define/token.md) command to define a token on a Scope with the also deprecated [`DEFINE SCOPE`](../../../reference/query-language/statements/define/scope.md) command, you will have to update your access management rules to use the new [`DEFINE ACCESS`](../../../reference/query-language/statements/define/access/index.md) which supports creating permissions using [TYPE JWT](../../../reference/query-language/statements/define/access/jwt.md) and [TYPE RECORD](../../../reference/query-language/statements/define/access/record.md) rules.

- If you were querying SurrealDB via the HTTP API, the `surreal fix` command will not update the header format for you. You will need to manually update the header format  from `ns` and `db` to `surreal-ns` and `surreal-db` respectively before using the `surreal fix` command. Learn more about this in the [HTTP documentation](https://surrealdb.com/docs/reference/rest-api/http).

### Upgrading from 2.0.0-alpha

The `surreal fix` command above has been created specifically for 1.x instances. However, data currently on a `2.0.0-alpha` instance can still be manually exported and then reimported into a project running on `2.0.0` via the following steps.

1. Export your current data as a `.surql` (SurrealQL) file. You can do this using the [`surreal export`](../../../reference/cli/surrealdb-cli/commands/export.md) command in the terminal:

```bash
# Example export command to export data to a file called `export.surql` in the downloads directory.
surreal export --conn http://localhost:8000 --user root --pass secret --ns main --db main downloads/export.surql
```

2. This will create a file called `export.surql` in the current directory.

3. You can now import this file back into your project running on `2.0.0`.

```bash
surreal import --conn http://localhost:8000 --user root --pass secret --ns main --db main downloads/export.surql
```

## Troubleshooting

### Error when connecting to a `2.x` instance.

If you are trying to connect to a `2.x` instance, and get an error similar to the following, you are likely using an older version of SurrealDB.

```bash
error: Storage version is out-of-date.
```

## Read the full changelog

There have been major improvements to SurrealDB in `2.0.0` release both in alpha and beta. Check out the changes on the [release page](/releases).
