---
title: Grids
---

A grid is a layout system. It places content into a two-dimensional coordinate
system and allows for flexible arrangements of elements while supporting
different screen sizes. Grids are the method of choice when it comes to align
elements for layout purposes.

The grid has a fixed amount of *12 column slots*. It will always occupy all of
the available width. As many rows as necessary can be added to the grid. Every
row can hold a number of columns. Columns can span several slots. Also they can
be shifted (offset).

:::::::example
In this example a simple grid with three rows is shown. The following drawing
illustrates the grid slots, rows and columns.

::::::figure
Grid schema
```tikz
\begin{tikzpicture}[y=-1cm]
    \def \padding {0.15}
    \newcommand\addrow[5]{ % row, start, width, color, label
        \fill[#4!50,opacity=0.9](#2+\padding,#1+\padding)
            rectangle (#3+#2-\padding,#1+1-\padding)
            node[pos=0.5,color=black] {\texttt{#5}};
    }
    \draw [draw=currentcolor, yshift=10, decorate, decoration={brace, amplitude=10}]
        (0,0) -- (24,0) node [midway,above=10,color=currentcolor] {24 slots};
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

To realize such a grid in Markdown, we add three rows with columns inside. The
colums use the `span` and `offset` attributes.

::::::tabs{labels="Result,Markdown"}

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

## Repsonsive Grid

A grid column can have different span values depending on the screen size. This
way the layout becomes *responsive*, adjusting to different devices, like
desktop computer or mobile phone.

:::info
To see the layout respond to different viewport sizes, try adjusting the size of
your browser window.
:::

:::::::example
In this practical example, a grid layout is used to show an image next to an
explanatory text. This works well on larger screens. On smaller screens,
however, the width is not sufficient to accommodate both elements. Our solution
therefore places the text below the image for small screen sizes.

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
```markdown
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

Instead of using a single `span` attribute per column, different span values can
be used. The boundaries when the layout should switch are called *breakpoints*.

:::table[Viewport breakpoints]
| Name              | Attribute | Viewport width (in pixels) | Device example      |
| ----------------- | --------- | -------------------------- | ------------------- |
| Extra small       | `xs`      | < 600                      | Small mobile phone  |
| Small             | `sm`      | ≥ 600                      | Mobile phone        |
| Medium            | `md`      | ≥ 900                      | Mobile phone/Tablet |
| Large             | `lg`      | ≥ 1200                     | Tablet/Desktop      |
| Extra large       | `xl`      | ≥ 1536                     | Desktop             |
:::

:::::::example
In this example there is one row with three colums. On a large screen the
columns will arrange next to each other occupying one third of the width. On
medium screens the first two columns will take one half each while the last
column will fill an entire row. On very small screens each column fills a row.

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
````markdown
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
