---
position: 1
title: version
description: The version method in the SurrealDB PHP SDK retrieves the current version of a remote database.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/php/v1/methods/version.mdx"
---

# `->version()` {#version}

This method retrieves the current version of a remote database.

```php title="Method Syntax"
$db->version();
```

### Example usage
```php
try {
	$version = $db->version();
	echo "The remote database is running version $version.";
} catch (Exception $e) {
	echo "An error occurred while retrieving the version: " . $e->getMessage();
}

```
