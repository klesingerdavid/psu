import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("mtcars.csv", "rb"),
                  usecols=(1,2,3,4,5,6),
                  delimiter=",",
                  skiprows=1)

mpg = data[:, 0]
cyl = data[:, 1]
hp  = data[:, 3]
wt  = data[:, 5]

plt.scatter(hp, mpg, s=wt*50)
plt.xlabel("Konjske snage (hp)")
plt.ylabel("Potrošnja (mpg)")
plt.title("Ovisnost mpg o hp (veličina = težina)")
plt.show()

print("Svi automobili:")
print("Minimalni mpg:", np.min(mpg))
print("Maksimalni mpg:", np.max(mpg))
print("Srednji mpg:", np.mean(mpg))

mpg_6 = mpg[cyl == 8]

print("\nAutomobili sa 6 cilindara:")
print("Minimalni mpg:", np.min(mpg_6))
print("Maksimalni mpg:", np.max(mpg_6))
print("Srednji mpg:", np.mean(mpg_6))