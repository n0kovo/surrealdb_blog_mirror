---
position: 1
title: Authentication methods
description: The four ways to authenticate with SurrealDB - system users, record users, JWT access and bearer access - what each is for, and how to sign in over HTTP or from an SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/security/authentication/overview.mdx"
---

# Authentication methods

SurrealDB has four authentication methods. Which one you want depends on who is signing in: a person administering the instance, an end user of your application, a client an external identity provider has already authenticated, or another system.

Each method is defined in SurrealQL and then used the same way from every interface, so the choice below decides the rest of the page.

## Choosing a method

| Method | Who it is for | Defined with | Signed in with |
| ------ | ------------- | ------------ | -------------- |
| [System users](users.md#system-users) | Operators and services administering an instance | [`DEFINE USER`](../../../reference/query-language/statements/define/user.md) at root, namespace or database level | A username and password |
| [Record users](users.md#record-users) | End users of your application, one record each | [`DEFINE ACCESS ... TYPE RECORD`](../../../reference/query-language/statements/define/access/record.md), whose `SIGNUP` and `SIGNIN` clauses are queries you write | Whatever fields your `SIGNIN` query reads |
| [JWT access](../../../reference/query-language/statements/define/access/jwt.md) | Clients an external provider has already authenticated | [`DEFINE ACCESS ... TYPE JWT`](../../../reference/query-language/statements/define/access/jwt.md), holding the issuer's public key or shared secret | A token the provider issued |
| [Bearer access](../../../reference/query-language/statements/define/access/bearer.md) | Other systems and software | [`DEFINE ACCESS ... TYPE BEARER`](../../../reference/query-language/statements/define/access/bearer.md), plus an [`ACCESS ... GRANT`](../../../reference/query-language/statements/access.md#grant) per client | The key from a grant |

System users and record users answer to credentials SurrealDB holds. JWT access holds no end user credential: it checks the signature on a token an external provider issued, then trusts the claims inside it, which is how an OpenID Connect or OAuth provider is brought in. It does hold the material for that check, and which kind matters - a [public key](../../../reference/query-language/statements/define/access/jwt.md#public-key-cryptography) or a [JWKS URL](../../../reference/query-language/statements/define/access/jwt.md#json-web-key-set-jwks) can only verify, while an [HMAC](../../../reference/query-language/statements/define/access/jwt.md#hash-based-message-authentication-code-hmac) key is symmetric and can also sign. Bearer access sits between the two, issuing a key per client that you can [audit](../../../reference/query-language/statements/access.md#show) and [revoke](../../../reference/query-language/statements/access.md#revoke) without touching the user it acts as.

> [!WARNING]
> `TYPE JWT` uses `HS256` when no algorithm is given, and the HMAC algorithms (`HS256`, `HS384`, `HS512`) take one secret that both signs and verifies. Anyone holding it can issue tokens with any claims they like, and SurrealDB will trust them. Protect that key on the SurrealDB side as well as at the issuer, or define the access method with a public key or a JWKS URL, neither of which can sign.

> [!NOTE]
> A record user is scoped to one database and restricted by table and field [permissions](../authorization/permissions-and-row-level-security.md). A root system user is not restricted by permissions at all, so it is the wrong credential to put in an application.

## Signing in

Every interface signs in with the same credentials, so an example written for one carries over to the others.

**SurrealQL, HTTP and the SDKs** are covered end to end on [Users](users.md), which defines a user of each kind and then signs in as it.

**Over HTTP**, post the credentials to [`POST /signin`](../../../reference/rest-api/http-protocol.md#signin), or create a record user with [`POST /signup`](../../../reference/rest-api/http-protocol.md#signup). Both return a token for later requests:

```bash
curl -X POST \
	-H "Accept: application/json" \
	-d '{"user":"root", "pass":"secret"}' \
	http://localhost:8000/signin
```

**From an SDK**, each language documents its own `signin` call and the shape of the credentials it takes:

[Rust](../../../reference/rust/methods/signin.md) · [JavaScript](../../../reference/javascript/concepts/authentication.md) · [Python](../../../reference/python/concepts/authentication.md) · [Go](../../../reference/golang/concepts/authentication.md) · [Java](../../../reference/java/concepts/authentication.md) · [Kotlin](../../../reference/kotlin/concepts/authentication.md) · [.NET](../../../reference/dotnet/methods/signin.md) · [PHP](../../../reference/php/v1/methods/signin.md) · [Swift](../../../reference/swift/methods/signin.md) · [Mojo](../../../reference/mojo/methods/signin.md)

## After signing in

- [Sessions](users.md#sessions) - what the connection carries once authenticated, and how tokens and sessions expire.
- [Permissions and row-level security](../authorization/permissions-and-row-level-security.md) - what the authenticated user is then allowed to read and write.
- [Tokens and JWTs](../authorization/tokens-and-jwts.md) - the claims SurrealDB reads from a token, and the parameters they populate.
- [Security best practices](../best-practices/security-best-practices.md) - choosing expiry, storing secrets, and what to expose to a browser.
