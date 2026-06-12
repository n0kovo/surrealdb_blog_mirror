---
position: 2
title: Authentication
description: Sign up, sign in, and manage authentication tokens with the SurrealDB Kotlin SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/concepts/authentication.mdx"
---

# Authentication

The Kotlin SDK supports the full range of SurrealDB [authentication](../../../learn/security/authentication/authentication.md) methods: root, namespace, and database users, as well as record (scoped) access. Credentials are supplied as a [`JsonObject`](value-types.md), built with [`buildJsonObject`](https://kotlinlang.org/api/kotlinx.serialization/kotlinx-serialization-json/kotlinx.serialization.json/build-json-object.html).

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
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#signup">`client.signup(params)`</a></td>
			<td scope="row" data-label="Description">Signs up against a record access method</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#signin">`client.signin(params)`</a></td>
			<td scope="row" data-label="Description">Signs in with credentials</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#authenticate">`client.authenticate(token)`</a></td>
			<td scope="row" data-label="Description">Authenticates with an existing token</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#auth">`client.auth()`</a></td>
			<td scope="row" data-label="Description">Returns the current authentication record</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#invalidate">`client.invalidate()`</a></td>
			<td scope="row" data-label="Description">Invalidates the current session authentication</td>
		</tr>
		<tr>
			<td scope="row" data-label="Method"><a href="/docs/languages/kotlin/api/core/surreal-client#reset">`client.reset()`</a></td>
			<td scope="row" data-label="Description">Resets the session to an unauthenticated state</td>
		</tr>
	</tbody>
</table>

## Signing in

Use [`.signin()`](../api/core/surreal-client.md#signin) with the credentials appropriate to the [level of access](../../../learn/security/authentication/authentication.md) you need. It returns the authentication token as a [`JsonElement`](value-types.md).

```kotlin

// Root user
client.signin(buildJsonObject {
    put("user", "root")
    put("pass", "root")
})

// Database user
client.signin(buildJsonObject {
    put("namespace", "surrealdb")
    put("database", "docs")
    put("user", "admin")
    put("pass", "secret")
})
```

## Signing up

Use [`.signup()`](../api/core/surreal-client.md#signup) to register against a [record access](../../../reference/query-language/statements/define/access/record.md) method.

```kotlin
val token = client.signup(buildJsonObject {
    put("namespace", "surrealdb")
    put("database", "docs")
    put("access", "user")
    put("email", "ada@example.com")
    put("password", "hunter2")
})
```

## Authenticating with a token

If you already hold a token (for example from a previous session), authenticate the connection with [`.authenticate()`](../api/core/surreal-client.md#authenticate).

```kotlin
client.authenticate("eyJ0eXAiOiJKV1Qi...")
```

## Inspecting and clearing authentication

Retrieve the currently authenticated record with [`.auth()`](../api/core/surreal-client.md#auth), drop the authentication while keeping the connection open with [`.invalidate()`](../api/core/surreal-client.md#invalidate), or fully reset the session state with [`.reset()`](../api/core/surreal-client.md#reset).

```kotlin
val me = client.auth()
client.invalidate()
client.reset()
```

## Automatic authentication and token renewal

The client can authenticate automatically on connect and after reconnects, and renew tokens shortly before they expire. Provide a `credentialProvider` and enable `autoAuthenticate` on your [`SurrealClientConfig`](../api/core/client-config.md). The provider returns a [`SurrealAuthInput`](../api/core/client-config.md#surreal-auth-input) — either a `SignIn` with credentials or an existing `Token`.

```kotlin

val client = SurrealClient(
    SurrealClientConfig(
        url = "wss://example.com",
        autoAuthenticate = true,
        tokenRenewalLeadMillis = 60_000, // renew 60s before expiry
        credentialProvider = {
            SurrealAuthInput.SignIn(buildJsonObject {
                put("user", "root")
                put("pass", "root")
            })
        },
    ),
)
```

## Learn more

- [SurrealClient API reference](../api/core/surreal-client.md) for complete method signatures
- [Client configuration](../api/core/client-config.md) for `credentialProvider` and renewal options
- [Multiple sessions](multiple-sessions.md) for per-session authentication
- [SurrealDB authentication](../../../learn/security/authentication/authentication.md) for an overview of authentication concepts
