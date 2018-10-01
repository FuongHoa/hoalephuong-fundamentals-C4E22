colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *

shape("turtle")
speed(5)

color(colors[0])
begin_fill()

for _ in range(3):
    forward(100)
    left(120)

color(colors[1])
begin_fill()

for _ in range(4):
    forward(100)
    left(90)

color(colors[2])
begin_fill()

for _ in range(5):
    forward(100)
    left(72)

color(colors[3])
begin_fill()

for _ in range(6):
    forward(100)
    left(60)

color(colors[4])
begin_fill()

for _ in range(7):
    forward(100)
    left(52)


mainloop()