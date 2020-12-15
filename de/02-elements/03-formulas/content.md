---
title: Formeldarstellung
---

Im Text können $\LaTeX$-Formeln verwendet werden. Sie werden durch die Software
[MathJax](https://www.mathjax.org/) dargestellt.

## Verwendung

Um Formeln auszuzeichnen wird das `$`-Zeichen verwendet. Sie können entweder
direkt im Fließtext (einfaches `$`) oder freistehend (doppeltes `$`)
dargestellt werden.

::: {.example}
**Markdown**

```markdown
Formeln, wie $\sum_{n=1}^{\infty} 2^{-n} = 1$ können direkt im Fließtext
stehen.

Sie können aber auch freistehend verwendet werden:

$$\sum_{n=1}^{\infty} 2^{-n} = 1$$
```

**Result**

Formeln, wie $\sum_{n=1}^{\infty} 2^{-n} = 1$ können direkt im Fließtext
stehen.

Sie können aber auch freistehend verwendet werden:

$$\sum_{n=1}^{\infty} 2^{-n} = 1$$
:::

::: {.example}
Ein weiteres, komplizierteres Beispiel mit `align`-Umgebung.

**Markdown**

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

**Result**

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

## Spezielle Erweiterungen

Manchmal ist es wünschenswert eigene Makros und Befehle zu definieren, um die
Funktionalität von MathJax zu erweitern. Die Details werden in diesem Dokument
nicht besprochen. An dieser Stelle wird auf die
[MathJax-Dokumentation](https://docs.mathjax.org/en/latest/advanced/extensions.html)
verwiesen.

Um Erweiterungen hinzuzufügen, wird das Kurs-Manifest angepasst. In Abschnitt
[](/section/01-project/02-files/01-manifest#mathjax) findet sich ein Beispiel.

::: {.info #innodoc-mathjax}
Es existieren die Erweiterungen
[**\@innodoc/mathjax-num**](https://gitlab.tu-berlin.de/innodoc/mathjax-num)
und
[**\@innodoc/mathjax-coordsep**](https://gitlab.tu-berlin.de/innodoc/mathjax-coordsep).

Sie implementieren einen lokalisierten Dezimalseparator
(`$\num{3.45}$` → $\num{3.45}$) und einen anpassbaren Trenner für Koordinaten
(`$(6\coordsep 5)$` → $(6\coordsep 5)$).
:::
