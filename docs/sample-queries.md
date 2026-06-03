---
position: 5
title: Sample queries
description: Learn how to get started with SurrealDB
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/sample-queries.mdx"
---

Welcome to SurrealDB! In this guide, you will learn about the various ways you can start using SurrealDB with interactive examples. Before we dive in, let's cover some basics.

## Running queries in SurrealDB

Much like any other database, you can communicate with SurrealDB by executing queries.

Queries are written using [SurrealQL](reference/query-language/index.md), SurrealDB's powerful and flexible query language. While SurrealQL takes inspiration from traditional SQL, it is designed to be more expressive and flexible, allowing you to query your data in a variety of ways.

Let's take a look at some of the basic queries you can run in SurrealDB.

### Creating data with CREATE

Before we can start querying data, we need to create some records. This can be done using the [CREATE statement](reference/query-language/statements/create.md), which is used to add new records to the database.

The following example demonstrates how to create a record in the `category` table, initialised with a `name` field and a `created_at` field. Press the *"Run query"* button to execute the query and view the response.

  
 

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%7B%60%0A%09%09CREATE%20category%20SET%0A%09%09%09name%20%3D%20%27Technology%27%2C%0A%09%09%09created_at%20%3D%20time%3A%3Anow%28%29%3B%0A%09%60%7D)

After executing this statement, the `category` record is created in the database, and a randomly generated unique id known as a [Record ID](reference/query-language/language-primitives/data-types/record-ids.md) is assigned to it. This ID represents the primary key of our record, and can be used to reference the record in future queries.

When creating records, you can also explicitly set the record ID. This can be useful when you are able to use predictable unique record IDs such as `company:surrealdb` or `planet:earth`. In the following example, we create a person record with the ID `john`, and set the `first`, `last`, `age`, `admin`, and `signup_at` fields.

  

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%7B%60%0A%09%09CREATE%20person%3Ajohn%20SET%0A%09%09%09first%20%3D%20%27John%27%2C%0A%09%09%09last%20%3D%20%27Adams%27%2C%0A%09%09%09age%20%3D%2029%2C%0A%09%09%09admin%20%3D%20true%2C%0A%09%09%09signup_at%20%3D%20time%3A%3Anow%28%29%3B%0A%09%60%7D)

One of the many powerful features of SurrealDB is the ability to write subqueries, which in the following example is used to populate the `category` field of the `article` record with the ID of the `Technology` category.

  

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%7B%60%0A%09%09CREATE%20article%20SET%0A%09%09%09created_at%20%3D%20time%3A%3Anow%28%29%2C%0A%09%09%09author%20%3D%20person%3Ajohn%2C%0A%09%09%09title%20%3D%20%27Lorem%20ipsum%20dolor%27%2C%0A%09%09%09text%20%3D%20%27Donec%20eleifend%2C%20nunc%20vitae%20commodo%20accumsan%2C%20mauris%20est%20fringilla.%27%2C%0A%09%09%09category%20%3D%20SELECT%20VALUE%20id%20FROM%20ONLY%20category%20WHERE%20name%20%3D%20%27Technology%27%20LIMIT%201%3B%0A%09%60%7D)

### Querying data with SELECT

After inserting records into your database, you can now use the [SELECT statement](reference/query-language/statements/select.md) to retrieve data. While this statement will be familiar to anyone who has used traditional SQL before, SurrealDB's SELECT statement includes additional powerful features inspired by NoSQL databases.

For example, in addition to selecting records from a single table, you can also select records from multiple tables, or select specific records by their Record ID.

  

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%7B%60%0A%09%09--%20Select%20all%20records%20from%20a%20table%0A%09%09SELECT%20%2A%20FROM%20article%3B%0A%0A%09%09--%20Select%20records%20from%20multiple%20tables%0A%09%09SELECT%20%2A%20FROM%20category%2C%20person%3B%0A%0A%09%09--%20Selecting%20specific%20records%0A%09%09SELECT%20%2A%20FROM%20person%3Ajohn%3B%0A%09%60%7D)

The [SELECT statement](reference/query-language/statements/select.md) offers a variety of different features, such as the ability to filter on fields, fetch and resolve record id contents, and the ability to access data directly from Record IDs without the need of JOINs or complex queries.

The following query combines a number of such features:
- **Filtering**: Use the `WHERE` clause to only include records where the author's age is less than 30.
- **Fetching**: Use the `.*` idiom to replace record ids with their actual field values.
- **Specific fields**: Only want to retrieve the title and author fields from the article table.
- **Record links**: Structure the field data from the author in a preferred format, including an alias for the field `name.full`.

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%0A%09%09SELECT%20%0A%09%09%09title%2C%20%0A%09%09%09category.%2A%2C%20%0A%09%09%09author.%7B%0A%09%09%09%09age%2C%0A%09%09%09%09name%3A%20name.full%2C%0A%09%09%09%7D%20%0A%09%09FROM%20article%0A%09%09WHERE%20author.age%20%3C%2030%3B%0A%09)

### Modifying data with UPDATE

Records can be updated using the [UPDATE](reference/query-language/statements/update.md) statement, which allows you to modify the contents of existing records.

Much like the `SELECT` statement, you can pass both table names and individual record IDs to the `UPDATE` statement. This allows you to update specific records, or update multiple records at once.

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%0A%09%09UPDATE%20person%3Ajohn%20SET%0A%09%09%09age%20%2B%3D%201%2C%0A%09%09%09admin%20%3D%20false%3B%0A%09)

The `UPDATE` statement offers a variety of features to further filter down records, and apply different update strategies. The following example demonstrates how we can merge new data into records matching a specific condition.

  

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%0A%09%09UPDATE%20person%20MERGE%20%7B%0A%09%09%09age%3A%2030%2C%0A%09%09%09admin%3A%20false%0A%09%09%7D%0A%09)

In addition to the `UPDATE` statement, SurrealDB also offers an [UPSERT statement](reference/query-language/statements/upsert.md), which has the added functionality of creating a record if it does not already exist. This can be useful when you want to update a record if it exists, or create it if it does not.

### Deleting data with DELETE

You can also delete records from your database using the [DELETE statement](reference/query-language/statements/delete.md). This statement allows you to remove records from your database, either by specifying the record ID, or by using specific conditions.

The following example demonstrates the use of the `RETURN` clause, which instructs SurrealDB to return the records before they are deleted.

  

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=%0A%09%09DELETE%20article%20WHERE%20author.name.first%20%3D%20%27David%27%20RETURN%20BEFORE%3B%0A%09)

Congratulations, you're now on your way to database and API simplicity! For the next steps, we will explore the different ways to integrate SurrealDB into your applications.
