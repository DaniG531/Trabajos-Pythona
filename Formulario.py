Formulario = []

def CrearPersona():
    Persona = {"Nombre" : input("Escribe el Nombre: "), "Edad" : int(input("Escribe la Edad: ")), "CURP" : input("Escribe la CURP: "), "Vacunado" : input("¿Ya se vacunó? ")=="Si"}
    return Persona


Continue = "si"
while Continue == "si" or Continue == "Si" or Continue == "SI" or Continue == "S":
    Formulario.append(CrearPersona())

    print("")
    print(Formulario)
    print("")

    Continue = input("Continuar?")
    print("")

def VacunadosFuncion():
    CantidadVacunados = 0
    for ciclo in Formulario:
        if ciclo['Vacunado']:
            CantidadVacunados += 1
    return CantidadVacunados
CantVacun = VacunadosFuncion

print(f"Cantidad de Personas: {len(Formulario)}")
print(f"Cantidad de Vacunados: {CantVacun}")
print("")
print(f"Porcentaje de Vacunados: {CantVacun/len(Formulario)*100}")

#UwU