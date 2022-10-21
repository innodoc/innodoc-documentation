---
title: Course manifest
---

Every course needs a [`manifest.yml`]{data-index-term="manifest.yml"} file in
the root directory.

The file contains meta data for the course. It is written in
[[YAML format](http://yaml.org/)]{data-index-term="YAML"}. In this section you
will find descriptions of the possible fields in this file.

:::{.info}
An
[example manifest file](https://git.tu-berlin.de/innodoc/tub_base/blob/master/manifest.yml)
can be found in the repository of this course.
:::

## `title` (mandatory)

> Course title

The course title is translated for each language.

```yaml
title:
    de: TUB Basis-Kurs
    en: TUB Base course
```

## `languages` (mandatory) {#languages}

> Course languages

```yaml
languages: [de, en]
```

## `home_link` (optional)

> Home link

The value of the field `home_link` needs to a valid internal link as described
in section [](/section/02-elements/02-links/01-internal). If it is omitted the
home link will be the first section of the course.

```yaml
home_link: /page/welcome
```

## `pages` (optional) {#pages}

> [Page]{data-index-term="page"} definition

As described in section [](/section/01-project/01-folders#pages), a number of
additional course pages can be specified.

```yaml
pages:
  - id: about
    icon: info-circle
    linked: [nav, footer]
```

Every page needs at least the `id` field. The name of the corresponding
Markdown file is derived from this ID, e.g. `about.md`.

### `icon` (optional)

> Icon identifier for menus

The identifier of the icon that is used for menus. A list of valid identifiers
can be found on the
[website of Ant Design](https://ant.design/components/icon/).

### `linked`

> Link in site navigation and footer

If there should be link in the main navigation and footer.

## `tikz_preamble` (optional)

> $\LaTeX$-Präembel

See section [](/section/02-elements/04-media/01-pgf-tikz#tikz_preamble) for a
detailed description.

```yaml
tikz_preamble: |
  \usetikzlibrary{arrows,calc}
  \newcommand{\sayhello}{Hello\ World!}
```

## `mathjax` (optional) {#mathjax}

In order to use custom extensions with MathJax you can override parts of the
MathJax configuration. It uses the
[MathJax configuation format](https://docs.mathjax.org/en/latest/options/index.html).

In this example we add the custom extension
[`innodoc-mathjax`](/section/02-elements/03-formulas#innodoc-mathjax).

```yaml
mathjax:
  loader:
    load:
      - "[innodoc]/innodoc-mathjax.min.js"
    paths:
      innodoc: http://localhost:8005
  tex:
    packages:
      "[+]":
        - innodoc-mathjax
```
