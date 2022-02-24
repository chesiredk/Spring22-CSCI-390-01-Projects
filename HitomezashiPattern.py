# This program creates a unique pattern every time its run that fits in a square patch. I however could not figure
# out how to make it look like the uniform sequence hitomezashi created, I guess the numpy func generates
#  a non-uniform pattern. Im still working on it though time is not in my side.
import turtle
import numpy as np


# create the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.screensize(700, 700)
wn.title("Hitomezashi Stitching Pattern")

# setting the horizontal and vertical lines in form of arrays
pixels = list()


def mark_horizontal_line(lo, x, y):
    line_horizontal = turtle.Turtle()
    line_horizontal.speed(0)
    line_horizontal.hideturtle()
    line_horizontal.up()
    line_horizontal.setposition(x, y)
    for n in lo:
        if (n % 2) == 0:  # sheds the on in the pattern
            for i in range(2):
                line_horizontal.forward(21 / 4)
                pixel = line_horizontal.clone()
                pixel.showturtle()
                pixel.shape("square")
                pixel.color("white")
                pixel.shapesize(1 / 20, 1 / 2)
                pixels.append(pixel)
                line_horizontal.forward(21 / 4)

        if (n % 2) != 0:  # leaves a blank in the off in the pattern
            line_horizontal.forward(21)


# goes to the next line
def mark_horizontal_lines(lo, x, y):
    step_y = y
    for n in lo:
        mark_horizontal_line(n, x, step_y)
        step_y += 21


# vertical line
def mark_line_vertical(lv, x, y):
    line_v = turtle.Turtle()
    line_v.hideturtle()
    line_v.speed(0)
    line_v.up()
    line_v.setposition(x, y)
    line_v.right(-90)
    for n in lv:
        if (n % 2) == 0:  # this makes sure that it draws when on
            for i in range(2):
                line_v.forward(21 / 4)
                pixel = line_v.clone()
                pixel.showturtle()
                pixel.shapesize(1 / 20, 1 / 2)
                pixel.shape("square")
                pixel.color("white")
                pixels.append(pixel)
                line_v.forward(21 / 4)
        if (n % 2) != 0:  # jumps a blank when off
            line_v.forward(21)


def mark_lines_vertical(lv, x, y):
    step_dx = x
    for n in lv:
        mark_line_vertical(n, step_dx, y)
        step_dx += 21


# this function connects the horizontal and vertical patterns

def mark_pattern(lo, lv, x, y):
    mark_horizontal_lines(lo, x, y)
    mark_lines_vertical(lv, x, y)


# generating random integers for the dimensions lists
lo = np.random.randint(10, 50, size=(25, 25))
print(lo)
lv = np.random.randint(10, 50, size=(25, 25))
print(lv)
# initializing the start point
x = -200
y = -200


# creating the square shaped patch and calling the pattern generator in the patch
patch = turtle.Turtle()
patch.penup()
patch.goto(x, y)
patch.pendown()
patch.speed(0)
patch.color("white")
patch.shape("arrow")
for i in range(4):
    patch.forward(525)
    patch.left(90)

patch.hideturtle()
mark_pattern(lo, lv, x, y)

wn.exitonclick()
