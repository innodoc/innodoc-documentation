---
title: 'TikZ Bilder'
---

Beispielbild:

```tikz
\begin{tikzpicture}[x=1.0cm, y=1.0cm]
\draw[thick, black] (-5.2,0) -- (6.2,0);
\foreach \x in {-5, -4, ..., 6}
\draw[shift={(\x,0)},color=black] (0pt,6pt) -- (0pt,-6pt) node[below=1.5pt] {\normalsize $\x$};
\end{tikzpicture}
```
