---
title: Links
---

Es existieren verschiedene Möglichkeiten, um Links darzustellen.

:::table[Syntax für Links]
| Ergebnis                                                                               | Markdown                                                                                 | Beschreibung                                                              |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <https://www.wikipedia.org/>                                                           | `<https://www.wikipedia.org/>`                                                           | Nur Linkziel                                                              |
| [Wikipedia](https://www.wikipedia.org/)                                                | `[Wikipedia](https://www.wikipedia.org/)`                                                | Linkziel und -text                                                        |
| [Wikipedia](https://www.wikipedia.org/ "Wikipedia ist eine freie Online-Enzyklopädie") | `[Wikipedia](https://www.wikipedia.org/ "Wikipedia ist eine freie Online-Enzyklopädie")` | Linkziel, -text und -titel (Titel wird bei Hovern über den Link sichtbar) |
:::

Der Link-Text kann aus beliebigen Inline-Elementen, wie [formatiertem
Text](app:section|02-elements/01-basics#formatting),
[Formeln](app:section|02-elements/03-formulas) oder auch
[Bildern](app:section|02-elements/04-media) bestehen.

Es wird zwischen *internen* und *externen* Links unterschieden. [Interne
Links](app:section|02-elements/02-links/01-internal) verweisen auf Seiten
innerhalb des Kurses, wie Inhaltsseiten oder auch die [Startseite](app:home) oder
das [Stichwortverzeichnis](app:glossary). Durch [externe
Links](app:section|02-elements/02-links/02-external) sind Verweise auf andere
Webseiten außerhalb dieses Kurses möglich.

:::info
In Abschnitt [](/section/02-elements/04-media#bilder-als-links)
ist beschrieben, wie Bilder als Link verwendet werden können.
:::

Linkadressen können auch gesammelt in eine Linkliste geschrieben werden.
Dazu wird anstatt einer Adresse in runden Klammern ein Bezeichner in eckigen
Klammern angegeben. Am Ende des Dokumentes muss dann eine Linkliste
stehen, die Bezeichnern Adressen zuordnet.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
[Link zur TU Berlin][TU Berlin]  
[Wikipedia]
:::

:::tab-item
```markdown
[Link zur TU Berlin][TU Berlin]  
[Wikipedia]
```

Ganz am Ende des Dokuments wird eine Linkliste angefügt.

```markdown
[TU Berlin]: https://www.tu-berlin.de
[Wikipedia]: https://www.wikipedia.org
```
:::
::::
:::::

[TU Berlin]: https://www.tu-berlin.de
[Wikipedia]: https://www.wikipedia.org
