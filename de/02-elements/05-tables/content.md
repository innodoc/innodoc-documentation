---
title: Tabellen
---

Tabellen erlauben keine mehrzeiligen Zellen oder Blockelemente. Sie verwenden
das Doppelpunktsymbol, um die Ausrichtung festzulegen.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
| Zentrierte Kopfzeile | Standard | Rechtsbündig | Linksbündig |
|:--------------------:|----------|-------------:|:------------|
| 11                   | 21       | 31           | 32          |
| 12                   | 22       | 32           | 42          |
:::

:::tab-item
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
Tabellen eignen sich zur Darstellung von tabellarischen Daten. Für
Layoutaufgaben, also um beispielsweise Elemente nebeneinander anzuordnen, wird
allerdings der Einsatz eines [Rasters](/section/02-elements/06-grids) empfohlen.
Im Gegensatz zu Tabellen passen sich Raster an unterschiedliche Bildschirmgrößen
an.
:::

## `table`-Direktive

In der Regel werden Tabellen mit einer `table`-Direktive umschlossen. Dadurch
werden sie optisch vom Hintergrund abgesetzt, können eine `id` zum Verlinken
sowie eine Beschriftung erhalten.

::::::example
:::::tabs{labels="Ergebnis,Markdown"}
::::tab-item
:::table[Einfache Tabelle mit Beschriftung]{#example-table}
| A  | B   | C  |
|----|-----|----|
| 11 | 21  | 31 |
:::
::::

::::tab-item
```markdown
:::table[Einfache Tabelle mit Beschriftung]{#example-table}
| A  | B   | C  |
|----|-----|----|
| 11 | 21  | 31 |
:::
```
::::
:::::
::::::
