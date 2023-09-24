import math
from tkinter import *


def draw_line_br(x1=0, y1=0, x2=0, y2=0):
    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    dist_x = abs(dx)
    dist_y = abs(dy)

    if dist_x > dist_y:
        pdx, pdy = sign_x, 0
        l, h = dist_y, dist_x
    else:
        pdx, pdy = 0, sign_y
        l, h = dist_x, dist_y

    x, y = x1, y1

    error, t = h / 2, 0

    canvas.create_line(x, y, x + 1, y)

    while t < h:
        error -= l
        if error < 0:
            error += h
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        canvas.create_line(x, y, x + 1, y)


def draw_line_vu(x1=0, y1=0, x2=0, y2=0):
    start_x, end_x = min(x1, x2), max(x1, x2)
    start_y, end_y = min(y1, y2), max(y1, y2)
    is_steep = abs(y2 - y1) > abs(x2 - x1)
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    is_reverse = x1 > x2
    if is_reverse:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = y2 - y1
    slope = dy / dx if dx != 0 else 0

    y = y1
    m = slope * (x1 + 1) - y1
    intensity1 = 1.0 - math.modf(m)[0]
    intensity2 = math.modf(m)[0]

    for x in range(x1, x2 + 1):
        if is_steep:
            my_color = '#%02x%02x%02x' % (255, 120, 0)
            canvas.create_line(y, x, y, x + 1, fill='#' + (f'{int(intensity1 * 255):02x}'*3))
            canvas.create_line(y - 1, x, y - 1, x + 1, fill='#' + (f'{-int(intensity2 * 255):02x}'*3))
        else:
            canvas.create_line(x, y, x + 1, y, fill='#' + (f'{int(intensity1 * 255):02x}'*3))
            canvas.create_line(x, y - 1, x + 1, y - 1, fill='#' + (f'{-int(intensity2 * 255):02x}'*3))
        y += slope
        m = slope * (x + 1) - y
        intensity1 = 1.0 - math.modf(m)[0]
        intensity2 = math.modf(m)[0]


def MouseDown(event):
    global mouse, old_x, old_y
    old_x = event.x
    old_y = event.y
    mouse = True


def MouseUp(event):
    global mouse
    draw_line_br(old_x, old_y, event.x, event.y)
    mouse = False


method = 0
mouse = False
old_x = 0
old_y = 0

root = Tk()
root.title("Task3")
root.geometry("600x400")

canvas = Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.bind("<Button-1>", MouseDown)
canvas.bind("<ButtonRelease-1>", MouseUp)
# button = Button(root, text="SAVE", command=saveImage)
# button.place(x=new_width + 20, y=new_height, anchor=SW, width=170, height=25)

root.mainloop()
