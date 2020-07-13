---
title: Ordnerstruktur
---

Die Verzechnisstruktur eines Kurse folgt einem festen Schema.

:::{.example}
```
[Wurzel]
├── _static
├── de
│   ├── _pages
│   ├── _static
│   ├── 01-project
│   │   ├── 01-folders
│   │   ├── 02-files
│   │   └── …
│   ├── 02-elements
│   │   ├── 01-headers
│   │   ├── 02-lists
│   │   └── …
│   └── …
├── en
│   ├── _pages
│   ├── _static
│   ├── 01-project
│   │   ├── 01-folders
│   │   ├── 02-files
│   │   └── …
│   ├── 02-elements
│   │   ├── 01-headers
│   │   ├── 02-lists
│   │   └── …
│   └── …
└── …
```
:::

Im Wurzelverzeichnis des Kurses befindet sich exakt ein
[Sprachordner](/section/01-project/03-languages) für jede unterstützte Sprache.

:::{.info}
Jeder Sprachordner muss die exakt gleiche Unterordnerstruktur an Abschnitten
enthalten.
:::

Die Struktur des Kurses selbst ist durch Ordner und Unterordner definiert.
Dabei entspricht jeder Ordner einem Abschnitt. Der Name des jeweiligen Ordners
entspricht der Abschnitts-ID. Die Reihenfolge der Abschnitte im
Inhaltsverzeichnis ergibt sich aus der alphanumerischen Sortierung der
Ordnernamen. Daher wird empfohlen den Ordnernamen eine Nummer voranzustellen.

:::{.info}
Ordnernamen dürfen nicht mit einem `_` beginnen oder Leerzeichen beinhalten.
:::

Zusätzlich kann sich im Wurzelverzeichnis, sowie in jedem Sprachordner, ein
Ordner `_static` befinden, in dem
[statische Dateien](/section/02-elements/07-media), also Bilder
und Videos abgelegt werden.

In jedem Sprachordner kann außerdem ein Verzeichnis `_pages` existieren, in dem
sich die [Seiten](/section/01-project/02-files/01-manifest#pages) für die
jeweilige Sprache befinden.

## Dateien

Im Wurzelverzeichnis befindet sich eine Datei `manifest.yml`. Sie enthält
[Metadaten zum Kurs](/section/01-project/02-files/01-manifest).

In jedem Abschnittsordner existiert eine `content.md`. Sie beinhaltet den
[Inhalt eines Kapitels](/section/01-project/02-files/02-content).

[]{#pages} Darüber hinaus können beliebige [Seiten]{data-index-term="Seite"}
angelegt werden. Für jede Seite wird eine Markdown-Datei im `_pages`-Ordner
abgelegt. Der Name dieser Datei entspricht der Seiten-ID, wie im
[`pages`-Feld](/section/01-project/02-files/01-manifest#pages) des
Kurs-Manifests angegeben.
