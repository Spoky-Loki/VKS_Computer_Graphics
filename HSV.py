import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

def show():
    return 0


def task3(name):
    root = Tk()
    root.title("Task3")
    root.geometry("700x600")

    h = Entry()
    h.pack(anchor=NW, padx=6, pady=6)

    s = Entry()
    s.pack(anchor=NW, padx=6, pady=6)

    v = Entry()
    v.pack(anchor=NW, padx=6, pady=6)

    btn = Button(text="Click", command=show)
    btn.pack(anchor=NW, padx=6, pady=6)

    img = PhotoImage(file=name)
    Label(root, image=img).pack()

    root.mainloop()


def fromHSVtoRGB(image):
    res = []
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            r = 255.0 / float(image[i][j][0])
            g = 255.0 / float(image[i][j][1])
            b = 255.0 / float(image[i][j][2])
            maxi = max(r, g, b)
            mini = max(r, g, b)
            v = maxi
            s = 0
            if maxi != 0:
                s = 1 - mini / maxi
            h = 0
            if maxi != mini:
                if maxi == r:
                    if g >= b:
                        h = 60 * (g - b) / (maxi - mini)
                    else:
                        h = 60 * (g - b) / (maxi - mini) + 360
                if maxi == g:
                    h = 60 * (b - r) / (maxi - mini) + 120
                else:
                    h = 60 * (r - g) / (maxi - mini) + 240
            res.append([h, s, v])
    return res


def fromRGBtoHSV(image):
    res = []
    for i in range(0, len(image)):
        for j in range(0, len(image[0])):
            r = 255.0 / float(image[i][j][0])
            g = 255.0 / float(image[i][j][1])
            b = 255.0 / float(image[i][j][2])
            maxi = max(r, g, b)
            mini = max(r, g, b)
            v = maxi
            s = 0
            if maxi != 0:
                s = 1 - mini / maxi
            h = 0
            if maxi != mini:
                if maxi == r:
                    if g >= b:
                        h = 60 * (g - b) / (maxi - mini)
                    else:
                        h = 60 * (g - b) / (maxi - mini) + 360
                if maxi == g:
                    h = 60 * (b - r) / (maxi - mini) + 120
                else:
                    h = 60 * (r - g) / (maxi - mini) + 240
            res.append([h, s, v])
    return res

#image = np.array(Image.open("test.png").convert("RGB"))
#fromRGBtoHSV(image)
