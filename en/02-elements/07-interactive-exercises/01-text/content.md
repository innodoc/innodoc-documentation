---
title: Text input
type: exercises
---

An input field is presented for text input questions.

The answer can be evaluated in different ways (parameter `validation`).
Furthermore all text inputs accept the parameter `length`.

| Parameter    | Description                                          |
|--------------|------------------------------------------------------|
| `length`     | The maximum number of characters that can be entered |
| `validation` | How `solution` is evaluated                          |

## Exact

> `validation="exact"`

For this type of question, the entered value must match the solution character
by character (case-sensitive).

<Exercise id="ex-text-exact">
  For the correct answer of the question the word *solution* must be entered
  exactly.

  ```markdown
  Solution: []{.question .text length="10" solution="solution" validation="exact" points="3"}
  ```

  Solution: []{.question .text length="10" solution="solution" validation="exact" points="3"}
</Exercise>

## Parsed expression

> `validation="parsed"`

The input is interpreted as a mathematical expression.

| Parameter   | Description                                                                                     |
|-------------|-------------------------------------------------------------------------------------------------|
| `precision` | Accuracy behind the decimal point (further digits are mathematically rounded before comparison) |

<Example>
  ```
  <Exercise id="ex-parsed-0">
    $\tfrac{\alpha+\beta}{\alpha-\beta}$ takes the value []{.question .text validation="parsed" length="10" solution="5" precision="3" points="4"} for $\alpha=6$ and $\beta=4$.
  </Exercise>
  ```

  <Exercise id="ex-parsed-0">
    $\tfrac{\alpha+\beta}{\alpha-\beta}$ takes the value []{.question .text validation="parsed" length="10" solution="5" precision="3" points="4"} for $\alpha=6$ and $\beta=4$.
  </Exercise>
</Example>

<Example>
  ```
  <Exercise id="ex-parsed-1">
    Transform the following linear equations and specify their solution sets:

    [Enter simply `{a}` for a unit set and `{}` for an empty set.]{.hint-text}

    1.  The equation $x-1=1-x$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="1,1" precision="4" points="4"},

    2.  The equation $4x-2=2x+2$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="2,2" precision="4" points="4"},

    3.  The equation $2x-6=2x-10$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="" precision="4" points="4"}.

    <Solution>
      The first equation can be transformed into $2x=2$ or $x=1$, respectively, so
      the solution set is $L=\lbrace 1\rbrace$. The second equation can be transformed into $2x=4$ and the solution set is
      $L=\lbrace 2\rbrace$. The third equation can be transformed into $-6=-10$ which is a false statement,
      hence $L=\lbrace\rbrace$.
    </Solution>
  </Exercise>
  ```

  <Exercise id="ex-parsed-1">
    Transform the following linear equations and specify their solution sets:

    [Enter simply `{a}` for a unit set and `{}` for an empty set.]{.hint-text}

    1.  The equation $x-1=1-x$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="1,1" precision="4" points="4"},

    2.  The equation $4x-2=2x+2$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="2,2" precision="4" points="4"},

    3.  The equation $2x-6=2x-10$ has the solution set $L$$\;\;=\;$[]{.question .text validation="parsed" length="4" solution="" precision="4" points="4"}.

    <Solution>
      The first equation can be transformed into $2x=2$ or $x=1$, respectively, so
      the solution set is $L=\lbrace 1\rbrace$. The second equation can be transformed into $2x=4$ and the solution set is
      $L=\lbrace 2\rbrace$. The third equation can be transformed into $-6=-10$ which is a false statement,
      hence $L=\lbrace\rbrace$.
    </Solution>
  </Exercise>
</Example>

## Function

> `validation="function"`

The input is interpreted as a mathematical function. It is evaluated at a number
of supporting points and compared to the solution. The results must be correct
within a configurable margin (`precision`).

| Parameter           | Description                                                    |
|---------------------|----------------------------------------------------------------|
| `supporting-points` | Number of support points                                       |
| `variables`         | Function variables separated by comma (not case-sensitive)     |
| `precision`         | Number of decimal places for comparison                        |
| `simplicification`  | Require specific simplification (see [below](#simplification)) |

### Require simplification {#simplification}

It is possible to require certain simplifications for the input to be accepted
as correct. Multiple simplifications can be specified by separating the values
with a comma (e. g. `simplification="no-brackets,no-sqrt"`).

| Value                      | Requirement                                                                                                              |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------|
| `""` or omitted            | No simplification required                                                                                               |
| `no-brackets`              | No brackets allowed                                                                                                      |
| `only-one-slash`           | Only one slash (fraction line) allowed                                                                                   |
| `antiderivative`           | Antiderivative requested: Normalize both terms to $f(1.234) = 0$ (and assume its just one variable)                      |
| `no-sqrt`                  | No root expression allowed (`sqrt(…)`). Note that e. g. `x^(1/2)` can still be used                                      |
| `no-abs`                   | No absolute value allowed (`abs(…)`). Individual cases needs to be written down                                          |
| `no-fractions-no-powers`   | No fractions or powers allowed                                                                                           |
| `special-support-points`   | Special support points requested: only positive ones and weakly rational, separate variables get separate support points |
| `only-natural-number`      | Only natural number allowed.                                                                                             |
| `one-power-no-mult-or-div` | At most one `^` and neither `/` nor `*` allowed                                                                          |

<!--
NOT IMPLEMENTED BUT 'factor-notation' is actually used in tub_mathe:

`factor-notation`     Require linear factor notation

`sum-notation`        Require summation notation
-->

### Examples

<Example>
  ```
  <Exercise id="ex-function-0">
    Which term is formed if the following object is inserted into the term $x^2+y^2$?

    1.  The angle $\alpha$ both for $x$ and $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" points="4"}.

    2.  The number $2$ for $y$ and the term $t+1$ for $x$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="4+(t+1)^2" supporting-points="5" variables="t" precision="5" points="4"}.

    3.  The term $z+1$ for $x$ and the term $z-1$ for $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*z*z+2" supporting-points="5" variables="z" precision="5" points="4"}.

    <InputHint>
      The Greek letter $\alpha$ can be entered as `alpha`.
    </InputHint>

    <Solution>
      It is safest to bracket the variables before inserting, if the new term contains several symbols:

      1.  $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$.

      2.  $x^2+y^2=(x)^2+y^2=(t+1)^2+2^2=t^2+2t+5$.

      3.  $x^2+y^2=(x)^2+(y)^2=(z+1)^2+(z-1)^2=z^2+2z+1+z^2-2z+1=2z^2+2$.
    </Solution>
  </Exercise>
  ```

  <Exercise id="ex-function-0">
    Which term is formed if the following object is inserted into the term $x^2+y^2$?

    1.  The angle $\alpha$ both for $x$ and $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*alpha^2" supporting-points="5" variables="alpha" precision="5" points="4"}.

    2.  The number $2$ for $y$ and the term $t+1$ for $x$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="4+(t+1)^2" supporting-points="5" variables="t" precision="5" points="4"}.

    3.  The term $z+1$ for $x$ and the term $z-1$ for $y$: Then $x^2+y^2$$\;\;=\;$[]{.question .text validation="function" length="13" solution="2*z*z+2" supporting-points="5" variables="z" precision="5" points="4"}.

    <InputHint>
      The Greek letter $\alpha$ can be entered as `alpha`.
    </InputHint>

    <Solution>
      It is safest to bracket the variables before inserting, if the new term contains several symbols:

      1.  $x^2+y^2=\alpha^2+\alpha^2=2\alpha^2$.

      2.  $x^2+y^2=(x)^2+y^2=(t+1)^2+2^2=t^2+2t+5$.

      3.  $x^2+y^2=(x)^2+(y)^2=(z+1)^2+(z-1)^2=z^2+2z+1+z^2-2z+1=2z^2+2$.
    </Solution>
  </Exercise>
</Example>

<Example>
  ```
  <Exercise id="ex-function-1">
    Transform into a sum:
    $a\cdot(b+c)+c\cdot(a+b)$$\;\;=\;$[]{.question .text validation="function" length="20" solution="a*(b+c)+c*(a+b)" supporting-points="3" variables="a,b,c" precision="3" simplification="no-brackets" points="4"}.

    <Solution>
      $$a\cdot(b+c)+c\cdot(a+b) \;=\; a b + a c + c a + c b \;=\; a b + 2 a c + b c$$
    </Solution>
  </Exercise>
  ```

  <Exercise id="ex-function-1">
    Transform into a sum:
    $a\cdot(b+c)+c\cdot(a+b)$$\;\;=\;$[]{.question .text validation="function" length="20" solution="a*(b+c)+c*(a+b)" supporting-points="3" variables="a,b,c" precision="3" simplification="no-brackets" points="4"}.

    <Solution>
      $$a\cdot(b+c)+c\cdot(a+b) \;=\; a b + a c + c a + c b \;=\; a b + 2 a c + b c$$
    </Solution>
  </Exercise>
</Example>

<Example>
  ```
  <Exercise id="ex-function-2">
    Rewrite the following expression containing powers and roots as a simple power with a rational exponent:

    $\dfrac{x^3}{\left({\sqrt{x}}\right)^3}$$\;\;=\;$[]{.question .text validation="function" length="25" solution="x^(3/2)" supporting-points="10" variables="x" precision="5" simplification="one-power-no-mult-or-div,special-support-points" points="4"}.

    [For example, enter $\sqrt{x}\cdot x^2$ = `x^(5/2)` or alternatively as `x^(2.5)`, mind the brackets around the fraction.]{.hint-text}

    <Solution>
      $$x^{\frac32}$$
    </Solution>
  </Exercise>
  ```

  <Exercise id="ex-function-2">
    Rewrite the following expression containing powers and roots as a simple power with a rational exponent:

    $\dfrac{x^3}{\left({\sqrt{x}}\right)^3}$$\;\;=\;$[]{.question .text validation="function" length="25" solution="x^(3/2)" supporting-points="10" variables="x" precision="5" simplification="one-power-no-mult-or-div,special-support-points" points="4"}.

    [For example, enter $\sqrt{x}\cdot x^2$ = `x^(5/2)` or alternatively as `x^(2.5)`, mind the brackets around the fraction.]{.hint-text}

    <Solution>
      $$x^{\frac32}$$
    </Solution>
  </Exercise>
</Example>

## Interval

> `validation="interval"`

The input is interpreted as an interval.

| Parameter   | Requirement                           |
|-------------|---------------------------------------|
| `precision` | Accuracy of the numerical value check |

<Example>
  ```
  <Exercise id="ex-interval">
    Find the solution set of the mixed equation $|x-3|\cdot x=9$.

    If $x$ is in the interval
    []{.question .text validation="interval" length="14" solution="[3,infty)" precision="5" points="4"}
    the absolute value term is non-negative.

    <Solution>
      If $x$ is in the interval $\left[3; \infty\right[$ the absolute value term is
      non-negative.

      Type `[3;infty)`.
    </Solution>
  </Exercise>
  ```

  <Exercise id="ex-interval">
    Find the solution set of the mixed equation $|x-3|\cdot x=9$.

    If $x$ is in the interval
    []{.question .text validation="interval" length="14" solution="[3,infty)" precision="5" points="4"}
    the absolute value term is non-negative.

    <Solution>
      If $x$ is in the interval $\left[3; \infty\right[$ the absolute value term is
      non-negative.

      Type `[3;infty)`.
    </Solution>
  </Exercise>
</Example>

## Exact fraction

> `validation="exact-fraction"`

The input must be equivalent to the solution, reduced to its maximum, and have a
positive denominator.

| Parameter   | Requirement                           |
|-------------|---------------------------------------|
| `precision` | Accuracy of the numerical value check |

<Example>
  ```
  <Exercise id="ex-exact-fraction">
    Calculate the following numbers by finding the least common denominator and
    reducing as much as possible:

    1.  $\dfrac12+\dfrac13$$\;\;=\;$[]{.question .text validation="exact-fraction" length="10" solution="5/6" precision="5" points="4"} but $\dfrac1{2+3}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="1/5" precision="5" points="4"}.

    2.  $\dfrac{1+2}{5+6}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="3/11" precision="5" points="4"} but $\dfrac15+\dfrac26$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="8/15" precision="5" points="4"}.

    <Solution>
      Sums of denominators may not be collected, not even in the case of like numerators. Here, we have

      $$\dfrac12+\dfrac13\;=\; \dfrac{3}{6}+\dfrac26 \;=\; \dfrac56\;\;\text{but}\;\;\dfrac{1}{2+3} \;=\; \dfrac15\, .$$

      Also, the simple "splitting" of fraction parts is not allowed, here we have

      $$\dfrac{1+2}{5+6} \;=\; \dfrac{3}{11}  \;\;\text{but}\;\; \dfrac15+\dfrac26 \;=\; \dfrac{6}{30}+\dfrac{10}{30} \;=\; \dfrac{16}{30}\;=\; \dfrac{8}{15}\, .$$
    </Solution>
  </Exercise>
  ```

  <Exercise id="ex-exact-fraction">
    Calculate the following numbers by finding the least common denominator and
    reducing as much as possible:

    1.  $\dfrac12+\dfrac13$$\;\;=\;$[]{.question .text validation="exact-fraction" length="10" solution="5/6" precision="5" points="4"} but $\dfrac1{2+3}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="1/5" precision="5" points="4"}.

    2.  $\dfrac{1+2}{5+6}$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="3/11" precision="5" points="4"} but $\dfrac15+\dfrac26$$\;\;=\;$[]{.question .text validation="exact-fraction" length="12" solution="8/15" precision="5" points="4"}.

    <Solution>
      Sums of denominators may not be collected, not even in the case of like numerators. Here, we have

      $$\dfrac12+\dfrac13\;=\; \dfrac{3}{6}+\dfrac26 \;=\; \dfrac56\;\;\text{but}\;\;\dfrac{1}{2+3} \;=\; \dfrac15\, .$$

      Also, the simple "splitting" of fraction parts is not allowed, here we have

      $$\dfrac{1+2}{5+6} \;=\; \dfrac{3}{11}  \;\;\text{but}\;\; \dfrac15+\dfrac26 \;=\; \dfrac{6}{30}+\dfrac{10}{30} \;=\; \dfrac{16}{30}\;=\; \dfrac{8}{15}\, .$$
    </Solution>
  </Exercise>
</Example>
