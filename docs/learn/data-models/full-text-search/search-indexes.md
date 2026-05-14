---
position: 3
title: Search indexes
description: Apply FULLTEXT ANALYZER indexes to single fields per index, and understand common parse errors when listing multiple columns.
source: "https://github.com/surrealdb/docs.surrealdb.com/blob/main/src/content/learn/data-models/full-text-search/search-indexes.mdx"
---

# Search indexes

## Defining an index that uses an analyzer

Once a search analyzer is defined, it can be applied to the fields of a table to make them searchable by [defining an index](../../../reference/query-language/statements/define/indexes.md#full-text-search-index) that uses the `FULLTEXT ANALYZER` clause.

```surql
DEFINE ANALYZER my_analyzer
  TOKENIZERS class
  FILTERS lowercase, ascii;

DEFINE INDEX body_index 
  ON TABLE article
  FIELDS body
  FULLTEXT ANALYZER my_analyzer;

DEFINE INDEX title_index
  ON TABLE article
  FIELDS title 
  FULLTEXT ANALYZER my_analyzer;
```

An index can only be defined on a single field (column).

```surql
DEFINE ANALYZER my_analyzer
  TOKENIZERS class
  FILTERS lowercase, ascii;

DEFINE INDEX body_index 
  ON TABLE article 
  FIELDS body, title 
  FULLTEXT ANALYZER my_analyzer;
```

```surql title="Output"
'Parse error: Expected one column, found 2
 --> [5:55]
  |
5 | ...LDS body, title FULLTEXT ANALYZER my_analyzer;
  |              ^^^^^
'
```

For querying with `@@`, BM25, and highlights, continue to [Scoring and ranking](scoring-and-ranking.md).
