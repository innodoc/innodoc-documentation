---
title: External Links
---

The easiest way to create a link is to enclose the URL in the characters `<` and
`>`.

:::example
**Markdown**

```markdown
<https://www.tu-berlin.de/>
```

**Result**

<https://www.tu-berlin.de/>
:::

Usually, however, it is desirable to specify a link text.

:::example
**Markdown**

```markdown
[TU Berlin](https://www.tu-berlin.de)
```

**Result**

[TU Berlin](https://www.tu-berlin.de)
:::

Links can also be provided with a title. This increases the Accessibility.
It is displayed when somebody hovers with the mouse over the link.

:::example
**Markdown**

```markdown
[TU Berlin](https://www.tu-berlin.de "Homepage of TU Berlin")
```

**Result**

[TU Berlin](https://www.tu-berlin.de "Homepage of TU Berlin")
:::

:::info
Section [](/section/02-elements/04-media#images-as-link) describes
how an image can be linked.
:::

Link addresses can also be written collectively in a link list. For this
purpose an identifier in square brackets is used instead of an address in round
brackets. At the end of the document, a link list must be written that maps
link identifiers to addresses.

:::example
**Markdown**

Use links like so in your document.

```markdown
[Link to TU Berlin][TU Berlin]  
[innoConv]
```

Put a link list at the very end of your document.

```markdown
[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
```

**Result**

[Link to TU Berlin][TU Berlin]  
[innoConv]
:::

[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
