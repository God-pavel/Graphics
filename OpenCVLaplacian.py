import cv2
from matplotlib import pyplot as plt

img = cv2.imread('images/river.jpg')

output = cv2.Laplacian(img, -1)

plt.imshow(output)
plt.show()
