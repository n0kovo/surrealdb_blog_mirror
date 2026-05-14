---
title: "Why SurrealDB is the Future of Database Technology - An In-Depth Look"
slug: "why-surrealdb-is-the-future-of-database-technology--an-in-depth-look"
date: "2024-05-09T00:00:00.000Z"
categories:
  - "community"
  - "tutorials"
read_time: "17 min read"
summary: "The people who are crazy enough to think that they can change the world, are the ones who do"
source: "https://surrealdb.com/blog/why-surrealdb-is-the-future-of-database-technology--an-in-depth-look"
cover: "../../assets/f400131e23366c15.jpg"
---

# Why SurrealDB is the Future of Database Technology - An In-Depth Look

![Why SurrealDB is the Future of Database Technology - An In-Depth Look](../../assets/f400131e23366c15.jpg)

> Here's to the crazy ones, the misfits, the rebels, the troublemakers, the round pegs in the square holes... the ones who see things differently -- they're not fond of rules, and they have no respect for the status quo... You can quote them, disagree with them, glorify or vilify them, but the only thing you can't do is ignore them because they change things... They push the human race forward, and while some may see them as the crazy ones, we see genius, because the people who are crazy enough to think that they can change the world, are the ones who do. - [Apple, 1997](https://www.youtube.com/watch?v=5sMBhDv4sik)

The conventional wisdom would be to build upon an existing ecosystem, focusing on one thing and then gradually expanding your capabilities carefully over years or even decades.

A crazy thing to do would be to create the ultimate multi-model database, or in simple terms, an "everything database" from scratch, all at once.

The conventional wisdom would be to join a start-up accelerator in Silicon Valley and grow the team locally as a US-based company.

A crazy thing to do would be to start a London-based but globally distributed company with your brother, and have your mother do the first screening of all your early employees.

The conventional wisdom would be to choose black, blue or green as your brand colours.

A crazy thing to do would be choosing pink and purple as your brand colours.

The conventional wisdom would be to choose C or C++ for building your database.

A crazy thing to do would be [betting on Rust](/blog/why-we-are-betting-on-rust) for building your database.

The conventional wisdom would be to hire top engineers from prestigious companies as your first employees.

A crazy thing to do would be hiring an opera singer as your first employee and a [founder with an accounting degree, based in Zimbabwe](/blog/maintainer-month-2023-behind-the-scenes-with-rushmore-mushambi) as your first engineering employee.

As the results show, however, not being blinded by conventional wisdom has been vital in assembling our team of truly world-class rebel geniuses, pushing the boundaries of what databases (and database companies) can or even should do.

Now that we've established that we are, by all accounts, "the crazy ones", let's dive into the change we want to see in the world and how we are pushing the database industry forward!

## Ghosts of databases past

> 欲知未來 先察已然 / Study the Past if You Would Define the Future. - Confucius

[Ebenezer Scrooge](https://en.wikipedia.org/wiki/Ebenezer_Scrooge) needed to understand his past and present to realise the painful future ahead of him unless he made significant changes. Just like Scrooge, we need to understand a bit about the past and present of database decisions to realise why the changes we made in SurrealDB enable you to avoid a painful future as well.

The most crucial thing to understand is that the developers of every database, old and new, are presented with a choice that has greater implications than any other.

Which database, if any, are you going to be compatible with?

### The Faustian bargain

Unless the change you want to see in the world is simply to be the best hosting provider of a commodity database, that question quickly turns into a [Faustian bargain.](https://www.britannica.com/topic/Faustian-bargain)

A Faustian bargain is a deal where you trade something of supreme importance such as your values or even your soul, in exchange for material benefits such as power or riches.

For startups, the conventional wisdom says you should take this deal, which often means building upon or being compatible with a popular legacy database to more easily capture market share.

This sounds reasonable, and at first it might make things easier, but that one decision will force you to make countless more and, perhaps without even realising it, you have now chained yourself to design decisions made in the previous century, decisions that made sense for a world that no longer exists.

Not to mention that to be truly compatible, you need to be [bug-for-bug compatible](https://www.techopedia.com/definition/18104/bug-compatible) which means you either have to introduce matching bugs in your code or spend a lot of your limited time fixing bugs in the legacy database at the expense of features in your new database.

There is also the option of using marketing instead of engineering and claiming compatibility but with a lot of fine print:

> We're legacy database compatible\*\*\* - trust me bro

This also puts a ceiling on your innovation by constraining yourself to only incremental innovation:

- legacy database, but faster
- legacy database, but distributed
- legacy database, but with better marketing

A classic [innovator's dilemma:](https://en.wikipedia.org/wiki/The_Innovator%27s_Dilemma)

> If I had asked people what they wanted, they would have said faster horses. - Henry Ford

This type of innovation can certainly help you improve the world. However, only disruptive innovation, like Henry Ford's cars, can change the world and move us into the future.

You might have started out with a grand vision, but through a series of reasonable compromises ended up [same same, but different.](https://www.youtube.com/watch?v=lXO0ylemz68) An innovative square peg that forced itself through a cookie cutter to fit through the round hole.

> The reasonable man adapts himself to the world: the unreasonable one persists in trying to adapt the world to himself. Therefore all progress depends on the unreasonable man. - George Bernard Shaw

Faustian bargains are therefore by their nature tragic or self-defeating for those who make them, because what is surrendered is ultimately far more valuable than what is obtained.

### To build or not to build

The second most important choice the developers of every database make is choosing which parts to build as your core product and which parts to rely on others for.

The conventional wisdom here again is focusing on one key idea. This usually means being best-of-breed for one thing and integrating with other best-of-breed products. It may also mean integrating with an ecosystem of extensions for functionality outside this one key idea.

This is also reasonable advice as it allows database developers to offload a lot of complexity to the end users.

As an end user of a database however, this will come back to haunt you, unless you're making the simplest of CRUD applications.

For most modern applications you now have to hunt down multiple databases, extensions or services and evaluate them to decide which ones are the best fit. They all come with their own limitations, various APIs and release cycles.

Not to mention each needing approval from IT and dealing with different maintenance guarantees. Either you put your critical infrastructure into the hands of [a random person in Nebraska](https://www.explainxkcd.com/wiki/index.php/2347:_Dependency) or you pay a premium for each best-of-breed database or extension, which often costs the same or more as your original database did because the other database or extension developers also need to make a living.

Before you know it, you'll have abstractions upon abstractions, managing a microservice architecture made up of expensive managed services in a data merry-go-round of your best-of-breed databases and extensions.

> complexity very, very bad. - [Grug](https://grugbrain.dev/#grug-on-complexity)

Nobody plans an overly complex system, but as the eight-time entrepreneur-turned-educator Steve Blank famously said:

> No Plan Survives First Contact With Customers. - [Steve Blank](https://steveblank.com/2010/04/08/no-plan-survives-first-contact-with-customers-%E2%80%93-business-plans-versus-business-models)

With all their requests, customers will force you into complexity, one way or another. This sets off a chain reaction resulting in databases being forced to abandon the idea of just doing one key thing and supporting more features, whether it makes sense to or not.

As an example, [PostgreSQL was forced to add JSON support](https://www.postgresql.org/docs/current/datatype-json.html) and [MongoDB was forced to add SQL support](https://www.mongodb.com/docs/atlas/data-federation/query/query-with-sql). Giving rise to [patchwork systems](https://tbtech.co/news/patchwork-systems-are-more-than-just-an-annoyance), which force new incompatible models on top of the old ones and call it a stack (don't forget to read the fine print).

> Everyone has a plan until they get punched in the face. - Mike Tyson

After being repeatedly punched in the face by the complex systems customers require you to build, you have three choices:

- Give up and go work on a farm
- Roll with the punches and learn to live with it
- [Dream of something better](/blog/dreaming-of-something-better) and fight back against the complexity!

## A new hope

> An elegant weapon for a more civilized age. - Obi-Wan Kenobi

At a high level, SurrealDB aims to be an elegant weapon cutting through the complexity of traditional systems and [making building fun again!](/blog/eli5-why-surrealdb-explained-through-building-with-lego)

Our vision is to be the ultimate data platform for tomorrow’s technology by being the most powerful multi-model database platform and serverless cloud offering for developers, SMEs and enterprises.

To achieve this vision, we have had to let go of conventional wisdom because:

> We can't solve problems by using the same kind of thinking we used when we created them. - Albert Einstein

But it’s not enough to think differently, we also need to execute differently!

> If you want something new, you have to stop doing something old. - Peter Drucker

This is why we have been innovating across every layer of the database to bring you a data platform where features from document, graph, transactional, time-series, temporal, full-text search, vector search, machine learning and more all work seamlessly together, because it’s all one coherent system.

### Storage layer innovation

#### Separation of storage and compute

![separation of storage and compute](../../assets/c6e66db0933e50d7.jpg)

One key architectural decision was the separation of storage and compute. This has been a trend that started with analytical databases (OLAP) and which has since made its way into operational databases (OLTP).

The key reason for separating storage and compute is so that you can scale your resources separately. This has several benefits such as:

- Less wasted capacity as scale is optimised for each workload
- Greater cost efficiency
- Greater flexibility
- Better fault tolerance

As we'll cover in more detail when we get to deployment, SurrealDB takes storage and compute separation to the next level by offering unparalleled deployment flexibility!

#### Creating a new data structure for our new key-value store

![vart](../../assets/8934dca00ec9a8e3.jpg)

We currently use a [range of leading key-value stores](/docs/surrealdb/introduction/architecture) depending on whether you're running SurrealDB embedded, single node, distributed, or directly in the browser. While they are all the best at what they do, we need them to do more!

In order to achieve our mission of enabling the world to access data in the most powerful way, we need more powerful key-value stores!

That is why we are building [SurrealKV](https://github.com/surrealdb/surrealkv), our own native ACID-compliant storage engine, written in Rust. SurrealKV will enable versioned queries over time, immutable data querying, data change auditing, historic aggregate query analysis, and versioned graph queries.

This goes well beyond the simple time travel or temporal tables you might be familiar with. It enables SurrealDB to be a [native temporal database](https://en.wikipedia.org/wiki/Temporal_database), further extending our multi-model approach to cover Bitemporal modelling efficiently (optimised storage) and performantly (optimised compute) at the storage layer without all the complexity and effort of [trying to do it yourself](https://www.abhinavomprakash.com/posts/understanding-bitemporal-data) at the query layer.

To achieve this we needed to design a new data structure, [an Immutable Versioned Adaptive Radix Trie (VART)](/blog/vart-a-persistent-data-structure-for-snapshot-isolation).

> The term "**Versioned**" in VART signifies the use of versioning, indicating a chronological record of every modification made to the tree.

>

> The "**Adaptive**" attribute refers to the dynamic node sizes and the path compression technique, aimed at optimising space utilisation and enhancing overall performance.

>

> Lastly, the "**Radix Trie**" component underscores the adoption of a tree-like data structure, specifically tailored for storing associative arrays. - [Farhan Ali Khan](/blog/vart-a-persistent-data-structure-for-snapshot-isolation)

Our journey building SurrealKV is still in its early stages but moving at an unbelievably fast pace and we already have an [experimental release.](https://www.youtube.com/watch?v=kQQV2kDFHQA)

If you also want a more powerful key-value store, we'd love for you to [contribute, provide feedback, or report issues](https://github.com/surrealdb/surrealkv) to help shape the future of SurrealKV!

### Query layer innovation

#### Record IDs

It all starts with [the life-changing magic of SurrealDB record IDs.](/blog/the-life-changing-magic-of-surrealdb-record-ids) A record ID has two parts, a table name and a record identifier, which looks like this `table:record`.

The key innovation here is that when doing [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) with a record ID, you don't have to do a table scan, it just directly fetches the record from the key-value store!

```surrealql
SELECT * FROM the_future:m3laj0u0r5gb03d9b6rq;
```

Because it is directly fetching the record, it will always be fast, regardless of scale.

Compared with having to rely on table scans, which get slower the more data you have.

```surrealql
SELECT * FROM the_past
WHERE id = 124316249;
```

This brings us to the second key point, introducing helpful default options that work well as you scale.

Instead of the traditional default of auto-increment or serial IDs you might be used to from legacy databases, when you create a record in the future table:

```surrealql
CREATE the_future;
```

A random ID is assigned:

```surrealql
the_future:m3laj0u0r5gb03d9b6rq
```

This allows you to avoid common scaling problems such as:

- Auto incrementing that locks, impacting concurrency and scalability of your database.
- Accidental information disclosure through using IDs in URLs, giving away data size and velocity.
- Non-uniqueness across tables or table shards across distributed nodes.

If sequential IDs are needed, we’d recommend you [use either a ulid or a uuid v7.](/docs/surrealql/functions/database/rand#randuuidv7)

```surrealql
CREATE the_future:ulid();
CREATE the_future SET id = rand::uuid::v7();
```

The integer as primary key defaults made sense for the world in which they were taken, the world before the internet, but they don't make sense anymore.

By having helpful defaults we want to make it as easy as possible to [fall into the pit of success:](https://english.stackexchange.com/questions/77535/what-does-falling-into-the-pit-of-success-mean)

> The Pit of Success: in stark contrast to a summit, a peak, or a journey across a desert to find victory through many trials and surprises, we want our customers to simply fall into winning practices by using our platform and frameworks. To the extent that we make it easy to get into trouble we fail. - [Rico Mariani](https://english.stackexchange.com/questions/77535/what-does-falling-into-the-pit-of-success-mean)

#### Native multi-model

![multi-model](../../assets/463eae0ec13100ee.jpg)

Earlier we talked about customers forcing complexity on you and databases needing to adapt by forcing new incompatible models on top of the old ones, JSON on top of SQL and SQL on top of JSON.

The problem you end up with there is a great experience for the original data model but a second-class experience, or worse, for the other data models forced on top of it. You might need to learn a whole different query language for the different data models and have all sorts of limitations, which the original data model doesn't have.

The [native multi-model database](/blog/what-are-multi-model-databases) solves these problems by making all the data models (document, graph, relational, etc) the original data model and having one unified query language. In our case, the SQL-like query language SurrealQL, which comes with many quality-of-life improvements over other SQL dialects.

For SurrealDB this means integrating the good parts of each data model seamlessly together.

For example, being schemaless by default allows for rapid prototyping, which is a great thing about the document model.

```surrealql
CREATE free_future CONTENT {
  message: "Freedom!!"
};
```

As well as being fully ACID compliant and schemafull, which are great things about the relational model.

```surrealql
DEFINE TABLE safe_future SCHEMAFULL;
DEFINE FIELD id ON safe_future TYPE record<safe_future>;
DEFINE FIELD message ON safe_future TYPE string
-- lets also make sure the message is more then 1 letter
ASSERT string::len($value) > 1;

INSERT INTO safe_future (message) VALUES ('lock it down!');
```

Or even something in between, a schemafull table with schemaless flexible fields.

```surrealql
DEFINE TABLE flexible_future SCHEMAFULL;
DEFINE FIELD metadata ON flexible_future FLEXIBLE TYPE object;

INSERT INTO flexible_future {
  metadata: {
    message: "so meta!"
  }
};
```

When we were taking the decision of how to make relationships between our data, we decided to go [beyond SQL Joins](/blog/beyond-sql-joins-exploring-surrealdbs-multi-model-relationships) and instead use [document record links](https://www.youtube.com/watch?v=TyX45cyZ-W0) and [graph relationships](https://www.youtube.com/watch?v=zwQwKvMa9sU) because establishing the relationships at write time makes it simpler and easier for everyone at query time.

```surrealql
-- Using record links to select from the person and product table
SELECT
rating,
person.name,
product.name AS product_name
FROM review;

-- Using graph relations to select from the person and product table
SELECT
order_date,
product_name,
<-person.name AS person_name,
->product.description
FROM order;
```

#### Real-time data sync

![lq](../../assets/ca7466ca840ec29d.jpg)

Streaming real-time transactional data is a difficult problem to solve, which is exactly why we made it extremely easy for you.

[Live Queries](/features) in SurrealDB enable a simple yet seamless way of building modern, responsive applications, whether connecting to SurrealDB as a traditional backend database, or when connecting directly to the database from the frontend.

Live Queries give developers the ability to receive real-time change notifications to data as it is happening. Integrated directly within the table, row, and field level permissions of SurrealDB, each Live Query notification is unique and tailored to the authentication of the user who issued the query.

Regardless of what a user has subscribed to, notifications will only be delivered based on the authenticated session of that user.

To make a query like this one a Live Query...

```surrealql
SELECT message FROM the_future;
```

...all it takes is one magic word to [unlock streaming data magic](/blog/unlocking-streaming-data-magic-with-surrealdb-live-queries-and-change-feeds)

```surrealql
LIVE SELECT message FROM the_future;
```

And by bringing the simplicity of Live Queries alongside the advanced nature of [pre-defined aggregate views](/docs/surrealql/statements/define/table#pre-computed-table-views), you can now build powerful dashboards that rely on aggregate data queries, computationally expensive analytics queries, and filtered collections of massive data sets - that update in real-time as your data in the database changes.

#### Machine learning made easy

![ml](../../assets/d70ead09eff53d4c.jpg)

[SurrealML](/features) enables machine learning models to be greatly simplified, ensuring reproducibility and consistency in machine learning pipelines. Running on our Rust engine, models can be built in Python and imported into SurrealDB for inference within the database runtime.

With support for model versioning, machine learning pipelines can be further simplified, bringing consistency and reproducibility to data normalisation and model inference, allowing for execution across multiple different Python versions, environments, and platforms.

[It's easy to get started](/blog/what-is-surrealml-a-getting-started-guide) and once a model is uploaded to SurrealDB you can use it directly in SurrealQL.

```surrealql
SELECT
  ml::house-price-prediction<0.0.1>({
    squarefoot: squarefoot_col,
    num_floors: num_floors_col
  }) AS price_prediction
FROM house_listing;
```

#### Indexing reimagined

![ix](../../assets/5a67454bfe2c8e92.jpg)

SurrealDB has support for traditional [indexing](/docs/surrealql/statements/define/indexes), unique indexes and constraints, full-text search indexes, and vector-embedding indexing.

We reimagined how indexing might be implemented - opting for a completely custom-built indexing engine, which sits within the SurrealDB core itself without the need for an additional external query language, or for indexing-specific functions or plugins.

```surrealql
DEFINE INDEX userEmailIndex ON TABLE user COLUMNS email UNIQUE;
```

The indexing engine is agnostic to its deployment environment - whether running on top of IndexedDB in the browser, an embedded run-time in Rust or Python, or distributed over multiple nodes in a highly scalable cluster.

Using the [full-text search](/docs/surrealdb/models/full-text-search) indexing engine, SurrealDB allows developers to define custom analysers which specify exactly how their text data should be processed, with support for multiple tokenisers, advanced filters including Ngram, EdgeNGram, and Snowball, and support for 17 languages from English to Arabic.

```surrealql
DEFINE INDEX userNameIndex ON TABLE user COLUMNS name SEARCH ANALYZER ascii BM25 HIGHLIGHTS;
```

With [vector-embedding indexing](/docs/surrealql/statements/define/indexes#vector-search-indexes), our initial implementation supports exact nearest neighbour retrieval for vectors of arbitrary size using Metric Trees, with support for HNSW-based approximate nearest neighbours retrieval coming soon.

```surrealql
DEFINE INDEX mt_pt ON pts FIELDS point MTREE DIMENSION 4;
```

[In the example below](/docs/surrealql/statements/define/indexes#brute-force-method), the query searches for points closest to the vector `[2,3,4,5]` and uses the [vector::distance::euclidean](/docs/surrealql/functions/database/vector#vectordistanceeuclidean) function to calculate the distance between two points, indicated by `<|2|>`.

```surrealql
LET $pt = [2,3,4,5];
SELECT
  id,
  vector::distance::euclidean(point, $pt) AS dist
FROM pts
WHERE point <|2|> $pt;
```

### Deployment innovation

![deploy](../../assets/fa484180542850f7.jpg)

As mentioned above, SurrealDB takes storage and compute separation to the next level!

Some companies have gone through the herculean effort of retrofitting a legacy database with decades of tech debt into a cloud-native solution with a custom storage backend, usually including some form of S3 object storage.

Others have created a cloud-native database from scratch, which is compatible with a particular legacy database.

What they all tend to have in common is that they are cloud-native, but also cloud-only because the architecture is custom-made with the cloud in mind.

SurrealDB was designed from the start to have unparalleled deployment flexibility, combining the ease of use of embedded databases such as SQLite and the power of client-server databases with all our multi-model features into [a single Rust binary!](https://github.com/surrealdb/surrealdb)

This means you have access to all the features wherever you are running SurrealDB:

- [In embedded devices and IoT](/docs/surrealdb/embedding/rust)
- [As a single-node, in-memory server](/docs/surrealdb/installation/running/memory)
- [As a single-node, on-disk server](/docs/surrealdb/installation/running/file)
- [As a multi-node, scalable cluster](/docs/surrealdb/installation/running/tikv)
- [Embedded directly in the web browser using Web Assembly](https://github.com/surrealdb/surrealdb.wasm)

As seeing is believing, you can check out the same SurrealDB that runs distributed, running in Web Assembly and storing data to your browser right now [using our official management interface](https://app.surrealdb.com), you don't even have to log in!

With unparalleled deployment flexibility, you naturally also need flexibility in how you connect to the database. That is why we offer [SDKs for various languages](/docs/surrealdb/integration/sdks) such as Rust, JavaScript, Python, Golang, Java, and more!

You can also connect directly to the database using our [RESTful HTTP endpoints](/docs/surrealdb/integration/http) or our unified [RPC protocol](/docs/surrealdb/integration/rpc), supporting both WebSockets and using HTTP to `POST` to the `/rpc` endpoint.

## Stepping into the future

> You cannot predict the future, but you can create it. - Peter Drucker

As we have seen, the change SurrealDB wants to see is to enable the world to access data in the most powerful way while simultaneously reducing your total system complexity, by offering a coherent data platform where everything works seamlessly together.

Help us push the database industry forward by taking a step ahead into the future with us by signing up for the [SurrealDB cloud waitlist](/cloud) or exploring [SurrealDB](https://github.com/surrealdb/surrealdb) right in your browser using [Surrealist.](https://app.surrealdb.com)
