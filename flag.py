import turtle
import time

make=turtle.Turtle()
make.speed(100)
time.sleep(10)

for i in range(24):
    make.pensize(4)
    make.forward(149)
    make.penup()
    make.setposition(0,0)
    make.pendown()
    make.right(15)

make.setposition(0,-150)
make.circle(151)
make.penup()

make.setposition(-500,150)

make.pendown()
make.pensize(4)
make.fillcolor("orange")
make.begin_fill()
make.forward(1000)
make.left(90)
make.forward(1000)
make.left(90)
make.forward(1000)
make.left(90)
make.forward(1000)
make.end_fill()
make.penup()

make.setposition(-500,-150)
make.pensize(4)
make.pendown()
make.fillcolor("green")
make.begin_fill()
make.right(270)
make.forward(1000)
make.right(90)
make.forward(1000)
make.right(90)
make.forward(1000)
make.right(90)
make.end_fill()
make.penup()

turtle.done()


    

