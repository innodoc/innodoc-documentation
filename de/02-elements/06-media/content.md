---
title: 'Bilder und Videos'
---

Es lassen sich Bilder und Videos einbinden.

## Bilder

Bilder sollten von einem figure-Element umgegeben sein. Dann erhalten sie
eine Formatierung und eine Bildunterschrift.

```markdown
::: {.figure}
![Die Erschaffung Adams von Michelangelo](adam.jpg "Die Erschaffung Adams"){.img}
:::
```
::: {.figure}
![Die Erschaffung Adams von Michelangelo](adam.jpg "Die Erschaffung Adams"){.img}
:::

Die Bildunterschrift kann auch leer gelassen werden, während der Bildtitel
komplett weggelassen werden kann.

```markdown
::: {.figure}
![](adam.jpg){.img}
:::
```

::: {.figure}
![](adam.jpg){.img}
:::

### Bilder im Text

Bilder können auch direkt im Fließtext auftauchen.

```markdown
Ein Bild ![Stern](star.png) im Fließtext.
```

Ein Bild ![Stern](star.png) im Fließtext.

### Bilder als Links

Bilder können auch Links sein.

```markdown
[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")
```

[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")

### Bildformate

TODO: SVG, PNG, JPG

## Videos

Es können auch Videos eingebunden werden.

### Lokale Videos

```markdown
["Test video" from _static](video.mp4){.video .video-static}
```

["Test video" from _static](video.mp4){.video .video-static}

### Externe Videos

```markdown
["L'Arrivee d'un train en gare de la Ciotat, 1895" aus der  Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}
```

["L'Arrivee d'un train en gare de la Ciotat, 1895" aus der  Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}

### Videos von YouTube

```markdown
[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}
```

[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}

## Speicherorte der Mediendateien

Statische Dateien befinden sich im Ordner `_static` im Projektverzeichnis.

Es ist möglich Dateien aus beliebigen Ordnern zu referenzieren:
`/subfolder/math.jpg` referenziert die Datei `_static/subfolder/math.jpg`.

```markdown
::: {.figure}
![Bild aus Unterordner](/subfolder/math.jpg "Beispiel Unterordner"){.img}
:::
```

::: {.figure}
![Bild aus Unterordner](/subfolder/math.jpg "Beispiel Unterordner"){.img}
:::

Ein Pfad ohne vorangestellten Schrägstrich wird als relativ zum Pfad des
Abschnitts verstanden. Bsp: `tu-logo.png` bezieht sich auf
`_static/02-elements/06-media/tu-logo.png`, während `/tu-logo.png`
sich auf `_static/tu-logo.png` bezieht.

```markdown
::: {.figure}
![Logo TU Berlin](tu-logo.png)
:::
```

::: {.figure}
![Logo TU Berlin](tu-logo.png)
:::

### Externe Dateien

Lokale statische Dateien sind zu bevorzugen. Es ist allerdings auch möglich
Dateien von externen Quellen einzubinden. Dies kann Datenschutzprobleme mit
sich bringen. Außerdem können externe Ressourcen jederzeit offline gehen oder
sich verändern.

### Übersetzung von statischen Dateien

Es ist möglich verschiedene Versionen einer Datei für verschiedene Sprachen
anzuzeigen.

In diesem Beispiel gibt es zwei Versionen von `lines.png`, eine für jede
Sprache:

- `de/_static/02-elements/06-media/lines.png`
- `en/_static/02-elements/06-media/lines.png`

::: {.figure}
![Geraden](lines.png)
:::
