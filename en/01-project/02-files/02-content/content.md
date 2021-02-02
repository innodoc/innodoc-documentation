---
title: Content files
---

Content is written using the [Markdown format]{data-index-term="Markdown"}.
There needs to be one content file for every section/page and language. Content
files consist of a [meta block](#meta-data) at the top of the file followed by
the actual content. A detailed explanation of the various content elements can
be found in section [](/section/02-elements).

For every **section** there must be a file `content.md` in the corresponding
section folder of the respective language. For example, the English content for
the section `01-project/02-files/02-content` is contained in the file
`en/01-project/02-files/02-content/content.md`.

For every **page** there must be a content file in the `_pages` folder of the
respective language. The filename corresponds to the page ID as specified in the
[course manifest](/section/01-project/02-files/01-manifest#pages). For example
the English content for the page `about` is contained in the file
`en/_pages/about.md`.

## Meta data {#meta-data}

Every content file needs to have a so-called [YAML
block]{data-index-term="YAML"} at the top of the file with at least a `title`
key.

:::{.example}
```yaml
---
title: About this course
short_title: About
---
```
:::

## `title` (mandatory)

> Page/section title

Every content file needs to have a title defined. This is the name that will
show up in the main header at the top of the page but also in the [table of
contents]{data-index-term="table of contents"} and other menus.

## `short_title` (optional)

> Page/section title (short)

A shorter version of the title may be specified using the field `short_title`.
It is used in places with limited space.

## `type` (optional)

> [Section type]{data-index-term="Section type"}

Sections can be one of the following types: `regular`, `exercises`, `test`. If
not specified the value defaults to `regular`. Pages do not support this key.

Exercise and test sections will be marked with a recognizable icon in the table
of contents. Test sections are shown separately in the [progress
overview](___PROGRESS___). Furthermore test exercises are only evaluated after
the test is submitted.

:::{.info}
[](/section/02-elements/07-interactive-exercises/01-text) is marked as an
exercise section. In section [](/section/03-test) an example test section can
be found.
:::
