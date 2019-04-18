---
title: Externe Links
---

Der einfachste Weg einen Link zu erstellen ist, die Zeichen `<` und `>` zu
verwenden.

```markdown
<https://www.tu-berlin.de/>
```

<https://www.tu-berlin.de/>

In der Regel ist es aber wünschenswert einen Linktext anzugeben.

```markdown
[TU Berlin](https://www.tu-berlin.de)
```

[TU Berlin](https://www.tu-berlin.de)

Links können zusätzlich auch mit einem Titel versehen werden. Das erhöht die
Barrierefreiheit. Er wird angezeigt, wenn mit der Maus über dem Link verweilt
wird.

```markdown
[TU Berlin](https://www.tu-berlin.de "Homepage der TU Berlin")
```

[TU Berlin](https://www.tu-berlin.de "Homepage der TU Berlin")

::: {.info}
In Abschnitt []{data-link-section="02-elements/07-media#bilder-als-links"}
ist beschrieben, wie Bilder als Link verwendet werden können.
:::

Linkadressen können auch gesammelt in eine Linkliste geschrieben werden.
Dazu wird anstatt einer Adresse in runden Klammern ein Bezeichner in eckigen
Klammern angegeben. Am Ende des Dokumentes muss dann eine Linkliste
stehen, die Bezeichnern Adressen zuweist.

```markdown
[Link zur TU Berlin][TU Berlin]

[innoConv]

# Ganz am Ende des Dokumentes
[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://gitlab.tu-berlin.de/innodoc/innoconv
```

[Link zur TU Berlin][TU Berlin]

[innoConv]

[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://gitlab.tu-berlin.de/innodoc/innoconv
