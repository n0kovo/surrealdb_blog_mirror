---
title: "The ultimate beginners guide to databases"
slug: "the-ultimate-beginners-guide-to-databases"
date: "2023-04-21T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "9 min read"
summary: "It is our belief that developers should be able to build secure, modern, collaborative applications without needing to build complicated backend APIs and database layers, and without being forced into using a single data model or cloud platform."
source: "https://surrealdb.com/blog/the-ultimate-beginners-guide-to-databases"
cover: "../../assets/2078fdba2662d6c2.jpg"
---

# The ultimate beginners guide to databases

![The ultimate beginners guide to databases](../../assets/2078fdba2662d6c2.jpg)

What is a database, and why do we need one?

Better yet, why do companies keep creating new databases since we already have over 300 of them?

If you are curious about those questions, you have come to the right place.

We will strip away all the fancy jargon and technical details and focus on understanding the essential concepts of databases through simple analogies.

## How do we make sense of the world?

As long as humans have existed on this planet, we have tried to make sense of it. Just as cavemen drew symbols on walls, we draw symbols on paper... or perhaps more accurately... we type emojis into our smartphones.

Regardless of how we do it, it's always about storing and sharing information in some form.

That, in its essence, is what databases do - store and share information.

We have gotten a lot better at storing and sharing information over the years, from cave walls to the printing press and many things in between.

However, something fundamentally changed when computers arrived. We transitioned from storing and sharing information physically to storing and sharing information digitally.

## From pen and paper to CRUD with digital paper

Instead of just using paper to store and share information, we now had access to digital paper: databases.

We couldn't interact with this digital world physically. Instead, we had to tell the computer how to interact with it on our behalf. This required new mental models and new languages.

The most fundamental mental model is CRUD, [a term coined in 1983](https://archive.org/details/managingdatabase00mart/page/380/mode/2up), which stands for Create, Read, Update and Delete.

Those are the four fundamental ways we interact with data of any kind, anywhere.

Put simply:

- Create = make data / let's write a poem on a piece of paper.
- Read = retrieve data / find the piece of paper you wrote on and read the poem.
- Update = change data / let's change a few lines in the poem.
- Delete = remove data / the poem wasn't good, let's throw the paper in the trash bin

While databases trace their origin back to the 1960s with the [Integrated Data Store (IDS)](https://en.wikipedia.org/wiki/Integrated_Data_Store), databases, as we know them today, got started in the 1970s.

In June of 1970, it's fair to say that Edgar F. Codd made a dent in the universe with his paper titled [A Relational Model of Data for Large Shared Data Banks](http://www.morganslibrary.net/files/codd-1970.pdf).

That paper gave rise to most of the concepts we still use today in relational databases, which we will explore soon.

The most notable thing missing from his paper was how to put these genius ideas into practice, since most people (myself included) are not set theory geniuses.

It wasn't until a few years later that Donald D. Chamberlin and Raymond Boyce, after reading Codd's paper, came up with another genius breakthrough. A new language for making practical use of the relational model ideas. They called it Structured English Query Language or [SEQUEL](https://en.wikipedia.org/wiki/SQL) for short.

Genius researchers can apparently also be somewhat petty, where part of the reason it was called SEQUEL was to tease other researchers who made the [QUEL](https://en.wikipedia.org/wiki/QUEL_query_languages) language. As in, SEQUEL is the sequel to QUEL. Well... I guess QUEL got the last laugh because they had to change the name to SQL (Structured Query Language) due to trademark infringement.

It wasn't until 1979 though, when [Relational Software, Inc. (now Oracle)](https://docs.oracle.com/database/121/SQLRF/intro001.htm#SQLRF50932) introduced the first commercially available implementation of SQL in a relational database.

That brings us to the other fundamental models we are going to cover today:

- The relational model -> relational databases
- The document model -> document databases
- The graph model -> graph databases
- Multi-model -> SurrealDB

## Relational databases - like a jigsaw puzzle

We have already touched on the origin of the relational model. However, we have yet to explore what it is.

In the simplest terms, relational databases are like a jigsaw puzzle, where each puzzle piece represents an Excel-like table.

One of the key innovations of the relational model is how you connect (or join) each puzzle piece together.

The basic workflow for working with a relational database is as follows:

- Plan how the puzzle pieces should look so they fit together (define a schema)
- Create the puzzle pieces (insert statements)
- Assemble the puzzle pieces (select queries)
- Then, you can see the complete picture of the puzzle (result set)

Just like for jigsaw puzzles, for each picture you want to see, you might need to assemble many different puzzle pieces.

## Document model - like a Word document

Now we come to the question people have been asking since the 1990s and will be asking for a long time.

Why do we need other database models when we have the relational database model?

It was because the internet was just getting started and becoming popular at the time.

Since relational databases were not invented with the internet in mind (because the internet did not exist then), they became very slow. You can imagine the chaos of trying to organise 1000 or more people who want to work on assembling the same puzzle.

Therefore the internet gave rise to other models like the document model.

In the simplest terms, document databases are like a Word document, where you make sure that the document has all the relevant information in one place, kind of like this blog post.

The thinking goes that it's easier to make 1000 copies of a single document for each of the 1000 people that need it rather than making 1000 puzzles, each with many oddly shaped puzzle pieces.

This also gave rise to the term [NoSQL in 1998 by Carlo Strozzi](https://en.wikipedia.org/wiki/Strozzi_NoSQL) who, interestingly enough, used it to describe a relational database which didn't use SQL. As we mentioned before, in the history of the relational model, SQL came much later as a way to implement the relational model, but it's entirely possible to find other ways to implement the relational model other than using standard SQL.

However, NoSQL, which originally literally meant 'No SQL', as in this database does not use SQL, is most commonly used to refer to databases that don't use the relational model.

For example, MongoDB, a popular document database, which came out in 2009 uses the MongoDB Query Language (MQL).

However, as relational databases started adopting internet technology and fixing the problem of how to organise the 1000 people who want to work on the same puzzle, people began wanting to use SQL in more and more places.

That is why the term NoSQL changed meaning to 'Not only SQL', as even popular databases like [MongoDB started adding support for SQL](https://www.mongodb.com/atlas/sql).

The basic workflow for working with a document database is as follows:

- Just like in a Word document, you just open a new document and start writing in all the information that you need.
- Then anyone can just read that document to get the information.

That works great when you don't have the time or the desire for so much upfront work of creating and solving a puzzle every time you want an answer.

However, this apparent simplicity comes with other disadvantages. We won't touch on that much here except to say, which organisation doesn't have a problem organising Word documents? Important_document_v5_final_final.docx [seem familiar?](https://www.mongodb.com/blog/post/building-with-patterns-the-document-versioning-pattern)

## Graph model - like your social network

As we were searching for new ways to interact with this digital world, especially with the advent of e-commerce and social media, we found that it can be very tricky to express complex networks as text in Word documents (document model) or jigsaw puzzles (relational model).

Therefore, a new mental model was needed to express complex networks more simply. In this new graph model, we think about relationships slightly differently than in the relational model.

In the simplest terms, graph databases are like your social network, where when you're looking for help you might know somebody that knows somebody that can help you.

The basic workflow for working with a graph database is as follows:

- You make a map of who knows what and how they are connected
- Then, you ask around the network for what you want until you find it.

## Multi-model - SurrealDB

If you've read this far, you might be beginning to understand why companies keep creating new databases. As the world keeps evolving, databases need to keep evolving as well. New technology enables us to take advantage of new ways of storing and sharing information.

The question is, how should databases evolve?

The answers to that generally fall into three categories:

- Let's make the relational model better. How oddly shaped we need to make the puzzle pieces doesn't matter. We can force them to fit using some clever tricks.
- Let's create a new model or new database for every different kind of task we have. If you could choose, wouldn't you choose the clothes that were tailor-made for you instead of the retail store clothes, which might be an awkward fit?
- What if we could do both? What if we could combine different innovative approaches to create a database that both feels custom tailored in its model flexibility but retains the simplicity we have come to expect from the relational model?

The third option is what we at SurrealDB have chosen, as we were [dreaming of something better](/blog/dreaming-of-something-better).

SurrealDB combines aspects of many different kinds of database models, including the major ones we talked about in the post. For an excellent technical introduction, you can [watch this short video](https://www.youtube.com/watch?v=C7WFwgDRStM).

In the simplest terms, however, SurrealDB is like WD-40, use SurrealDB on problems that need lubricating for things to go much more smoothly. But, of course, if you want things to go smoothly from the beginning, you also use it as a preventative measure.

## This is just the start

We have covered a lot of ideas and concepts in the post. If you want to learn more about the technical side and how to do CRUD practically across all these models and SurrealDB, subscribe so you don't miss our next post.
