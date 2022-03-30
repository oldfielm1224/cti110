#CTI-110
#P4LAB2B
#Michael Oldfield
#03-30-2022
#
#turtle drawing initials.
#import and name turtle.
#set background color.
#set width, color of line drawn, and shape of turtle.
#execute to draw initials.
#

import turtle
drawing_area = turtle.Screen()
drawing_area.bgcolor('black')
mikey = turtle.Turtle()
mikey.color('magenta')
mikey.width(6)
mikey.shape('turtle')

mikey.right(90)
mikey.forward(150)
mikey.backward(150)

mikey.left(45)
mikey.forward(90)

mikey.left(95)
mikey.forward(90)

mikey.right(140)
mikey.forward(150)

mikey.penup()

mikey.goto(300, -150)
mikey.right(200)
mikey.forward(50)

mikey.pendown()

mikey.circle(80)



