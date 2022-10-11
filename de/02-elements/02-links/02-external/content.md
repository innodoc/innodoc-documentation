---
title: Externe Links
---

Der einfachste Weg einen Link zu erstellen ist, die URL mit den Zeichen `<` und
`>` zu umschließen.

::: {.example}
**Markdown**

```markdown
<https://www.tu-berlin.de/>
```

**Ergebnis**

<https://www.tu-berlin.de/>
:::

In der Regel ist es aber wünschenswert einen Linktext anzugeben.

::: {.example}
**Markdown**

```markdown
[TU Berlin](https://www.tu-berlin.de)
```

**Ergebnis**

[TU Berlin](https://www.tu-berlin.de)
:::

Links können zusätzlich auch mit einem Titel versehen werden. Das erhöht die
Barrierefreiheit. Er wird angezeigt, wenn mit der Maus über dem Link verweilt
wird.

::: {.example}
**Markdown**

```markdown
[TU Berlin](https://www.tu-berlin.de "Homepage der TU Berlin")
```

**Ergebnis**

[TU Berlin](https://www.tu-berlin.de "Homepage der TU Berlin")
:::

::: {.info}
In Abschnitt [](/section/02-elements/04-media#bilder-als-links)
ist beschrieben, wie Bilder als Link verwendet werden können.
:::

Linkadressen können auch gesammelt in eine Linkliste geschrieben werden.
Dazu wird anstatt einer Adresse in runden Klammern ein Bezeichner in eckigen
Klammern angegeben. Am Ende des Dokumentes muss dann eine Linkliste
stehen, die Bezeichnern Adressen zuweist.

::: {.example}
**Markdown**

```markdown
[Link zur TU Berlin][TU Berlin]  
[innoConv]
```

Ganz am Ende des Dokuments wird eine Linkliste angefügt.

```markdown
[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
```

**Ergebnis**

[Link zur TU Berlin][TU Berlin]  
[innoConv]
:::

[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
