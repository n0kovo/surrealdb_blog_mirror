---
position: 3
title: Vue.js
description: The SurrealDB SDK for JavaScript can be used in Vue.js applications to interact with your SurrealDB instance.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/javascript/frameworks/vuejs.mdx"
---

# Vue.js

[Vue.js](https://vuejs.org/) is a progressive JavaScript framework for building user interfaces. The SurrealDB SDK for JavaScript can be used in your Vue applications to interact with your SurrealDB instance.

This guide walks you through setting up a connection plugin and executing queries in a Vue 3 project using the Composition API.

## Prerequisites

- A basic understanding of Vue 3 and the Composition API
- A running [SurrealDB instance](https://surrealdb.com/docs/start)
- The [JavaScript SDK installed](../installation.md) in your project

## Installing dependencies

In addition to `surrealdb`, this guide uses [@tanstack/vue-query](https://tanstack.com/query/latest/docs/framework/vue) to manage the asynchronous connection state. Install both packages:

**npm**

```bash
npm install --save surrealdb @tanstack/vue-query
```

**yarn**

```bash
yarn add surrealdb @tanstack/vue-query
```

**pnpm**

```bash
pnpm install surrealdb @tanstack/vue-query
```

Follow the [installation guide](../installation.md) for more information on how to install the SDK in your project.

## Value classes

Before you can use the SDK in your Vue application, you need to configure the codec options to mark all returned [value classes](../concepts/value-types.md) as raw. This prevents Vue's reactivity system from being applied to them, and allows you to use them in your components without any issues.

```ts

const db = new Surreal({
	codecOptions: {
		valueDecodeVisitor: (value) => value instanceof Value ? markRaw(value) : value,
	},
});
```

The `valueDecodeVisitor` function is called for each value returned from the database. If the value is an instance of a value class, it is marked as raw so Vue's reactivity system is not triggered.

## Creating the connection plugin

We recommend providing the `Surreal` client through Vue's [dependency injection](https://vuejs.org/guide/components/provide-inject) system so it is accessible in any component. The composable below manages the connection lifecycle, tracks status via TanStack Query, and cleans up when the component unmounts.

The `params` option accepts the same values as [`.connect()`](../concepts/connecting-to-surrealdb.md#connection-options), including `namespace`, `database`, and [`authentication`](../concepts/authentication.md#providing-credentials-on-connect).

```ts

interface SurrealOptions {
    endpoint: string;
    client?: Surreal;
    params?: Parameters<Surreal["connect"]>[1];
    autoConnect?: boolean;
}

interface SurrealState {
    client: Surreal;
    isConnecting: Ref<boolean>;
    isSuccess: Ref<boolean>;
    isError: Ref<boolean>;
    error: Ref<unknown>;
    connect: () => Promise<true>;
    close: () => Promise<true>;
}

const SurrealKey: InjectionKey<SurrealState> = Symbol("surreal");

export function provideSurreal(options: SurrealOptions) {
    const instance = options.client ?? new Surreal();

    const { mutateAsync, isPending, isSuccess, isError, error, reset } = useMutation({
        mutationFn: () => instance.connect(options.endpoint, options.params),
    });

    if (options.autoConnect !== false) {
        mutateAsync();
    }

    onUnmounted(() => {
        reset();
        instance.close();
    });

    const state: SurrealState = {
        client: instance,
        isConnecting: isPending,
        isSuccess,
        isError,
        error,
        connect: () => mutateAsync(),
        close: () => instance.close(),
    };

    provide(SurrealKey, state);
    return state;
}

export function useSurreal(): SurrealState {
    const state = inject(SurrealKey);
    if (!state) throw new Error("useSurreal() requires provideSurreal() in a parent component");
    return state;
}

export function useSurrealClient(): Surreal {
    return useSurreal().client;
}
```

## Initializing the plugin

Register the TanStack Query plugin in your application entry point, then call `provideSurreal()` in your root component. Pass the endpoint and any [connection options](../concepts/connecting-to-surrealdb.md#connection-options) through the `params` field.

```ts

const app = createApp(App);
app.use(VueQueryPlugin);
app.mount("#app");
```

```vue
<script setup lang="ts">

provideSurreal({
    endpoint: "ws://127.0.0.1:8000",
    params: {
        namespace: "surrealdb",
        database: "docs",
        authentication: {
            username: "root",
            password: "root",
        },
    },
});
</script>

<template>
    <router-view />
</template>
```

## Executing queries

Use the `useSurrealClient()` composable to access the `Surreal` instance from any descendant component. All [query methods](../concepts/executing-queries.md) are available on the client, including `.query()`, `.select()`, `.create()`, and more.

```vue
<script setup lang="ts">

interface User {
    id: string;
    name: string;
    email: string;
}

const { isConnecting, isError, error } = useSurreal();
const client = useSurrealClient();
const users = ref<User[]>([]);

onMounted(async () => {
    users.value = await client.select<User>(new Table("users"));
});
</script>

<template>
    <p v-if="isConnecting">Connecting...</p>
    <p v-else-if="isError">Connection failed: {{ String(error) }}</p>
    <ul v-else>
        <li v-for="user in users" :key="String(user.id)">
            {{ user.name }} ({{ user.email }})
        </li>
    </ul>
</template>
```

## Handling authentication

You can build an authentication layer on top of the composable using the SDK's [`.signin()`](../concepts/authentication.md#signing-in-users) and [`.signup()`](../concepts/authentication.md#signing-up-users) methods. The example below shows a minimal composable for record access authentication.

```ts

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
- [JavaScript SDK API reference](https://surrealdb.com/docs/reference/javascript/api) for the complete method reference
