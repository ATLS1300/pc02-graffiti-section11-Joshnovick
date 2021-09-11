#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Josh Novick
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
#variables
t = turtle.Turtle()
t.clear()
leftForehead = (-25, 150)
rightForehead = (33, 190)
rightShoulder = (146, -63)
fingertip = (111, -90)

#code
t.pen(pencolor="green", pensize=2.5, speed=10)
t.up()
t.goto(fingertip)
t.rt(90)
t.down()
n=5
while n <= 120:
    t.circle(n)
    n = n+5
t.up()
t.goto(rightForehead)
t.lt(90)
t.bk(55)
t.shape("circle")
t.shapesize(2.5,12,8)
t.pen(pencolor="darkblue", pensize=2.5, fillcolor="purple")
t.down()
t.stamp()
t.shape("triangle")
t.lt(90)
t.fd(48)
t.shapesize(8.5,9,8)
t.stamp()
t.up()
t.pen(pencolor="yellow", fillcolor="yellow", pensize=3.5)
t.shapesize(1,1,1)
t.lt(90)
t.fd(20)
t.rt(90)
t.down()
t.fd(30)
t.rt(45)
t.fd(30)
t.rt(90)
t.fd(30)
t.rt(45)
t.fd(30)
t.rt(90)
t.fd(40)
t.hideturtle()


        
    



#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
