---
title: Interactive exercises
---

Interactive exercises are enclosed in an `exercise` box. Within the box one or
more question elements are placed.

Also an ID needs to be added per exercise. The ID has to be unique within the
document. It can be used to reference questions from other parts of the course.

<Tabs>
  <TabItem label="Result">
    <Exercise id="ex-dummy">
      [CONTENT]
    </Exercise>
  </TabItem>
  <TabItem label="Markdown">
    ```markdown
    <Exercise id="ex-dummy">
      [CONTENT]
    </Exercise>
    ```
  </TabItem>
</Tabs>

The box typically includes the exercise text and one or more questions.
Optionally, hints, the solution, a button for checking the answer and other
content can be presented.

The total achievable score of an exercise is the sum of the points of all the
containing questions.

<Example>
  Below is a complete example of an exercise.

  <Tabs>
    <TabItem label="Result">
      <Exercise id="ex-full">
        Which term is formed if the following object is inserted into the term
        $x^2+y^2$?

        The angle $\alpha$ both for $x$ and $y$: Then $x^2+y^2\;=\;$ <TextQuestion length="13" points="4" precision="5" solution="2*alpha^2" supporting-points="5" validation="mathExpression" variables="alpha" />

        <InputHint>
          The Greek letter $\alpha$ can be entered as `alpha`.
        </InputHint>

        <Solution>
          $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
        </Solution>
      </Exercise>
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      <Exercise id="ex-full">
        Which term is formed if the following object is inserted into the term
        $x^2+y^2$?

        The angle $\alpha$ both for $x$ and $y$: Then $x^2+y^2\;=\;$ <TextQuestion length="13" points="4" precision="5" solution="2*alpha^2" supporting-points="5" validation="mathExpression" variables="alpha" />

        <InputHint>
          The Greek letter $\alpha$ can be entered as `alpha`.
        </InputHint>

        <Solution>
          $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$
        </Solution>
      </Exercise>
      ```
    </TabItem>
  </Tabs>
</Example>

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

| Parameter    | Description                                 |
|--------------|---------------------------------------------|
| `solution`   | The solution                                |
| `validation` | Type of verification                        |
| `points`     | Achievable points if the answer is correct  |
