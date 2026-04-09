import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#a)
data = pd.read_csv("data_C02_emission.csv")

features = ["Engine Size (L)", "Cylinders", "Fuel Consumption City (L/100km)", "Fuel Consumption Hwy (L/100km)", "Fuel Consumption Comb (L/100km)"]

X = data[features]
y = data["CO2 Emissions (g/km)"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)


#b)
import matplotlib.pyplot as plt

plt.scatter(X_train["Engine Size (L)"], y_train, color='blue', label='Train')
plt.scatter(X_test["Engine Size (L)"], y_test, color='red', label='Test')

plt.xlabel("Engine size")
plt.ylabel("CO2 emissions")
plt.legend()
plt.show()

#c)
sc = StandardScaler()

plt.hist(X_train["Engine Size (L)"], bins=30)
plt.title("Prije skliranja")
plt.show()

X_train_scaled = sc.fit_transform(X_train)
X_test_scaled = sc.transform(X_test)

plt.hist(X_train_scaled[:,0], bins=30)
plt.title("Nakon skaliranja")
plt.show()

