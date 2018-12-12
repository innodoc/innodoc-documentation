---
title: Folders
---

The root directory contains the
[language folders]{data-link-section="01-project/02-languages"}.

The course structure is defined by folders and subfolders. Every folder
corresponds to a section. The folder name is the section ID. The section order
is determined by the alphanumerical sorting of the folder names.

Every language folder must have the exact same folder structure.

Section folder names should not start with a `_` or contain spaces.

```
root
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

There is a `manifest.yml` in the root directory. It contains
[course meta data]{data-link-section="01-project/03-files/01-manifest"}.

Every section folder contains one `content.md`. It contains the
[section content]{data-link-section="01-project/03-files/02-content"}.

Additionally the root directory, as well as every language folder, can contain
one `_static` folder. It contains
[static files]{data-link-section="02-elements/06-media"} such as images and
videos.
