import turtle
import tkinter as TK

wn = turtle.Screen()
wn.bgcolor("pink")
wn.title("VentanaTortuga")
skk = turtle.Turtle()

skk.speed(45)
skk.left(90)
for i in range(90):
    skk.forward(1)
    skk.right(2)
for i in range(90):
    skk.forward(1)
    skk.left(2)
for i in range(90):
    skk.forward(1)
    skk.right(2)
for i in range(180):
    skk.forward(1.5)
    skk.right(1)
for i in range(90):
    skk.back(1.5)
    skk.left(1)
skk.pencolor("pink")
skk.forward(150)
skk.right(90)
skk.forward(200)
skk.right(90)
skk.pencolor("black")
for i in range(180):
    skk.forward(1)
    skk.right(2)
skk.pencolor("pink")
skk.forward(300)
skk.pencolor("black")
for i in range(180):
    skk.forward(1)
    skk.right(2)
skk.pencolor("pink")
skk.forward(50)
TK.mainloop()