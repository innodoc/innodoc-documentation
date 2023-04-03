---
title: Interne Links
---

Es können Links zu jeder internen Applikationsseite gesetzt werden. Das Linkziel
folgt dabei dem Schema `app:ROUTE|PARAMETER`.

<Grid>
  <GridItem xs="4" md="2">
    `ROUTE`
  </GridItem>
  <GridItem xs="8" md="10">
    Der Name der Route. Am Ende dieses Abschnitts ist eine
    [Übersicht aller Routen](#routes) zu finden.
  </GridItem>
  <GridItem xs="4" md="2">
    `PARAMETER`
  </GridItem>
  <GridItem xs="8" md="10">
    Der Parameter der Route wird nur bei Links zu Seiten und Abschnitten angegeben.
  </GridItem>
</Grid>

## Verweise auf Abschnitte und Seiten

Um einen Link zu einem Abschnitt oder einer Seite zu erstellen, muss der
*Abschnittspfad* bzw. der *Seitenname* als Parameter angegebenen werden. Die
Route und der Parameter werden mit dem Pipe-Symbol `|` voneinander getrennt.
Wird kein Linktext angegeben, so wird automatisch der Titel des Linkziels
eingefügt.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      [](app:section|02-elements/04-media)  
      [anderer Abschnitt](app:section|02-elements/04-media)  
      [](app:page|about)  
      [andere Seite](app:page|about)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      [](app:section|02-elements/04-media)  
      [anderer Abschnitt](app:section|02-elements/04-media)  
      [](app:page|about)  
      [andere Seite](app:page|about)
      ```
    </TabItem>
  </Tabs>
</Example>

<Info>
  Wenn ein verlinkter Abschnitt bzw. eine Seite nicht existiert, wird ein
  Fehlertext dargestellt:  
  [Dies ist ein Link zu einem nicht existierendem Kapitel.](/section/does-not-exist)
</Info>

## Verweise auf Elemente {#referencing-elements}

Um auf ein bestimmtes Element innerhalb eines Abschnitts zu verweisen, werden
*Anker-IDs* verwendet. Diese müssen innerhalb eines Dokuments einzigartig sein
und können manuell zugewiesen werden.

Inhaltselementen können Anker-IDs zugewiesen werden, indem der Bezeichner mit
einem vorangestelltem `#` angegeben wird. So lassen sich etwa Überschriften,
aber auch andere Elemente referenzieren.

<Example>
  Link zu Überschrift mit händisch vergebener ID.

  <Tabs>
    <TabItem label="Ergebnis">
      ### Überschrift mit ID {#my-id}

      [Link zur Überschrift](#my-id)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      ### Überschrift mit ID {#my-id}

      [Link zur Überschrift](#my-id)
      ```
    </TabItem>
  </Tabs>

  Wird keine explizit angegeben, so erhalten Überschriften automatisch eine vom
  Text abgeleitete ID. Aus Konsistenzgründen vor allem bei mehrsprachigen Texten
  wird dazu geraten, referenzierten Überschriften manuell eine explizite ID
  zuzuweisen.

  <Tabs>
    <TabItem label="Ergebnis">
      ### Überschrift mit automatischer ID

      [Link zur Überschrift](#überschrift-mit-automatischer-id)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      ### Überschrift mit automatischer ID

      [Link zur Überschrift](#überschrift-mit-automatischer-id)
      ```
    </TabItem>
  </Tabs>

  Link zur Überschrift _Videos_ in einem anderen Kapitel:

  <Tabs>
    <TabItem label="Ergebnis">
      [Unterabschnitt _Videos_ im Kapitel _Bilder und Videos_](/section/02-elements/04-media#videos)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      [Unterabschnitt _Videos_ im Kapitel _Bilder und Videos_](/section/02-elements/04-media#videos)
      ```
    </TabItem>
  </Tabs>
</Example>

## Verweise auf andere Seiten

In jedem Kurs gibt es weitere Seiten, wie das Stichwort- und Inhaltsverzeichnis.
Diese werden durch die Verwendung der entsprechenden Route referenziert.

<Example>
  <Tabs>
    <TabItem label="Ergebnis">
      [](app:home)  
      [](app:progress)  
      [](app:toc)
    </TabItem>
    <TabItem label="Markdown">
      ```markdown
      [](app:home)  
      [](app:progress)  
      [](app:toc)
      ```
    </TabItem>
  </Tabs>
</Example>

### Übersicht der Routen {#routes}

Nachfolgend eine Übersicht der verfügbaren Applikationsrouten.

<Table>
  <Caption>Applikationsrouten</Caption>
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
</Table>
