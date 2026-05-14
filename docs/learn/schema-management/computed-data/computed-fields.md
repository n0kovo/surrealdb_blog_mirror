---
position: 1
title: Computed fields
description: Fields that are derived on read with COMPUTED, traversing record links, and how they differ from VALUE and stored data.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/schema-management/computed-data/computed-fields.mdx"
---

# Computed fields

Most fields are stored: you write a value and it stays on the record until you change it. A computed field differs from a normal field in that it is recalculated whenever the record is read, using an expression you attach in the schema. That makes it ideal for derived data that should always reflect a certain state instead of needing a separate update job.

## Compared to `VALUE` and normal storage

* `VALUE` on a field sets what gets stored (often normalising input); it runs on write, not on every read in the same way a computed field does.
* `COMPUTED` stores an expression, as opposed to set data.
* You cannot mark `id` or nested paths (for example `meta.score`) as computed—only top-level field names.

For everything else about field definitions—types, `ASSERT`, `DEFAULT`, permissions—see [Fields and validation](../tables-and-fields/fields-and-validation.md) and the [`DEFINE FIELD`](../../../reference/query-language/statements/define/field.md) reference.

## Example: always-fresh timestamp on read

```surql
DEFINE TABLE user SCHEMAFULL;
DEFINE FIELD name ON user TYPE string;
DEFINE FIELD accessed_at ON user COMPUTED time::now();

CREATE user:one SET name = "Ada";
SELECT * FROM ONLY user:one;
SLEEP 1s;
SELECT * FROM ONLY user:one;
```

The second `SELECT` should show a new `accessed_at` each time, because the expression is evaluated when the record is projected.

## Record references

A stored field can hold a [record link](../../../reference/query-language/language-primitives/record-links.md)—a record ID that points at another record—often declared with `record<table>` or `option<record<table>>`, and optionally with [`REFERENCE`](../../../reference/query-language/statements/define/field.md) so deletes on the target record are handled predictably. A computed field does not store a link itself (the `REFERENCE` clause applies to stored fields only), but the expression may traverse link fields already on the record and read fields from the related record.

In the example below, `book.author` stores `person:ada`, while `author_name` is derived from that link. If you change the person’s `name`, the next read of the book shows the updated label without writing back to `book`.

```surql
DEFINE TABLE person SCHEMAFULL;
DEFINE FIELD name ON person TYPE string;

DEFINE TABLE book SCHEMAFULL;
DEFINE FIELD title ON book TYPE string;
DEFINE FIELD author ON book TYPE record<person>;
DEFINE FIELD author_name ON book COMPUTED author.name;

CREATE person:ada SET name = "Ada Lovelace";
CREATE book:one SET title = "Notes", author = person:ada;

SELECT title, author_name FROM book:one;

UPDATE person:ada SET name = "Augusta Ada King";
SELECT title, author_name FROM book:one;
```

## When to use computed fields

Use them when:

* The result is cheap enough to evaluate on read and you want zero staleness.
* The logic is purely relative to the record and its graph.

Computed fields may not always be the best option. They should not be used when:

* You need the value indexed or searched like a normal field (compute into a stored field via events or application writes instead).
* The expression depends on external systems.

## See also

* [Closures](closures.md) — small anonymous functions in expressions.
* [Record links](../../../reference/query-language/language-primitives/record-links.md) — storing and traversing record IDs.
* [Reactive patterns](../events-and-triggers/reactive-patterns.md) — when updates should flow from writes instead of reads.
