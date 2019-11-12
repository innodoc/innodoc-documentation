---
title: Formulas
---

It is possible to use $\LaTeX$ formulas. They are rendered using the
[MathJax library](https://www.mathjax.org/).

## Basic usage

Formulas use the `$` sign as delimiter. They can be displayed inline (single
`$`) or as a block (double `$`).

```markdown
Formulas like $\sum_{n=1}^{\infty} 2^{-n} = 1$ can be inlined into text.

Or they can stand alone as a block element:

$$\sum_{n=1}^{\infty} 2^{-n} = 1$$
```

Formulas like $\sum_{n=1}^{\infty} 2^{-n} = 1$ can be inlined into text.

Or they can stand alone as a block element:

$$\sum_{n=1}^{\infty} 2^{-n} = 1$$

::: {.example}
Another more complicated example using an `align` environment.

```markdown
$$
\begin{align*}
  \sum_{i=1}^{k+1}i & = \left(\sum_{i=1}^{k}i\right) + (k+1) \\
  & = \frac{k(k+1)}{2}+k+1 & (\text{by inductive hypothesis}) \\
  & = \frac{k(k+1)+2(k+1)}{2} \\
  & = \frac{(k+1)(k+2)}{2} \\
  & = \frac{(k+1)((k+1)+1)}{2}
\end{align*}
$$
```

$$
\begin{align*}
  \sum_{i=1}^{k+1}i & = \left(\sum_{i=1}^{k}i\right) + (k+1) \\
  & = \frac{k(k+1)}{2}+k+1 & (\text{by inductive hypothesis}) \\
  & = \frac{k(k+1)+2(k+1)}{2} \\
  & = \frac{(k+1)(k+2)}{2} \\
  & = \frac{(k+1)((k+1)+1)}{2}
\end{align*}
$$
:::

## Using custom extensions

Sometimes it is desirable to use custom macros that add functionality. Writing
extensions for MathJax is out of scope for this document. Please refer to the
[MathJax documentation](https://docs.mathjax.org/en/latest/advanced/extensions.html)
to learn about this topic.

The course manifest lets you override parts of the MathJax configuration to add
custom extensions to the mix. Please refer to the section
[](/section/01-project/02-files/01-manifest#mathjax) for an example.

::: {.info #innodoc-mathjax}
There is an extension called **innodoc-mathjax**. It implements a localized
decimal separator (`$\num{3.45}$` → $\num{3.45}$) and a customizable
coordinates seperator (`$(6\coordsep 5)$` → $(6\coordsep 5)$). The source code
repository is
[publicly available](https://gitlab.tu-berlin.de/innodoc/innodoc-mathjax).
:::
