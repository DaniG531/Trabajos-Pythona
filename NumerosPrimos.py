def FindPrimos(primero, ultimo):
    Primos = []

    if primero < 2:
        primero = 2
    
    for n in range(primero, ultimo+1):
        Odd = True
        for i in range(2, n):
            if n % i == 0:
                Odd = False
                break
        if Odd:
            Primos.append(n)
    return Primos

x = int(input("Define el Primer Número del Rango: "))
y = int(input("Define el Ultimo Número del Rango: "))

print(FindPrimos(x, y))