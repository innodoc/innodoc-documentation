---
title: Basics
---

## Paragraphs and line breaks {#paragraphs-and-line-breaks}

Paragraphs are automatically created simply by leaving an empty line between
text. Adding more than one empty line will not create a larger distance between
the paragraphs.

:::info
Line breaks within a paragraph are not displayed in the result. To force a line
break, a double space must be used at the end of the line.
:::

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
:::

:::tab-item
```markdown
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Lorem ipsum
dolor sit amet,
consectetur adipiscing elit.

Lorem ipsum  
dolor sit amet,  
consectetur adipiscing elit.
:::

:::tab-item
```markdown
Lorem ipsum
dolor sit amet,
consectetur adipiscing elit.

Lorem ipsum  
dolor sit amet,  
consectetur adipiscing elit.
```

*Note: There is a double space at the end of each line of the second
paragraph.*
:::
::::
:::::

## Text Formatting {#formatting}

This section demonstrates the possibilities of basic text formatting.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
It is possible to highlight *important words*. There are _two ways_ to
accomplish this.
:::

:::tab-item
```markdown
It is possible to highlight *important words*. There are _two ways_ to
accomplish this.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Even more **important words** are printed in bold. For this there are also two
__different ways__.
:::

:::tab-item
```markdown
Even more **important words** are printed in bold. For this there are also two
__different ways__.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Another formatting option is crossing out ~~words~~ or ~~whole phrases~~.
:::

:::tab-item
```markdown
Another formatting option is crossing out ~~words~~ or ~~whole phrases~~.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
The formatting options can of course be combined. For example, *in an important
part of a sentence you can cross out ~~words~~*.
:::

:::tab-item
```markdown
The formatting options can of course be combined. For example, *in an important
part of a sentence you can cross out ~~words~~*.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
If a formatting character is to be printed, it must be prefixed with a
\*Backslash\*.
:::

:::tab-item
```markdown
If a formatting character is to be printed, it must be prefixed with a
\*Backslash\*.
```
:::
::::
:::::

## Headings

Individual sections can be further structured by using headings.

See also the [example for adding IDs to
headers](/section/02-elements/02-links/01-internal#referencing-elements).

:::info
First-order headings should not be used as they are reserved for the page title.
:::

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
## Second-order heading
### Third-order heading
#### Fourth-order heading
:::

:::tab-item
```markdown
## Second-order heading
### Third-order heading
#### Fourth-order heading
```
:::
::::
:::::

## Lists and Enumerations

Numbered and unnumbered lists can be displayed.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
- A
- B
- C

1. A
1. B
1. C
:::

:::tab-item
```markdown
- A
- B
- C

1. A
1. B
1. C
```
:::
::::

Lists can be nested and combined.

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
- I
   - II
      1. III
      1. III
   - II
- I
   1. II
   1. II
:::

:::tab-item
```markdown
- I
   - II
      1. III
      1. III
   - II
- I
   1. II
   1. II
```
:::
::::
:::::

## Block quotations

By prefixing lines with the character `>` block quotations can be displayed.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
> To be, or not to be: that is the question  
> —William Shakespeare
:::

:::tab-item
```markdown
> To be, or not to be: that is the question  
> —William Shakespeare
```
:::
::::
:::::
