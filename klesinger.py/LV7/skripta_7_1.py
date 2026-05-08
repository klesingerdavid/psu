import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# 1. PRIKAZ NEKOLIKO SLIKA IZ TRAIN SKUPA

plt.figure(figsize=(10, 5))

for i in range(10):
    plt.subplot(2, 5, i + 1)
    plt.imshow(x_train[i], cmap="gray")
    plt.title(f"Label: {y_train[i]}")
    plt.axis("off")

plt.tight_layout()
plt.show()

# PRIPREMA PODATAKA

# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)

# 2. KREIRANJE NEURONSKE MREZE

model = keras.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(128, activation='relu'),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

# Prikaz strukture mreze
model.summary()

# 3. DEFINICIJA PROCESA UCENJA

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# 4. TRENIRANJE MREZE

history = model.fit(
    x_train_s,
    y_train_s,
    epochs=10,
    batch_size=128,
    validation_split=0.1
)

# 5. TOCNOST NA TRAIN I TEST SKUPU

train_loss, train_acc = model.evaluate(x_train_s, y_train_s, verbose=0)
test_loss, test_acc = model.evaluate(x_test_s, y_test_s, verbose=0)

print(f"\nTocnost na train skupu: {train_acc:.4f}")
print(f"Tocnost na test skupu: {test_acc:.4f}")

# 6. MATRICA ZABUNE

# Predikcije
y_train_pred = np.argmax(model.predict(x_train_s), axis=1)
y_test_pred = np.argmax(model.predict(x_test_s), axis=1)

# Matrica zabune - TRAIN
cm_train = confusion_matrix(y_train, y_train_pred)

plt.figure(figsize=(8, 8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm_train)
disp.plot(cmap="Blues")
plt.title("Matrica zabune - Train skup")
plt.show()

# Matrica zabune - TEST
cm_test = confusion_matrix(y_test, y_test_pred)

plt.figure(figsize=(8, 8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm_test)
disp.plot(cmap="Reds")
plt.title("Matrica zabune - Test skup")
plt.show()

# 7. POGRESNO KLASIFICIRANI PRIMJERI

# Pronadi pogresno klasificirane slike
wrong = np.where(y_test != y_test_pred)[0]

# Prikazi nekoliko pogresnih primjera
plt.figure(figsize=(12, 8))

for i in range(10):
    index = wrong[i]

    plt.subplot(2, 5, i + 1)
    plt.imshow(x_test[index], cmap="gray")

    plt.title(
        f"Stvarna: {y_test[index]}\nPredikcija: {y_test_pred[index]}"
    )

    plt.axis("off")

plt.tight_layout()
plt.show()