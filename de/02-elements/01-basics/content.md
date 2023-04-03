---
title: Grundlagen
---

## Absätze und Zeilenumbrüche {#paragraphs-and-line-breaks}

Absätze werden automatisch erstellt, indem zwischen dem Text eine Leerzeile
Abstand gelassen wird. Das Hinzufügen von mehr als einer Leerzeile führt nicht
zu einem größeren Abstand zwischen den Absätzen.

<Info>
  Zeilenumbrüche innerhalb eines Absatzes werden nicht im Ergebnis angezeigt. Um
  einen Zeilenumbruch zu erzwingen, muss ein doppeltes Leerzeichen am Ende der
  Zeile verwendet werden.
</Info>

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
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
    <TabItem label="Ergebnis">
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

      *Hinweis: Am Ende der Zeilen des zweiten Absatzes befindet sich ein doppeltes Leerzeichen.*
    </TabItem>
  </Tabs>
</Example>

## Textformatierung {#formatting}

Dieser Abschnitt demonstriert Möglichkeiten der einfachen Textformatierung.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      Es ist möglich, *wichtige Wörter* hervorzuheben. Dafür gibt es zwei
      _verschiedene Möglichkeiten_.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Es ist möglich, *wichtige Wörter* hervorzuheben. Dafür gibt es zwei
      _verschiedene Möglichkeiten_.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Ergebnis">
      **Noch wichtigere Wörter** werden fett gedruckt. Auch dafür gibt es zwei
      __verschiedene Möglichkeiten__.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      **Noch wichtigere Wörter** werden fett gedruckt. Auch dafür gibt es zwei
      __verschiedene Möglichkeiten__.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Ergebnis">
      Eine weitere Formatierungsmöglichkeit ist das ~~Durchstreichen~~ von Wörtern
      ~~oder ganzen Satzteilen~~.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Eine weitere Formatierungsmöglichkeit ist das ~~Durchstreichen~~ von Wörtern
      ~~oder ganzen Satzteilen~~.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Ergebnis">
      Die Formatierungsmöglichkeiten können natürlich kombiniert werden.
      Beispielsweise lassen sich *in einem wichtigen Satzteil ~~Wörter~~
      durchstreichen*.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Die Formatierungsmöglichkeiten können natürlich kombiniert werden.
      Beispielsweise lassen sich *in einem wichtigen Satzteil ~~Wörter~~
      durchstreichen*.
      ```
    </TabItem>
  </Tabs>

  <Tabs>
    <TabItem label="Ergebnis">
      Soll ein Formatierungszeichen gedruckt werden, so kann ein \*Backslash\*
      vorangestellt werden.
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      Soll ein Formatierungszeichen gedruckt werden, so kann ein \*Backslash\*
      vorangestellt werden.
      ```
    </TabItem>
  </Tabs>
</Example>

## Überschriften

Einzelne Abschnitte können durch Überschriften weiter strukturiert werden.

Siehe auch das [Beispiel für die Vergabe von
IDs](/section/02-elements/02-links/01-internal#referencing-elements).

<Info>
  Die Verwendung von Überschriften erster Ordnung sollte vermieden werden, da
  diese dem Seitentitel vorbehalten ist.
</Info>

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      ## Überschrift zweiter Ordnung
      ### Überschrift dritter Ordnung
      #### Überschrift vierter Ordnung
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      ## Überschrift zweiter Ordnung
      ### Überschrift dritter Ordnung
      #### Überschrift vierter Ordnung
      ```
    </TabItem>
  </Tabs>
</Example>

## Listen und Aufzählungen

Es können nummerierte und unnummerierte Listen angezeigt werden.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      - A
      - B
      - C

      1. A
      2. B
      3. C
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

  Listen können untergliedert und kombiniert werden.

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

## Blockzitate

Durch ein Voranstellen des Zeichens `>` lassen sich Blockzitate umsetzen.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      > Sein oder Nichtsein: das ist die Frage  
      > —William Shakespeare
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      > Sein oder Nichtsein: das ist die Frage  
      > —William Shakespeare
      ```
    </TabItem>
  </Tabs>
</Example>
