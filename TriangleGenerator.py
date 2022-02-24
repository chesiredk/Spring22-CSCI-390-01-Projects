import turtle
from turtle import *
import random as rand

t = turtle.Turtle()
# Environment settings
speed(0)
pensize(2)
bgcolor("grey")

# initializing random angles and triangles for an isosceles triangle
line_A = rand.randint(200, 300)  # initializes a random baseline from start point - east
angle_c = rand.randint(1, 178)  # initializes a random angle for the first turn
line_B = line_A  # isosceles triangle
angle_a = (180 - angle_c) / 2
line_C = 600  # preset to draw past the triangle end spot but doesn't affect triangle formation
angle_b = angle_a  # isosceles triangle


def generate_triangle(x, y, *colors):  # generating a triangle
    penup()
    begin_fill()
    goto(x, y)
    pendown()
    color(*colors)
    begin_fill()
    side_count = 0
    while side_count <= 3:
        if side_count == 0:
            t.left(180 - (angle_b / 2))
            t.forward(400)
            t.backward(400)  # last angle is bisected
            t.right(180 - (angle_b / 2))
            t.left(180 - angle_b)
            t.forward(line_A)  # draws base
        elif side_count == 1:
            t.left(180 - (angle_c / 2))  # turns the cursor left by degrees to draw bisector
            t.forward(300)
            t.backward(300)
            t.right(180 - (angle_c / 2))
            t.left(180 - angle_c)  # turns this angle at end of base
            t.forward(line_B)
        elif side_count == 2:
            t.left(180 - (angle_a / 2))
            t.forward(400)
            t.backward(400)  # the second angle bisected
            t.right(180 - (angle_a / 2))
            t.left(180 - angle_a)
            t.forward(line_C)  # draws last line
        elif side_count == 3:
            t.left(180 - angle_b)
            hideturtle()
            done()

        side_count += 1

    end_fill()


while True:
    penup()
    x = 0
    y = 0
    generate_triangle(x, y, "black")  # begin drawing
    x += 5
    y -= 5
    pendown()
    goto(x,y)
exitonclick()
