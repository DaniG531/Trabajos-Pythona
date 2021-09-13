def CrearMatriz(a,b):
    Matriz = []
    Col = a
    Lin = b
    print("")
    for i in range(1,Col+1):
        columnas = []
        for e in range(1,Lin+1):
            columnas.append(int(input("Introduce un dato.")))
        Matriz.append(columnas)

    for row in Matriz:
        print(row)
    print("")
    print("")
    return Matriz

Continue = "si"
while Continue == "si" or Continue == "Si" or Continue == "SI" or Continue == "S":
    matriz1 = CrearMatriz(int(input("¿De Cuántas Columnas la Matríz?:  ")),int(input("¿De Cuántas Lineas la Matríz?:  ")))
    
    matriz2 = CrearMatriz(int(input("¿De Cuántas Columnas la Matríz?:  ")),int(input("¿De Cuántas Lineas la Matríz?:  ")))

    print("")

    
    Continue = input("Continuar?")
    
