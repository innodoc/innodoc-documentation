---
title: Tables
---

Tables do not allow for multi-line cells or block-level elements. They use the
colon symbol to specify alignment.

<Example>
  <Tabs>
    <TabItem label="Result">
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
  Tables are suitable for displaying tabular data. However, for layout tasks, such
  as arranging elements side by side, the use of a
  [grid](/section/02-elements/06-grids) is recommended. Unlike tables, grids adapt
  to different screen sizes.
</Info>


## `table` directive

Usually, tables are enclosed with a table directive. This visually sets them
apart from the background and allows them to have an `id` for linking purposes
as well as a caption.

<Example>
  <Tabs>
    <TabItem label="Result">
      <Table id="example-table">
        <Caption>Simple table with caption</Caption>
        | A  | B   | C  |
        |----|-----|----|
        | 11 | 21  | 31 |
      </Table>
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      <Table id="example-table">
        <Caption>Simple table with caption</Caption>
        | A  | B   | C  |
        |----|-----|----|
        | 11 | 21  | 31 |
      </Table>
      ```
    </TabItem>
  </Tabs>
</Example>
