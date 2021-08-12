import random
carta1 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
carta2 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
carta3 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
carta4 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
carta5 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])

print("Carta1 = " + carta1)
print("Carta2 = " + carta2)
print("Carta3 = " + carta3)
print("Carta4 = " + carta4)
print("Carta5 = " + carta5)

Devolver = input("Devolver alguna de las cartas? (Si/No): ")
while Devolver == "Si" or "si":
    CartaDeVuelta = str(input("¿Cuál Carta?   *Ej: carta2. :"))
    if CartaDeVuelta == "carta1" or "1":
        carta1 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
        print("Carta1 = " + carta1)
        Devolver = input("Devolver alguna de las cartas? (Si/No): ")
    elif CartaDeVuelta == "carta2" or "2":
        carta2 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
        print("Carta2 = " + carta2)
        Devolver = input("Devolver alguna de las cartas? (Si/No): ")
    elif CartaDeVuelta == "carta3" or "3":
        carta3 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
        print("Carta3 = " + carta3)
        Devolver = input("Devolver alguna de las cartas? (Si/No): ")
    elif CartaDeVuelta == "carta4" or "4":
        carta4 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
        print("Carta4 = " + carta4)
        Devolver = input("Devolver alguna de las cartas? (Si/No): ")
    elif CartaDeVuelta == "carta5" or "5":
        carta5 = str(random.randint(1, 13)) + (" de ") + random.choice(['Corazones', 'Diamantes', 'Treboles', 'Espadas'])
        print("Carta5 = " + carta5)
        Devolver = input("Devolver alguna de las cartas? (Si/No): ")
        if Devolver != "Si" or "si"

print("Carta1 = " + carta1)
print("Carta2 = " + carta2)
print("Carta3 = " + carta3)
print("Carta4 = " + carta4)
print("Carta5 = " + carta5)