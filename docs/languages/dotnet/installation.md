---
position: 2
title: Installation
description: In this section, you will learn how to install the .NET SDK in your project.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/index/languages/dotnet/installation.mdx"
---

export const value = await fetchNugetVersion();
export const packageReferenceXml = `<PackageReference Include="SurrealDb.Net" Version="${value}" />`;

# Installation

Before you can use this SDK in your .NET applications regardless of your environment, you need to install and import it into your project.
This guide will walk you through the process of installing and importing the SDK into your project.

## Install the SDK

- Create a new project using your favorite IDE (Visual Studio, JetBrains Rider, etc...) 
- or use an existing template from the `dotnet new` command.

Once ready, add the SurrealDB SDK to your dependencies:

  
**.NET CLI**

```bash
dotnet add package SurrealDb.Net
```

  
**PackageReference**

<pre>
  <code class="language-xml">
    {packageReferenceXml}
  </code>
</pre>

  

Alternatively, you can install the SDK via the NuGet user interface provided in your IDE.
Here is an example within Visual Studio:

![Visual Studio NuGet Package Manager](../../assets/img/dotnet-nuget-search.png)

## Initialize the SDK

The SDK's initialization may vary depending on the context of your project.

The de facto initialization method is to create and [consume a SurrealDbClient created manually](core/create-a-new-connection.md).
Most .NET projects provide a way to configure services using [Dependency Injection](core/dependency-injection.md), which is the recommended way to use the SDK in your application.
