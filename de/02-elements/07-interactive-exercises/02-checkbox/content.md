---
title: Checkbox
---

Eine weitere Aufgabenform ist die Checkbox- oder auch Multiple-Choice-Aufgabe.
Hier gibt es mehrere anwählbare Optionen, bei denen keine, eine oder mehrere
richtig sein können.

Checkbox-Aufgaben werden durch die Angabe mehrerer Fragen des Typs `checkbox`
realisiert, wobei jede Frage eine einzelne Checkbox ergibt.

Zu Beginn sind die Checkboxen nicht ausgefüllt, also weder ausgewählt noch
nicht ausgewählt.

<Exercise>
  Sind diese Ungleichungen richtig oder falsch?

  <Grid>
    <GridItem xs="4">
      []{.question .checkbox #EX_CB_1 solution="0" validation="boolean"}
    </GridItem>
    <GridItem xs="8">
      $\frac12>1-\frac13$
    </GridItem>
    <GridItem xs="4">
      []{.question .checkbox #EX_CB_2 solution="1" validation="boolean"}
    </GridItem>
    <GridItem xs="8">
      $a^2\geq 2a b-b^2$ (wobei $a$ und $b$ unbekannte Zahlen sind)
    </GridItem>
    <GridItem xs="4">
      []{.question .checkbox #EX_CB_3 solution="1" validation="boolean"}
    </GridItem>
    <GridItem xs="8">
      $\frac12<\frac23<\frac34$
    </GridItem>
  </Grid>
</Exercise>
