import numpy as np
from matplotlib import pyplot as plt
import matplotlib as mpl
mpl.use("pgf")
mpl.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})


# Señal analógica
# Senoide de amplitud 5V y frecuencia 100Hz
f = 100             # frecuencia
w = 2*np.pi*f       # velocidad angular
T = 1/f             # periodo
A = 5               # amplitud

tiempo = np.arange(0,5*T,T/100) #como range pero con flotantes -> argumentos (inicio, fin, paso)
senoide = A*np.sin(w*tiempo)

plt.figure(figsize=(6, 2))
plt.xlabel("tiempo (ms)")
plt.ylabel("voltaje (V)")
plt.plot(tiempo*1000,senoide) # argumentos -> (x,y)
plt.show()

plt.savefig('sine.pgf')