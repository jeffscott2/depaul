
from turtle import *

wn = Screen()
raph = Turtle(shape='turtle')

for i in range(3):
    raph.forward(100)

    # the angle of each vertice of a regular polygon
    # is 360 divided by the number of sides
    raph.left(360/3)


def draw_square(tur, size):
    for i in range(4):
        tur.forward(size)
        tur.left(360 / 4)


raph.left(90)
raph.forward(150)

draw_square(raph, 200)

wn.exitonclick()


# Steps:
# 1. Create a new file in your project, named turtles.py
# 2. Type the code above into turtles.py
# 3. Run turtles.py    (click in the window to close it)
# 4. Try changing up numbers to see what changes, try to figure out how it works

# Stretch Goals:
# A. write your own `draw_triangle` function similar to `draw_square`
# B. write a function to drawn an object with any number of sides
# C. Use your functions to draw a house:
#
#        /\
#       /  \
#      /    \
#     /      \
#    /        \
#   /          \
#  /            \
# +--------------+
# |              |
# |              |
# |     +-+      |
# |     | |      |
# +--------------+




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