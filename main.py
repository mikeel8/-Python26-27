import turtle
from myfunctions import *
import random

turtle.bgcolor("DeepSkyBlue")
bob.speed(0)

for i in range(50):
    x = random.randint(-300, 300)
    y = random.randint(-200, 200)
    
    jump(x, y)
    bob.color(random.choice(["red", "blue", "green", "purple", "orange"]))
    
    sides = random.choice([3, 4])
    size = random.randint(100, 200)
    
    polygon(sides, size)

sun(250, 300)
