---
position: 2
title: Nested objects and arrays
description: Store nested JSON-like structures in SurrealDB records, use SurrealQL examples with addresses and record links, and relate documents via fields such as article authors.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/data-models/document/nested-objects-and-arrays.mdx"
---

# Nested objects and arrays

Documents in SurrealDB behave like structured objects you might already use in application code: fields can hold primitives, nested objects, and arrays of values.

## Example: a user with nested addresses

The example below creates a `users` record with an `addresses` array of objects.

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=CREATE%20users%20CONTENT%20%7B%0A%20%20%20%20name%3A%20%27Alice%20Smith%27%2C%0A%20%20%20%20email%3A%20%27alice%40example.com%27%2C%0A%20%20%20%20age%3A%2029%2C%0A%20%20%20%20addresses%3A%20%5B%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20type%3A%20%27home%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20address_line%3A%20%27123%20Maple%20St%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20city%3A%20%27Springfield%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20country%3A%20%27USA%27%0A%20%20%20%20%20%20%20%20%7D%2C%0A%20%20%20%20%20%20%20%20%7B%0A%20%20%20%20%20%20%20%20%20%20%20%20type%3A%20%27work%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20address_line%3A%20%27456%20Oak%20Ave%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20city%3A%20%27Metropolis%27%2C%0A%20%20%20%20%20%20%20%20%20%20%20%20country%3A%20%27USA%27%0A%20%20%20%20%20%20%20%20%7D%0A%20%20%20%20%5D%0A%7D%3B)

By clicking the **Run query** button, you will see a result similar to:

```surql
[
	{
		addresses: [
			{
				address_line: '123 Maple St',
				city: 'Springfield',
				country: 'USA',
				type: 'home'
			},
			{
				address_line: '456 Oak Ave',
				city: 'Metropolis',
				country: 'USA',
				type: 'work'
			}
		],
		age: 29,
		email: 'alice@example.com',
		id: 'users:a2ndbh1hsquvkvthws09',
		name: 'Alice Smith'
	}
]
```

You may notice that the `id` field has a `users:` prefix. This is because SurrealDB uses an [id](../../../reference/query-language/language-primitives/data-types/record-ids.md) to uniquely identify each record, and the combination of the table name and the record id is used as the [record link](../../../reference/query-language/language-primitives/record-links.md).

## Embedding and linking

Document model databases are designed to store data in a flexible, nested structure. **Data organisation** often means self-describing documents in JSON or a similar format. Relationships can be represented **inside** the document (embedding) or via **references** using record links to other documents.

For example, if you wanted to associate a `person` with an `article` they wrote, you could assign the person's ID to the `author` field of the article document. This binds the `person` and `article` together, allowing you to query the `article` by the `person`'s ID.

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=CREATE+article+SET%0A%09created_at+%3D+time%3A%3Anow%28%29%2C%0A%09author+%3D+person%3Ajohn%2C%0A%09title+%3D+%27Lorem+ipsum+dolor%27%2C%0A%09text+%3D+%27Donec+eleifend%2C+nunc+vitae+commodo+accumsan%2C+mauris+est+fringilla.%27%3B%0A%0ACREATE+person%3Ajohn+SET%0A%09name.first+%3D+%27John%27%2C%0A%09name.last+%3D+%27Adams%27%2C%0A%09name.full+%3D+string%3A%3Ajoin%28%27+%27%2C+name.first%2C+name.last%29%2C%0A%09age+%3D+29%2C%0A%09admin+%3D+true%2C%0A%09signup_at+%3D+time%3A%3Anow%28%29%0A%3B)

## Retrieving documents

To read documents back, use a normal `SELECT`. For example, to return every field from the `users` table:

```surql
SELECT * FROM users;
```

SurrealDB automatically generates a unique [`id`](../../../reference/query-language/language-primitives/data-types/record-ids.md) for each document unless you supply your own identifiers.

For more on schema options and CRUD patterns, see [Schema modes](schema-modes.md) and [Common patterns](common-patterns.md).
