---
title: Tabellen
---

Tabellen erlauben keine mehrzeiligen Zellen oder Blockelemente. Sie verwenden
das Doppelpunktsymbol, um die Ausrichtung festzulegen.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      | Zentrierte Kopfzeile | Standard | Rechtsbündig | Linksbündig |
      |:--------------------:|----------|-------------:|:------------|
      | 11                   | 21       | 31           | 32          |
      | 12                   | 22       | 32           | 42          |
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      | Zentrierte Kopfzeile | Standard | Rechtsbündig | Linksbündig |
      |:--------------------:|----------|-------------:|:------------|
      | 11                   | 21       | 31           | 32          |
      | 12                   | 22       | 32           | 42          |
      ```
    </TabItem>
  </Tabs>
</Example>

<Info>
  Tabellen eignen sich zur Darstellung von tabellarischen Daten. Für
  Layoutaufgaben, also um beispielsweise Elemente nebeneinander anzuordnen, wird
  der Einsatz eines [Rasters](/section/02-elements/06-grids) empfohlen. Im
  Gegensatz zu Tabellen passen sich Raster an unterschiedliche Bildschirmgrößen
  an.
</Info>

## `table`-Umgebung

In der Regel werden Tabellen mit einer `table`-Umgebung umschlossen. Dadurch
werden sie optisch vom Hintergrund abgesetzt, können eine `id` zum Verlinken
sowie eine Beschriftung erhalten.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      <Table id="example-table">
        <Caption>Einfache Tabelle mit Beschriftung</Caption>
        | A  | B   | C  |
        |----|-----|----|
        | 11 | 21  | 31 |
      </Table>
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      <Table id="example-table">
        <Caption>Einfache Tabelle mit Beschriftung</Caption>
        | A  | B   | C  |
        |----|-----|----|
        | 11 | 21  | 31 |
      </Table>
      ```
    </TabItem>
  </Tabs>
</Example>
