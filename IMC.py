peso = int(input("Ingresa el Peso"))
altura = float(input("Ingresa la Altura"))

imc = peso/altura**2

if imc<18:
    print("Peso Bajo")
elif 18.5 < imc <24.9:
    print("Peso Normal")
elif 25 < imc < 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")

print("Tu IMC es:")
print(imc)
