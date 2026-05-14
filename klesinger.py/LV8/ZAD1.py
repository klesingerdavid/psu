from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

tensorboard_cb = callbacks.TensorBoard(
    log_dir='logs',
    histogram_freq=1
)

checkpoint_cb = callbacks.ModelCheckpoint(
    'best_model.keras',
    monitor='val_accuracy',
    save_best_only=True,
    mode='max'
)

history = model.fit(
    x_train_s,
    y_train_s,
    epochs=10,
    batch_size=128,
    validation_split=0.1,
    callbacks=[tensorboard_cb, checkpoint_cb]
)

best_model = keras.models.load_model('best_model.keras')

train_pred = np.argmax(best_model.predict(x_train_s), axis=1)
test_pred = np.argmax(best_model.predict(x_test_s), axis=1)

train_acc = accuracy_score(y_train, train_pred)
test_acc = accuracy_score(y_test, test_pred)

print("Train accuracy:", train_acc)
print("Test accuracy:", test_acc)

cm_train = confusion_matrix(y_train, train_pred)
cm_test = confusion_matrix(y_test, test_pred)

print("Confusion matrix - train:")
print(cm_train)

print("Confusion matrix - test:")
print(cm_test)