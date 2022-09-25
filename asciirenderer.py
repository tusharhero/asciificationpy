def createblankimg(
    x, y
):  # the image is just a list of list of spaces forming a grid of spaces
    ilist = list(" " * x)
    image = []
    for n in range(y):
        image.append(ilist.copy())
    return image


def getstring(image):
    string = ""
    for n in image:
        for m in n:
            string+=m
        string+="\n"
    return string

def printimage(image):
    print(getstring(image))
