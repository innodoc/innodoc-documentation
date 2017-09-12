import random # neben random können weitere Python3-module importiert werden
#import numpy as np
#import matplotlib.pyplot as plt

# Jede automatisierte Aufgabe definiert eine generate-Funktion, die eine seed-Nummer für den Zufallsgenerator
# (oder andere Anwendungen) erhält sowie ein Präfix, dass vor alle UXIDs gesetzt werden sollte.
# Die genereate-Funktion liefert einen String mit LaTeX-Befehlen zurück.
def generate(exid, prefix):

    # Zufallsgenerator MUSS mit der Aufgaben-ID initialisiert werden
    random.seed(exid)

    # Vorberechnung der Aufgabenbausteine und Lösungen
    a = random.randint(-3, 3)
    b = random.randint(-3, 3)

    # Erstellung eines Plots mit matplotlib, dieser wird dann gespeichert und als Grafik im LaTeX-Code eingebunden
    # ax = plt.subplot(111)
    p = random.randint(-3, 3)
    # t = np.arange(-6.0, 6.0, 0.02)
    # s = (t - a) * (t - b)
    # line, = plt.plot(t, s, lw = 2)
    fname = "IMG_" + prefix + ".png"
    # plt.savefig(fname, transparent = True, dpi = 180)
    # plt.clf()
    # plt.cla()
    # plt.close()

    # Erstellung des LaTeX-Texts für die Aufgabe
    text = "Der abgebildete Funktionsgraph gehört zu einer Parabelfunktion der Form $f(x)=x^2+px+q$:\\\\"
    text = text + "\\MUGraphicsSolo{" + fname + "}{width=0.5\\linewidth}{width:550px}\\ \\\\"
    text += '\\begin{html}'
    text += '<div id="jsxbox_' + str(prefix) + str(exid) + '" class="jxgbox" style="width:500px; height:500px;">'
    text += 'var p = board.create("point",[1,1],{size:4,name:"A"});'
    text += 'board.create("functiongraph", [function(x){return (x-(' + str(a) + ')) * (x-(' + str(b) +')) ;}]);'
    text += '</div>'
    text += '\\end{html}'
    text = text + "Der Funktionsgraph verläuft durch die Punkte $P(0|" + str(a * b) + ")$ sowie $Q(" + str(p) + "|" + str((p - a) * (p - b)) + ")$.\n"
    text = text + "Wie lautet die Funktionsvorschrift?\\ \\\\ \\ \\\\"
    text = text + "Antwort: \\MEquationItem{$f(x)$}{\\MLSimplifyQuestion{25}{(x-(" + str(a) + "))*(x-(" + str(b) + "))}{5}{x}{5}{0}{" + prefix + "_fx" + "}}\\ \\\\ \\ \\\\"
    text = text + "Die Nullstellenmenge dieser Funktion ist \\MLParsedQuestion{12}{" + str(a) + "," + str(b) + "}{2}{" + prefix + "_1" + "}\\ \\\\"
    text = text + "\\MInputHint{Geben Sie Mengen in der Form \\texttt{\\{i;j;k;}$\\ldots$\\texttt{\\}} an.}"

    return text
