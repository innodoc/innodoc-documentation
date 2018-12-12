---
title: Ordner
---

Im Wurzelverzeichnis des Kurses befinden sich die
[Sprachordner]{data-link-section="01-project/02-languages"}.

Die Struktur des Kurses ist durch Ordner und Unterordner definiert.
Dabei entspricht jeder Ordner einem Abschnitt. Der Name des jeweiligen Ordners
entspricht der Abschnitts-ID. Die Reihenfolge der Abschnitte im
Inhaltsverzeichnis ergibt sich aus der alphanumerischen Sortierung der
Ordnernamen.

Jeder Sprachordner muss die exakt gleiche Unterordnerstruktur an Abschnitten
enthalten.

Die Namen der Ordner sollten nicht mit einem `_` beginnen oder Leerzeichen
beinhalten.

```
Wurzel
├── de
│   ├── 01-project
│   │   ├── 01-folders
│   │   ├── 02-languages
│   │   └── …
│   ├── 02-elements
│   │   ├── 01-headers
│   │   ├── 02-lists
│   │   └── …
│   └── …
├── en
│   ├── 01-project
│   │   ├── 01-folders
│   │   ├── 02-languages
│   │   └── …
│   ├── 02-elements
│   │   ├── 01-headers
│   │   ├── 02-lists
│   │   └── …
│   └── …
└── …
```

Im Wurzelverzeichnis befindet sich eine `manifest.yml`. Sie enthält
[Metadaten zum Kurs]{data-link-section="01-project/03-files/01-manifest"}.

In jedem Abschnittsordner existiert eine `content.md`. Sie beinhaltet den
[Inhalt eines Kapitels]{data-link-section="01-project/03-files/02-content"}.

Zusätzlich kann sich im Wurzelverzeichnis, sowie in jedem Sprachordner, ein
Ordner `_static` befinden, in dem
[statische Dateien]{data-link-section="02-elements/06-media"}, also Bilder
und Videos abgelegt werden.
