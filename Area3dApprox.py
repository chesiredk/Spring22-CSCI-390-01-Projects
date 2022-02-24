from vpython import *
import random as rand
import math

canvas(width=500, height=500)

# creating exterior random shapes with known lengths and areas
ext = rand.randint(1, 2)
if ext == 1:
    box(pos=vector(0, 0, 0), size=vector(10, 10, 10), color=color.red, opacity=0.5)  # creates a cube
    surfArea = 6 * 100
    extVolume = 10 * 10 * 10
    print("EXT AREA = ", surfArea)
    print("EXT VOLUME = ", extVolume)
else:
    box(pos=vector(0, 0, 0), size=vector(10, 10, 11), color=color.green, opacity=0.5)  # creates a cuboid
    surfArea = (2 * 100) + (4 * 110)
    extVolume = 10 * 10 * 11
    print("EXT AREA = ", surfArea)
    print("EXT VOLUME = ", extVolume)

# This part generates a random interior shape with random sizes and volume
intr = rand.randint(1, 2)
ra = rand.randint(1, 5)
l = rand.randint(3, 7)
if intr == 1:  # creates an interior sphere
    sphere(pos=vector(0, 0, 0), radius=ra, color=color.blue, opacity=1)
    surfArea2 = 4 * math.pi * ra * ra
    intVolume = (4/3) * math.pi * ra * ra * ra
    print("INT AREA = ", surfArea2)
    print("INT VOLUME = ", intVolume)
else:  # creates an interior cube
    box(pos=vector(0, 0, 0), size=vector(l, l, l), color=color.blue, opacity=1)  # creates a cube
    surfArea2 = 6 * l * l
    intVolume = l * l * l
    print("INT AREA = ", surfArea2)
    print("INT VOLUME = ", intVolume)


# finding actual area and volume ratio
actualVolumeRatio = extVolume / intVolume
actualAreaRatio = surfArea / surfArea2
print("Actual Volume Ratio = ", actualVolumeRatio)
print("Actual Surface Area Ratio = ", actualAreaRatio)

""" I had the same problem with matplotlib,then I tried vpython, to no avail
It took me a long time, I have tried to generate random points but could not figure out
a suitable function for it: also being a 3d shape random points did not seem a suitable method to 
estimate the surface area of the two shapes, unless I could
 approximate the area based on one dimension which would not be fitting for
 non - verticed shapes like spheres. And if I was to go with volume,
I still cannot understand how it'd work:( 
I'm disappointed I could not do something productive but eager to see what the
others have done.
I'm still figuring it out
"""

