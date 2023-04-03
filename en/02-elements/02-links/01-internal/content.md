---
title: Internal Links
---

It is possible to create links to any internal application page using the
`app:ROUTE|PARAMETER` schema.

<Grid>
  <GridItem xs="4" md="2">
    `ROUTE`
  </GridItem>
  <GridItem xs="8" md="10">
    The name of the route. An [overview of all routes](#routes) can be found at the
    end of this section.
  </GridItem>
  <GridItem xs="4" md="2">
    `PARAMETER`
  </GridItem>
  <GridItem xs="8" md="10">
    The parameter of the route is only specified for links to pages and sections.
  </GridItem>
</Grid>

## Links to Sections and Pages

To create a link to a section or a page, the *section path* or *page name* must
be provided as a parameter. The route and parameter are separated by a pipe
symbol `|`. If no link text is specified, the title of the link destination is
automatically inserted.

<Example>
  <Tabs>
    <TabItem label="Result">
      [](app:section|02-elements/04-media)  
      [other section](app:section|02-elements/04-media)  
      [](app:page|about)  
      [other page](app:page|about)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      [](app:section|02-elements/04-media)  
      [other section](app:section|02-elements/04-media)  
      [](app:page|about)  
      [other page](app:page|about)
      ```
    </TabItem>
  </Tabs>
</Example>

<Info>
  If a linked section or page does not exist, an error message is shown:  
  [This is a link to a non-existent chapter.](/section/does-not-exist)
</Info>

## Referencing elements {#referencing-elements}

To refer to a specific element within a section, *anchor IDs* are used. These
must be unique within a document and can be assigned manually.

Anchor IDs can be assigned to content elements by specifying the identifier with
a preceding `#`. This allows for referencing headings, as well as other
elements.

<Example>
Link to heading with manually assigned ID.

  <Tabs>
    <TabItem label="Result">
      ### Heading with ID {#my-id}

      [Link to heading](#my-id)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      ### Heading with ID {#my-id}

      [Link to heading](#my-id)
      ```
    </TabItem>
  </Tabs>

  If no ID is explicitly assigned, headings are automatically assigned an ID
  derived from the text. For consistency, especially in multilingual texts, it is
  recommended to manually assign an explicit ID when referencing headings.

  <Tabs>
    <TabItem label="Result">
      ### Heading with automatic ID

      [Link to heading](#heading-with-automatic-id)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      ### Heading with automatic ID

      [Link to heading](#heading-with-automatic-id)
      ```
    </TabItem>
  </Tabs>

  Link to heading _Videos_ in another chapter:

  <Tabs>
    <TabItem label="Result">
      [Subsection _Videos_ in chapter _Images and Videos_](/section/02-elements/04-media#videos)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      [Subsection _Videos_ in chapter _Images and Videos_](/section/02-elements/04-media#videos)
      ```
    </TabItem>
  </Tabs>
</Example>

## References to Other Pages

In every course, there are additional pages such as the glossary and table of
contents. These are referenced by using the corresponding route.

<Example>
  <Tabs>
    <TabItem label="Result">
      [](app:home)  
      [](app:progress)  
      [](app:toc)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      [](app:home)  
      [](app:progress)  
      [](app:toc)
      ```
    </TabItem>
  </Tabs>
</Example>

### Overview of Routes {#routes}

Below is an overview of the available application routes.

<Table>
  <Caption>Application routes</Caption>
  | Name                   | Destination       | Parameter    |
  |------------------------|-------------------|--------------|
  | `page`                 | Content page      | Page name    |
  | `section`              | Content section   | Section path |
  | `home`                 | Course homepage   |              |
  | `progress`             | Learning progress |              |
  | `toc`                  | Table of contents |              |
  | `glossary`             | Glossary          |              |
  | `user:login`           | Login             |              |
  | `user:forgot-password` | Password recovery |              |
  | `user:sign-up`         | Create account    |              |
</Table>
