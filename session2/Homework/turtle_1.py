from turtle import *

shape("turtle")
color("red", "white")
speed(10)

begin_fill()

for i in range(4):
    left(30)
    forward(100)
    right(60)
    forward(100)
    right(120)
    forward(100)
    right(60)
    forward(100)
    right(60)

left(120)

end_fill()

mainloop()