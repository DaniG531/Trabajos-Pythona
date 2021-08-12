Arreglo = ["Manzana", "Pera"]
print(Arreglo)

def Addelement(valor, matriz):
    matriz += [valor]

def Lista(nuevoobj, matriz):
    for buscardor in matriz:
        if nuevoobj == buscardor:
            return "El Objeto ya está en la lista."
    Addelement(nuevoobj, matriz)
    return "El Objeto se agregó la lista."
print("")

Condicion = input("¿Deseas Incluir otro objeto?  ")
while Condicion == ("Si"):
    print("")
    object = input("Agrega un objeto a la lista: ")
    print("")
    print(Lista(object, Arreglo))
    print("")
    Condicion = input("¿Deseas Incluir otro objeto?  ")

print("")
print(Arreglo)

