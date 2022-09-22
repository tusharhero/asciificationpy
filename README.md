# Asciification

My attempt to create simple images in ascii.

## asciirenderer

It uses a simple 2d list to store the characters.

## asciiplotter

Uses `asciirenderer` to plot mathematical equations.

### some examples

- a parabola
  
`code:`
```py
import asciirenderer as asc
import asciiplotter as ascp

image = ascp.plot("y == (x-5)**2", img= asc.createblankimg(10,10))

asc.printimage(image)
```

`output:`

```
⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛
⬛⬛⬛⬛⬜⬛⬜⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬜⬛⬛⬛⬛⬛⬜⬛
```