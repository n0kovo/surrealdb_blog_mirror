---
position: 2
title: Installation
description: The SurrealDB SDK for Java is available on Maven Central and can be installed using Gradle or Maven.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/java/installation.mdx"
---

# Installation

The SurrealDB SDK for Java is available on the [Maven Central](https://mvnrepository.com/artifact/com.surrealdb/surrealdb) repository. You can add it to your project using Gradle or Maven.

> [!NOTE]
> The SDK requires Java JDK version `8` or later.

### Install the SDK

Install the [SurrealDB SDK](https://mvnrepository.com/artifact/com.surrealdb/surrealdb) from Maven Central using [Gradle](https://gradle.org/) or [Maven](https://maven.apache.org/).

  
**Gradle (Groovy)**

```groovy
ext {
    surrealdbVersion = "3.0.0-ALPHA.1"
}

dependencies {
    implementation "com.surrealdb:surrealdb:${surrealdbVersion}"
}
```

  
  
**Gradle (Kotlin)**

```kotlin
val surrealdbVersion by extra("3.0.0-ALPHA.1")

dependencies {
    implementation("com.surrealdb:surrealdb:${surrealdbVersion}")
}
```

  
**Maven**

```xml
<dependency>
    <groupId>com.surrealdb</groupId>
    <artifactId>surrealdb</artifactId>
    <version>3.0.0-ALPHA.1</version>
</dependency>
```

### Import the SDK

After installing, you can access the SDK by importing from the `com.surrealdb` package.

```java
```

## Next steps

- [Quickstart](start.md) for a complete working example
- [Connecting to SurrealDB](concepts/connecting-to-surrealdb.md) for connection options and protocols
- [Authentication](concepts/authentication.md) for signing in and managing credentials
