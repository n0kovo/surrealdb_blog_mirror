---
title: "Making your own PR to the SurrealDB source code"
slug: "making-your-own-pr-to-the-surrealdb-source-code"
date: "2025-01-24T00:00:00.000Z"
categories:
  - "community"
read_time: "11 min read"
summary: "Making a small PR to the SurrealDB source code is easier than you think, even if you come from another programming language."
source: "https://surrealdb.com/blog/making-your-own-pr-to-the-surrealdb-source-code"
cover: "../../assets/acfa6afdbdeeee2d.jpg"
---

# Making your own PR to the SurrealDB source code

![Making your own PR to the SurrealDB source code](../../assets/acfa6afdbdeeee2d.jpg)

One of the first things people usually notice when they check out SurrealDB is the fact that [it is written entirely in Rust](/blog/why-we-are-betting-on-rust), and is open source.

The source code for the SurrealDB database is open, and can be seen [on GitHub](https://github.com/surrealdb/surrealdb). While the bulk of the changes to the database are made by the core engineering team, anyone is invited to put a PR together and many of these get merged! In fact, as of the writing of this blog, it has been less than a day since the most recent user-submitted PR was merged. This PR is a small one that [fixed an error](https://github.com/surrealdb/surrealdb/pull/5340/files) to do with handling file URLs. The whole PR is just under 50 lines, including a test.

So what happens if you find a bug that you think you know how to fix, or a feature that you'd like to add? Because although Rust continues to gain popularity (as of January 2025, it is [in ninth place on the PYPL Index](https://pypl.github.io/PYPL.html)), the majority of the people using SurrealDB come from languages like Python and JavaScript.

That's what this post is for, to help you get set up and ready to make your first PR, even if you've never touched any Rust code before. To be honest, the reason why people don't usually experiment with other programming languages as much as they otherwise would is not because of the language, it's because it takes a while to get set up and install the tools to start writing code. And making a PR to an existing code base...that can be pretty intimidating.

Fortunately, Rust is particularly accessible in this respect, both in setting up the tools and adding code.

One of the reasons why user PRs are so frequent is that Rust itself is a pretty straightforward language to contribute to. While the language itself is on the complex side (to say the least), its strict compiler and single [package manager](https://doc.rust-lang.org/cargo/) make it relatively manageable to run and test any changes and to be confident that what you've submitted will work as expected.

Many other companies have discovered the same. In fact, Google discovered in 2023 that 2 out of 3 of the respondents to the survey [were confident in contributing to a Rust codebase within two months or less](https://opensource.googleblog.com/2023/06/rust-fact-vs-fiction-5-insights-from-googles-rust-journey-2022.html).

So let's get started!

# Setup to start testing your code

The first step is to [install Rust](https://www.rust-lang.org/tools/install), which doesn't take all that long. Once it is installed, you will begin using `Cargo` for everything such as building and testing your code.

Rust is a compiled language, and the first compilation always takes the longest because it builds the entire program from scratch. Once you have cloned the content from the SurrealDB repo, most likely using the `git clone https://github.com/surrealdb/surrealdb` command, you'll next want to type `cargo build`. This will begin compiling the code in debug mode. This mode produces a less optimised version but compiles faster, and is recommended unless the PR you are making involves testing performance.

On the computer I use to compile SurrealDB a clean build takes slightly over two minutes, while recompiling after making a small change takes about 20 seconds. On my previous slower computer this took about three times longer.

To test out your changes, you'll want two open terminal windows. The first will be used to start the database using the `surreal start` command, while the second will use the `surreal sql` command to connect using the CLI. (Or if you are the graphical type, then just use [Surrealist](https://app.surrealdb.com/query) and set up a new connection to the default `localhost:8000`).

Here are the commands that I recommend using when testing a new feature:

- `surreal start --unauthenticated --allow-all` in one window to start the database. The `--unauthenticated` command will let anyone use the database for any purposes without logging in as a user, while `--allow-all` allows normally restricted functionality like SurrealDB's [HTTP functions](/docs/surrealql/functions/database/http).
- `surreal sql --namespace ns --database db --pretty` to start a CLI in the other window inside a namespace called `ns` and a database called `db`. The `--pretty` flag makes the output look a little nicer, and also displays the time it took for a query to execute.

These commands can be used by going to the `/target/debug` folder where your code has been built. Inside a Mac you'll want to add `./` to instruct the system to access the `surrealdb` executable inside this directory, instead of the general `surrealdb` executable that can be run in any directory. You'll know that it is running your build executable if the version number is really long, like this:

```syntax
2025-01-10T03:31:17.177147Z  INFO surreal::env: src/env/mod.rs:12: Running 2.1.4+20250109.40657042.dirty for macos on aarch64
```

Another way to run the executable is just by doing it through Cargo, adding a `--` after which the SurrealDB commands can be passed through.

- `cargo run -- start --unauthenticated --allow-all`
- `cargo run -- sql --namespace ns --database db --pretty`

Personally I prefer going into the directory though because running through Cargo can take a tiny bit longer and produce some extra output like this:

```syntax
mithr@mithr surrealdb % cargo run -- sql --namespace ns --database db --pretty
warning: unused variable: `val2`
  --> crates/core/src/doc/pluck.rs:86:10
   |
86 |                     let val2 = Value::Strand("test".into());
   |                         ^^^^ help: if this is intentional, prefix it with an underscore: `_val2`
   |
   = note: `#[warn(unused_variables)]` on by default
```

But overall, the difference is not that great and you can use whichever method you prefer.

Now that everything is all set up, it's time to make a PR! What change should we make?

# Our tiny, unserious change to the database

Since a real PR that would actually be accepted requires a real issue, and real issues take a good amount of time and code to solve, we'll have to go with an unserious one. Let's put something together that creates a new predefined variable.

Before making a predefined variable, let's make sure that we know what one is.

A [predefined variable](/docs/surrealql/parameters#reserved-variable-names) is one that is automatically set and can be accessed inside a statement. An example of one is `$session`, which contains the data for the current session.

```surrealql
RETURN $session;
```

```surrealql
{
  ac: NONE,
  db: 'sandbox',
  exp: NONE,
  id: NONE,
  ip: NONE,
  ns: 'sandbox',
  or: NONE,
  rd: NONE,
  tk: NONE
}
```

Another example is the variables `$before` and `$after`. These variables exist because by default, SurrealDB returns the output after an operation is over, but you might want to customise your output to return something else instead.

```surrealql
CREATE person;
UPDATE person SET age = 25;
DELETE person;
```

```surrealql
-------- Query 1 (19.9ms) --------

[
  {
    id: person:qbl3yz2wprvl0wp6zgm8
  }
]

-------- Query 2 (2.6ms) --------

[
  {
    age: 25,
    id: person:qbl3yz2wprvl0wp6zgm8
  }
]

-------- Query 3 (500µs) --------

[]
```

One way is by using the keywords `RETURN BEFORE`, `RETURN DIFF`, `RETURN NONE`, `RETURN` plus a list of fields, and so on.

```surrealql
CREATE person RETURN NONE;
UPDATE person SET age = 25 RETURN BEFORE;
DELETE person RETURN BEFORE;
```

```surrealql
-------- Query 1 (400µs) --------

[]

-------- Query 2 (200µs) --------

[
  {
    id: person:gqb09v97e33b8urd6old
  }
]

-------- Query 3 (200µs) --------

[
  {
    age: 25,
    id: person:gqb09v97e33b8urd6old
  }
]
```

But you can also return custom fields, in which case you can also access the value before and after the operation by the parameters `$before` and `$after`.

```surrealql
CREATE person 
    RETURN
    "person created at " + <string>time::now() + "!" AS message,
    $session, 
    $after;
```

```surrealql
[
  {
    after: {
      id: person:b74fnyomgyd4zowipu84
    },
    message: 'person created at 2025-01-10T02:22:40.021Z!',
    session: {
      ac: NONE,
      db: 'sandbox',
      exp: NONE,
      id: NONE,
      ip: NONE,
      ns: 'sandbox',
      or: NONE,
      rd: NONE,
      tk: NONE
    }
  }
]
```

Now that we understand how they work, let's see if we can set up our own predefined variable! It might be nice to have one called `$pep_talk` that has a value of `"You are awesome!"`. Developers can then access this predefined variable every time we feel like getting a little motivation.

# Rummaging through the source code

To make this change, let's see if we can find where the variables `$before` and `$after` are set up. Since we are in no way familiar with the source code yet, let's just open up an IDE like Visual Studio Code and do a search for `$before`. Doing so takes us to [this piece of code](https://github.com/surrealdb/surrealdb/blob/406570424403bd55dc6cd82a3778f471da7be07c/crates/core/src/doc/lives.rs#L90), which looks pretty close to the spot we want! This section deals with [live queries](/docs/surrealql/statements/live) in particular which is not what we want, but we can see some lines that are clearly setting variables including the ones we saw before: "session", "after", and "before".

Reading the code, it looks like these parameters are added using a method called `.add_value()` which and takes simple strings for their name. The `$` must be added afterwards, and we won't have to think about that part.

```rust
// Add the session params to this LIVE query, so
// that queries can use these within field
// projections and WHERE clauses.
lqctx.add_value("access", sess.pick(AC.as_ref()).into());
lqctx.add_value("auth", sess.pick(RD.as_ref()).into());
lqctx.add_value("token", sess.pick(TK.as_ref()).into());
lqctx.add_value("session", sess.clone().into());
// Add $before, $after, $value, and $event params
// to this LIVE query so the user can use these
// within field projections and WHERE clauses.
lqctx.add_value("event", met.into());
lqctx.add_value("value", current.clone());
lqctx.add_value("after", current);
lqctx.add_value("before", initial);
```

Now let's do a search for `.add_value("` to see what other places this method is being used. The search results show the method used in about a dozen or so places, but one of them stands out in particular thanks to a comment above the code. It appears to be inside a function called [`pluck()`](https://github.com/surrealdb/surrealdb/blob/406570424403bd55dc6cd82a3778f471da7be07c/crates/core/src/doc/pluck.rs#L20). Here is the comment:

```rust
/// Evaluates a doc that has been modified so that it can be further computed into a result Value
/// This includes some permissions handling, output format handling (as specified in statement),
/// field handling (like params, links etc).
```

That sounds about right! Further down in the code we can see a `match` statement that tells the program what to do when it gets a certain instruction on what sort of output to return. The `Output::None`, `Output::Null`, `Output::Diff`, `Output::After`, and `Output::Before` variants all seem to match with the statements we saw before like `RETURN BEFORE` and `RETURN AFTER`. The final variant is `Output::Fields`, which is when the user customises the output like we did. And it's inside there that "before" and "after" are set!

```rust
// Process the desired output
let mut out = match stm.output() {
  Some(v) => match v {
    Output::None => Err(Error::Ignore),
    Output::Null => Ok(Value::Null),
    Output::Diff => {
      // Process the permitted documents
      let (initial, current) = match self.reduced(stk, ctx, opt, Both).await? {
        true => (&self.initial_reduced, &self.current_reduced),
        false => (&self.initial, &self.current),
      };
      // Output a DIFF of any changes applied to the document
      Ok(initial.doc.as_ref().diff(current.doc.as_ref(), Idiom::default()).into())
    }
    Output::After => {
      // Process the permitted documents
      match self.reduced(stk, ctx, opt, Current).await? {
        // This is an already processed reduced document
        true => Ok(self.current_reduced.doc.as_ref().to_owned()),
        // Output the full document before any changes were applied
        false => {
          self.current
            .doc
            .as_ref()
            .compute(stk, ctx, opt, Some(&self.current))
            .await
        }
      }
    }
    Output::Before => {
      // Process the permitted documents
      match self.reduced(stk, ctx, opt, Initial).await? {
        // This is an already processed reduced document
        true => Ok(self.initial_reduced.doc.as_ref().to_owned()),
        // Output the full document before any changes were applied
        false => {
          self.initial
            .doc
            .as_ref()
            .compute(stk, ctx, opt, Some(&self.initial))
            .await
        }
      }
    }
    Output::Fields(v) => {
      // Process the permitted documents
      let (initial, current) = match self.reduced(stk, ctx, opt, Both).await? {
        true => (&mut self.initial_reduced, &mut self.current_reduced),
        false => (&mut self.initial, &mut self.current),
      };
      // Configure the context
      let mut ctx = MutableContext::new(ctx);
      ctx.add_value("after", current.doc.as_arc());
      ctx.add_value("before", initial.doc.as_arc());
      let ctx = ctx.freeze();
      // Output the specified fields
      v.compute(stk, &ctx, opt, Some(current), false).await
    }
  },
```

So we should be able to add our own predefined variable here! We will start with `ctx.add_value("pep_talk"` and then follow it up with...some value. But what? The second parameter in this `.add_value()` function isn't clear to us.

```rust
ctx.add_value("after", current.doc.as_arc());
ctx.add_value("before", initial.doc.as_arc());
```

# Letting the Rust compiler do the work for you

This is where Rust's strict typing system and helpful compiler come in handy. If the code won't compile unless it is correct, and the compiler often knows what we are trying to do, we can just try completing the method with whatever comes to mind and see what the compiler says.

Let's just end this with the string that we'd like to output and see what the compiler says.

```rust
ctx.add_value("pep_talk", "You are awesome!");
```

The error output is pretty good! Though the code didn't work, we now know that it's because the method wants to see some type called `Arc<sql::value::value::Value>`.

```syntax
error[E0308]: mismatched types
   --> crates/core/src/doc/pluck.rs:87:32
    |
87  |                     ctx.add_value("pep_talk", "You are awesome!");
    |                         ---------             ^^^^^^^^^^^^^^^^^^ expected `Arc<Value>`, found `&str`
    |                         |
    |                         arguments to this method are incorrect
    |
    = note: expected struct `Arc<sql::value::value::Value>`
            found reference `&'static str`
note: method defined here
   --> crates/core/src/ctx/context.rs:236:16
    |
236 |     pub(crate) fn add_value<K>(&mut self, key: K, value: Arc<Value>)
    |                   ^^^^^^^^^                       -----------------
```

A quick Google for "Rust Arc" will take us directly to [this page](https://doc.rust-lang.org/std/sync/struct.Arc.html). Okay, it looks like an `Arc` is atomically safe reference counter. And creating one is as simple as calling `Arc::new()` and putting something inside, as one of the examples on that page shows.

```rust
let five = Arc::new(5);
```

So we will need to `Arc::new()` and put something called a `Value` in.

Now let's see what a `Value` is. The error message displays it as `sql::value::value::Value`, so that's [the path we'll follow](https://github.com/surrealdb/surrealdb/blob/main/crates/core/src/sql/value/value.rs#L91) to find it. This takes us to something called an `enum Value`. It's pretty clear that this enum is a way to represent the various data types you'll see in the database such as numbers, durations, datetimes, objects, and so on.

```rust
pub enum Value {
  // These value types are simple values which
  // can be used in query responses sent to
  // the client. They typically do not need to
  // be computed, unless an un-computed value
  // is present inside an Array or Object type.
  // These types can also be used within indexes
  // and sort according to their order below.
  #[default]
  None,
  Null,
  Bool(bool),
  Number(Number),
  Strand(Strand),
  Duration(Duration),
  Datetime(Datetime),
  Uuid(Uuid),
  Array(Array),
  Object(Object),
  Geometry(Geometry),
  Bytes(Bytes),
  Thing(Thing),
  // These Value types are un-computed values
  // and are not used in query responses sent
  // to the client. These types need to be
  // computed, in order to convert them into
  // one of the simple types listed above.
  // These types are first computed into a
  // simple type before being used in indexes.
  Param(Param),
  Idiom(Idiom),
  Table(Table),
  Mock(Mock),
  Regex(Regex),
  Cast(Box<Cast>),
  Block(Box<Block>),
  #[revision(end = 2, convert_fn = "convert_old_range", fields_name = "OldValueRangeFields")]
  Range(OldRange),
  #[revision(start = 2)]
  Range(Box<Range>),
  Edges(Box<Edges>),
  Future(Box<Future>),
  Constant(Constant),
  Function(Box<Function>),
  Subquery(Box<Subquery>),
  Expression(Box<Expression>),
  Query(Query),
  Model(Box<Model>),
  Closure(Box<Closure>),
  // Add new variants here
}
```

The one that we are looking for is a string, and it will be one of the possibilities listed in the top which are said to be "values which can be used in query responses". The ones on the bottom aren't used in query responses, so we don't want that.

Let's see...we know that we don't want None, or Null, or Bool, or Number, or Duration, or Datetime, or Uuid, or Array, or Object, or Geometry, or Bytes. That leaves Strand and Thing. `Strand` is probably the one we want, so let's take a look at [that page](https://github.com/surrealdb/surrealdb/blob/main/crates/core/src/sql/strand.rs#L20).

```rust
/// A string that doesn't contain NUL bytes.
#[revisioned(revision = 1)]
#[derive(Clone, Debug, Default, Eq, PartialEq, Ord, PartialOrd, Serialize, Deserialize, Hash)]
#[serde(rename = "$surrealdb::private::sql::Strand")]
#[cfg_attr(feature = "arbitrary", derive(arbitrary::Arbitrary))]
#[non_exhaustive]
pub struct Strand(#[serde(with = "no_nul_bytes")] pub String);
```

The comment describes it as `A string that doesn't contain NUL bytes`, that sounds about right!

So how do we construct a `Value` that is a `Strand`? Let's look at come more code inside the `value.rs` page. About 150 lines down there are tons of examples showing these `Value` variants being created.

```rust
impl From<bool> for Value {
  #[inline]
  fn from(v: bool) -> Self {
    Value::Bool(v)
  }
}

impl From<Uuid> for Value {
  fn from(v: Uuid) -> Self {
    Value::Uuid(v)
  }
}

impl From<Closure> for Value {
  fn from(v: Closure) -> Self {
    Value::Closure(Box::new(v))
  }
}

impl From<Param> for Value {
  fn from(v: Param) -> Self {
    Value::Param(v)
  }
}
```

So we should be able to use `Value::Strand()` with a string inside. Let's give that a try! We'll first try to create a variable called `pep_talk` which is a `Value::Strand`.

```surrealql
Output::Fields(v) => {
  // Process the permitted documents
  let (initial, current) = match self.reduced(stk, ctx, opt, Both).await? {
    true => (&mut self.initial_reduced, &mut self.current_reduced),
    false => (&mut self.initial, &mut self.current),
  };
  // Configure the context
  let mut ctx = MutableContext::new(ctx);
  ctx.add_value("after", current.doc.as_arc());
  ctx.add_value("before", initial.doc.as_arc());
  let pep_talk = Value::Strand("You are awesome!"); // This line
  let ctx = ctx.freeze();
  // Output the specified fields
  v.compute(stk, &ctx, opt, Some(current), false).await
}
```

Not quite, but once again the compiler tells us exactly what to do. The type that we entered is called a `&str`, but the compiler expected a `Strand`. On the line below, it lets us know that we can just add `.into()` because apparently our input can be converted into a `Strand` by doing this. Sounds easy enough!

```syntax
error[E0308]: mismatched types
   --> crates/core/src/doc/pluck.rs:85:35
    |
85  |                     let pep_talk = Value::Strand("You are awesome!");
    |                                    ------------- ^^^^^^^^^^^^^^^^^^ expected `Strand`, found `&str`
    |                                    |
    |                                    arguments to this enum variant are incorrect
    |
note: tuple variant defined here
   --> crates/core/src/sql/value/value.rs:104:2
    |
104 |     Strand(Strand),
    |     ^^^^^^
help: call `Into::into` on this expression to convert `&'static str` into `sql::strand::Strand`
    |
85  |                     let pep_talk = Value::Strand("You are awesome!".into());
    |                                                                    +++++++
```

So now we can just stick this into a new line containing `ctx.add_value`. And don't forget to wrap the `Value` inside `Arc::new()`!

```rust
Output::Fields(v) => {
  // Process the permitted documents
  let (initial, current) = match self.reduced(stk, ctx, opt, Both).await? {
    true => (&mut self.initial_reduced, &mut self.current_reduced),
    false => (&mut self.initial, &mut self.current),
  };
  // Configure the context
  let mut ctx = MutableContext::new(ctx);
  ctx.add_value("after", current.doc.as_arc());
  ctx.add_value("before", initial.doc.as_arc());
  let pep_talk = Value::Strand("You are awesome!".into()); // Our code
  ctx.add_value("pep_talk", Arc::new(pep_talk)); // Our code
  let ctx = ctx.freeze();
  // Output the specified fields
  v.compute(stk, &ctx, opt, Some(current), false).await
}
```

# Trying out the code and adding a test

No more errors are showing up in the IDE anymore, so let's give it a try.

Type `cargo build` and go into the `/target/debug` directory to use the `surreal start` and `surreal sql` commands above, or type `cargo run -- start --unauthenticated --allow-all` in one terminal window and `cargo run -- sql --namespace ns --database db --pretty` in another.

So does it work?

It sure does! We now have access to a quick `$pep_talk` any time we are working with a statement like CREATE or UPDATE.

```syntax
ns/db> CREATE person RETURN $pep_talk;
-- Query 1 (execution time: 5.159042ms)
[
  {
    pep_talk: 'You are awesome!'
  }
]

ns/db> UPDATE person RETURN $before, $pep_talk AS nice_speech, time::now() AS time_of_query;
-- Query 1 (execution time: 2.79125ms)
[
  {
    before: {
      id: person:2lyuxch0cx31o09bfbfu
    },
    nice_speech: 'You are awesome!',
    time_of_query: d'2025-01-10T05:20:17.393290Z'
  }
]
```

Before submitting a PR, it might be a good idea to add a test or two. Tests in Rust can be located anywhere, and are simply made by adding an annotation to a function that designates it as a test function.

Because there are many such tests in the source code already, you can just find an existing test like [this one](https://github.com/surrealdb/surrealdb/blob/main/crates/sdk/tests/field.rs#L406) that tests a query and its output...

```rust
#[tokio::test]
async fn field_definition_array_any() -> Result<(), Error> {
  let sql = "
    DEFINE TABLE user SCHEMAFULL;
    DEFINE FIELD custom ON user TYPE array<any>;
    INFO FOR TABLE user;
  ";
  let mut t = Test::new(sql).await?;
  t.skip_ok(2)?;
  t.expect_val(
    "
{
  events: {  },
  fields: { custom: 'DEFINE FIELD custom ON user TYPE array PERMISSIONS FULL' },
  indexes: {  },
  lives: {  },
  tables: {  }
}
    ",
  )?;
  Ok(())
}
```

...and then just modify the query and the expected output. A test for our `$pep_talk` variable could then look like this.

```rust
#[tokio::test]
async fn pep_talk() -> Result<(), Error> {
  let query = "CREATE person:one RETURN *, $pep_talk;";
  let mut t = Test::new(query).await?;
  t.expect_val(
    "
[
  {
    id: person:one,
    pep_talk: 'You are awesome!'
  }
]
    ",
  )?;
  Ok(())
}
```

Once this is over, then just submit the PR as you would to any other repo! A PR submitted to the `/surrealdb` repo contains an automatically generated template to fill out that contains a few fields such as:

- What is the motivation?
- What does this change do?
- What is your testing strategy?

And so on. It also contains a checkbox to make sure that you have [read the contributing guidelines](https://github.com/surrealdb/surrealdb/blob/main/CONTRIBUTING.md). Once the PR is submitted, the tests will run and the SurrealDB team will see that a PR has been submitted. And if the PR is accepted, it will be merged into main and included in the next release!
