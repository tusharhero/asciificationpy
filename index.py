import asciirenderer as asc
import asciiplotter as ascp
from browser import document, html
print("Hello! https://github.com/tusharhero")

SIZELIMIT = int(document["-sizeLimit"].innerHTML)

def clear(evt):
    document["output"].value = ""
    document["error"].html = "$ I ate the graph"

def check():
    eqt = document["text-src"].value
    size = document["size"].value
    scaling = document["scaling"].value

    i = int(size)
    scale = float(scaling)

    if (i > SIZELIMIT):
        return False
    else:
        return [eqt, i, scale]

def getequation(evt):
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
    
def forcePlot():
    equation = document["text-src"].value
    size = int(document["size"].value)
    scaling = float(document["scaling"].value)
    graph = asc.getstring(ascp.plot(equation, img=asc.createblankimg(size, size), s=scaling))
    document["error"].html = "$ checking"
    document["box"].width = size
    document["output"].value = graph
    document["error"].html = "$ done!"
    document["error"].html = "$ " + str(e)

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

document["forcePlot"].bind("click", forcePlot)

startup()
