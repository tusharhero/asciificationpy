import asciirenderer as asc
import math


def plot(equation, img=asc.createblankimg(100, 100), white="⬜", black="⬛"):
    for coor in getrange(img):
        x = coor[0]
        y = coor[1]
        nx , ny = cart2ascii(x, y, img)
        condition = eval(equation)
        if condition:
            img[ny][nx] = white
        else:
            img[ny][nx] = black
        return img


def getrange(img):
    length_y = len(img) // 2
    length_x = len(img[0]) // 2
    yran = list(range(-length_y,length_y))
    xran = list(range(-length_x,length_x))
    ran = list()
    for y in yran:
        for x in xran:
            ran.append([x,y])
    return ran

def ascii2cart(x, y, img):
    length_y = len(img)
    length_x = len(img[0])
    print(length_x)
    y = -y + length_y // 2
    x = x + length_x // 2
    return x, y


def cart2ascii(x, y, img):
    length_y = len(img)
    length_x = len(img[0])
    print(length_x)
    y = y - length_y // 2
    x = x - length_x // 2
    return x , y