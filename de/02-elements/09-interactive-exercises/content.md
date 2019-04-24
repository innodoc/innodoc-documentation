---
title: Interaktive Aufgaben
---

Inhalte können interaktiven Aufgaben umfassen. Aufgaben sollten von einer
Textbox des Typs `exercise` umschlossen sein.

```markdown
::: {.exercise}
[INHALT]
:::
```

::: {.exercise}
[INHALT]
:::

::: {.example}
Die Textbox enthält typischerweise die Aufgabenstellung und eine oder mehrere
Fragen. Optional können auch Hinweise, der Lösungsweg, ein Button zur
Überprüfung der Lösung oder andere Inhalte dargestellt werden.

```markdown
::: {.exercise}
Welcher Term entsteht, wenn man in $x^2+y^2$ Folgendes einsetzt und soweit wie
möglich vereinfacht:

Den Winkel $\alpha$ sowohl für $x$ als auch für $y$: Dann ist
$x^2+y^2$$\;\;=\;$[]{.question .text #EX_EXAMPLE length="13"
solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5"
validation="mathFormula" points="4"}.

:::: {.hint-text}
Der griechische Buchstabe $\alpha$ kann als `alpha` eingetippt werden.
::::

:::: {.hint}
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
::::
:::
```

::: {.exercise}
Welcher Term entsteht, wenn man in $x^2+y^2$ Folgendes einsetzt und soweit wie
möglich vereinfacht:

Den Winkel $\alpha$ sowohl für $x$ als auch für $y$: Dann ist
$x^2+y^2$$\;\;=\;$[]{.question .text #EX_EXAMPLE length="13"
solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5"
validation="mathFormula" points="4"}.

:::: {.hint-text}
Der griechische Buchstabe $\alpha$ kann als `alpha` eingetippt werden.
::::

:::: {.hint}
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
::::
:::
:::

## Aufbau einer Frage

Innerhalb einer `exercise`-Textbox gibt es eine oder mehrere Fragen. Eine Frage
wird durch die Klasse `question` und dem Typen (z. B. `text`) angegeben.

Darüber hinaus muss jeder Frage eine ID zugewiesen werden, die innerhalb eines
Dokumentes eindeutig sein muss. Die ID kann verwendet werden, um Fragen von
anderen Stellen zu referenzieren.

Außerdem besitzen manche Fragetypen spezifische Parameter.

```markdown
[]{.question .text #ID parameter1=wert1 parameter2=wert2}
```

Der Rest dieses Kapitels widmet sich den verschiedenen Fragetypen und deren
Parametern.

## Fragetypen

Alle Fragetypen akzeptieren mindestens folgende Parameter:

------------------- -----------------------------------------------------------
`solution`          Die korrekte Lösung. (Wird abhängig vom Paramter
                    `validation` unterschiedlich interpretiert.)

`validation`        Art der Überprüfung der eingegeben Lösung.

`points`            Die Anzahl der erreichbaren Punkte bei korrekter
                    Beantwortung.

`supporting-points` *TODO: Was ist das?*
------------------- -----------------------------------------------------------

### Texteingabe (`.text`)

Bei der Texteingabe wird ein Eingabefeld präsentiert. Sie existiert in
verschiedenen Varianten. Diese unterscheiden sich in der Art und Weise, wie
die Lösung überprüft wird, gesteuert über den Parameter `validation`.

Alle Varianten der Texteingabe akzeptieren den Parameter `length`.

--------- -------------------------------------------------------------
`length`  Die maximale Anzahl an Zeichen, die eingegeben werden können.
--------- -------------------------------------------------------------

#### Exakt (`validation="exact"`)

Bei diesem Fragetypen muss der eingetippte Wert exakt der Lösung entsprechen.

::: {.example}
Für die korrekte Beantwortung der Frage muss das Lösungswort *Lösung* exakt
eingegeben werden.

```markdown
Lösungswort: []{.question .text #EX_EXACT length="10" solution="Lösung"
validation="exact"}
```

Lösungswort: []{.question .text #EX_EXACT length="10" solution="Lösung"
validation="exact"}
:::

#### Mathematischer Ausdruck (`validation="mathExpression"`)

Die Eingabe wird als mathematischer Ausdruck interpretiert.

*TODO: Erklärung, mehr Beispiele, Parameter*


```
::: {.exercise}
Berechnen Sie mit Hilfe der round-Funktion die Rundung von
$\pi=\num{3,141592654}\ldots$ auf $4$ Nachkommastellen:

$\overline{\pi}\;=\;$[]{.question .text #EX_EXPR length="16"
solution="3.1416" precision="7" validation="mathExpression" points="4"}.
:::
```

::: {.exercise}
Berechnen Sie mit Hilfe der round-Funktion die Rundung von
$\pi=\num{3,141592654}\ldots$ auf $4$ Nachkommastellen:

$\overline{\pi}\;=\;$[]{.question .text #EX_EXPR length="16"
solution="3.1416" precision="7" validation="mathExpression" points="4"}.
:::

#### Vereinfachung eines mathematischen Terms (`validation="mathSimplify"`)

Bei diesem Fragetypen muss ein mathematischer Term vereinfacht werden.

*TODO: Erklärung, mehr Beispiele, Parameter*

```
::: {.exercise}
Vereinfachen Sie den Term:

$(x-3)(x+3)\;=\;$[]{.question .text #EX_SIMPLIFY length="14"
solution="(x-3)*(x+3)" supporting-points="10" variables="x" precision="5"
simplification-code="1" validation="mathSimplify"}
:::
```

::: {.exercise}
Vereinfachen Sie den Term:

$(x-3)(x+3)\;=\;$[]{.question .text #EX_SIMPLIFY length="14"
solution="(x-3)*(x+3)" supporting-points="10" variables="x" precision="5"
simplification-code="1" validation="mathSimplify"}
:::

#### Mathematische Funktion (`validation="mathFunction"`)

Bei diesem Fragetypen muss eine mathematische Funktion angegeben werden.

*TODO: Erklärung, mehr Beispiele, Parameter*

```
::: {.exercise}
Stellen Sie die Geradengleichung auf:

$y\;=\;$[]{.question .text #EX_FUNC length="15" solution="-1+x"
supporting-points="2" variables="x" precision="5" validation="mathFunction"
points="4"}
:::
```

::: {.exercise}
Stellen Sie die Geradengleichung auf:

$y\;=\;$[]{.question .text #EX_FUNC length="15" solution="-1+x"
supporting-points="2" variables="x" precision="5" validation="mathFunction"
points="4"}
:::

#### Intervall (`validation="mathInterval"`)

Dieser Fragetyp erfordert die Eingabe eines Intervalls.

*TODO: Erklärung, mehr Beispiele, Parameter*

```
::: {.exercise}
$\frac1x\geq\frac13$ besitzt die Lösungsmenge
$L$$\;=\;$[]{.question .text #EX_INTERVAL length="14" solution="(0;3]"
precision="3" validation="mathInterval" points="4"}.
:::
```

::: {.exercise}
$\frac1x\geq\frac13$ besitzt die Lösungsmenge
$L$$\;=\;$[]{.question .text #EX_INTERVAL length="14" solution="(0;3]"
precision="3" validation="mathInterval" points="4"}.
:::

#### Spezial (`validation="special"`)

*TODO: was ist das?*

### Checkbox-Aufgabe

Eine weitere Aufgabenform ist die Checkbox- oder auch Multiple-Choice-Aufgabe.
Hier gibt es mehrere anwählbare Optionen, bei denen keine, eine oder mehrere
richtig sein können.

Checkbox-Aufgaben werden durch die Angabe mehrerer Fragen des Typs `checkbox`
realisiert, wobei jede Frage eine einzelne Checkbox ergibt.

Zu Beginn sind die Checkboxen nicht ausgefüllt, also weder ausgewählt noch
nicht ausgewählt.

::: {.exercise}
Sind diese Ungleichungen richtig oder falsch?

------------------------------------------------------------------ ---------------------------------------------------------------
[]{.question .checkbox #EX_CB_1 solution="0" validation="boolean"} $\frac12>1-\frac13$
[]{.question .checkbox #EX_CB_2 solution="1" validation="boolean"} $a^2\geq 2a b-b^2$ (wobei $a$ und $b$ unbekannte Zahlen sind)
[]{.question .checkbox #EX_CB_3 solution="1" validation="boolean"} $\frac12<\frac23<\frac34$
------------------------------------------------------------------ ---------------------------------------------------------------

:::: {.verify-input-button}
Eingabe überprüfen
::::
:::
