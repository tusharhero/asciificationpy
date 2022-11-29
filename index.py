import asciirenderer as asc
import asciiplotter as ascp
from browser import document, html
print("Hello! https://github.com/tusharhero")

def clear(evt):
    document["output"].value = ""
    document["error"].html = "$ I ate the graph"

def check():
    eqt = document["text-src"].value
    size = document["size"].value
    scaling = document["scaling"].value

    i = int(size)
    scale = int(scaling)

    if (i > 250):
        return False
    else:
        return [eqt, i, scale]

def getequation(evt):
    # equation = document["text-src"].value
    # try:
    #     size = int(document["size"].value)
    #     scaling = float(document["scaling"].value)
    #     graph = asc.getstring(ascp.plot(equation, img=asc.createblankimg(size, size), s=scaling))
    #     document["error"].html = "$ checking"
    #     document["box"].width = size
    #     document["output"].value = graph
    #     document["error"].html = "$ done!"
    # except Exception as e:
    #     document["error"].html = "$ " + str(e)
    checkData = check()

    if (checkData != False):
        eqt = checkData[0]
        size = checkData[1]
        scale = checkData[2]

        graph = asc.getstring(ascp.plot(eqt, img=asc.createblankimg(size, size), s=scale))
        document["error"].html = "$ checking"
        document["box"].width = size
        document["output"].value = graph
        document["error"].html = "$ done!"


def startup():

    if document["-eqt"] == 'default' or document["-size"] == 'default' or document["-scale"] == 'default':
        return None

    checkData = check()

    if (checkData != False):
        eqt = checkData[0]
        size = checkData[1]
        scale = checkData[2]

        graph = asc.getstring(ascp.plot(eqt, img=asc.createblankimg(size, size), s=scale))
        document["box"].width = size
        document["output"].value = graph
        document["error"].html = "$ I am done plotting the equation shared to you!"

document["submit"].bind("click", getequation)

document["clear"].bind("click", clear)

startup()
