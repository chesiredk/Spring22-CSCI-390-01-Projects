import math
import turtle
import random as rand

# This creates the display screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.screensize(700, 700)
wn.title("Estimating Area ")

# This part chooses the outside shape either a square or rectangle
# Area is rounded off to the nearest integer
ext = rand.randint(1, 2)
x = -150
y = -150
t = turtle.Turtle()
t.color("white")
t.shape("square")
t.speed(0)
t.penup()
t.goto(x, y)
t.pendown()
if ext == 1:  # square
    for i in range(4):
        t.forward(350)
        t.left(90)
        outArea = 122500
        ssize = 350, 350
else:  # rectangle
    for i in range(2):
        t.forward(350)
        t.left(90)
        t.forward(250)
        t.left(90)
        outArea = 87500
        ssize = 350, 250

t.hideturtle()

# This part chooses the random shape to draw depict in interior shape and draws it
# in this case a circle or a triangle

inte = rand.randint(1, 2)
a = rand.randint(-120, -90)
b = rand.randint(-120, -90)
ra = rand.randint(50, 75)
len = rand.randint(100, 250)
if inte == 1:  # triangle
    z = turtle.Turtle()
    z.color("white")
    z.shape("square")
    z.speed(0)
    z.penup()
    z.goto(a, b)
    z.pendown()
    for i in range(3):
        z.forward(len)
        z.left(120)
        z.hideturtle()
        heightt = math.sqrt((len * len) - ((len / 2) * (len / 2)))
        inArea = 0.5 * len * heightt
else:  # circle
    z = turtle.Turtle()
    z.color("white")
    z.shape("square")
    z.speed(0)
    z.penup()
    z.goto(20, -75)
    z.pendown()
    z.circle(ra)
    z.hideturtle()
    inArea = math.pi * ra * ra

diff = 0.00256
actualRatio = outArea / inArea

# generating random dots and using the count to determine the estimated area
def change_turtle_position(position):
    t.penup()
    t.goto(position[0], position[1])
    t.pendown()


dotCount = 1000
x = actualRatio - diff

def generate_extdots(origin, dotCount, size=ssize):
    for i in range(dotCount):
        rand_x = rand.randint(min(origin[0], origin[0] + size[0]),     max(origin[0], origin[0] + size[0]))
        rand_y = rand.randint(min(origin[1], origin[1] + size[1]),     max(origin[1], origin[1] + size[1]))
        change_turtle_position((rand_x, rand_y))
        t.dot()
        # trying to find the number of dots in the interior shape
        if t.distance(z) <= 20:
            x+1


# This calls the dot function
generate_extdots((-150, -150), dotCount)
calcPoints = dotCount/actualRatio

# I could not figure a function to count the interior shape dots so I just used the actual ratio
# Writing values on the screen
penn = turtle.Turtle()
penn.penup()
penn.color("red")
penn.speed(0)
penn.shape("arrow")
penn.penup()
penn.goto(-350, 200)
penn.write("Exterior Area: " + str(outArea))
penn.goto(-350, 170)
penn.write("Interior Area: " + str(inArea))
penn.goto(-350, 140)
penn.write("Actual Ratio: " + str(actualRatio))
penn.goto(-350, 110)
penn.write("Interior Points: " + str(calcPoints))
penn.goto(-350, 80)
penn.write("Total Points: " + str(dotCount))
penn.hideturtle()

wn.exitonclick()
