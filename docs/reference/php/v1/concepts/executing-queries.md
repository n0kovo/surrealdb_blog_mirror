---
position: 3
title: Executing queries
description: Interact with the database and perform CRUD operations using version 1 of the SurrealDB PHP SDK.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/php/v1/concepts/executing-queries.mdx"
---

# Executing queries

The methods below are used to interact with the database and perform CRUD operations.
You can also use the [`query`](../methods/query.md) method to run [SurrealQL statements](../../../query-language/statements/overview.md) against the database.

## Creating records

If we wish to create a new record in the database, we can use the [`create`](../methods/create.md) method. The first argument
is the table name and the second argument is an associative array with the field names and values.

```php
$person = $db->create("person:tobie", [
	"name" => "Tobie",
	"lastname" => "Morgan Hitchcock",
	"age" => 30,
	"hobbies" => ["reading", "coding"]
]);
```

## Selecting records

After creating a record, you can use the [`select`](../methods/select.md) method to fetch the newly created person.
The first argument is the newly created person's ID or a string which is the table name.

```php
$person = $db->select($person->id);
```

Or you can fetch it manually by using the RecordID or RecordStringId.

```php
// using the StringRecordId
$id = StringRecordId::create("person:tobie");
$person = $db->select($id);

// using the RecordId
$id = RecordId::create("person", "tobie");
$person = $db->select($id);
```

## Updating records

To update a record, you can use the [`update`](../methods/update.md) method. The first argument is the RecordID or a StringRecordId,
and the second argument is an associative array with the field names and values. Updating a record can be done in 3 ways:

	
**update**

The [`update`](../methods/update.md) method will replace the entire record with the new values. So make sure you include all the fields in the associative array.
		```php
		$person = $db->update($person->id, [
			"name" => "Tobie",
			"lastname" => "Morgan Hitchcock",
			"age" => 31
		]);
		```
		You can find more information about updating a record using the update method in [the `UPDATE` statement reference](../../../query-language/statements/update.md).

	
**merge**

The [`merge`](../../../query-language/statements/update.md#merge-clause) method will merge the new values with the existing record. If the field already exists, it will be replaced with the new value.
		```php
		$person = $db->merge($person->id, [
			"age" => 31
		]);
		```
		You can find more information about updating a record using the merge method in [the RPC protocol reference](../../../rest-api/rpc-protocol.md#merge).

	
**patch**

The [`patch`](../methods/patch.md) method will update a field in a single or multiple record(s) based on the path provided.
		```php
		$person = $db->patch($person->id, [
			"path" => "/hobbies/0",
			"op" => "replace",
			"value" => "writing"
		]);
		```
		You can find more information about updating a record using the patch method in [the `UPDATE` statement reference](../../../query-language/statements/update.md).

## Deleting records

To delete a record, you can use the [`delete`](../methods/delete.md) method. The first argument is the RecordID or a StringRecordId.

```php
$db->delete($person->id);
```

or we can use the RecordId or StringRecordId to delete the record.

```php
$id = StringRecordId::create("person:tobie");
$db->delete($id);

$id = RecordId::create("person", "tobie");
$db->delete($id);
```
