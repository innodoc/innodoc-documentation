---
title: Index
---

For every course an index is automatically generated if at least on entry was
specified.

To create an entry in the index a position in the text needs to be marked.

<Example>
  ```markdown
  This sentence contains an entry for the [index]{data-index-term="index"}.
  ```

  This sentence contains an entry for the [index]{data-index-term="index"}.
</Example>

The entry itself is not recognizable in the text. The word or phrase needs to
be appended with an attribute `data-index-term`. The value of this attribute is
the term as it appears in the index. Naturally any number of references can
exist for a single index term.

<Info>
  You can also use $\LaTeX$ inside the index term.

  ```markdown
  [$\LaTeX$ formula]{data-index-term="$\LaTeX$ formula"}
  ```

  [$\LaTeX$ formula]{data-index-term="$\LaTeX$ formula"}
</Info>
