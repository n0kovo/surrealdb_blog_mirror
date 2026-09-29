---
position: 1
title: Robin Hood character graph
description: "Pyle's Robin Hood ingested chapter by chapter into SurrealDB Agent Memory, drawn as the cast known at each reading position, with name variants linked."
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/agent-memory/cookbooks/showcase/robin-hood/index.mdx"
---

# Robin Hood character graph

This demo ingests *The Merry Adventures of Robin Hood* (Howard Pyle, 1883) into SurrealDB Agent Memory one chapter at a time, and draws the cast as the memory knew it at each point in the book. Move the reading position and the graph shows only what had been learned by then, so it never gives away a later chapter.

## As you go through the demo, note the following

- **The reading position is a known time.** Each chapter was stamped with its own date on ingest, and the graph reads the memory `asOf` the chapter you have reached. Nothing from a later chapter appears before you reach it.
- **Relations arrive in the chapter they were learned in.** A link draws itself in when you reach that chapter, and a character's size is how many facts the memory holds about them so far.
- **Facts are superseded, not overwritten.** Press **F** for the raw fields, then hover a character: a value a later chapter replaced is shown struck through and marked "replaced", because the memory keeps the old value with the time it stopped being current.
- **Each name is its own entity.** `Robin` and `Robin Hood` are separate from the first chapter, and the dashed gold lines are the page's suggestion that they are one person. **Names** folds them together.
- **Descriptions are written from the memory, not by it.** A separate model (Gemini 2.5 Flash) writes the text beside a character from the facts the memory held at that chapter, never from the book. Agent Memory stores and returns the facts, so a different model given the same facts would write different text from the same record.
- **The Story button plays a chapter.** It introduces the characters the chapter brings in, then narrates the chapter's summary, putting on stage the people each sentence names and the relations between them.
- **The last tab shows the calls.** What the memory returns lists the API requests behind the graph, with the responses recorded as they came back.

<DemoEmbed title="Robin Hood character graph" pages={[{"label": "Graph", "src": "/docs/showcase/robin-hood/graph.html"}, {"label": "Introduction", "src": "/docs/showcase/robin-hood/intro.html"}, {"label": "What the memory returns", "src": "/docs/showcase/robin-hood/memory.html"}]} />

## Names for one person

The book renames its characters as part of the plot. John Little becomes Little John, Little John serves the Sheriff as Reynold Greenleaf, and Robin appears as a butcher, a beggar and a tattered stranger. Agent Memory creates one entity for each name, so `Robin` and `Robin Hood` are two entities from the first chapter.

Keeping them apart is deliberate, because each name carries facts of its own, in the same way that somebody called Bill by one group and William by another is known differently by each. [Entities with several names](https://surrealdb.com/docs/agent-memory/mental-model/entities-with-several-names) covers the cases in general. What should join them is a `same_as` edge, which records that two entities refer to one person and which lookups already follow. Agent Memory does not yet write that edge for name variants like these, so this graph suggests the links itself from the names:

- A dashed gold line joins two names the page reads as one person, such as `Robin` and `Robin Hood`, or `Tuck` and `Friar Tuck`.
- **Names** switches between every name on its own and one node for each person.
- A name that could belong to several people is left unlinked. `Will` could be Will Scarlet, Will Stutely or Will Gamwell.

## Reading without spoilers

Every chapter was ingested with a synthetic known time, one day per chapter, and the graph reads the memory as of the reading position. [Spoiler-safe narrative memory](../../patterns/spoiler-safe-narrative-memory.md) describes the pattern, and [How it was built](how-it-was-built.md) gives the steps for this demo, and [Build your own character graph](build-your-own.md) shows how to make one from your own text.

## Query the records yourself

The embed below loads what the Agent Memory API returned for this demo into a SurrealDB instance in your browser, as three tables: `entity`, `attribute` and `relation`. This is the API's response shape, not the data Agent Memory holds internally, which also includes embeddings, source chunks and indexes. Each attribute and relation names the document it was extracted from in `source`. Edit the query and run it again, or download the file from [datasets.surrealdb.com](https://datasets.surrealdb.com/datasets/agent-memory/robin-hood.surql).

The Robin Hood file also holds every value a later chapter replaced, from the entity history endpoint, so an attribute can be read in order through the book. The dates are the demo's narrative clock: chapter 1 is 1 January 2000, and each chapter is one day later.

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=--%20How%20Robin%20Hood%27s%20temperament%20changed%20through%20the%20book%0ASELECT%20createdAt%2C%20value%2C%20validUntil%2C%20source%20FROM%20attribute%20WHERE%20entity%20%3D%20entity%3A%5B%27person%27%2C%20%27robin_hood%27%5D%20AND%20key%20%3D%20%27temperament%27%20ORDER%20BY%20createdAt%3B%0A--%20Little%20John%27s%20alias%3A%20Reynold%20Greenleaf%20in%20chapter%206%2C%20Giles%20Hobble%20in%20chapter%2020%0ASELECT%20createdAt%2C%20value%2C%20validUntil%20FROM%20attribute%20WHERE%20entity%20%3D%20entity%3A%5B%27person%27%2C%20%27little_john%27%5D%20AND%20key%20%3D%20%27alias%27%20ORDER%20BY%20createdAt%3B%0A)
