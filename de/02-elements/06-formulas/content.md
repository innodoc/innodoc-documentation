---
title: Formeln
---

Es können in einem Kurs auch $\LaTeX$-Formeln verwendet werden.

Alles, was zwischen zwei '\$' steht, und dabei weder mit einem Leerzeichen beginnt
noch mit einem Leerzeichen endet, wird als TeX-Mathe-Formel interpretiert (direkt
nach dem Abschließenden '\$' darf dabei keine Zahl stehen). Dadurch wird $123,456$
oder $( x_F \equiv p_z^{}/p^{\mathrm{MAX}}_z = p_z/(\sqrt{s}/2) = 2p_z/\sqrt s )$
als $\LaTeX$ interpretiert, aber $100 und $200,00 nicht

Braucht man in einem TeX-Teil das '$' Zeichen, dann kann das mit \\\$ darstellen, z.B.
$\$100.00-\$50.00=\$50.00$

Es gibt auch die Möglichkeit, eigenständige, mehrzeilige TeX-Mathe-Blöcke zu
definieren. Solch ein Block beginnt und endet mit '\$\$', und befolgt ansonsten die
gleichen Regeln wie die Teile mit einzelnen '$'

$$\begin{align*}
\sum_{i=1}^{k+1}i & = \left(\sum_{i=1}^{k}i\right) +(k+1)\\ 
& = \frac{k(k+1)}{2}+k+1 & (\text{by inductive hypothesis})\\
& = \frac{k(k+1)+2(k+1)}{2}\\
& = \frac{(k+1)(k+2)}{2}\\
& = \frac{(k+1)((k+1)+1)}{2}.
\end{align*}$$

Zusätzlich zum Normalen $\LaTeX$ gibt es noch einige Erweiterungen, die man benutzen kann.

Es steht \\num{Zahl} zur Verfügung, welches Zahl je nach ausgewählter Sprache mit
'.' oder "," als Dezimaltrennzeichen anzeigt. z.B. \\num{0.5} kann je anch Sprache
als '0.5' oder '0,5' dargestellt werden. Dabei sind \\num{0,5} und \\num{0.5} äqui­va­lent.

$$\dfrac{1}{2} = \num{0.5} \,, \,\, \dfrac{1}{3} = \num{0.33333}\ldots= \num{0.}\bar{3} \,, \,\, \dfrac{1}{7} = \num{0.}\overline{142857} \,, \,\, \dfrac{1}{8} = \num{0.125} \, .$$

Weiters gibt es \\decmarker, welches je nach ausgewählter Sprache das
Dezimaltrennzeichen ausgibt, also entweder '.' oder ','

$$\dfrac{1}{n} \overset{n > 1}= 0 \decmarker \ldots$$

Schließlich gibt es \\coordsep, welches das Trennzeichen für Koordinaten
ausgibt: \coordsep

$$A = (3\coordsep 5) \\ B = (5\coordsep 3)$$

