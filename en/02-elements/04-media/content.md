---
title: 'Images and Videos'
---

This chapter shows how to embed images and videos.

## Images

A simple image element takes the following form: `![ALT_TEXT](FILENAME)`.

`FILENAME` is the image filename (for details see [File
locations](#file-locations)). `ALT_TEXT` is an alternate text for when the image
cannot be displayed.

The preferred image formats are PNG or JPG for raster graphics and SVG for
vector graphics. By default an image is an inline element, meaning it will be
displayed inside of a paragraph.

:::example
**Markdown**

```markdown
An inline image ![Star](star.png) in the regular text flow.
```

**Result**

An inline image ![Star](star.png) in the regular text flow.
:::

Bigger images should be wrapped in a `figure` element. This way they are
formatted with a surrounding frame and can also receive a caption and a
reference ID. The alternate text is referred automatically from the image title
in this case.

::::example
**Markdown**

```markdown
:::figure
![The Creation of Adam by Michelangelo](adam.jpg "The Creation of Adam"){.img}
:::
```

**Result**

:::figure
![The Creation of Adam by Michelangelo](adam.jpg "The Creation of Adam"){.img}
:::
::::

:::example{#images-as-link}
Images can also be used inside links.

**Markdown**

```markdown
[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")
```

**Result**

[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")
:::

## Videos

Videos are embedded similarly to images. The format is as follows:
`[VIDEO_TITLE](FILENAME){.video .video-static}`.

Use the `video-static` class for files that are stored within the `_static`
folder or on a remote server. For embedding videos from YouTube, the
`video-youtube` class is supported. Use browser-supported codecs and container
format for optimal compatibility.

:::::example
Embed a video file simply by referencing its filename and adding a title.

::::tabs{labels="Result,Markdown"}
:::tab-item
::video[Test video]{src="video.mp4"}
:::

:::tab-item
```markdown
::video[Test video]{src="video.mp4"}
```
:::
::::

Video elements can also reference a video file from an external server.

::::tabs{labels="Result,Markdown"}
:::tab-item
::video["L'Arrivee d'un train en gare de la Ciotat, 1895" from  Wikipedia]{src="https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv"}
:::

:::tab-item
```markdown
::video["L'Arrivee d'un train en gare de la Ciotat, 1895" from  Wikipedia]{src="https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv"}
```
:::
::::
:::::

The following example embeds a video from YouTube.

::::tabs{labels="Result,Markdown"}
:::tab-item
::youtube[Wir sind TU Berlin - Weitersagen]{videoId="OlH6bqv5Z-c"}
:::

:::tab-item
```markdown
::youtube[Wir sind TU Berlin - Weitersagen]{videoId="OlH6bqv5Z-c"}
```
:::
::::

## File locations {#file-locations}

All static files reside in the `_static` folder of the project root unless they
point to external servers. File locations are relative to the `_static` folder.
It's possible to reference files from arbitrary subfolders. E.g.
`/subfolder/math.jpg` refers to the file `_static/subfolder/math.jpg`.

A path specified without a leading slash is considered relative to the `_static`
folder plus the section path for easy file management, e.g. `tu-logo.png` refers
to the image file `_static/02-elements/04-media/tu-logo.png` while
`/tu-logo.png` refers to `_static/tu-logo.png`.

::::example
An image stored in a sub-folder of `_static`.

**Markdown**

```markdown
:::figure
![Loaded from a subfolder](/subfolder/math.jpg "Example subfolder"){.img}
:::
```

**Result**

:::figure
![Loaded from a subfolder](/subfolder/math.jpg "Example subfolder"){.img}
:::

An image stored in `_static/02-elements/04-media`.

**Markdown**

```markdown
:::figure
![Logo TU Berlin](tu-logo.png)
:::
```

**Result**

:::figure
![Logo TU Berlin](tu-logo.png)
:::
::::

:::info
When using media from external servers, please keep in mind that these

1. might go offline or change at any time without notice, and
2. do have privacy implications for your users.

Therefore it's generally recommended to load media from the project's `_static`
folder instead of relying on external services.
:::

### Translation of static files

It is possible to have different versions of a static file for different
languages. innoDoc will always display the language-specific file if it is
present. The translated version of the file needs to be placed in the `_static`
folder of the respective language.

::::example
For this example there are two versions of `lines.png`, one for each language:

- `de/_static/02-elements/04-media/lines.png`
- `en/_static/02-elements/04-media/lines.png`

**Markdown**

```markdown
:::figure
![Lines](lines.png)
:::
```

**Result**

:::figure
![Lines](lines.png)
:::

*(Try switching the language to see the other version of the file.)*
::::
