import asciirenderer as asc

def plot(equation, img = asc.createblankimg(100,100) , white = "⬜" , black = "⬛"):
    for y in range(len(img)):
        for x in range(len(img[y])):
            condition = eval(equation)
            if condition:
                img[y][x] = white
            else:
                img[y][x] = black
    return img
