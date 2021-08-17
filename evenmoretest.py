import turtle
import tkinter as TK

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("VentanaTortuga")
skk = turtle.Pen()
skk.speed(50)
skk.pencolor("red")
for i in range(60):
    skk.circle(100)
    skk.forward(20)
    skk.left(6)

TK.mainloop()