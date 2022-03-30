#CTI-110
#P4LAB2A
#Michael Oldfield
#03-30-2022
#
#turtle drawing a square and triangle.
#import and name turtle.
#set width, color of line drawn, and shape of turtle.
#execute to draw square and then a triangle.
#

import turtle
ichigo = turtle.Turtle()
ichigo.color('orange')
ichigo.width(4)
ichigo.shape('turtle')

drawing_area = turtle.Screen()
for i in range(4):
    ichigo.forward(200)
    ichigo.left(90)

for side in range(3):
    ichigo.forward(100)
    ichigo.left(120)
    

