---
title: Grundlagen
---

## Absätze und Zeilenumbrüche {#paragraphs-and-line-breaks}

Absätze werden automatisch erstellt, indem zwischen dem Text eine Leerzeile
Abstand gelassen wird. Das Hinzufügen von mehr als einer Leerzeile führt nicht
zu einem größeren Abstand zwischen den Absätzen.

:::info
Zeilenumbrüche innerhalb eines Absatzes werden nicht im Ergebnis angezeigt. Um
einen Zeilenumbruch zu erzwingen, muss ein doppeltes Leerzeichen am Ende der
Zeile verwendet werden.
:::

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
:::

:::tab-item
```markdown
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Lorem ipsum
dolor sit amet,
consectetur adipiscing elit.

Lorem ipsum  
dolor sit amet,  
consectetur adipiscing elit.
:::

:::tab-item
```markdown
Lorem ipsum
dolor sit amet,
consectetur adipiscing elit.

Lorem ipsum  
dolor sit amet,  
consectetur adipiscing elit.
```

*Hinweis: Am Ende der Zeilen des zweiten Absatzes befindet sich ein doppeltes
Leerzeichen.*
:::
::::
:::::

## Textformatierung {#formatting}

Dieser Abschnitt demonstriert Möglichkeiten der einfachen Textformatierung.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Es ist möglich, *wichtige Wörter* hervorzuheben. Dafür gibt es zwei
_verschiedene Möglichkeiten_.
:::

:::tab-item
```markdown
Es ist möglich, *wichtige Wörter* hervorzuheben. Dafür gibt es zwei
_verschiedene Möglichkeiten_.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
**Noch wichtigere Wörter** werden fett gedruckt. Auch dafür gibt es zwei
__verschiedene Möglichkeiten__.
:::

:::tab-item
```markdown
**Noch wichtigere Wörter** werden fett gedruckt. Auch dafür gibt es zwei
__verschiedene Möglichkeiten__.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Eine weitere Formatierungsmöglichkeit ist das ~~Durchstreichen~~ von Wörtern
~~oder ganzen Satzteilen~~.
:::

:::tab-item
```markdown
Eine weitere Formatierungsmöglichkeit ist das ~~Durchstreichen~~ von Wörtern
~~oder ganzen Satzteilen~~.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Die Formatierungsmöglichkeiten können natürlich kombiniert werden.
Beispielsweise lassen sich *in einem wichtigen Satzteil ~~Wörter~~
durchstreichen*.
:::

:::tab-item
```markdown
Die Formatierungsmöglichkeiten können natürlich kombiniert werden.
Beispielsweise lassen sich *in einem wichtigen Satzteil ~~Wörter~~
durchstreichen*.
```
:::
::::

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
Soll ein Formatierungszeichen gedruckt werden, so kann ein \*Backslash\*
vorangestellt werden.
:::

:::tab-item
```markdown
Soll ein Formatierungszeichen gedruckt werden, so kann ein \*Backslash\*
vorangestellt werden.
```
:::
::::
:::::

## Überschriften

Einzelne Abschnitte können durch Überschriften weiter strukturiert werden.

Siehe auch das [Beispiel für die Vergabe von
IDs](/section/02-elements/02-links/01-internal#referencing-elements).

:::info
Die Verwendung von Überschriften erster Ordnung sollte vermieden werden, da
diese dem Seitentitel vorbehalten ist.
:::

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
## Überschrift zweiter Ordnung
### Überschrift dritter Ordnung
#### Überschrift vierter Ordnung
:::

:::tab-item
```markdown
## Überschrift zweiter Ordnung
### Überschrift dritter Ordnung
#### Überschrift vierter Ordnung
```
:::
::::
:::::

## Listen und Aufzählungen

Es können nummerierte und unnummerierte Listen angezeigt werden.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
- A
- B
- C

1. A
2. B
3. C
:::

:::tab-item
```markdown
- A
- B
- C

1. A
1. B
1. C
```
:::
::::

Listen können untergliedert und kombiniert werden.

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
- I
   - II
      1. III
      1. III
   - II
- I
   1. II
   1. II
:::

:::tab-item
```markdown
- I
   - II
      1. III
      1. III
   - II
- I
   1. II
   1. II
`:::
::::
:::::

## Blockzitate

Durch ein Voranstellen des Zeichens `>` lassen sich Blockzitate umsetzen.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
> Sein oder Nichtsein: das ist die Frage  
> —William Shakespeare
:::

:::tab-item
```markdown
> Sein oder Nichtsein: das ist die Frage  
> —William Shakespeare
```
:::
::::
:::::
