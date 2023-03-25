---
title: Raster
---

Ein Raster ist ein Layout-System. Es platziert Inhalte in ein zweidimensionales
Koordinatensystem und ermöglicht eine flexible Anordnung der Elemente für
verschiedene Bildschirmgrößen. Es ist die Methode der Wahl um Elemente
auszurichten.

Das Raster hat eine feste Anzahl von *12 Spaltenplätzen*. Es nimmt immer die
gesamte verfügbare Breite ein. Es können beliebig viele Zeilen hinzugefügt
werden. Jede Zeile beherbergt eine Anzahl von Spalten. Spalten können sich über
mehrere Spaltenplätze erstrecken. Sie können auch verschoben werden (Offset).

:::::::example
In diesem Beispiel wird ein einfaches Raster mit drei Zeilen erzeugt. Die
folgende Zeichnung veranschaulicht die Spaltenplätze, Zeilen und Spalten.

::::::figure
Rasterschema
```tikz
\begin{tikzpicture}[y=-1cm]
    \def \padding {0.15}
    \newcommand\addrow[5]{ % row, start, width, color, label
        \fill[#4!50,opacity=0.9](#2+\padding,#1+\padding)
            rectangle (#3+#2-\padding,#1+1-\padding)
            node[pos=0.5,color=black] {\texttt{#5}};
    }
    \draw [draw=currentcolor, yshift=10, decorate, decoration={brace, amplitude=10}]
        (0,0) -- (24,0) node [midway,above=10,color=currentcolor] {24 Slots};
    \draw [draw=currentcolor] (0,0) grid (24,3);
    \addrow{0}{0}{24}{green}{span=24};
    \addrow{1}{0}{12}{red}{span=12};
    \addrow{1}{12}{12}{blue}{span=12};
    \addrow{2}{0}{2}{yellow}{span=2};
    \addrow{2}{2}{3}{brown}{span=3};
    \addrow{2}{13}{7}{cyan}{span=7 offset=8};
    \addrow{2}{20}{3}{pink}{span=3};
\end{tikzpicture}
```
::::::

Um dieses Raster in Markdown umzusetzen, fügen wir drei Zeilen mit Spalten
hinzu. Die Spalten verwenden die Attribute `span` und `offset`.

::::::tabs{labels="Ergebnis,Markdown"}

:::::tab-item
::::grid
:::grid-item{xs="12"}
```
xs=12
```
:::

:::grid-item{xs="6"}
```
xs=6
```
:::

:::grid-item{xs="6"}
```
xs=6
```
:::

:::grid-item{xs="2"}
```
xs=2
```
:::

:::grid-item{xs="3"}
```
xs=3
```
:::

:::grid-item{xs="3" xs-offset="1"}
```
xs=3 xs-offset=1
```
:::

:::grid-item{xs="3"}
```
xs=3
```
:::
::::
:::::

:::::tab-item
````markdown
::::grid
:::grid-item{xs="12"}
```
xs=12
```
:::

:::grid-item{xs="6"}
```
xs=6
```
:::

:::grid-item{xs="6"}
```
xs=6
```
:::

:::grid-item{xs="2"}
```
xs=2
```
:::

:::grid-item{xs="3"}
```
xs=3
```
:::

:::grid-item{xs="3" xs-offset="1"}
```
xs=3 xs-offset=1
```
:::

:::grid-item{xs="3"}
```
xs=3
```
:::
::::
````
:::::

::::::

:::::::

## Repsonsives Raster

Die Anzahl an Spaltenplätze können abhängig von der Bildschirmgröße gesetzt
werden. Dadurch wird das Layout *responsiv*, d.h. es passt sich verschiedenen
Ausgabegeräten wie Smartphone oder Desktop-Computer an.

:::info
Um zu sehen, wie das Layout auf verschiedene Größen reagiert, kann die Größe des
Browserfensters verändert werden.
:::

:::::::example
In diesem praktischen Beispiel wird ein Raster verwendet, um ein Bild
neben einem erläuternden Text anzuzeigen. Dies funktioniert gut auf größeren
Bildschirmen. Auf kleineren Bildschirmen reicht die Breite jedoch nicht aus, um
beide Elemente unterzubringen. Unsere Lösung platziert daher bei kleinen
Bildschirmen den Text unterhalb des Bildes.

::::::tabs{labels="Result,Markdown"}

:::::tab-item
::::grid
:::grid-item{xs="12" md="8"}
![Lake side](lake-side.jpg "Lake side"){.img}
:::

:::grid-item{xs="12" md="4"}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fringilla tempus
mollis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
inceptos himenaeos. Ut vitae sodales mi. Nulla dolor dui, faucibus non mi et,
fringilla porta massa. In posuere, elit ut congue tempor, erat enim ultricies
ipsum.
:::
::::
:::::

:::::tab-item
```
::::grid
:::grid-item{xs="12" md="8"}
![Lake side](lake-side.jpg "Lake side"){.img}
:::

:::grid-item{xs="12" md="4"}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed fringilla tempus
mollis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per
inceptos himenaeos. Ut vitae sodales mi. Nulla dolor dui, faucibus non mi et,
fringilla porta massa. In posuere, elit ut congue tempor, erat enim ultricies
ipsum.
:::
::::
```
:::::

::::::

:::::::

Anstatt ein einzelnes `span`-Attribut pro Spalte zu verwenden, können
verschiedene Werte angegeben werden. Die Grenzen, an denen das Layout wechseln
soll, werden als *Breakpoints* bezeichnet.

| Name              | Attribut  | Breite (in Pixel) | Beispielgerät      |
| ----------------- | --------- | ----------------- | ------------------ |
| Extra klein       | `xs`      | < 600             | Kleines Smartphone |
| Klein             | `sm`      | ≥ 600             | Smartphone         |
| Medium            | `md`      | ≥ 900             | Smartphone/Tablet  |
| Groß              | `lg`      | ≥ 1200            | Tablet/Desktop     |
| Extra groß        | `xl`      | ≥ 1536            | Desktop            |

: Breakpoints

:::::::example
Dieses Beispiel enthält eine Zeile mit drei Spalten. Auf einem großen Bildschirm
werden die Spalten nebeneinander angeordnet und nehmen je ein Drittel der Breite
ein. Auf einem mittleren Bildschirm nehmen die ersten beiden Spalten jeweils die
Hälfte ein, während die letzte Spalte eine ganze Zeile ausfüllt. Auf sehr
kleinen Bildschirmen füllt jede Spalte eine Zeile aus.

::::::tabs{labels="Result,Markdown"}

:::::tab-item
::::grid
:::grid-item{xs="12" md="6" lg="4"}
```
xs=12 md=6 lg=4
```
:::

:::grid-item{xs="12" md="6" lg="4"}
```
xs=12 md=6 lg=4
```
:::

:::grid-item{xs="12" md="12" lg="4"}
```
xs=12 md=12 lg=4
```
:::
::::
:::::

:::::tab-item
````
::::grid
:::grid-item{xs="12" md="6" lg="4"}
```
xs=12 md=6 lg=4
```
:::

:::grid-item{xs="12" md="6" lg="4"}
```
xs=12 md=6 lg=4
```
:::

:::grid-item{xs="12" md="12" lg="4"}
```
xs=12 md=12 lg=4
```
:::
::::
````
:::::

::::::

:::::::
