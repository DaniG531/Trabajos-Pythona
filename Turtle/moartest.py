import turtle
import tkinter as TK

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("VentanaTortuga")
skk = turtle.Pen()
skk.speed(50)
skk.pencolor("red")
skk.goto(275,0)
for i in range(360):
    skk.back(550)
    skk.right(179)




TK.mainloop()