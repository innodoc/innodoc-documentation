---
title: Inhaltsdateien
---

In jedem Inhaltsordner eines Abschnitts befindet sich eine Datei `content.md`.
Diese Datei wird im [Markdown-Format]{data-index-term="Markdown"} verfasst.

Für Seiten gibt es eine Markdown-Datei im `_pages`-Ordner der jeweiligen
Sprache. Der Dateiname hier entspricht der Seiten-ID, wie im
[Kursmanifest](/section/01-project/02-files/01-manifest#pages) angegeben, also
beispielsweise `about.md` für die Seite mit der ID `about`.

Am Anfang jeder Inhaltsdatei befindet sich ein sogenannter
[YAML-Block]{data-index-term="YAML"}, in dem per `title` der Titel eines
Dokumentes definiert wird. Dies ist auch der Name, unter dem ein Kapitel im
[Inhaltsverzeichnis]{data-index-term="Inhaltsverzeichnis"} erscheint bzw. der
Eintrag im Menü im Falle einer Seite. Bei Seiten kann optional außerdem noch
`short_title` angegeben werden. Der Kurztitel wird nur für Menüs verwendet, da
hier der Platz begrenzt ist.

:::{.example}
```yaml
---
title: Über diesen Kurs
short_title: Über
---
```
:::

Darauf folgt der eigentliche Inhalt des Kapitels. Eine ausführliche Besprechung
der Möglichkeiten gibt es in Kapitel [](/section/02-elements).
