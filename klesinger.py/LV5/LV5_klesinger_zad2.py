import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

df = pd.read_csv("occupancy_processed.csv")

X = df.iloc[:, 0:2]
y = df.iloc[:, 2]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train_s, y_train)

y_pred = knn.predict(X_test_s)

print("d)")
print("Matrica zabune:")
print(confusion_matrix(y_test, y_pred))

print("\nTočnost:")
print(accuracy_score(y_test, y_pred))

print("\nPreciznost po klasama:")
print(precision_score(y_test, y_pred, average=None))

print("\nOdziv po klasama:")
print(recall_score(y_test, y_pred, average=None))

print("\ne)")
print("Manji k -> model osjetljiv na šum (overfitting). Veći k -> model generalizira bolje, ali može izgubiti preciznost (underfitting).")

print("\nf)")
print("Bez skaliranja rezultati su lošiji jer KNN ovisi o udaljenostima, a različite skale atributa utječu na izračun udaljenosti.")