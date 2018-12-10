---
title: Verlinkung innerhalb eines Kapitels
---

Es kann auch Links zu stellen innerhlab eines Kapitels geben.

Um ein Link innerhalb eines Kapitels zu haben, müssen erst ankerpunkte definiert
werden, zu denen man Verlinken kann. Diese können einfache [Wörter]{#woerter} sein,
[Bilder]{data-link-section="/02-elements/06-media"} denene eine ID zugewiesen wird,
[Links]{data-link-section="02-elements/03-links-and-formatting/02-links" #links},
denen eine ID zugewiesen wird, oder alle anderen Elemente, die eine ID haben können.

Nachdem solche Anker definiert sind, kann man dann mit einem
[Link zu dem definierten Anker](#woerter) ein Link zu dem Anker erstellen.

[Es kann]{#titellink} auch [Links zu Anker, die erst später im Text definiert werden](#auch-titel).

Genauso kann man auch [Links zu Anker in anderen Kapitel]{data-link-section="02-elements/03-links-and-formatting/02-links#internal-links"}
definieren.

Es kann auch beliebig viele [Links zu einem definierten Anker](#woerter) geben.

# Auch Titel!
 
Es kann auch links zu [Titel]{data-link-section="/02-elements/01-headers"} innerhalb eines Kapitels
geben - wie wir bereits [weiter oben](#titellink) gesehen haben

Dabei wird für ein Titel immer automatisch eine ID generiert: Generell sieht diese
ID so aus: die Wörter des Titels, ab des ersten Buchstabens im Titel, ohne
Formatierung, ohne Satzzeichen (ausser Unterstrich, Bindestrich und Punkt), in
Kleinbuchstaben, getrennt von einem '-'.
Also bei dem Titel ["Auch Titel!"](#auch-titel) lautet die ID "#auch-titel"

Weiters werden auch [Referenzen]{data-link-section="02-elements/03-links-and-formatting/02-links/01-references"}
für Titel automatisch generiert,
also kann man Titel innerhalb eines Kapitels ganz einfach durch ihren Text
referenzieren, z.B. [Auch Titel!]
