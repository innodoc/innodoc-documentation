---
title: Links
---

Es gibt viele verschieden Möglichkeiten, Links in einem Text einzufügen. Dabei
können einzelne Wörter, Satzteile oder Sätze verlinkt werden, oder auch weitere
Elemente, z.B. [Bilder](/02-elements/06-media)

Es gibt mehrere Arten Links, und mehrere Arten zu Verlinken.

Will man ein Link zu einer externen Seite im Text haben, ist dies am Einfachsten
möglich, indem die einfach URL im Text vorhanden ist. Will man z.B. findet man die 
Homepage der TU Berlin bei https://www.tu-berlin.de

Den gleichen Effekt erreicht man auch, wenn sich die URL zwischen '<' und '>'
befindet, also kann man die Homepage der TU Berlin auch unter <https://www.tu-berlin.de>
ereichen.

Man ist nicht darauf beschränkt, URLs im Text zu haben, man kann auch
beliebige Wörter verlinken, z.B. [Homepage der TU Berlin](https://www.tu-berlin.de)

Entscheidet man sich für diese Möglichkeit, kann man Links auch ein Titel geben.
Dies ist eine Empfohlene vorgehensweise, um die
[Barrierefreiheit](https://www.w3.org/TR/WCAG20-TECHS/H33.html "Details über die Vorteile von Titel bei Links für Barrierefreiheit")
des Kurses zu gewährleisten.

Das direkte Verlinken von Wörtern (oder anderen Inhalten) ermöglicht auch das
[Linken zu anderen Teilen des Kurses]{#internal-links}. Dabei gibt es grundsätzlich
zwei verschiedene Arten um zu identifizieren, wohin ein Link führen soll: absolute
Links und relative Links.

Absolute Links identifizieren Inhalte anhand des vollen Pfades innerhalb des
Verzeichnisbaumes, ausgehend vom Sprachordner. Absolute Links beginnen mit einem
'/', z.B. kann man so also zur [Übersicht des Kurses](/), zur Beschreibung des
[Aufbau des Kurses](/01-project) oder zum [Aufbau der content.md](/01-project/03-files/02-content)
linken. Dabei muss man den Pfad zu einem Ordner angeben.

Relative Links hingegen identifizieren Inhalte anhand des Pfades vom aktuellen
Kapitel zum Ziel. Dabei kann man bei [Unterordnern](01-references) als URL einfach
direkt den Ordnernamen angeben. [Übergeordnete Ordner](..) kann man mit '..'
referenzieren. Man kann somit alle Kapitel referenzieren, z.B. [Formatierung](../01-formatting),
die [Übersicht des Kurses](../../../) oder [Listen](../../02-lists)
