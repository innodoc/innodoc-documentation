---
title: Tables
---

Tables do not allow for multi-line cells or block-level elements. They use the
colon symbol to specify alignment.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item{index="1"}
| Zentrierte Kopfzeile | Standard | Rechtsbündig | Linksbündig |
|:--------------------:|----------|-------------:|:------------|
| 11                   | 21       | 31           | 32          |
| 12                   | 22       | 32           | 42          |
:::

:::tab-item{index="2"}
```markdown
| Zentrierte Kopfzeile | Standard | Rechtsbündig | Linksbündig |
|:--------------------:|----------|-------------:|:------------|
| 11                   | 21       | 31           | 32          |
| 12                   | 22       | 32           | 42          |
```
:::
::::
:::::

:::info
Tables are suitable for displaying tabular data. However, for layout tasks, such
as arranging elements side by side, the use of a
[grid](/section/02-elements/06-grids) is recommended. Unlike tables, grids adapt
to different screen sizes.
:::

## `table` directive

Usually, tables are enclosed with a table directive. This visually sets them
apart from the background and allows them to have an `id` for linking purposes
as well as a caption.

::::::example
:::::tabs{labels="Result,Markdown"}
::::tab-item{index="1"}
:::table[Simple table with caption]{#example-table}
| A  | B   | C  |
|----|-----|----|
| 11 | 21  | 31 |
:::
::::

::::tab-item{index="2"}
```markdown
:::table[Simple table with caption]{#example-table}
| A  | B   | C  |
|----|-----|----|
| 11 | 21  | 31 |
:::
```
::::
:::::
::::::
