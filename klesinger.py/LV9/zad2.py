import os
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dropout, Flatten, Dense
from tensorflow.keras.callbacks import ModelCheckpoint, TensorBoard
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score

train_path = "GTSRB/Train"
test_csv = "GTSRB/Test.csv"
test_path = "GTSRB/Test"

images = []
labels = []

for class_id in os.listdir(train_path):
    class_dir = os.path.join(train_path, class_id)

    if os.path.isdir(class_dir):
        csv_file = os.path.join(class_dir, f"GT-{class_id}.csv")
        df = pd.read_csv(csv_file, sep=';')

        for _, row in df.iterrows():
            img_path = os.path.join(class_dir, row['Filename'])
            image = load_img(img_path, target_size=(48, 48))
            image = img_to_array(image) / 255.0

            images.append(image)
            labels.append(row['ClassId'])

X = np.array(images)
y = np.array(labels)

y = tf.keras.utils.to_categorical(y, 43)

X_train, X_val, y_train, y_val = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = Sequential()

model.add(Conv2D(32, (3, 3), strides=1, padding='same', activation='relu', input_shape=(48, 48, 3)))
model.add(Conv2D(32, (3, 3), strides=1, padding='valid', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))

model.add(Conv2D(64, (3, 3), strides=1, padding='same', activation='relu'))
model.add(Conv2D(64, (3, 3), strides=1, padding='valid', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))

model.add(Conv2D(128, (3, 3), strides=1, padding='same', activation='relu'))
model.add(Conv2D(128, (3, 3), strides=1, padding='valid', activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2), strides=2))

model.add(Dropout(0.2))

model.add(Flatten())

model.add(Dense(512, activation='relu'))

model.add(Dropout(0.5))

model.add(Dense(43, activation='softmax'))

model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

checkpoint = ModelCheckpoint(
    "best_model.h5",
    monitor='val_accuracy',
    save_best_only=True,
    mode='max'
)

tensorboard = TensorBoard(log_dir="logs")

model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=64,
    validation_data=(X_val, y_val),
    callbacks=[checkpoint, tensorboard]
)

model = tf.keras.models.load_model("best_model.h5")

test_df = pd.read_csv(test_csv)

X_test = []
y_test = []

for _, row in test_df.iterrows():
    img_path = os.path.join(test_path, row['Path'].split('/')[-1])

    image = load_img(img_path, target_size=(48, 48))
    image = img_to_array(image) / 255.0

    X_test.append(image)
    y_test.append(row['ClassId'])

X_test = np.array(X_test)
y_test = np.array(y_test)

predictions = model.predict(X_test)

y_pred = np.argmax(predictions, axis=1)

accuracy = accuracy_score(y_test, y_pred)

print("Tacnost:", accuracy)

cm = confusion_matrix(y_test, y_pred)

print("Matrica zabune:")
print(cm)