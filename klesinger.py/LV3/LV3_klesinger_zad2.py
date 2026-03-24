import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("mtcars.csv")

if 'Unnamed: 0' in df.columns:
    df = df.rename(columns={'Unnamed: 0': 'car'})
avg_mpg = df.groupby("cyl")["mpg"].mean()

plt.figure()
avg_mpg.plot(kind="bar")
plt.title("Prosječna potrošnja po broju cilindara")
plt.xlabel("Cilindri")
plt.ylabel("mpg")
plt.show()


plt.figure()
df.boxplot(column="wt", by="cyl")
plt.title("Distribucija težine po cilindrima")
plt.suptitle("") 
plt.xlabel("Cilindri")
plt.ylabel("Težina (1000 lbs)")
plt.show()


plt.figure()

manual = df[df["am"] == 1]["mpg"]
auto = df[df["am"] == 0]["mpg"]

plt.boxplot([auto, manual], labels=["Automatski", "Ručni"])
plt.title("Potrošnja: ručni vs automatski")
plt.ylabel("mpg")
plt.show()


plt.figure()

auto = df[df["am"] == 0]
manual = df[df["am"] == 1]

plt.scatter(auto["hp"], auto["qsec"], label="Automatski")
plt.scatter(manual["hp"], manual["qsec"], label="Ručni")

plt.xlabel("Snaga (hp)")
plt.ylabel("Ubrzanje (qsec)")
plt.title("Odnos snage i ubrzanja")
plt.legend()
plt.show()