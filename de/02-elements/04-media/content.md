---
title: 'Bilder und Videos'
---

Dieses Kapitel beschreibt, wie sich Bilder und Videos einbinden lassen.

## Bilder

Ein einfaches Bildelement hat die folgende Form: `![ALT_TEXT](DATEINAME)`.

`DATEINAME` ist der Dateiname des Bildes (siehe
[Speicherorte](#file-locations)). `ALT_TEXT` ist ein alternativer Text für den
Fall, dass das Bild nicht angezeigt werden kann.

Für Rastergrafiken sollte PNG oder JPG, für Vektorgrafiken SVG als Bildformat
gewählt werden. Standardmäßig werden Bilder inline, d. h. im Textfluss innerhalb
eines Absatzes angezeigt.

::: {.example}
**Markdown**

```markdown
Ein Bild ![Stern](star.png) im Fließtext.
```

**Ergebnis**

Ein Bild ![Stern](star.png) im Fließtext.
:::

Größere Bilder sollten in ein `figure`-Element eingeschlossen werden. Dadurch
werden sie mit einem umgebenden Rahmen angezeigt. Außerdem können sie so auch
eine Beschriftung und eine Referenz-ID erhalten. Der Alternativtext wird in
diesem Fall automatisch aus dem Bildtitel erzeugt.

:::: {.example}
**Markdown**

```markdown
::: {.figure}
![Die Erschaffung Adams von Michelangelo](adam.jpg "Die Erschaffung Adams"){.img}
:::
```

**Ergebnis**

::: {.figure}
![Die Erschaffung Adams von Michelangelo](adam.jpg "Die Erschaffung Adams"){.img}
:::
::::

::: {.example}
Bilder können auch innerhalb von Links benutzt werden.

**Markdown**

```markdown
[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")
```

**Ergebnis**

[![Logo TU Berlin](tu-logo.png)](https://www.tu-berlin.de/ "Homepage TU Berlin")
:::

## Videos

Videos werden ähnlich wie Bilder eingebettet. Das Format ist wie folgt:
`[VIDEO_TITEL](DATEINAME){.video .video-static}`.

Die Klasse `video-static` wird für Videos verwendet, die im Ordner `_static`
oder auf einem externen Server gespeichert sind. Um YouTube-Videos einzubinden,
kann die Klasse `video-youtube` verwendet werden. Für die Videodateien sollten
die von Browsern unterstützten gängigen Codecs und Containerformate verwendet
werden.

::: {.example}
Eine Videodatei wird eingebettet, indem auf den Dateinamen verwiesen und ein
Titel angegeben wird.

**Markdown**

```markdown
[Test video](video.mp4){.video .video-static}
```

**Ergebnis**

[Test video](video.mp4){.video .video-static}

Videoelemente können auch auf eine Videodatei von einem externen Server
verweisen.

**Markdown**

```markdown
["L'Arrivee d'un train en gare de la Ciotat, 1895" aus der  Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}
```

**Ergebnis**

["L'Arrivee d'un train en gare de la Ciotat, 1895" aus der  Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}

Das folgende Beispiel bettet ein Video von YouTube ein.

**Markdown**

```markdown
[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}
```

**Ergebnis**

[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}
:::

## Speicherorte der Mediendateien  {#file-locations}

Alle statischen Dateien befinden sich im Ordner `_static` des
Wurzelverzeichnisses, sofern sie nicht auf externe Server verweisen. Die
Angabe des Dateinamens ist relativ zum Ordner `_static`.

Es ist möglich, Dateien aus beliebigen Unterordnern zu referenzieren. So
verweist z. B. `/subfolder/math.jpg` auf die Datei
`_static/subfolder/math.jpg`.

Ein ohne führenden Schrägstrich angegebener Pfad wird als relativ zum Ordner
`_static` und dem Abschnittspfad betrachtet, um die Dateiverwaltung zu
vereinfachen. Beispielsweise bezieht sich `tu-logo.png` auf die Bilddatei
`_static/02-elements/04-media/tu-logo.png`, während sich `/tu-logo.png` auf
`_static/tu-logo.png` bezieht.

:::: {.example}
Ein Bild, das in einem Unterordner von `_static` gespeichert ist.

**Markdown**

```markdown
::: {.figure}
![Bild aus Unterordner](/subfolder/math.jpg "Beispiel Unterordner"){.img}
:::
```

**Ergebnis**

::: {.figure}
![Bild aus Unterordner](/subfolder/math.jpg "Beispiel Unterordner"){.img}
:::

Ein Bild, das in `_static/02-elements/04-media` gespeichert ist.

**Markdown**

```markdown
::: {.figure}
![Logo TU Berlin](tu-logo.png)
:::
```

**Ergebnis**

::: {.figure}
![Logo TU Berlin](tu-logo.png)
:::
::::

::: {.info}
Wenn Medien von externen Servern verwenden werden, ist es wichtig zu bedenken,
dass diese

1. jederzeit ohne Vorankündigung offline gehen oder sich ändern können, und
2. Auswirkungen auf die Privatsphäre Ihrer Benutzer haben.

Daher wird grundsätzlich angeraten, Medien aus dem `_static`-Ordner des
Projekts zu laden, anstatt sich auf externe Dienste zu verlassen.
:::

### Übersetzung von statischen Dateien

Es ist möglich, verschiedene Versionen einer Datei für verschiedene Sprachen
anzuzeigen. innoDoc benutzt automatisch die sprachspezifische Datei, wenn sie
vorhanden ist. Die übersetzte Version der Datei muss im Ordner `_static` der
jeweiligen Sprache abgelegt werden.

:::: {.example}
In diesem Beispiel gibt es zwei Versionen von `lines.png`, eine für jede
Sprache:

- `de/_static/02-elements/04-media/lines.png`
- `en/_static/02-elements/04-media/lines.png`

**Markdown**

```markdown
::: {.figure}
![Lines](lines.png)
:::
```

**Ergebnis**

::: {.figure}
![Lines](lines.png)
:::

*(Um die verschiedenen Versionen der Datei zu sehen, kann die Kurssprache
gewechselt werden.)*
::::
