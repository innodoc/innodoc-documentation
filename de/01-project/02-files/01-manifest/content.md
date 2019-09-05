---
title: manifest.yml
---

Jeder Kurs benötigt eine
[`manifest.yml`-Datei]{data-index-term="manifest.yml"} im Wurzelverzeichnis.

Die Datei beinhaltet Metadaten für den jeweiligen Kurs. Sie wird im
[[YAML-Format](http://yaml.org/)]{data-index-term="YAML"} verfasst. Im
Folgenden finden sich Beschreibungen der möglichen Angaben in dieser Datei.

:::{.info}
Eine
[beispielhafte Manifestdatei](https://gitlab.tu-berlin.de/innodoc/tub_base/blob/master/manifest.yml)
befindet sich im Repository dieses Kurses.
:::

## `title` (Pflichtfeld)

> Kurstitel

Der Kurstitel wird für jede Sprache angegeben.

```yaml
title:
    de: TUB Basis-Kurs
    en: TUB Base course
```

## `languages` (Pflichtfeld) {#languages}

> Kurssprachen

```yaml
languages: [de, en]
```

## `home_link` (optional)

> Startseite

Der Wert des Feldes `home_link` muss ein gültiger interner Link sein, wie im
Abschnitt [](/section/02-elements/04-links/01-internal) beschrieben. Wird
dieses Feld ausgelassen, so wird als Startseite automatisch der erste Abschnitt
des Kurses gesetzt.

```yaml
home_link: /page/welcome
```

## `pages` (optional) {#pages}

> Definition der [Seiten]{data-index-term="Seite"}

Wie in Abschnitt [](/section/01-project/01-folders#pages) beschrieben, können
zusätzliche Kursseiten angegeben werden.

```yaml
pages:
  - id: about
    icon: info-circle
    link_in_nav: true
    link_in_footer: true
```

Jede Seite benötigt zumindest eine `id`. Aus dieser Angabe ergibt sich der
Dateiname der zugehörigen Markdown-Datei, hier also beispielhaft `about.md`.

### `icon` (optional)

> Bezeichner des Menüicons

Der Bezeichner eines Icons zur Darstellung in Menüs. Eine Liste von Bezeichnern
ist auf der [Webseite von Ant Design](https://ant.design/components/icon/) zu
finden.

### `link_in_nav`/`link_in_footer` (optional)

> Verlinkung in Hauptnavigation und Footer

Gibt an, ob die Seite in der Hauptnavigation bzw. im Footer verlinkt wird.

## `tikz_preamble` (optional)

> $\LaTeX$-Präembel

Siehe Abschnitt [](/section/02-elements/07-media/01-pgf-tikz#tikz_preamble) für
eine detaillierte Beschreibung.

```yaml
tikz_preamble: |
  \usetikzlibrary{arrows,calc}
  \newcommand{\sayhello}{Hello\ World!}
```