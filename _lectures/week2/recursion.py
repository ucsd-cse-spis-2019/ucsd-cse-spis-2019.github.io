import turtle
from recursionhelper import *


# We have an external function
# draw3Circles(turtle_name, size_first_circle)


def draw4Circles(t,radius):
    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)
    t.pendown()
    draw3Circles(t,radius//2)


def draw5Circles(t,radius):
    t.circle(radius)
    t.penup()
    t.left(90)
    t.forward(radius)
    t.right(90)
    t.pendown()
    draw4Circles(t,radius//2)


def drawNCircles(t,radius,n):
    if (n == 0):
        print('done doing recursion')
    else:
        t.circle(radius)
        t.penup()
        t.left(90)
        t.forward(radius)
        t.right(90)
        t.pendown()
        drawNCircles(t,radius//2,n-1)
    
    
drogon = turtle.Turtle()

drawNCircles(drogon,100,5)
