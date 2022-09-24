import asciiplotter as ascp
import asciirenderer as asc

image = ascp.plot("(y <= 2 * math.sin(x)) and (y >= 2 * math.sin(x) - 2)", img=asc.createblankimg(10, 10))

asc.printimage(image)