---
title: Interactive exercises
---

Content can include interactive exercises. Tasks should be enclosed in an
`exercise` box.

```markdown
::: {.exercise}
[CONTENT]
:::
```

::: {.exercise}
[CONTENT]
:::

::: {.example}
The text box typically includes the exercise text and one or more questions.
Optionally, hints, the solution, a button for checking the answer or other
content can be presented.

```markdown
::: {.exercise}
Which term is formed if the following object is inserted into the term
$x^2+y^2$?

The angle $\alpha$ both for $x$ and $y$: Then
$x^2+y^2$$\;\;=\;$[]{.question .text #EX_EXAMPLE length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" validation="mathFormula" points="4"}.

:::: {.hint-text}
The Greek letter $\alpha$ can be entered as `alpha`.
::::

:::: {.hint}
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
::::
:::
```

::: {.exercise}
Which term is formed if the following object is inserted into the term
$x^2+y^2$?

The angle $\alpha$ both for $x$ and $y$: Then
$x^2+y^2$$\;\;=\;$[]{.question .text #EX_EXAMPLE length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" validation="mathFormula" points="4"}.

:::: {.hint-text}
The Greek letter $\alpha$ can be entered as `alpha`.
::::

:::: {.hint}
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
::::
:::
:::

## Aufbau einer Frage

An `exercise` box can contain one or more questions. A question is specified by
the class `question` and the question type (e. g. `text`).

Also an ID needs to be added per question. The ID has to be unique within the
document. It can be used to reference questions from other parts of the work.

In addition, some question types have specific parameters.

```markdown
[]{.question .text #ID parameter1=value1 parameter2=value2}
```

The rest of this chapter is devoted to the different types of questions and
their parameters.

## Question types

All types accept the following parameters:

------------------- -----------------------------------------------------------
`solution`          The correct solution. (Is interpreted differently depending
                    on the parameter `validation`.)

`validation`        Type of verification of the entered solution.

`points`            The number of achievable points if the answer is correct.

`supporting-points` *TODO: What is it?*
------------------- -----------------------------------------------------------

### Text input (`.text`)

An input field is presented for text input questions. It exists in different
variants. These differ in the way the solution is checked, controlled by the
parameter `validation`.

All text input variants accept the parameter `length`.

--------- -----------------------------------------------------
`length`  The maximum number of characters that can be entered.
--------- -----------------------------------------------------

#### Exact (`validation="exact"`)

For this type of question, the entered value must match the solution character
by character.

::: {.example}
For the correct answer of the question the word *solution* must be entered
exactly.

```markdown
Solution: []{.question .text #EX_EXACT length="10" solution="solution"
validation="exact"}
```

Solution: []{.question .text #EX_EXACT length="10" solution="solution"
validation="exact"}
:::

#### Mathematical expression (`validation="mathExpression"`)

The input is interpreted as a mathematical expression.

*TODO: Erklärung, mehr Beispiele, Parameter*

```
::: {.exercise}
Use the round function to calculate the rounding of pi to 4 decimal places:

$\overline{\pi}\;=\;$[]{.question .text #EX_EXPR length="16"
solution="3.1416" precision="7" validation="mathExpression" points="4"}.
:::
```

::: {.exercise}
Use the round function to calculate the rounding of pi to 4 decimal places:

$\overline{\pi}\;=\;$[]{.question .text #EX_EXPR length="16"
solution="3.1416" precision="7" validation="mathExpression" points="4"}.
:::

#### Simplification of a mathematical term (`validation="mathSimplify"`)

A mathematical term must be simplified for this question type.

*TODO: Erklärung, mehr Beispiele, Parameter*

```
::: {.exercise}
Simplify the term:

$(x-3)(x+3)\;=\;$[]{.question .text #EX_SIMPLIFY length="14"
solution="(x-3)*(x+3)" supporting-points="10" variables="x" precision="5"
simplification-code="1" validation="mathSimplify"}
:::
```

::: {.exercise}
Simplify the term:

$(x-3)(x+3)\;=\;$[]{.question .text #EX_SIMPLIFY length="14"
solution="(x-3)*(x+3)" supporting-points="10" variables="x" precision="5"
simplification-code="1" validation="mathSimplify"}
:::

#### Mathematical function (`validation="mathFunction"`)

A mathematical function must be specified for this question type.

*TODO: Erklärung, mehr Beispiele, Parameter*

```
::: {.exercise}
Give the linear equation:

$y\;=\;$[]{.question .text #EX_FUNC length="15" solution="-1+x"
supporting-points="2" variables="x" precision="5" validation="mathFunction"
points="4"}
:::
```

::: {.exercise}
Give the linear equation:

$y\;=\;$[]{.question .text #EX_FUNC length="15" solution="-1+x"
supporting-points="2" variables="x" precision="5" validation="mathFunction"
points="4"}
:::

#### Interval (`validation="mathInterval"`)

This question type requires the user to specify an interval.

*TODO: Erklärung, mehr Beispiele, Parameter*

```
::: {.exercise}
$\frac1x\geq\frac13$ has the solution set
$L$$\;=\;$[]{.question .text #EX_INTERVAL length="14" solution="(0;3]"
precision="3" validation="mathInterval" points="4"}.
:::
```

::: {.exercise}
$\frac1x\geq\frac13$ has the solution set
$L$$\;=\;$[]{.question .text #EX_INTERVAL length="14" solution="(0;3]"
precision="3" validation="mathInterval" points="4"}.
:::

#### Special (`validation="special"`)

*TODO: was ist das?*

### Checkbox question

Another type of exercise is the checkbox or *multiple response* task. Several
selectable options are presented where zero, one or multiple can be correct.

Checkbox exercises have several questions of type `checkbox`. One for each
checkbox that is displayed.

At the beginning, the checkbox are not filled in, i. e. meaning neither
selected nor not selected.

::: {.exercise}
Are the following inequalities true or false?

------------------------------------------------------------------ -----------------------------------------------------------
[]{.question .checkbox #EX_CB_1 solution="0" validation="boolean"} $\frac12>1-\frac13$
[]{.question .checkbox #EX_CB_2 solution="1" validation="boolean"} $a^2\geq 2a b-b^2$ (where $a$ and $b$ are unknown numbers)
[]{.question .checkbox #EX_CB_3 solution="1" validation="boolean"} $\frac12<\frac23<\frac34$
------------------------------------------------------------------ -----------------------------------------------------------

:::: {.verify-input-button}
Check input
::::
:::
