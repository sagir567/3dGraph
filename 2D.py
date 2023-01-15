from graphics import *
from math import *
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt


# side def to calc z
def getZ(x, y, t):
    r = sqrt(x ** 2 + y ** 2)
    return (cos(radians(r))) * (300 * t ** (-r))


if __name__ == "__main__":
    width = 1200
    t = 1.003
    height = 640

    Min = int(-width / 2)
    Max = int(width / 2)

    d = 20
    # Set lable
    graph = GraphWin("myGraph", height, height)
    graph.setCoords(Min, Min, Max, Max)
    graph.setBackground("Black")
    # check min values for each x-axis to prevent from drawing unnecessary points
    MinVar = [-height] * int(Max * 2)
    # scale
    image = Image.new("RGB", (1500, 1500))
    draw = ImageDraw.Draw(image)
    # drawing the graph with nested loop
    for i in range(Min, Max, d):
        for j in range(Min, Max):
            y = i + getZ(j, i, t)
            # this condition will check whether the value of y is below the minimum
            if y > MinVar[j - Min]:
                MinVar[j - Min] = y
                graph.plot(j + Max, 1800 - (y + Max), 'white')
                # draw.point([(j + Max, 1800 - (y + Max))], fill="white")

                graph.plot(j, y, "White")
    # rotate the picture and save the files
    image = image.rotate(45)
    image.show()
    image.save("C:\graph\graph.GIF")
    graph.getMouse()
