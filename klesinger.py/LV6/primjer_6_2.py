# -*- coding: utf-8 -*-
"""
Created on Sun Dec 02 12:08:00 2018

@author: Grbic
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_sample_image

# Učitaj primjer slike (zamjena za scipy.face)
china = load_sample_image("china.jpg")

# Pretvori u grayscale
face = np.mean(china, axis=2)

# Priprema podataka
X = face.reshape((-1, 1))

# KMeans
k_means = KMeans(n_clusters=5, n_init=10, random_state=0)
k_means.fit(X)

values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_

# Rekonstrukcija slike
face_compressed = np.choose(labels, values)
face_compressed = face_compressed.reshape(face.shape)

# Prikaz originalne slike
plt.figure(1)
plt.imshow(face, cmap='gray')
plt.title("Original")
plt.axis('off')

# Prikaz komprimirane slike
plt.figure(2)
plt.imshow(face_compressed, cmap='gray')
plt.title("Compressed")
plt.axis('off')

plt.show()