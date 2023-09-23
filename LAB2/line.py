from tkinter import *


def draw_line(x1=0, y1=0, x2=0, y2=0):
    dx = x2 - x1
    dy = y2 - y1

    sign_x = 1 if dx > 0 else -1 if dx < 0 else 0
    sign_y = 1 if dy > 0 else -1 if dy < 0 else 0

    if dx < 0:
        dx = -dx
    if dy < 0:
        dy = -dy

    if dx > dy:
        pdx, pdy = sign_x, 0
        es, el = dy, dx
    else:
        pdx, pdy = 0, sign_y
        es, el = dx, dy

    x, y = x1, y1

    error, t = el / 2, 0

    canvas.create_line(x, y, x + 1, y)

    while t < el:
        error -= es
        if error < 0:
            error += el
            x += sign_x
            y += sign_y
        else:
            x += pdx
            y += pdy
        t += 1
        canvas.create_line(x, y, x + 1, y)


def MouseDown(event):
    global mouse, old_x, old_y
    old_x = event.x
    old_y = event.y
    mouse = True


def MouseUp(event):
    global mouse
    draw_line(old_x, old_y, event.x, event.y)
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
#button = Button(root, text="SAVE", command=saveImage)
#button.place(x=new_width + 20, y=new_height, anchor=SW, width=170, height=25)

root.mainloop()
