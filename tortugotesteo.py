import turtle
import tkinter as TK

wn = turtle.Screen()
wn.title("VentanaTortuga")
skk = turtle.Pen()
skk.speed(60)
skk.goto(-100,-200)
for i in range(13):
    skk.left(15)
    skk.forward(700)
    skk.back(700)
    skk.right(15)

    skk.left(30)
    skk.forward(700)
    skk.back(700)
    skk.right(30)

    skk.left(45)
    skk.forward(700)
    skk.back(700)
    skk.right(45)

    skk.left(60)
    skk.forward(700)
    skk.back(700)
    skk.right(60)

    skk.left(75)
    skk.forward(700)
    skk.back(700)
    skk.right(75)

    skk.left(90)
    skk.forward(700)
    skk.back(700)
    skk.right(90)

    skk.left(105)
    skk.forward(700)
    skk.back(700)
    skk.right(105)

    skk.left(120)
    skk.forward(700)
    skk.back(700)
    skk.right(120)

    skk.left(135)
    skk.forward(700)
    skk.back(700)
    skk.right(135)

    skk.forward(100)
    skk.left(30)

skk.goto(-25,-55)
skk.pencolor("red")
skk.width(10)
skk.circle(50)
tamaño= 15
skk.right(104)
while tamaño != 0:
    skk.width(tamaño)
    skk.forward(2)
    tamaño -= 0.5

TK.mainloop()