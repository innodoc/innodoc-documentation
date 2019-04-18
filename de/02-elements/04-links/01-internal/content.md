---
title: Interne Links
---

Es können beliebige Ankerpunkte definiert und verlinkt werden. Dazu wird einem
Element eine ID angefügt, so dass es sich referenzieren lässt. IDs dürfen
innerhalb eines Dokumentes nur einmal vorkommen.

```markdown
## Überschrift mit ID {#meine-id}

[Link zur Überschrift](#meine-id)
```

## Überschrift mit ID {#meine-id}

[Link zur Überschrift](#meine-id)

:::info
Jede Überschrift bekommt automatisch eine ID, die aus dem Text abgeleitet
wird.

```markdown
## Das ist ein Test

[Link zu implizitem Anker](#das-ist-ein-test)
```

## Das ist ein Test

[Link zu implizitem Anker](#das-ist-ein-test)
:::

Soll ein Link zu einem anderen Abschnitt gesetzt werden, so muss dieser
angegeben werden. Wird der Linktext leer gelassen, erscheint der Titel des
Abschnitts.

```markdown
[]{data-link-section="02-elements/07-media"}  
[anderer Kapitel]{data-link-section="02-elements/07-media"}
```

[]{data-link-section="02-elements/07-media"}  
[anderes Kapitel]{data-link-section="02-elements/07-media"}

Links zu anderen Abschnitten funktionieren auch mit Ankerpunkten.

```markdown
[]{data-link-section="02-elements/07-media#videos"}
```

[]{data-link-section="02-elements/07-media#videos"}
