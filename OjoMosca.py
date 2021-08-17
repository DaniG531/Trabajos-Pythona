import turtle
import tkinter as TK

wn = turtle.Screen()
wn.title("VentanaTortuga")
skk = turtle.Pen()
skk.speed(45)
for i in range(13):
    skk.left(14)
    skk.forward(82.5)
    skk.back(82.5)
    skk.right(14)

    skk.left(31)
    skk.forward(116.6)
    skk.back(116.6)
    skk.right(31)

    skk.left(45)
    skk.forward(141.4)
    skk.back(141.4)
    skk.right(45)

    skk.left(60.3)
    skk.forward(161.2)
    skk.back(161.2)
    skk.right(60.3)

    skk.left(76)
    skk.forward(164.9)
    skk.back(164.9)
    skk.right(76)

    skk.left(90)
    skk.forward(160)
    skk.back(160)
    skk.right(90)

    skk.left(105.9)
    skk.forward(145.6)
    skk.back(145.6)
    skk.right(105.9)

    skk.left(121)
    skk.forward(116.6)
    skk.back(116.6)
    skk.right(121)

    skk.left(135)
    skk.forward(84.9)
    skk.back(84.9)
    skk.right(135)

    skk.forward(40)
    skk.left(29)

TK.mainloop()