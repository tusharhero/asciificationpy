import asciirenderer as asc
import math


def plot(equation, img=asc.createblankimg(49, 49), white="⬜", black="⬛", s=5):
    for coor in getrange(img, s):
        x = coor[0]
        y = coor[1]
        nx, ny = cart2ascii(x, y, img, s)
        condition = eval(equation)
        if condition:
            img[ny][nx] = white
        else:
            img[ny][nx] = black
    return img


def getrange(img, s=5):
    ran = list()
    for y in range(len(img)):
        for x in range(len(img)):
            ran.append(ascii2cart(x, y, img, s))
    return ran


def ascii2cart(x, y, img, s=5):
    length_y = len(img)
    length_x = len(img[0])
    ny = (length_y // 2 - y) / s
    nx = (x - length_x // 2) / s
    return nx, ny


def cart2ascii(nx, ny, img, s=5):
    length_y = len(img)
    length_x = len(img[0])
    y = length_y // 2 - s * ny
    x = s * nx + length_x // 2
    return int(x), int(y)


def axes(x, y):
    return not (x and y)


def point(a, b, x, y):
    return x == a and y == b


def circle(x, y, r=1, a=0, b=0):
    return (x - a) ** 2 + (y - b) ** 2 <= r**2
