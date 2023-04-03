---
title: 'PGF/TikZ Images'
---

[PGF/Ti*k*Z](https://sourceforge.net/projects/pgf/) is a language to create
vector graphics. It is embedded using code blocks of type `tikz`.

<Info>
  While these images work by itself it is considered good practice to wrap them
  in a figure. You can also add a caption to the figure by prepending a paragraph
  just before the Ti*k*Z code block.

  ````markdown
  <Figure>
    <Caption>Caption</Caption>
    ```tikz
    \begin{tikzpicture}
    […]
    \end{tikzpicture}
    ```
  </Figure>
  ````
</Info>

<Example>
  This code is slightly different for the German version. That way translated
  labels or other language specific features can be realized.

  ````markdown
  ```tikz
  \begin{tikzpicture}
    \shade[left color=blue,right color=red,rounded corners=8pt] (-0.5,-0.5) rectangle (2.5,3.45);
    \draw[white,thick,dashed,rounded corners=8pt] (0,0) -- (0,2) -- (1,3.25)
    -- (2,2) -- (2,0) -- (0,2) -- (2,2) -- (0,0) -- (2,0);
    \node[white] at (1,-0.25) {\footnotesize House of Santa Claus};
  \end{tikzpicture}
  ```
  ````

  <Figure>
    <Caption>Ti*k*Z image with translated content</Caption>
    ```tikz
    \begin{tikzpicture}
      \shade[left color=blue,right color=red,rounded corners=8pt] (-0.5,-0.5) rectangle (2.5,3.45);
      \draw[white,thick,dashed,rounded corners=8pt] (0,0) -- (0,2) -- (1,3.25)
      -- (2,2) -- (2,0) -- (0,2) -- (2,2) -- (0,0) -- (2,0);
      \node[white] at (1,-0.25) {\footnotesize House of Santa Claus};
    \end{tikzpicture}
    ```
  </Figure>
</Example>

<Example>
  Another example shows the usage of $\LaTeX$ formulae inside a picture.

  ````markdown
  ```tikz
  \begin{tikzpicture}
    % coordinate system
    \node (xMAX) at (2.8,0){};
    \node (yMAX) at (0,4.8){};
    \draw[->] (-2.5,0) -- (xMAX);
    \foreach \x in {-2,-1,1,2}
    \draw[shift={(\x,0)}] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
    \draw[->] (0,-0.5) -- (yMAX);
    \foreach \y in {1,2,3,4}
    \draw[shift={(0,\y)}] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
    \draw (0pt,-10pt) node[right] {\footnotesize $0$};
    % axis labels
    \draw (xMAX) node[anchor=north east] {$x$};
    \draw (yMAX) node[anchor=east] {$f(x)$};
    % graph
    \draw[color=blue,smooth,samples=50,domain=-2.1:2.1] plot(\x,{(\x)^(2.0)});
    \draw[color=blue] (2.1,4.41) node[anchor=south] {$f(x)=x^2$};
  \end{tikzpicture}
  ```
  ````

  <Figure>
  ```tikz
  \begin{tikzpicture}
    % coordinate system
    \node (xMAX) at (2.8,0){};
    \node (yMAX) at (0,4.8){};
    \draw[->] (-2.5,0) -- (xMAX);
    \foreach \x in {-2,-1,1,2}
    \draw[shift={(\x,0)}] (0pt,2pt) -- (0pt,-2pt) node[below] {\footnotesize $\x$};
    \draw[->] (0,-0.5) -- (yMAX);
    \foreach \y in {1,2,3,4}
    \draw[shift={(0,\y)}] (2pt,0pt) -- (-2pt,0pt) node[left] {\footnotesize $\y$};
    \draw (0pt,-10pt) node[right] {\footnotesize $0$};
    % axis labels
    \draw (xMAX) node[anchor=north east] {$x$};
    \draw (yMAX) node[anchor=east] {$f(x)$};
    % graph
    \draw[color=blue,smooth,samples=50,domain=-2.1:2.1] plot(\x,{(\x)^(2.0)});
    \draw[color=blue] (2.1,4.41) node[anchor=south] {$f(x)=x^2$};
  \end{tikzpicture}
  ```
  </Figure>
</Example>

## Dark mode

Ti*k*Z images should be easy to read even in dark mode. In particular the
contrast for the relevant elements should not be too low.

A contrast color is available for this, which is light or dark depending on the
mode. This color is also used for regular text. If no color is explicitly
assigned to an element, the contrasting color is automatically selected. This
color can also be selected by using `currentcolor` explicitly.

<Example>
  ````markdown
  ```tikz
  \begin{tikzpicture}
    \fill (0,0) circle (0.5) node[yshift=-22]{\emph{default}};
    \fill[currentcolor] (2,0) circle (0.5) node[yshift=-22]{currentcolor};
    \fill[black] (4,0) circle (0.5) node[yshift=-22]{black};
    \fill[white] (6,0) circle (0.5) node[yshift=-22]{white};
  \end{tikzpicture}
  ```
  ````

  ```tikz
  \begin{tikzpicture}
    \fill (0,0) circle (0.5) node[yshift=-22]{\emph{default}};
    \fill[currentcolor] (2,0) circle (0.5) node[yshift=-22]{currentcolor};
    \fill[black] (4,0) circle (0.5) node[yshift=-22]{black};
    \fill[white] (6,0) circle (0.5) node[yshift=-22]{white};
  \end{tikzpicture}
  ```

  *To see the change, please switch the color mode.*
</Example>

## Overriding the $\LaTeX$ preamble {#tikz_preamble}

PGF/Ti*k*Z is a complex and extensive $\LaTeX$ package. In order to support
specific features it might be necessary to include additional Ti*k*Z libaries.

To do so one must add directives to the preamble of the corresponding $\LaTeX$
document. Add a `tikz_preamble` key to the manifest file.

```yml
# manifest.yml
tikz_preamble: |
  \usetikzlibrary{arrows}
  \newcommand{\sayhello}{Hello\ World!}
```

<Info>
  As this technique allows you to add arbitrary commands to the preamble you can
  use it to define custom $\LaTeX$ commands for convenience.
</Info>

<Example>
  This examples uses the `arrows` library. It allows us to use `diamond` as arrow
  tip kind.

  ````markdown
  ```tikz
  \begin{tikzpicture}
    \node (A) at (0, 0) {A};
    \node (B) at (1, 0) {B};
    \draw[-diamond] (A) -- (B);
  \end{tikzpicture}
  ```
  ````

  <Figure>
  ```tikz
  \begin{tikzpicture}
    \node (A) at (0, 0) {A};
    \node (B) at (1, 0) {B};
    \draw[-diamond] (A) -- (B);
  \end{tikzpicture}
  ```
  </Figure>
</Example>

<Example>
  Here we're using the custom command `\sayhello`.

  ````markdown
  ```tikz
  \begin{tikzpicture}
    \node {$\sayhello$};
  \end{tikzpicture}
  ```
  ````

  <Figure>
    ```tikz
    \begin{tikzpicture}
      \node {$\sayhello$};
    \end{tikzpicture}
    ```
  </Figure>
</Example>
