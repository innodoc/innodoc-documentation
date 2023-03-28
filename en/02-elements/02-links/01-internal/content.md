---
title: Internal Links
---

It is possible to create links to any internal application page using the
`app:ROUTE|PARAMETER` schema.

::::grid
:::grid-item{xs="4" md="2"}
`ROUTE`
:::
:::grid-item{xs="8" md="10"}
The name of the route. An [overview of all routes](#routes) can be found at the
end of this section.
:::
:::grid-item{xs="4" md="2"}
`PARAMETER`
:::
:::grid-item{xs="8" md="10"}
The parameter of the route is only specified for links to pages and sections.
:::
::::

## Links to Sections and Pages

To create a link to a section or a page, the *section path* or *page name* must
be provided as a parameter. The route and parameter are separated by a pipe
symbol `|`. If no link text is specified, the title of the link destination is
automatically inserted.

:::::example
::::tabs{labels="Result,Markdown"}
:::tab-item
[](app:section|02-elements/04-media)  
[other section](app:section|02-elements/04-media)  
[](app:page|about)  
[other page](app:page|about)
:::

:::tab-item
```markdown
[](app:section|02-elements/04-media)  
[other section](app:section|02-elements/04-media)  
[](app:page|about)  
[other page](app:page|about)
```
:::
::::
:::::

If a linked section or page does not exist, an error message will be displayed:  
[This is a link to a non-existent chapter.](/section/does-not-exist)

## References to elements

To refer to a specific element within a section, anchor IDs are used. These must
be unique within a document and can be assigned manually.

Anchor IDs can be assigned to content elements by specifying the identifier with
a preceding `#`. This allows for referencing headings, as well as other
elements.

:::::example
Link to heading with manually assigned ID..

::::tabs{labels="Result,Markdown"}
:::tab-item
### Heading with ID {#my-id}

[Link to heading](#my-id)
:::

:::tab-item
```markdown
### Heading with ID {#my-id}

[Link to heading](#my-id)
```
:::
::::

If no ID is explicitly assigned, headings are automatically assigned an ID
derived from the text. For consistency, especially in multilingual texts, it is
recommended to manually assign an explicit ID to referenced headings.

::::tabs{labels="Result,Markdown"}
:::tab-item
### Heading with automatic ID

[Link to heading](#heading-with-automatic-id)
:::

:::tab-item
```markdown
### Heading with automatic ID

[Link to heading](#heading-with-automatic-id)
```
:::
::::

Link to heading _Videos_ in another chapter:

::::tabs{labels="Result,Markdown"}
:::tab-item
[Subsection _Videos_ in chapter _Images and Videos_](/section/02-elements/04-media#videos)
:::

:::tab-item
```markdown
[Subsection _Videos_ in chapter _Images and Videos_](/section/02-elements/04-media#videos)
```
:::
::::
:::::

## References to Other Pages

In every course, there are additional pages such as the glossary and table of
contents. These are referenced by using the corresponding route.

:::::example
::::tabs{labels="Result,Markdown"}
:::tab-item
[](app:home)  
[](app:progress)  
[](app:toc)
:::

:::tab-item
```markdown
[](app:home)  
[](app:progress)  
[](app:toc)
```
:::
::::
:::::

### Overview of Routes {#routes}

Below is an overview of the available application routes.

:::table[Applikationsrouten]
| Name                   | Destination       | Parameter    |
|------------------------|-------------------|--------------|
| `page`                 | Content page      | Page name    |
| `section`              | Content section   | Section path |
| `home`                 | Course homepage   |              |
| `progress`             | Learning progress |              |
| `toc`                  | Table of contents |              |
| `glossary`             | Glossary          |              |
| `user:login`           | Login             |              |
| `user:forgot-password` | Password recovery |              |
| `user:sign-up`         | Create account    |              |
:::
