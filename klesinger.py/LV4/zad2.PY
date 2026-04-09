import matplotlib.pyplot as plt

plt.scatter(X_train["Engine Size (L)"], y_train, color='blue', label='Train')
plt.scatter(X_test["Engine Size (L)"], y_test, color='red', label='Test')

plt.xlabel("Engine size")
plt.ylabel("CO2 emissions")
plt.legend()
plt.show()