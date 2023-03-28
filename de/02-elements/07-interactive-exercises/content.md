---
title: Interaktive Aufgaben
---

Interaktive Übungen sind von einer Box der Klasse `exercise` umschlossen.
Innerhalb der Box werden eine oder mehr Elemente der Klasse `question` platziert.

Außerdem muss jede Aufgabe eine ID haben. Die ID muss innerhalb des Dokumentes
eindeutig sein. Sie kann verwendet werden, um aus anderen Teilen des Kurses
zur Aufgabe zu verweisen.

**Markdown**

```markdown
:::exercise{#EX_DUMMY}
[INHALT]
:::
```

**Ergebnis**

:::exercise{#EX_DUMMY}
[INHALT]
:::

Die Box enthält typischerweise die Aufgabenstellung und eine oder mehrere
Fragen. Optional können auch Hinweise, der Lösungsweg, ein Button zur
Überprüfung der Lösung und andere Inhalte dargestellt werden.

Die erreichbare Gesamtpunktzahl einer Aufgabe ist die Summe der Punkte aller
enthaltenen Fragen.

:::::example
Unten finden Sie ein vollständiges Beispiel für eine Aufgabe.

**Markdown**

```markdown
::::exercise{#EX_FULL}
Welcher Term entsteht, wenn man in $x^2+y^2$ Folgendes einsetzt und soweit wie
möglich vereinfacht:

Den Winkel $\alpha$ sowohl für $x$ als auch für $y$: Dann ist
$x^2+y^2$$\;\;=\;$[]{.question .text length="13"
solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5"
validation="mathExpression" points="4"}.

:::hint-text
Der griechische Buchstabe $\alpha$ kann als `alpha` eingetippt werden.
:::

:::hint
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
:::
::::
```

**Ergebnis**

::::exercise{#EX_FULL}
Welcher Term entsteht, wenn man in $x^2+y^2$ Folgendes einsetzt und soweit wie
möglich vereinfacht:

Den Winkel $\alpha$ sowohl für $x$ als auch für $y$: Dann ist
$x^2+y^2$$\;\;=\;$[]{.question .text length="13"
solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5"
validation="mathExpression" points="4"}.

:::hint-text
Der griechische Buchstabe $\alpha$ kann als `alpha` eingetippt werden.
:::

:::hint
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
:::
::::
:::::

## Aufbau einer Frage

Innerhalb einer `exercise`-Textbox gibt es eine oder mehrere Fragen. Eine Frage
wird durch die Klasse `question` und dem Typen (z. B. `text`) angegeben. Außerdem
besitzen manche Fragetypen spezifische Parameter.

```markdown
[]{.question .text parameter1=wert1 parameter2=wert2}
```

Der Rest des Abschnitts widmet sich den verschiedenen Fragetypen und deren
Parametern.

## Fragetypen

Derzeit sind zwei Arten von Fragen implementiert: `text` und `checkbox`. Sie
werden in den Unterabschnitten
[](/section/02-elements/07-interactive-exercises/01-text) und
[](/section/02-elements/07-interactive-exercises/02-checkbox) beschrieben.

Alle Fragetypen akzeptieren mindestens folgende Parameter.

------------------- -----------------------------------------------------------
`solution`          Die Lösung.

`validation`        Art der Überprüfung.

`points`            Erreichbare Punkte bei korrekter Antwort.
------------------- -----------------------------------------------------------
