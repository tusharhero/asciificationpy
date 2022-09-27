import asciirenderer as asc
import asciiplotter as ascp
from browser import document, html

def getequation(evt):
    equation = document["text-src"].value
    try:
        size = int(document["size"].value)
        graph = asc.getstring(ascp.plot(equation, img=asc.createblankimg(size, size)))
        document["error"].html = "$ checking"
        document["box"].width = size
        document["output"].value = graph
        document["error"].html = "$ done!"
    except Exception as e:
        document["error"].html = "$ " + str(e)

def clear(evt):
    document["output"].value = ""
    document["error"].html = "$ I ate the graph"

def startup():
    eqt = document["-eqt"].value
    size = document["-size"].value

    if eqt == 'default' or size == 'default':
        return None

    i = int(size)
    graph = asc.getstring(ascp.plot(eqt, img=asc.createblankimg(i, i)))
    document["box"].width = i
    document["output"].value = graph
    document["error"].html = "$ I am done plotting the equation shared to you!"

document["submit"].bind("click", getequation)

document["clear"].bind("click", clear)

startup()
