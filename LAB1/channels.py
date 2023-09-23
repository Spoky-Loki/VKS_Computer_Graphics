import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt


def histogram(image):
    r = []
    g = []
    b = []
    indexes = []
    for i in range(0, 256):
        indexes.append(i)
        r.append(0)
        g.append(0)
        b.append(0)
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            r[image[i][j][0]] += 1
            g[image[i][j][1]] += 1
            b[image[i][j][2]] += 1
    plt.plot(indexes, r, color="red")
    plt.plot(indexes, g, color="green")
    plt.plot(indexes, b, color="blue")
    plt.show()


def channels(image_r, image_g, image_b):
    pixels_r = image_r.load()
    pixels_g = image_g.load()
    pixels_b = image_b.load()
    width, height = image_r.size
    for i in range(width):
        for j in range(height):
            r, g, b = image_r.getpixel((i, j))
            pixels_r[i, j] = (r, 0, 0)
            pixels_g[i, j] = (0, g, 0)
            pixels_b[i, j] = (0, 0, b)
    image_r.show()
    image_g.show()
    image_b.show()


def task2(name):
    image = np.array(Image.open(name).convert("RGB"))
    histogram(image)
    image1 = Image.open(name)
    image2 = Image.open(name)
    image3 = Image.open(name)
    channels(image1, image2, image3)


task2("test.jpg")
