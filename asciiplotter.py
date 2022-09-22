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
