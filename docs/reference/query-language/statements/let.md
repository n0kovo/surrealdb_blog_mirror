---
position: 16
title: LET
description: The LET statement sets and stores a value which can then be used in a subsequent query.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/let.mdx"
---

# `LET` statement

The `LET` statement allows you to create parameters to store any value, including the results of queries or the outputs of expressions. These parameters can then be referenced throughout your SurrealQL code, making your queries more dynamic and reusable.

## Syntax

The syntax for the `LET` statement is straightforward. The parameter name is prefixed with a `$` symbol.

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
LET $parameter [: @type_name] = @value;
```

  
**Railroad Diagram**

```
                                               ╭───────────────────────────────╮                                        
                                               │                               │                                        
        ╭─────╮     ╭───╮     ┌────────────┐   │    ╭───╮     ┌────────────┐   │   ╭───╮     ┌────────┐     ╭───╮       
├┼──────│ LET │─────│ $ │─────│ @parameter │───╯────│ : │─────│ @type_name │───╰───│ = │─────│ @value │─────│ ; │─────┼┤
        ╰─────╯     ╰───╯     └────────────┘        ╰───╯     └────────────┘       ╰───╯     └────────┘     ╰───╯
```

## Example usage

### Basic parameter assignment

You can use the `LET` statement to store simple values or query results. For example, storing a string value and then using it in a `CREATE` statement:

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "[{ id: person:qt3itwoql7oodlg3n077, name: 'tobie' }]"
skip-record-id-key = true

*/

-- Define the parameter
LET $name = "tobie";
-- Use the parameter
CREATE person SET name = $name;
```

### Storing query results

The `LET` statement is also useful for storing the results of a query, which can then be used in subsequent operations:

```surql
/**[test]

[[test.results]]
error = "The table 'person' does not exist"

[[test.results]]
error = "Cannot execute UPDATE statement using value: NONE"

*/

-- Define the parameter
LET $adults = SELECT * FROM person WHERE age > 18;
-- Use the parameter
UPDATE $adults SET adult = true;
```

### Conditional logic with `IF ELSE`

SurrealQL allows you to define parameters based on conditional logic using `IF ELSE` statements:

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "NONE"

[[test.results]]
value = "'integer'"

*/

LET $num = 10;

LET $num_type =
         IF type::is_int($num)     { "integer" }
    ELSE IF type::is_decimal($num) { "decimal" }
    ELSE IF type::is_float($num)   { "float"   };

RETURN $num_type;
-- 'integer'
```

## Anonymous functions

You can define anonymous functions also known as closures using the `LET` statement. These functions can be used to encapsulate reusable logic and can be called from within your queries. Learn more about [anonymous functions](../language-primitives/data-types/closures.md) in the Data model section.

## Pre-defined and protected parameters

SurrealDB comes with [pre-defined parameters](../language-primitives/parameters.md) that are accessible in any context. However, parameters created using `LET` are not accessible within the scope of these pre-defined parameters.

Furthermore, some pre-defined parameters are protected and cannot be overwritten using `LET`:

```surql
/**[test]

[[test.results]]
value = "NONE"

[[test.results]]
value = "'Before!'"

[[test.results]]
error = "The table 'person' does not exist"

[[test.results]]
value = "'Before!'"

*/

LET $before = "Before!";

-- Returns ["Before!"];
RETURN $before;

-- Returns the `person` records before deletion
DELETE person RETURN $before;

-- Returns "Before!" again
RETURN $before;
```

Attempting to redefine protected parameters will result in an error:

```surql
/**[test]

[[test.results]]
error = ""'auth' is a protected variable and cannot be set""

[[test.results]]
error = ""'session' is a protected variable and cannot be set""

*/

LET $auth = 1;
LET $session = 10;
```

```surql title="Output"
-------- Query 1 --------

"'auth' is a protected variable and cannot be set"

-------- Query 2 --------

"'session' is a protected variable and cannot be set"
```

## Typed LET statements

*Since v2.0.0*

Type safety in a `LET` statement can be ensured by adding a `:` (a colon) and the type name after the `LET` keyword.

```surql
/**[test]

[[test.results]]
error = ""Tried to set `$number`, but couldn't coerce value: Expected `int` but found `'9'`""

*/

LET $number: int = "9";
```

```surql title="Output"
"Tried to set `$number`, but couldn't coerce value: Expected `int` but found `'9'`"
```

### Typed literal statements

Multiple possible types can be specified in a `LET` statement by adding a `|` (vertical bar) in between each possible type.

```surql
/**[test]

[[test.results]]
value = "NONE"

*/

LET $number: int | string = "9";
```

Even complex types such as objects can be included in a typed `LET` statement.

```surql
/**[test]

[[test.results]]
value = "NONE"

*/

LET $error_info: 
  string | { error: string } = 
  { 
    error: "Something went wrong plz help" 
  };
```

For more information on this pattern, see the page on [literals](../language-primitives/data-types/literals.md).

## Conclusion

The `LET` statement in SurrealDB is versatile, allowing you to store values, results from subqueries, and even define anonymous functions. Understanding how to use `LET` effectively can help you write more concise, readable, and maintainable queries.
