import asciirenderer as asc
import math


def plot(equation, img=asc.createblankimg(100, 100), white="⬜", black="⬛"):
    for y in range(len(img)):  # iterate through the y-axis
        for x in range(
            len(img[y])
        ):  # iterate through each abcissa in the x-axis of the current y-axis
            condition = eval(equation)
            if condition:
                img[y][x] = white
            else:
                img[y][x] = black
    return img


def givecartesianpoint(x, y, img):
    length_y = len(img[0][0])
    length_x = len(img[0])

    if y == length_y / 2:
        y = 0
    else:
        y = length_y / 2 - y

    if x == length_x / 2:
        x = 0
    else:
        x = length_x / 2 - x
    return x, y


def getcorrectedcoor(x, y, img):
    length_y = len(img[0][0])
    length_x = len(img[0])
    if y == 0:
        y = length_y / 2
    if x == 0:
        x = length_x / 2
    if y > 0:
        y = length_y / 2 + y
    if x > 0:
        x = length_x / 2 + x
    if y > 0:
        y = length_y / 2 - y
    if x > 0:
        x = length_x / 2 - x
    return x, y
