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

:::example
**Markdown**

```markdown
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
```

**Result**

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.

**Markdown**

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

**Result**

Lorem ipsum
dolor sit amet,
consectetur adipiscing elit.

Lorem ipsum  
dolor sit amet,  
consectetur adipiscing elit.
:::

## Text Formatting

This section demonstrates the possibilities of basic text formatting.

:::example
**Markdown**

```markdown
It is possible to highlight *important words*. There are _two ways_ to
accomplish this.
```

**Result**

It is possible to highlight *important words*. There are _two ways_ to
accomplish this.

**Markdown**

```markdown
Even more **important words** are printed in bold. For this there are also two
__different ways__.
```

**Result**

Even more **important words** are printed in bold. For this there are also two
__different ways__.

**Markdown**

```markdown
Another formatting option is crossing out ~~words~~ or ~~whole phrases~~.
```

**Result**

Another formatting option is crossing out ~~words~~ or ~~whole phrases~~.

**Markdown**

```markdown
The formatting options can of course be combined. For example, *in an important
part of a sentence you can cross out ~~words~~*.
```

**Result**

The formatting options can of course be combined. For example, *in an important
part of a sentence you can cross out ~~words~~*.

**Markdown**

```markdown
If a formatting character is to be printed, it must be prefixed with a
\*Backslash\*.
```

**Result**

If a formatting character is to be printed, it must be prefixed with a
\*Backslash\*.
:::

## Headings

Individual sections can be further structured by using headings.

See also the [example for adding IDs to
headers](/section/02-elements/02-links/01-internal#heading-example).

:::info
First-order headings should not be used as they are reserved for the page title.
:::

:::example
**Markdown**

```markdown
## Second-order heading
### Third-order heading
#### Fourth-order heading
```

**Result**

## Second-order heading
### Third-order heading
#### Fourth-order heading
:::

## Lists and Enumerations

Numbered and unnumbered lists can be displayed.

:::example
**Markdown**

```markdown
- A
- B
- C

1. A
1. B
1. C
```

**Result**

- A
- B
- C

1. A
2. B
3. C

Lists can be nested and combined.

**Markdown**

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

**Result**

- I
   - II
      1. III
      1. III
   - II
- I
   1. II
   1. II
:::

## Block quotations

By prefixing lines with the character `>` block quotations can be displayed.

:::example
**Markdown**

```markdown
> I would like to die on Mars. Just not on impact.  
> *Elon Musk*
```

**Result**

> I would like to die on Mars. Just not on impact.  
> *Elon Musk*
:::
