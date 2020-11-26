---
title: Grids
---

A grid is a layout system. It places content into a two-dimensional coordinate
system and allows for flexible arrangements of elements while supporting
different screen sizes. Grids are the method of choice when it comes to align
elements for layout purposes.

The grid has a fixed amount of *24 column slots*. It will always occupy all of
the available width. As many rows as necessary can be added to the grid. Every
row can hold a number of columns. Columns can span several slots. Also they can
be shifted (offset).

::: {.example}
In this example a simple grid with three rows is shown. The following drawing
illustrates the grid slots, rows and columns.

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

To realize such a grid in Markdown, we add three rows with columns inside. The
colums use the `span` and `offset` attributes.

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

**Result**

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

## Repsonsive Grid

A grid column can have different span values depending on the screen size. This
way the layout becomes *responsive*, adjusting to different devices, like
desktop computer or mobile phone.

::: {.example}
In this practical example, a grid layout is used to show an image next to an
explanatory text. This works well on larger screens. On smaller screens,
however, the width is not sufficient to accommodate both elements. Our solution
therefore places the text below the image for small screen sizes.

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

**Result**

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
To see the layout respond to different viewport sizes, try adjusting the size of
your browser window.
:::

Instead of using a single `span` attribute per column, different span values can
be used. The boundaries when the layout should switch are called *breakpoints*.

Name              Attribute Viewport width (in pixels) Device example
----------------- --------- -------------------------- ------------------
Extra small       `xs`      < 576                      Small mobile phone
Small             `sm`      ≥ 576                      Mobile phone
Medium            `md`      ≥ 768                      Mobile phone/Tablet
Large             `lg`      ≥ 992                      Tablet/Desktop
Extra large       `xl`      ≥ 1200                     Desktop
Extra extra large `xxl`     ≥ 1600                     Large desktop

: Viewport breakpoints

::: {.example}
In this example there is one row with three colums. On a large screen the
columns will arrange next to each other occupying one third of the width. On
medium screens the first two columns will take one half each while the last
column will fill an entire row. On very small screens each column fills a row.

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

**Result**

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
