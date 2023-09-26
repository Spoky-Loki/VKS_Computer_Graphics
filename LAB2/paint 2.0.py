import math
from tkinter import *

import numpy as np


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
            canvas.create_line(y, x, y, x + 1, fill='#' + (f'{int(intensity1 * 255):02x}' * 3))
            canvas.create_line(y - 1, x, y - 1, x + 1, fill='#' + (f'{-int(intensity2 * 255):02x}' * 3))
        else:
            canvas.create_line(x, y, x + 1, y, fill='#' + (f'{int(intensity1 * 255):02x}' * 3))
            canvas.create_line(x, y - 1, x + 1, y - 1, fill='#' + (f'{-int(intensity2 * 255):02x}' * 3))
        y += slope
        m = slope * (x + 1) - y
        intensity1 = 1.0 - math.modf(m)[0]
        intensity2 = math.modf(m)[0]


def calculate_barycentric_cords(x, y, v1, v2, v3):
    v1_x, v1_y = v1
    v2_x, v2_y = v2
    v3_x, v3_y = v3

    triangle_area = abs((v2_x - v1_x) * (v3_y - v1_y) - (v3_x - v1_x) * (v2_y - v1_y))
    triangle_area1 = abs((v2_x - x) * (v3_y - y) - (v3_x - x) * (v2_y - y))
    triangle_area2 = abs((v3_x - x) * (v1_y - y) - (v1_x - x) * (v3_y - y))
    triangle_area3 = abs((v1_x - x) * (v2_y - y) - (v2_x - x) * (v1_y - y))

    alpha = triangle_area1 / triangle_area
    beta = triangle_area2 / triangle_area
    gamma = triangle_area3 / triangle_area

    return alpha, beta, gamma


def interpolate_color(barycentric_cords, c1, c2, c3):
    alpha, beta, gamma = barycentric_cords
    c1 = np.array(c1)
    c2 = np.array(c2)
    c3 = np.array(c3)

    interpolated_color = alpha * c1 + beta * c2 + gamma * c3
    interpolated_color = np.clip(interpolated_color, 0, 255).astype(int)

    return tuple(interpolated_color)


def inside_triangle(x, y, v1, v2, v3):
    x1, y1 = v1
    x2, y2 = v2
    x3, y3 = v3
    b1 = (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) > 0
    b2 = (x3 - x2) * (y - y2) - (y3 - y2) * (x - x2) > 0
    b3 = (x1 - x3) * (y - y3) - (y1 - y3) * (x - x3) > 0

    return b1 == b2 == b3


def triangle(c1, c2, c3, x1=0, y1=0, x2=0, y2=0, x3=0, y3=0):
    min_x = min(x1, x2, x3)
    max_x = max(x1, x2, x3)
    min_y = min(y1, y2, y3)
    max_y = max(y1, y2, y3)

    draw_line_br(x1, y1, x2, y2)
    draw_line_br(x2, y2, x3, y3)
    draw_line_br(x3, y3, x1, y1)

    for x in range(max_x - min_x + 1):
        for y in range(max_y - min_y + 1):
            if inside_triangle(x + min_x, y + min_y, (x1, y1), (x2, y2), (x3, y3)):
                barycentric_cords = calculate_barycentric_cords(x + min_x, y + min_y, (x1, y1), (x2, y2), (x3, y3))
                pixel_color = interpolate_color(barycentric_cords, c1, c2, c3)
                canvas.create_line(x + min_x, y + min_y, x + min_x + 1, y + min_y + 1,
                                   width=0, fill='#%02x%02x%02x' % pixel_color)


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

color1 = (255, 0, 0)
color2 = (0, 255, 0)
color3 = (0, 0, 255)
triangle(color1, color2, color3, 10, 10, 50, 200, 300, 300)

root.mainloop()
