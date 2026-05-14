---
title: "Surreal Stickies 2.0: Adding Graph Relations, Live Queries, and Authentication"
slug: "surreal-stickies-2-0-adding-graph-relations-live-queries-and-authentication"
date: "2023-10-13T00:00:00.000Z"
categories:
  - "tutorials"
read_time: "9 min read"
summary: "Welcome back to the second instalment of our tutorial series on building a notes app with Next.js, Tailwind, and SurrealDB."
source: "https://surrealdb.com/blog/surreal-stickies-2-0-adding-graph-relations-live-queries-and-authentication"
cover: "../../assets/613b61a85c00af38.jpg"
---

# Surreal Stickies 2.0: Adding Graph Relations, Live Queries, and Authentication

![Surreal Stickies 2.0: Adding Graph Relations, Live Queries, and Authentication](../../assets/613b61a85c00af38.jpg)

## Introduction

Welcome back to the second instalment of our tutorial series on building a notes app with Next.js, Tailwind, and SurrealDB. In [Part 1](/blog/tutorial-build-a-notes-app-with-next-js-tailwind-and-surrealdb), we laid the groundwork for Surreal Stickies, a full-stack note-taking application. We covered the essentials, from setting up your development environment to building CRUD APIs and a user interface. If you haven't read it yet, we recommend starting there as a prerequisite to get the most out of this tutorial.

In this tutorial, we're taking Surreal Stickies to the next level! With the release of SurrealDB 1.0, we have many new features to explore and integrate into our application. In this part, we will introduce:

👉 [Multi-user capabilities, authentication and permissions.](https://www.notion.so/Surreal-Stickies-2-0-Adding-Graph-Relations-Live-Queries-and-Authentication-b54866eaf82a4ba3ac300b0eceb880ef?pvs=21)

👉 [Tagging features for better note organisation.](https://www.notion.so/Surreal-Stickies-2-0-Adding-Graph-Relations-Live-Queries-and-Authentication-b54866eaf82a4ba3ac300b0eceb880ef?pvs=21)

👉 [Real-time updates using Live Queries](https://www.notion.so/Surreal-Stickies-2-0-Adding-Graph-Relations-Live-Queries-and-Authentication-b54866eaf82a4ba3ac300b0eceb880ef?pvs=21).

So, let's dive right in and make our notes app more efficient and customisable!

For those who want to directly skip to running the application, you can clone it from our examples repository on [GitHub](https://github.com/surrealdb/examples). Steps to set up the project and run it for the first time are included in our [README](https://github.com/surrealdb/examples/tree/main/notes-v2).

After you build this application, here’s how your updated stickies app will look! In this example, we’re helping Harry Potter take some critical notes on his first day at Hogwarts!

![stickiesdesktop.png](../../assets/24dacb9ee958880e.jpg)

## Direct Database Connection

In the new version, we've eliminated the need for a separate API layer to interact with the database. By directly connecting to SurrealDB, we've streamlined the architecture and simplified the codebase.

In contrast, the first version used a more traditional approach, where API routes were defined to handle CRUD operations. These routes would then interact with SurrealDB.

Let’s start by running the SurrealDB instance locally on our machine by running the following command in your terminal.

```surrealql
surreal sql --conn ws://localhost:3001 --user root --pass root --ns test --db test --pretty
```

This command will open up a particular terminal window where you can type and run database commands directly. We recommend reading more about the [SQL command](/docs/surrealdb/cli/sql) in SurrealQL.

### Creating and Running Schemas

Now that we are connected to SurrealDB, let's recreate the schemas for our stickies app and manually add them to our SurrealDB instance. Specifically, we'll define schemas for our tables - `user`, `tag` and `sticky`.

![pinknodes.png](../../assets/95f0a9015c7263b6.jpg)

### User Table

The `user` table will store information about each user, such as their name, username, and password. We also define permissions to ensure users can only modify their own data.

Define [a schemafull table](/docs/surrealql/statements/define/table) named `user` and set the permissions for the user table which allows select, update, and delete operations only where the ID of the record matches the authenticated user's ID.

```surrealql
DEFINE TABLE user SCHEMAFULL
    PERMISSIONS
        FOR select, update, delete WHERE id = $auth.id;
```

Define a field named `name` of type string on the user table and assert that the length of the string must be greater than or equal to 2

```surrealql
DEFINE FIELD name ON user TYPE string ASSERT string::len($value) >= 2;
```

Define the field `username` of type string and set the value to be the lowercase version of the input

```surrealql
DEFINE FIELD username ON user TYPE string VALUE string::lowercase($value);
```

Define the field `password` of type string and set its permissions such that the password field cannot be selected

```surrealql
DEFINE FIELD password ON user TYPE string PERMISSIONS FOR select NONE;
```

Define the field `created` with its value set to the current time the record is created. If the record is updated, the created field will not change

```surrealql
DEFINE FIELD created ON user VALUE $before OR time::now() DEFAULT time::now();
```

Define the field `updated` and have its value set to the current time whenever the record is created or updated

```surrealql
DEFINE FIELD updated ON user VALUE time::now() DEFAULT time::now();
```

In SurrealDB 1.0, you can now add traditional and [unique indexes](/docs/surrealql/statements/define/indexes) to your fields. So, we define a unique index on the `username` field, ensuring that no two user records can have the same username.

```surrealql
DEFINE INDEX unique_username ON user FIELDS username UNIQUE;
```

Define an event that triggers when a user record is deleted. It deletes all sticky and tag records where the author or owner matches the ID of the deleted user.

```surrealql
DEFINE EVENT removal ON user WHEN $event = 'DELETE' THEN {
    DELETE sticky WHERE author = $before.id;
    DELETE tag WHERE owner = $before.id;
};
```

#### Tag table

The `tag` table will store information about each tag, including its name and the owner who created it. The owner field will resemble the user record type.

```typescript
DEFINE FIELD owner ON tag TYPE record<user>
```

Permissions will ensure that only the owner can modify or delete their tags. We will later focus on how we use the tag table.

#### Sticky table

The `sticky` table will store details about each sticky note, such as its content, colour, and the author who created it. Table permissions ensure that only the author can perform CRUD operations on their sticky notes.

#### Assigned-To table

The `assigned_to` table will establish a [many-to-many relationship](<https://en.wikipedia.org/wiki/Many-to-many_(data_model)>) between tags and sticky notes. It will contain fields to link a tag with a sticky note and timestamps for creation and updates. Table permissions will ensure that only the owner of the tag and the sticky note can modify or delete the relationship.

You can find all the schema queries in the [schema folder](https://github.com/surrealdb/examples/tree/main/notes-v2/src/schema) of the notes-v2 project.

### Multi-user capabilities, authentication and permissions

Our authentication layer will reside inside our database itself. Defined in the [`auth.surql`](https://github.com/surrealdb/examples/blob/main/notes-v2/src/schema/auth.surql) schema it will handle the sign-in and sign-up processes. We will let our front-end code take care of the signout process.

```surrealql
DEFINE SCOPE user SESSION 7d
    SIGNIN (
        SELECT * FROM user WHERE username = $username AND crypto::argon2::compare(password, $password)
    )
    SIGNUP (
        CREATE user CONTENT {
            name: $name,
            username: $username,
            password: crypto::argon2::generate($password)
        }
    );
```

The `DEFINE SCOPE` [statement](/docs/surrealql/statements/define/scope) is used to set up the scoped authentication rules for user sessions. Here's a breakdown:

- `DEFINE SCOPE user SESSION 7d`: This sets up a scope named `user` and specifies that the session will be valid for 7 days. We’ve picked up a random number here.
- `SIGNIN (...)`: This part of the statement defines the signing-in logic. It selects a user from the `user` table where the username matches the provided `$username` and the `$password` matches the hashed `password` stored in the database.
- `SIGNUP (...)`: This part defines the logic for signing up a new user. It creates a new record in the `user` table with the name, username, and a hashed version of the password.

It uses SurrealDB's built-in [cryptographic functions](/docs/surrealql/functions/database/crypto) to manage user credentials securely.

![SiginSignUp.png](../../assets/d194edf0aa312357.jpg)

## Add tagging features for better note organisation

In this section, we'll walk through implementing tagging functionalities in our Surreal Stickies app using SurrealDB's graph capabilities. We'll focus on creating, assigning, and deleting tags and how these operations interact with our schema.

First, let's create a new file called `tag_assignments.ts` in your project's `lib` directory. This file will house the logic for tag assignments.

### Step 1: Implement the `assignTag` Function

In `tag_assignments.ts`, let's start by writing a function called `assignTag`. This function will use the `RELATE` statement to establish a relationship between a tag and a sticky note.

```typescript
export async function assignTag({
    tag,
    sticky,
}: {
    tag: Tag['id'];
    sticky: Sticky['id'];
}) {
    tag = record('tag').parse(tag);
    sticky = record('sticky').parse(sticky);

    const [result] = await surreal.query<[AssignedTo[]]>(
        /* surrealql */ `
            RELATE ONLY $tag->assigned_to->$sticky;
        `,
        { tag, sticky }
    );

    return result.result && result.result.length > 0;
}
```

This query will create a new edge from the tag to the sticky only if it doesn't already exist.

### Step 2: Implement the `unassignTag` Function

Next, let's write another function called `unassignTag`. This function will remove the relationship between a tag and a sticky note.

```typescript
export async function unassignTag({
    tag,
    sticky,
}: {
    tag: Tag['id'];
    sticky: Sticky['id'];
}) {
    tag = record('tag').parse(tag);
    sticky = record('sticky').parse(sticky);

    const [result] = await surreal.query<[AssignedTo[]]>(
        /* surrealql */ `
            DELETE $tag->assigned_to WHERE out = $sticky RETURN BEFORE;
        `,
        { tag, sticky }
    );

    return result.result && result.result.length > 0;
}
```

The `DELETE` query will delete the edge from the tag to the sticky.

### Step 3: Implement the `assignedTags` Function

Finally, let's write a function called `assignedTags` to fetch all tags related to a specific sticky note.

```typescript
export async function assignedTags(sticky: Sticky['id']) {
    sticky = record('sticky').parse(sticky);

    const [result] = await surreal.query<[Tag[]]>(
        /* surrealql */ `
            $sticky<-assigned_to<-tag.*
        `,
        { sticky }
    );

    return z
        .array(Tag)
        .parse(result.result ?? [])
        .filter(
            ({ id }, index, arr) =>
                index == arr.findIndex((item) => item.id == id)
        );
}
```

The `RELATE` query fetches all tags that are related to the sticky through the `assigned_to` edge.

And there you have it! You've successfully added tagging functionalities to your Surreal Stickies app using SurrealDB's graph capabilities. Now go ahead and run your app to see the tagging in action!

![tags.png](../../assets/1d194dbf0450820f.jpg)

### Enable real-time updates using Live Queries.

As we build our application, one feature that will significantly enhance the user experience across multiple devices is [Live Queries](/features). This ensures that changes are immediately reflected in the UI whenever a sticky note is created, updated, or deleted in the database. To achieve this, we'll integrate Surreal's live queries into our [Zustand store](https://docs.pmnd.rs/zustand/migrations/migrating-to-v4#create) for sticky notes. We use Zustand in order to render our UI correctly and hold the state of all our sticky notes.

```surrealql
surreal.live<Sticky>('sticky', ({ action, result }) => {
    switch (action) {
        case 'CREATE':
        case 'UPDATE':
            store.mergeStickies([Sticky.parse(result)]);
            break;
        case 'DELETE':
            store.deleteSticky(result.id);
            break;
    }
});
```

### Understanding the Live Query Listener

Here's what each part does:

- `surreal.live('sticky')` listens for real-time updates on the `sticky` table.
- The `action` parameter can be either `CREATE`, `UPDATE`, or `DELETE`, representing the type of operation that triggered the update.
- `store.mergeStickies([Sticky.parse(result)]);` merges the newly created or updated sticky note into the existing Zustand state.
- `store.deleteSticky(result.id);` removes the deleted sticky note from the Zustand state.

![LiveQueriesdemo.gif](../../assets/51d9d8e3272b6628.jpg)

## Building the Frontend for Stickies

While the backend logic and database interactions are the main focus of this blog, let's briefly touch upon the frontend structure. The frontend code is organised into components and hooks, each serving a specific purpose in the application. This can be explored in detail in the [GitHub repository](https://github.com/surrealdb/examples/tree/main/notes-v2/src).

### Component Structure

- Add-Sticky Component: Responsible for adding new stickies. Utilises the `useCreateSticky` hook.
- Sticky Component: Manages the display, editing, and deletion of individual stickies. Employs hooks like `useDeleteSticky` and `useUpdateSticky`.
- Tag Picker: Allows users to pick tags for their stickies. Fetches available tags using the `useTags` hook.

### Hooks and State Management

- Stickies Hook: Defined in `[lib/hooks/stickies.ts](https://github.com/surrealdb/examples/blob/main/notes-v2/src/lib/hooks/stickies.ts)`, this hook uses SWR for data fetching and caching.
- Zustand for Auth: Zustand is used for managing the authentication state in `[lib/stores/auth.tsx](https://github.com/surrealdb/examples/blob/main/notes-v2/src/lib/stores/auth.tsx)`.

### A Closer Look at the Navbar Logic

The sign-out logic of our notes app resides inside our Navbar. When a user clicks the sign-out button, the following sequence of actions occurs:

```typescript
const { trigger: signout } = useSWRMutation('auth:signout', async () => {
    await surreal.invalidate(); // Invalidate the user session
    localStorage.removeItem('token'); // Remove the token from local storage
    await refresh(); // Refresh the authentication state
});
```

This logic ensures that the user session is invalidated using the in-built `surreal.invalidate()` [method](/docs/sdk/javascript), and the token is removed from local storage, effectively signing the user out of the application.

For a complete understanding of the sign-out code in the frontend, please refer to the [GitHub repository](https://github.com/surrealdb/examples/blob/2ec96e566c4079e8533ce35ca91cf60311db6964/notes-v2/src/components/navbar.tsx#L15).

## Live Demo and Q&A

We recently hosted a live demo of Surreal Stickies at Surrealdb World. If you missed it, you can [watch the recording here](https://surrealdb.world/conference).

## Wrapping It Up: Your Next Steps

We've come a long way, from setting up our Surreal Stickies app to leveraging top features from the 1.0 release. But this is just the start. Here's how you can keep the momentum going:

👉 Show and Tell: We'd love to see what you've built. Share your project on social media and tag @SurrealDB on [Twitter](https://twitter.com/SurrealDB). Your work could inspire others!

👉 Join the Conversation: Our [community on Discord](https://discord.gg/surrealdb) is a great place to get your questions answered, stay updated on new releases, and showcase your own projects!

So, what are you waiting for? Dive in, explore more, and keep building. Looking forward to seeing you in the community!
