---
title: Tabellen
---

Dieser Abschnitt beschreibt die verschiedenen Arten Tabellen zu erstellen.
Weitere Details zum Thema sind der
[Pandoc-Dokumentation](https://pandoc.org/MANUAL.html#tables) zu entnehmen.

:::info
Tabellen neben Text auch Bilder, Aufgaben und alle anderen Elemente enthalten.
Für Layoutaufgaben, also um beispielsweise Elemente nebeneinander anzuordnen,
wird allerdings der Einsatz eines [Rasters](/section/02-elements/06-grids)
empfohlen. Im Gegensatz zu Tabellen passen sich Raster an unterschiedliche
Bildschirmgrößen an.
:::

## Tabellenbeschriftung

Jede Tabelle kann optional eine Beschriftung erhalten. Dafür wird unter der
Tabelle eine Zeile mit dem Inhalt `Table: [Beschriftungstext]` eingefügt.
Alternativ kann dies auch auf `: [Beschriftungstext]` verkürzt werden.

:::example
**Markdown**

```markdown
A   B   C
--- --- --
11  21  31

Table: Einfache Tabelle mit Beschriftung
```

**Ergebnis**

A   B   C
--- --- --
11  21  31

Table: Einfache Tabelle mit Beschriftung
:::

## Tabellenarten

Für die Erstellung von Tabellen existieren vier verschiedene Formen, die sich in
der Schreibweise und den Möglichkeiten unterscheiden:

- [Einfach (simple)](#simple)
- [Mehrzeilig (multiline)](#multiline)
- [Gitter (grid)](#grid)
- [Pipe-Symbol (pipe)](#pipe)

### Einfach (simple) {#simple}

Einfache Tabellen bestehen aus einer Kopfzeile und den Zelleninhalten. Auf die
Ausrichtung der Inhalte kann Einfluss genommen werden. Die Kopfzeile kann auch
ganz weggelassen werden. Allerdings muss die Tabelle dann mit einer Zeile aus
Bindestrichen abeschlossen werden.

:::example
**Markdown**

```markdown
  Zentrierte Kopfzeile   Standard   Rechtsbündig Linksbündig
------------------------ -------- -------------- ---------------------------------------------------------
           11            21                   31 Zeilenumbrüche innerhalb einer Zelle sind nicht möglich.
           12            22                   32 42

: Einfache Tabelle mit Kopfzeile
```

**Ergebnis**

  Zentrierte Kopfzeile   Standard   Rechtsbündig Linksbündig
------------------------ -------- -------------- ---------------------------------------------------------
           11            21                   31 Zeilenumbrüche innerhalb einer Zelle sind nicht möglich.
           12            22                   32 42

: Einfache Tabelle mit Kopfzeile

**Markdown**

```markdown
------ -- ---- ----------------------------------------------------------
  11   21   31 Zeilenumbrüche innerhalb einer Zelle sind nicht möglich.
  12   22   32 42
------ -- ---- ----------------------------------------------------------

: Einfache Tabelle ohne Kopfzeile
```

**Ergebnis**

------ -- ---- ----------------------------------------------------------
  11   21   31 Zeilenumbrüche innerhalb einer Zelle sind nicht möglich.
  12   22   32 42
------ -- ---- ----------------------------------------------------------

: Einfache Tabelle ohne Kopfzeile
:::

### Mehrzeilig (multiline) {#multiline}

Zur besseren Lesbarkeit können mehrzeilige Tabellen verwendet werden. Hier
lässt sich Text innerhalb einer Zelle umbrechen. In der Darstellung ist der
Textumbruch von der verfügbaren Breite abhängig.

Mehrzeilige Tabellen sind ähnlich zu einfachen Tabellen, müssen aber von einer
durchgängigen Linie aus Bindestrichen und einer Leerzeile umschlossen sein.

:::example
**Markdown**

```markdown
---------------------------------------------------------------------
 Zentrierte  Standard   Rechtsbündig Linksbündig
  Kopfzeile
------------ -------- -------------- --------------------------------
     11      21                   31 Zeilenumbrüche innerhalb einer\
                                     Zelle sind möglich.

     12      22                   32 42
---------------------------------------------------------------------

: Mehrzeilige Tabelle mit Kopfzeile
```

**Ergebnis**

---------------------------------------------------------------------
 Zentrierte  Standard   Rechtsbündig Linksbündig
  Kopfzeile
------------ -------- -------------- --------------------------------
     11      21                   31 Zeilenumbrüche innerhalb einer\
                                     Zelle sind möglich.

     12      22                   32 42
---------------------------------------------------------------------

: Mehrzeilige Tabelle mit Kopfzeile

**Markdown**

```markdown
-------- ----- ----- --------------------------------
   11    21       31 Zeilenumbrüche innerhalb einer\
                     Zelle sind möglich.

   12    22       32 42
-------- ----- ----- --------------------------------

: Mehrzeilige Tabelle ohne Kopfzeile
```

**Ergebnis**

-------- ----- ----- --------------------------------
   11    21       31 Zeilenumbrüche innerhalb einer\
                     Zelle sind möglich.

   12    22       32 42
-------- ----- ----- --------------------------------

: Mehrzeilige Tabelle ohne Kopfzeile
:::


### Gitter (grid) {#grid}

Gittertabellen bieten eine weitere Methode Tabellen zu verfassen. Sie lassen die
beliebige Verwendung von Blockelementen, wie mehrere Absätze, Listen, usw.,
innerhalb einer Zelle zu.

Die Tabelle wird hier aus einer Kombination der Zeichen `-`, `+`, `|`, `=` und
`:` beschrieben. Die Kopfzeile wird durch eine Linie aus Gleichheitszeichen vom
Rest der Zeilen getrennt. Die Textausrichtung der Spalten wird durch das
Doppelpunktsymbol in der Linie unterhalb der Kopfzeile definiert.

:::example
**Markdown**

```markdown
+------------+----------+--------------+---------------------------------+
| Zentrierte | Standard | Rechtsbündig | Linksbündig                     |
| Kopfzeile  |          |              |                                 |
+:==========:+==========+=============:+:================================+
| 11         | 21       | 31           | Zeilenumbrüche innerhalb einer\ |
|            |          |              | Zelle sind möglich.             |
+------------+----------+--------------+---------------------------------+
| 12         | 22       | 32           | - Beliebige Blockelemente       |
|            |          |              | - sind möglich.                 |
+------------+----------+--------------+---------------------------------+

: Gittertabelle mit Kopfzeile
```

**Ergebnis**

+------------+----------+--------------+---------------------------------+
| Zentrierte | Standard | Rechtsbündig | Linksbündig                     |
| Kopfzeile  |          |              |                                 |
+:==========:+==========+=============:+:================================+
| 11         | 21       | 31           | Zeilenumbrüche innerhalb einer\ |
|            |          |              | Zelle sind möglich.             |
+------------+----------+--------------+---------------------------------+
| 12         | 22       | 32           | - Beliebige Blockelemente       |
|            |          |              | - sind möglich.                 |
+------------+----------+--------------+---------------------------------+

: Gittertabelle mit Kopfzeile

**Markdown**

```markdown
+:----------:+----------+-------------:+:--------------------------------+
| 11         | 21       | 31           | Zeilenumbrüche innerhalb einer\ |
|            |          |              | Zelle sind möglich.             |
+------------+----------+--------------+---------------------------------+
| 12         | 22       | 32           | - Beliebige Blockelemente       |
|            |          |              | - sind möglich.                 |
+------------+----------+--------------+---------------------------------+

: Gittertabelle ohne Kopfzeile
```

**Ergebnis**

+:----------:+----------+-------------:+:--------------------------------+
| 11         | 21       | 31           | Zeilenumbrüche innerhalb einer\ |
|            |          |              | Zelle sind möglich.             |
+------------+----------+--------------+---------------------------------+
| 12         | 22       | 32           | - Beliebige Blockelemente       |
|            |          |              | - sind möglich.                 |
+------------+----------+--------------+---------------------------------+

: Gittertabelle ohne Kopfzeile
:::

### Pipe-Symbol (pipe) {#pipe}

Eine weitere Möglichkeit Tabellen zu formatieren bieten Pipe-Tabellen. Sie
werden mit Hilfe des Pipe-Symbols `|` erstellt.

Pipe-Tabellen erlauben keine mehrzeiligen Zellen oder Blockelemente. Sie
verwenden das Doppelpunktsymbol, um die Ausrichtung festzulegen. Außerdem
müssen sie nicht zwingend vertikal exakt ausgerichtet werden.

:::example
**Markdown**

```markdown
| Zentrierte Kopfzeile | Standard | Rechtsbündig | Linksbündig                                                    |
|:--------------------:|----------|-------------:|:---------------------------------------------------------------|
| 11                   |  21      | 31           | Zeilenumbrüche innerhalb einer Zelle werden nicht unterstützt. |
| 12                   | 22       | 32           | 42                                                             |

: Pipe-Tabelle mit vertikaler Ausrichtung
```

**Ergebnis**

| Zentrierte Kopfzeile | Standard | Rechtsbündig | Linksbündig                                                    |
|:--------------------:|----------|-------------:|:---------------------------------------------------------------|
| 11                   |  21      | 31           | Zeilenumbrüche innerhalb einer Zelle werden nicht unterstützt. |
| 12                   | 22       | 32           | 42                                                             |

: Pipe-Tabelle mit vertikaler Ausrichtung

**Markdown**

```markdown
|Zentrierte Kopfzeile|Standard|Rechtsbündig|Linksbündig|
:--:|--|--:|:--|
|11|21|31|Zeilenumbrüche innerhalb einer Zelle werden nicht unterstützt.|
|12|22|32|42|

: Pipe-Tabelle ohne vertikale Ausrichtung
```

**Ergebnis**

|Zentrierte Kopfzeile|Standard|Rechtsbündig|Linksbündig|
:--:|--|--:|:--|
|11|21|31|Zeilenumbrüche innerhalb einer Zelle werden nicht unterstützt.|
|12|22|32|42|

: Pipe-Tabelle ohne vertikale Ausrichtung
:::
