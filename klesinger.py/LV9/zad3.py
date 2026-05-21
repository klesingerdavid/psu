import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import load_img, img_to_array

model = tf.keras.models.load_model("best_model.h5")

image_path = "znak.jpg"

image = load_img(image_path, target_size=(48, 48))
image = img_to_array(image) / 255.0

image = np.expand_dims(image, axis=0)

prediction = model.predict(image)

predicted_class = np.argmax(prediction)

print("Predvidjena klasa:", predicted_class)