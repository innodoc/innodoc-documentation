---
title: Stichwortverzeichnis
---

Für jeden Kurs wird automatisch ein Stichwortverzeichnis generiert, wenn
zumindest ein Eintrag angelegt wurde.

Um Einträge im Stichwortverzeichnis zu erzeugen, werden einzelne Stellen im
Text markiert.

::: {.example}
```markdown
In diesem Satz befindet sich ein Wort, welches im
[Stichwortverzeichnis]{data-index-term="Stichwortverzeichnis"} erscheint.
```

In diesem Satz befindet sich ein Wort, welches im
[Stichwortverzeichnis]{data-index-term="Stichwortverzeichnis"} erscheint.
:::

Der Eintrag selbst ist nicht erkennbar im Text. Das markierte Wort oder der
markierte Satz wird mit dem Attribut `data-index-term` versehen. Der Wert
des Attributs ist der Ausdruck, so wie er im Stichwortverzeichnis erscheint.
Natürlich können eine beliebige Anzahl von Verweisen zu einem einzelnen
Ausdruck erstellt werden.

::: {.info}
Es können auch $\LaTeX$-Formeln im Ausdruck verwendet werden.

```markdown
[$\LaTeX$-Formel]{data-index-term="$\LaTeX$-Formel"}
```

[$\LaTeX$-Formel]{data-index-term="$\LaTeX$-Formel"}
:::
