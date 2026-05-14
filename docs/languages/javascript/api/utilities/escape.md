---
position: 6
title: Escape Functions
description: Functions for escaping identifiers and values in SurrealQL queries.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/api/utilities/escape.mdx"
---

# Escape functions {#escape}

Escape functions provide safe handling of identifiers and values in SurrealQL queries when you need to construct queries manually.

> [!NOTE: Tip]
> Prefer using [`surql`](surql.md) or [`BoundQuery`](bound-query.md) for automatic parameterization. Use escape functions only when absolutely necessary.

**Import:**
```ts
    escapeIdent,
    escapeKey,
    escapeRid,
    escapeValue
} from 'surrealdb';
```

**Source:** [utils/escape.ts](https://github.com/surrealdb/surrealdb.js/blob/main/packages/sdk/src/utils/escape.ts)

## Functions

### `escapeIdent(name)` {#escapeident}

Escape table names, field names, and other identifiers.

```ts title="Signature"
function escapeIdent(name: string): string
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`name` <label label="required" /></td>
            <td>`string`</td>
            <td>The identifier to escape.</td>
        </tr>
    </tbody>
</table>

#### Returns
`string` - Escaped identifier

#### Examples

```ts

// Simple identifiers (no escaping needed)
console.log(escapeIdent('users')); // 'users'
console.log(escapeIdent('first_name')); // 'first_name'

// Special characters (wrapped in backticks)
console.log(escapeIdent('user-table')); // '`user-table`'
console.log(escapeIdent('my table')); // '`my table`'
console.log(escapeIdent('user.name')); // '`user.name`'

// Reserved keywords
console.log(escapeIdent('select')); // '`select`'
console.log(escapeIdent('from')); // '`from`'
```

---

### `escapeKey(key)` {#escapekey}

Escape object keys for use in queries.

```ts title="Signature"
function escapeKey(key: string): string
```

#### Returns
`string` - Escaped key

#### Example

```ts
const key = 'user-property';
console.log(escapeKey(key)); // Properly escaped for object notation
```

---

### `escapeRid(value)` {#escaperid}

Escape record ID components.

```ts title="Signature"
function escapeRid(value: string | number): string
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`value` <label label="required" /></td>
            <td>`string | number`</td>
            <td>The record ID component to escape.</td>
        </tr>
    </tbody>
</table>

#### Returns
`string` - Escaped record ID component

#### Examples

```ts

// Simple IDs
console.log(escapeRid('john')); // 'john'
console.log(escapeRid(123)); // '123'

// IDs with special characters
console.log(escapeRid('user-123')); // '`user-123`'
console.log(escapeRid('user@email.com')); // '`user@email.com`'
```

---

### `escapeValue(value)` {#escapevalue}

Escape values for use in queries.

```ts title="Signature"
function escapeValue(value: unknown): string
```

#### Parameters
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>`value` <label label="required" /></td>
            <td>`unknown`</td>
            <td>The value to escape.</td>
        </tr>
    </tbody>
</table>

#### Returns
`string` - Escaped value representation

#### Examples

```ts

// Strings
console.log(escapeValue('hello')); // "'hello'"
console.log(escapeValue("O'Reilly")); // "'O\\'Reilly'"

// Numbers
console.log(escapeValue(42)); // '42'
console.log(escapeValue(3.14)); // '3.14'

// Booleans
console.log(escapeValue(true)); // 'true'
console.log(escapeValue(false)); // 'false'

// null/undefined
console.log(escapeValue(null)); // 'null'
console.log(escapeValue(undefined)); // 'none'
```

## Complete examples

### Dynamic table names

```ts

async function selectFromTable(tableName: string) {
    // Validate and escape table name
    const safeTable = escapeIdent(tableName);
    
    // Use in query (still prefer Table class)
    const query = `SELECT * FROM ${safeTable}`;
    const [results] = await db.query(query).collect();
    
    return results;
}

await selectFromTable('user-sessions'); // Safe
```

### Dynamic field selection

```ts

async function selectFields(table: string, fields: string[]) {
    const escapedFields = fields.map(escapeIdent).join(', ');
    const escapedTable = escapeIdent(table);
    
    const query = `SELECT ${escapedFields} FROM ${escapedTable}`;
    const [results] = await db.query(query).collect();
    
    return results;
}

await selectFields('users', ['first-name', 'last-name', 'email']);
```

### Building raw queries (not recommended)

```ts
// Only when you absolutely must build raw queries

function buildUnsafeQuery(table: string, filters: Record<string, unknown>) {
    const escapedTable = escapeIdent(table);
    
    const conditions = Object.entries(filters)
        .map(([key, value]) => {
            const field = escapeIdent(key);
            const val = escapeValue(value);
            return `${field} = ${val}`;
        })
        .join(' AND ');
    
    return `SELECT * FROM ${escapedTable} WHERE ${conditions}`;
}

// Better: Use surql instead!
const filters = { status: 'active', age: 18 };
const query = surql`
    SELECT * FROM users 
    WHERE status = ${filters.status} 
    AND age = ${filters.age}
`;
```

## When to use

### ✅ use escape functions when:
- Constructing queries with user-provided table/field names
- Working with identifiers that have special characters
- Building dynamic schema definitions
- Interfacing with external query builders

### ❌ prefer other solutions:
- **For values:** Use [`surql`](surql.md) or [`BoundQuery`](bound-query.md)
- **For tables:** Use [`Table`](../values/table.md) class
- **For record IDs:** Use [`RecordId`](../values/record-id.md) class
- **For conditions:** Use [`expr`](expr.md)

## Best practices

### 1. Prefer type-safe alternatives

```ts
// Good: Type-safe
const table = new Table('users');
const users = await db.select(table);

// Avoid: Manual escaping
const escaped = escapeIdent('users');
const users = await db.query(`SELECT * FROM ${escaped}`).collect();
```

### 2. Validate before escaping

```ts
// Good: Validate first
function safeQuery(tableName: string) {
    if (!isValidTable(tableName)) {
        throw new Error('Invalid table name');
    }
    
    const escaped = escapeIdent(tableName);
    return `SELECT * FROM ${escaped}`;
}

// Avoid: Blind escaping
function unsafeQuery(tableName: string) {
    return `SELECT * FROM ${escapeIdent(tableName)}`;
}
```

### 3. Use surql for complex queries

```ts
// Good: Automatic parameterization
const query = surql`SELECT * FROM users WHERE name = ${name}`;

// Avoid: Manual escaping
const query = `SELECT * FROM users WHERE name = ${escapeValue(name)}`;
```

## Security considerations

> [!WARNING]
> Escaping functions are NOT a complete defense against SQL injection. Always prefer parameterized queries using `surql` or `BoundQuery`.

```ts
// Secure: Parameterized
const query = surql`SELECT * FROM users WHERE name = ${userInput}`;

// Less secure: Manual escaping
const query = `SELECT * FROM users WHERE name = ${escapeValue(userInput)}`;

// Insecure: No escaping
const query = `SELECT * FROM users WHERE name = '${userInput}'`;
```

## See also

- [surql](surql.md) - Recommended for parameterized queries
- [BoundQuery](bound-query.md) - Parameterized query class
- [Table](../values/table.md) - Type-safe table references
- [RecordId](../values/record-id.md) - Type-safe record identifiers
