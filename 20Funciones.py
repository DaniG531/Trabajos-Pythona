from hashlib import new
import random 
import turtle
import tkinter as TK

class color:
    Rosa = "\033[1;31m"
    Default = "\033[0;0m"
    Cyan = "\033[0;36m"
    Lime = "\033[1;32m"
    BabyBlue = "\033[1;34m"
    Yellow = "\033[1;33m"

Colores = [color.Rosa, color.Cyan, color.Lime, color.BabyBlue, color.Yellow]
arregloX = ["A", "B", "C"]
arregloRand = []

def Tablas(): #Función 1
    for i in range(1,4):
        for e in range(1,3):
            print(f'{i}*{e}={i*e}')
    print("~~~~~~~~~~~~~~~~~")

def Mood(humor): #Función 2
    print(f"mi estado de humor es: {humor}")

def MoodMal(): #Función 3
    Mood("Enojado")

def Impresion(): #Función 4
    print("Esto es una simple impresión.")

def Cuadrado(a, b): #Función 5
    for i in range(0,a):
        print("*"*b)
    print("")

def Triangulo(AlturaTriangulo): #Función 6
    for i in range(1, AlturaTriangulo+1):
        print("*"*i) #Solo en Python

def Arreglo(): #Función 7
    print(arregloX)

def NumerosRandom(): #Función 8
    for i in range(10):
        numero = random.randrange(10)
        arregloRand.append(numero)
    print(arregloRand)

def TextoRojo(): #Función 9
    print(f"{color.Rosa}~Este Texto Es Color Rojo.~ {color.Default}")

def TextoCyan(): #Función 10
    print(f"{color.Cyan}~Este Texto Es Color Cyan.~ {color.Default}")

def Separar(Texto): #función 11
    Algo = []
    for i in Texto:
        Algo.append(i)
    print(Algo)

def MostrarIdArregloRand(): #función 12
    print(f"{id(arregloRand)} = Id de arregloRand")

def CrearStringPorArreglo(): #función 13
    TempArray = []
    NewString= ("")
    Caracteres= int(input("cuantos caracteres tiene la palabra?  "))
    for i in range(Caracteres):
        letra = input("Introduce Letra:  ")
        TempArray.append(letra)
    for e in TempArray:
        NewString = (NewString+e)
    print(NewString)

def CuadradoAColor(): #función 14
    print(f"{random.choice(Colores)}")
    Cuadrado(3,3)
    print(f"{color.Default}")

def TrianguloAColor(): #función 15
    print(f"{random.choice(Colores)}")
    Triangulo(5)
    print(f"{color.Default}")

def NumeroA50(numero): #función 16
    if numero < 50:
        print("El número es menor a 50.")
    elif numero > 50:
        print("El número es mayor a 50.")
    else:
        print("El número es 50.")
    print("")

def GruposYExamenes(): #función 17
    Examen1 = int(input("Calificación del Exámen: "))
    if Examen1 >= 90:
        print("Ocupas realizar hacer otro exámen.")
        Examen2 = int(input("Calificación del segundo Exámen: "))
        if Examen2 >= 90:
            print("Tu grupo asignado es Matematicas 103.")
        else:
            print("Tu grupo asignado es Matematicas 102.")
    else:
        print("Ocupas realizar hacer otro exámen.")
        Examen3 = int(input("Calificación del segundo Exámen: "))
        if Examen3 >= 90:
            print("Tu grupo asignado es Matematicas 102.")
        else:
            print("Tu grupo asignado es Matematicas 101.")

from Fibonacci import FindFibonacci
#def FindFibonacci impotado      # función 18
 
def Dados(): #función 19
    Dado1 = int(random.randrange(1,6))
    Dado2 = int(random.randrange(1,6))
    total = Dado1 + Dado2
    print(f"Dado 1 = {Dado1},  Dado2 = {Dado2},  Total = {total}")

def CirculoTortuga():
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


Tablas()                                        #funcion 1
Mood("Feliz")                                   #funcion 2
MoodMal()                                       #funcion 3
Impresion()                                     #función 4
Cuadrado(5,5)                                   #función 5
Triangulo(4)                                    #función 6
Arreglo()                                       #función 7
NumerosRandom()                                 #función 8
TextoRojo()                                     #función 9    http://es.tldp.org/COMO-INSFLUG/COMOs/Bash-Prompt-Como/Bash-Prompt-Como-5.html
TextoCyan()                                     #función 10
Separar(input("Introduce algo: "))              #función 11
MostrarIdArregloRand()                          #función 12
CrearStringPorArreglo()                         #función 13
CuadradoAColor()                                #función 14
TrianguloAColor()                               #función 15
NumeroA50(int(input("Introduce un número:  "))) #función 16
GruposYExamenes()                               #función 17
print(FindFibonacci(int(input("Cantidad de Números:  ")))) #función 18
Dados()                                         #Función 19
CirculoTortuga()                                #función 20
