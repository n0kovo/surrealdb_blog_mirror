---
position: 6
title: Invoking APIs
description: The JavaScript SDK allows you to invoke user-defined API endpoints in SurrealDB with type-safe HTTP-style methods.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/concepts/invoking-apis.mdx"
---

# Invoking APIs

SurrealDB allows you to define custom [API endpoints](../../query-language/statements/define/api.md) that expose database operations through HTTP-style routes. The JavaScript SDK provides the `.api()` method to invoke these endpoints with full type safety, custom headers, and structured responses.

## API references

<table>
	<thead>
		<tr>
			<th scope="col">Method</th>
			<th scope="col">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/javascript/api/core/surreal-queryable#api"> ` db.api(prefix?) `</a></td>
			<td scope="row" data-label="Description">Creates a SurrealApi instance for invoking user-defined endpoints</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/javascript/api/core/surreal-api#get"> ` api.get(path) `</a></td>
			<td scope="row" data-label="Description">Invokes a GET endpoint</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/javascript/api/core/surreal-api#post"> ` api.post(path, body?) `</a></td>
			<td scope="row" data-label="Description">Invokes a POST endpoint</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/reference/javascript/api/core/surreal-api#invoke"> ` api.invoke(path, request?) `</a></td>
			<td scope="row" data-label="Description">Invokes an endpoint with a custom request object</td>
		</tr>
	</tbody>
</table>

## Accessing API endpoints

To invoke user-defined endpoints, call `.api()` on any `Surreal`, `SurrealSession`, or `SurrealTransaction` instance. The returned [`SurrealApi`](../api/core/surreal-api.md) object exposes HTTP-style methods like `.get()`, `.post()`, `.put()`, `.delete()`, and `.patch()`.

```ts
// Obtain the API reference
const api = db.api();

// Execute a GET request
const users = await api.get('/users').value();

// Execute a POST request
const newUser = await api.post('/users', {
    name: 'John Doe',
    email: 'john@example.com',
}).value();
```

By default, API calls return a response object containing `body`, `status`, and `headers`. Chaining `.value()` returns only the response body directly.

```ts
const response = await api.get('/users');

console.log(response.status);	// 200
console.log(response.headers);	// { 'content-type': 'application/json' }
console.log(response.body);	// [ { id: RecordId, name: 'John Doe', email: 'john@example.com' } ]

const users = await api.get('/users').value();

console.log(users); // [ { id: RecordId, name: 'John Doe', email: 'john@example.com' } ]
```

## Defining type-safe APIs

You can define TypeScript types for your API paths to get compile-time type checking on both request bodies and responses. Each path maps HTTP methods to a tuple of `[RequestBody, ResponseBody]`.

```ts
// Define API types using an object literal
type MyApi = {
    '/users': {
        get: [void, User[]];
        post: [CreateUserInput, User];
    };
    [K: `/users/${string}`]: {
        get: [void, User];
        put: [UpdateUserInput, User];
        delete: [void, void];
    };
};

// Pass the custom API types to the .api() method
const api = db.api<MyApi>();

// All handlers will now be type-safe
const users: User[] = await api.get('/users').value();
```

## Setting request headers

You can set headers on individual requests by chaining `.header()`, or set default headers on the API instance using `api.header()`. Setting a header value to `null` removes it.

```ts
// Single-request header
const result = await api.get('/protected')
    .header('X-Custom-Header', 'value')
    .value();

// Global header
api.header('Content-Type', 'application/json');

// Remove global header
api.header('Content-Type', null);
```

## Using a path prefix

When working with a group of related endpoints, you can pass a prefix to `.api()`. All subsequent calls will be relative to that prefix.

```ts
const usersApi = db.api<UserPaths>('/users');

const allUsers = await usersApi.get('/').value();
const user = await usersApi.get('/123').value();
```

## Handling API errors

When an API call fails, the SDK throws an [`UnsuccessfulApiError`](../api/errors/index.md#unsuccessfulapierror). This error includes the path, HTTP method, and the full response object.

```ts

try {
    await api.get('/users/999').value();
} catch (error) {
    if (error instanceof UnsuccessfulApiError) {
        console.error(`${error.method} ${error.path} failed`);
        console.error('Status:', error.response.status);
    }
}
```

## Learn more

- [SurrealApi API reference](../api/core/surreal-api.md) for the complete list of methods and type parameters
- [ApiPromise API reference](../api/queries/api-promise.md) for response configuration options
- [DEFINE API](../../query-language/statements/define/api.md) for defining custom API endpoints in SurrealQL
