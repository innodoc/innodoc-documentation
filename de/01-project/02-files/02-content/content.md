---
title: Inhaltsdateien
---

Inhalte werden im [Markdown-Format]{data-index-term="Markdown"} geschrieben. Es
braucht genau eine Inhaltsdatei pro Abschnitt/Seite und Sprache. Inhaltsdateien
bestehen aus einem [Metablock](#meta-data) am Anfang der Datei sowie dem
eigentlichen Inhalt. Eine ausführliche Besprechung der einzelnen
Inhaltselemente folgt in Kapitel [](/section/02-elements).

Für jeden **Abschnitt** muss eine Datei `content.md` im entsprechenden Ordner
der jeweiligen Sprache abgelegt sein, bspw. die Datei
`en/01-project/02-files/02-content/content.md` für die Englische Version des
Abschnitts `01-project/02-files/02-content`.

Für jede **Seite** muss eine Inhaltsdatei im Ordner `_pages` der jeweiligen
Sprache abgelegt sein. Der Dateiname entspricht der Seiten-ID, wie im
[Kursmanifest](/section/01-project/02-files/01-manifest#pages) definiert.
Beispielsweise ist der Englische Inhalt für die Seite `about` in der Datei
`en/_pages/about.md` gespeichert.

## Metadaten {#meta-data}

Jede Inhaltsdatei benötigt einen sogenannten
[YAML-Block]{data-index-term="YAML"} am Anfang der Datei, der mindestens den
Eintrag `title` enthält.

<Example>
  ```yaml
  ---
  title: Über diesen Kurs
  short_title: Über
  ---
  ```
</Example>

## `title` (Pflichtfeld)

> Seiten- bzw. Abschnittstitel

Jede Inhaltsdatei muss einen Titel definieren. Dieser Name erscheint als
Überschrift über dem Inhalt, im
[Inhaltsverzeichnis]{data-index-term="Inhaltsverzeichnis"} und anderen Menüs.

## `short_title` (optional)

> Seiten- bzw. Abschnittstitel (Kurzform)

Eine kurze Version des Titels kann angegeben werden. Diese wird an Stellen mit
begrenztem Platz verwendet.

## `type` (optional)

> [Abschnittstyp]{data-index-term="Abschnittstyp"}

Abschnitte können vom Typ `regular` (normal), `exercises` (Aufgaben), `test`
(Test) sein. Wenn nicht explizit angegeben, ist die Vorgabe `regular`.
Seiten unterstützen dieses Attribut nicht.

Abschnitte des Typs `exercises` und `test` erhalten ein spezielles Icon im
Inhaltsverzeichnis. Abschnitte des Typs `test` werden separat im
[Lernfortschritt](app:progress) aufgeführt. Außerdem werden die Aufgaben
erst nach dem Einreichen des Tests ausgewertet.

<Info>
  Der Abschnitt [](/section/02-elements/07-interactive-exercises/01-text) ist als
  Aufgabenabschnitt gekennzeichnet. In Abschnitt [](/section/03-test) ist ein
  Beispieltest zu finden.
</Info>

