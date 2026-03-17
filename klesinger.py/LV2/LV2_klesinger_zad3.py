import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('tiger.png')  
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  

# a) Posvijetliti sliku (povećati brightness)
brightness_factor = 50
bright_img = np.clip(img + brightness_factor, 0, 255).astype(np.uint8)

# b) Rotirati sliku za 90 stupnjeva u smjeru kazaljke na satu
rotated_img = np.rot90(img, k=3)  # k=3 jer np.rot90 rotira CCW, pa 3 puta = 90° CW

# c) Zrcaliti sliku (horizontalno)
mirrored_img = np.fliplr(img)

# d) Smanjiti rezoluciju slike x puta
scale_factor = 10
small_img = img[::scale_factor, ::scale_factor]

# e) Prikazati samo drugu četvrtinu slike po širini
height, width, channels = img.shape
quarter_img = np.zeros_like(img)
quarter_img[:, width//4:width//2, :] = img[:, width//4:width//2, :]

# Prikaz svih rezultata
plt.figure(figsize=(15,10))

plt.subplot(2,3,1)
plt.title('Original')
plt.imshow(img)
plt.axis('off')

plt.subplot(2,3,2)
plt.title('Brightened')
plt.imshow(bright_img)
plt.axis('off')

plt.subplot(2,3,3)
plt.title('Rotated 90° CW')
plt.imshow(rotated_img)
plt.axis('off')

plt.subplot(2,3,4)
plt.title('Mirrored')
plt.imshow(mirrored_img)
plt.axis('off')

plt.subplot(2,3,5)
plt.title(f'Reduced Resolution x{scale_factor}')
plt.imshow(small_img)
plt.axis('off')

plt.subplot(2,3,6)
plt.title('Second Quarter Only')
plt.imshow(quarter_img)
plt.axis('off')

plt.show()