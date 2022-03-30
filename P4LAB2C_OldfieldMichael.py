#CTI-110
#P4LAB2C
#Michael Oldfield
#03-30-2022
#
#turtle drawing a snowflake.
#import and name turtle.
#set background color.
#set width, color of line drawn, and shape of turtle.
#execute to draw initials.
#

import turtle
drawing_area = turtle.Screen()
drawing_area.bgcolor('navy')
mikey = turtle.Turtle()
mikey.color('cyan')
mikey.width(10)
mikey.shape('turtle')

mikey.left(90)
for i in range(0,6):
    mikey.forward(100)
    mikey.forward(-40)
    mikey.left(40)
    mikey.forward(30)
    mikey.forward(-30)
    mikey.right(80)
    mikey.forward(30)
    mikey.forward(-30)
    mikey.left(40)
    mikey.forward(-60)
    mikey.right(60)




