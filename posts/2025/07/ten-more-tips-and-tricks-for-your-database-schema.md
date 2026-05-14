---
title: "Ten more tips and tricks for your database schema"
slug: "ten-more-tips-and-tricks-for-your-database-schema"
date: "2025-07-15T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "7 min read"
summary: "Schema definition in SurrealDB is a powerful thing, and the more you know the more you can make your schema work for you."
source: "https://surrealdb.com/blog/ten-more-tips-and-tricks-for-your-database-schema"
cover: "../../assets/627640b5c7f0f840.jpg"
---

# Ten more tips and tricks for your database schema

![Ten more tips and tricks for your database schema](../../assets/627640b5c7f0f840.jpg)

In a [recent blog post](/blog/ten-tips-and-tricks-for-your-database-schema) we went over ten tips that you might find helpful when building and working with your database schema.

A month later, it looks like we've come up with ten more! Let's see what else SurrealDB has to offer your schema that you might not have encountered before.

Did you know that...

### 11: You can use the output of expressions inside `DEFINE FIELD` statements?

Take the following schema that includes a `customer` and a `purchase` table, followed by a separate invoice that is then linked to the original `purchase`.

```surrealql
DEFINE FIELD name     ON customer TYPE string;
DEFINE FIELD customer ON purchase TYPE record<customer>;
DEFINE FIELD amount   ON purchase TYPE int;
DEFINE FIELD product  ON purchase TYPE record<product>;

CREATE customer:billy SET name = "Billy Johnson";
CREATE product:computer;
CREATE purchase:one SET amount = 100, product = product:computer, customer = customer:billy;
CREATE invoice:one SET for = purchase:one.customer.name, amount = purchase:one.amount, of = purchase:one.product;
UPDATE purchase:one SET invoice = invoice:one;
```

This works fine, but the three lines that create a `purchase`, then an `invoice`, and then link one to the other are a bit awkward.

If every `purchase` comes with a linked `invoice`, we can just define that field as the output of the `CREATE` statement that makes the invoice. The `$parent` parameter can be used here to access the fields of `purchase` when creating it.

With this set up, a linked `invoice` is guaranteed to be created with every `purchase`.

```surrealql
DEFINE FIELD name     ON customer TYPE string;
DEFINE FIELD customer ON purchase TYPE record<customer>;
DEFINE FIELD amount   ON purchase TYPE int;
DEFINE FIELD product  ON purchase TYPE record<product>;
DEFINE FIELD invoice  ON purchase VALUE 
  CREATE ONLY invoice SET
    for = $parent.customer.name,
    amount = $parent.amount,
    of = $parent.product;

CREATE customer:billy SET name = "Billy Johnson";
CREATE product:computer;
CREATE purchase SET amount = 100, product = product:computer, customer = customer:billy;

SELECT * FROM invoice;
```

Output:

```surrealql
[
	{
		amount: 100,
		for: 'Billy Johnson',
		id: invoice:inhl76hdm08qawhs0iyg,
		of: product:computer
	}
]
```

### 12: Geohashes can be performant?

This example shows a query on each record in a `location` table that checks to see which `location` records are closest to it, in this case within 600 metres. As each random location is being created between a pretty small longitude and latitude (0.1 to 0.3 and 50.0 to 50.2),

```surrealql
FOR $_ IN 0..100 {
    LET $location = <point>[rand::float(0.1, 0.3), rand::float(50, 50.2)];
    CREATE event SET location = $location, at = time::now(), info = rand::string(10);
};

SELECT *, (SELECT * FROM event WHERE 
  geo::distance($parent.location, location) < 600 AND 
  geo::distance($parent.location, location) < 600 != 0) AS nearby_events
FROM event;
```

The example does work, with an output featuring records that should look something like this.

```surrealql
	{
		at: d'2025-07-10T05:06:33.840103Z',
		id: event:zcqic0gxvfp494a5r3rp,
		info: 'xnK3nxurE5',
		location: (0.1420432237694935, 50.10137089344105),
		nearby_events: [
			{
				at: d'2025-07-10T05:06:33.839627Z',
				id: event:b6l02h18r00zk5681cnu,
				info: '4170QyQNom',
				location: (0.13572951348705997, 50.09843129811583)
			},
			{
				at: d'2025-07-10T05:06:33.840103Z',
				id: event:zcqic0gxvfp494a5r3rp,
				info: 'xnK3nxurE5',
				location: (0.1420432237694935, 50.10137089344105)
			}
		]
	}
```

But using `SELECT * FROM event` for each and `event` to find its nearest neighbours feels like overkill. There are other ways to improve this query, but we're only using it as a setup to using geohashes so let's set it aside.

A [Geohash](https://en.wikipedia.org/wiki/Geohash) is a value that represents a rectangular space on our planet. The more characters in the geohash, the more precise the location.

You can give it a try [here](https://www.movable-type.co.uk/scripts/geohash.html). If you enter the character `u` then you'll see a big rectangle stretching from the Arctic down to Germany - not very precise. Add an extra digit of precision with `u3` and now the hash only shows a fraction of it, from Sweden and Denmark to Poland and Germany. Add one more to get `u3b` and now it is limited to a small part of Denmark. A Geohash at its full length of eight characters will have a precision of 19 metres, in the case of `u3btbb1b` showing two houses close to a fitness studio and pizza shop.

To get a precision of 600 metres, you can use a geohash with a length of 6 characters. We'll put it into the format `location:[string, ulid]` to represent an `event` that takes place inside a certain area. Let's try creating these random `event` records again with this new format.

```surrealql
FOR $_ IN 0..100 {
    LET $location = <point>[rand::float(0.1, 0.3), rand::float(50, 50.2)];
    CREATE event:[geo::hash::encode($location, 6), rand::ulid()] SET info = rand::string(10);
};
```

Now you can put the first part of the ID (the geohash) into a range query. Anything with the same geohash will show up as a nearby event.

```surrealql
SELECT 
    *, 
    -- Use array::complement to exclude records with the same ID
    array::complement(
      (SELECT VALUE id FROM event:[$parent.id[0], NONE]..=[$parent.id[0], ..]), [id]
    ) AS nearby_events
FROM event;

-- Example from output
{
  id: event:[
    'u0bhdr',
    '01JZPRBE5ZN3F1QQKMKNBTF6CF'
  ],
  info: 'WriwJNDNr3',
  nearby_events: [
    event:[
      'u0bhdr',
      '01JZPRBE5Y6TAFN5ZT0Y9Y0PYS'
    ]
  ]
},
```

### 13: Search analyzers can be manually used?

The main way to use a search analyzer for full-text search is to define an index that uses it so that the `@@` operator (the *matches* operator) can be used. However, because the `search::analyze()` function shows you the output of any given analyzer, you can use them manually too.

Here is an example of a number of analyzers that you can mix and match depending on the type of filtering you want to do. Just don't forget to call `.flatten()` every time.

```surrealql
DEFINE ANALYZER class TOKENIZERS class FILTERS lowercase;
DEFINE ANALYZER snowball_en FILTERS snowball(english);
DEFINE ANALYZER snowball_fr FILTERS snowball(english);
DEFINE ANALYZER ngram2_5 FILTERS ngram(2,5);
DEFINE ANALYZER ngram2_10 FILTERS ngram(2,10);

search::analyze("class", "According to legend, Memphis was founded by King Menes.")
  .map(|$n| search::analyze("snowball_en", $n))
  .flatten();
search::analyze("class", "La légende raconte que Memphis fut fondée par le roi Ménès.")
  .map(|$n| search::analyze("snowball_fr", $n))
  .flatten();
search::analyze("class", "La légende raconte que Memphis fut fondée par le roi Ménès.")
  .map(|$n| search::analyze("snowball_fr", $n))
  .flatten();

search::analyze("class", "La légende raconte que Memphis fut fondée par le roi Ménès.")
    .map(|$n| search::analyze("snowball_fr", $n)).flatten()
    .map(|$n| search::analyze("ngram2_5", $n)).flatten();
```

### 14: You can now define a sequence?

Defining a [sequence](/docs/surrealql/statements/define/sequence) is a recent addition to SurrealQL, available since the 3.0.0-alpha versions. Let's give it a try and see how it works.

```surrealql
DEFINE SEQUENCE seq;
sequence::nextval("seq"); -- returns 0
sequence::nextval("seq"); -- returns 1
sequence::nextval("seq"); -- returns 2
sequence::nextval("seq"); -- returns 3
```

It looks like a sequence is an incrementing number. What is the use case for a sequence then?

The first thing to know about a sequence is that it is guaranteed to be unique, even across multiple nodes. It allows lock-free reads, which means that a sequence will never be rolled back in a failed transaction.

```surrealql
BEGIN;
CREATE person; -- This will be rolled back
LET $x = sequence::nextval("seq"); -- returns 4
CANCEL;

sequence::nextval("seq"); -- Sequences are not rolled back, so returns 5
```

A sequence will usually use the `BATCH` clause which allows a node to request a range of sequences at once, reducing network chatter.

```surrealql
DEFINE SEQUENCE mySeq2 BATCH 1000;
```

Do you need a sequence in your schema? If [the following description](https://github.com/surrealdb/surrealdb/pull/5583) from the PR adding sequences matches what you are building, then the answer might be yes.

```syntax
The implementation of distributed sequences in SurrealDB meets the critical need for generating reliable, monotonically increasing numeric identifiers across a cluster of nodes without excessive coordination overhead, allowing applications to utilize sequences for unique IDs, counters, and ordered operations with optimal performance in distributed environments.
```

### 15: Text can be sorted lexically?

In the following example working with Hungarian text we have a field called `unique_tokens` that takes the output of a search analyzer to store the unique tokens (using casting into a `<set>`) from a certain sample text.

```surrealql
DEFINE ANALYZER simplify TOKENIZERS class FILTERS lowercase;
DEFINE FIELD text ON example TYPE string;
DEFINE FIELD unique_tokens ON example VALUE <set>search::analyze("simplify", text).sort();
CREATE example SET text = "A Wikipédia egy enciklopédia, pontosabban az a célja, hogy elfogadható enciklopédiává váljon, megbízható és bőséges ismeretanyagot nyújtson az olvasóinak, azok hasznára, szórakoztatására és megelégedésére. Az enciklopédia különlegessége, hogy az önkéntesek folyamatosan...";
```

This works well, except that the final tokens `'szórakoztatására', 'váljon', 'wikipédia', 'és', 'önkéntesek'` show that `és` and `önkéntesek` show up at the end instead of together with the other words that start with e and o.

To ensure that these words show up in proper lexical order, just change `.sort()` to `.sort_lexical()`!

```surrealql
DEFINE FIELD unique_tokens ON example VALUE <set>search::analyze("simplify", text).sort_lexical();
```

Now a token like `'és'` that begins with an accented character will show up next to the other words that start with e instead of showing up after z.

```surrealql
'elfogadható',
'enciklopédia',
'enciklopédiává',
'és',
'folyamatosan',
```

### 16: User-submitted HTML can be sanitized for safety?

This tip is a quick but important one: if your app takes raw HTML from users, don't forget to sanitize it to remove malicious parts such as scripting.

```surrealql
DEFINE FIELD html ON style TYPE string VALUE string::html::sanitize($value);
CREATE style SET html = "<h1>Safe Title</h1><script>alert('XSS')</script><p>Safe paragraph. <span onload='logout()'>event</span>.</p>";
```

As the output shows, the unsafe scripting portion has been removed.

```syntax
[
	{
		html: '<h1>Safe Title</h1><p>Safe paragraph. <span>event</span>.</p>',
		id: style:ikyd02a1125fl4i2zsdd
	}
]
```

### 17: You can use field definitions like events?

While `DEFINE EVENT` is the usual way to create an event, a `VALUE` clause can hold an entire code block so you can use it for similar behaviour.

The following code builds on the former HTML sanitization to create an alert whenever the sanitized HTML doesn't match the original HTML that a user attempted to insert.

```surrealql
DEFINE FIELD html ON style TYPE string VALUE {
    LET $sanitized = string::html::sanitize($value);
    IF $sanitized != $value {
        CREATE event SET val = "Warning: User attempted to insert: `" + $value + "`";
    };
    $sanitized;
};

CREATE style SET html = "<h1>Some Title</h1><script>alert('XSS')</script><p><span onload='logout()'>event</span>.</p>";

SELECT * FROM event;
```

Output:

```surrealql
[
	{
		id: event:eqpltdewcij9wacsq9wn,
		val: "Warning: User attempted to insert: `<h1>Some Title</h1><script>alert('XSS')</script><p><span onload='logout()'>event</span>.</p>`"
	}
]
```

### 18: SurrealDB has a lot of constant values?

SurrealDB is fairly rare among databases in having a large selection of mathematical and time-related constant values that you can make use of. Using a constant value is good practice for both accuracy and performance.

```surrealql
DEFINE FIELD circumference ON circle VALUE radius * 2 * math::pi;
CREATE circle SET radius = 10.5;

DEFINE FIELD future_value ON account VALUE principal * math::pow(math::e, rate * time);
CREATE account SET principal = 1000, rate = 0.05, time = 3;

DEFINE FIELD since_epoch ON user VALUE time::now() - time::epoch READONLY;
CREATE user;
```

### 19: The question mark operator can be used to avoid errors?

Take the following statements that create a `bank` and its customers, along with a field that filters out customers except those that have particularly high deposits.

```surrealql
DEFINE FIELD accounts ON bank TYPE option<array<record<customer>>>;
DEFINE FIELD vips ON bank VALUE accounts.filter(|$a| $a.amount > 10000);

CREATE bank:one;

CREATE customer:one SET amount = 100;
CREATE customer:two SET amount = 50000;

UPDATE bank:one SET accounts = [customer:one, customer:two];
```

Unfortunately, the `CREATE bank:one` statement won't work because `.filter()` can't be called on a value that is `NONE`, and this bank doesn't have any customers yet.

```surrealql
'There was a problem running the filter() function. no such method found for the none type'
```

But no problem! Using the `.?` operator will allow us to skip out on the `filter()` call in case the value is `NONE`, and now the statement will no longer fail.

```surrealql
DEFINE FIELD vips ON bank VALUE accounts.?.filter(|$a| $a.amount > 10000);
```

Once the customers are added, we will see this final output.

```surrealql
[
	{
		accounts: [
			customer:one,
			customer:two
		],
		id: bank:one,
		vips: [
			customer:two
		]
	}
]
```

### 20: Creating a mirror table can make range queries more flexible?

SurrealDB's record ranges are extremely performant because they are effectively a query on just a small portion of a table instead of the whole table.

```surrealql
CREATE event:[user:one, "debug", time::now()];
```

A query on this `event` table might look like this, in which case all the records with exactly `user:one` followed by `"debug"` within the latest 5 hours will show up.

```surrealql
SELECT * FROM event:[user:one, "debug", time::now() - 5h]..[user:one, "debug", time::now()];
```

But a query like this won't work as expected, because it will first return all `user:one`s between "debug" and "production", and only then check the next part of the ID. It's not a filter, but a whittling down of the space to be queried.

```surrealql
SELECT * FROM event:[user:one, "debug", time::now() - 5h]..[user:one, "production", time::now()];
```

If being able to use range queries in different ways is important, you can set up a mirror table that simply stores the same data in a different order. For example, this table is identical except that the middle string is removed.

```surrealql
DEFINE EVENT create_duplicate ON event WHEN $event = "CREATE" THEN {
    CREATE event2:[$after.id[0], $after.id[2]];
};
```

With that set up, you can now do record range queries on the second table based on just a `user` and the time of an event.

```surrealql
CREATE event:[user:one, "debug", time::now()];
SELECT * FROM event:[user:one, "debug", time::now() - 5h]..[user:one, "debug", time::now()];
SELECT * FROM event2:[user:one, time::now() - 5h]..[user:one, time::now()];
```
