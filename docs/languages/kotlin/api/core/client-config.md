---
position: 2
title: SurrealClientConfig
description: Configuration options for the SurrealDB Kotlin client, including reconnection and authentication.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/kotlin/api/core/client-config.mdx"
---

# `SurrealClientConfig` {#surreal-client-config}

`SurrealClientConfig` configures a [`SurrealClient`](surreal-client.md). The only required field is `url`; everything else has a sensible default.

**Source:** [surrealdb.kotlin](https://github.com/surrealdb/surrealdb.kotlin)

```kotlin title="Import"
```

---

## Fields

<table>
    <thead>
        <tr><th>Field</th><th>Type</th><th>Default</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr>
            <td>`url` *[required]*</td>
            <td>`String`</td>
            <td>—</td>
            <td>The connection URL. The scheme (`ws`/`wss`/`http`/`https`) selects the transport.</td>
        </tr>
        <tr>
            <td id="json">`json`</td>
            <td>`Json`</td>
            <td>lenient</td>
            <td>The `kotlinx.serialization` instance used for encoding and decoding.</td>
        </tr>
        <tr>
            <td>`autoConnect`</td>
            <td>`Boolean`</td>
            <td>`true`</td>
            <td>Connect lazily on the first request.</td>
        </tr>
        <tr>
            <td>`autoAuthenticate`</td>
            <td>`Boolean`</td>
            <td>`false`</td>
            <td>Authenticate automatically using `credentialProvider` on connect and reconnect.</td>
        </tr>
        <tr>
            <td>`credentialProvider`</td>
            <td>`(suspend () -&gt; SurrealAuthInput?)?`</td>
            <td>`null`</td>
            <td>Supplies credentials for automatic authentication and token renewal.</td>
        </tr>
        <tr>
            <td>`requestTimeoutMillis`</td>
            <td>`Long`</td>
            <td>`30_000`</td>
            <td>Per-request timeout in milliseconds.</td>
        </tr>
        <tr>
            <td>`reconnect`</td>
            <td>`ReconnectConfig`</td>
            <td>`ReconnectConfig()`</td>
            <td>WebSocket reconnection behaviour.</td>
        </tr>
        <tr>
            <td>`tokenRenewalLeadMillis`</td>
            <td>`Long`</td>
            <td>`60_000`</td>
            <td>How long before token expiry to renew, in milliseconds.</td>
        </tr>
        <tr>
            <td>`httpClientFactory`</td>
            <td>`((SurrealClientConfig) -&gt; HttpClient)?`</td>
            <td>`null`</td>
            <td>Supplies a custom Ktor `HttpClient`.</td>
        </tr>
    </tbody>
</table>

```kotlin title="Example"

val config = SurrealClientConfig(
    url = "wss://example.com",
    requestTimeoutMillis = 30_000,
    autoAuthenticate = true,
    tokenRenewalLeadMillis = 60_000,
    reconnect = ReconnectConfig(enabled = true, multiplier = 1.5),
    credentialProvider = {
        SurrealAuthInput.SignIn(buildJsonObject {
            put("user", "root")
            put("pass", "root")
        })
    },
)
```

---

## `ReconnectConfig` {#reconnect-config}

Controls exponential-backoff reconnection on the WebSocket transport.

```kotlin title="Import"
```

<table>
    <thead>
        <tr><th>Field</th><th>Type</th><th>Default</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`enabled`</td><td>`Boolean`</td><td>`true`</td><td>Whether reconnection is attempted.</td></tr>
        <tr><td>`initialDelayMillis`</td><td>`Long`</td><td>`250`</td><td>Delay before the first retry.</td></tr>
        <tr><td>`maxDelayMillis`</td><td>`Long`</td><td>`30_000`</td><td>Maximum delay between retries.</td></tr>
        <tr><td>`multiplier`</td><td>`Double`</td><td>`1.5`</td><td>Backoff multiplier applied each attempt.</td></tr>
        <tr><td>`maxAttempts`</td><td>`Int?`</td><td>`null`</td><td>Maximum attempts; `null` retries indefinitely.</td></tr>
    </tbody>
</table>

---

## `SurrealAuthInput` {#surreal-auth-input}

A sealed interface describing how `credentialProvider` should authenticate.

```kotlin title="Import"
```

<table>
    <thead>
        <tr><th>Variant</th><th>Payload</th><th>Description</th></tr>
    </thead>
    <tbody>
        <tr><td>`SurrealAuthInput.SignIn`</td><td>`params: JsonObject`</td><td>Sign in with credentials.</td></tr>
        <tr><td>`SurrealAuthInput.Token`</td><td>`token: String`</td><td>Authenticate with an existing token.</td></tr>
    </tbody>
</table>

## Learn more

- [SurrealClient API reference](surreal-client.md)
- [Connecting to SurrealDB](../../concepts/connecting-to-surrealdb.md)
- [Authentication](../../concepts/authentication.md)
