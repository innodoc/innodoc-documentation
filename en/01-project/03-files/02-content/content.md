---
title: content.md
---

In jedem Inhalts-Ordner befindet sich eine content.md Datei.

Am Anfang der Datei befindet sich ein [YAML](http://yaml.org/)-Block, in dem der
Titel dieses Kapitels definiert wird. Dies ist auch der Name, unter dem dieser
Kapitel im Index zu sehen ist. Dies könntre zum Beispiel so aussehen:

```yaml
---
title: Titel des Kapitels
---
```

Die restliche Datei ist der eigentliche Inhalt des Kapitels, der dargestellt
werden soll. Dabei stehen verschiedene [Elemente](/02-elements) zur Verfügung,
um eine [Strukturierung des Kapitels](/02-elements/01-headers),
[Texformatierung](/02-elements/03-links-and-formatting/01-formatting),
[Verlinkung](/02-elements/03-links-and-formatting/02-links),
[mediale Einbindung](/02-elements/06-media), usw. vorzunehmen.

Hier Beispiel für den Inhalt einer Solchen Datei:

```markdown
Lorem markdownum casus, generosior **spectata** metu in fugit. Se lepori animo
haec, utilis [examinat utero ubi](http://viscera.com/currantopprimere.php)
filius animata posse.

1. Vulnere suis vicinaque est soror cognatas timidusque
2. Dedit quoque quotiens neque ferrea luctus transitus
3. Cibos movebatur florente carmina verterit inplumes deditque

```
