import numpy as np
import matplotlib.pyplot as plt

tocke = np.array([
    [1, 1],
    [2, 2],
    [3, 2],
    [3, 1],
    [1, 1]  
])

x = tocke[:, 0]
y = tocke[:, 1]

plt.plot(x, y, marker='.', markersize=12, color='r')

plt.title("Primjer")
plt.xlabel("x os")
plt.ylabel("y os")
plt.xlim(0, 4)
plt.ylim(0, 4)

plt.show()










#numpy polje definira sa pozivanjem funkcije array  ndim- broj dimenzija shape - dimenzija polja size - ukupni broj elemnata