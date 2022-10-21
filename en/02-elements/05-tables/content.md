---
title: Tables
---

This section describes the different ways to create tables. Further details on
the topic can be found in the [Pandoc
documentation](https://pandoc.org/MANUAL.html#tables).

::: {.info}
Besides text, tables can contain images, exercises and all other elements.
However, for creating layout, e.g. to arrange elements next to each other, the
use of [grids](/section/02-elements/06-grids) is recommended. Unlike tables,
grids adapt to different screen sizes.
:::

## Table caption

Each table can optionally have a caption. For this purpose, a line with the
content `Table: [Caption text]` is inserted below the table. Alternatively this
can be shortened to `: [Caption text]`.

::: {.example}
**Markdown**

```markdown
A   B   C
--- --- --
11  21  31

Table: Simple table with caption
```

**Result**

A   B   C
--- --- --
11  21  31

Table: Simple table with caption
:::

## Table types

There are four different kinds of tables. They differ in the way to write them
down but also in their functionality.

- [Simple](#simple)
- [Multiline](#multiline)
- [Grid](#grid)
- [Pipe](#pipe)

### Simple {#simple}

Simple tables consist of a header row and the cell contents. The alignment of
the contents can be influenced. The header line can also be omitted completely.
However, the table must then be closed with a line of hyphens.

::: {.example}
**Markdown**

```markdown
   Align center   Default   Right Left
----------------- ------- ------- ---------------------------------------------
        11             21      31 Line breaks within a cell are not possible.
        12             22      32 42

: Simple table with header row
```

**Result**

   Align center   Default   Right Left
----------------- ------- ------- ---------------------------------------------
        11             21      31 Line breaks within a cell are not possible.
        12             22      32 42

: Simple table with header row

**Markdown**

```markdown
------ -- ---- ---------------------------------------------
  11   21   31 Line breaks within a cell are not possible.
  12   22   32 42
------ -- ---- ---------------------------------------------

: Simple table without header row
```

**Result**

------ -- ---- ---------------------------------------------
  11   21   31 Line breaks within a cell are not possible.
  12   22   32 42
------ -- ---- ---------------------------------------------

: Simple table without header row
:::

### Multiline {#multiline}

Multiline tables can be used for better readability. Here you can wrap text
within a cell. In the display, the text wrap depends on the available width.

Multiline tables are similar to simple tables, but must be enclosed by a line
of dashes and a blank line.

::: {.example}
**Markdown**

```markdown
--------------------------------------------------
  Align    Default    Right Left
  center
---------- ------- -------- ----------------------
    11     21            31 Line breaks within\
                            a cell are possible.

    12     22            32 42
--------------------------------------------------

: Multiline table with header row
```

**Result**

--------------------------------------------------
  Align    Default    Right Left
  center
---------- ------- -------- ----------------------
    11     21            31 Line breaks within\
                            a cell are possible.

    12     22            32 42
--------------------------------------------------

: Multiline table with header row

**Markdown**

```markdown
-------- ----- ----- ----------------------
   11    21       31 Line breaks within\
                     a cell are possible.

   12    22       32 42
-------- ----- ----- ----------------------

: Multiline table without header row
```

**Result**

-------- ----- ----- ----------------------
   11    21       31 Line breaks within\
                     a cell are possible.

   12    22       32 42
-------- ----- ----- ----------------------

: Multiline table without header row
:::


### Grid {#grid}

Grid tables are another way of writing tables. They allow the arbitrary use
of block elements, such as several paragraphs, lists, etc., within a cell.

The table is created with a combination of the symbols `-`, `+`, `|`, `=` and
`:`. The header is separated from the other rows by using a dashed line. The
colon can be used to change the column alignment.

::: {.example}
**Markdown**

```markdown
+--------+---------+-------+----------------------------+
| Align  | Default | Right | Left                       |
| center |         |       |                            |
+:======:+=========+======:+:===========================+
| 11     | 21      | 31    | Line breaks within\        |
|        |         |       | a cell are possible.       |
+--------+---------+-------+----------------------------+
| 12     | 22      | 32    | - Arbitrary block elements |
|        |         |       | - are possible.            |
+--------+---------+-------+----------------------------+

: Grid table with header row
```

**Result**

+--------+---------+-------+----------------------------+
| Align  | Default | Right | Left                       |
| center |         |       |                            |
+:======:+=========+======:+:===========================+
| 11     | 21      | 31    | Line breaks within\        |
|        |         |       | a cell are possible.       |
+--------+---------+-------+----------------------------+
| 12     | 22      | 32    | - Arbitrary block elements |
|        |         |       | - are possible.            |
+--------+---------+-------+----------------------------+

: Grid table with header row

**Markdown**

```markdown
+:------:+---------+------:+:---------------------------+
| 11     | 21      | 31    | Line breaks within\        |
|        |         |       | a cell are possible.       |
+--------+---------+-------+----------------------------+
| 12     | 22      | 32    | - Arbitrary block elements |
|        |         |       | - are possible.            |
+--------+---------+-------+----------------------------+

: Grid table without header row
```

**Result**

+:------:+---------+------:+:---------------------------+
| 11     | 21      | 31    | Line breaks within\        |
|        |         |       | a cell are possible.       |
+--------+---------+-------+----------------------------+
| 12     | 22      | 32    | - Arbitrary block elements |
|        |         |       | - are possible.            |
+--------+---------+-------+----------------------------+

: Grid table without header row
:::

### Pipe {#pipe}

Another way to format tables is to use pipe tables. They are created with the
help of the pipe symbol `|`.

Pipe tables do not allow multiline cells or block elements. They use the colon
symbol to specify the alignment. Columns do not need to be vertically aligned.

::: {.example}
**Markdown**

```markdown
| Align center | Default | Right | Left                                        |
|:------------:|---------|------:|:--------------------------------------------|
| 11           | 21      | 31    | Line breaks within a cell are not possible. |
| 12           | 22      | 32    | 42                                          |

: Pipe table with vertical alignment
```

**Result**

| Align center | Default | Right | Left                                        |
|:------------:|---------|------:|:--------------------------------------------|
| 11           | 21      | 31    | Line breaks within a cell are not possible. |
| 12           | 22      | 32    | 42                                          |

: Pipe table with vertical alignment

**Markdown**

```markdown
|Align center|Default|Right|Left|
:--:|--|--:|:--|
|11|21|31|Line breaks within a cell are not possible.|
|12|22|32|42|

: Pipe table without vertical alignment
```

**Result**

|Align center|Default|Right|Left|
:--:|--|--:|:--|
|11|21|31|Line breaks within a cell are not possible.|
|12|22|32|42|

: Pipe table without vertical alignment
:::
