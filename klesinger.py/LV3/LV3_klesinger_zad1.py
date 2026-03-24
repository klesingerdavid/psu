import pandas as pd

df = pd.read_csv("mtcars.csv")

# ako postoji stupac za ime auta kao index, preimenuj ga

if 'Unnamed: 0' in df.columns:
    df = df.rename(columns={'Unnamed: 0': 'car'})

# 1. 5 automobila s najvećom potrošnjom (mpg)

top5 = df.sort_values(by="mpg", ascending=False).head(5)
print("1. Top 5 auta s najvećom potrošnjom:")
print(top5[["car", "mpg"]])
print()

# 2. 3 auta s 8 cilindara i najmanjom potrošnjom

v8 = df[df["cyl"] == 8]
v8_najmanje = v8.sort_values(by="mpg", ascending=True).head(3)
print("2. 3 auta s 8 cilindara i najmanjom potrošnjom:")
print(v8_najmanje[["car", "mpg"]])
print()

# 3. srednja potrošnja za 6 cilindara

v6 = df[df["cyl"] == 6]
avg_v6 = v6["mpg"].mean()
print("3. Prosječna potrošnja (6 cilindara):", avg_v6)
print()

# 4. srednja potrošnja za 4 cilindra i masu između 2000 i 2200 lbs

v4 = df[(df["cyl"] == 4) & (df["wt"]*1000 >= 2000) & (df["wt"]*1000 <= 2200)]
avg_v4 = v4["mpg"].mean()
print("4. Prosječna potrošnja (4 cilindra, 2000-2200 lbs):", avg_v4)
print()

# 5. broj auta po mjenjaču (0=automatski, 1=ručni)

manual = df[df["am"] == 1].shape[0]
auto = df[df["am"] == 0].shape[0]
print("5. Ručni:", manual, "Automatski:", auto)
print()

# 6. broj auta s automatskim mjenjačem i preko 100 KS

auto_100hp = df[(df["am"] == 0) & (df["hp"] > 100)].shape[0]
print("6. Automatski i >100 KS:", auto_100hp)
print()

# 7. masa svakog auta u kg 

df["wt_kg"] = df["wt"] * 1000 * 0.453592
print("7. Masa auta u kg:")
print(df[["car", "wt_kg"]])
print(df.describe())