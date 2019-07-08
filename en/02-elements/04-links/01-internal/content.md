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
[]{data-link-section="02-elements/07-media"}  
[other section]{data-link-section="02-elements/07-media"}
```

[]{data-link-section="02-elements/07-media"}  
[other section]{data-link-section="02-elements/07-media"}

Links to other sections can also have IDs.

```markdown
[]{data-link-section="02-elements/07-media#videos"}
```

[]{data-link-section="02-elements/07-media#videos"}

This is a [Link]{data-link-section="does-not-exist"} to a non-existent chapter.
