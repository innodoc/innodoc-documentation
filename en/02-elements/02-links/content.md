---
title: Links
---

There are several ways to display links.

<Table>
  <Caption>Syntax for Links</Caption>
  | Result                                                                            | Markdown                                                                            | Description                                            |
  |-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|--------------------------------------------------------|
  | [Wikipedia](https://www.wikipedia.org/)                                           | `[Wikipedia](https://www.wikipedia.org/)`                                           | Link target and text                                   |
  | [Wikipedia](https://www.wikipedia.org/ "Wikipedia is a free online encyclopedia") | `[Wikipedia](https://www.wikipedia.org/ "Wikipedia is a free online encyclopedia")` | Link target, text and title (displayed on mouse hover) |
</Table>

The link text can consist of any inline elements, such as [formatted
text](app:section|02-elements/01-basics#formatting),
[formulas](app:section|02-elements/03-formulas), or even
[images](app:section|02-elements/04-media).

A distinction is made between *internal* and *external* links. [Internal
links](app:section|02-elements/02-links/01-internal) refer to pages within the
course, such as content pages, the [home page](app:home) or the
[glossary](app:glossary). External links enable references to other websites
outside of this course.

<Info>
  Section [](/section/02-elements/04-media#images-as-link) describes
  how an image can be linked.
</Info>

Link addresses can also be written collectively in a link list. For this
purpose an identifier in square brackets is used instead of an address in round
brackets. At the end of the document, a link list must be written that maps
link identifiers to addresses.

<Example>
  <Tabs>
    <TabItem label="Result">
      [Link to TU Berlin][TU Berlin]  
      [Wikipedia]
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      [Link to TU Berlin][TU Berlin]  
      [Wikipedia]
      ```

      Put a link list at the very end of your document.

      ```markdown
      [TU Berlin]: https://www.tu-berlin.de
      [Wikipedia]: https://www.wikipedia.org
      ```
    </TabItem>
  </Tabs>
</Example>

[TU Berlin]: https://www.tu-berlin.de
[Wikipedia]: https://www.wikipedia.org
