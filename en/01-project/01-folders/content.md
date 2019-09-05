---
title: Folders
---

The course folder structure is determined by a fixed schema.

:::{.example}
```
[root]
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

The root directory contains exactly one
[language folder](/section/01-project/03-languages) for every supported
language.

:::{.info}
Every language folder must have the exact same section folder structure.
:::

The course structure is defined by folders and subfolders. Every folder
corresponds to a section. The folder name is the section ID. The section order
is determined by the alphanumerical sorting of the folder names. Therefore
it is advised to use a number prefix for folder names.

:::{.info}
Section folder names must not start with a `_` or contain spaces.
:::

Additionally the root directory, as well as any language folder, can contain
one `_static` folder. It holds [static files](/section/02-elements/06-media)
such as images and videos.

In every language directory there can be a `_pages` folder. It holds the
[pages](/section/01-project/02-files/01-manifest#pages) for this language.

## Files

There is a `manifest.yml` in the root directory. It contains
[course meta data](/section/01-project/02-files/01-manifest).

Every section folder contains one `content.md`. It contains the
[section content](/section/01-project/02-files/02-content).

[]{#pages} Furthermore a number of [pages]{data-index-term="page"} can be
created. For every page a Markdown file is placed inside the `_pages` folder.
The name of the file equals the page ID as specified in the
[`pages` field](/section/01-project/02-files/01-manifest#pages) in the course
manifest.
