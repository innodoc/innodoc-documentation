---
title: Externe Links
---

Der einfachste Weg einen Link zu erstellen ist, die URL mit den Zeichen `<` und
`>` zu umschließen.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
<https://www.tu-berlin.de/>
:::

:::tab-item
```markdown
<https://www.tu-berlin.de/>
```
:::
::::
:::::

In der Regel ist es aber wünschenswert einen Linktext anzugeben.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
[TU Berlin](https://www.tu-berlin.de)
:::

:::tab-item
```markdown
[TU Berlin](https://www.tu-berlin.de)
```
:::
::::
:::::

Links können zusätzlich auch mit einem Titel versehen werden. Das erhöht die
Barrierefreiheit. Er wird angezeigt, wenn mit der Maus über dem Link verweilt
wird.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
[TU Berlin](https://www.tu-berlin.de "Homepage der TU Berlin")
:::

:::tab-item
```markdown
[TU Berlin](https://www.tu-berlin.de "Homepage der TU Berlin")
```
:::
::::
:::::

:::info
In Abschnitt [](/section/02-elements/04-media#bilder-als-links)
ist beschrieben, wie Bilder als Link verwendet werden können.
:::

Linkadressen können auch gesammelt in eine Linkliste geschrieben werden.
Dazu wird anstatt einer Adresse in runden Klammern ein Bezeichner in eckigen
Klammern angegeben. Am Ende des Dokumentes muss dann eine Linkliste
stehen, die Bezeichnern Adressen zuweist.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
[Link zur TU Berlin][TU Berlin]  
[innoConv]
:::

:::tab-item
```markdown
[Link zur TU Berlin][TU Berlin]  
[innoConv]
```

Ganz am Ende des Dokuments wird eine Linkliste angefügt.

```markdown
[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
```
:::
::::
:::::

[TU Berlin]: https://www.tu-berlin.de
[innoConv]: https://git.tu-berlin.de/innodoc/innoconv
