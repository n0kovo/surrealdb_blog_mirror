---
position: 7
title: CONTINUE
description: The CONTINUE statement can be used to skip an iteration of a loop, like within the FOR statement
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/continue.mdx"
---

# `CONTINUE` statement

The CONTINUE statement can be used to skip an iteration of a loop, like within the [FOR statement](for.md).

### Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
CONTINUE
```

  
**Railroad Diagram**

```
        ╭──────────╮       
├┼──────│ CONTINUE │─────┼┤
        ╰──────────╯
```

## Example usage

The following queries shows example usage of this statement.

Skipping an iteration of a loop unless a certain condition is met:

```surql
/**[test]

[[test.results]]
error = "The table 'person' does not exist"

*/

-- Set can_vote to true for every person over 18 years old.
FOR $person IN (SELECT id, age FROM person) {
	IF ($person.age < 18) {
		CONTINUE;
	};

	UPDATE $person.id SET can_vote = true;
};
```

Skipping an iteration of a loop when bad data is encountered:

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "NONE"

*/

-- Data retrieved from somewhere which contains many NONE values
LET $weather = [
	{
		city: 'London',
		temperature: 22.2,
		timestamp: 1722565566389
	},
	NONE,
	{
		city: 'London',
		temperature: 20.1,
		timestamp: 1722652002699
	},
    {
        city: 'Phoenix',
        temperature: 45.1,
        timestamp: 1722565642160
    },
    NONE,
    NONE,
    {
        city: 'Phoenix',
        temperature: 45.1,
        timestamp: 1722652070372
    },
];

FOR $data IN $weather {
    IF $data IS NONE {
        CONTINUE;
    };

	CREATE weather CONTENT $data;
};
```
