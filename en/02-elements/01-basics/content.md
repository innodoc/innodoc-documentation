---
title: Basics
---

## Paragraphs and line breaks {#paragraphs-and-line-breaks}

Paragraphs are automatically created simply by leaving an empty line between
text. Adding more than one empty line will not create a larger distance between
the paragraphs.

<Info>
  Line breaks within a paragraph are not displayed in the result. To force a line
  break, a double space must be used at the end of the line.
</Info>

<Example>
  <Tabs>
    <TabItem label="Result">
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
      at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
      vestibulum.

      Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
      vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
      at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
      vestibulum.

      Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
      vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Result">
      Lorem ipsum
      dolor sit amet,
      consectetur adipiscing elit.

      Lorem ipsum  
      dolor sit amet,  
      consectetur adipiscing elit.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Lorem ipsum
      dolor sit amet,
      consectetur adipiscing elit.

      Lorem ipsum  
      dolor sit amet,  
      consectetur adipiscing elit.
      ```

      *Note: There is a double space at the end of each line of the second
      paragraph.*
    </TabItem>
  </Tabs>
</Example>

## Text Formatting {#formatting}

This section demonstrates the possibilities of basic text formatting.

<Example>
  <Tabs>
    <TabItem label="Result">
      It is possible to highlight *important words*. There are _two ways_ to
      accomplish this.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      It is possible to highlight *important words*. There are _two ways_ to
      accomplish this.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Result">
      Even more **important words** are printed in bold. For this there are also two
      __different ways__.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Even more **important words** are printed in bold. For this there are also two
      __different ways__.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Result">
      Another formatting option is crossing out ~~words~~ or ~~whole phrases~~.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Another formatting option is crossing out ~~words~~ or ~~whole phrases~~.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Result">
      The formatting options can of course be combined. For example, *in an important
      part of a sentence you can cross out ~~words~~*.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      The formatting options can of course be combined. For example, *in an important
      part of a sentence you can cross out ~~words~~*.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Result">
      If a formatting character is to be printed, it must be prefixed with a
      \*Backslash\*.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      If a formatting character is to be printed, it must be prefixed with a
      \*Backslash\*.
      ```
    </TabItem>
  </Tabs>
</Example>

## Headings

Individual sections can be further structured by using headings.

See also the [example for adding IDs to
headers](/section/02-elements/02-links/01-internal#referencing-elements).

<Info>
  First-order headings should not be used as they are reserved for the page title.
</Info>

<Example>
  <Tabs>
    <TabItem label="Result">
      ## Second-order heading
      ### Third-order heading
      #### Fourth-order heading
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      ## Second-order heading
      ### Third-order heading
      #### Fourth-order heading
      ```
    </TabItem>
  </Tabs>
</Example>

## Lists and Enumerations

Numbered and unnumbered lists can be displayed.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      - A
      - B
      - C

      1. A
      1. B
      1. C
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      - A
      - B
      - C

      1. A
      1. B
      1. C
      ```
    </TabItem>
  </Tabs>

  Lists can be nested and combined.

  <Tabs>
    <TabItem label="Ergebnis">
      - I
        - II
            1. III
            1. III
        - II
      - I
        1. II
        1. II
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      - I
        - II
            1. III
            1. III
        - II
      - I
        1. II
        1. II
      ```
    </TabItem>
  </Tabs>
</Example>

## Block quotations

By prefixing lines with the character `>` block quotations can be displayed.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      > To be, or not to be: that is the question  
      > —William Shakespeare
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      > To be, or not to be: that is the question  
      > —William Shakespeare
      ```
    </TabItem>
  </Tabs>
</Example>
