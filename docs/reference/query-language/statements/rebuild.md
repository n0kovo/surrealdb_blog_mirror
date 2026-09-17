---
position: 20
title: REBUILD
description: The REBUILD statement is used to rebuild indexes.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/reference/query-language/statements/rebuild.mdx"
---

# `REBUILD` statement

The `REBUILD` statement is used to rebuild indexes in SurrealDB. It is usually used in relation to a specified [Index](define/indexes.md) to optimise performance. It is useful to rebuild indexes because sometimes [HNSW](define/indexes.md#hnsw-hierarchical-navigable-small-world) index performance can degrade due to frequent updates.

Rebuilding the index will ensure the index is fully optimised.

> [!NOTE]
> By default, `REBUILD INDEX` waits until the rebuild finishes before the statement returns (the same behaviour as `DEFINE INDEX` without `CONCURRENTLY`). Adding `CONCURRENTLY` on the rebuild statement will cause it to return immediately, after which progress can be monitored via [`INFO FOR INDEX`](info.md#index-information). Whether the index was originally created with `CONCURRENTLY` does not affect rebuilds. See the [`CONCURRENTLY` clause](define/indexes.md#using-concurrently-clause) on `DEFINE INDEX` for the same blocking vs non-blocking distinction when creating an index.

## Statement syntax

  
**SurrealQL Syntax**

```syntax title="SurrealQL Syntax"
REBUILD [
	INDEX [ IF EXISTS ] @name ON [ TABLE ] @table [ CONCURRENTLY ]
]
```

  
**Railroad Diagram**

```
                                      ╭────────────────────────────╮                          ╭─────────────╮                ╭────────────────────╮                
                                      │                            │                          │             │                │                    │                
        ╭─────────╮       ╭───────╮   │    ╭────╮     ╭────────╮   │   ┌───────┐     ╭────╮   │  ╭───────╮  │   ┌────────┐   │  ╭──────────────╮  │    ╭───╮       
├┼──────│ REBUILD │───────│ INDEX │───╯────│ IF │─────│ EXISTS │───╰───│ @name │─────│ ON │───╯──│ TABLE │──╰───│ @table │───╯──│ CONCURRENTLY │──╰────│ ; │─────┼┤
        ╰─────────╯       ╰───────╯        ╰────╯     ╰────────╯       └───────┘     ╰────╯      ╰───────╯      └────────┘      ╰──────────────╯       ╰───╯
```

> [!NOTE]
> The `IF EXISTS` and TABLE clauses are optional.

## Example usage

For example, if you have a table called `book` and you have an index called `uniq_isbn` on the `isbn` field, you can rebuild the index using the following query:

```surql
REBUILD INDEX uniq_isbn ON book;
```

[▶ Open in Surrealist](https://app.surrealdb.com/mini?query=CREATE%20book%3A1%20SET%20title%20%3D%20%27Rust%20Web%20Programming%27%2C%20isbn%20%3D%20%27978-1803234694%27%2C%20author%20%3D%20%27Jon%20Doe%27%3B%0A//%20Define%20a%20unique%20index%20on%20the%20isbn%20field%0ADEFINE%20INDEX%20uniq_isbn%20ON%20book%20FIELDS%20isbn%20UNIQUE%3B%0A//%20Rebuild%20this%20index%20incase%20of%20more%20updates%0AREBUILD%20INDEX%20IF%20EXISTS%20uniq_isbn%20ON%20book%3B%0A//%20Check%20that%20the%20index%20has%20been%20created%0AINFO%20FOR%20TABLE%20book%3B%0AREBUILD%20INDEX%20IF%20EXISTS%20idx_author%20ON%20book%3B%0AREBUILD%20INDEX%20IF%20EXISTS%20ft_title%20ON%20book%3B%0A//%20Define%20index%20on%20the%20author%20field%20%0ADEFINE%20INDEX%20idx_author%20ON%20book%20FIELDS%20author%3B%0A//%20Define%20an%20analyzer%20which%20has%20blank%20and%20class%20Tokenizers%20and%20converts%20the%20tokens%20to%20lowercase%20%0ADEFINE%20ANALYZER%20simple%20TOKENIZERS%20blank%2Cclass%20FILTERS%20lowercase%3B%0ADEFINE%20INDEX%20ft_title%20ON%20book%20FIELDS%20title%20FULLTEXT%20ANALYZER%20simple%20BM25%20HIGHLIGHTS%3B%0AREBUILD%20INDEX%20uniq_isbn%20ON%20book%3B%0AREBUILD%20INDEX%20idx_author%20ON%20book%3B%0AREBUILD%20INDEX%20ft_title%20ON%20book%3B%0A//%20Check%20that%20the%20index%20has%20been%20created%0AINFO%20FOR%20TABLE%20book%3B%0A//Checks%20whether%20the%20term%20RUST%20IS%20found%20in%20a%20full-text%20indexed%20field.%0ASELECT%20%2A%20FROM%20book%20WHERE%20title%20%40%40%20%27Rust%27%3B)

### Using if exists clause

The following queries show an example of how to rebuild resources using the `IF EXISTS` clause, which will only rebuild the resource if it exists.

```surql
/**[test]

[[test.results]]
value = "NONE"

*/

REBUILD INDEX IF EXISTS uniq_isbn ON book;
```
