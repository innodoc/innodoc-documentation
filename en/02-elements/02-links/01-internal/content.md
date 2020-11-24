---
title: Internal Links
---

You can link to other sections, specific elements within sections and "special"
pages.

## Link to other sections

To create a link to another section, you need to specify the section ID. If you
leave out the link text the section number and title will be shown.

::: {.example}

```markdown
[](/section/02-elements/04-media)  
[other section](/section/02-elements/04-media)
```

[](/section/02-elements/04-media)  
[other section](/section/02-elements/04-media)
:::

If you specify a non-existent section the link will still be shown but leads to
an error page:  
[This is a Link to a non-existent chapter.](/section/does-not-exist)

## Link with anchors

In order to link to a particular element within a section you can use anchor
IDs. These IDs need to be unique within one page and can be assigned manually.

::: {.example}
Link to heading _Videos_ in another section:

```markdown
[](/section/02-elements/04-media#videos)
```

[](/section/02-elements/04-media#videos)
:::

You can assign IDs by adding the identifier preceded by a `#` symbol.

::: {.example #heading-example}
```markdown
## Heading with ID {#my-id}

[Link to heading](#my-id)
```

## Heading with ID {#my-id}

[Link to heading](#my-id)
:::

::: {.info}
Each heading is automatically assigned an ID if not explicitly given. The
generated ID is derived from the text.

```markdown
## This is a test

[Link to heading](#this-is-a-test)
```

## This is a test

[Link to heading](#this-is-a-test)
:::

## Link to special pages

Every course includes the special pages _Index Page_, _Progress_ and _Table of
contents_. They don't have a section ID but you can still link to them using
special identifiers `___INDEX_PAGE___`, `___PROGRESS___` and `___TOC___`.

::: {.example}

```markdown
[](___INDEX_PAGE___)  
[](___PROGRESS___)  
[](___TOC___)
```

[](___INDEX_PAGE___)  
[](___PROGRESS___)  
[](___TOC___)
:::
