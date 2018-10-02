colors = ['red', 'blue', 'brown', 'yellow', 'grey']
from turtle import *

shape("turtle")
speed(5)

for _ in range(5):
    color(colors[_])
    begin_fill()
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    left(90)
    forward(100)
    left(90)
    forward(50)
    end_fill()
    
print(_)
mainloop()