AlturaTriangulo = int(input("Tamaño del Triangulo: "))

for i in range(1, AlturaTriangulo+1):
    print("*"*i) #Solo en Python
print(" ")

a = int(input("Altura: "))
b = int(input("Base: "))
v = 0

print(" ")

for j in range(0,a):
    print("*"*b) #Solo en Python

print(" ")

while v < a:
    if v == 0 or v == a - 1:
        for h in range(b):
            print("*", end=" ")
    else:
        for l in range(1, b):
            if l == 1:
                print("*", end=" ")
            print(" ", end=" ")
            if l == b - 2:
                print("*", end=" ")
    print("")
    v += 1