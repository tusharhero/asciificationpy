import asciirenderer as asc
import asciiplotter as ascp
from browser import document , html


def getequation(evt):
    equation = document["text-src"].value
    graph = asc.getstring(ascp.plot(equation, img = asc.createblankimg(50, 50)))
    print(graph)
    document["output"].value = graph

def clear(evt):
    document["output"].value = ""

document["submit"].bind("click", getequation)

document["clear"].bind("click", clear)  