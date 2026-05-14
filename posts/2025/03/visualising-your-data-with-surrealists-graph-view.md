---
title: "Visualising your data with Surrealist's Graph view"
slug: "visualising-your-data-with-surrealists-graph-view"
date: "2025-03-13T00:00:00.000Z"
categories:
  - "tutorials"
  - "featured"
read_time: "11 min read"
summary: "We as humans love visual data, and the new graph view for Surrealist provides exactly this."
source: "https://surrealdb.com/blog/visualising-your-data-with-surrealists-graph-view"
cover: "../../assets/4f3312d1475b5373.jpg"
---

# Visualising your data with Surrealist's Graph view

![Visualising your data with Surrealist's Graph view](../../assets/4f3312d1475b5373.jpg)

## Why we love visual data

Nothing drives a point home like a good visualisation. Our languages show this too, with the famous "One picture is worth a thousand words" maxim found in languages around the globe:

- 百聞不如一見 (seeing once beats hearing 100 times) in Chinese,
- "Un bon croquis vaut mieux qu'un long discours" (a good sketch is better than a long speech) in French,

and so on.

We are visual creatures, and this can be seen in our writing. Even the writing we use in English today is a direct descendent of Egyptian hieroglyphs, which originates from less structured symbols, which themselves come from prehistoric drawings.

In fact, every letter in our alphabet, and thus this blog post, is an abstraction of something that used to be an image.

For example, the letter B comes from the `𓉐` character, which was pronounced PR and represents a house. The Phoenicians then used it to make their letter `𐤁` (bet) -> the Greeks used that to make their letter beta (`β`) -> the Romans used it too, and that's why we use it.

Other ancestors of our alphabet include `𓀠`, `𓁶`, `𓁹`, `𓂝`, `𓂧`, and `𓃾`.

Because of these changes, pretty much all of the visual cues in our language are now gone, aside from a few exceptions such as the Roman numerals `Ⅰ` and `Ⅱ` and `Ⅲ` that look exactly like what they represent.

The Egyptian numeric system is sort of like that on a larger scale. Each character represented a unit (like 1, 10, or 100), and is simply repeated as many times as needed.

For example, the number 5585 in Egyptian hieroglyphs is:`𓆼𓆼𓆼𓆼𓆼𓏲𓏲𓏲𓏲𓏲𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓏤𓏤𓏤𓏤𓏤`

Each of those five flowers represent 1000, each squiggly thing (a coil of rope) represents 100, and the next two represent 10 and 1.

While less efficient to write, visually it can be much easier to grasp than our numbers, in which only the length gives an immediate visual clue to its size (e.g. that 10,000,000 is much greater than 10,000). Appearances can be deceiving for numbers this abstract, which is why 5585 looks similar to 5855 but 6000 looks different, even though 6000 is closer to 5855 than 5585 is.

In programming terms, our numbers are sort of like pointers to data, not the data itself. In addition, you also have to know its position in a number to parse it into what it actually represents. The number 5 might represent 5000, or 50, or 0.5 depending on its position. That's why it takes a bit of work to mentally sort sets of similar-looking numbers.

Let's give it a try. Quick, sort these four numbers from greatest to least!

- 5585
- 5558
- 8558
- 5855

Interestingly, the Egyptian versions of the same numbers are easier to sort!

- 𓆼𓆼𓆼𓆼𓆼𓏲𓏲𓏲𓏲𓏲𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓏤𓏤𓏤𓏤𓏤
- 𓆼𓆼𓆼𓆼𓆼𓏲𓏲𓏲𓏲𓏲𓎆𓎆𓎆𓎆𓎆𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤
- 𓆼𓆼𓆼𓆼𓆼𓆼𓆼𓆼𓏲𓏲𓏲𓏲𓏲𓎆𓎆𓎆𓎆𓎆𓏤𓏤𓏤𓏤𓏤𓏤𓏤𓏤
- 𓆼𓆼𓆼𓆼𓆼𓏲𓏲𓏲𓏲𓏲𓏲𓏲𓏲𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓎆𓏤𓏤𓏤𓏤𓏤

When reading them, your eye immediately jumps to the flowers on the left which makes it clear that the third number is the largest of them all. Then on to the next larger unit, and so on. You can more easily see which number is greater than another, instead of interpreting it.

So in modern times we've sacrificed a bit of visual expressiveness for the sake of efficiency. Maybe that's part of the reason why people reach for emojis so much. 😆

And that's essentially what **Surrealist's Graph view** does with your data. Instead of seeing the raw data when making a graph query, it visually sums it up in a way that gives you a top-down view of the connections between the records in your database.

Since a picture is worth a thousand words, let's move on to a whole bunch of pictures that show just how this graph view looks in practice.

## Rock-paper-scissors visualised

The first example is the simplest one: three `hand` records, each of which `beats` another one. At the end, a `SELECT` query includes each record's `id` as well as a [graph path](/docs/surrealdb/models/graph#creating-a-graph-relation) to follow.

```surrealql
CREATE hand:rock, hand:paper, hand:scissors;

RELATE hand:rock->beats->hand:scissors;
RELATE hand:scissors->beats->hand:paper;
RELATE hand:paper->beats->hand:rock;

SELECT id, ->beats->hand AS beats FROM hand;
```

To give the data a try yourself, go to the [app.surrealdb.com](https://app.surrealdb.com/query), click on **Open the Sandbox**, paste in the data and click **Run query**.

The non-visual output is quick to read too, but only because there are only three actors involved.

```surrealql
[
  {
    beats: [
      hand:rock
    ],
    id: hand:paper
  },
  {
    beats: [
      hand:scissors
    ],
    id: hand:rock
  },
  {
    beats: [
      hand:paper
    ],
    id: hand:scissors
  }
]
```

To change to Surrealist's graph view, click on the button next to **Run query** that says **Combined** and change it to **Graph**. Then highlight the last statement and click on **Run query** again to see the output. Instead of a list of records and their fields, it now provides a top-down view showing the state of the relationship: a triangle! That's exactly what rock-paper-scissors is.

## Interactions inside a growing company

Let's say that you and three friends decided to found a company. With four people in total, how many possible interactions does it have and what does the company dynamic look like?

This can be represented by creating some `person` records, then using the [`array::complement()`](/docs/surrealql/functions/database/array#arraycomplement) function to get all of the other `person` records for each one except itself.

```surrealql
FOR $person IN CREATE |person:4| {
    LET $others = array::complement((SELECT * FROM person), [$person]);
    FOR $counterpart IN $others {
      RELATE $person->knows->$counterpart;
    };
};

SELECT id, ->knows->person FROM person;
```

The graphical view shows the company dynamic: a square! On the bottom right you can see the number 12 for the total number of edges. Inside this small company each person can talk to three others, multiply that by four people and you get 12 possible ways that communication takes place.

Later on the company grows to nine people. Replacing `person:4` with `person:9` in the example above it is enough to make this change. While nine people doesn't feel like a huge change compared with four, the image generated shows otherwise. There are now 72 possible interactions instead of 12!

Hovering over a single record shows that record's connections. Doing this shows how little of the total a single record is connected to. While you can talk to eight coworkers, the vast majority of interactions in the company now don't involve you.

It's this exponential growth in connections that leads growing companies to establish teams.

This next example shows a company with some structure: one CEO, three VPs, three managers for each VP, and three employees for each manager: 40 employees in total.

```surrealql
LET $CEO = CREATE ONLY person SET title = "CEO";

FOR $vp IN CREATE |person:3| SET title = "VP" {
    RELATE $vp->works_under->$CEO;
    FOR $manager IN CREATE |person:3| SET title = "Manager" {
        RELATE $manager->works_under->$vp;
        FOR $employee IN CREATE |person:3| SET title = "Employee" {
            RELATE $employee->works_under->$manager;
        };
    };
};

SELECT id, ->works_under->person FROM person;
```

The output this time shows a much cleaner layout. While much larger than the company with nine employees, there are only 39 edges connecting them. A quick look at this graph quickly sums up the situation: the company has small teams that are probably quite agile, while the CEO is up to three steps away from the lowest-ranked employees on the org chart.

By the way, SurrealDB recently added a number of [algorithms for recursive graph queries](/docs/surrealql/datamodel/idioms#path-and-unique-node-collection-shortest-path), one of which will allow us to automatically see the shortest distance between every employee and the CEO.

```surrealql
LET $CEO = (SELECT * FROM ONLY person WHERE title = "CEO" LIMIT 1).id;
SELECT 
    id, 
    title,
    @.{..+shortest=$CEO}->works_under->person AS path_to_CEO
FROM person;
```

A sample of three records from the above query shows the shortest path for each type of employee.

```surrealql
  {
    id: person:91viuxc1msuivlfdhx4n,
    path_to_CEO: [
      person:wcckukzvfm1fzcpik6t8,
      person:qkns72ivij9iw9izd337,
      person:oc4an6ugy1xdrs8p5362
    ],
    title: 'Employee'
  },
  {
    id: person:8cfy4631zm7gvpsmd7iv,
    path_to_CEO: [
      person:8slsuaz1xgq7fiezkgh5,
      person:oc4an6ugy1xdrs8p5362
    ],
    title: 'Manager'
  },
  {
    id: person:8slsuaz1xgq7fiezkgh5,
    path_to_CEO: [
      person:oc4an6ugy1xdrs8p5362
    ],
    title: 'VP'
  }
```

## Making maps

The moment that Surrealist's graph view first clicked for me was when I gave it a try using [the dataset](https://datasets.surrealdb.com/learn/book/book-part-11-final-geo-dataset.surql) from the end of Chapter 11 of the book [Aeon's Surreal Renaissance](/learn/book/chapter-11) that I wrote to give users a chance to immerse themselves completely in SurrealDB for the length of a full book.

This book takes place in modern-day Victoria in western Canada centuries in the future, and at this point the main character Aeon has begun recreating the civilisation of the 21st century. Using SurrealDB, Aeon's team have put together a map of the places that they know, which stretch [from Victoria to just across the Rocky Mountains to the east](https://www.openstreetmap.org/?#map=7/50.906/-120.685).

Inside the dataset, towns are joined to each other by a graph edge called `to` that goes both ways, setting the distance and some basic info on how easy or hard a trip it is. For example, going from Town A to Town B might be a nice downhill walk, while going the other way is that much harder.

```surrealql
LET $relation = RELATE $begin->to->$end
    SET
    crookedness = $crookedness,
    terrain = $terrain,
    slope = $slope,
    distance = geo::distance($begin.location, $end.location),
    speed_modifier = 
        (IF     crookedness = "straight"     { 1.0 }
        ELSE IF crookedness = "crooked"      { 0.8 }
        ELSE IF crookedness = "very crooked" { 0.5 })
        *
        (IF     slope = "flat"               { 1.0 }
        ELSE IF slope = "up"                 { 0.8 }
        ELSE IF slope = "down"               { 1.2 }
        ELSE IF slope = "steep"              { 0.5 })
        *
        (IF terrain = "road"                 { 1.2 }
        ELSE IF terrain = "normal"           { 1.0 }
        ELSE IF terrain = "hard"             { 0.7 }
        ELSE IF terrain = "water"            { 1.0 }),
    days_travel = 
        IF $trip.terrain = "water" { 1 + (distance / 100000 * speed_modifier) }
        ELSE                       {      distance / 20000  * speed_modifier  };
```

I followed this up with a quick `SELECT id, ->to->town FROM town` query to see what Surrealist would produce, and was blown away when it came back with this, a group of connected paths that together look almost like the map used for the book.

Since it's not very likely that you will be familiar with this part of western Canada, let's put something together over a larger area: Europe. Here is a similar dataset showing some of the rail connections between a large number of European capitals.

```surrealql
FOR $city IN [
    ["Amsterdam", ["Brussels", "Paris", "Berlin", "London"]],
    ["Belgrade", ["Budapest", "Sarajevo", "Skopje", "Zagreb"]],
    ["Berlin", ["Amsterdam", "Prague", "Vienna", "Warsaw", "Copenhagen"]],
    ["Bern", ["Paris", "Berlin", "Vienna"]],
    ["Bratislava", ["Vienna", "Budapest", "Prague"]],
    ["Brussels", ["Amsterdam", "Paris", "Berlin", "London", "Luxembourg"]],
    ["Bucharest", ["Sofia", "Budapest"]],
    ["Budapest", ["Vienna", "Bratislava", "Bucharest", "Belgrade"]],
    ["Copenhagen", ["Berlin", "Stockholm", "Oslo"]],
    ["Lisbon", ["Madrid"]],
    ["Ljubljana", ["Vienna", "Zagreb"]],
    ["London", ["Paris", "Brussels", "Amsterdam"]],
    ["Luxembourg", ["Brussels", "Paris", "Berlin"]],
    ["Madrid", ["Lisbon", "Paris"]],
    ["Oslo", ["Stockholm", "Copenhagen"]],
    ["Paris", ["Brussels", "Amsterdam", "London", "Madrid", "Berlin"]],
    ["Podgorica", ["Belgrade"]],
    ["Prague", ["Berlin", "Vienna", "Bratislava"]],
    ["Rome", ["Paris", "Vienna"]],
    ["Sarajevo", ["Belgrade", "Zagreb"]],
    ["Skopje", ["Belgrade"]],
    ["Sofia", ["Bucharest", "Belgrade"]],
    ["Stockholm", ["Copenhagen", "Oslo"]],
    ["Tirana", ["Podgorica"]],
    ["Vienna", ["Berlin", "Prague", "Bratislava", "Budapest", "Ljubljana", "Rome"]],
    ["Warsaw", ["Berlin", "Prague", "Vienna"]],
    ["Zagreb", ["Ljubljana", "Sarajevo", "Belgrade"]]
] {
    LET $name = $city[0];
    LET $connections = $city[1];
    LET $created = UPSERT ONLY type::record("city", $name);
    FOR $connection IN $connections {
        LET $other_city = UPSERT ONLY type::record("city", $connection);
        RELATE $created->to->$other_city;
    };
};

SELECT id, ->to->city FROM city;
```

The Graph visualiser in Surrealist looks just like a map you might see at a train station!

## EU and related institutions

Speaking of Europe, have you ever noticed that it's a pretty complex place? If you do a search for "Euler diagram Europe" you can see images that sum up the political situation in a single view. Some countries are in the EU. Some are in the EU but don't use the Euro. Some use the Euro but aren't in the EU. Some are in the EU Customs Union, or the Council of Europe, and so on and so forth.

For data this complex, we will use a more complex setup. Instead of a single edge like `member_of`, we'll have the name of the organisation be the name of the edge. We can define a function to take a string with the name of the agreement, and an array of the names of the member countries, which it will use to create the relevant records and join them together by whatever the agreement name is.

The query used at the very end is `SELECT id, ->?->? FROM country`, which uses ? as a wildcard to show all of the relations instead of single ones like "Schengen Zone".

```surrealql
DEFINE FUNCTION fn::add_members($agreement: string, $countries: array<string>) {
    -- Make a string into a table name
    LET $agreement_name = type::table($agreement);
    -- Create a record for the agreement if it doesn't exist yet
    LET $agreement = UPSERT ONLY type::record("agreement", $agreement);
    FOR $country IN $countries {
        LET $this_country = UPSERT ONLY type::record("country", $country);
        RELATE $this_country->$agreement_name->$agreement;
    };
};

fn::add_members("European Union", ["Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]);
fn::add_members("European Free Trade Association", ["Iceland", "Liechtenstein", "Norway", "Switzerland"]);
fn::add_members("Council of Europe", ["Albania", "Andorra", "Armenia", "Austria", "Azerbaijan", "Belgium", "Bosnia and Herzegovina", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Turkey", "Ukraine", "United Kingdom"]); 
fn::add_members("Eurozone", [ "Austria", "Belgium", "Croatia", "Cyprus", "Estonia", "Finland", "France", "Germany", "Greece", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Portugal", "Slovakia", "Slovenia", "Spain"]);
fn::add_members("European Economic Area", [ "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden"]); 
fn::add_members("Central European Free Trade Agreement",  [ "Albania", "Bosnia and Herzegovina", "Kosovo", "Moldova", "Montenegro", "North Macedonia", "Serbia"]); 
fn::add_members("EU Customs Union", [ "Austria", "Belgium", "Bulgaria", "Croatia", "Cyprus", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Ireland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden", "Turkey"]);
fn::add_members("Schengen Area", [ "Austria", "Belgium", "Bulgaria", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Malta", "Netherlands", "Norway", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden", "Switzerland", "Liechtenstein", "Norway", "Monaco", "San Marino", "Andorra", "Vatican City"] ); 
fn::add_members("NATO", [ "Albania", "Belgium", "Bulgaria", "Canada", "Croatia", "Czechia", "Denmark", "Estonia", "Finland", "France", "Germany", "Greece", "Hungary", "Iceland", "Italy", "Latvia", "Lithuania", "Luxembourg", "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal", "Romania", "Slovakia", "Slovenia", "Spain", "Sweden", "Turkey", "United Kingdom", "United States"]); 

SELECT id, ->?->? FROM country;
```

The top level view shows a big web that gets thinner at the edges. The most crowded part of the web is where you'll find your Spains and Frances and Netherlandses, while the thinner parts are where countries like Moldova and Ukraine and Armenia are.

When you have more than one type of edge, however, you can refine the view by deselecting any edges that you don't care to see.

For example, we can unclick everything except Eurozone and NATO. This will show a smaller web of countries composed of those that are in NATO but don't use Euros, which use Euros but aren't in NATO, and which are both.

## Prototyping, practicing and creating random art

One of the most addictive parts of developing software that you are never entirely sure what will happen once the code runs. You are often 99.99% sure, but wouldn't bet your house on it in the same way that you would on a concrete fact such as "gravity exists" or "the sun will rise tomorrow".

Using the graph view can help you both practice and visualise small prototypes of systems that you would like to put together.

For the next few examples, try to imagine what the output will be before scrolling down to see.

This first example creates 100 `person` records. Then for each person, it finds another `person` record that isn't joined by any relation. It will then `RELATE` one to the other.

Once it is done, each of the 100 `person` records will be related to exactly one of the others. What will the final shape be?

```surrealql
LET $people = CREATE |person:100|;

FOR $person IN $people {
    LET $counterpart = rand::enum(array::complement(SELECT * FROM person WHERE !<-likes, [$person]));
    RELATE $person->likes->$counterpart;
};

SELECT ->?->?, <-?<-? FROM person;
```

The answer is...

A bunch of circles. Maybe one, but likely more.

The possibly surprising part about this result is that you won't always end up with a single circle, because if one record `->likes` a record that already `->likes` another one (and so on and so forth for quite a few more), then none of those records will show up in the `SELECT * FROM person WHERE !<-likes, [$person]` part of the query anymore. If you could see this `FOR` loop in real time, you would first see various lines of relations growing, after which the tail of one would be joined to its own head, form a complete circle, and stop growing.

In fact, we can see this `FOR` loop in real time! Let's change the number of `person` records to 25 and give this a try. By manually selecting the last four queries and choosing to display the fourth one, each click on the "Run selection" button will show the state of the rings as they develop.

```surrealql
LET $people = CREATE |person:25|;

LET $person = (SELECT * FROM person WHERE !->likes ORDER BY RAND())[0];
LET $counterpart = rand::enum(array::complement(SELECT * FROM person WHERE !<-likes, [$person]));
RELATE $person->likes->$counterpart;

SELECT ->?->?, <-?<-? FROM person;
```

![](../../assets/cb1a9cd8be7f1886.mov)

This next example is a bit easier to imagine. It creates 50 `person` records and relates one of them to another. It then goes through each of the records and relates one to another in the following way: `SELECT * FROM person WHERE <-likes OR ->likes`. This is the opposite of the previous example, as now the record to pass into the `RELATE` statement must be one that already *has* a relation, not one that doesn't.

```surrealql
LET $people = CREATE |person:50|;

LET $first = SELECT * FROM ONLY person LIMIT 1;
LET $second = SELECT * FROM ONLY person LIMIT 1;
RELATE $first->likes->$second;

FOR $person IN $people {
    LET $counterpart = rand::enum(SELECT * FROM person WHERE <-likes OR ->likes);
    RELATE $person->likes->$counterpart;
};

SELECT id, ->?->? FROM person;
```

Graphically, this produces something that is the opposite of the circles above: a single shape instead of possibly more than one, and one that is sharp in appearance instead of round - a bit like a snowflake.

Hopefully by now you are as excited about the new Graph visualisation feature as we are. If you have any questions about it or a visualisation of your own to show off, drop by [our Discord](https://discord.gg/surrealdb) where SurrealDB users and staff gather, and get in touch!
