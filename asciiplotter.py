import asciirenderer as asc
import math


def plot(equation, img=asc.createblankimg(100, 100), white="⬜", black="⬛"):
    for y in range(len(img)):  # iterate through the y-axis
        for x in range(
            len(img[y])
        ):  # iterate through each abcissa in the x-axis of the current y-axis
            # x , y = getcorrectedcoor(x, y, img)
            condition = eval(equation)
            if condition:
                img[y][x] = white
            else:
                img[y][x] = black
    return img


def ascii2cart(x, y, img):
    length_y = len(img[0])
    length_x = len(img[0][0])
    y = -y + length_y // 2
    x = x + length_x // 2
    return x, y


def cart2ascii(x, y, img):
    return ascii2cart(x, y, img)
