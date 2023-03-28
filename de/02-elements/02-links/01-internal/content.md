---
title: Interne Links
---

Es können Links zu jeder internen Applikationsseite gesetzt werden. Das Linkziel
folgt dabei dem Schema `app:ROUTE|PARAMETER`.

::::grid
:::grid-item{xs="4" md="2"}
`ROUTE`
:::
:::grid-item{xs="8" md="10"}
Der Name der Route. Am Ende dieses Abschnitts ist eine
[Übersicht aller Routen](#routes) zu finden.
:::
:::grid-item{xs="4" md="2"}
`PARAMETER`
:::
:::grid-item{xs="8" md="10"}
Der Parameter der Route wird nur bei Links zu Seiten und Abschnitten angegeben.
:::
::::

## Verweise auf Abschnitte und Seiten

Um einen Link zu einem Abschnitt oder einer Seite zu erstellen, muss der
*Abschnittspfad* bzw. der *Seitenname* als Parameter angegebenen werden. Die
Route und der Parameter werden mit dem Pipe-Symbol `|` voneinander getrennt.
Wird kein Linktext angegeben, so wird automatisch der Titel des Linkziels
eingefügt.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
<app:section|02-elements/03-formulas>  
[](app:section|02-elements/04-media)  
[anderer Abschnitt](app:section|02-elements/04-media)  
<app:page|about>  
[andere Seite](app:page|about)
:::

:::tab-item
```markdown
<app:section|02-elements/03-formulas>  
[](app:section|02-elements/04-media)  
[anderer Abschnitt](app:section|02-elements/04-media)  
<app:page|about>  
[andere Seite](app:page|about "Link zu anderer Seite")
```
:::
::::
:::::

:::info
Wenn ein verlinkter Abschnitt bzw. eine Seite nicht existiert, wird ein
Fehlertext dargestellt:  
[Dies ist ein Link zu einem nicht existierendem
Kapitel.](/section/does-not-exist)
:::

## Verweise auf Elemente {#referencing-elements}

Um auf ein bestimmtes Element innerhalb eines Abschnitts zu verweisen, werden
*Anker-IDs* verwendet. Diese müssen innerhalb eines Dokuments einzigartig sein
und können manuell zugewiesen werden.

Inhaltselementen können Anker-IDs zugewiesen werden, indem der Bezeichner mit
einem vorangestelltem `#` angegeben wird. So lassen sich etwa Überschriften,
aber auch andere Elemente referenzieren.

:::::example
Link zu Überschrift mit händisch vergebener ID.

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
### Überschrift mit ID {#my-id}

[Link zur Überschrift](#my-id)
:::

:::tab-item
```markdown
### Überschrift mit ID {#my-id}

[Link zur Überschrift](#my-id)
```
:::
::::

Wird keine explizit angegeben, so erhalten Überschriften automatisch eine vom
Text abgeleitete ID. Aus Konsistenzgründen vor allem bei mehrsprachigen Texten
wird dazu geraten, referenzierten Überschriften manuell eine explizite ID
zuzuweisen.

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
### Überschrift mit automatischer ID

[Link zur Überschrift](#überschrift-mit-automatischer-id)
:::

:::tab-item
```markdown
### Überschrift mit automatischer ID

[Link zur Überschrift](#überschrift-mit-automatischer-id)
```
:::
::::

Link zur Überschrift _Videos_ in einem anderen Kapitel:

::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
[Unterabschnitt _Videos_ im Kapitel _Bilder und Videos_](/section/02-elements/04-media#videos)
:::

:::tab-item
```markdown
[Unterabschnitt _Videos_ im Kapitel _Bilder und Videos_](/section/02-elements/04-media#videos)
```
:::
::::
:::::

## Verweise auf andere Seiten

In jedem Kurs gibt es weitere Seiten, wie das Stichwort- und Inhaltsverzeichnis.
Diese werden durch die Verwendung der entsprechenden Route referenziert.

:::::example
::::tabs{labels="Ergebnis,Markdown"}
:::tab-item
<app:home>  
<app:progress>  
<app:toc>
:::

:::tab-item
```markdown
<app:home>  
<app:progress>  
<app:toc>
```
:::
::::
:::::

### Übersicht der Routen {#routes}

Nachfolgend eine Übersicht der verfügbaren Applikationsrouten.

:::table[Applikationsrouten]
| Name                   | Ziel                       | Parameter      |
|------------------------|----------------------------|----------------|
| `page`                 | Inhaltsseite               | Seitenname     |
| `section`              | Inhaltsabschnitt           | Abschnittspfad |
| `home`                 | Startseite des Kurses      |                |
| `progress`             | Lernfortschritt            |                |
| `toc`                  | Inhaltsverzeichnis         |                |
| `glossary`             | Stichwortverzeichnis       |                |
| `user:login`           | Anmeldung                  |                |
| `user:forgot-password` | Passwort-Wiederherstellung |                |
| `user:sign-up`         | Konto erstellen            |                |
:::
