---
position: 5
title: React Native
description: The SurrealDB SDK for JavaScript can be used in React Native applications to connect to a remote SurrealDB instance from Android and iOS.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/frameworks/react-native.mdx"
---

# React Native

[React Native](https://reactnative.dev/) builds native Android and iOS applications from React components. The SurrealDB SDK for JavaScript runs inside React Native apps and connects to a remote SurrealDB instance over WebSocket or HTTP.

This guide covers a bare React Native project, created with the React Native Community CLI. If your project uses [Expo](expo.md), follow that guide instead: Expo supplies several of the runtime APIs that you otherwise have to install yourself.

## What is different on mobile

The SDK surface is the same one used in [React](react.md) applications, but four constraints apply on Android and iOS that do not apply in a browser.

- **Embedded engines are not supported.** The [WebAssembly engine](../engines/wasm.md) needs a WebAssembly runtime, which Hermes does not provide. The [Node.js engine](../engines/node.md) is a native Node addon and cannot be loaded by React Native. Every connection from a React Native app is a remote connection.
- **The JavaScript engine is not a browser.** Hermes leaves out several web APIs that the SDK depends on. You install them as polyfills before the SDK loads.
- **Your JavaScript bundle ships to the device.** Anyone who installs the app can read the values you compile into it. Use [record access](../../query-language/statements/define/access/record.md) for end users, and keep system user credentials on a server.
- **The connection does not survive backgrounding.** Both platforms suspend your process shortly after the user leaves the app, which closes the socket. You reconnect when the app returns to the foreground.

## Prerequisites

- A basic understanding of React and React Native
- A React Native project on 0.79 or newer
- A running [SurrealDB instance](../../../running/overview.md) that the device can reach
- The [JavaScript SDK installed](../installation.md) in your project

## Supported connection protocols

| Protocol | Supported | Notes |
|----------|-----------|-------|
| `wss://` | Yes | Long-lived connection. Required for [live queries](../concepts/live-queries.md). |
| `https://` | Yes | Stateless requests. No live queries. Needs the `ReadableStream` global. |
| `ws://`, `http://` | Development only | Blocked by default on both platforms. See [reaching your database from a device](#reaching-your-database-from-a-device). |

Use `wss://` unless you only need occasional one-off requests. A WebSocket connection keeps the session authenticated between calls and is the only protocol that supports live queries.

## Installing the required polyfills

Hermes ships `TextEncoder`, but not `TextDecoder`. React Native ships a reduced `URL` implementation that omits properties the SDK reads, such as `protocol` and `pathname`. Install both, along with a secure random source.

```bash
npm install --save surrealdb react-native-url-polyfill @bacons/text-decoder react-native-get-random-values
```

Import them at the very top of your entry file, before any other import. Metro evaluates imports in order, and the SDK constructs a `TextDecoder` when its module is first loaded.

```js title="index.js"

AppRegistry.registerComponent(appName, () => App);
```

`react-native-get-random-values` is a native module, so run `npx pod-install` and rebuild the app after installing it.

| Global | Available by default | Polyfill | Needed for |
|--------|----------------------|----------|------------|
| `TextEncoder` | Yes, from Hermes | — | CBOR encoding |
| `TextDecoder` | No | `@bacons/text-decoder` | CBOR decoding |
| `URL`, `URLSearchParams` | Partly, from React Native | `react-native-url-polyfill` | Parsing the endpoint |
| `crypto.getRandomValues` | No | `react-native-get-random-values` | `Uuid.v4()` and `Uuid.v7()` |
| `ReadableStream` | No | `web-streams-polyfill` | HTTP connections only |

The SDK falls back to `Math.random()` when `crypto.getRandomValues` is missing, so UUIDs are still generated but are not cryptographically random. Install the polyfill if your app creates `Uuid` values on the device.

To confirm the polyfills are in place, log the globals once during startup:

```ts
for (const name of ["TextEncoder", "TextDecoder", "URL", "URLSearchParams"]) {
    if (!(name in globalThis)) console.warn(`Missing global: ${name}`);
}
```

> [!NOTE]
> If you connect over `https://` rather than `wss://`, add `web-streams-polyfill` as well and import `web-streams-polyfill/polyfill` alongside the others. The HTTP engine checks the request body against `ReadableStream`, which throws a `ReferenceError` when the global is undefined.

## Installing the remaining dependencies

This guide uses [@tanstack/react-query](https://tanstack.com/query/latest) to manage the asynchronous connection state, and [react-native-keychain](https://github.com/oblador/react-native-keychain) to keep session tokens in the platform keystore.

```bash
npm install --save @tanstack/react-query react-native-keychain
```

Follow the [installation guide](../installation.md) for more information on how to install the SDK in your project.

## Reaching your database from a device

On a device or emulator, `localhost` points at the device itself, not at your development machine. Set the endpoint according to where the app runs.

| Where the app runs | Host to use |
|--------------------|-------------|
| iOS simulator | `127.0.0.1` |
| Android emulator | `10.0.2.2` |
| Physical device | Your machine's LAN address, for example `192.168.1.24` |
| Production | Your deployed hostname over `wss://` |

Android blocks cleartext traffic from API level 28, and iOS blocks it through App Transport Security. A project created from the React Native template already carries the exceptions needed to develop against a local endpoint, so `ws://` works in a debug build without further setup.

**iOS**

The template's `Info.plist` sets `NSAllowsLocalNetworking`, which permits connections to local addresses:

```xml title="ios/<YourApp>/Info.plist"
<key>NSAppTransportSecurity</key>
<dict>
    <key>NSAllowsArbitraryLoads</key>
    <false/>
    <key>NSAllowsLocalNetworking</key>
    <true/>
</dict>
```

For a host that is not on the local network, add an entry under `NSExceptionDomains` with `NSExceptionAllowsInsecureHTTPLoads` rather than widening the policy.

**Android**

The template's manifest resolves `usesCleartextTraffic` from a build-type placeholder, which the React Native Gradle plugin sets to `true` for debug builds and `false` for release builds:

```xml title="android/app/src/main/AndroidManifest.xml"
<application
    android:usesCleartextTraffic="${usesCleartextTraffic}"
    ...>
```

> [!WARNING]
> Neither exception applies to a release build, and neither should be widened to cover one. Connect over `wss://` in the builds you ship.

## Creating the connection provider

Initialise the SDK in a [Context Provider](https://react.dev/learn/passing-data-deeply-with-context) so the `Surreal` client is available anywhere in your component tree. The provider below manages the connection lifecycle, tracks connection status through TanStack Query, closes the socket when the app moves to the background, and reconnects when it becomes active again.

The `params` prop accepts the same options as [`.connect()`](../concepts/connecting-to-surrealdb.md#connection-options), including `namespace`, `database`, and [`authentication`](../concepts/authentication.md#providing-credentials-on-connect).

```tsx title="SurrealProvider.tsx"

interface SurrealProviderProps {
    children: React.ReactNode;
    endpoint: string;
    client?: Surreal;
    params?: Parameters<Surreal["connect"]>[1];
}

interface SurrealProviderState {
    client: Surreal;
    isConnecting: boolean;
    isSuccess: boolean;
    isError: boolean;
    error: unknown;
    connect: () => Promise<true>;
    close: () => Promise<true>;
}

const SurrealContext = createContext<SurrealProviderState | undefined>(undefined);

export function SurrealProvider({ children, client, endpoint, params }: SurrealProviderProps) {
    const [instance] = useState(() => client ?? new Surreal());

    const {
        mutateAsync: connectMutation,
        isPending,
        isSuccess,
        isError,
        error,
        reset,
    } = useMutation({
        mutationFn: () => instance.connect(endpoint, params),
    });

    const connect = useCallback(() => connectMutation(), [connectMutation]);
    const close = useCallback(() => instance.close(), [instance]);

    useEffect(() => {
        connect();

        return () => {
            reset();
            instance.close();
        };
    }, [connect, reset, instance]);

    useEffect(() => {
        const subscription = AppState.addEventListener("change", (state) => {
            if (state === "active" && instance.status === "disconnected") {
                connect();
            } else if (state === "background") {
                instance.close();
            }
        });

        return () => subscription.remove();
    }, [instance, connect]);

    const value: SurrealProviderState = useMemo(
        () => ({ client: instance, isConnecting: isPending, isSuccess, isError, error, connect, close }),
        [instance, isPending, isSuccess, isError, error, connect, close],
    );

    return <SurrealContext.Provider value={value}>{children}</SurrealContext.Provider>;
}

export function useSurreal() {
    const context = useContext(SurrealContext);
    if (!context) throw new Error("useSurreal must be used within a SurrealProvider");
    return context;
}

export function useSurrealClient() {
    return useSurreal().client;
}
```

The handler closes the connection on `background` but ignores `inactive`. On iOS, `inactive` also fires for the app switcher and for incoming calls, which are usually too short to be worth dropping the socket.

## Wrapping your application

Mount the providers in `App.tsx`, above your navigation container.

```tsx title="App.tsx"

const queryClient = new QueryClient();

export default function App() {
    return (
        <QueryClientProvider client={queryClient}>
            <SurrealProvider
                endpoint="ws://10.0.2.2:8000"
                params={{
                    namespace: "surrealdb",
                    database: "docs",
                }}
            >
                <UserList />
            </SurrealProvider>
        </QueryClientProvider>
    );
}
```

## Executing queries

Use the `useSurreal()` hook to reach the `Surreal` instance from any component. All [query methods](../concepts/executing-queries.md) are available on the client, including `.query()`, `.select()`, and `.create()`.

Gate the query on `isSuccess` so it runs once the connection is open, and again after each reconnect.

```tsx title="UserList.tsx"

interface User {
    id: string;
    name: string;
    email: string;
}

export function UserList() {
    const { client, isConnecting, isSuccess, isError, error } = useSurreal();
    const [users, setUsers] = useState<User[]>([]);

    useEffect(() => {
        if (!isSuccess) return;

        client.select<User>(new Table("users"))
            .then(setUsers)
            .catch(console.error);
    }, [client, isSuccess]);

    if (isConnecting) return <ActivityIndicator />;
    if (isError) return <Text>Connection failed: {String(error)}</Text>;

    return (
        <FlatList
            data={users}
            keyExtractor={(user) => String(user.id)}
            renderItem={({ item }) => (
                <View>
                    <Text>{item.name}</Text>
                    <Text>{item.email}</Text>
                </View>
            )}
        />
    );
}
```

## Subscribing to live queries

[Live queries](../concepts/live-queries.md) push changes to the device as they happen, which removes the need to poll on a metered connection. They require a WebSocket connection.

Because the provider closes the socket on background, tie the subscription to `isSuccess` as well. The effect then recreates the subscription every time the connection reopens.

```tsx

interface Message {
    id: string;
    body: string;
}

export function useLiveMessages() {
    const { client, isSuccess } = useSurreal();
    const [messages, setMessages] = useState<Message[]>([]);

    useEffect(() => {
        if (!isSuccess) return;

        const pending = client.live<Message>(new Table("messages"));

        pending
            .then((live) => {
                live.subscribe((action, result) => {
                    if (action === "CREATE") {
                        setMessages((current) => [...current, result]);
                    }
                });
            })
            .catch(console.error);

        return () => {
            pending.then((live) => live.kill()).catch(() => {});
        };
    }, [client, isSuccess]);

    return messages;
}
```

## Handling authentication

Sign users in with [record access](../../query-language/statements/define/access/record.md) and keep the resulting tokens in the keystore, so the session survives an app restart.

```tsx title="useAuth.ts"

const ACCESS_SERVICE = "surreal.access";
const REFRESH_SERVICE = "surreal.refresh";

export async function readToken(service: string) {
    const entry = await Keychain.getGenericPassword({ service });
    return entry ? entry.password : null;
}

export function useAuth() {
    const { client } = useSurreal();

    useEffect(() => {
        return client.subscribe("auth", async (tokens) => {
            if (tokens) {
                await Keychain.setGenericPassword("surreal", tokens.access, { service: ACCESS_SERVICE });
                if (tokens.refresh) {
                    await Keychain.setGenericPassword("surreal", tokens.refresh, { service: REFRESH_SERVICE });
                }
            } else {
                await Keychain.resetGenericPassword({ service: ACCESS_SERVICE });
                await Keychain.resetGenericPassword({ service: REFRESH_SERVICE });
            }
        });
    }, [client]);

    async function login(email: string, password: string) {
        return client.signin({
            namespace: "surrealdb",
            database: "docs",
            access: "account",
            variables: { email, password },
        });
    }

    async function register(email: string, password: string) {
        return client.signup({
            namespace: "surrealdb",
            database: "docs",
            access: "account",
            variables: { email, password },
        });
    }

    async function logout() {
        return client.invalidate();
    }

    return { login, register, logout };
}
```

The `auth` event fires on sign in, sign up, token refresh, and invalidation, and `.subscribe()` returns the function that removes the listener.

### Restoring a session on launch

Pass a function to the `authentication` connection option. The SDK calls it while opening the connection and again whenever it needs to re-authenticate after a reconnect. The option accepts a token string or `null`, which is what `readToken()` returns.

```tsx title="App.tsx"

<SurrealProvider
    endpoint="ws://10.0.2.2:8000"
    params={{
        namespace: "surrealdb",
        database: "docs",
        authentication: () => readToken("surreal.access"),
    }}
>
```

If the stored access token has expired and you also hold a refresh token, exchange the pair with [`.authenticate()`](../concepts/authentication.md#authenticating-with-an-existing-token) instead.

```ts
const access = await readToken("surreal.access");
const refresh = await readToken("surreal.refresh");

if (access) {
    await client.authenticate(refresh ? { access, refresh } : access);
}
```

> [!IMPORTANT]
> Once you call `.signin()`, `.signup()`, or `.authenticate()`, the `authentication` connection option is ignored for the rest of that session. Choose one of the two approaches per session rather than mixing them.

## Troubleshooting

| Symptom | Cause |
|---------|-------|
| `ReferenceError: Property 'TextDecoder' doesn't exist` | The polyfill imports are missing, or they sit below the SDK import in the entry file. |
| The endpoint fails to parse, or `URL` throws on construction | `react-native-url-polyfill/auto` is not imported. |
| `Network request failed` on Android, works in the browser | The endpoint uses `localhost`. Use `10.0.2.2` on the emulator or the LAN address on a device. |
| Connection hangs, then fails with no server log entry | Cleartext traffic is blocked. Switch to `wss://` or apply the [development configuration](#reaching-your-database-from-a-device). |
| `Unable to resolve module node:util` | Metro resolved the SDK's server build. Remove `node` from `unstable_conditionNames` in **metro.config.js**. |
| Queries fail after the app returns from the background | The query ran before the socket reopened. Gate it on `isSuccess` from the provider. |

## Learn more

- [Expo](expo.md) for the same setup in an Expo project, where the polyfills are already provided
- [Connecting to SurrealDB](../concepts/connecting-to-surrealdb.md) for connection protocols and reconnection behaviour
- [Authentication](../concepts/authentication.md) for signing in, signing up, and token management
- [Executing queries](../concepts/executing-queries.md) for query builders and raw SurrealQL
- [Live queries](../concepts/live-queries.md) for real-time subscriptions
- [JavaScript SDK API reference](https://surrealdb.com/docs/reference/javascript/api) for the complete method reference
