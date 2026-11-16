import turtle

bob = turtle.Turtle()

def triangle():
    for i in range(3):
        bob.forward(200)
        bob.left(120)

def square():
    for i in range(4):
        bob.forward(200)
        bob.left(90)

def jump(x, y):
    bob.penup()
    bob.goto(x, y)
    bob.pendown()

def polygon(sides, dist):
    angle = 360/sides
    bob.begin_fill()
    for times in range(sides):
        bob.forward(dist)
        bob.left(angle)
    bob.end_fill()

def sun(x, y):
    jump(x, y)
    bob.width(10)
    bob.color("yellow")
    for times in range(10):
        bob.forward(50)
        bob.right(144)
    jump(x , -75 + y)
    bob.width(20)
    bob.circle(50)
