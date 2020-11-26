---
title: Raster
---

Ein Raster ist ein Layout-System. Es platziert Inhalte in ein zweidimensionales
Koordinatensystem und ermöglicht eine flexible Anordnung der Elemente für
verschiedene Bildschirmgrößen. Es ist die Methode der Wahl um Elemente
auszurichten.

Das Raster hat eine feste Anzahl von *24 Spaltenplätzen*. Es nimmt immer die
gesamte verfügbare Breite ein. Es können beliebig viele Zeilen hinzugefügt
werden. Jede Zeile beherbergt eine Anzahl von Spalten. Spalten können sich über
mehrere Spaltenplätze erstrecken. Sie können auch verschoben werden (Offset).

::: {.example}
In diesem Beispiel wird ein einfaches Raster mit drei Zeilen erzeugt. Die
folgende Zeichnung veranschaulicht die Spaltenplätze, Zeilen und Spalten.

::: {.figure}
Grid schema
```tikz
\begin{tikzpicture}[y=-1cm]
    \def \padding {0.15}
    \newcommand\addrow[5]{ % row, start, width, color, label
        \fill[#4!50,opacity=0.9](#2+\padding,#1+\padding)
            rectangle (#3+#2-\padding,#1+1-\padding)
            node[pos=0.5,color=black] {\texttt{#5}};
    }
    \draw [yshift=10, decorate, decoration={brace, amplitude=10}]
        (0,0) -- (24,0) node [black,midway,above=10] {24 slots};
    \draw (0,0) grid (24,3);
    \addrow{0}{0}{24}{green}{span=24};
    \addrow{1}{0}{12}{red}{span=12};
    \addrow{1}{12}{12}{blue}{span=12};
    \addrow{2}{0}{2}{yellow}{span=2};
    \addrow{2}{2}{3}{brown}{span=3};
    \addrow{2}{13}{7}{cyan}{span=7 offset=8};
    \addrow{2}{20}{3}{pink}{span=3};
\end{tikzpicture}
```
:::

**Markdown**

Um dieses Raster in Markdown umzusetzen, fügen wir drei Zeilen mit Spalten
hinzu. Die Spalten verwenden die Attribute `span` und `offset`.

```markdown
::: {.row}
:::: {.col span="24"}
`span=24`
::::
:::

::: {.row}
:::: {.col span="12"}
`span=12`
::::
:::: {.col span="12"}
`span=12`
::::
:::

::: {.row}
:::: {.col span="2"}
`span=2`
::::
:::: {.col span="3"}
`span=3`
::::
:::: {.col span="7" offset="8"}
`span=7 offset=8`
::::
:::: {.col span="3"}
`span=3`
::::
:::
```

**Ergebnis**

::: {.row}
:::: {.col span="24"}
`span=24`
::::
:::

::: {.row}
:::: {.col span="12"}
`span=12`
::::
:::: {.col span="12"}
`span=12`
::::
:::

::: {.row}
:::: {.col span="2"}
`span=2`
::::
:::: {.col span="3"}
`span=3`
::::
:::: {.col span="7" offset="8"}
`span=7 offset=8`
::::
:::: {.col span="3"}
`span=3`
::::
:::
:::

## Repsonsives Raster

Die Anzahl an Spaltenplätze können abhängig von der Bildschirmgröße gesetzt
werden. Dadurch wird das Layout *responsiv*, d.h. es passt sich verschiedenen
Ausgabegeräten wie Smartphone oder Desktop-Computer an.

::: {.example}
In diesem praktischen Beispiel wird ein Raster verwendet, um ein Bild
neben einem erläuternden Text anzuzeigen. Dies funktioniert gut auf größeren
Bildschirmen. Auf kleineren Bildschirmen reicht die Breite jedoch nicht aus, um
beide Elemente unterzubringen. Unsere Lösung platziert daher bei kleinen
Bildschirmen den Text unterhalb des Bildes.

**Markdown**

```markdown
::: {.row}
:::: {.col xs="24" md="16"}
![Lake side](lake-side.jpg "Lake side"){.img}
::::
:::: {.col xs="24" md="8"}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fringilla tempus
mollis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
inceptos himenaeos. Ut vitae sodales mi. Nulla dolor dui, faucibus non mi et,
fringilla porta massa. In posuere, elit ut congue tempor, erat enim ultricies
ipsum.
::::
:::
```

**Ergebnis**

::: {.row}
:::: {.col xs="24" md="16"}
![Lake side](lake-side.jpg "Lake side"){.img}
::::
:::: {.col xs="24" md="8"}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fringilla tempus
mollis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
inceptos himenaeos. Ut vitae sodales mi. Nulla dolor dui, faucibus non mi et,
fringilla porta massa. In posuere, elit ut congue tempor, erat enim ultricies
ipsum.
::::
:::
:::

::: {.info}
Um zu sehen, wie das Layout auf verschiedene Größen reagiert, kann die Größe des
Browserfensters verändert werden.
:::

Anstatt ein einzelnes `span`-Attribut pro Spalte zu verwenden, können
verschiedene Werte angegeben werden. Die Grenzen, an denen das Layout wechseln
soll, werden als *Breakpoints* bezeichnet.

Name             Attribut Breite (in Pixel) Beispielgerät
---------------- -------- ----------------- ------------------
Extra klein      `xs`     < 576             Kleines Smartphone
Klein            `sm`     ≥ 576             Smartphone
Medium           `md`     ≥ 768             Smartphone/Tablet
Groß             `lg`     ≥ 992             Tablet/Desktop
Extra groß       `xl`     ≥ 1200            Desktop
Extra extra groß `xxl`    ≥ 1600            Großer Desktop

: Breakpoints

::: {.example}
Dieses Beispiel enthält eine Zeile mit drei Spalten. Auf einem großen Bildschirm
werden die Spalten nebeneinander angeordnet und nehmen je ein Drittel der Breite
ein. Auf einem mittleren Bildschirm nehmen die ersten beiden Spalten jeweils die
Hälfte ein, während die letzte Spalte eine ganze Zeile ausfüllt. Auf sehr
kleinen Bildschirmen füllt jede Spalte eine Zeile aus.

**Markdown**

```markdown
::: {.row}
:::: {.col xs="24" md="12" lg="8"}
Column `xs=24 md=12 lg=8`
::::
:::: {.col xs="24" md="12" lg="8"}
Column `xs=24 md=12 lg=8`
::::
:::: {.col xs="24" md="24" lg="8"}
Column `xs=24 md=12 lg=8`
::::
:::
```

**Ergebnis**

::: {.row}
:::: {.col xs="24" md="12" lg="8"}
Column `xs=24 md=12 lg=8`
::::
:::: {.col xs="24" md="12" lg="8"}
Column `xs=24 md=12 lg=8`
::::
:::: {.col xs="24" md="24" lg="8"}
Column `xs=24 md=12 lg=8`
::::
:::
:::
