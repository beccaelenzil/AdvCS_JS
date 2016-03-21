from visual import *

#b = box()

#b.length = .5
#b.width = 2
#b.height = 1.5
#b.color = (1, 0, 0)
#b.material = material.wood
#b.material = material.glass

#c = box()
#print(c.color)
#print(vector(b.pos))

import random

def spinBoxes():
    boxList = []
    for boxNumber in range(10):
        x = random.randint(-5, 5) # integer between -5,5
        y = random.randint(-5, 5)
        z = random.randint(-5, 5)
        red = random.random()     # real number between 0 & 1
        green = random.random()
        blue = random.random()
        newBox = box(pos = vector(x, y, z),
                     color = (red, green, blue) )
        boxList.append(newBox)
    while True:
        for myBox in boxList:
            rate(60)
            myBox.rotate(angle=pi/100)

spinBoxes()