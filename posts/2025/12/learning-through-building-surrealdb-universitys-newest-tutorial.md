---
title: "Learning through building: SurrealDB University's newest tutorial"
slug: "learning-through-building-surrealdb-universitys-newest-tutorial"
date: "2025-12-18T00:00:00.000Z"
categories:
  - "featured"
  - "tutorials"
read_time: "5 min read"
summary: "Now you can learn SurrealDB by building your own database that takes advantage of its multi-model capabilities to store and query over 100 of the world's most popular movies."
source: "https://surrealdb.com/blog/learning-through-building-surrealdb-universitys-newest-tutorial"
cover: "../../assets/3dc8f7fe3cf8c468.jpg"
---

# Learning through building: SurrealDB University's newest tutorial

![Learning through building: SurrealDB University's newest tutorial](../../assets/3dc8f7fe3cf8c468.jpg)

## A new offering for the project-focused learner

Today we're pleased to announce a new addition to SurrealDB University, the best place to learn SurrealDB and its query language. This [new tutorial](/learn/movies) brings the number of ways to learn SurrealDB through the university to four.

SurrealDB University began with quite a bit of content. When it was first announced it had the following two courses:

- [SurrealDB Fundamentals](/learn/fundamentals), a course that follows the classic learning method of following along with an instructor who addresses you through video. SurrealDB Fundamentals can be completed in as little as three hours.
- [Aeon's Surreal Renaissance](/learn/book), a book that teaches SurrealDB through a story. As a full book, this course takes days and days to get through.

Later on we felt the need to have a course for people who want that sense of completion but don't have a great deal of time, and added the [Tour of SurrealDB](/learn/tour) as our third course. The Tour can be completed in as little as 30 minutes.

Those courses served as learning paths for three types of learners. However, there is another type whose learning preferences weren't yet satisfied: people that want to learn by *doing*. Learners of this type tend to feel most satisfied by building, and want to have a running project at the end that they can continue to work on after the tutorial is over.

## Where the new tutorial comes from

Now here is the interesting part: the last four chapters of Aeon's Surreal Renaissance already do exactly that! These chapters involve taking loosely structured JSON data about the world's most popular movies and using it to build an instance that allows you to take advantage of everything SurrealDB offers. In these last four chapters you follows along as this data is turned into strictly typed SurrealQL types inside a schemafull database with graph relations, full-text search, events and more.

However, pointing users to the *last* four chapters of a book didn't feel quite right, because:

- The [movie database tutorial](/learn/movies) begins at the end of the book where the reader has already learned these concepts, so it is used to reinforce what was already learned in previous chapters. As very little of the content is new at this point, it rushes from topic to topic at a pace that is far too fast for a new user.
- Perhaps just as importantly: the last four chapters are also the last four chapters in the story, and directing a user to those chapters first would spoil the whole thing! It's roughly the equivalent of hustling someone unfamiliar with Star Wars into a movie theatre one minute before Darth Vader tells Luke Skywalker the truth about who he is.

So that made these final four chapters perfect for a separate rewrite.

## What you'll learn

Here's a rough overview of the learning path followed in the tutorial. You will:

- Insert a bunch of loosely typed JSON data.
- Learn some of the SurrealQL types that the original data will be converted to, and their benefits.
- Define functions to do the conversions.
- Define database parameters to hold movie genres and ratings.
- Insert the new movie data.
- Add a schema.
- Define indexes, including two for full-text search.
- Add the actors, writers and directors, and join them to their movies via graph edges.
- Define database system users with different roles.
- Define an access method so that non-system users can access the database with strictly defined permissions.
- Test out the database as seen by each type of user, both in Surrealist and via curl requests in the terminal.

In terms of sheer volume, this new tutorial clocks in at about 12,000 words. You could get through it in a focused afternoon, or over two days if you prefer a more leisurely pace.

## Keep building, then let us know

Once this database is up and running, then it's yours to keep building on! For example, you might want to add a UI to show how the [edgengram](/docs/surrealql/statements/define/analyzer#edgengramminmax) filter in the full-text index can be used to display results for movie titles and plots as the user types a word (such as showing search results that include "Terminator 2" as soon as the user has typed "ter"), instead of requiring an exact match.

We have one example [here](https://github.com/surrealdb/examples/tree/main/surreal-book/movie-database-rust-egui/readme.md) of a frontend written in Rust that uses this movie database, and even shows the posters for each movie because the original movie data includes a field called `Poster` that holds a link to a url to an image for the poster.

If you end up building something on top of the movie tutorial, feel free to open up a PR to add it to the examples in the same folder! That's an easy way to show the world that you've not only completed the tutorial, but know how to integrate SurrealDB as a backend to your favourite programming language.
