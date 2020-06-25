---
title: Interne Links
---

Es kann auf andere Abschnitte, bestimmte Elemente innerhalb von Abschnitten und
"spezielle" Seiten verweist werden.

## Verweise auf andere Abschnitte

Um einen Link zu einem anderen Abschnitt zu erstellen, muss die Abschnitts-ID
angeben werden. Wenn der Linktext weglassen wird, werden die Abschnittsnummer
und der Titel angezeigt.

::: {.example}

```markdown
[](/section/02-elements/07-media)  
[anderer Abschnitt](/section/02-elements/07-media)
```

[](/section/02-elements/07-media)  
[anderer Abschnitt](/section/02-elements/07-media)
:::

Wenn ein verlinkter Abschnitt nicht existiert, wird der Link trotzdem
dargestellt, führt aber zu einer Fehlerseite:  
[Dies ist ein Link zu einem nicht existierendem
Kapitel.](/section/does-not-exist)

## Verweise auf einzelne Elemente innerhalb eines Abschnitts

Um auf ein bestimmtes Element innerhalb eines Abschnitts zu verweisen, werden
IDs verwendet. Diese müssen innerhalb eines Dokuments einzigartig sein und
können manuell zugewiesen werden.

::: {.example}
Link zur Überschrift _Videos_ in einem anderen Kapitel:

```markdown
[](/section/02-elements/07-media#videos)
```

[](/section/02-elements/07-media#videos)
:::

IDs können zugewiesen werden, indem der Bezeichner mit einem vorangestelltem `#`
angegeben wird.

::: {.example}

```markdown
## Überschrift mit ID {#my-id}

[Link zur Überschrift](#my-id)
```

## Überschrift mit ID {#my-id}

[Link zur Überschrift](#my-id)
:::

::: {.info}
Wird kein Bezeichner angegeben, erhalten Überschriften automatisch eine vom
Text abgeleitete ID.

```markdown
## Das ist ein test

[Link zur Überschrift](#das-ist-ein-test)
```

## Das ist ein test

[Link zur Überschrift](#das-ist-ein-test)
:::

## Verweise auf spezielle Seiten

In jedem Kurs gibt es die speziellen Seiten für das _Stichwort-_ und
_Inhaltsverzeichnis_. Diese haben keine Abschnitts-ID, aber können mittels der
speziellen Bezeichner `___INDEX_PAGE___` und `___TOC___` trotzdem referenziert
werden.

::: {.example}

```markdown
[](___INDEX_PAGE___)  
[](___TOC___)
```

[](___INDEX_PAGE___)  
[](___TOC___)
:::
