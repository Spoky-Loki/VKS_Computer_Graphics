import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

filename = "ФРУКТЫ.jpg"

input_image1 = Image.open(filename)
input_image2 = Image.open(filename)
input_image_diff = Image.open(filename)

pixel_map1 = input_image1.load()
pixel_map2 = input_image2.load()
pixel_map_diff = input_image_diff.load()

width, height = input_image1.size

for i in range(width):
    for j in range(height):
        r, g, b = input_image1.getpixel((i, j))

        grayscale1 = (0.299 * r + 0.587 * g + 0.114 * b)
        grayscale2 = (0.2126 * r + 0.7152 * g + 0.0722 * b)

        pixel_map1[i, j] = (int(grayscale1), int(grayscale1), int(grayscale1))
        pixel_map2[i, j] = (int(grayscale2), int(grayscale2), int(grayscale2))
        pixel_map_diff[i, j] = (int(abs(grayscale1 - grayscale2)), int(abs(grayscale1 - grayscale2)), int(abs(grayscale1 - grayscale2)))

#input_image1.show()
#input_image2.show()
#input_image_diff.show()

image_1 = np.array(input_image1)
image_2 = np.array(input_image2)
image_3 = np.array(input_image_diff)

r = []
g = []
b = []
indexes = []
for i in range(0, 256):
        r.append(0)
        g.append(0)
        b.append(0)
        indexes.append(i)

for i in range(0, height):
    for j in range(0, width):
        r[image_1[i][j][0]] += 1
        g[image_2[i][j][1]] += 1
        b[image_3[i][j][1]] += 1

plt.plot(indexes, r)
plt.show()
plt.plot(indexes, g)
plt.show()
plt.plot(indexes, b)
plt.show()