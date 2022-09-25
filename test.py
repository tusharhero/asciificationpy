import asciiplotter as ascp
import asciirenderer as asc
from asciiplotter import axes
image = ascp.plot(input(), img=asc.createblankimg(100, 100))

asc.printimage(image)