import turtle
import tkinter as TK

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("VentanaTortuga")
skk = turtle.Pen()
skk.speed(10)
skk.pencolor("red")
for i in range(60):
    for e in range(360):
        skk.left(1)
        skk.forward(1)
    skk.forward(15)
    skk.left(6)



TK.mainloop()