import asciirenderer as asc
import math


def plot(equation, img=asc.createblankimg(100, 100), white="⬜", black="⬛"):
    for coor in getrange(img):
        x = coor[0]
        y = coor[1]
        nx, ny = cart2ascii(x, y, img)
        condition = eval(equation)
        if condition:
            img[ny][nx] = white
        else:
            img[ny][nx] = black
    return img


def getrange(img):
    ran = list()
    for y in range(len(img)):
        for x in range(len(img)):
            ran.append(ascii2cart(x, y, img))
    return ran


def ascii2cart(x, y, img):
    length_y = len(img)
    length_x = len(img[0])
    ny = length_y // 2 - y
    nx = x - length_x // 2
    return nx, ny


def cart2ascii(nx, ny, img):
    length_y = len(img)
    length_x = len(img[0])
    y = length_y // 2 - ny
    x = nx + length_x // 2
    return x, y

def axes(x,y):
    return (not (x and y))

def point(a,b,x,y):
    return (x == a and y == b)

def circle(x,y,r = 1 ,a = 0 ,b = 0):
    return ((x-a)**2 + (y-b)**2 <= r**2)