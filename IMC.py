peso = int(input("Ingresa el Peso: "))
altura = float(input("Ingresa la Altura: "))
print("")
imc = peso/altura**2

if imc<18:
    print("Peso Bajo")
elif 18.5 < imc <24.9:
    print("Peso Normal")
elif 25 < imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")

Pesoideal = altura**2*23
print("")
print(f"tu peso ideal es: {Pesoideal} kg.")
print(f"Ocupas bajar: {peso-Pesoideal} kg.")
print("Tu IMC es:")
print(imc)
# UwU
