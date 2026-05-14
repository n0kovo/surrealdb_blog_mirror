---
title: "Ten tips and tricks for your SurrealDB queries"
slug: "ten-tips-and-tricks-for-your-surrealdb-queries"
date: "2025-08-18T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "7 min read"
summary: "SurrealQL queries are expressive and powerful, and the more you know the more you can make your queries work for you."
source: "https://surrealdb.com/blog/ten-tips-and-tricks-for-your-surrealdb-queries"
cover: "../../assets/dfa3e6e23d22fbbd.jpg"
---

# Ten tips and tricks for your SurrealDB queries

![Ten tips and tricks for your SurrealDB queries](../../assets/dfa3e6e23d22fbbd.jpg)

We recently took a look at [ten ways to improve your database schema](/blog/ten-tips-and-tricks-for-your-database-schema), followed by [ten more](/blog/ten-more-tips-and-tricks-for-your-database-schema)! Schema is all about setting definitions and expectations for your database, after which the operations are entirely passive. This blog post takes a look at the other part of working with your data: how to get the most out of active queries.

Did you know that you can...

### 1. Use the `??` operator to specify a default value for a field

The following `person` records are pretty similar, except that one doesn't have a value for the `age` field.

```surrealql
CREATE person SET name = "Billy", age = 10;
CREATE person SET name = "Huma";
```

A query on both `name` and `age` works fine, with `age` showing up as the value `NONE` for one of them.

```surrealql
SELECT name, age FROM person;

-- Output
[
	{
		age: NONE,
		name: 'Huma'
	},
	{
		age: 10,
		name: 'Billy'
	}
]
```

But you might need to pass this information into an app that expects a value, such as either an integer or the value "unknown". In that case, you can change `age` to `age ?? "unknown"`. An easy mnemonic to remember this syntax:

"Is there a value for `age`?? If not, return `"unknown"`"

After making that change, be sure to add `AS age` so that the field name stays as `age` instead of `"age ?? 'unknown'"`, the expression used to calculate it.

```surrealql
SELECT 
    name,
    age ?? "unknown", // Works but output is ugly
    age ?? "unknown" AS age // Much cleaner output
FROM person;

-- Output
[
	{
		age: 10,
		"age ?? 'unknown'": 10,
		name: 'Billy'
	},
	{
		age: 'unknown',
		"age ?? 'unknown'": 'unknown',
		name: 'Huma'
	}
]
```

### 2. Use the `?` operator to skip out ahead of time and avoid errors

Another questionable SurrealQL operator is `?`, which lets you avoid errors by skipping out ahead of time and returning `NONE`.

Let's add a value for `friends` for the above queries, which contains an array of record IDs. Here as well, only one `person` record has a value for this field.

```surrealql
CREATE person SET 
	name = "Billy", 
	age = 10;
CREATE person SET 
	name = "Huma", 
	friends = [minotaur:kaz, person:magius];

SELECT 
	name, 
	age, 
	friends.len() AS num_friends
FROM person;
```

This time we get an error, because `.len()` (the function `array::len()`) can't be called on a NONE.

```surrealql
'There was a problem running the len() function. no such method found for the none type'
```

A dot and a question mark is enough to fix this. If the query finds no value for the field, it will give up at that point and the `.len()` method will not be called.

```surrealql
SELECT 
	name, 
	age, 
	friends.?.len() AS num_friends
FROM person;

-- Output:
[
	{
		age: NONE,
		name: 'Huma',
		num_friends: 2
	},
	{
		age: 10,
		name: 'Billy',
		num_friends: NONE
	}
]
```

The `??` can be used here too, because `friends?` may end up returning a `NONE` value, which is what the `??` operator looks for.

```surrealql
SELECT 
    name, 
    age ?? "unknown" AS age,
    friends.?.len() ?? 0 AS num_friends FROM person;

-- Output:
[
	{
		age: 10,
		name: 'Billy',
		num_friends: 0
	},
	{
		age: 'unknown',
		name: 'Huma',
		num_friends: 2
	}
]
```

### 3. Use a `SELECT` expression at any point inside a graph query

Take the following example that uses graph relations to connect a recipe with its ingredients.

```surrealql
CREATE recipe:cake SET name = "Cake";
CREATE ingredient:flour SET name = "Flour";
CREATE ingredient:sugar SET name = "Sugar";
CREATE ingredient:cinnamon SET name = "Cinnamon";
RELATE recipe:cake->contains->ingredient:flour SET quantity_grams = 375;
RELATE recipe:cake->contains->ingredient:sugar SET quantity_grams = 250;
RELATE recipe:cake->contains->ingredient:cinnamon SET quantity_grams = 10;
```

A query on the ingredients can be done by using `.{}` on the `contains` edge and selecting which fields you want to display.

```surrealql
SELECT
    name AS recipe_name,
    ->contains.{ grams: quantity_grams, name: out.name } AS ingredient_list
FROM recipe;

-- Output
[
	{
		ingredient_list: [
			{
				grams: 375,
				name: 'Flour'
			},
			{
				grams: 250,
				name: 'Sugar'
			},
			{
				grams: 10,
				name: 'Cinnamon'
			}
		],
		recipe_name: 'Cake'
	}
]
```

Now what if you wanted to only show the main ingredients, those with the largest quantity? No problem here either, because `SELECT` can be used at any point inside a graph query. Just wrap it in parentheses and use `SELECT` as you normally would. The only difference is that `SELECT` at this point will be done on only the output from the previous step (the `->` arrow), instead of the whole `contains` table.

```surrealql
SELECT
    name AS recipe_name,
    ->(SELECT quantity_grams, out.name AS ingredient FROM contains WHERE quantity_grams >= 100) AS major_ingredients
FROM recipe;

-- Output
[
	{
		major_ingredients: [
			{
				ingredient: 'Sugar',
				quantity_grams: 250
			},
			{
				ingredient: 'Flour',
				quantity_grams: 375
			}
		],
		recipe_name: 'Cake'
	}
]
```

### 4. Use the `SPLIT` clause instead of `[0]`

This example shows two companies, one the parent of the other.

```surrealql
CREATE company:one, company:two;

RELATE company:one->owns->company:two;
RELATE company:one->owns->company:two;
```

To see each company's parent company, you can use a graph query. Since a company can only have a single parent company, parentheses are used to grab the expression and then `[0]` to access the first record.

```surrealql
SELECT 
    id, 
    (<-owns<-company)[0] AS parent_company
FROM company;

-- Output:
[
	{
		id: company:one,
		parent_company: NONE
	},
	{
		id: company:two,
		parent_company: company:one
	}
]
```

Using `SPLIT` is another option here, which will return one object for each result at the `<-owns<-company` path. This will remove `company:one` from the results because there is nothing for it to split, so in this case `SPLIT` also acts as a filter.

In addition, using `SPLIT` shows that we mistakenly used a `RELATE` statement twice for the same two companies!

(Did you catch that?)

```surrealql
SELECT 
    id, 
    <-owns<-company AS parent_company
FROM company
SPLIT parent_company;

-- Output:
[
	{
		id: company:two,
		parent_company: company:one
	},
	{
		id: company:two,
		parent_company: company:one
	}
]
```

By the way, you can ensure that the two `RELATE` statements couldn't happen in the first place by creating a `UNIQUE` index. While this is a query tips and not schema tips blog, we would be remiss to not mention this fact!

```surrealql
DEFINE INDEX only_one ON owns FIELDS in, out UNIQUE;
```

### 5. Graph edges can have non-standard IDs too

The usual way to add metadata to a graph edge is by using `RELATE` and then `SET` to add the fields.

```surrealql
CREATE user:one, post:one;

RELATE user:one->likes->post:one SET liked_at = time::now();
```

The `liked_at` edge will have a random ID like `likes:geci4id19wk3k5g45iqb`.

You can then use a [filter query](/docs/surrealql/datamodel/arrays#mapping-and-filtering-on-arrays) of this sort to see a user's posts over the last five days. This approach is great if you are doing queries from the user's side.

```surrealql
SELECT
	->likes[WHERE liked_at > time::now() - 5d] AS likes
FROM user;
```

However, if you are using a lot of queries from the `likes` table itself, you might want to opt for a complex array ID such as this one that includes a record and a datetime.

```surrealql
likes:[user:one, d'2025-08-14T02:09:30.303Z']
```

The relation can be created in the same way, except that this time the ID of the edge is specified.

```surrealql
RELATE user:one->likes:[user:one, time::now()]->user:two;
```

If the `RELATE` statement can't parse the ID you are attempting to pass in, you can use [`INSERT RELATION`](/docs/surrealql/statements/insert#insert-relation-tables) instead.

```surrealql
// RELATE can't handle function calls yet, returns error
RELATE user:one->type::thing("likes", [user:one, time::now()])->user:two;

// But this will work
INSERT RELATION {
    id: type::thing("likes", [user:one, time::now()]),
    in: user:one,
    out: user:two
};
```

With this complex ID, you can use the former query in almost the same way (changing `liked_at` to `id.liked_at`) while also being able to use a record range query on the `likes` table itself, thereby avoiding a full table scan.

```surrealql
SELECT 
	->likes[WHERE id.liked_at > time::now() - 5d] AS likes
FROM user;
SELECT * FROM likes:[user:one, time::now() - 5d]..[user:one, time::now()];
```

### 6. You can use fields for polymorphic relationships in graph queries

A graph query can be done on multiple types of graph edges. The example below shows how you can combine multiple edges into a single field.

```surrealql
CREATE person:one, person:two, person:three, person:four;
RELATE person:one->friends_with->person:two;
RELATE person:one->works_with->person:three;
RELATE person:one->married_to->person:four;

SELECT 
	->(friends_with, works_with, married_to)->person AS knows
FROM person;
```

If you feel like you are using too many types of edge relations, you can combine them into a single relation and differentiate by field values instead.

```surrealql
CREATE person:one, person:two, person:three, person:four;
RELATE person:one->knows->person:two SET 
  friends_with = true, 
  knows_since = time::now() - 10y;
RELATE person:one->knows->person:three SET 
  works_with = true, 
  friends_with = true, 
  knows_since = time::now() - 1y;
RELATE person:one->knows->person:four SET
  married_to = true,
  knows_since = time::now() - 10y;
```

Now there is only one edge connecting `person` records, but you can use the `[WHERE]` syntax at any point to filter by relationship type.

```surrealql
SELECT 
    id, 
    ->knows[WHERE friends_with AND works_with]->person AS friendly_coworkers,
    ->knows[WHERE friends_with AND time::now() - knows_since > 5y]->person AS long_term_friends
FROM ONLY person:one;

-- Output:
{
	friendly_coworkers: [
		person:three
	],
	id: person:one,
	long_term_friends: [
		person:two
	]
}
```

### 7. Use SELECT to get around current closure limitations

A current limitation of SurrealQL is that closures are not aware of variables. In the query below, this means that the `$now` parameter will show up as `NONE` instead of a datetime when attempting to map some record IDs into an array of objects.

```surrealql
LET $now = time::now();

[user:one, user:two, user:three].map(|$user| {
    id: $user,
    name: "User number " + <string>$user.id(),
    created_at: $now
});

-- Output:
[
	{
		created_at: NONE,
		id: user:one,
		name: 'User number one'
	},
	{
		created_at: NONE,
		id: user:two,
		name: 'User number two'
	},
	{
		created_at: NONE,
		id: user:three,
		name: 'User number three'
	}
]
```

However, since `.map()` returns an array of objects with field names, these field names can be selected in the usual way - along with the `$now` parameter as the `created_at` field.

```surrealql
LET $now = time::now();

SELECT id, name, $now AS created_at FROM
    [user:one, user:two, user:three].map(|$user| {
    id: $user,
    name: "User number " + <string>$user.id()
});

-- Output:
[
	{
		created_at: d'2025-08-13T05:16:36.492Z',
		id: user:one,
		name: 'User number one'
	},
	{
		created_at: d'2025-08-13T05:16:36.492Z',
		id: user:two,
		name: 'User number two'
	},
	{
		created_at: d'2025-08-13T05:16:36.492Z',
		id: user:three,
		name: 'User number three'
	}
]
```

### 8. Use .reduce() for the time being

Parameters in SurrealDB are currently immutable, meaning that this sort of pattern to increment the value of a parameter will not work.

```surrealql
LET $num = 0;

FOR $int IN [1,2,3] {
    $num += $int
};
```

Functions like `array::reduce()`, `array::fold()`, and `.chain()` can be used in these cases instead.

The `array::reduce()` function performs an operation on each item in an array, `array::fold()` does the same but with an extra initial value, and `.chain()` allows you to take any value and perform one operation on it.

```surrealql
-- Returns 6
[1,2,3].reduce(|$one, $two| $one + $two);

-- Returns 106
[1,2,3].fold(100, |$one, $two| $one + $two);

-- Returns 53
[1,2,3].fold(100, |$one, $two| $one + $two).chain(|$final| $final / 2);
```

### 9. Use statements inside another statement

This example shows a laptop that is created and assigned to an new employee.

```surrealql
LET $laptop = CREATE ONLY computer SET model_num = 87687576;
CREATE ONLY employee SET 
    name = "Johnny Johnclaw McJohnson",
    dob = '1985-09-01T00:00:00Z',
    computer = $laptop.id;

-- Output:
{
	computer: computer:k1vshq9stmg3kxmqcp9k,
	dob: '1985-09-01T00:00:00Z',
	id: employee:je01eet3jxn4b69e889o,
	name: 'Johnny Johnclaw McJohnson'
}
```

However, when creating records that depend on each other it can be preferable to do the entire creation inside a single query. This will allow all of the statements to fail at once if something has gone wrong, and you won't have to manually undo any previous statements.

This time we'll have the `dob` field as a `datetime`.

```surrealql
DEFINE FIELD dob ON employee TYPE datetime;

CREATE ONLY employee SET 
    name = "Johnny Johnclaw McJohnson",
    dob = '1985-09-01T00:00:00Z',
    computer = CREATE ONLY computer SET model_num = 87687576 RETURN VALUE id;
```

Oops! The value `'1985-09-01T00:00:00Z'` that we passed in is a `string` and not a `datetime`.

```surrealql
"Found '1985-09-01T00:00:00Z' for field `dob`, with record `employee:v17nqyhi6gxh8jd1cgg1`, but expected a datetime"
```

Fortunately, both create statements for `employee` and `computer` failed so we still have a clean slate to work with. All we need to do is add a `d` in front of the date to have the input recognised as a `datetime` and not a `string`.

```surrealql
DEFINE FIELD dob ON employee TYPE datetime;

CREATE ONLY employee SET 
    name = "Johnny Johnclaw McJohnson",
    dob = d'1985-09-01T00:00:00Z',
    computer = CREATE ONLY computer SET model_num = 87687576 RETURN VALUE id;

SELECT * FROM employee;

-- Output:
[
	{
		computer: computer:b5sh7jbjs5ixqzx9740n,
		dob: d'1985-09-01T00:00:00Z',
		id: employee:r057f7pvirlz9f4lfmz5,
		name: 'Johnny Johnclaw McJohnson'
	}
]
```

### 10. Add metadata with RETURN

This last tip is about a functionality that is pretty basic but easy to forget about.

There are quite a few options available to you when using `RETURN` after a query. You can `RETURN BEFORE`, `RETURN AFTER`, `RETURN DIFF`, `RETURN VALUE field_name`, or just about anything else.

Returning a variable output makes it possible to return some content once without touching the actual saved data. For example, you could return a message for a developer that you know is monitoring the database activity and needs to be alerted to something.

```surrealql
CREATE user SET
	created_at = time::now()
RETURN 
	*,
	"Jeff, seriously don't delete this user this time, he's threatening to cancel his membership!!!" AS `👉👉👉👉👉Look at this, Jeff👈👈👈👈👈`,
    "Also please deposit 100 gold in the user's Bank of Astonia account as a way to say sorry" AS `👉👉👉👉👉Plus please do this👈👈👈👈👈`;

-- Output:
[
	{
		created_at: d'2025-08-14T02:52:18.156Z',
		id: user:amhq2v4errgbujwvzkgp,
		"👉👉👉👉👉Look at this, Jeff👈👈👈👈👈": "Jeff, seriously don't delete this user this time, he's threatening to cancel his membership!!!",
		"👉👉👉👉👉Plus please do this👈👈👈👈👈": "Also please deposit 100 gold in the user's Bank of Astonia account as a way to say sorry"
	}
]
```

But the original `user` record will stay untouched.

```surrealql
SELECT * FROM user;

-- Output
[
	{
		created_at: d'2025-08-14T02:52:18.156Z',
		id: user:amhq2v4errgbujwvzkgp,
	}
]
```
