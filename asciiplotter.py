import asciirenderer as asc

def plot(equation, img = asc.createblankimg(100,100) , white = "⬜" , black = "⬛"):
    condition = eval(equation)
    for y in img:
        for x in y:
            if condition:
                img[y][x] = white
            else:
                img[y][x] = black
    return plot
