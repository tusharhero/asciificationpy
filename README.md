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

image = ascp.plot("y == (x)**2", img= asc.createblankimg(10,10))

asc.printimage(image)
```

`output:`

```
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬜⬛⬛⬛⬜⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬜⬛⬜⬛⬛⬛
⬛⬛⬛⬛⬛⬜⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
```

- circle

`code:`
```py
import asciiplotter as ascp
import asciirenderer as asc

image = ascp.plot("(x)**2 + (y)**2 <= 3.2**2", img=asc.createblankimg(10, 10))

asc.printimage(image)
```

`output:`

```
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬜⬜⬜⬛⬛⬛
⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛
⬛⬛⬜⬜⬜⬜⬜⬜⬜⬛
⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛
⬛⬛⬛⬛⬜⬜⬜⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
```

`code:`
```py
import asciiplotter as ascp
import asciirenderer as asc

image = ascp.plot("(y <= 2 * math.sin(x)) and (y >= 2 * math.sin(x) - 2)", img=asc.createblankimg(10, 10))

asc.printimage(image)
```

`output`

```
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
⬜⬜⬛⬛⬛⬛⬜⬜⬛⬛
⬜⬜⬛⬛⬛⬜⬜⬜⬜⬛
⬛⬛⬜⬛⬛⬜⬛⬛⬜⬛
⬛⬛⬜⬜⬜⬜⬛⬛⬛⬜
⬛⬛⬛⬜⬜⬛⬛⬛⬛⬜
⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛
```