from turtle import *

shape("turtle")
speed(10)

color("red","white")
begin_fill()

for _ in range(4):
    forward(100)
    left(90)


color("blue","white")
begin_fill()

for _ in range(3):
    forward(100)
    left(120)

for _ in range(5):
    forward(100)
    left(72)

color("red","white")
begin_fill()

for _ in range(6):
    forward(100)
    left(60)

end_fill()

mainloop()