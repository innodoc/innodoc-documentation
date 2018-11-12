---
title: 'Bilder und Videos'
---

Man kann auch Bilder und Videos in einbinden.

Diese können statische Dateien in diesem Projekt sein, oder auf einem externen Server liegen.

Eine statische Bilddatei kann auf folgende Art und weise Eingebunden werden:
![Text-Beschreibung des Bildes](/adam.jpg "Bildtitel")
Die Bilddatei selbst liegt hierbei im _static Ordner im Wurzelverzeichnis des Projekes.

Man kann auch lokalisierte Versionen einer Datei referenzieren:
![Deutsche Flagge](/flag.png "Es wird die Deutsche Flagge aus de/_static geladen")
Diese Dateien liegen im _static Ordner der jeweiligen Sprache.

Man kann die Bilddateien auch referenzieren, wenn diese auf Unterordner verteilt sind.
![Eine Mathe-Aufgabe](/subfolder/math.jpeg "Ein Beispiel-Bild aus einem Unterordner")

Der Bildtitel kann auch weggelassen werden.
![Eine Mathe-Aufgabe](/subfolder/math.jpeg)

Falls die Ordnerstruktur der statischen Daten die Ordnerstruktur dieses Inhalts wieder spiegelt, kann man auch den Pfad zu Bildern weglassen:
![Logo der TU Berlin aus _static](TU_Logo_kurz.png)
Dies funktioniert auch für die lokalisierten Ordner:
![Logo der TU Berlin aus de/_static](TU_Logo.png)

Selbstverständlich können Bilder auch ihrerseits verlinkt sein.
[![Logo der TU Berlin aus de/_static](TU_Logo.png)](https://www.tu-berlin.de "Homepage der TU Berlin")

Externe Bilddateien, also Bilddateien, die auf fremden Server liegen, werden auf die selbe Art eingebunden:
![Externe Beispiel-Datei](https://picsum.photos/200 "Ein Beispiel-Bild von einem Externen Server")

Videos können auf eine ähnliche Weise eingebunden werden. Dabei ist zu beachten, dass am Anfang kein "!" zu finden ist, und am ende {.video .video-static} stehen muss
["Test video" von _static](/video.mp4){.video .video-static}

Das gleiche gilt auch für Videos auf externen Server:
["L'Arrivee d'un train en gare de la Ciotat, 1895" von Wikipedia](https://upload.wikimedia.org/wikipedia/en/c/c3/L%27Arrivee_d%27un_train_en_gare_de_la_Ciotat%2C_1895.ogv){.video .video-static}

Youtube-Videos können ahenlich eingebunden werden. Dabei muss am Ende {.video .video-youtube} stehen
[Wir sind TU Berlin - Weitersagen](https://www.youtube.com/watch?v=OlH6bqv5Z-c){.video .video-youtube}
