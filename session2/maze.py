from turtle import *

shape("turtle")
speed(100)

# for _ in range(90):
#     forward(d)
#     d = d + 10
#     left(90)

for i in range(90):
    forward(i * 10)
    left(90)

mainloop()