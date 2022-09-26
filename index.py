import asciirenderer as asc
import asciiplotter as ascp
from browser import document, html


def getequation(evt):
    equation = document["text-src"].value
    size = int(document["size"].value)
    graph = asc.getstring(ascp.plot(equation, img=asc.createblankimg(size, size)))
    print(graph)
    document["box"].width = size
    document["output"].value = graph

def clear(evt):
    document["output"].value = ""

def startup():
    eqt = document["-eqt"].value
    size = document["-size"].value

    if eqt == 'default' or size == 'default' : return

    i = int(size)
    graph = asc.getstring(ascp.plot(eqt, img=asc.createblankimg(i, i)))
    document["box"].width = i
    document["output"].value = graph

document["submit"].bind("click", getequation)

document["clear"].bind("click", clear)

startup()
