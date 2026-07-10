---
position: 2
title: TanStack AI
description: Adding Spectron memory to a TanStack Start application.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/spectron/integrations/ai-sdks/tanstack-ai.mdx"
---

# TanStack AI

[TanStack](https://tanstack.com) applications call model providers from server functions and API routes. Spectron adds long-term memory to those handlers: recall relevant context before a generation, then store the exchange afterwards. There is no dedicated adapter. The [JavaScript SDK](../sdks/javascript-and-typescript.md) (`@surrealdb/spectron`) runs in any TanStack Start server route.

> [!NOTE]
> This is an integration guide. There is no first-party TanStack package; the code below wires the Spectron SDK into TanStack's server layer, and you can adapt it to your handler shape.

## Installation

```bash
npm install @surrealdb/spectron ai @ai-sdk/openai
```

Spectron holds an API key, so construct the client only on the server, never in a component or loader that ships to the browser.

## A memory-aware server route

Recall context, prepend it to the system prompt, generate, then store the turn:

```typescript
// src/routes/api/chat.ts

const spectron = new Spectron({
    endpoint: process.env.SPECTRON_ENDPOINT!,
    context: "acme-prod",
    apiKey: process.env.SPECTRON_API_KEY!,
});

export const ServerRoute = createServerFileRoute("/api/chat").methods({
    POST: async ({ request }) => {
        const { userId, message } = await request.json();
        const scope = [`org/acme/user/${userId}`];

        // 1. Recall relevant memory as a ready-to-inject context block.
        const memory = await spectron.context(message, { scope, k: 8 });

        // 2. Generate with the context block in the system prompt.
        const { text } = await generateText({
            model: openai("gpt-4o"),
            system: `You are a helpful assistant.\n\n## Memory\n${memory}`,
            prompt: message,
        });

        // 3. Store the exchange so it is available next time.
        await spectron.rememberMany(
            [
                { role: "user", content: message },
                { role: "assistant", content: text },
            ],
            { scope },
        );

        return Response.json({ text });
    },
});
```

## Scope per user or session

Pass a `scope` on every call to isolate memory. A scope is a slash path or an array of paths, for example `["org/acme/user/alice"]` for one user, or a session-specific path such as `["org/acme/session/abc123"]`. Register paths with `spectron scopes create` before first use.

## Recall as a tool

To let the model decide when to reach for memory, expose the [`@surrealdb/vercel-ai`](vercel-ai-sdk.md) tool set from the same route. TanStack Start runs the Vercel AI SDK unchanged:

```typescript

const memory = createSpectron({ defaultScopes: "org/acme" });
// pass memory.tools({ sessionId }) into generateText / streamText
```

## Next steps

- [JavaScript SDK](../sdks/javascript-and-typescript.md): the full client surface
- [Vercel AI SDK](vercel-ai-sdk.md): middleware and tools that automate recall and storage
- [REST API](../surfaces/rest.md): if you would rather call Spectron over HTTP directly
