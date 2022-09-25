import asciirenderer as asc
import asciiplotter as ascp
from browser import document, html


def getequation(evt):
    equation = document["text-src"].value
    size = int(document["size"].value)
    graph = asc.getstring(ascp.plot(equation, img=asc.createblankimg(size, size)))
    print(graph)
    document["output"].rows = size
    document["output"].cols = 2 * size
    document["output"].value = graph


def clear(evt):
    document["output"].value = ""


document["submit"].bind("click", getequation)

document["clear"].bind("click", clear)
