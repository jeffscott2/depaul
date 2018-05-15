
from turtle import *

wn = Screen()

def setup():
    draw_axis(0, "(250,0)")
    draw_axis(90, "(0,250)")
    draw_hoop(150,100)
    draw_hoop(250, 100)
    draw_hoop(150, 225)

def draw_axis(heading, label):
    t = Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(heading)
    for i in range(1, 11):
        t.forward(25)
        t.dot()
    t.write(label)


def draw_hoop(x, y):
    h = Turtle()
    h.speed(0)
    h.penup()
    h.goto(x,y)

    h.shape("circle")
    h.shapesize(1,3,1)
    h.color("red")
    h.fillcolor("white")
    h.stamp()

setup()

t = Turtle(shape='turtle')

# Use commands like these to move your turtle
t.left(85)
t.forward(300)


wn.exitonclick()


# Setup:
# 1. Create a new file in your project, named turtle_hoops.py
# 2. Type the code above into turtle_hoops.py
# 3. Run turtle_hoops.py   through the Run menu then "Run..." and choose our file: turtle_hoops.py

# Goals
# 1. Try to use the commands we learned last week to move your turtle into the bottom left circle
# 2. Make a program that moves the turtle through each circle, leaving a "stamp" in each


# Turtle methods
# method_name       parameters      description
# Turtle	        None	Creates and returns a new turtle object

# forward	        amount	Moves the turtle forward by the specified amount
# backward	        amount	Moves the turle backward by the specified amount
# right	            angle	Turns the turtle clockwise
# left	            angle	Turns the turtle counter clockwise

# penup	            None	Picks up the turtle’s pen
# pendown	        None	Puts down the turtle’s pen
# up	               None	Picks up the turtle’s pen
# down	            None	Puts down the turtle’s pen

# color	color       name	Changes the color of the turtle’s pen
# fillcolor	        color name	    Changes the color of the turtle will use to fill a polygon
# heading	        None	Returns the current heading
# position	        None	Returns the current position
# goto	            x,y     Move the turtle to position x,y
# begin_fill	    None	Remember the starting point for a filled polygon
# end_fill	        None	Close the polygon and fill with the current fill color
# dot	            None	Leave a dot at the current position
# stamp	            None	Leaves an impression of a turtle shape at the current location
# shape	            shapename	Should be ‘arrow’, ‘classic’, ‘turtle’, or ‘circle’