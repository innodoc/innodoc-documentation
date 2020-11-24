---
title: 'PGF/TikZ-Bilder'
---

Die Sprache [PGF/Ti*k*Z](https://sourceforge.net/projects/pgf/) kann benutzt
werden um Vektorgrafiken zu erstellen. Dafür wird ein Codeblock vom Typ `tikz`
verwendet.

::: {.info}
Ti*k*Z-Bilder können problemlos für sich alleine stehen, allerdings ist es
empfehlenswert diese innerhalb in einer Abbildung zu verwenden. So kann
optional auch ein Bilduntertitel angefügt werden, indem ein Paragraph direkt
vor dem Codeblock hinzugefügt wird.

````markdown
::: {.figure}
Untertitel
```tikz
\begin{tikzpicture}
[…]
\end{tikzpicture}
```
:::
````
:::

::: {.example}
Der folgende Code ist für die Englische Version leicht abgewandelt. So können
Beschriftungen übersetzt und andere sprachspezifische Unterschiede realisiert
werden.

````markdown
```tikz
\begin{tikzpicture}
\shade[left color=blue,right color=red,rounded corners=8pt] (-0.5,-0.5) rectangle (2.5,3.45);
\draw[white,thick,dashed,rounded corners=8pt] (0,0) -- (0,2) -- (1,3.25)
 -- (2,2) -- (2,0) -- (0,2) -- (2,2) -- (0,0) -- (2,0);
\node[white] at (1,-0.25) {\footnotesize Haus vom Nikolaus};
\end{tikzpicture}
```
````

::: {.figure}
Beispiel eines Ti*k*Z-Bildes mit übersetztem Inhalt.
```tikz
\begin{tikzpicture}
\shade[left color=blue,right color=red,rounded corners=8pt] (-0.5,-0.5) rectangle (2.5,3.45);
\draw[white,thick,dashed,rounded corners=8pt] (0,0) -- (0,2) -- (1,3.25)
 -- (2,2) -- (2,0) -- (0,2) -- (2,2) -- (0,0) -- (2,0);
\node[white] at (1,-0.25) {\footnotesize Haus vom Nikolaus};
\end{tikzpicture}
```
:::
:::

::: {.example}
Ein weiteres Beispiel zeigt die Verwendung von $\LaTeX$-Formeln innerhalb
eines Ti*k*Z-Bildes.

````markdown
```tikz
\begin{tikzpicture}
% coordinate system
\node (xMAX) at (2.8,0){};
\node (yMAX) at (0,4.8){};
\draw[->,color=black] (-2.5,0) -- (xMAX);
\foreach \x in {-2,-1,1,2}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
\draw[->,color=black] (0,-0.5) -- (yMAX);
\foreach \y in {1,2,3,4}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
% axis labels
\draw (xMAX) node[anchor=north east] {$x$};
\draw (yMAX) node[anchor=east] {$f(x)$};
% graph
\draw[color=blue,smooth,samples=50,domain=-2.1:2.1] plot(\x,{(\x)^(2.0)});
\draw[color=blue] (2.1,4.41) node[anchor=south] {$f(x)=x^2$};
\end{tikzpicture}
```
````

::: {.figure}
```tikz
\begin{tikzpicture}
% coordinate system
\node (xMAX) at (2.8,0){};
\node (yMAX) at (0,4.8){};
\draw[->,color=black] (-2.5,0) -- (xMAX);
\foreach \x in {-2,-1,1,2}
\draw[shift={(\x,0)},color=black] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
\draw[->,color=black] (0,-0.5) -- (yMAX);
\foreach \y in {1,2,3,4}
\draw[shift={(0,\y)},color=black] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
\draw[color=black] (0pt,-10pt) node[right] {\footnotesize $0$};
% axis labels
\draw (xMAX) node[anchor=north east] {$x$};
\draw (yMAX) node[anchor=east] {$f(x)$};
% graph
\draw[color=blue,smooth,samples=50,domain=-2.1:2.1] plot(\x,{(\x)^(2.0)});
\draw[color=blue] (2.1,4.41) node[anchor=south] {$f(x)=x^2$};
\end{tikzpicture}
```
:::
:::

## Die $\LaTeX$-Präembel anpassen {#tikz_preamble}

PGF/Ti*k*Z ist ein äußerst umfangreiches $\LaTeX$-Paket. Um bestimmte
Funktionen zu nutzen, müssen zusätzliche Ti*k*Z-Bibliotheken eingebunden
werden.

Dafür werden Kommandos in der Präembel des $\LaTeX$-Dokumentes eingefügt. Das
ist möglich, indem man den Wert von `tikz_preamble` in der Manifest-Datei des
Kurses setzt.

```yml
# manifest.yml
tikz_preamble: |
  \usetikzlibrary{arrows}
  \newcommand{\sayhello}{Hello\ World!}
```

::: {.info}
Diese Technik erlaubt es beliebige Kommandos in die Präembel einzufügen. So
können beispielsweise eigene $\LaTeX$-Befehle definiert werden.
:::

::: {.example}
Das folgende Beispiel nutzt die `arrows`-Bibliothek. So können wir nun
`diamond` als spezielle Pfeilspitze verwenden.

````markdown
```tikz
\begin{tikzpicture}
\node (A) at (0, 0) {A};
\node (B) at (1, 0) {B};
\draw[-diamond,black] (A) -- (B);
\end{tikzpicture}
```
````

::: {.figure}
```tikz
\begin{tikzpicture}
\node (A) at (0, 0) {A};
\node (B) at (1, 0) {B};
\draw[-diamond,black] (A) -- (B);
\end{tikzpicture}
```
:::
:::

::: {.example}
In diesem Beispiel greifen wir auf das selbst erstellte Makro `\sayhello`
zurück.

````markdown
```tikz
\begin{tikzpicture}
\node {$\sayhello$};
\end{tikzpicture}
```
````

::: {.figure}
```tikz
\begin{tikzpicture}
\node {$\sayhello$};
\end{tikzpicture}
```
:::
:::
