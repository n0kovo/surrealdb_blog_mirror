---
position: 2
title: FETCH
description: The `FETCH` clause is used to fetch records from a table.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/clauses/fetch.mdx"
---

# `FETCH` clause

The `FETCH` clause is used to retrieve related records or data from other tables in a single query. This is particularly useful when you want to gather data that is linked through relationships ([record links](../language-primitives/record-links.md) or [graph edges](../statements/relate.md)) without having to perform multiple separate queries.

The `FETCH` clause predates and is functionally identical to the [`ALL`](../language-primitives/idioms.md#all-elements) idiom which is used by appending a `.*` to a related record.

## Example usage

Suppose you have a person table and a post table, where each post is related to a person. You can use the FETCH clause to retrieve a person along with their posts in a single query:

```surql
-- Using FETCH syntax
SELECT * FROM person FETCH posts;

-- Using .*
SELECT *, posts.* FROM person;
```

In this example, `posts` would be a related field in the `person` table that links to the `post` table. The `FETCH` clause allows you to retrieve all posts associated with each person in the result set.

The following example shows querying using `FETCH` or `.*` compared to selecting individual fields of a related record.

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%0A%09%09--%20Fetch%20all%20fields%20from%20author%20and%20category%0A%09%09SELECT%20%0A%09%09%09title%2C%20%0A%09%09%09category%2C%20%0A%09%09%09author%0A%09%09FROM%20article%0A%09%09FETCH%20author%2C%20category%3B%0A%09%09--%20Use%20.%2A%20syntax%20to%20do%20the%20same%0A%09%09SELECT%20%0A%09%09%09title%2C%20%0A%09%09%09category.%2A%2C%20%0A%09%09%09author.%2A%0A%09%09FROM%20article%3B)

### Fetching more than one level

To fetch a record link inside a fetched record, name its path with dots. Each part of the path is fetched, so `FETCH author.role` fetches both the author and the author's role, and a path can go as deep as the links do. A link inside an array, such as `permissions` below, is fetched for every element.

Separate several paths with commas to fetch links to different tables in the same query. Each path can have its own depth: the query below follows `author` three levels, to the role's permissions, and `category` one level further, to its parent category.

```surql
CREATE permission:read SET name = 'read';
CREATE permission:write SET name = 'write';
CREATE role:admin SET name = 'Admin', permissions = [permission:read, permission:write];
CREATE person:one SET name = 'Ann', role = role:admin;
CREATE category:science SET name = 'Science';
CREATE category:tech SET name = 'Tech', parent = category:science;
CREATE post:one SET title = 'Hi', author = person:one, category = category:tech;

SELECT * FROM post:one FETCH author.role.permissions, category.parent;
```

```surql title="Output"
[
	{
		author: {
			id: person:one,
			name: 'Ann',
			role: {
				id: role:admin,
				name: 'Admin',
				permissions: [
					{ id: permission:read, name: 'read' },
					{ id: permission:write, name: 'write' }
				]
			}
		},
		category: {
			id: category:tech,
			name: 'Tech',
			parent: { id: category:science, name: 'Science' }
		},
		id: post:one,
		title: 'Hi'
	}
]
```

The same works when the links sit inside objects in an array. Both queries below return the residents with each person fetched:

```surql
CREATE person:ann SET name = 'Ann';
CREATE person:bob SET name = 'Bob';
CREATE flat:one SET residents = [
	{ person: person:ann, since: 2020 },
	{ person: person:bob, since: 2023 }
];

SELECT *, residents.{ since, person: person.* } AS residents FROM flat:one;
SELECT * FROM flat:one FETCH residents.person;
```

```surql title="Output"
[
	{
		id: flat:one,
		residents: [
			{ person: { id: person:ann, name: 'Ann' }, since: 2020 },
			{ person: { id: person:bob, name: 'Bob' }, since: 2023 }
		]
	}
]
```

The destructuring in the first query returns only the fields it names, so the other fields of each object, here `since`, have to be listed. `FETCH` keeps them without naming them. To get only the linked records, `residents.person.*` is enough.

### Fetching only some linked records

`FETCH` replaces every link in the field it names, and has no `LIMIT` of its own. To fetch a few of a record's posts, such as the latest two, use a subquery in the field list. The subquery can sort and limit, and `.*` is not needed because it selects the records themselves:

```surql
CREATE user:one SET name = 'Ann';
CREATE post:1 SET title = 'First', at = d'2026-01-01';
CREATE post:2 SET title = 'Second', at = d'2026-01-02';
CREATE post:3 SET title = 'Third', at = d'2026-01-03';
RELATE user:one->wrote->[post:1, post:2, post:3];

SELECT name, (SELECT title, at FROM ->wrote->post ORDER BY at DESC LIMIT 2) AS latest FROM user:one;
```

```surql title="Output"
[
	{
		latest: [
			{ at: d'2026-01-03T00:00:00Z', title: 'Third' },
			{ at: d'2026-01-02T00:00:00Z', title: 'Second' }
		],
		name: 'Ann'
	}
]
```

For a field that holds an array of record links, the subquery reads from the field of the current record: `(SELECT title FROM $parent.posts ORDER BY title LIMIT 2)`. A slice such as `posts[0..2].*` also works, but it takes the first links in the order they are stored rather than the ones a sort would choose.

## Without the `FETCH` clause

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%0A%09%09--%20Access%20single%20field%20from%20author%20link%0A%09%09SELECT%20%0A%09%09%09title%2C%20%0A%09%09%09category%2C%20%0A%09%09%09author.full_name%20AS%20author_name%0A%09%09FROM%20article%3B%0A%09)
