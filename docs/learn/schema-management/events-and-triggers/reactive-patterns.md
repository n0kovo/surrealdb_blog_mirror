---
position: 2
title: Reactive patterns
description: Choosing between synchronous and asynchronous events, LIVE SELECT subscriptions, and evolving reactive behaviour safely.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/schema-management/events-and-triggers/reactive-patterns.mdx"
---

# Designing reactive systems in SurrealDB

[Events](defining-events.md) are SurrealDB's built-in way to react to changes: you attach logic that runs after a create, update, or delete using [`DEFINE EVENT`](../../../reference/query-language/statements/define/event.md). They do not run during bulk [import](../../../reference/cli/surrealdb-cli/commands/import.md), so plan backfills separately or use the [sql](../../../reference/cli/surrealdb-cli/commands/sql.md) endpoint if you rely on them for derived data. When deciding how to define an event, consider the following:

* What should happen immediately, what can wait, and how do you keep the system predictable?

## Immediate vs deferred work

Every event introduces work triggered by a write. The first and most important decision is whether that work belongs in the same transaction as the write or outside it. The sections below mirror that split; the [`DEFINE EVENT`](../../../reference/query-language/statements/define/event.md) reference describes `ASYNC`, `MAXDEPTH`, and `RETRY` in full.

### Strong consistency (synchronous events)

By default, events run in the same transaction as the triggering write (see [parameters](../../../reference/query-language/language-primitives/parameters.md#before-after) such as `$before` and `$after` in the event body). That means:

* If the event fails, the original write is rolled back
* All changes are immediately consistent
* The write includes the cost of the event

You will want to use this pattern when:

* The follow-up must always succeed
* The database must never enter an inconsistent state
* The logic is lightweight and predictable

This might be the case when you need to enforce constraints across tables or when writing audit records that must exist. Remember that [queries inside events bypass permission checks](defining-events.md#events-and-permissions), so validate anything security-sensitive explicitly in the `THEN` block.

The tradeoff with this pattern is that event logic should stay as small as practical to avoid added latency on every write.

### Deferred processing (asynchronous events)

With [`ASYNC`](../../../reference/query-language/statements/define/event.md#async-events), the event is queued and processed outside the original transaction. That implies:

* The write succeeds independently of the event
* The event runs in a separate transaction
* Failures do not roll back the original change

You will want to use this pattern when:

* The write must be fast
* The work is expensive or unreliable
* Temporary inconsistency is acceptable

For the background processing interval, [`MAXDEPTH`](../../../reference/query-language/statements/define/event.md#the-maxdepth-clause), and [`RETRY`](../../../reference/query-language/statements/define/event.md#the-retry-clause), see [Async events](../../../reference/query-language/statements/define/event.md#async-events) in the `DEFINE EVENT` reference.

### `LIVE SELECT`

While different from an event, a [`LIVE SELECT`](../../../reference/query-language/statements/live-select.md) is reactive in that it streams notifications when records matching the selection change. While an event embeds what the database should do in a `THEN` block, a live query only tells subscribers that something changed, so your app (or another service) decides how to react - typically in [SDK code](../../../reference/javascript/concepts/live-queries.md) using the connection's live-query APIs.

For behaviour on the wire, subscriptions, and production caveats, read [Live queries](../../querying/real-time/live-queries.md). To end a subscription, use [`KILL`](../../../reference/query-language/statements/kill.md) with the query UUID the server returns when you register the live select. [Real-time best practices](../../querying/real-time/real-time-best-practices.md#defining-events) also contrasts live queries with defining events when the database can do the work without a client listener.

### Building reactive systems incrementally

The sheer convenience of reactive systems makes them tempting to use early. They are harder to debug when many are introduced together. For example, an error that occurs may be difficult to debug inside an [event](defining-events.md) that chains into further writes plus several [`LIVE SELECT`](../../../reference/query-language/statements/live-select.md), especially if all of these reactive patterns were introduced all at once.

For this reason, it is often best to introduce reactive behaviour gradually.

A good rule of thumb is to do the following:

* Start with explicit logic, and build your core behaviour in straightforward queries or application code.
* Stabilise your data model and workflows.
* Make sure the system behaves correctly before introducing automation.
* Introduce reactivity where it adds clear value.
* Move well-understood logic into [events](defining-events.md) or [live queries](../../querying/real-time/live-queries.md) once the behaviour is predictable.
* Avoid large or highly coupled chains of events.

## Records that expire

SurrealDB does not yet have a time-to-live (TTL) setting or a built-in scheduler, so a record stays until something deletes it. Two patterns cover most needs in the meantime: hide a record's value once it is too old, or delete old records as new ones arrive.

### Hiding expired values with a computed field

A [`COMPUTED`](../computed-data/computed-fields.md) field is worked out each time the record is read, so it can compare the current time with a stored timestamp. The field below returns the invite code for an hour and `NONE` after that, and a second field says whether the invite has expired:

```surql
DEFINE FIELD created_at ON invite DEFAULT time::now();
DEFINE FIELD code ON invite COMPUTED IF time::now() - created_at < 1h { secret } ELSE { NONE };
DEFINE FIELD expired ON invite COMPUTED time::now() - created_at >= 1h;

CREATE invite:old SET secret = 'OLD123', created_at = time::now() - 2h;
CREATE invite:new SET secret = 'NEW456';

SELECT id, code, expired FROM invite;
```

```surql title="Output"
[
	{ code: 'NEW456', expired: false, id: invite:new },
	{ code: NONE, expired: true, id: invite:old }
]
```

A query can then leave expired records out with `WHERE !expired`. The expired record and its `secret` are still stored, so give `secret` a [field permission](../../../reference/query-language/statements/define/field.md) if it must not be read directly.

### Deleting old records with an event

An [event](../../../reference/query-language/statements/define/event.md) can delete the records that have expired each time a new record is created:

```surql
DEFINE FIELD created_at ON session DEFAULT time::now();
DEFINE INDEX session_created ON session FIELDS created_at;

DEFINE EVENT expire_old ON session WHEN $event = 'CREATE' THEN {
    DELETE session WHERE created_at < time::now() - 1h;
};

CREATE session:old SET created_at = time::now() - 2h;
CREATE session:recent SET created_at = time::now() - 10m;

SELECT VALUE id FROM session;
```

```surql title="Output"
[session:recent]
```

The expired `session:old` is deleted when `session:recent` is created. The index on `created_at` keeps the `DELETE` fast, because it runs on every create. Old records stay until the next record is created, so a table that stops receiving writes keeps them. For cleanup on a fixed schedule instead, run the `DELETE` statement from an external scheduler such as `cron`, for example with [`surreal sql`](../../../reference/cli/surrealdb-cli/commands/sql.md).
