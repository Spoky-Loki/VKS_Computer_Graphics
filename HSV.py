from tkinter import *
from tkinter.ttk import Scale
from PIL import Image, ImageTk


def saveImage():
    new_image = replacePixelsToImage(image, fromHSVtoRGB(fromRGBtoHSV(image)))
    new_image.save("modified_image.jpg")


def changeH(local_h):
    global h_value
    h_value = local_h
    new_image = ImageTk.PhotoImage(replacePixelsToImage(small_image, fromHSVtoRGB(fromRGBtoHSV(small_image))))
    panel.configure(image=new_image)
    panel.image = new_image


def changeS(local_s):
    global s_value
    s_value = local_s
    res = fromRGBtoHSV(small_image)
    res2 = fromHSVtoRGB(res)
    new_image = replacePixelsToImage(small_image, res2)
    img2 = ImageTk.PhotoImage(new_image)
    panel.configure(image=img2)
    panel.image = img2


def changeV(local_v):
    global v_value
    v_value = local_v
    res = fromRGBtoHSV(small_image)
    res2 = fromHSVtoRGB(res)
    new_image = replacePixelsToImage(small_image, res2)
    img2 = ImageTk.PhotoImage(new_image)
    panel.configure(image=img2)
    panel.image = img2


def replacePixelsToImage(image_rgb, new_pixels):
    image_rgb_2 = image_rgb.copy()
    pixels = image_rgb_2.load()
    width_rgb, height_rgb = image_rgb_2.size
    for i in range(width_rgb):
        for j in range(height_rgb):
            pixels[i, j] = (new_pixels[i][j][0], new_pixels[i][j][1], new_pixels[i][j][2])
    return image_rgb_2


def fromHSVtoRGB(image_hsv):
    res = []
    for i in range(0, len(image_hsv)):
        line = []
        for j in range(0, len(image_hsv[0])):
            local_h = image_hsv[i][j][0]
            local_s = image_hsv[i][j][1]
            local_v = image_hsv[i][j][2]
            c = local_v * local_s
            x = c * (1 - abs((local_h / 60.0) % 2 - 1))
            m = local_v - c
            h_i = int(float(local_h) / 60.0) % 6
            if h_i == 0:
                r = c
                g = x
                b = 0
            elif h_i == 1:
                r = x
                g = c
                b = 0
            elif h_i == 2:
                r = 0
                g = c
                b = x
            elif h_i == 3:
                r = 0
                g = x
                b = c
            elif h_i == 4:
                r = x
                g = 0
                b = c
            else:
                r = c
                g = 0
                b = x
            line.append([int(255 * (r + m)), int(255 * (g + m)), int(255 * (b + m))])
        res.append(line)
    return res


def fromRGBtoHSV(image_rgb):
    width_rgb, height_rgb = image_rgb.size
    res = []
    for i in range(width_rgb):
        line = []
        for j in range(height_rgb):
            r, g, b = image_rgb.getpixel((i, j))
            r /= 255.0
            g /= 255.0
            b /= 255.0
            maxi = max(r, g, b)
            mini = min(r, g, b)
            delta = maxi - mini
            local_v = maxi
            local_s = 0
            if maxi != 0:
                local_s = 1 - mini / maxi
            local_h = 0
            if delta != 0:
                if maxi == r:
                    local_h = 60 * ((g - b) / delta % 6)
                elif maxi == g:
                    local_h = 60 * ((b - r) / delta + 2)
                else:
                    local_h = 60 * ((r - g) / delta + 4)
            line.append([local_h + float(h_value), local_s + float(s_value), local_v + float(v_value)])
        res.append(line)
    return res


h_value = 0.0
s_value = 0.0
v_value = 0.0

filename = "ФРУКТЫ.jpg"

image = Image.open(filename)
width, height = image.size
new_width = 400
new_height = int(new_width * height / width)
#small_image = Image.open(filename)
small_image = image.resize((new_width, new_height))

if new_height < 100:
    new_height = 100
root = Tk()
root.title("Task3")
root.geometry(str(new_width + 200) + "x" + str(new_height + 20))

img = ImageTk.PhotoImage(small_image)
panel = Label(root, image=img)
panel.pack(padx=10, pady=10, anchor=W)

text_h = Label(root, text="H")
text_h.place(x=new_width + 20, y=10 + new_height / 2 - 40, anchor=W, width=20, height=40)
h = Scale(root, from_=0.0, to=360.0, value=0.0, command=changeH)
h.place(x=new_width + 40, y=10 + new_height / 2 - 40, anchor=W, width=150, height=40)

text_s = Label(root, text="S")
text_s.place(x=new_width + 20, y=10 + new_height / 2, anchor=W, width=20, height=40)
s = Scale(root, from_=0.0, to=1.0, value=0.0, command=changeS)
s.place(x=new_width + 40, y=10 + new_height / 2, anchor=W, width=150, height=40)

text_v = Label(root, text="V")
text_v.place(x=new_width + 20, y=10 + new_height / 2 + 40, anchor=W, width=20, height=40)
v = Scale(root, from_=0.0, to=1.0, value=0.0, command=changeV)
v.place(x=new_width + 40, y=10 + new_height / 2 + 40, anchor=W, width=150, height=40)

button = Button(root, text="SAVE", command=saveImage)
button.place(x=new_width + 20, y=new_height, anchor=SW, width=170, height=25)

root.mainloop()
