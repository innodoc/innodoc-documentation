---
title: Content files
---

Every content folder of a section needs to have file `content.md`. This file is
written in [Markdown format]{data-index-term="Markdown"}.

For pages there is a Markdown file in the `_pages` folder of the respective
language. The filename corresponds to the page ID as specified in the
[course manifest](/section/01-project/02-files/01-manifest#pages), e.g.
`about.md` for a page with the ID `about`.

At the top of every content file there is a so-called
[YAML block]{data-index-term="YAML"}. The document title is specified by using
the `title` field. This is also the name used in the
[table of contents]{data-index-term="table of contents"} or, for a page, in the
menus. For pages another field `short_title` can be specified. It's being used
for menus where space is limited.

:::{.example}
```yaml
---
title: About this course
short_title: About
---
```
:::

After that the actual content follows. A detailed explanation of different
possibilities can be found in section [](/section/02-elements).
