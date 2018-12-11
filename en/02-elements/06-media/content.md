---
title: 'Images and Videos'
---

It's possible to include images and videos.

## Images

Images should be wrapped in a figure element. This way they are formatted
properly and receive a caption.

```markdown
::: {.figure}
![The Creation of Adam by Michelangelo](adam.jpg "The Creation of Adam"){.img}
:::
```

::: {.figure}
![The Creation of Adam by Michelangelo](adam.jpg "The Creation of Adam"){.img}
:::

The image caption can be left empty while the title may be completely omitted.

```markdown
::: {.figure}
![](adam.jpg){.img}
:::
```

::: {.figure}
![](adam.jpg){.img}
:::

### Inline images

Beside images wrapped in figure elements they can also occur within text.

```markdown
An inline image ![Star](star.png) in the text.
```

An inline image ![Star](star.png) in the text.

### Images as link

Images can be links.

```markdown
[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")
```

[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")

### Image formats

TODO: SVG, PNG, JPG

## Videos

Videos can be used.

### Lokale Videos

```markdown
["Test video" from _static](video.mp4){.video .video-static}
```

["Test video" from _static](video.mp4){.video .video-static}

### Externe Videos

```markdown
["L'Arrivee d'un train en gare de la Ciotat, 1895" from  Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}
```

["L'Arrivee d'un train en gare de la Ciotat, 1895" from  Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}

### Videos von YouTube

```markdown
[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}
```

[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}

## File locations

All static files reside in the `_static` folder in the project root.

It's possible to reference files from arbitrary subfolders:
`/subfolder/math.jpg` refers to the file `_static/subfolder/math.jpg`.

```markdown
::: {.figure}
![Loaded from a subfolder](/subfolder/math.jpg "Example subfolder"){.img}
:::
```

::: {.figure}
![Loaded from a subfolder](/subfolder/math.jpg "Example subfolder"){.img}
:::

An path specified without a leading slash it is considered relative to
the section path. E.g. `tu-logo.png` refers to the image file
`_static/02-elements/06-media/tu-logo.png` while `/tu-logo.png`
refers to `_static/tu-logo.png`.

```markdown
::: {.figure}
![Logo TU Berlin](tu-logo.png)
:::
```

::: {.figure}
![Logo TU Berlin](tu-logo.png)
:::

### External files

Static files local to the project are the preferred way to include media. While
external locations do work they are questionable from a privacy point-of-view
and also might go offline or change at any time.

### Translation of static files

It's possible to use different versions of static files for different
languages.

For this example there are two versions of `lines.png`, one for each language:

- `de/_static/02-elements/06-media/lines.png`
- `en/_static/02-elements/06-media/lines.png`

```markdown
::: {.figure}
![Lines](lines.png)
:::
```

::: {.figure}
![Lines](lines.png)
:::

(You can switch the language to see the other version of the file.)
