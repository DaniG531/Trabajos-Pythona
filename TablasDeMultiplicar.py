PrimerNumero = int(input("Cantidad de Tablas: "))
SegundoNumero = int(input("Hasta donde las Tablas: "))


for i in range(0, PrimerNumero+1):
    for j in range(0, SegundoNumero+1):
        print( str(i) + "*" + str(j) + "=" + str(i*j) )
    print(" ")