---
title: External Links
---

The easiest way to create a link is to use the characters `<` and `>`.

```markdown
<https://www.tu-berlin.de/>
```

<https://www.tu-berlin.de/>

Usually, however, it is desirable to specify a link text.

```markdown
[TU Berlin](https://www.tu-berlin.de)
```

[TU Berlin](https://www.tu-berlin.de)

Links can also be provided with a title. This increases the Accessibility.
It is displayed when somebody hovers with the mouse over the link.

```markdown
[TU Berlin](https://www.tu-berlin.de "Homepage of TU Berlin")
```

[TU Berlin](https://www.tu-berlin.de "Homepage of TU Berlin")

::: {.info}
Section []{data-link-section="02-elements/07-media#images-as-link"} describes
how an image can be linked.
:::

Link addresses can also be written collectively in a link list. For this
purpose an identifier in square brackets is used instead of an address in round
brackets. At the end of the document, a link list must be written that maps
link identifiers to addresses.

```markdown
[Link to TU Berlin][TU Berlin]

[innoConv]

# At the very end of the document
[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://gitlab.tu-berlin.de/innodoc/innoconv
```

[Link to TU Berlin][TU Berlin]

[innoConv]

[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://gitlab.tu-berlin.de/innodoc/innoconv
