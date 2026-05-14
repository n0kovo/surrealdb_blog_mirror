---
title: "Find your celebrity soulmate with the magic of vector search"
slug: "find-your-celebrity-soulmate-with-the-magic-of-vector-search"
date: "2025-02-27T00:00:00.000Z"
categories:
  - "tutorials"
  - "featured"
read_time: "7 min read"
summary: "Have you ever wondered how to find someone or something that’s most like you, whether it’s a roommate, someone who shares your Christmas traditions, or even a celebrity? Vector search is the answer. It’s a modern way to find matches based on multiple preferences at once, and tools like SurrealDB make it incredibly easy to use. Let’s explore what vector search is and how it works, step by step."
source: "https://surrealdb.com/blog/find-your-celebrity-soulmate-with-the-magic-of-vector-search"
cover: "../../assets/0a5f42e3112defb8.jpg"
---

# Find your celebrity soulmate with the magic of vector search

![Find your celebrity soulmate with the magic of vector search](../../assets/0a5f42e3112defb8.jpg)

Have you ever wondered how to find someone or something that’s most like you, whether it’s a roommate, someone who shares your Christmas traditions, or even a celebrity? Vector search is the answer. It’s a modern way to find matches based on multiple preferences at once, and tools like SurrealDB make it incredibly easy to use. Let’s explore what vector search is and how it works, step by step.

## What is Vector Search?

Vector Search is a method to find the most similar items in a dataset by considering multiple dimensions (or preferences) simultaneously. Unlike traditional database queries, which filter data based on specific conditions, vector search calculates the "distance" between items in a multi-dimensional space to find the closest match. The easiest way to explain this is with an example.

### Step 1: Finding Your Conference Roommate

Imagine a scenario where you’re at a conference, and you must be paired with a roommate. Everyone filled out a questionnaire, and one of the questions was:

> "The mornings are terrible. Don’t talk to me before 8."

(Ranked from 1 to 5, where 1 means "Strongly Disagree," and 5 means "Strongly Agree.")

It would be a good idea to find someone who feels the same way about mornings as you do to avoid those awkward early morning conversations. If you answered 4, a traditional database with tables could easily find a list of people who also answered 4, and you would have to make a decision whether to room with one of them. If there was no one who answered 4, you would have to settle for someone who answered 3 or 5 and run a query to pull them out of the database.

### Step 2: Adding a New Metric

Now, let’s add a second question to the mix again asked on a scale of 1 to 5, with 1 being "Strongly Disagree" and 5 being "Strongly Agree."

> "I like to sleep in a cool room."

At this point, traditional search methods start to feel clunky because you now need to consider both preferences. Say you answered 3, we would have to consider a query perhaps searches for an exact match on both questions. If there was no exact match, we would have to decide how to rank the importance of each question and how to weigh the answers. You would have to decide whether you would rather room with someone who answered 4 on the first question and 3 on the second or someone who answered 3 on the first question and 4 on the second.

## Visualising Vector Search

A vector search would consider both preferences simultaneously. Imagine laying out a 5x5 grid on the floor. Each person’s answer to the first question (mornings) is their X-coordinate, and their answer to the second question (cool room) is their Y-coordinate.

**For example:** If Abigail answered 4 for mornings and 3 for cool rooms, her position on the grid is (4, 3). This is her vector, and position on the grid:

![Abigail's vector search position](../../assets/a2e10699e2bbd454.jpg)

Say Jane answered 2 for mornings and 4 for cool rooms, her position on the grid is (2, 4). Say Sarah answered 1 for mornings and 3 for cool rooms, making her position (1, 3)

We can place everyone on the grid and measure the distance between them. The shortest distance represents the most similar person. We can see that compared to Abigail, Jane is the closest match, but Jane and Sarah are the most similar to each other.

### Step 3: Adding a third dimension

Now let's include a third question on conference roommates:

> "Ditching the conference for a day at the beach sounds like a great idea."

Again, this question is on a scale of 1 to 5, with 1 being "Strongly Disagree" and 5 being "Strongly Agree." Each person’s position now has three coordinates, like (4, 3, 5). The same principle applies: the shortest distance in this 3D space indicates the person most similar to you across all three preferences. You can see that in a traditional database, this would be difficult to query for. In a vector search, it's as simple as calculating the distance between the vectors.

If we visualise this in 3D cube, we would be able to see the distance between each person's preferences.

### Adding more dimensions

You can keep adding dimensions to the vector space to represent more preferences. At this point our visual representation becomes difficult to imagine, but the concept remains the same. The more dimensions you add, the more complex the search becomes.

## Vector Search in SurrealDB

SurrealDB makes it easy to perform vector search on large datasets. Each set of answers is represented by a set of answers or metrics.

Let's use the example of finding the most similar celebrity to you. I selected 5 statements that represent different personality traits, with answers ranging from 1 to 5 (1 being "Strongly Disagree" and 5 being "Strongly Agree").:

1. I enjoy taking risks and trying new things.

1. I prefer quiet nights in over social gatherings.

1. I am very competitive and strive to be the best in everything I do.

1. I rely heavily on routines and planning in my daily life.

1. I often seek out creative outlets to express myself.

Represent your answers as a vector, like [4, 2, 5, 4, 5].

I used ChatGPT to generate a list of celebrities and their answers based on what it knows about them to create a dataset. Each celebrity is represented by a set of metrics. In the case of Beyoncé Knowles, her answers are [4, 2, 5, 4, 5], and we can add her to the dataset with a simple command.

```surrealql
CREATE celebrities SET name="Beyoncé Knowles", answers=[4,2,5,4,5];
```

If you want to play along, I recommend that you use the [Surrealist sandbox](https://app.surrealdb.com/) to try this out yourself.

Let's flesh out the dataset with more celebrities and their answers.

```surrealql

CREATE celebrities SET name="Beyoncé Knowles", answers=[4,2,5,4,5];

CREATE celebrities SET name="Leonardo DiCaprio", answers=[5,4,5,3,5];

CREATE celebrities SET name="Adele Adkins", answers=[3,5,3,4,5];

CREATE celebrities SET name="Dwayne Johnson", answers=[5,2,5,4,4];

CREATE celebrities SET name="Taylor Swift", answers=[4,4,4,5,5];

CREATE celebrities SET name="Keanu Reeves", answers=[2,5,3,3,4];

CREATE celebrities SET name="Rihanna Fenty", answers=[5,2,4,3,5];

CREATE celebrities SET name="Chris Pine", answers=[4,4,4,4,4];

CREATE celebrities SET name="Emma Watson", answers=[3,4,3,5,5];

CREATE celebrities SET name="Bruno Mars", answers=[4,3,4,3,5];

CREATE celebrities SET name="Jennifer Lawrence", answers=[4,3,5,3,4];

CREATE celebrities SET name="Tom Hanks", answers=[3,5,3,4,4];

CREATE celebrities SET name="Lady Gaga", answers=[5,2,5,3,5];

CREATE celebrities SET name="Will Smith", answers=[5,2,5,4,4];

CREATE celebrities SET name="Scarlett Johansson", answers=[4,4,4,4,5];

CREATE celebrities SET name="Elton John", answers=[3,4,4,3,5];

CREATE celebrities SET name="Ariana Grande", answers=[4,3,4,3,5];

CREATE celebrities SET name="Robert Downey Jr.", answers=[5,2,5,3,5];

CREATE celebrities SET name="Meryl Streep", answers=[3,5,4,4,4];

CREATE celebrities SET name="Johnny Depp", answers=[5,4,4,3,5];

CREATE celebrities SET name="Miley Cyrus", answers=[5,3,4,3,5];

CREATE celebrities SET name="Chris Hemsworth", answers=[4,3,4,4,4];

CREATE celebrities SET name="Anne Hathaway", answers=[3,4,3,5,4];

CREATE celebrities SET name="Kanye West", answers=[5,2,5,2,5];

CREATE celebrities SET name="Zendaya Coleman", answers=[4,4,4,4,5];

CREATE celebrities SET name="Justin Timberlake", answers=[4,3,4,3,5];

CREATE celebrities SET name="Emma Stone", answers=[4,4,3,4,5];

CREATE celebrities SET name="Hugh Jackman", answers=[5,3,5,4,4];

CREATE celebrities SET name="Selena Gomez", answers=[4,4,4,4,4];

CREATE celebrities SET name="Tom Cruise", answers=[5,2,5,3,4];

CREATE celebrities SET name="Natalie Portman", answers=[3,5,3,5,5];

CREATE celebrities SET name="Samuel L. Jackson", answers=[5,3,5,3,4];

CREATE celebrities SET name="Billie Eilish", answers=[3,5,3,4,5];

CREATE celebrities SET name="Chris Pratt", answers=[5,3,4,3,4];

CREATE celebrities SET name="Gal Gadot", answers=[4,3,4,4,5];

CREATE celebrities SET name="Shakira", answers=[5,2,5,3,5];

CREATE celebrities SET name="Joaquin Phoenix", answers=[4,5,4,3,5];

CREATE celebrities SET name="Angelina Jolie", answers=[4,4,4,3,5];

CREATE celebrities SET name="Ryan Reynolds", answers=[5,3,5,3,4];

CREATE celebrities SET name="Charlize Theron", answers=[4,4,4,4,4];

CREATE celebrities SET name="Brad Pitt", answers=[5,3,5,3,4];

CREATE celebrities SET name="Jennifer Lopez", answers=[5,3,5,4,5];

CREATE celebrities SET name="Ellen DeGeneres", answers=[4,4,4,4,4];

CREATE celebrities SET name="Daniel Radcliffe", answers=[3,5,3,4,5];

CREATE celebrities SET name="Justin Bieber", answers=[5,3,5,3,4];

CREATE celebrities SET name="Harrison Ford", answers=[4,4,4,4,3];

CREATE celebrities SET name="Sandra Bullock", answers=[3,4,3,5,4];

CREATE celebrities SET name="Katy Perry", answers=[5,3,5,3,5];

CREATE celebrities SET name="Matthew McConaughey", answers=[5,2,5,4,4];

CREATE celebrities SET name="Nicole Kidman", answers=[3,5,3,5,4];

```

We now have a dataset of celebrities and their answers to the 5 questions in a table called `celebrities`, and if you navigate to the `celebrities` table in the Surrealist sandbox, you can see the dataset.

## Finding the Most Similar Celebrity

Now that we have a dataset of celebrities and their answers, we can find the most similar celebrity to you. Let's say your answers are [4, 2, 5, 4, 5]. We can run a query to find the most similar celebrity to you like this:

```surrealql

LET $celebrities = [4,2,5,4,5];

SELECT id, name, vector::similarity::cosine(answers, $celebrities) AS dist

FROM celebrities

ORDER BY dist DESC

LIMIT 3;

```

In this query, we are calculating the cosine similarity between your answers and each celebrity's answers. There are a few different options on how to calculate similarity, but cosine similarity is a common one, and it is worth reading up on the [SurrealDB documentation](/docs/surrealdb/models/vector#computation-on-vectors-vector-package-of-functions) to understand the different options.

The [`ORDER BY dist DESC`](/docs/surrealql/statements/select#sort-records-using-the-order-by-clause) sorts the results by the distance in descending order, so the most similar celebrity is at the top. The `LIMIT 3` limits the results to the top 3 most similar celebrities.

If you run this query in the Surrealist sandbox, you will see the top 3 most similar celebrities to you based on your answers. In my case, Harrison Ford is my celebrity twin! Not sure how I feel about that, but it's fun to see the results.

## Conclusion

Vector search is an elegant and powerful way to find similarities in data. By transforming preferences into multi-dimensional coordinates and calculating distances, you can uncover the closest matches in any context. Whether it’s finding your ideal roommate or discovering your celebrity twin, vector search makes it possible.
