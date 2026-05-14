---
title: "Behind the scenes of the exciting beta 9 release"
slug: "behind-the-scenes-of-the-exciting-beta-9-release"
date: "2023-04-12T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "3 min read"
summary: "Our team has been working very hard on the new release, which introduces a ton of new features, bug fixes and performance improvements you can see here..."
source: "https://surrealdb.com/blog/behind-the-scenes-of-the-exciting-beta-9-release"
cover: "../../assets/a9560ebee1c1cf28.jpg"
---

# Behind the scenes of the exciting beta 9 release

![Behind the scenes of the exciting beta 9 release](../../assets/a9560ebee1c1cf28.jpg)

Our team has been working very hard on the new release, which introduces a ton of new features, bug fixes and performance improvements [you can see here](/releases).

However, the story of the beta 9 release is not about our team; it's about you!

How you use the database and the ideas you have to improve it.

Let's explore a few of these ideas and how they ended up getting released.

## Returning a single field from `SELECT` statements

Brian ([Du-z](https://github.com/Du-z)) joined our community last September and has made several great contributions, [including the one you’re reading about.](https://github.com/surrealdb/surrealdb/issues/1326)

He noticed that the query `SELECT name FROM user` would result in something like the following.

```javascript
[
    {
        Name: 'Name 1',
    },
    {
        Name: 'Name 2',
    },
];
```

However, he felt it would be far easier to deserialise and work with a simple string array.

```javascript
['Name 1', 'Name 2'];
```

He gave this very helpful suggestion for a solution based on CosmosDB's `FIELD` keyword:

`SELECT VALUE name FROM user`

After some discussion, this was implemented by our team, and now you can `SELECT VALUE name FROM user`, thanks to Brian!

## Custom functions with `DEFINE FUNCTION` statements

Sebastian (**[mathe42](https://github.com/mathe42)**) has been a very active community member since last September, with around 20 pull requests and many other great contributions [like this one](https://github.com/surrealdb/surrealdb/issues/247).

For his use case, he was looking for some sort of user-defined functions that would allow us to have a callable list of SurrealQL instructions with arguments etc.

He came up with this example of how it could be done:

```surrealql
-- Define a procedure to get a person

DEFINE PROCEDURE get_person ($firstname, $lastname, $birthdate) {
  LET $person = SELECT * FROM person WHERE firstname = $firstname AND lastname = $lastname AND birthdate = $birthdate;

  IF (COUNT($person)==1) THEN
     RETURN 1;
  ELSE
    RETURN CREATE person {
       firstname: $firstname,
       lastname: $lastname,
       birthdate: $birthdate
    }
  END
}

-- and call it by
LET $myPerson = CALL get_person('Sebastian', 'Krüger', '2022-09-21')
```

After some discussion and some magic from Tobie, you can now define global database-wide custom functions!

```surrealql
-- Define a global function which can be used in any query
DEFINE FUNCTION fn::get_person($first: string, $last: string, $birthday: string) {

  LET $person = SELECT * FROM person WHERE [first, last, birthday] = [$first, $last, $birthday];

  RETURN IF $person[0].id THEN
    $person[0];
  ELSE
    CREATE person SET first = $first, last = $last, birthday = $birthday;
  END;

};

-- Call the global custom function, receiving the returned result
LET $person = fn::get_person('Tobie', 'Morgan Hitchcock', '2022-09-21');
```

This allows complicated or repeated user-defined code to run seamlessly within any query across the database.

Custom functions support typed arguments and multiple nested queries with custom logic.

All this started with Sebastian’s idea for what he wanted in the database, thanks Sebastian!

## Code blocks and advanced expressions

Tom (**[tomsseisums](https://github.com/tomsseisums)**) also joined us on our journey in September and has been sharing some great insights into what can be done better, such as [this use case](https://github.com/surrealdb/surrealdb/issues/1319).

He was trying to fit his project into SurrealDB from the perspective of 'SurrealDB as a Backend', where with the power of SurrealDB, we could handle all data operations in SurrealDB without the need for any intermediate layer.

He tried to set up events and fields with rich expressions in `CREATE` / `UPDATE` but was faced with parse errors.

This is one of several things Tom was trying to do:

```surrealql
CREATE metrics SET average_sales = (
    LET $sales = (SELECT quantity FROM sales);
    LET $total = math::sum($sales);
    LET $count = count($sales);

    RETURN ($total / $count);
);
```

However he was disappointed when he received an unexpected parse error.

```javascript
{
    "code": 400,
    "details": "Request problems detected",
    "description": "There is a problem with your request. Refer to the documentation for further information.",
    "information": "There was a problem with the database: Parse error on line 1 at character 15 when parsing 'SET average_sales = (
    LET $sales = (SELECT quantity FROM sales);
    LET $total = math::sum($sal'"
}
```

That didn’t stop him from wanting this to exist, and therefore he created a [feature request for it](https://github.com/surrealdb/surrealdb/issues/1319).

After some discussion and some more magic, it is now possible, thanks to Tom!

```surrealql
DEFINE FIELD average_sales ON metrics VALUE {
  LET $sales = (SELECT VALUE quantity FROM sales);
  LET $total = math::sum($sales);
  LET $count = count($sales);
  RETURN ($total / $count);
};
```

You can now run blocks of code with support for an arbitrary number of statements, including `LET` and `RETURN`!

This allows for writing advanced custom logic and allows for more complicated handling of data operations.

## Thank you, everyone, for being a part of this ambitious journey with us!

We only scratched the surface of what was released, and you can [find more here](/releases).

We are always happy to work on things together [on GitHub](https://github.com/surrealdb/surrealdb) and [our Discord server](https://discord.gg/surrealdb).

We’re looking forward to seeing what ideas and improvements you have in mind next!

Until then we’ll be sharing more deep-dive blog posts about some of the new features coming out.

Use the subscribe button on the left to make sure you don’t miss out!
