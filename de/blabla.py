import numpy as np
import matplotlib.pyplot as plt

# Erstellung eines Plots mit matplotlib, dieser wird dann gespeichert und als Grafik im LaTeX-Code eingebunden
ax = plt.subplot(111)
t = np.arange(-6.0, 6.0, 0.02)
s = (t - 2) * (t - 1) * t * (t + 1) * (t + 2)
line, = plt.plot(t, s, lw = 2)
fname = "pybild.png"
plt.savefig(fname, transparent = True, dpi = 600)
plt.clf()
plt.cla()
plt.close()

print("Hier ein Python-erzeugtes richtig hochauflösendes Bild:\\\\\\MUGraphicsSolo{" + fname + "}{width=0.8\\linewidth}{width:400px}\\ \\\\")
print("Und etwas schleifengeneriertes BlaBla:\\")
for k in range(100):
    print("Bla" + str(k) + " ")
