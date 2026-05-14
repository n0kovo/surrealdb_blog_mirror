---
position: 5
title: SurrealQL functions
description: Embedded JavaScript functions access native SurrealQL via surrealdb.functions for richer, performant server-side logic.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/scripting/surrealql-functions.mdx"
---

Embedded scripting functions have access to native SurrealQL functions, allowing for complex and performant operations otherwise not possible.
---

# SurrealQL functions

Embedded scripting functions have access to native SurrealQL functions, allowing for complex and performant operations otherwise not possible. SurrealQL functions are published under the `surrealdb.functions` variable. Custom functions are not available within the embedded JavaScript function at the moment.

```surql
RETURN function() {
	// Using the rand::uuid::v4() function
	const uuid = surrealdb.functions.rand.uuid.v4();
};
```
