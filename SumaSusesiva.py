def SumaSusesiva(A,B):
    Numeros = 0
    for i in range(A,B+1):
        Numeros = (Numeros + i)
    print(f"La respuesta es = {Numeros}")

SumaSusesiva(int(input("Primer Número:  ")),int(input("Segundo Número: ")))

