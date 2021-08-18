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
    skk.forward(116.5)
    skk.back(116.5)
    skk.right(31)

    skk.left(45)
    skk.forward(141.5)
    skk.back(141.5)
    skk.right(45)

    skk.left(60.3)
    skk.forward(162)
    skk.back(162)
    skk.right(60.3)

    skk.left(76)
    skk.forward(165)
    skk.back(165)
    skk.right(76)

    skk.left(90)
    skk.forward(160)
    skk.back(160)
    skk.right(90)

    skk.left(106)
    skk.forward(145.5)
    skk.back(145)
    skk.right(106)

    skk.left(121)
    skk.forward(116.5)
    skk.back(116.5)
    skk.right(121)

    skk.left(135)
    skk.forward(85)
    skk.back(85)
    skk.right(135)

    skk.forward(40)
    skk.left(29)

TK.mainloop()