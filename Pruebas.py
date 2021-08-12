numeros = [4,5,6,7]
numeros2 = [4,6,9]
def identificador(numeroparabuscar,matriz):
    for elem in matriz:
        if numeroparabuscar==elem:
            return True
    return False
x = int(input("Introduce el numero a buscar: "))
print(identificador(x,numeros))
print(identificador(x,numeros2))