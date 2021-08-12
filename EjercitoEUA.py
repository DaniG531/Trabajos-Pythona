Edad = int(input("Ingresa La Edad:  "))
if Edad >= 17 and Edad <= 35:
    print("Edad Valida.")
elif Edad > 35:
    print("Solicitud Rechazada. Edad mayor a la permitida.")
    exit(0)
else:
    print("Solicitud Rechazada. Edad mínima no alcanzada.")
    exit(0)


Diploma = input("¿Tiene diploma de preparatória? (S/N):  ")
if Diploma == "S" or Diploma == "Si" or Diploma == "SI" or Diploma == "si":
    print("Aceptado.")
elif Diploma == "N" or Diploma == "No" or Diploma == "NO" or Diploma == "no":
    print("Solicitud Rechazada. Es necesario el certificado de preparatoria terminada.")
    exit(0)
else:
    print("Datos erroneos.")
    exit(0)

Residencia = input("¿Es residente estadounidense o extrangero con residencia permanente? (S/N):  ")
if Residencia == "S" or Residencia == "Si" or Residencia == "SI" or Residencia == "si":
    print("Aceptado.")
elif Residencia == "N" or Residencia == "No" or Residencia == "NO" or Residencia == "no":
    print("Solicitud Rechazada. Es necesario ser residente Estadounidense.")
    exit(0)
else:
    print("Datos erroneos.")
    exit(0)

Salud = input("¿La persona se encuentra dentro de los parámetros de salúd necesarios de acuerdo al examen de salud? (S/N):  ")
if Salud == "S" or Salud == "Si" or Salud == "SI" or Salud == "si":
    print("Aceptado.")
elif Salud == "N" or Salud == "No" or Salud == "NO" or Salud == "no":
    print("Solicitud Rechazada. Es necesario cumplir los parámetros de salud.")
    exit(0)
else:
    print("Datos erroneos.")
    exit(0)
   
Altura = float(input("Ingresa la Altura en metros:  "))
if Altura >= 1.52:
    print("Altura Valida.")
else:
    print("Solicitud Rechazada. Altura mínima no alcanzada.")
    exit(0)

IQ = int(input("Ingresa el Coeficiente Intelectual de la persona:  "))
if IQ >= 80:
    print("Coeficiente Intelectual Valido.")
else:
    print("Solicitud Rechazada. Coeficiente Intelectual mínimo no alcanzado.")
    exit(0)

print("Solicitud Aceptada.")
exit(0)