---
position: 5
title: Comments
description: In SurrealQL, comments can be written in a number of different ways.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/language-primitives/comments.mdx"
---

# Comments

In SurrealQL, comments can be written in a number of different ways.

```surql
/*
In SurrealQL, comments can be written as single-line
or multi-line comments, and comments can be used and
interspersed within statements.
*/

SELECT * FROM /* get all users */ user;

# There are a number of ways to use single-line comments
SELECT * FROM user;

// Alternatively using two forward-slash characters
SELECT * FROM user;

-- Another way is to use two dash characters
SELECT * FROM user;
```
