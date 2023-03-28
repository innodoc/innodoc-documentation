---
title: External Links
---

The easiest way to create a link is to enclose the URL in the characters `<` and
`>`.

:::::example
::::tabs{labels="Result,Markdown"}
:::tab-item
<https://www.tu-berlin.de/>
:::

:::tab-item
```markdown
<https://www.tu-berlin.de/>
```
:::
::::
:::::

Usually, however, it is desirable to specify a link text.

:::::example
::::tabs{labels="Result,Markdown"}
:::tab-item
[TU Berlin](https://www.tu-berlin.de)
:::

:::tab-item
```markdown
[TU Berlin](https://www.tu-berlin.de)
```
:::
::::
:::::

Links can also be provided with a title. This increases the Accessibility.
It is displayed when somebody hovers with the mouse over the link.

:::::example
::::tabs{labels="Result,Markdown"}
:::tab-item
[TU Berlin](https://www.tu-berlin.de "Homepage of TU Berlin")
:::

:::tab-item
```markdown
[TU Berlin](https://www.tu-berlin.de "Homepage of TU Berlin")
```
:::
::::
:::::

:::info
Section [](/section/02-elements/04-media#images-as-link) describes
how an image can be linked.
:::

Link addresses can also be written collectively in a link list. For this
purpose an identifier in square brackets is used instead of an address in round
brackets. At the end of the document, a link list must be written that maps
link identifiers to addresses.

:::::example
::::tabs{labels="Result,Markdown"}
:::tab-item
[Link to TU Berlin][TU Berlin]  
[innoConv]
:::

:::tab-item
```markdown
[Link to TU Berlin][TU Berlin]  
[innoConv]
```

Put a link list at the very end of your document.

```markdown
[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
```
:::
::::
:::::

[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
