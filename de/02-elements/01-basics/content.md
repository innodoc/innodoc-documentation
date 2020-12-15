---
title: Grundlagen
---

## Absätze und Zeilenumbrüche {#paragraphs-and-line-breaks}

Absätze werden automatisch erstellt, indem zwischen dem Text eine Leerzeile
Abstand gelassen wird. Das Hinzufügen von mehr als einer Leerzeile führt nicht
zu einem größeren Abstand zwischen den Absätzen.

::: {.info}
Zeilenumbrüche innerhalb eines Absatzes werden nicht im Ergebnis angezeigt. Um
einen Zeilenumbruch zu erzwingen, muss ein doppeltes Leerzeichen am Ende der
Zeile verwendet werden.
:::

::: {.example}
**Markdown**

```markdown
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.
```

**Ergebnis**

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc nunc velit, dictum
at tristique sit amet, aliquet id urna. Praesent aliquam ligula id urna
vestibulum.

Consectetur adipiscing elit. Proin nec tincidunt nunc. Curabitur orci eros,
vestibulum eu elementum ac, semper eget metus. Vivamus nulla sem.

**Markdown**

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

**Ergebnis**

Lorem ipsum
dolor sit amet,
consectetur adipiscing elit.

Lorem ipsum  
dolor sit amet,  
consectetur adipiscing elit.
:::

## Textformatierung

Dieser Abschnitt demonstriert Möglichkeiten der einfachen Textformatierung.

::: {.example}
**Markdown**

```markdown
Es ist möglich, *wichtige Wörter* hervorzuheben. Dafür gibt es zwei
_verschiedene Möglichkeiten_.
```

**Ergebnis**

Es ist möglich, *wichtige Wörter* hervorzuheben. Dafür gibt es zwei
_verschiedene Möglichkeiten_.

**Markdown**

```markdown
**Noch wichtigere Wörter** werden fett gedruckt. Auch dafür gibt es zwei
__verschiedene Möglichkeiten__.
```

**Ergebnis**

**Noch wichtigere Wörter** werden fett gedruckt. Auch dafür gibt es zwei
__verschiedene Möglichkeiten__.

**Markdown**

```markdown
Eine weitere Formatierungsmöglichkeit ist das ~~Durchstreichen~~ von Wörtern
~~oder ganzen Satzteilen~~.
```

**Ergebnis**

Eine weitere Formatierungsmöglichkeit ist das ~~Durchstreichen~~ von Wörtern
~~oder ganzen Satzteilen~~.

**Markdown**

```markdown
Die Formatierungsmöglichkeiten können natürlich kombiniert werden.
Beispielsweise lassen sich *in einem wichtigen Satzteil ~~Wörter~~
durchstreichen*.
```

**Ergebnis**

Die Formatierungsmöglichkeiten können natürlich kombiniert werden.
Beispielsweise lassen sich *in einem wichtigen Satzteil ~~Wörter~~
durchstreichen*.

**Markdown**

```markdown
Soll ein Formatierungszeichen gedruckt werden, so kann ein \*Backslash\*
vorangestellt werden.
```

**Ergebnis**

Soll ein Formatierungszeichen gedruckt werden, so kann ein \*Backslash\*
vorangestellt werden.
:::

## Überschriften

Einzelne Abschnitte können durch Überschriften weiter strukturiert werden.

Siehe auch das [Beispiel für die Vergabe von
IDs](/section/02-elements/02-links/01-internal#heading-example).

::: {.info}
Die Verwendung von Überschriften erster Ordnung sollte vermieden werden, da
diese dem Seitentitel vorbehalten ist.
:::

::: {.example}
**Markdown**

```markdown
## Überschrift zweiter Ordnung
### Überschrift dritter Ordnung
#### Überschrift vierter Ordnung
```

**Ergebnis**

## Überschrift zweiter Ordnung
### Überschrift dritter Ordnung
#### Überschrift vierter Ordnung
:::

## Listen und Aufzählungen

Es können nummerierte und unnummerierte Listen angezeigt werden.

::: {.example}
**Markdown**

```markdown
- A
- B
- C

1. A
1. B
1. C
```

**Ergebnis**

- A
- B
- C

1. A
2. B
3. C

Listen können untergliedert und kombiniert werden.

**Markdown**

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

**Ergebnis**

- I
   - II
      1. III
      1. III
   - II
- I
   1. II
   1. II
:::

## Blockzitate

Durch ein Voranstellen des Zeichens `>` lassen sich Blockzitate umsetzen.

:::{.example}
**Markdown**

```markdown
> Ich würde gerne auf dem Mars sterben. Aber nicht bei der Landung.  
> *Elon Musk*
```

**Ergebnis**

> Ich würde gerne auf dem Mars sterben. Aber nicht bei der Landung.  
> *Elon Musk*
:::
