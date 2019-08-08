---
title: Internal Links
---

In order to link to another element, anchor points need to be defined. Elements
can be referenced by attaching an ID to them. IDs need to be unique within one
document.

```markdown
## Heading with ID {#my-id}

[Link to heading](#my-id)
```

## Heading with ID {#my-id}

[Link to heading](#my-id)

:::info
Each heading is automatically assigned an ID, derived from the text.

```markdown
## This is a test

[Link to implicit ID](#this-is-a-test)
```

## This is a test

[Link to implicit ID](#this-is-a-test)
:::

To create a link to another section, you need to specify the section ID. You
can leave the link text blank to show the section title or add a custom one.

```markdown
[](/section/02-elements/07-media)  
[other section](/section/02-elements/07-media)
```

[](/section/02-elements/07-media)  
[other section](/section/02-elements/07-media)

Links to other sections can also have IDs.

```markdown
[](/section/02-elements/07-media#videos)
```

[](/section/02-elements/07-media#videos)

This is a [Link](/section/does-not-exist) to a non-existent chapter.
