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

input_image1.show()
input_image2.show()
input_image_diff.show()

histogram = input_image1.histogram()
plt.hist(histogram, bins=256, color='blue', alpha=0.7)
plt.show()

histogram = input_image2.histogram()
plt.hist(histogram, bins=256, color='blue', alpha=0.7)
plt.show()
