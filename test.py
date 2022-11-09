import asciiplotter as ascp
import asciirenderer as asc
from asciiplotter import axes

image = ascp.plot("circle(x,y,1)", img=asc.createblankimg(9, 9), s=2)

asc.printimage(image)
