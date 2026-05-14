---
position: 1
title: React
description: The SurrealDB SDK for JavaScript can be used in React applications to interact with your SurrealDB instance.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/javascript/frameworks/react.mdx"
---

# React

[React](https://react.dev/) is a popular JavaScript library for building user interfaces. The SurrealDB SDK for JavaScript can be used in your React applications to interact with your SurrealDB instance.

This guide walks you through setting up a connection provider and executing queries in a React project.

## Prerequisites

- A basic understanding of React
- A running [SurrealDB instance](https://surrealdb.com/docs/start)
- The [JavaScript SDK installed](../installation.md) in your project

## Installing dependencies

In addition to `surrealdb`, this guide uses [@tanstack/react-query](https://tanstack.com/query/latest) to manage the asynchronous connection state. Install it alongside the SDK:

**npm**

```bash
npm install --save surrealdb @tanstack/react-query
```

**yarn**

```bash
yarn add surrealdb @tanstack/react-query
```

**pnpm**

```bash
pnpm install surrealdb @tanstack/react-query
```

Follow the [installation guide](../installation.md) for more information on how to install the SDK in your project.

## Creating the connection provider

We recommend initializing the SDK in a [Context Provider](https://react.dev/learn/passing-data-deeply-with-context) so the `Surreal` client is accessible anywhere in your component tree. The provider below manages the connection lifecycle, tracks connection status via TanStack Query, and cleans up on unmount.

The `params` prop accepts the same options as [`.connect()`](../concepts/connecting-to-surrealdb.md#connection-options), including `namespace`, `database`, and [`authentication`](../concepts/authentication.md#providing-credentials-on-connect).

```tsx

interface SurrealProviderProps {
    children: React.ReactNode;
    endpoint: string;
    client?: Surreal;
    params?: Parameters<Surreal["connect"]>[1];
    autoConnect?: boolean;
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

export function SurrealProvider({
    children,
    client,
    endpoint,
    params,
    autoConnect = true,
}: SurrealProviderProps) {
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
        if (autoConnect) connect();

        return () => {
            reset();
            instance.close();
        };
    }, [autoConnect, connect, reset, instance]);

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

## Wrapping your application

In your top-level component, wrap the root with `QueryClientProvider` and `SurrealProvider`. Pass the endpoint and any [connection options](../concepts/connecting-to-surrealdb.md#connection-options) through the `params` prop.

```tsx

const queryClient = new QueryClient();

ReactDOM.createRoot(document.getElementById("root")!).render(
    <React.StrictMode>
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
    </React.StrictMode>,
);
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
    const [users, setUsers] = useState<User[]>([]);

    useEffect(() => {
        client.select<User>(new Table("users"))
            .then(setUsers)
            .catch(console.error);
    }, [client]);

    if (isConnecting) return <p>Connecting...</p>;
    if (isError) return <p>Connection failed: {String(error)}</p>;

    return (
        <ul>
            {users.map((user) => (
                <li key={String(user.id)}>{user.name} ({user.email})</li>
            ))}
        </ul>
    );
}
```

## Handling authentication

You can build an authentication layer on top of the provider using the SDK's [`.signin()`](../concepts/authentication.md#signing-in-users) and [`.signup()`](../concepts/authentication.md#signing-up-users) methods. The example below shows a minimal hook for record access authentication.

```tsx

export function useAuth() {
    const client = useSurrealClient();

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

## Learn more

- [Connecting to SurrealDB](../concepts/connecting-to-surrealdb.md) for connection protocols and reconnection behavior
- [Authentication](../concepts/authentication.md) for signing in, signing up, and token management
- [Executing queries](../concepts/executing-queries.md) for query builders and raw SurrealQL
- [Live queries](../concepts/live-queries.md) for real-time subscriptions
- [JavaScript SDK API reference](https://surrealdb.com/docs/languages/javascript/api) for the complete method reference
