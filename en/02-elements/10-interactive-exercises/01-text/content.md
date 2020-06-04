---
title: Text input
---

An input field is presented for text input questions.

The answer can be evaluated in different ways (parameter `validation`).
Furthermore all text inputs accept the parameter `length`.

------------ ------------------------------------------------------
`length`     The maximum number of characters that can be entered.
`validation` How `solution` is evaluated.
------------ ------------------------------------------------------

## Exact

> `validation="exact"`

For this type of question, the entered value must match the solution character
by character (case-sensitive).

::: {.exercise #EX_TEXT_EXACT}
For the correct answer of the question the word *solution* must be entered
exactly.

```markdown
Solution: []{.question .text length="10" solution="solution" validation="exact" points="3"}
```

Solution: []{.question .text length="10" solution="solution" validation="exact" points="3"}
:::

## Parsed expression

> `validation="parsed"`

The input is interpreted as a mathematical expression.

----------- ----------------------------------------------------------------------------------------------------
`precision` Accuracy behind the decimal point (further digits are mathematically rounded before comparison)
----------- ----------------------------------------------------------------------------------------------------

::: {.example}
```
::: {.exercise #EX_PARSED_0}
$\tfrac{\alpha+\beta}{\alpha-\beta}$ takes the value []{.question .text validation="parsed" length="10" solution="5" precision="3" points="4"} for $\alpha=6$ and $\beta=4$.
:::
```
::: {.exercise #EX_PARSED_0}
$\tfrac{\alpha+\beta}{\alpha-\beta}$ takes the value []{.question .text validation="parsed" length="10" solution="5" precision="3" points="4"} for $\alpha=6$ and $\beta=4$.
:::
:::

::: {.example}
```
::: {.exercise #EX_PARSED_1}
Transform the following linear equations and specify their solution sets:

[Enter simply `{a}` for a unit set and `{}` for an empty set.]{.hint-text}

1.  The equation $x-1=1-x$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="1,1" precision="4" points="4"},

2.  The equation $4x-2=2x+2$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="2,2" precision="4" points="4"},

3.  The equation $2x-6=2x-10$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="" precision="4" points="4"}.

:::: {.hint caption="Solution"}
The first equation can be transformed into $2x=2$ or $x=1$, respectively, so
the solution set is $L=\lbrace 1\rbrace$. The second equation can be transformed into $2x=4$ and the solution set is
$L=\lbrace 2\rbrace$. The third equation can be transformed into $-6=-10$ which is a false statement,
hence $L=\lbrace\rbrace$.
::::
:::
```

::: {.exercise #EX_PARSED_1}
Transform the following linear equations and specify their solution sets:

[Enter simply `{a}` for a unit set and `{}` for an empty set.]{.hint-text}

1.  The equation $x-1=1-x$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="1,1" precision="4" points="4"},

2.  The equation $4x-2=2x+2$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="2,2" precision="4" points="4"},

3.  The equation $2x-6=2x-10$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="" precision="4" points="4"}.

:::: {.hint caption="Solution"}
The first equation can be transformed into $2x=2$ or $x=1$, respectively, so
the solution set is $L=\lbrace 1\rbrace$. The second equation can be transformed into $2x=4$ and the solution set is
$L=\lbrace 2\rbrace$. The third equation can be transformed into $-6=-10$ which is a false statement,
hence $L=\lbrace\rbrace$.
::::
:::
:::

## Function

> `validation="function"`

The input is interpreted as a mathematical function.

--------------------- ------------------------------------------------------------------
`supporting-points`   Number of support points
`variables`           Function variables separated by comma (not case-sensitive)
`precision`           Number of decimal places for comparison
`simplification-code` TODO
--------------------- ------------------------------------------------------------------

TODO: `simplification-code` table

::: {.example}
```
::: {.exercise #EX_FUNCTION_0}
Which term is formed if the following object is inserted into the term $x^2+y^2$?

1.  The angle $\alpha$ both for $x$ and $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" points="4"}.

2.  The number $2$ for $y$ and the term $t+1$ for $x$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="4+(t+1)^2" supporting-points="5" variables="t" precision="5" points="4"}.

3.  The term $z+1$ for $x$ and the term $z-1$ for $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*z*z+2" supporting-points="5" variables="z" precision="5" points="4"}.

:::: {.hint-text}
The Greek letter $\alpha$ can be entered as `alpha`.
::::

:::: {.hint caption="Solution"}
It is safest to bracket the variables before inserting, if the new term contains several symbols:

1.  $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$.

2.  $x^2+y^2=(x)^2+y^2=(t+1)^2+2^2=t^2+2t+5$.

3.  $x^2+y^2=(x)^2+(y)^2=(z+1)^2+(z-1)^2=z^2+2z+1+z^2-2z+1=2z^2+2$.
::::
:::
```

:::: {.exercise #EX_FUNCTION_0}
Which term is formed if the following object is inserted into the term $x^2+y^2$?

1.  The angle $\alpha$ both for $x$ and $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" points="4"}.

2.  The number $2$ for $y$ and the term $t+1$ for $x$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="4+(t+1)^2" supporting-points="5" variables="t" precision="5" points="4"}.

3.  The term $z+1$ for $x$ and the term $z-1$ for $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*z*z+2" supporting-points="5" variables="z" precision="5" points="4"}.

::::: {.hint-text}
The Greek letter $\alpha$ can be entered as `alpha`.
:::::

::::: {.hint caption="Solution"}
It is safest to bracket the variables before inserting, if the new term contains several symbols:

1.  $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$.

2.  $x^2+y^2=(x)^2+y^2=(t+1)^2+2^2=t^2+2t+5$.

3.  $x^2+y^2=(x)^2+(y)^2=(z+1)^2+(z-1)^2=z^2+2z+1+z^2-2z+1=2z^2+2$.
:::::
::::
:::

::: {.example}
```
::: {.exercise #EX_FUNCTION_1}
Transform into a sum:
$a\cdot(b+c)+c\cdot(a+b)$$\;\;=\;$[]{.question .text validation="function" length="20" solution="a*(b+c)+c*(a+b)" supporting-points="3" variables="a,b,c" precision="3" simplification-code="1" points="4"}.

:::: {.hint caption="Solution"}
$$a\cdot(b+c)+c\cdot(a+b) \;=\; a b + a c + c a + c b \;=\; a b + 2 a c + b c$$
::::
:::
```

:::: {.exercise #EX_FUNCTION_1}
Transform into a sum:
$a\cdot(b+c)+c\cdot(a+b)$$\;\;=\;$[]{.question .text validation="function" length="20" solution="a*(b+c)+c*(a+b)" supporting-points="3" variables="a,b,c" precision="3" simplification-code="1" points="4"}.

::::: {.hint caption="Solution"}
$$a\cdot(b+c)+c\cdot(a+b) \;=\; a b + a c + c a + c b \;=\; a b + 2 a c + b c$$
:::::
::::
:::

::: {.example}
```
::: {.exercise #EX_FUNCTION_2}
Rewrite the following expression containing powers and roots as a simple power with a rational exponent:

$\dfrac{x^3}{\left({\sqrt{x}}\right)^3}$$\;\;=\;$[]{.question .text validation="function" length="25" solution="x^(3/2)" supporting-points="10" variables="x" precision="5" simplification-code="576" points="4"}.

[For example, enter $\sqrt{x}\cdot x^2$ = `x^(5/2)` or alternatively as `x^(2.5)`, mind the brackets around the fraction.]{.hint-text}

:::: {.hint caption="Solution"}
$$x^{1.5}$$
::::
:::
```

:::: {.exercise #EX_FUNCTION_2}
Rewrite the following expression containing powers and roots as a simple power with a rational exponent:

$\dfrac{x^3}{\left({\sqrt{x}}\right)^3}$$\;\;=\;$[]{.question .text validation="function" length="25" solution="x^(3/2)" supporting-points="10" variables="x" precision="5" simplification-code="576" points="4"}.

[For example, enter $\sqrt{x}\cdot x^2$ = `x^(5/2)` or alternatively as `x^(2.5)`, mind the brackets around the fraction.]{.hint-text}

::::: {.hint caption="Solution"}
$$x^{1.5}$$
:::::
::::
:::

## Interval

> `validation="interval"`

The input is interpreted as an interval.

------------------- --------------------------------------
`precision`         Accuracy of the numerical value check
------------------- --------------------------------------

::: {.example}
```
::: {.exercise #EX_INTERVAL}
Find the solution set of the mixed equation $|x-3|\cdot x=9$.

If $x$ is in the interval
[]{.question .text validation="interval" length="14" solution="[3,infty)" precision="5" points="4"}
the absolute value term is non-negative.
:::

::: {.hint caption="Solution"}
If $x$ is in the interval $\left[3; \infty\right[$ (`[3,infty)`) the absolute
value term is non-negative.
:::
```

:::: {.exercise #EX_INTERVAL}
Find the solution set of the mixed equation $|x-3|\cdot x=9$.

If $x$ is in the interval
[]{.question .text validation="interval" length="14" solution="[3,infty)" precision="5" points="4"}
the absolute value term is non-negative.
::::

:::: {.hint caption="Solution"}
If $x$ is in the interval $\left[3; \infty\right[$ the absolute value term is
non-negative.

Type `[3,infty)`.
::::
:::

## Exact fraction

> `validation="exact-fraction"`

Die Eingabe muss äquivalent zur Lösung, maximal gekürzt sein und einen
positiven Nenner haben.

------------------- --------------------------------------
`precision`         Accuracy of the numerical value check
------------------- --------------------------------------

::: {.example}
```
::: {.exercise #EX_EXACT_FRACTION}
Calculate the following numbers by finding the least common denominator and
reducing as much as possible:

1.  $\dfrac12+\dfrac13$$\;\;=\;$[]{.question .text validation="exact-fraction" length="10" solution="5/6" precision="5" points="4"} but $\dfrac1{2+3}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="1/5" precision="5" points="4"}.

2.  $\dfrac{1+2}{5+6}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="3/11" precision="5" points="4"} but $\dfrac15+\dfrac26$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="8/15" precision="5" points="4"}.

:::: {.hint caption="Solution"}
Sums of denominators may not be collected, not even in the case of like numerators. Here, we have

$$\dfrac12+\dfrac13\;=\; \dfrac{3}{6}+\dfrac26 \;=\; \dfrac56\;\;\text{but}\;\;\dfrac{1}{2+3} \;=\; \dfrac15\, .$$

Also, the simple "splitting" of fraction parts is not allowed, here we have

$$\dfrac{1+2}{5+6} \;=\; \dfrac{3}{11}  \;\;\text{but}\;\; \dfrac15+\dfrac26 \;=\; \dfrac{6}{30}+\dfrac{10}{30} \;=\; \dfrac{16}{30}\;=\; \dfrac{8}{15}\, .$$
::::
:::
```

:::: {.exercise #EX_EXACT_FRACTION}
Calculate the following numbers by finding the least common denominator and
reducing as much as possible:

1.  $\dfrac12+\dfrac13$$\;\;=\;$[]{.question .text validation="exact-fraction" length="10" solution="5/6" precision="5" points="4"} but $\dfrac1{2+3}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="1/5" precision="5" points="4"}.

2.  $\dfrac{1+2}{5+6}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="3/11" precision="5" points="4"} but $\dfrac15+\dfrac26$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="8/15" precision="5" points="4"}.

::::: {.hint caption="Solution"}
Sums of denominators may not be collected, not even in the case of like numerators. Here, we have

$$\dfrac12+\dfrac13\;=\; \dfrac{3}{6}+\dfrac26 \;=\; \dfrac56\;\;\text{but}\;\;\dfrac{1}{2+3} \;=\; \dfrac15\, .$$

Also, the simple "splitting" of fraction parts is not allowed, here we have

$$\dfrac{1+2}{5+6} \;=\; \dfrac{3}{11}  \;\;\text{but}\;\; \dfrac15+\dfrac26 \;=\; \dfrac{6}{30}+\dfrac{10}{30} \;=\; \dfrac{16}{30}\;=\; \dfrac{8}{15}\, .$$
:::::
::::
:::
