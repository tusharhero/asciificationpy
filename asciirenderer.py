def createblankimg(
    x, y
):  # the image is just a list of list of spaces forming a grid of spaces
    ilist = list(" " * x)
    image = []
    for n in range(y):
        image.append(ilist.copy())
    return image


def printimage(image):
    for n in image:
        for m in n:
            print(m, end="")
        print()


def coor(image, coor):
    color = image[coor[1]][0]
    return color
