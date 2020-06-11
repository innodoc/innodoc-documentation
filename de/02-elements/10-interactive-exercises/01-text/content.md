---
title: Texteingabe
---

Für Texteingabefragen wird ein Eingabefeld angezeigt.

Die Antwort kann auf verschiedene Arten ausgewertet werden (Parameter
`validation`). Außerdem akzeptieren alle Texteingaben den Parameter `length`.

------------ -------------------------------------------------------------
`length`     Maximale Anzahl an Zeichen, die eingegeben werden können.
`validation` Art wie `solution` ausgewertet wird.
------------ -------------------------------------------------------------

## Exakt

> `validation="exact"`

Bei diesem Fragetypen muss der eingetippte Wert exakt der Lösung entsprechen
(Groß-/Kleinschreibung wird beachtet).

::: {.exercise #EX_TEXT_EXACT}
Für die korrekte Beantwortung der Frage muss das Lösungswort *Lösung* exakt
eingegeben werden.

```markdown
Lösungswort: []{.question .text length="10" solution="Lösung" validation="exact" points="3"}
```

Lösungswort: []{.question .text length="10" solution="Lösung" validation="exact" points="3"}
:::

## Geparster Ausdruck

> `validation="parsed"`

Die Eingabe wird als mathematischer Ausdruck interpretiert.

----------- ----------------------------------------------------------------------------------------------------
`precision` Genauigkeit hinter dem Dezimalpunkt (weitere Stellen werden vor dem Vergleich mathematisch gerundet)
----------- ----------------------------------------------------------------------------------------------------

::: {.example}
```
::: {.exercise #EX_PARSED_0}
$\tfrac{\alpha+\beta}{\alpha-\beta}$ nimmt den Wert []{.question .text length="10" solution="5" precision="3" points="4"} an für $\alpha=6$ und $\beta=4$.
:::
```
::: {.exercise #EX_PARSED_0}
$\tfrac{\alpha+\beta}{\alpha-\beta}$ nimmt den Wert []{.question .text length="10" solution="5" precision="3" points="4"} an für $\alpha=6$ und $\beta=4$.
:::
:::

::: {.example}
```
::: {.exercise #EX_PARSED_1}
Formen Sie um und geben Sie die Lösungsmengen dieser linearen Gleichungen an:

[Schreiben Sie einfach `{a}` für eine einelementige Menge und `{}` für die leere Menge.]{.hint-text}

1.  $x-1=1-x$ hat die Lösungsmenge $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="1,1" precision="4" points="4"},

2.  $4x-2=2x+2$ hat die Lösungsmenge $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="2,2" precision="4" points="4"},

3.  $2x-6=2x-10$ hat die Lösungsmenge $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="" precision="4" points="4"}.

:::: {.hint caption="Lösung"}
Die erste Gleichung kann man zu $2x=2$ bzw. $x=1$ umformen, also ist $L=\lbrace 1\rbrace$ die Lösungsmenge. Die zweite Gleichung
kann zu $2x=4$ mit $L=\lbrace 2\rbrace$ umgeformt werden. Die dritte Gleichung kann zu $-6=-10$ umgeformt werden, einer an sich falschen
Aussage mit $L=\lbrace\rbrace$.
::::
:::
```

::: {.exercise #EX_PARSED_1}
Formen Sie um und geben Sie die Lösungsmengen dieser linearen Gleichungen an:

[Schreiben Sie einfach `{a}` für eine einelementige Menge und `{}` für die leere Menge.]{.hint-text}

1.  $x-1=1-x$ hat die Lösungsmenge $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="1,1" precision="4" points="4"},

2.  $4x-2=2x+2$ hat die Lösungsmenge $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="2,2" precision="4" points="4"},

3.  $2x-6=2x-10$ hat die Lösungsmenge $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="" precision="4" points="4"}.

:::: {.hint caption="Lösung"}
Die erste Gleichung kann man zu $2x=2$ bzw. $x=1$ umformen, also ist $L=\lbrace 1\rbrace$ die Lösungsmenge. Die zweite Gleichung
kann zu $2x=4$ mit $L=\lbrace 2\rbrace$ umgeformt werden. Die dritte Gleichung kann zu $-6=-10$ umgeformt werden, einer an sich falschen
Aussage mit $L=\lbrace\rbrace$.
::::
:::
:::

## Funktion

> `validation="function"`

Die Eingabe wird als mathematische Funktion interpretiert. Er wird an einer
Anzahl Stützstellen ausgewertet und mit der Lösung verglichen. Das Ergebnis
muss innerhalb einer konfigurierbaren Distanz (`precision`) richtig sein.

--------------------- --------------------------------------------------------------------------------------
`supporting-points`   Anzahl Stützstellen
`variables`           Funktionsvariablen durch Kommata getrennt (Groß-/Kleinschreibung wird nicht beachtet)
`precision`           Anzahl Nachkommastellen für Vergleich
`simplification`      Spezifische Vereinfachung erforderlich (see [below](#simplification))
--------------------- --------------------------------------------------------------------------------------

### Vereinfachungen {#simplification}

Die Form der Eingabe kann auf verschiedene Vereinfachungen hin überprüft werden.
Um mehrere Vereinfachungen zu fordern, können die Werte durch Kommata getrennt
angegeben werden (z. B. `simplification="no-brackets,no-sqrt"`).

-----------------------------------------------------------------------------------------------------------------------------------------------------
Wert                        Bedingung
--------------------------- -------------------------------------------------------------------------------------------------------------------------
`""` or ausgelassen         Keine Vereinfachung erforderlich.

`no-brackets`               Keine Klammern erlaubt.

`only-one-slash`            Nur ein Schrägstrich (Bruchstrich) erlaubt.

`antiderivative`            Stammfunktion gefordert: Beide Terme werden zu $f(1.234) = 0$ normiert (und nur eine Variable wird angenommen).

`no-sqrt`                   Keine Wurzelfunktion erlaubt (`sqrt(…)`), allerdings ist bspw. `x^(1/2)` weiterhin erlaubt.

`no-abs`                    Keine Betragsfunktion erlaubt (`abs(…)`). Muss als Fallunterscheidung geschrieben werden.

`no-fractions-no-powers`    Keine Brüche und keine Potenzen erlaubt.

`special-support-points`    Besondere Stützstellen (nur $>1$ und schwach rational, sonst symmetrisch um Nullpunkt und ganze Zahlen)

`only-natural-number`       Nur natürliche Zahlen erlaubt.

`one-power-no-mult-or-div`  Nur hoechstens ein `^` und kein `/` und `*` erlaubt.
-----------------------------------------------------------------------------------------------------------------------------------------------------

<!--
NOT IMPLEMENTED BUT 'factor-notation' is actually used in tub_mathe:

`factor-notation`     Faktordarstellung erfordert

`sum-notation`        Summendarstellung erfordert
-->

### Beispiele

::: {.example}
```
:::: {.exercise #EX_FUNCTION_0}
Welcher Term entsteht, wenn man in $x^2+y^2$ Folgendes einsetzt und soweit wie möglich vereinfacht?

1.  Den Winkel $\alpha$ sowohl für $x$ als auch für $y$: Dann ist $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" points="4"}.

2.  Die Zahl $2$ für $y$ und der Term $t+1$ für $x$: Dann ist $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="4+(t+1)^2" supporting-points="5" variables="t" precision="5" points="4"}.

3.  Den Term $z+1$ für $x$ und der Term $z-1$ für $y$: Dann ist $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*z*z+2" supporting-points="5" variables="z" precision="5" points="4"}.

::::: {.hint-text}
Der griechische Buchstabe $\alpha$ kann als `alpha` eingetippt werden.
:::::

::::: {.hint caption="Lösung"}
Am sichersten ist es, die Variablen vor der Termeinsetzung zu klammern, wenn der neue Term mehrere Symbole enthält:

1.  $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$.

2.  $x^2+y^2=(x)^2+y^2=(t+1)^2+2^2=t^2+2t+5$.

3.  $x^2+y^2=(x)^2+(y)^2=(z+1)^2+(z-1)^2=z^2+2z+1+z^2-2z+1=2z^2+2$.
:::::
::::
```

:::: {.exercise #EX_FUNCTION_0}
Welcher Term entsteht, wenn man in $x^2+y^2$ Folgendes einsetzt und soweit wie möglich vereinfacht?

1.  Den Winkel $\alpha$ sowohl für $x$ als auch für $y$: Dann ist $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" points="4"}.

2.  Die Zahl $2$ für $y$ und der Term $t+1$ für $x$: Dann ist $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="4+(t+1)^2" supporting-points="5" variables="t" precision="5" points="4"}.

3.  Den Term $z+1$ für $x$ und der Term $z-1$ für $y$: Dann ist $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*z*z+2" supporting-points="5" variables="z" precision="5" points="4"}.

::::: {.hint-text}
Der griechische Buchstabe $\alpha$ kann als `alpha` eingetippt werden.
:::::

::::: {.hint caption="Lösung"}
Am sichersten ist es, die Variablen vor der Termeinsetzung zu klammern, wenn der neue Term mehrere Symbole enthält:

1.  $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$.

2.  $x^2+y^2=(x)^2+y^2=(t+1)^2+2^2=t^2+2t+5$.

3.  $x^2+y^2=(x)^2+(y)^2=(z+1)^2+(z-1)^2=z^2+2z+1+z^2-2z+1=2z^2+2$.
:::::
::::
:::

::: {.example}
```
::: {.exercise #EX_FUNCTION_1}
Formen Sie in eine Summendarstellung um:
$a\cdot(b+c)+c\cdot(a+b)$$\;\;=\;$[]{.question .text validation="function" length="20" solution="a*(b+c)+c*(a+b)" supporting-points="3" variables="a,b,c" precision="3" simplification="no-brackets" points="4"}.

:::: {.hint caption="Lösung"}
$$a\cdot(b+c)+c\cdot(a+b) \;=\; a b + a c + c a + c b \;=\; a b + 2 a c + b c$$
::::
:::
```

:::: {.exercise #EX_FUNCTION_1}
Formen Sie in eine Summendarstellung um:
$a\cdot(b+c)+c\cdot(a+b)$$\;\;=\;$[]{.question .text validation="function" length="20" solution="a*(b+c)+c*(a+b)" supporting-points="3" variables="a,b,c" precision="3" simplification="no-brackets" points="4"}.

::::: {.hint caption="Lösung"}
$$a\cdot(b+c)+c\cdot(a+b) \;=\; a b + a c + c a + c b \;=\; a b + 2 a c + b c$$
:::::
::::
:::

::: {.example}
```
::: {.exercise #EX_FUNCTION_2}
Schreiben Sie diesen Potenz- und Wurzelausdruck als einfache Potenz mit einem rationalen Exponenten:

$\dfrac{x^3}{\left({\sqrt{x}}\right)^3}$$\;\;=\;$[]{.question .text validation="function" length="25" solution="x^(3/2)" supporting-points="10" variables="x" precision="5" simplification="one-power-no-mult-or-div,special-support-points" points="4"}.

[Beispielsweise tippen Sie $\sqrt{x}\cdot x^2$ = `x^(5/2)` oder auch `x^(2.5)`, vergessen Sie die Klammern um den Bruch nicht.]{.hint-text}

:::: {.hint caption="Lösung"}
$$x^{\frac32}$$
::::
:::
```

:::: {.exercise #EX_FUNCTION_2}
Schreiben Sie diesen Potenz- und Wurzelausdruck als einfache Potenz mit einem rationalen Exponenten:

$\dfrac{x^3}{\left({\sqrt{x}}\right)^3}$$\;\;=\;$[]{.question .text validation="function" length="25" solution="x^(3/2)" supporting-points="10" variables="x" precision="5" simplification="one-power-no-mult-or-div,special-support-points" points="4"}.

[Beispielsweise tippen Sie $\sqrt{x}\cdot x^2$ = `x^(5/2)` oder auch `x^(2.5)`, vergessen Sie die Klammern um den Bruch nicht.]{.hint-text}

::::: {.hint caption="Lösung"}
$$x^{\frac32}$$
:::::
::::
:::

## Interval

> `validation="interval"`

Die Eingabe wird als Intervall interpretiert.

------------------- ----------------------------------
`precision`         Genauigkeit der Zahlenwertprüfung
------------------- ----------------------------------

::: {.example}
```
::: {.exercise #EX_INTERVAL}
Wie lautet die Lösungsmenge für die gemischte Gleichung $|x-3|\cdot x=9$?

Ist $x$ aus dem Intervall
[]{.question .text validation="interval" length="14" solution="[3,infty)" precision="5" points="4"},
so ist der Term im Betrag nicht negativ.
:::

::: {.hint caption="Lösung"}
Ist $x$ aus dem Intervall $\left[3; \infty\right[$, so ist der Term im Betrag
nicht negativ.

Lösung: `[3;infty)`.
:::
```

:::: {.exercise #EX_INTERVAL}
Wie lautet die Lösungsmenge für die gemischte Gleichung $|x-3|\cdot x=9$?

Ist $x$ aus dem Intervall
[]{.question .text validation="interval" length="14" solution="[3,infty)" precision="5" points="4"},
so ist der Term im Betrag nicht negativ.
::::

:::: {.hint caption="Lösung"}
Ist $x$ aus dem Intervall $\left[3; \infty\right[$, so ist der Term im Betrag
nicht negativ.

Lösung: `[3,infty)`.
::::
:::

## Exakter Bruch

> `validation="exact-fraction"`

Input must be equivalent to the solution, irreducible and with positive
denominator.

::: {.example}
```
::: {.exercise #EX_EXACT_FRACTION}
Berechnen Sie die folgenden Zahlenwerte, indem Sie den Hauptnenner bilden und
soweit wie möglich kürzen:

1.  $\dfrac12+\dfrac13$$\;\;=\;$[]{.question .text validation="exact-fraction" length="10" solution="5/6" precision="5" points="4"} aber $\dfrac1{2+3}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="1/5" precision="5" points="4"}.

2.  $\dfrac{1+2}{5+6}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="3/11" precision="5" points="4"} aber $\dfrac15+\dfrac26$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="8/15" precision="5" points="4"}.

:::: {.hint caption="Lösung"}
Summen von Nennern darf man nicht zusammenfassen, auch nicht bei gleichem Zähler, hier ist

$$\dfrac12+\dfrac13\;=\; \dfrac{3}{6}+\dfrac26 \;=\; \dfrac56\;\;\text{aber}\;\;\dfrac{1}{2+3} \;=\; \dfrac15\, .$$

Auch das einfache „Auseinandernehmen" von Bestandteilen der Brüche ist nicht erlaubt, hier ist

$$\dfrac{1+2}{5+6} \;=\; \dfrac{3}{11}  \;\;\text{aber}\;\; \dfrac15+\dfrac26 \;=\; \dfrac{6}{30}+\dfrac{10}{30} \;=\; \dfrac{16}{30}\;=\; \dfrac{8}{15}\, .$$
::::
:::
```

:::: {.exercise #EX_EXACT_FRACTION}
Berechnen Sie die folgenden Zahlenwerte, indem Sie den Hauptnenner bilden und
soweit wie möglich kürzen:

1.  $\dfrac12+\dfrac13$$\;\;=\;$[]{.question .text validation="exact-fraction" length="10" solution="5/6" precision="5" points="4"} aber $\dfrac1{2+3}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="1/5" precision="5" points="4"}.

2.  $\dfrac{1+2}{5+6}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="3/11" precision="5" points="4"} aber $\dfrac15+\dfrac26$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="8/15" precision="5" points="4"}.

::::: {.hint caption="Lösung"}
Summen von Nennern darf man nicht zusammenfassen, auch nicht bei gleichem Zähler, hier ist

$$\dfrac12+\dfrac13\;=\; \dfrac{3}{6}+\dfrac26 \;=\; \dfrac56\;\;\text{aber}\;\;\dfrac{1}{2+3} \;=\; \dfrac15\, .$$

Auch das einfache „Auseinandernehmen" von Bestandteilen der Brüche ist nicht erlaubt, hier ist

$$\dfrac{1+2}{5+6} \;=\; \dfrac{3}{11}  \;\;\text{aber}\;\; \dfrac15+\dfrac26 \;=\; \dfrac{6}{30}+\dfrac{10}{30} \;=\; \dfrac{16}{30}\;=\; \dfrac{8}{15}\, .$$
:::::
::::
:::
