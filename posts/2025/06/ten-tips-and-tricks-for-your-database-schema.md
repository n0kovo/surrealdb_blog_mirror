---
title: "Ten tips and tricks for your database schema"
slug: "ten-tips-and-tricks-for-your-database-schema"
date: "2025-06-17T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "5 min read"
summary: "Schema definition in SurrealDB is a powerful thing."
source: "https://surrealdb.com/blog/ten-tips-and-tricks-for-your-database-schema"
cover: "../../assets/abd305b23fd83d00.jpg"
---

# Ten tips and tricks for your database schema

![Ten tips and tricks for your database schema](../../assets/abd305b23fd83d00.jpg)

There are a lot of places to learn how to use SurrealDB, including the documentation, our [fundamentals course](/learn/fundamentals), the [Tour of SurrealDB](/learn/fundamentals), and even a [full book](/learn/book) that teaches SurrealDB through a story set centuries in the future!

But sometimes a quick rundown of a few tips and tricks hits the spot, and that's what this blogpost is about. In this post, let's look at some of the ways to put together a schema that works for you and not the other way around.

Did you know that you can...

### 1: Use a `set` for an array of distinct items

The lowly [`set`](/docs/surrealql/datamodel/sets) is a subtype of `array` that doesn't get a great deal of attention, but has the convenience of holding no duplicate items.

```surrealql
DEFINE FIELD ordered_unique ON stuff TYPE set VALUE $value.sort();

CREATE ONLY stuff SET ordered_unique = [8,7,8,8,8,8,6,45,3] RETURN VALUE ordered_unique;
-- Returns this:
[ 3, 6, 7, 8, 45 ]
```

As the query above shows, a `set` is just a subtype and not its own type so you can pass in an `array` into anything expecting a `set`. The only difference is that it will never hold a duplicate item.

### 2: Define arrays and sets with a type and maximum size

In addition to a type, both arrays and sets can have a maximum number of items built into the type definition itself. The definition below pairs this with an assertion using the [`array::all()`](/docs/surrealql/functions/database/array#arrayall) function to also ensure that every item in the `bytes` field is between 0 and 255.

```surrealql
DEFINE FIELD bytes ON data TYPE array<int, 640> ASSERT $value.all(|$int| $int IN 0..=255);
```

### 3: Define nested indexes

Even the individual indexes of an array can be defined. This is useful for data types like RGB colours that must be exactly three items in length. This time the schema uses an `ASSERT value.len() = 3` instead of `array<3>` to ensure that the array is an exact length instead of a maximum length.

```surrealql
DEFINE FIELD rgb ON colour TYPE array ASSERT $value.len() = 3;
DEFINE FIELD rgb[0] ON colour TYPE int ASSERT $value IN 0..=255;
DEFINE FIELD rgb[1] ON colour TYPE int ASSERT $value IN 0..=255;
DEFINE FIELD rgb[2] ON colour TYPE int ASSERT $value IN 0..=255;

CREATE colour SET rgb = [0, 2, 30];
```

### 4. Use `FLEXIBLE` objects and defined fields in `SCHEMAFULL` tables

The documentation mentions that a `SCHEMAFULL` table requires objects to have the `FLEXIBLE` keyword in order to treat them as free-form objects. Without this keyword, a `TYPE object` only tells the database that an object is to be expected but a `SCHEMAFULL` table disallows any field that hasn't been defined yet.

```surrealql
DEFINE TABLE user SCHEMAFULL;
DEFINE FIELD name ON user TYPE string;
DEFINE FIELD metadata ON user TYPE object;

-- Returns {} for `metadata`
CREATE user SET name = "Billy", metadata = {
    created_at: time::now(),
    age: 5
};
```

With the `FLEXIBLE` keyword the `metadata` field will now work, accepting any and all input.

```surrealql
DEFINE FIELD metadata ON user TYPE object FLEXIBLE;

CREATE user SET name = "Billy", metadata = {
    created_at: time::now(),
    age: 5
};
```

However, you can also simply define each field of an object in the same way you would with the field of a table. This allows the `metadata` field to hold these fields and ignore all other data used during a `CREATE` or `INSERT` statement.

```surrealql
DEFINE TABLE user SCHEMAFULL;
DEFINE FIELD name ON user TYPE string;
DEFINE FIELD metadata ON user TYPE object;
DEFINE FIELD metadata.created_at ON user TYPE datetime;
DEFINE FIELD metadata.age ON user TYPE int;

CREATE user SET name = "Billy", metadata = {
    created_at: time::now(),
    age: 5,
    wrong_field: "WRONG DATA"
};
```

### 5. Use `THROW` to add more detailed error messages to `ASSERT` clauses

A `DEFINE FIELD` statement allows an `ASSERT` clause to be added in order to ensure that the value, which here is represented as the parameter `$value`, meets certain expectations. A simple example here makes sure that the `name` field on the `person` table is under 20 characters in length.

```surrealql
DEFINE FIELD name ON person TYPE string ASSERT $value.len() < 20;

CREATE person SET name = "Mr. Longname who has much too long a name";
```

In this case, the default error message is pretty good.

```surrealql
"Found 'Mr. Longname who has much too long a name' for field `name`, with record `person:2gpvut914k1qfysqs3lc`, but field must conform to: $value.len() < 20"
```

However, `ASSERT` only expects a truthy value at the end and otherwise isn't concerned at all with what happens before. This means that you can outright customise the logic, including a custom error message. Let's give this a try.

```surrealql
DEFINE FIELD name ON person TYPE string ASSERT {
    IF $value.len() >= 20 {
        THROW "`" + <string>$value + "` too long, must be under 20 characters. Up to `" + $value.slice(0,19) + "` is acceptable";
    } ELSE {
       RETURN true;
    }
};

CREATE person SET name = "Mr. Longname who has much too long a name";
```

Not bad!

```surrealql
'An error occurred: `Mr. Longname who has much too long a name` too long, must be under 20 characters.
Up to `Mr. Longname who ha` is acceptable'
```

### 6. Use formatters on internal datetimes for strings with alternative formats

A lot of legacy systems require datetimes to be displayed in a format that doesn't quite match a `datetime`.

That doesn't mean that you have to give up the precision of a `datetime` though. By using the [`time::format()`](/docs/surrealql/datamodel/formatters) function, you can keep the actual stored date as a precise SurrealQL `datetime` and then use that to output a string in any format you like.

```surrealql
DEFINE FIELD created_at ON user VALUE time::now() READONLY;
DEFINE FIELD since ON user VALUE time::format(created_at, "%Y-%m-%d");

CREATE user RETURN id, since;
```

```surrealql
[
	{
		id: user:50s2riya8fm3cdbrhwpe,
		since: '2025-06-12'
	}
]
```

### 7. Use `!!$value` in `DEFINE` statements

As the `!` operator reverses the truthiness of a value, using it twice in a row as `!!` returns a value's truthiness. As empty and default values (such as 0 for numbers) are considered to be non-truthy, this operator is handy if you want to ensure that a value is both present and not empty.

```surrealql
DEFINE FIELD name ON character TYPE string;
DEFINE FIELD metadata ON character TYPE object;
-- Works because "" is of type string
CREATE character SET name = "", metadata = {};

DEFINE FIELD OVERWRITE name ON character TYPE string ASSERT !!$value;
-- Now returns an error because "" and {} are non-truthy
CREATE character SET name = "", metadata = {};
```

### 8. Use `DEFINE PARAM` for clarity

If you find that parts of your table- or field-specific code are getting a bit long, it might be time to think about moving parts of it to a [database-wide parameter](/docs/surrealql/statements/define/param).

```surrealql
DEFINE FIELD month_published ON book TYPE string ASSERT $value IN ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
```

Doing so not only makes the code cleaner, but makes it easy to reuse in other parts of the schema as well.

```surrealql
DEFINE PARAM $MONTHS VALUE ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

DEFINE FIELD month_published ON book TYPE string ASSERT $value IN $MONTHS;
DEFINE FUNCTION fn::do_something_with_month($input: string) {
    IF !($input IN $MONTHS) {
        THROW "Some error about wrong input";
    } ELSE {
        // do something with months here
    }
};
```

### 9. Use literals to return rich error output

Error types in programming languages often take the form of a long list of possible things that could go wrong. SurrealQL's [literal](/docs/surrealql/datamodel/literals) type allows you to specify a list of all possible forms it could take, making it the perfect type for error logic.

```surrealql
DEFINE PARAM $ERROR_CODES VALUE [200, 300, 400, 500];

DEFINE FUNCTION fn::return_response($input: 
    { type: "internal_error", message: string } |
    { type: "bad_request", message: string } | 
    { type: "invalid_date", got: any, expected: "YYYY-MM-DD" } |
    int) {
    IF $input.is_int() {
        IF $input IN $ERROR_CODES {
            RETURN $input
        } ELSE {
            THROW "Input must be one of " + <string>$ERROR_CODES;
        }
    } ELSE {
        RETURN $input
    }
};

fn::return_response(500);
fn::return_response({ type: "internal_error", message: "You can't do that"});
```

### 10. Use graph queries in the schema

While graph queries are usually seen in `SELECT` statements in the documentation, they can live inside your database schema just like any other datatype or expression. In the schema below for a family tree, any inserted record must either have a parent (via the `<-parent_of<-person` path) or be `first_generation`.

```surrealql
DEFINE FIELD parents ON person ASSERT <-parent_of<-person OR first_generation;

CREATE person:one SET first_generation = true;
CREATE person:two;

RELATE person:one->parent_of->person:two;
CREATE person:two;
```

By the way, this pattern is possible because `RELATE` statements can be used before the records to relate exist. To disallow this, you can add the [`ENFORCED`](/docs/surrealql/statements/define/table#using-enforced-to-ensure-that-related-records-exist) clause to a `DEFINE TABLE table_name TYPE RECORD` definition.

Got your own tip or have any other schema tips you'd like to see? Drop by [the SurrealDB Discord](https://discord.gg/surrealdb) to share your thoughts!
