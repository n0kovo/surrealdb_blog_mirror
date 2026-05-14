---
position: 2
title: SolidJS
description: The SurrealDB SDK for JavaScript can be used in SolidJS applications to interact with your SurrealDB instance.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/frameworks/solidjs.mdx"
---

# SolidJS

[SolidJS](https://docs.solidjs.com/) is a modern JavaScript framework for building responsive and high-performing user interfaces. The SurrealDB SDK for JavaScript can be used in your SolidJS applications to interact with your SurrealDB instance.

This guide walks you through setting up a connection provider and executing queries in a SolidJS project.

## Prerequisites

- A basic understanding of SolidJS
- A running [SurrealDB instance](https://surrealdb.com/docs/start)
- The [JavaScript SDK installed](../installation.md) in your project

## Installing dependencies

In addition to `surrealdb`, this guide uses [@tanstack/solid-query](https://tanstack.com/query/latest/docs/framework/solid) to manage the asynchronous connection state. Install it alongside the SDK:

**npm**

```bash
npm install --save surrealdb @tanstack/solid-query
```

**yarn**

```bash
yarn add surrealdb @tanstack/solid-query
```

**pnpm**

```bash
pnpm install surrealdb @tanstack/solid-query
```

Follow the [installation guide](../installation.md) for more information on how to install the SDK in your project.

## Creating the connection provider

We recommend initializing the SDK in a [Context Provider](https://docs.solidjs.com/concepts/context) so the `Surreal` client is accessible anywhere in your component tree. The provider below manages the connection lifecycle, tracks connection status via TanStack Query, and cleans up automatically.

The `params` prop accepts the same options as [`.connect()`](../concepts/connecting-to-surrealdb.md#connection-options), including `namespace`, `database`, and [`authentication`](../concepts/authentication.md#providing-credentials-on-connect).

```tsx

interface SurrealProviderProps {
    children: JSX.Element;
    endpoint: string;
    client?: Surreal;
    params?: Parameters<Surreal["connect"]>[1];
    autoConnect?: boolean;
}

interface SurrealProviderState {
    client: Accessor<Surreal>;
    isConnecting: Accessor<boolean>;
    isSuccess: Accessor<boolean>;
    isError: Accessor<boolean>;
    error: Accessor<unknown | null>;
    connect: () => Promise<void>;
    close: () => Promise<true>;
}

interface SurrealProviderStore {
    instance: Surreal;
    status: "connecting" | "connected" | "disconnected";
}

const SurrealContext = createContext<SurrealProviderState>();

export function SurrealProvider(props: SurrealProviderProps) {
    const [store, setStore] = createStore<SurrealProviderStore>({
        instance: props.client ?? new Surreal(),
        status: "disconnected",
    });

    const { mutateAsync, isError, error, reset } = createMutation(() => ({
        mutationFn: async () => {
            setStore("status", "connecting");
            await store.instance.connect(props.endpoint, props.params);
        },
    }));

    createEffect(() => {
        if (props.autoConnect !== false) mutateAsync();

        onCleanup(() => {
            reset();
            store.instance.close();
        });
    });

    onMount(() => {
        store.instance.subscribe("connected", () => {
            setStore("status", "connected");
        });

        store.instance.subscribe("disconnected", () => {
            setStore("status", "disconnected");
        });
    });

    const value: SurrealProviderState = {
        client: () => store.instance,
        close: () => store.instance.close(),
        connect: mutateAsync,
        error: () => error,
        isConnecting: () => store.status === "connecting",
        isError: () => isError,
        isSuccess: () => store.status === "connected",
    };

    return (
        <SurrealContext.Provider value={value}>
            {props.children}
        </SurrealContext.Provider>
    );
}

export function useSurreal(): SurrealProviderState {
    const context = useContext(SurrealContext);
    if (!context) throw new Error("useSurreal must be used within a SurrealProvider");
    return context;
}

export function useSurrealClient() {
    return useSurreal().client;
}
```

## Wrapping your application

In your top-level component, wrap the root with `QueryClientProvider` and `SurrealProvider`. Pass the endpoint and any [connection options](../concepts/connecting-to-surrealdb.md#connection-options) through the `params` prop.

```tsx

const queryClient = new QueryClient();

const Root: Component = () => {
    return (
        <QueryClientProvider client={queryClient}>
            <SurrealProvider
                endpoint="ws://127.0.0.1:8000"
                params={{
                    namespace: "surrealdb",
                    database: "docs",
                    authentication: {
                        username: "root",
                        password: "root",
                    },
                }}
            >
                <App />
            </SurrealProvider>
        </QueryClientProvider>
    );
};

export default Root;
```

## Executing queries

Use the `useSurrealClient()` hook to access the `Surreal` instance from any component. All [query methods](../concepts/executing-queries.md) are available on the client, including `.query()`, `.select()`, `.create()`, and more.

```tsx

interface User {
    id: string;
    name: string;
    email: string;
}

export function UserList() {
    const { isConnecting, isError, error } = useSurreal();
    const client = useSurrealClient();

    const [users] = createResource(async () => {
        return client().select<User>(new Table("users"));
    });

    return (
        <Show when={!isConnecting()} fallback={<p>Connecting...</p>}>
            <Show when={!isError()} fallback={<p>Connection failed: {String(error())}</p>}>
                <ul>
                    <For each={users()}>
                        {(user) => <li>{user.name} ({user.email})</li>}
                    </For>
                </ul>
            </Show>
        </Show>
    );
}
```

## Handling authentication

You can build an authentication layer on top of the provider using the SDK's [`.signin()`](../concepts/authentication.md#signing-in-users) and [`.signup()`](../concepts/authentication.md#signing-up-users) methods. The example below shows a minimal hook for record access authentication.

```tsx

export function useAuth() {
    const client = useSurrealClient();

    async function login(email: string, password: string) {
        return client().signin({
            namespace: "surrealdb",
            database: "docs",
            access: "account",
            variables: { email, password },
        });
    }

    async function register(email: string, password: string) {
        return client().signup({
            namespace: "surrealdb",
            database: "docs",
            access: "account",
            variables: { email, password },
        });
    }

    async function logout() {
        return client().invalidate();
    }

    return { login, register, logout };
}
```

## Learn more

- [Connecting to SurrealDB](../concepts/connecting-to-surrealdb.md) for connection protocols and reconnection behavior
- [Authentication](../concepts/authentication.md) for signing in, signing up, and token management
- [Executing queries](../concepts/executing-queries.md) for query builders and raw SurrealQL
- [Live queries](../concepts/live-queries.md) for real-time subscriptions
- [JavaScript SDK API reference](https://surrealdb.com/docs/languages/javascript/api) for the complete method reference
