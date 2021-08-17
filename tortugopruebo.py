import turtle
import tkinter as TK

colores = ["blue", "purple", "red", "yellow", "white", "pink", "green"]
wn = turtle.Screen()


wn.title("VentanaTortuga")
skk = turtle.Pen()
skk.speed(10)

colors = ["red", "white"]

contador = 0
indexGen = 0
for i in range(360):
    skk.pencolor(colors[i % 2])
    skk.width(5)
    skk.forward(i)
    skk.left(45)
    wn.bgcolor(colores[indexGen])
    contador += 1
    if contador == 52:
        contador = 0
        indexGen += 1 

TK.mainloop()


skk.goto(-400,-400)