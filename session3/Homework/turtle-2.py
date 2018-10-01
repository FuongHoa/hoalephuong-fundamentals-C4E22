colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *

shape("turtle")
speed(5)

color(colors[0])
begin_fill()
for _ in range(1):
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)



mainloop()