---
title: Interactive exercises
---

Interactive exercises are enclosed in an `exercise` box. Within the box one or
more question elements are placed.

Also an ID needs to be added per exercise. The ID has to be unique within the
document. It can be used to reference questions from other parts of the course.

**Markdown**

```markdown
::: {.exercise #EX_DUMMY}
[CONTENT]
:::
```

**Result**

::: {.exercise #EX_DUMMY}
[CONTENT]
:::

The box typically includes the exercise text and one or more questions.
Optionally, hints, the solution, a button for checking the answer and other
content can be presented.

The total achievable score of an exercise is the sum of the points of all the
containing questions.

::::: {.example}
Below is a complete example of an exercise.

**Markdown**

```markdown
:::: {.exercise #EX_FULL}
Which term is formed if the following object is inserted into the term
$x^2+y^2$?

The angle $\alpha$ both for $x$ and $y$: Then
$x^2+y^2$$\;\;=\;$[]{.question .text length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" validation="mathExpression" points="4"}.

::: {.hint-text}
The Greek letter $\alpha$ can be entered as `alpha`.
:::

::: {.hint}
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
:::
::::
```

**Result**

:::: {.exercise #EX_FULL}
Which term is formed if the following object is inserted into the term
$x^2+y^2$?

The angle $\alpha$ both for $x$ and $y$: Then
$x^2+y^2$$\;\;=\;$[]{.question .text length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" validation="mathExpression" points="4"}.

::: {.hint-text}
The Greek letter $\alpha$ can be entered as `alpha`.
:::

::: {.hint}
$x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
:::
::::
:::::

## Structure of a question

An `exercise` box can contain one or more questions. A question is specified by
the class `question` and the question type (e. g. `text`). In addition, some
question types have specific parameters.

```markdown
[]{.question .text parameter1=value1 parameter2=value2}
```

The rest of this section discusses different types of questions and their
parameters.

## Question types

Currently two types of questions are implemented: `text` and `checkbox`. They
are described in the subsections
[](/section/02-elements/07-interactive-exercises/01-text) and
[](/section/02-elements/07-interactive-exercises/02-checkbox).

The following parameters are common to all question types.

------------------- -----------------------------------------------------------
`solution`          The solution.

`validation`        Type of verification.

`points`            Achievable points if the answer is correct.
------------------- -----------------------------------------------------------
